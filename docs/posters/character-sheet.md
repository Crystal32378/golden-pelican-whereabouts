# 鵜鶘角色設定表（character sheet）

給 `game/` 用的角色設定圖。**目標是一張圖同時定死三件事**：
之後不管畫什麼，餵這張當參考圖，風格就不會漂。

## 參考圖

`refs/4-island.png`（由 `postcards/island.png` 複製而來）
→ 低多邊形紙剪風格、灰白身體、橘色長喙、紅色單車、頭戴毛帽。
**生任何東西之前先確認這張還在 `refs/` 的第一位**，因為腳本只抓排序後的第一張。

## 為什麼是設定表而不是直接畫遊戲圖

遊戲現在三個地方缺圖：圖鑑的帽子、翻牌卡背、蓋章的鳥頭。
但直接畫這三樣會各自飄走。**設定表是那三樣的共同上游**——
它先定義清楚「這隻鳥長什麼樣」，後面才有東西可以對著畫。

## 尺寸與比例

- **3:4（1152×1536）**。設定表需要塞下多格，橫式會太扁。
- 純色淺底（米白 #F4F1EA 系），不要場景、不要陰影氣氛——設定表要的是乾淨可讀。

## 硬性規則（沿用 merch.md 的 DNA）

- 每格都要有**鵜鶘或紅色單車**，這是整組的視覺主軸
- **紅色系**是命脈：單車紅、格線紅、編號紅
- **不要水印、不要 logo、不要網址、不要任何網站文字**
- **不要 glossy 3D render、不要塑膠感、不要卡通可愛風**——要低多邊形紙剪
- 文字**全英文**，且只留列出的那些。數字編號要清楚可讀

## 已知的坑（實測）

- Hy Image 3.5 的中文字正確率極低（「鵜鶘」會變成鷦鯨、鵜鸕、鵜鶬）
  → **這張表全部走英文**，不放任何中文
- 純英文幾乎不出錯，數字也穩
- 不要叫模型「畫得素一點」，質感要靠物理痕跡帶出來

---

## CS-01｜角色設定表

```
A character model sheet on a flat warm off-white background, low-poly faceted
paper-cutout illustration style, flat shading with visible polygon facets. On a
plain pale beige ground, arranged in a neat grid with thin red dividing lines
and small red printed numbers.

Top row, three views of the same character: a tall long-legged pelican, off-white
body made of angular folded paper facets, a long flat orange beak with a small
red tip, black dot eye, standing upright. Left view is facing right in full
profile, centre view is facing forward, right view is from behind. Each figure
wears a small knitted grey hat.

Middle row, the bicycle in three views: a red road bicycle with thin black
tyres, black spoked wheels, drop handlebars and a brown leather saddle, drawn
side-on, from the front, and at a three-quarter angle. Simple, clean, no rider.

Bottom row, four smaller head-and-shoulder studies of the pelican's head only,
each wearing a different small hat: a knitted beanie, a flat cap, a straw sun
hat, a plain bowler hat. The orange beak is identical in all four.

Style: flat vector-like low-poly, crisp facet edges, limited palette of off-white,
orange, red, black, grey and brown. No background scenery, no shadows on the
ground, no text other than the small red numbers and thin red divider lines.
```

---

## 參考圖（帽子表用）

`refs/1-ref-pelican.png` —— 設定表裁下來的**側面頭部**，毛線帽那格。
乾淨、單一主體、不含瑕疵格，比整張設定表更適合當參考圖。
`refs/2-ref-bike.png` 是單車側面，要畫含單車的東西時用。

> 原本的 `refs/1-rabbit.png` 等四張已移入 `refs/_old/`，避免腳本抓錯。
> 腳本只抓排序後的第一張，所以命名時前面的序號才重要。


遊戲圖鑑直接吃這張。**重點是 27 格整齊、風格一致、每格只有頭**。
一張圖生完，遊戲那 27 個 emoji 問號就都能換掉。

### 已知要權衡的

- 27 格在 1152×1536 裡每格只有約 355×355（9×3 排），頭部要畫得夠大才認得出帽子
  → **排 6 欄 × 5 行**（最後一列 3 格），每格約 190×300，頭部更大
- 格子太多會讓模型開始省略。**實測 27 格很可能生不出 27 個**，
  寧可先生成 12 格的樣板確認畫法，再分三批生出 27 頂。
  → 先跑 `CS-02A`（12 格），過關了再 `CS-02b`、`CS-02c` 各 9 格，最後由程式拼成一張

## CS-02A｜帽子圖鑑 · 第一批 12 頂（樣板）

格子順序＝`game/index.html` GEAR 裡的**站號順序**，1–12 對應站 1,2,3,4,5,7,9,10,13,14,15,16。
（6,8,11,12,21,22 是特殊裝備，另有 EQ-01～06，不在這張表裡。）

```
A hat catalogue sheet on a flat warm off-white background, low-poly faceted
paper-cutout illustration style. A neat grid of twelve equal cells divided by
thin red lines, three columns by four rows. Each cell contains the head and
neck of the same long-legged pelican in right-facing profile, drawn
identically every time: off-white angular paper-facet body, long flat orange
beak with a small red tip, one black dot eye, upright neck.

Only the hat changes from cell to cell, in this order:
1 wide woven straw sun hat with a frayed brim
2 plain white athletic sweatband
3 simple grey knitted beanie
4 hard white bicycle helmet with ventilation slots
5 dark brown folded zen monk cap, worn slightly tilted
6 red knitted hat with ear flaps and a bobble
7 leather aviator flying helmet with goggles pushed up on the forehead
8 soft black beret worn at an angle, slightly dented
9 plain brown paper bag pulled down over the head, two cut holes
10 wide-brimmed straw sun hat, brim shading the face
11 dark green flat peaked cap
12 yellow rain hat, beaded with water droplets

Style: flat vector-like low-poly, crisp facet edges, limited palette. The head
is identical in all twelve cells apart from the hat. No background scenery, no
ground shadows, no text, no numbers, no logos.
```

## CS-02b｜帽子圖鑑 · 第二批 9 頂

依 GEAR 站號依序：13 耳機 / 14 玻璃球 / 15 花冠 / 16 救生帽 / 17 漁夫帽 /
18 頭巾 / 19 僧帽（橙色） / 20 耳塞 / 21 歪戴的毛帽。
3×3 格子，格線同樣用紅色，其餘描述沿用 CS-02A 開頭那段，只換帽子清單。

## CS-02c｜補齊

21 站非特殊裝備 = CS-02A 的 12 頂 + CS-02b 的 9 頂，剛好齊全，無需第三批。
6 站特殊裝備由 EQ-01～06 單獨出圖。合計 27 站，與 GEAR 一一對應。

---

## 頭部配備表（10/24 生日版用）

27 站，每站頭上戴**固定**的東西（不是玩家亂抽）。**理由：這是世界觀的設定檔，
不是收集品。** 抽到登月站一定戴太空頭盔，因為牠就是穿那個下來的。

只生「特殊裝備」那幾站，其餘站用 CS-02A 的通用帽子表當預設。

⚠️ 編號對應（10/24 修正，勿再搞錯）：本表的 # 是**站號**（1–27），
對應 `game/index.html` 的 `STOPS[ # - 1 ]` 與 `GEAR[ # - 1 ]`。
GEAR 只有 6 筆特殊裝備（EQ-EQ-01～06），其餘 21 筆走 CS-02A 通用表。

參考圖：`refs/1-ref-pelican.png`（側面頭部，乾淨）

| # | 站 | 頭上戴的 |
|---|---|---|
| 6 | 登月 | 太空頭盔＋氣瓶 |
| 8 | 雨林 | 探險家軟木帽 |
| 11 | 深海 | 氧氣面罩＋全罩頭盔 |
| 12 | 宇宙 | 全罩式太空頭盔（圓球面罩） |
| 21 | 兔子洞 | 頭燈 |
| 22 | 威尼斯 | 面具 |

## EQ-01｜登月 · 太空頭盔＋氣瓶

```
The head and neck of a low-poly faceted paper-cutout pelican, right-facing
profile, off-white angular paper-facet body, long flat orange beak with a red
tip, one black dot eye. It wears a white space helmet with a wide curved gold
visor, and a small oxygen tank is strapped to the back of its neck. Flat warm
off-white background. Crisp facet edges, flat shading, limited palette of
off-white, gold, orange, grey. No text, no logos, no scenery.
```

## EQ-02｜雨林 · 探險家軟木帽

```
The head and neck of a low-poly faceted paper-cutout pelican, right-facing
profile, off-white angular paper-facet body, long flat orange beak with a red
tip, one black dot eye. It wears a tan pith helmet, the classic explorer style,
with a chin strap. Flat warm off-white background. Crisp facet edges, flat
shading, limited palette of off-white, tan, orange, brown. No text, no logos,
no scenery.
```

## EQ-03｜深海 · 氧氣面罩＋全罩頭盔

```
The head and neck of a low-poly faceted paper-cutout pelican, right-facing
profile, off-white angular paper-facet body, long flat orange beak with a red
tip, one black dot eye. It wears a full-face diving helmet in dark brass, round
and heavy, with a thick glass window, and a breathing hose curves down from the
side. Flat warm off-white background. Crisp facet edges, flat shading, limited
palette of off-white, brass, orange, dark grey. No text, no logos, no scenery.
```

## EQ-04｜宇宙 · 圓球面罩太空頭盔

```
The head and neck of a low-poly faceted paper-cutout pelican, right-facing
profile, off-white angular paper-facet body, long flat orange beak with a red
tip, one black dot eye. It wears a space helmet with a large round spherical
gold-tinted glass bubble, sitting on a white collar ring. Flat warm off-white
background. Crisp facet edges, flat shading, limited palette of off-white, gold,
orange, grey. No text, no logos, no scenery.
```

## EQ-05｜兔子洞 · 頭燈

```
The head and neck of a low-poly faceted paper-cutout pelican, right-facing
profile, off-white angular paper-facet body, long flat orange beak with a red
tip, one black dot eye. It wears a knitted wool beanie with a small headlamp
strapped to the front, the lamp off. Flat warm off-white background. Crisp
facet edges, flat shading, limited palette of off-white, grey, orange, red. No
text, no logos, no scenery.
```

## EQ-06｜威尼斯 · 面具

```
The head and neck of a low-poly faceted paper-cutout pelican, right-facing
profile, off-white angular paper-facet body, long flat orange beak with a red
tip, one black dot eye. It wears an ornate Venetian carnival mask pushed up on
its forehead, gold with black filigree. Flat warm off-white background. Crisp
facet edges, flat shading, limited palette of off-white, gold, orange, black. No
text, no logos, no scenery.
```
