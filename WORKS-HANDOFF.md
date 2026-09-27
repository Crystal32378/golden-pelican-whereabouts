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

## 各作品的「真實色票」與前台風格（2026-09-27 從原始碼抽出）

**為什麼要這張表**：海報看起來都一樣，主因是我整批用同一種「昏黃桌上光」。
但每個專案自己的 CSS 裡就有它真正的顏色，照著做就不會撞。

| 作品 | 真實色票 | 前台調性 | 海報該走的色溫 |
|---|---|---|---|
| **truth-translator** | `#f2b84b` 琥珀 · `#e86d79` 珊瑚紅 · `#82ce7a` 綠 · `#70a7ff` 藍 · `#56606b` 灰 · 底 `#0b0c0e` | 深底 + 五色對應五種譯法 | **深色底＋五色** |
| **walk-me-there** | `#fbbf24` 琥珀金 · `#f59e0b` · 底 `#1e293b` 深藍灰 · `#4ade80` 綠 | 暖琥珀 × 深藍灰，貓頭鷹 | **琥珀暖光**（溫暖陪伴） |
| **talk-me-out** | `#ff3b30` 紅 · `#ffd60a` 黃 · `#ff9f0a` 橘 · `#30d158` 綠 · `#2c2c2e` 深灰 | Apple 系統色，四色 verdict | **冷白＋系統色**（不是暖黃） |
| **cinephile-radar** | `#ff1744` 紅 · `#f3d18c`/`#e5c158`/`#c5a059` 金 · `#0c0f13` 近黑 · `#2979ff` 藍 | 黑底 + 金，電影感 | **黑金**（我原本做太淺太白） |
| **life-blind-box** | shadcn 預設，未改 | 無專屬色 | 深夜、單一光源（成立） |
| **three-body-game** | shadcn 預設，未改 | 無專屬色 | 深色＋星野 |
| **reel-crew** | 前端在 `demo_app/`，無根目錄 css | agentic production | 工業／倉庫（成立） |
| **Unseen-pain** | 中華電信提案，臨床 | 醫療資訊 | **冷白臨床**（成立） |
| **draw-one** | 無獨立 css | 東方 oracle | **暖木＋米白**（成立） |
| **beat-the-villain** | — | 出氣筒 | 暗紅金（成立，最搶眼） |

**結論**：我這批 19 張裡 16 張暖色為主，但 truth-translator 本身是**深底五色**、
cinephile-radar 是**黑金**、talk-me-out 是**冷白系統色** ——
我把它們全做成暖黃，等於把三個作品自己的視覺身份抹掉了。

---

## 26 個 repo 對照（2026-09-27 從 GitHub API 重查）

**GitHub 上實際是 26 個**，handoff 舊版寫的 27 個是錯的。

**GitHub 上不存在、磁碟上也找不到**（別再找了）：
`estate-detective` · `portfolio-doctor` · `three-body-game`（有磁碟沒 GitHub）
· `draw-one-research` · `nude-hardening` · `talk-me-out-archive`
· `apparel-fitting-collaboration-workspace` · `three-body-problem`
（前三者磁碟上不存在，`three-body-game` 有磁碟但 GitHub 404）

**GitHub 有、handoff 漏掉的兩個（值得做）**：
- **`Nightingale-Walk-with-Me`** — 9/27 剛更新。「地圖說你到了，夜鶯把你送到對的門口」
  專治最後 300 公尺（捷運出口→醫院正確入口），AI interprets / verified data decides，
  路線是人工走過拍照的。**跟 walk-me-there 同血統但風格該完全不同：真實街景、白天、有人。**
- **`second-eyes-agent`** — Python。「保留證據、保留不確定性、保留人類最終決定權」
  400 張照片分流成 SHORTLIST 18 / REVIEW 7 / REMAINING 375。**資訊整理類，走冷色臨床。**

**life-blind-box 狀態**：`~/Documents/Life Blind Box/repo` 的 remote 指向
`github.com/Crystal32378/life-blind-box`，但該頁 **404**（2026-09-27 實測）。
Crystal 說會自己公開。公開版身分是 `voice-microdrama-engine`（AMD Hackathon，
有 Railway demo），只有 3 個場景。

---

## 產圖速查

```bash
cd ~/golden-pelican-whereabouts
python3 tools/gen_posters.py AB-01 --series docs/posters/works/works.md S 3:4
sips -s format jpeg -s formatOptions 72 -Z 1100 \
  ~/Desktop/hermes/out/S-AB-01.png --out works-posters/AB-01.jpg
/tmp/ocr works-posters/AB-01.jpg
```

**生圖前先把 refs 移開**（教訓 7）：
```bash
mv ~/Desktop/hermes/refs ~/Desktop/hermes/refs.bak
python3 tools/gen_posters.py TT-01 --series docs/posters/works/works.md S 3:4 &
mv ~/Desktop/hermes/refs.bak ~/Desktop/hermes/refs   # 跑完再移回
```

- 免費期到 **2026-10-02 14:59**，之後要花錢（$0.024/張官方價）
- 一張約 20 秒 + 輪詢，**超過 30 秒要 `nohup … &` 放背景**（教訓 6）
- 中文可以用，但避開生僻字（教訓 1）
- 模糊用物理機制：距離、雨漬、刪除線、斜角（教訓 2）
- **不要用「壓到穿紙的紅色液體」**去表示暴力／升級，會讀成血。
  用「對照」「拆解」「層級」這類結構元素（2026-09-27 TT-01 教訓）
- OCR 低於 0.5 信心度、或直排文字，都要目視確認（教訓 8、9）
