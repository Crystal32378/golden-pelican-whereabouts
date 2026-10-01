#!/usr/bin/env python3
"""黃金鵜鶘 品牌識別系統 —— 標誌鎖定產生器

為什麼是腳本而不是手寫 SVG：
  spec.md 的 (c) 條說「擴散模型的本質是每次都重新發明」，而 6 張圖裡的圓徽鳥的姿勢
  和輪子的構圖都不一樣。手寫 SVG 只是把一次性的發明固定下來；參數化產生器固定的
  是「幾何規則」—— 改一個參數，圖、單色版、反白版、最小尺寸測試同時重生。

用法：
    python3 build_marks.py                 # 產生全部 SVG
    python3 build_marks.py --preview       # 另產生驗收頁 preview.html

色票（spec.md 第二節）：紙白 #F4F1EA · 近黑 #2B2D33 · 印章紅 #B8322A
硬規則：最小尺寸 8mm；單色必須成立；反白必須成立；留白 = 一個「車輪直徑」。
"""
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------- 色票
PAPER = "#F4F1EA"   # 紙白
INK = "#2B2D33"     # 近黑
RED = "#B8322A"     # 印章紅

# ---------------------------------------------------------------- 幾何參數
# 座標在 S×S 的 viewBox 內，外圓剛好貼齊 viewBox 邊緣。
S = 240.0
C = S / 2

RING_OUTER = 118.0           # 外圓半徑
RING_W = 9.0                 # 圓環線寬
DISC_R = RING_OUTER - RING_W # 實心碟半徑 = 109

# 單車輪（側面）
WHEEL_CX, WHEEL_CY = C, 152.0
WHEEL_RIM_R = 58.0
WHEEL_RIM_W = 9.0
HUB_R = 8.5
SPOKES = 10
SPOKE_W = 5.0

PERCH_Y = WHEEL_CY - WHEEL_RIM_R   # 鵜鶘站立點 = 輪圈正上方 = 94


def spokes_path():
    """輪輻：從軸心放射到輪圈內緣，SPOKES 條整齊分布。"""
    r_in = HUB_R + 1.0
    r_out = WHEEL_RIM_R - WHEEL_RIM_W / 2 - 1.0
    d = []
    for i in range(SPOKES):
        a = math.radians(i * (360.0 / SPOKES) + 18.0)
        x0 = WHEEL_CX + r_in * math.cos(a)
        y0 = WHEEL_CY + r_in * math.sin(a)
        x1 = WHEEL_CX + r_out * math.cos(a)
        y1 = WHEEL_CY + r_out * math.sin(a)
        d.append(f"M{x0:.2f} {y0:.2f}L{x1:.2f} {y1:.2f}")
    return "".join(d)


# 鵜鶘側影（朝右），站在輪圈上。
#
# ⚠️ 這是**手調**的貝茲曲線，不是描圖來的。
# 曾用 `trace_pelican.py` 從 `BR-01.png` 自動抓輪廓（門檻化 → 連通元件 → 輪圈圓
# 擬合 → Moore 邊界追蹤 → Douglas–Peucker），確實抓到乾淨的剪影，但整隻一團、
# 沒有喉囊、腳那邊有斷口，最小尺寸直接崩掉，於是**放棄**。腳本保留作為紀錄。
#
# 這條 path 的演化（v2 喉囊明確、v3 身體飽滿的版本試過，**都已丟掉**）。
#
# **定案是這個 v1。**（2026-09-29 Crystal）
# 理由：v1 沒有喉囊、嘴是尖刺 —— 這不是缺點。讀成「鵜鶘」還是讀成「一隻長腳鳥站在
# 輪子上」，後者更耐看也更誠實；線條更少，小尺寸更乾淨（珐瑯徽章、貼紙受益最大）。
# 記號本來就不需要寫實。別再改回寫實版，除非有人要求「看得出是鵜鶘」的大尺寸場合。
PELICAN = (
    "M86 88"                                # 尾端
    "C90 80 94 71 97 63"                    # 背線上升
    "C100 55 105 50 112 47"                 # 肩 → 頸根
    "C116 40 122 35 130 33"                 # 頸背上行
    "C137 31 143 34 147 39"                 # 頭頂 → 額
    "L199 49"                               # 上喙：一筆到底的尖刺，線條最少
    "C202 50 202 53 199 54"                 # 喙尖
    "L152 61"                               # 下喙回來
    "C150 69 143 76 135 79"                 # 胸頸
    "C131 84 130 88 130 91"                 # 胸線下到腳
    "L137 94L127 94L126 88L119 88L117 94L107 94L109 87"   # 雙腳
    "C100 91 91 92 86 88Z"                  # 腹線回尾
)


def mark(fill=RED, knock=PAPER, ring=True):
    """Primary mark：實心圓徽 + 挖空的輪與鵜鶘。

    fill  = 碟面顏色
    knock = 挖空顏色（單色版與反白版靠它切出負形）
    """
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {S:g} {S:g}" width="{S:g}" height="{S:g}" '
        'role="img" aria-label="The Golden Pelican mark">',
        "<title>The Golden Pelican — primary mark</title>",
        # 圖形層，不含任何文字（spec.md (b) 條，2026-09-29 決定）
        f'<circle cx="{C:g}" cy="{C:g}" r="{DISC_R:g}" fill="{fill}"/>',
        f'<g fill="none" stroke="{knock}" stroke-linecap="round">',
        f'<circle cx="{WHEEL_CX:g}" cy="{WHEEL_CY:g}" r="{WHEEL_RIM_R:g}" '
        f'stroke-width="{WHEEL_RIM_W:g}"/>',
        f'<path d="{spokes_path()}" stroke-width="{SPOKE_W:g}"/>',
        f'<circle cx="{WHEEL_CX:g}" cy="{WHEEL_CY:g}" r="{HUB_R:g}" '
        f'fill="{knock}" stroke="none"/>',
        f'<path d="{PELICAN}" fill="{knock}" stroke="none" '
        'stroke-linejoin="round"/>',
        "</g>",
    ]
    if ring:
        parts.append(
            f'<circle cx="{C:g}" cy="{C:g}" r="{RING_OUTER - RING_W / 2:g}" '
            f'fill="none" stroke="{fill}" stroke-width="{RING_W:g}"/>'
        )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


FILES = {
    "mark-primary.svg": lambda: mark(RED, PAPER),
    "mark-primary-1colour.svg": lambda: mark(INK, PAPER),
    "mark-primary-reversed.svg": lambda: mark(PAPER, RED),
}


def preview_html():
    """最小尺寸與單色版的驗收頁（spec.md 第五節的驗收標準）。"""
    cells = "".join(
        f'<figure><div class="box">{fn()}</div>'
        f"<figcaption>{name}</figcaption></figure>"
        for name, fn in FILES.items()
    )
    sizes = "".join(
        f'<span class="s" style="width:{w}px;height:{w}px">'
        f'<img src="mark-primary.svg" width="{w}" height="{w}"></span>'
        for w in (24, 32, 48, 72, 120)
    )
    return f"""<!doctype html>
<meta charset="utf-8">
<title>Golden Pelican — mark lock</title>
<style>
 body {{ background:{PAPER}; color:{INK};
        font:12px/1.7 ui-monospace,Menlo,monospace; margin:0; padding:32px; }}
 h1,h2 {{ font-size:12px; letter-spacing:.14em; text-transform:uppercase; }}
 h2 {{ color:#6b6f78; margin-top:40px; border-top:1px solid #d8cfb4;
       padding-top:12px; }}
 .grid {{ display:flex; flex-wrap:wrap; gap:24px; margin-top:16px; }}
 figure {{ margin:0; }}
 .box {{ background:#fff; border:1px solid #d8cfb4; padding:14px;
         display:flex; align-items:center; justify-content:center; }}
 figcaption {{ margin-top:6px; color:#6b6f78; }}
 .sizes {{ display:flex; align-items:flex-end; gap:28px; margin-top:16px; }}
 .s {{ background:#fff; border:1px solid #d8cfb4; display:flex;
       align-items:center; justify-content:center; }}
 .dark {{ background:{INK}; }}
</style>
<h1>The Golden Pelican — mark lock</h1>
<p>圖形層，不含任何文字。最小尺寸 8 mm。單色版與反白版必須成立。</p>
<h2>Layers</h2>
<div class="grid">{cells}</div>
<h2>Minimum size — 24 / 32 / 48 / 72 / 120 px</h2>
<div class="sizes">{sizes}</div>
<h2>On dark</h2>
<div class="grid"><div class="box dark">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="120"
     height="120"><circle cx="120" cy="120" r="109" fill="{PAPER}"/>
<g fill="none" stroke="{RED}" stroke-linecap="round">
<circle cx="120" cy="152" r="58" stroke-width="9"/>
<path d="{spokes_path()}" stroke-width="5"/>
<circle cx="120" cy="152" r="8.5" fill="{RED}" stroke="none"/>
<path d="{PELICAN}" fill="{RED}" stroke="none" stroke-linejoin="round"/>
</g>
<circle cx="120" cy="120" r="113.5" fill="none" stroke="{PAPER}"
        stroke-width="9"/></svg>
</div></div>
"""


if __name__ == "__main__":
    import sys

    for name, fn in FILES.items():
        (HERE / name).write_text(fn(), encoding="utf-8")
        print("wrote", name)
    if "--preview" in sys.argv:
        (HERE / "preview.html").write_text(preview_html(), encoding="utf-8")
        print("wrote preview.html")
