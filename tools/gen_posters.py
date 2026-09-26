#!/usr/bin/env python3
"""用 GMI Cloud（Hy Image 3.5 preview）批次生海報。

用法：
  1) 把 API key 存成一行文字：  echo -n 'YOUR_KEY' > ~/.gmi_key
  2) 執行：  python3 tools/gen_posters.py            # 只生 A 版
              python3 tools/gen_posters.py A B F      # 生指定的版本
              python3 tools/gen_posters.py all        # 全部六版

輸出：~/Desktop/hermes/out/<版>.png
參考圖：~/Desktop/hermes/refs/1-moon-頭盔與國旗.png（可換）

設計note：GMI 的 image endpoint 在 console 的 model card 裡，這支腳本會依序
嘗試幾種常見的 OpenAI 相容路徑與模型名，成功就記下來，之後沿用。
"""
import base64, json, os, re, sys, time, urllib.request, urllib.error
from pathlib import Path

HOME = Path.home()
KEY_FILE = HOME / ".gmi_key"
OUT = HOME / "Desktop" / "hermes" / "out"
REFS = HOME / "Desktop" / "hermes" / "refs"
PROMPTS_MD = Path(__file__).resolve().parent.parent / "docs" / "posters" / "prompts.md"

# Hy Image 只有三個比例；哪一版用哪個
RATIO = {"A": "4:3", "B": "4:3", "C": "4:3", "D": "4:3", "E": "4:3", "F": "4:3"}
SIZES = {"4:3": "1440x1080", "1:1": "1024x1024", "9:16": "1080x1920", "16:9": "1920x1080"}

CANDIDATE_BASES = [
    "https://api.gmicloud.ai/v1",
    "https://api.gmicloud.ai/api/v1",
    "https://inference.gmicloud.ai/v1",
]
CANDIDATE_MODELS = ["hy-image-3.5-preview", "hy-image-3.5", "hunyuan-image-3.5", "hy-image"]


def key():
    if not KEY_FILE.exists():
        sys.exit(f"找不到 {KEY_FILE}。請先執行： echo -n 'YOUR_KEY' > ~/.gmi_key")
    return KEY_FILE.read_text().strip()


def parse_prompts():
    """從 prompts.md 抽出每個版本的 prompt（第一個 ``` 區塊）。"""
    text = PROMPTS_MD.read_text()
    out = {}
    for m in re.finditer(r"^## ([A-F])｜(.+?)$(.*?)(?=^## |\Z)", text, re.S | re.M):
        letter, title, body = m.group(1), m.group(2), m.group(3)
        code = re.search(r"```(.*?)```", body, re.S)
        if code:
            out[letter] = (title.strip(), code.group(1).strip())
    return out


def ref_images(max_n=1):
    if not REFS.exists():
        return []
    files = sorted([p for p in REFS.iterdir() if p.suffix.lower() in (".png", ".jpg", ".jpeg")])[:max_n]
    return [("data:image/png;base64," + base64.b64encode(f.read_bytes()).decode()) for f in files]


def call(base, model, prompt, ratio, refs, timeout=180):
    size = SIZES.get(ratio, "1440x1080")
    payload = {"model": model, "prompt": prompt, "n": 1, "size": size}
    if refs:
        payload["image"] = refs if len(refs) > 1 else refs[0]
    req = urllib.request.Request(
        base + "/images/generations",
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {key()}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def save(data_json, path):
    OUT.mkdir(parents=True, exist_ok=True)
    item = data_json["data"][0]
    if item.get("b64_json"):
        path.write_bytes(base64.b64decode(item["b64_json"]))
    else:
        urllib.request.urlretrieve(item["url"], path)
    return path


def main():
    which = sys.argv[1:] or ["A"]
    if which == ["all"]:
        which = list(parse_prompts().keys())
    variants = parse_prompts()
    if not variants:
        sys.exit(f"從 {PROMPTS_MD} 解析不到 prompt")
    refs = ref_images()
    print(f"參考圖：{len(refs)} 張；輸出到 {OUT}")
    for letter in which:
        if letter not in variants:
            print(f"跳過不存在的版本：{letter}"); continue
        title, prompt = variants[letter]
        ratio = RATIO.get(letter, "4:3")
        ok = False
        for base in CANDIDATE_BASES:
            for model in CANDIDATE_MODELS:
                try:
                    print(f"[{letter}] {title} → {base} / {model} ({ratio})")
                    res = call(base, model, prompt, ratio, refs)
                    p = save(res, OUT / f"{letter}.png")
                    print(f"  ✅ {p}")
                    ok = True
                    break
                except urllib.error.HTTPError as e:
                    detail = e.read().decode(errors="replace")[:200]
                    print(f"  ✗ {e.code} {detail}")
                except Exception as e:
                    print(f"  ✗ {type(e).__name__}: {e}")
            if ok: break
        if not ok:
            print(f"[{letter}] 全部端點都失敗——請到 console 看 model card 的實際 endpoint / 模型名")
        time.sleep(2)


if __name__ == "__main__":
    main()
