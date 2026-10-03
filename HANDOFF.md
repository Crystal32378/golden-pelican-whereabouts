# Handoff — Golden Pelican Whereabouts（2026-10-03）

主站 HEAD `acaa6a7`　分店 HEAD `f8d626f`　網域 `crystal32378.github.io`

> 本文件為**現況快照**。過期的競賽時程已於本次重寫移除（比賽未參加，該項線作廢）。
> 寫作調性比照主站 README：有數字、有名字、講清楚為什麼是這樣。

---

## 三個頁面

| | repo | 網址 | 狀態 |
|---|---|---|---|
| **主站** | `golden-pelican` | `/golden-pelican/` | 27 個場景 |
| **分店** | `golden-pelican-whereabouts` | `/golden-pelican-whereabouts/` | 地圖 24 站 + 證物牆 17 件 |
| **系列** | 同上，已併入 main | `…/golden-pelican-whereabouts/series/` | 卷宗 16 張 + 周邊 12 件 |

三個數字（27／24／26）**不是筆誤，是數不同的東西**：

- 主站 27 ＝ 全部場景，含兔子洞、島波海道
- 分店地圖 24 ＝ 刻意不標兔子洞與島波海道（`postcards/` 有這兩張圖，但 `SIGHTINGS` 沒有）
- 蓋章遊戲 26 ＝ 24 站 ＋ 兔子洞 ＋ 島波海道

---

## 本階段完成

**`share/README.md` 與 `README.md` 校正**（`f8d626f` 起）

- `share/README.md` 原寫「`singles-posters/`、`singles-merch/` 是資料夾」——**這兩個資料夾不存在**。
  28 張 `single-*.jpg` 是平放在 `share/` 根目錄。已改正。
- `README.md` Layout 表：`postcards/` 實際是 26 個 **`.png`**（非 jpg）；
  `posters/` 實際 34 張（`A`～`V` 22 ＋ `reddit/` 12）。已改正並補上數字差異說明。

**`.DS_Store` 移出版控**（`f8d626f`）

- `.gitignore` 加規則，`git rm --cached posters/.DS_Store`（本機檔案保留，只是不再追蹤）。

**蓋章遊戲上線**（`78ed1ff`、`cc73fa3`）

- 四種玩法：24 秒蓋章、頭部物件設定檔、翻牌配對、「It Just Left」猜站。
- 集滿 26 站發一張**假造的結案證書**。英文版，純前端，不收集任何資料。
- 地圖頁加入口（`cc73fa3`）——從證物牆進得去。

---

## ⚠️ 已知問題（本階段發現，未修）

**🔴 `game/` 斷圖**：game/index.html 引用 `postcards/tide.png`，但該檔不存在。
潮間帶是主站祕密站，**未在 repo 內提供圖片是刻意的**。需決定是改指向現有圖、
或移除該卡的插圖。未自行修改，因牽涉祕密站設定。

**數字不一致（有意為之，非 bug）**：`game/index.html` 內同時出現 24／26／27 三種說法，
對應上文三個不同集合。README 已加註，但頁面文字本身仍混用。

---

## 待辦

- **RC-02**（Reel Crew 索引卡牆）手寫中文變亂碼，已移出 `works-posters/`，待重做
- **BV-02** OCR 只讀到 `-1 -3 -5`，漏 `-2`，需目視確認
- **TT-02**（真話翻譯機）已重做，舊版備份在 `~/Desktop/hermes/out/old-posters/`
- **證物牆** 17 件對 22 張 `A`～`V` 海報，`F/G/H/I/S` 5 張未上牆
- **`game/` 斷圖**（見上方已知問題）

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

6. **macOS 沒有 `timeout`。** 生圖一輪 6 張要 3 分鐘以上，
   前景指令會被 30 秒砍掉，要 `nohup … &` 放背景再輪詢。

7. **做非主站的海報時，先把 `~/Desktop/hermes/refs/` 改名。**
   那是主站的鵜鶘參考圖，`gen_posters.py` 會自動抓 1 張當參考圖上傳，
   結果會滲進別的作品——LB-02 重跑時桌面中央長出一台「月亮的鵜鶘單車」。
   拿掉 refs 畫面乾淨很多。

8. **OCR 讀不到直排字。** CR-01 的直排邊欄註記 OCR 全無，
   但目視完全正確。**垂直排版不列入 OCR 驗收標準**，要目視。

9. **OCR 也會誤報已正確的字。** LB-02 的「明天再抽一次」被讀成
   「明天再抽二茨」，圖上是對的。低於 0.5 信心度的要目視再確認。

---

## 祕密（不可寫進任何公開頁面）

- **潮間帶**（`#tide`）與**花絮**（`#bts`）是主站藏起來的層
- **那條魚**——只有自己下車、NG 兩次才撈到的那條
- 系列頁 `tide` 出現次數須維持 **0**
- 分店不得提及花絮與魚

---

## 下一步

1. **`game/` 斷圖**——唯一會壞掉的地方，先修這個
2. RC-02 重做、BV-02 目視確認（見待辦）
3. 金流若要轉 live：見下方「金流」段
4. 作品集頁面與更多作品海報（無期限）

---

## 金流：test mode 已接好（2026-10-01）

`brand/index.html` 的贊助按鈕接到 Dodo Payments **test mode**，流程可完整跑完但**不動真錢**。
金額 US$2（checkout 顯示約 NT$65）。

**要轉成真的收款，改兩個地方：**

1. 完成 Dodo 的 KYC（台灣在支援名單內，用台灣身分證件即可，個人戶也可以）
2. 改 `brand/index.html` 裡的：

```js
const PAY = {
  mode: 'live',                    // 'test' → 'live'
  url: 'https://checkout.dodopayments.com/buy/<live 的 pdt_ 或 pl_ 連結>',
};
```

其餘不動。**注意：真的收錢之後就不是純敘事了** —— 頁面第 5 條寫著「不負責爭議、不做客服」，
那會變成一項實質承諾。要維持那個設定，就得真的自己承擔，或把第 5 條改掉。

## 為什麼沒有 2% 抽成

原本設計是「賣了就給 2%」。2026-10-01 放棄，理由記在 `brand/spec.md` 第八節：
真實收入幾乎是零、抽成與「沒有權力的機關」這個母題矛盾、
而且 payment link 金額固定（動態計算需要伺服器，做不到）。

## 分支

只剩 `main`。`series` 分支已於 2026-10-01 刪除（其 commit 28238a9 已在 main 歷史中，
刪除不遺失任何東西）。
