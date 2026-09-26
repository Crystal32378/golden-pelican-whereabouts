#!/usr/bin/env python3
"""GMI Cloud（Hy Image v3.5 preview）批次生海報。

前置：echo -n 'YOUR_KEY' > ~/.gmi_key
用法：python3 tools/gen_posters.py A        # 生一版
      python3 tools/gen_posters.py all      # 六版全生
輸出：~/Desktop/hermes/out/<版>.png

流程（依官方文件 console.gmicloud.ai/api/v1/ie/requestqueue/apikey）：
  1. 查模型參數 → 決定 size 欄位該用哪個值（3:4 / 4:3 / 1:1 / 9:16 / 16:9）
  2. 上傳參考圖 → 拿 public_url（最多 5 張，這裡用 1 張最清楚）
  3. POST /requests 提交 → 拿 request_id
  4. 輪詢 GET /requests/{id} → outcome.image_url
  5. 下載存檔
"""
import base64, json, os, re, sys, time, urllib.request, urllib.error
from pathlib import Path

HOME = Path.home()
KEY_FILE = HOME / ".gmi_key"
OUT = HOME / "Desktop" / "hermes" / "out"
REFS = HOME / "Desktop" / "hermes" / "refs"
PROMPTS_MD = Path(__file__).resolve().parent.parent / "docs" / "posters" / "prompts.md"
BASE = "https://console.gmicloud.ai/api/v1/ie/requestqueue/apikey"
MODEL = "hy-image-v3.5-preview"
RATIO = {"A": "4:3", "B": "4:3", "C": "4:3", "D": "4:3", "E": "4:3", "F": "4:3"}


def key():
    if not KEY_FILE.exists():
        sys.exit(f"找不到 {KEY_FILE}：請先執行 echo -n 'YOUR_KEY' > ~/.gmi_key")
    k = KEY_FILE.read_text().strip().strip("'\"")
    if not k:
        sys.exit("~/.gmi_key 是空的")
    return k


def _curl(args, data=None, raw_out=False, timeout=120):
    """全部走 curl：python.org 的 Python 3.13 在這台 Mac 上抓不到系統根憑證，curl 可以。"""
    import subprocess, tempfile
    cmd = ["curl", "-sS", "--max-time", str(timeout),
           "-H", f"Authorization: Bearer {key()}"]
    if data is not None:
        cmd += ["-H", "Content-Type: application/json", "-X", "POST", "-d", json.dumps(data)]
    cmd += args
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError(f"curl 失敗：{out.stderr.strip()[:200]}")
    txt = out.stdout
    if raw_out:
        return txt
    return json.loads(txt)


def api(path, data=None, method=None, timeout=60, raw=False):
    url = path if path.startswith("http") else BASE + path
    if raw:
        return _curl([url], raw_out=True, timeout=timeout)
    if data is not None:
        return _curl([url], data=data, timeout=timeout)
    return _curl([url], timeout=timeout)


def put(url, path, ctype="image/png", timeout=120):
    import subprocess
    r = subprocess.run(["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", "-X", "PUT",
                        "-H", f"Content-Type: {ctype}", "--data-binary", f"@{path}", url],
                       capture_output=True, text=True, timeout=timeout)
    return r.stdout.strip()


def download(url, path, timeout=120):
    import subprocess
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(["curl", "-sSL", "-o", str(path), url], capture_output=True, text=True, timeout=timeout)
    return Path(path)


def pick_size(ratio):
    """從模型 schema 裡挑最接近的合法 size 值。"""
    try:
        sch = api(f"/models/{MODEL}")
        for p in sch.get("parameters", []):
            if p.get("name") == "size":
                vals = p.get("enum") or p.get("options") or p.get("values") or []
                flat = []
                for v in vals:
                    flat.append(v if isinstance(v, str) else (v.get("value") if isinstance(v, dict) else str(v)))
                want = {"4:3": "4:3", "3:4": "3:4", "1:1": "1:1", "9:16": "9:16", "16:9": "16:9"}[ratio]
                exact = [v for v in flat if v == want]
                px = [v for v in flat if re.fullmatch(r"\d{3,5}x\d{3,5}", str(v))]
                target = (4, 3) if ratio == "4:3" else (3, 4) if ratio == "3:4" else (1, 1) if ratio == "1:1" else (9, 16) if ratio == "9:16" else (16, 9)
                scored = []
                for v in px:
                    w, h = (int(x) for x in v.split("x"))
                    scored.append((abs((w / h) - (target[0] / target[1])), v))
                if exact:
                    return exact[0], flat
                if scored:
                    scored.sort()
                    return scored[0][1], flat
                if flat:
                    return flat[0], flat
    except Exception as e:
        print("  (拿不到 size schema，改用比例字串)", e)
    return ratio, []


def upload_refs(max_n=1):
    if not REFS.exists():
        return []
    files = sorted([p for p in REFS.iterdir() if p.suffix.lower() in (".png", ".jpg", ".jpeg")])[:max_n]
    urls = []
    for f in files:
        r = api("/upload-url", {"file_type": f.suffix.lstrip(".").lower()})
        put(r["upload_url"], f, "image/png" if f.suffix.lower() == ".png" else "image/jpeg")
        urls.append(r["public_url"])
        print(f"  ↑ 已上傳參考圖 {f.name}")
    return urls


def parse_prompts():
    text = PROMPTS_MD.read_text()
    out = {}
    for m in re.finditer(r"^## ([A-I])｜(.+?)$(.*?)(?=^## |\Z)", text, re.S | re.M):
        code = re.search(r"```(.*?)```", m.group(3), re.S)
        if code:
            out[m.group(1)] = (m.group(2).strip(), code.group(1).strip())
    return out


def generate(letter, title, prompt, ratio, refs):
    size, avail = pick_size(ratio)
    if avail and letter == "A":
        print(f"  size 合法值：{avail[:12]}")
    inner = {"prompt": prompt}
    if size:
        inner["size"] = size
    if refs:
        inner["image"] = refs
    job = api("/requests", {"model": MODEL, "payload": inner})
    rid = job.get("request_id") or job.get("id")
    print(f"  → 提交完成 request_id={rid} status={job.get('status')}")
    for i in range(180):
        time.sleep(4)
        st = api(f"/requests/{rid}")
        s = (st.get("status") or "").lower()
        if s in ("success", "succeeded", "completed"):
            outcome = st.get("outcome") or {}
            media = outcome.get("media_urls") or []
            url = outcome.get("image_url") or outcome.get("image_urls", [None])[0] or outcome.get("url")
            if not url and media:
                first = media[0]
                url = first.get("url") if isinstance(first, dict) else first
            if not url:
                print("  ⚠️ 成功但沒拿到圖片 url：", json.dumps(outcome)[:300]); return None
            OUT.mkdir(parents=True, exist_ok=True)
            path = OUT / f"{letter}.png"
            return download(url, path)
        if s in ("failed", "error", "cancelled"):
            print("  ✗ 失敗：", json.dumps(st)[:400]); return None
    print("  ⏱ 超時"); return None


def main():
    which = sys.argv[1:] or ["A"]
    variants = parse_prompts()
    if which == ["all"]:
        which = list(variants.keys())
    refs = upload_refs(1)
    print(f"輸出到 {OUT}；參考圖 {len(refs)} 張")
    for letter in which:
        if letter not in variants:
            print(f"跳過：{letter}"); continue
        title, prompt = variants[letter]
        print(f"\n[{letter}] {title}（{RATIO.get(letter,'4:3')}）")
        p = generate(letter, title, prompt, RATIO.get(letter, "4:3"), refs)
        if p:
            print(f"  ✅ {p}  ({p.stat().st_size//1024} KB)")
        time.sleep(1)


if __name__ == "__main__":
    main()
