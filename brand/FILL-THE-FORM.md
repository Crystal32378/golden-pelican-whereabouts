# Track 1 表單 · 照抄用

頁面：https://www.gmicloud.ai/hy-week
截止：2026-10-01 23:59 PT ＝ **10/2 14:59 台灣**（剩 2 天多）

---

## 1. Full name

```
Crystal Chang
```

## 2. GMI Cloud account email

```
crystalys.chang@gmail.com
```

## 3. Country

```
Taiwan
```

⚠️ 下拉要真的選到 Taiwan，不能是 Other

## 4. X handle

```
@CChang9909
```

## 5. Link to your X post

```
https://x.com/CChang9909/status/2104199879681843365
```

## 6. Track

```
Type & Layout
```

⚠️ 不要選到 Commercial 或 Game Art

## 7. Title

```
16 Posters, One Missing Pelican
```

## 8. Link to the work

```
https://crystal32378.github.io/golden-pelican-whereabouts/series/
```

⚠️ 貼完整網址，不要貼 t.co

## 9. Prompt or workflow description

**下面三段全部貼進去，中間不要斷開。** 全文 870 字。

### 第 1 段（貼這個）

```
A 16-poster series, all generated on Hy-Image-3.5-preview at 1152x1536 (3:4).
Hy-Image was the only model used for every final image.

WHY A 16-PIECE SET, AND WHY THIS MODEL
$0.024 per image at 2K, about 20 seconds per generation. That unit economics is
the whole reason this entry is a set and not a single hero image. One polished
poster costs almost nothing either way — but a set costs 16 times nothing, and
that gap is the difference between an image and a world. At this price I could
not only afford the final poster, I could afford the four failures behind it.
Verification is what turns a cheap model into a usable one, and verification is
only affordable if generation is cheap.

To make that concrete: the 16-poster set plus the single submission poster
came to 27 generations, about $0.65 at the campaign rate, counting every failed
attempt and every re-roll. 17 shipped, 10 were discarded — roughly a third of
everything I generated did not make the set. I mention the number because a
cheap model is only useful if being wrong about it is also cheap, and for
anything involving rendered text, being wrong is the normal case.

So the work is not 16 posters, it is 16 statements in one continuous voice:
the same bird, the same 24 hours, the same case number, seen from sixteen
different desks. Judged one at a time they are competent. Judged as a set they
build a place — a file room, a wall of index cards, a world being reported by
people who were there. The narrative is the deliverable. The posters are how it
gets said.

THE METHOD: generate, then verify.
Hy-Image renders text well enough to build on, but not reliably enough to trust.
So nothing shipped unread. Every candidate was converted to 825x1100 JPEG and
passed through macOS Vision OCR; a poster shipped only if its text read back
correctly. Failures were re-rolled, up to five attempts each. 12 of 16 passed
on the first run. The other 4 were re-rolled, not hand-corrected — I have no
image editor in the loop, because a hand-corrected poster would stop being
evidence about what the model can do.

The one defect I did not fix, and shipped on purpose: a lower line on the
submission poster reads 目警者 instead of 目擊者. The rule for this set was
that information text must read back correctly, and this one line does not.
I re-rolled seven times and never got it, then kept the best of the seven
anyway. It is the only known wrong glyph in the set.
```

### 第 2 段（接在後面，中間空一行）

```
WHAT RUNNING 16 POSTERS TAUGHT ME, stated as findings rather than conclusions:

1. Character frequency decides more than language does.
   Every short, common phrase rendered correctly on the first attempt. Rare,
   low-frequency characters degraded reliably and consistently: 鵜鶘 came back
   as 鷦鯨, 鵜鸕, 鵧鶓 across different runs. The model handles Chinese; it
   does not handle rare Chinese. So information text was restricted to
   high-frequency characters, and no poster was ever allowed to depend on the
   bird's name rendering correctly.

2. Illegibility must be physical, not instructed.
   Prompting "write this smudged" or "make it unclear" produces noise with no
   legible structure. Prompting a physical cause — distance, rain staining, a
   deletion line, an oblique angle, a torn edge — produces degradation that
   still reads as a real object. Several posters depend on this: unreadable
   index labels are the subject, not a failure. The corollary matters for
   judging the set: OCR finding no text is not automatically a failed poster.

3. Valid syntax is not correct logic.
   A field-ordering bug put an anchor string in the scene column of a data
   array, which silently generated a dead /##ballot link on the live page.
   Every linter passed and node --check passed. It surfaced only when I
   executed the render logic and printed the final hrefs. Worth stating
   plainly: the things that caught it were the least clever checks in the set.
```

### 第 3 段（接在第 2 段後面，中間空一行）

```
4. I never used the seed parameter, and that was a mistake I can now name.
   The API exposes seed, and re-running an identical prompt is supposed to be
   reproducible when you pin it. I re-rolled 7 times on one poster, which
   means every attempt was a different random draw. I was changing two
   variables at once and could not tell whether a failure belonged to the
   prompt or to the draw. Pinning seed and re-rolling the prompt alone would
   have made each attempt comparable. I verified seed exists in the API
   schema, and then left it at 0 for the entire series.

THE SET
Two groups of eight. Office: case file, traffic citation, wanted notice,
evidence bag, a map, a typewriter. The world outside: testimony, lost
property, a cat, pigeons, chalk, a till receipt.

The posters come from a larger project. A golden pelican rode a red bicycle
through 24 locations in 24 hours, then went missing underground. This series
is its Reddit feed — office and world, as seen by people reporting it. The
last exhibit in the series is a confession, and the pelican is not in custody.

Full working files, prompts and the OCR pass are public in the repository.
```

## 10. Consent

- [x] This is original work made during the campaign.
- [x] I give GMI Cloud and Tencent Hunyuan permission to feature this work, including at LA and SF Tech Week.
- [ ] Send me product updates from GMI Cloud.　← 選填，**建議不勾**

按 Submit。

---

## 送出前檢查

- [ ] Country 選到 Taiwan，不是 Other
- [ ] Track 是 Type & Layout
- [ ] Link to the work 是完整網址，不是 t.co
- [ ] X 貼文還是公開的
- [ ] Description 三段都貼了，開頭結尾沒被截掉

## 風險（都評估過了，可以安心填）

- **Link to the work 寫的是 "Image, gallery or short video"** —— 沒有「網站」選項。填系列頁有一點風險，但 X 貼文也指向那裡，兩者一致最安全，Description 開頭也說明了是 16 張一組。
- **七天窗口 9/25–10/1** —— X 貼文和作品都在窗口內。9/28 之後的 4 個 commit 是後續更新，不影響符合資格。
- **主動揭露錯字** —— 這組評 Type & Layout，比的就是字。藏著被發現損失遠大於自己講。

---

# 背景資料（不用填，參考用）

## 規則核對

| 規則 | 狀態 |
|---|---|
| 一人一件、一個 track | ✅ 只投 Type & Layout |
| 七天窗口內製作 | ✅ |
| 生成跑在 Hy Image 3.5 preview | ✅ `hy-image-v3.5-preview` |
| X 公開 + tag 兩個帳號 | ✅ 已驗證 |
| 截止 10/1 23:59 PT | ⏰ 剩 2 天 14 小時 |

## 官方規格（用 `~/.gmi_key` 實查 API，不是看行銷頁）

| 項目 | 官方實際 |
|---|---|
| 模型 | `hy-image-v3.5-preview`（org: tencent-hunyuan） |
| 支援尺寸 | **13 種**：1:1 / 16:9 / 9:16 / 4:3 / 3:4 / QHD / 4K |
| 本次使用 | `1152×1536`（3:4，1,769,472 px） |
| 價格 | $0.024（≤2K）／$0.032（>2K） |
| 參考圖 | 最多 5 張，不影響價格 |
| 參數 | `prompt` / `size` / `image` / `seed` / `generate_max_pixels` |
| 同步 | submit block 到完成，通常 10–60 秒 |

⚠️ **舊 handoff 有錯**：「只有 3:4 支援」不對，官方支援 13 種尺寸。`1152x1536` 是選擇，不是唯一可能。

## 費用

| 項目 | 張數 | 費用 |
|---|---|---|
| 16 張系列（12 一次過 + 4 重跑） | 20 | $0.48 |
| A 投稿稿（重跑 7 次） | 7 | $0.17 |
| **合計** | **27** | **≈ $0.65** |

17 成品、10 廢稿。整個 7 天視窗（含後來所有作品集與品牌系統）約 78 張 ≈ $1.87。

