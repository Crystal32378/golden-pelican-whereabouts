# 場景概念插畫（scene concept）

給 `game/` 用的無文字場景圖。**全部不帶任何文字**——這個模型畫字會糊成亂碼
（實測：MK-25 旁邊四個手寫字直接Blur 掉），所以 UI 交給 HTML，這裡只管畫面。

## 前置：參考圖順序是綁死的

`tools/gen_posters.py` 的 `upload_refs()` 只抓 `refs/` 排序後**第一張 png**。
目前順序：`0-ref-full.png`（全身三視圖）→ `1-ref-pelican.png`（只有頭部）→ `2-ref-bike.png`。

**改任何 refs/ 檔名都可能讓整組圖風格漂掉。** 尤其不要讓 `1-ref-pelican.png`
排到第一——只有頭部的參考圖會讓生出來的鵜鶘變成一顆浮著的頭。

## 共通尾巴（每張都重複寫，不要用變數）

## SC-01｜遊戲主畫面 · 24 秒計時開始前

橫式 16:9。這是首頁／遊戲開始那一格的氛圍圖：鵜鶘從某個地方探頭，
格子還沒蓋章，時間還沒跑。

```
A wide horizontal game title scene, a tall long-legged pelican standing
right of centre on a warm pale beige open ground, its off-white body built from
angular folded paper facets, a long flat orange beak with a small red tip, one
black dot eye, wearing a small knitted grey hat. It stands completely motionless,
upright, facing right, a long red road bicycle with thin black spoked wheels
leaning against its leg.

Around it, a loose grid of many empty square holes pressed into the ground,
each a shallow square recess with a soft inner shadow, all of them empty and
unmarked. Far in the background a few very simple low-poly shapes suggest a
distant shoreline and a single tall post, small and out of focus.

Mood: quiet, still, unhurried, the moment before a timer starts. Low sun,
long soft shadows, warm cream and dusty red tones. Generous empty space on the
left side of the frame.

Style: flat vector-like low-poly paper-cutout, crisp visible polygon facets, flat
shading, limited palette of off-white, warm beige, orange, red and black. Warm
pale background, no text, no letters, no numbers, no watermark, no logo, no
user interface, no buttons, no panels.
```

## SC-02｜站點 · 登月（太空頭盔＋氣瓶）

橫式 16:9。GEAR 站 6。代表「特殊裝備」那一類怎麼畫。

```
A wide horizontal scene on a flat grey-white lunar plain under a black sky. A
tall long-legged pelican stands upright in right-facing profile, its off-white
body built from angular folded paper facets, wearing a round white space helmet
with a circular glass faceplate and a small red tip on its long orange beak. A
short metal oxygen tank is strapped to its back with a thin strap. Its two thin
dark legs are slightly apart, standing still.

A red road bicycle with thin black spoked wheels rests beside it on the ground,
held upright by a small stand. Low-poly faceted boulders of various sizes
scatter across the middle distance, and a tiny footpad sits far away near the
horizon, small and simple.

Mood: still, procedural, unexcited about being on the moon. Hard even light,
sharp faceted shadows, palette of grey, off-white, orange and one strong red.

Style: flat vector-like low-poly paper-cutout, crisp visible polygon facets, flat
shading, limited palette of off-white, warm beige, orange, red and black. Warm
pale background, no text, no letters, no numbers, no watermark, no logo, no
user interface, no buttons, no panels.
```

## SC-03｜站點 · 深海（氧氣面罩＋全罩頭盔）

橫式 16:9。GEAR 站 11。同一隻鳥換一個環境，驗證風格能不能跨場景穩住。

```
A wide horizontal underwater scene, a tall long-legged pelican standing upright
in right-facing profile on a flat pale sandy seabed. Its off-white body is built
from angular folded paper facets. It wears a full-head diving helmet of clear
glass over a dark oxygen mask, and a small air hose curves from the mask down
toward its back. Its long flat orange beak protrudes through the front of the
helmet, tipped in red. It stands completely motionless with both thin dark legs
planted.

A red road bicycle with thin black spoked wheels lies on its side on the sand
beside the pelican, half sunk, one wheel still turning slightly and trailing a
small puff of sand. Flat-topped faceted coral shapes in muted red and orange
stand in the middle distance, and shafts of pale light fall from above.

Mood: calm, slightly absurd, entirely unbothered by the pressure. Cool but still
warm-tinted light, palette of pale sand, off-white, orange and red.

Style: flat vector-like low-poly paper-cutout, crisp visible polygon facets, flat
shading, limited palette of off-white, warm beige, orange, red and black. Warm
pale background, no text, no letters, no numbers, no watermark, no logo, no
user interface, no buttons, no panels.
```


Style: flat vector-like low-poly paper-cutout, crisp visible polygon facets,
flat shading, limited palette of off-white, warm beige, orange, red and black.
Warm pale background, no text, no letters, no numbers, no watermark, no logo,
no user interface, no buttons, no panels.