# GMI Hy Week · Track 1 報名表單（照抄用）

頁面：https://www.gmicloud.ai/hy-week
**截止：2026-10-01 23:59 PT ＝ 2026-10-02 14:59（台灣）**
規則：一人一件、一個 track。已投 Type & Layout。

---

## Contact

| 欄位 | 填 |
|---|---|
| Full name | `Crystal Chang` |
| GMI Cloud account email | `crystalys.chang@gmail.com` |
| Country | `Taiwan` |
| X handle | `@CChang9909` |
| Link to your X post | `https://x.com/CChang9909/status/2104199879681843365` |

貼文已確認包含 `@gmi_cloud` 與 `@TencentHunyuan`，且為公開。

## Work

| 欄位 | 填 |
|---|---|
| Track | `Type & Layout` |
| Title | `16 Posters, One Missing Pelican` |

### Link to the work

```
https://crystal32378.github.io/golden-pelican-whereabouts/series/
```

即 X 貼文裡 `Full set →` 那個 t.co 短網址的實際目的地（已驗證）。
16 張全系列在這一頁；單張圖另見下方 description 開頭的說明。

### Prompt or workflow description

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

## Consent

- [x] This is original work made during the campaign.
- [x] I give GMI Cloud and Tencent Hunyuan permission to feature this work, including at LA and SF Tech Week.
- [ ] Send me product updates from GMI Cloud.（選填，不勾）

---

## 填之前檢查

- [ ] Country 下拉選單要選到 **Taiwan**（不是 "Other"）
- [ ] Track 選 **Type & Layout**，不要選到 Commercial 或 Game Art
- [ ] Link to the work 貼系列頁網址，不要貼 t.co
- [ ] 送出前確認 X 貼文仍是**公開**（鎖定帳號不能評審）

## 風險筆記

1. **`Link to the work` 欄位寫的是 "Image, gallery or short video"**，
   三個選項都是視覺媒體，沒有「網站」。填系列頁（網頁）有一點風險，
   但 X 貼文本身也指向那裡，兩者一致最安全。description 開頭已說明是 16 張一組的網頁系列。
2. **七天窗口**：活動 9/25–10/1。X 貼文發佈在窗口內。9/28 之後 repo 又有
   4 個 commit（品牌系統、分店改淺色、蒲甘站、系列頁復古質感）。
   規則原文是 "made during the seven-day window" —— 作品在窗口內製作即符合，
   貼文後續更新不影響。若評審嚴格要求貼文當時版本，系列頁現在是新版。
3. **已知瑕疵已主動揭露**：目警者/目擊者。判斷是對的 —— 這組是
   Type & Layout，比的是字與排版，藏一個錯字被發現的損失遠大於揭露的損失。
4. **12/16 一次過關也寫了**（Crystal 決定：他們需要知道真實狀態）。
   搭配「4 張重跑、未使用修圖工具」與「1 處已知錯字」，三段合起來是一個
   可信的方法論敘述，不是弱點曝露。
