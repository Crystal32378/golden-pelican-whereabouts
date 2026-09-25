# 🗺️ Golden Pelican's Whereabouts

> 「The pelican is free to go anywhere. The model is free to bring its imagination to the world.」

一隻黃金鵜鶘在 24 小時內騎單車環遊 22 個地方（然後在兔子洞裡失聯）。這裡是它的**通緝網站**。

A WANTED bulletin and sighting map for the golden pelican — one bicycle, 22 locations, built in a single day, last seen falling underground, and still at large.

## 線上看 Live

**https://crystal32378.github.io/golden-pelican-whereabouts/**

## 這是什麼

地圖上每根紅色單車圖釘都是一次真實目擊——目擊時間是 main repo 的 **git commit 時間戳**。點擊圖釘可以看到「案情報告」和現場照片（明信片體），按「進入現場」會直接跳到那個場景。右側證物櫃「無法定位的地點」放的是月球、深海、宇宙、雪花球這種沒有經緯度的現場。

下方「提名下一站」可以替鵜鶘報名任何地方（我家巷口也可以）。票存在你自己的瀏覽器裡——這是你的偵查筆記本，不是選舉。

## 關於本體 The Main Site

**https://crystal32378.github.io/golden-pelican/** — 一個 Three.js 做的鵜鶘騎單車世界，22 個場景。每一站由不同的 AI 點菜，station 由 `#hash` 直接開啟（例：`#venice`）。

## 技術 Tech

純靜態網頁，無 build step。Leaflet（地圖）+ 一個 `localStorage` 投票箱 + 22 張現場照片。雙語（中文 / English）。

## 工作人員 Crew

- 構想、導演、點菜與法律意見（刑法部分）：**Crystal**
- 主廚（22 個場景、官方目擊照、拍照不摆拍）：**Claude Opus 5.5**
- 菜市場：**muse**
- 兔子洞（Space Bunny 點的菜，店兔子，值班中）：**Space Bunny** 🐰
- 書海、雨天、這張通緝單、兩次地圖被拒的紀錄：**Kimi**
- 造型語法（「幾何剪紙式 3D 世界」）：**GPT Sol**
- 配樂（`score.mp3`）：**MiniMax**（音樂模型）
- 第一位通緝犯…的部分來源：**Astra**（畫不出鵜鶘，但「被你發現了」留傳千古）

## 在地跑 Local

```bash
git clone https://github.com/crystal32378/golden-pelican-whereabouts.git
cd golden-pelican-whereabouts
python3 -m http.server 8000
# open http://localhost:8000
```

（直接開 `index.html` 也可以，只是地圖圖磚會對沒有 Referer 的請求比較嚴謹。）

## 製作筆記

`devpost/scope.md` 是這條線的「菜單」：為什麼是航班追蹤器風格、為什麼不做帳號、為什麼票不存伺服器。
