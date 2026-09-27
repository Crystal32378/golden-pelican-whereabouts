# Handoff — Golden Pelican（2026-09-27）

主站 HEAD `c7f2fb0`　分店 HEAD `e35b0a1`　網域 `crystal32378.github.io`

---

## 三個頁面

| | repo | 網址 | 狀態 |
|---|---|---|---|
| **主站** | `golden-pelican` | `/golden-pelican/` | 25 站（24 公開 + 1 祕密） |
| **分店** | `golden-pelican-whereabouts` | `/golden-pelican-whereabouts/` | 24 站地圖 + 證物牆 17 件 |
| **系列** | 同上，已併入 main | `…/golden-pelican-whereabouts/series/` | 16 張海報 |

三者已串成一圈：

```
主站 README「延伸」→ 分店地圖
   └ 證物牆第 17 件後「case file GP-001 →」→ 系列 16 張
        ├ 6 張  → 主站 #rabbit / #venice / #salt / #shima
        └ 10 張 → 回分店 #ballot（提名地圖）或 #wall（證物牆）
```

系列頁與分店首頁**都不放入口連結**，要自己找才找得到。

---

## 本階段完成

**主站 `#hash` 深連結修好**（`c7f2fb0`）
初始 hash 檢查原本寫在 `pose(0)` 之前會被覆蓋回小島，已移到之後。
這是三場景以來就存在的 bug，由系列頁的回連第一次暴露。

**16 張系列海報**（`series/`）
- A「辦公室」× 6：卷宗、罰單、通緝令、證物袋、地圖、打字機
- B「外界」× 6：證詞、失物、貓、鴿子、粉筆字、櫥窗
- 全英文資訊文字；中文「鵜鶘」裝飾字已棄用
- 12/16 一次過關

**13 張作品集海報**（`works-posters/`，見 `WORKS-HANDOFF.md`）

---

## 競賽（唯一有硬期限）

**HY Image Challenge**，Track 1「Type & Layout」
- 截止 **2026-10-02 14:59（台灣）** ← 剩 5 天
- 必須在 **X 公開發文**並 tag `@gmi_cloud` 與 `@TencentHunyuan`
- 必須填 GMI 報名表單（X 連結、track、同意聲明）
- 得獎 $1,800（$200 現金 + $200 credits + $200 Hy credits + 展覽機會）

**投稿稿 `posters/A.jpg`（鄉民檔案室通緝令）已修好**
- 重跑 7 次挑最佳，「鵜鶘」正確、「最後目擊」正確（原本誤寫成「最後目灣」）
- 僅餘「目警者」與印章斷行兩處小瑕疵
- 備份在 `~/Desktop/hermes/out/A.png` / `A.prev.png` / `A.new-try2.png`

**⬜ 尚未做：X 發文。** 這是投稿必要條件，不能省。

---

## 待辦

- **RC-02**（Reel Crew 索引卡牆）手寫中文變亂碼，已移出 `works-posters/`，待重做
- **TT-02**（真話翻譯機五種譯法）5 個標籤只中 1 個，可重跑或改版式
- **BV-02** OCR 只讀到 `-1 -3 -5`，漏 `-2`，需目視確認
- **證物牆** 17 件對 22 張海報，`F/G/H/I/S` 5 張未上牆

---

## 工具鏈（已驗證）

**OCR（macOS Vision）**
```bash
# 編譯（只需一次，約 2 分鐘）
cd ~/golden-pelican-whereabouts/tools
swiftc -O ocr.swift -o ocr

# 使用
./ocr <圖檔…>     # 每張輸出辨識文字與信心度
```
原始碼在 `tools/ocr.swift`（已進版控），不必再找。

**生圖（GMI Cloud / Hy Image 3.5 preview）**
```bash
cd ~/golden-pelican-whereabouts
python3 tools/gen_posters.py A                                  # 比賽稿
python3 tools/gen_posters.py all                                # 比賽稿全部
python3 tools/gen_posters.py RA-03 --series docs/posters/prompts.md R 3:4
python3 tools/gen_posters.py PS-01 --series docs/posters/works/works.md S 3:4
```
- 鑰匙 `~/.gmi_key`（已存在）
- 輸出 `~/Desktop/hermes/out/<前綴>-<代碼>.png`
- **只有 3:4 = 1152×1536**（2:3 不支援）
- 約 20 秒／張
- 轉網頁版：`sips -s format jpeg -s formatOptions 72 -Z 1100 in.png --out out.jpg`

**流程**：生圖 → 轉 825×1100 jpeg → `/tmp/ocr` → 有錯重跑（單張最多 5 次）

---

## 關鍵教訓

1. **中文可行，但特定字不可行。**「鵜鶘」低頻，常變鷦鯨／鵜鸕／鵧鶓；
   「拖鞋一拍」「那就去看」這類常用語一次就對。避開專有名詞與生僻字。

2. **模糊用物理機制，不用指令。**「請寫得不清楚」只得到純亂碼；
   要用距離、雨漬、刪除線、斜角。反過來說 **OCR 讀不到不等於失敗**——
   幾張是靠模糊在說話（Reel Crew 的標籤、Draw One 還沒抽的籤）。

3. **語法通過 ≠ 邏輯正確。**曾有欄位錯位（`'#ballot'` 掉進 scene 欄，
   產生 `/##ballot` 壞網址），`node --check` 抓不到。
   要**實際執行渲染邏輯並印出最終 href** 驗證。

4. **headless Chrome 測不了 WebGL。**主站是 Three.js，`--headless` 拿不到
   WebGL context，dump 出來永遠是 HTML 原始值。要嘛請使用者用真瀏覽器驗，
   要嘛在 Node 跑 three.js stub harness。

5. **GitHub Pages 一 repo 只發布一個分支。**分店已佔用 `main`，
   系列頁改用目錄 `/series/`。

6. **macOS 沒有 `timeout`。**

---

## 祕密（不可寫進任何公開頁面）

- **潮間帶**（`#tide`）與**花絮**（`#bts`）是主站藏起來的層
- **那條魚**——只有自己下車、NG 兩次才撈到的那條
- 系列頁 `tide` 出現次數須維持 **0**
- 分店不得提及花絮與魚

---

## 下一步

1. **X 發文投稿**（硬期限 5 天）
2. 作品集頁面與更多作品海報（無期限）
