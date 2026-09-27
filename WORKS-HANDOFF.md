# Handoff — 作品集（另一個對話用）

日期：2026-09-27　分店 HEAD 見 `HANDOFF.md`
目標：做作品集頁面 + 補作品海報。**無硬期限**，但比賽投稿優先（見 HANDOFF.md）。

---

## 現有產出

**13 張作品海報**在 `works-posters/`，7 個作品：

| 代碼 | 作品 | 風格 | OCR |
|---|---|---|---|
| BV-01 | beat-the-villain | 昭和驚蟄祭壇，暗紅金燭火 | ✅ 全對 |
| BV-02 | beat-the-villain | 四種法器與傷害值 | ⚠️ 讀到 -1 -3 -5，漏 -2 |
| UP-01 | unseen-pain | 診所指示牌，冷白 | ✅ 全對 |
| UP-02 | unseen-pain | 夜間牆上的手寫字 | ✅ 全對 |
| TT-01 | truth-translator | 公文紙 + 紅筆白話對照 | ✅ 全對（最美） |
| TT-02 | truth-translator | 五種譯法五種筆跡 | ⚠️ 5 中 1 |
| PS-01 | THE-PROMPT-SANG-ITSELF | 暗房器材棚 + 五標籤 | ✅ 全對 |
| PS-02 | THE-PROMPT-SANG-ITSELF | 五線譜上印出的字 | ✅ 全對 |
| WC-01 | walk-me-there | 路口路牌上的真貓頭鷹 | ✅（`ONE WAY` 刻意） |
| WC-02 | walk-me-there | 濕地面上的手機 | ✅ `...recalculating` |
| DO-01 | draw-one | 茶桌上的籤 | ✅（刻意無文字） |
| DO-02 | draw-one | 宣紙上唯一一筆 | ✅ 全對 |
| RC-01 | reel-crew | 膠片庫長廊 | ✅（標籤刻意看不清） |

**RC-02 已移出**（手寫中文變亂碼），待重做。

原始 PNG：`~/Desktop/hermes/out/S-*.png`（1152×1536）

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

## 尚未做海報的 repo（27 個）

有網址的（作品集頁面要連這些）：
```
Flow-Switch          換掉環境的音樂
Unseen-pain          ✅ 已做
celestial-dev-pets   星座小動物
cinephile-radar      電影獎片單追蹤
estate-detective     工程活動時間線重建
odyssey              AI 互動旅程
pawradar             遇見你的狗狗
portfolio-doctor     作品集可恢復性檢查
second-eyes-agent    照片分流 agent
talk-me-out          勸退我的朋友
three-body-game      三體遊戲
voice-microdrama-engine  語音微劇場引擎
zhongyuan-festival   中元節
```

沒網址的（需先確認是否有 demo，或純讀 README 決定要不要做海報）：
```
Ginkgo  Nightingale  draw-one-research  brand-librarian
fable-night-owl-app  life-blind-box  apparel-fitting-collaboration-workspace
nude-*（三個）  talk-me-out-archive  three-body-problem
```

**下一步建議**：先挑 3-5 個有網址且調性鮮明的做，湊到 10-12 個作品再做頁面。
最想先做：`talk-me-out`（半夜勸你別這樣）、`estate-detective`（偵探）、
`life-blind-box`、`three-body-game`。

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
