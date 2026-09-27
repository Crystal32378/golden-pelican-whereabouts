# Handoff — 作品集（另一個對話用）

日期：2026-09-27　分店 HEAD 見 `HANDOFF.md`
目標：做作品集頁面 + 補作品海報。**無硬期限**，但比賽投稿優先（見 HANDOFF.md）。

---

## 現有產出

**19 張作品海報**在 `works-posters/`，**10 個作品**：

| 代碼 | 作品 | 風格 | OCR |
|---|---|---|---|
| BV-01 | beat-the-villain | 昭和驚蟄祭壇，暗紅金燭火 | ✅ 全對 |
| BV-02 | beat-the-villain | 四種法器與傷害值 | ⚠️ 讀到 -1 -3 -5，漏 -2 |
| UP-01 | unseen-pain | 診所指示牌，冷白 | ✅ 全對 |
| UP-02 | unseen-pain | 夜間牆上的手寫字 | ✅ 全對 |
| TT-01 | truth-translator | 凌亂廚桌上的五張複寫條，最後一張紅墨水 | ✅ 五句全對 |
| TT-02 | truth-translator | 辦公室桌燈旁「請先深呼吸」的卡片 | ✅ 全對 |
| PS-01 | THE-PROMPT-SANG-ITSELF | 暗房器材棚 + 五標籤 | ✅ 全對 |
| PS-02 | THE-PROMPT-SANG-ITSELF | 五線譜上印出的字 | ✅ 全對 |
| WC-01 | walk-me-there | 路口路牌上的真貓頭鷹 | ✅（`ONE WAY` 刻意） |
| WC-02 | walk-me-there | 濕地面上的手機 | ✅ `...recalculating` |
| DO-01 | draw-one | 茶桌上的籤 | ✅（刻意無文字） |
| DO-02 | draw-one | 宣紙上唯一一筆 | ✅ 全對 |
| RC-01 | reel-crew | 膠片庫長廊 | ✅（標籤刻意看不清） |
| TM-01 | talk-me-out | 試衣間鏡上貼的裁決卡 | ✅ `WALK AWAY` `13` 全對 |
| TM-02 | talk-me-out | 折成八格的五問記分紙 | ✅ 五列全中 |
| LB-01 | life-blind-box | 玻璃罐裡的大白菜＋耳麥紅燈 | ✅ 整句全對 |
| LB-02 | life-blind-box | 撕碎的熱感紙＋唯一完整一張 | ✅ 四行全對（畫面偏暗） |
| CR-01 | cinephile-radar | 打勾的片單方格紙 | ✅ 直排字 OCR 讀不到，**目視全對** |
| CR-02 | cinephile-radar | 索引卡牆＋紅框「暫譯」 | ✅ 紅框那張正確，周圍亂碼是刻意的 |

**RC-02 已移出**（手寫中文變亂碼），待重做。

原始 PNG：`~/Desktop/hermes/out/S-*.png`（1152×1536）

**⚠️ 生圖時把 `~/Desktop/hermes/refs/` 暫時改名**，裡面是主站的鵜鶘參考圖，
會滲進來——LB-02 第一次重跑時畫面中央出現「月亮的鵜鶘騎單車」。
沒有 refs 時畫面乾淨很多，之後做非主站海報都該這樣跑。

---

## Prompt 檔

`docs/posters/works/works.md` — 14 個區塊，每個 `## XX-NN｜標題` + ```` ``` ```` 內是 prompt。
**不要改檔名或結構**，`gen_posters.py --series` 靠 `^## ([A-Z]{2}-\d+)｜` 解析。

新增作品的寫法：
```
## AB-01｜作品名 · 場景描述

```
<英文 prompt>
```
```

---

## 尚未做海報的 repo

有網址的（作品集頁面要連這些）：
```
Flow-Switch          換掉環境的音樂
celestial-dev-pets   星座小動物
odyssey              AI 互動旅程
pawradar             遇見你的狗狗
portfolio-doctor     作品集可恢復性檢查
second-eyes-agent    照片分流 agent
three-body-game      三體遊戲
voice-microdrama-engine  語音微劇場引擎
zhongyuan-festival   中元節
```

沒網址的（需先確認是否有 demo，或純讀 README 決定要不要做海報）：
```
Ginkgo  Nightingale  draw-one-research  brand-librarian
fable-night-owl-app  apparel-fitting-collaboration-workspace
nude-*（三個）  talk-me-out-archive  three-body-problem
```

**各 repo 的實際路徑與網址**（家目錄底下沒有，都在 Documents 等資料夾裡）：

| 作品 | 路徑 | 網址 |
|---|---|---|
| talk-me-out | `~/Documents/Talk Me Out of it/talk-me-out-hackathon` | github.com/Crystal32378/talk-me-out |
| life-blind-box | `~/Documents/Life Blind Box/repo` | life-blind-box.onrender.com |
| cinephile-radar | `~/Documents/三體遊戲/cinephile-radar` | majestic-toffee-9733c4.netlify.app |
| three-body-game | `~/Documents/三體遊戲/three-body-game` | （無公開網址） |
| Flow-Switch | `~/Documents/三體遊戲/Flow-Switch` | github.com/Crystal32378/Flow-Switch |
| pawradar | `~/Documents/三體遊戲/pawradar` | github.com/Crystal32378/pawradar |
| cinephile-radar | 同上 | 見上 |

**下一步建議**：已經 10 個作品，**可以開始做作品集頁面了**。
剩下的按「有網址且調性鮮明」挑，`three-body-game`、`zhongyuan-festival`、
`voice-microdrama-engine` 看起來最有潛力。
`estate-detective` 在磁碟上找不到，別再找了。

---

## 作品集頁面（要做的）

- 位置：建議 `~/golden-pelican-whereabouts/works/`，網址 `/golden-pelican-whereabouts/works/`
- 結構：每個作品一張海報 + 標題 + 一句話 + 連結
- **風格刻意不統一**（這是這批的特色，不要做成跟 series 一樣的兩個系統）
- 用 JS 陣列驅動，參考 `series/index.html` 的做法
- 海報 825×1100（3:4），`loading="lazy"`

**驗證方式**：跑 Node 印出每張的最終 href，確認無空錨點、無 `/##` 壞網址
（見 HANDOFF.md 教訓 3）。

---

## 產圖速查

```bash
cd ~/golden-pelican-whereabouts
python3 tools/gen_posters.py AB-01 --series docs/posters/works/works.md S 3:4
sips -s format jpeg -s formatOptions 72 -Z 1100 \
  ~/Desktop/hermes/out/S-AB-01.png --out works-posters/AB-01.jpg
/tmp/ocr works-posters/AB-01.jpg
```

- 免費期到 **2026-10-02 14:59**，之後要花錢（$0.024/張官方價）
- 一張約 20 秒 + 輪詢
- 中文可以用，但避開生僻字（教訓 1）
- 模糊用物理機制：距離、雨漬、刪除線、斜角（教訓 2）
