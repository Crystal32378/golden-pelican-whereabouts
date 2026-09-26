# Reddit 系列海報（40 張計畫）· 樣板第一批 4 張

給 Reddit 用：每天一張、兩組風格交替、只放作品本身不做推廣。
受眾以英文為主，所以**資訊文字全英文**；唯一的例外是「鵜鶘」兩個中文字，
它是**裝飾性的品牌標記**，不是要傳達的資訊——就算模型把它畫歪了，
也只是裝飾走樣，不會讓人讀到錯誤的內容。

> 這是有意的取捨。實測 Hy Image 3.5 的中文字正確率極低
> （「鵜鶘」常變成鷦鯨、鵜鸕、鵧鶓、鵜鶬），而純英文幾乎不出錯。
> 所以把中文限制在一個「錯了也無害」的位置，其餘全部走英文。

## 通則（四張都適用）

- 比例 **3:4**（Hy Image 3.5 不支援 2:3；最接近的直式是 1152×1536。Reddit feed 用 3:4 合適。）
- 參考圖沿用 `refs/1-moon-頭盔與國旗.png`，讓鵜鶘的剪紙質感、紅色單車一致
- 每張都要求：**除列出的文字外不得出現任何其他文字**
- 不要水印、不要浮水印 logo。**不做視覺引流**——引流靠作品本身
- 「鵜鶘」藝術字：**視為瑕疵，不再使用**（實測走樣成亂碼，且觀感怪異）
- **主角規則（硬性）**：每張畫面裡都要有**鵜鶘或紅色單車**，哪怕只是剪影、
  倒影、遠景、插畫，或別人畫的樣子。這是整組的視覺主軸；沒有它的海報
  會顯得抽象、沒有主角。
  → 優先用「照片裡真實出現的鵜鶘／單車」，其次是「物件上的插畫或剪影」，
    再其次是「玻璃反射裡的模糊影子」。
- **質感原則（重要）**：粗糙的手寫感要**從照片本身的紙張與光線自然帶出**，
  不要靠「請寫得潦草一點」這種指令。實測證實：主體是照片時手感最好
  （RA-01 資料夾封面、RB-01 雨夜街頭），主體是「表格上的手寫字」時
  模型會把它畫成工整印刷體，質感全失（RB-02 失物招領即為此例）。
  → **一律以照片為主體**，字寫在照片裡的物件上（便條、紙片、牆上的字），
    而非讓模型在白紙上排版文字。

---

## RA-01｜案件卷宗 · 總覽（風格 A · the case file）

```
A printed case file cover on a manila folder, photographed straight on under a
single warm desk lamp. The folder is worn at the corners and has a red string
tied around it. A rubber stamp is pressed at the lower right, slightly crooked,
ink uneven.

Printed across the top in tall condensed black capitals:

THE GOLDEN PELICAN

Below, in a smaller monospaced typewriter face, perfectly legible:

CASE FILE GP-001
STATUS: STILL AT LARGE
CHARGE: 24 LOCATIONS WITHOUT A PERMIT
LAST SEEN: THE RABBIT HOLE
INVESTIGATING: THE VILLAGE JEALOUSY OFFICE

Along the bottom edge, small, as if written by hand in faded red ink:

a bicycle, one pelican, twenty-four places, and nobody will say where it went

At the very bottom, a small decorative mark of two Chinese characters brushed in
red ink, like a seal. The characters are decorative only; they may look
hand-lettered or slightly malformed.

The Chinese characters are the only non-Latin text in the image. No other text
anywhere. No watermark, no logo, no website.
```

## RA-02｜案件卷宗 · 威尼斯罰單（風格 A · the fine）

```
A photograph of a worn pink traffic citation taped to a damp stone wall by a
harbour, taken at night with a phone flash. The paper is curling at one corner,
water-stained, held up by a strip of yellowing tape. The wall behind it is rough
grey stone with moss in the joints. Everything slightly out of focus except the
paper. Flash shadow cast to the lower left.

The form is filled in by hand in blue ballpoint, the writing hurried and uneven,
as if written at the harbour in the rain. It reads:

COMUNE DI VENEZIA
OFFENCE: BICYCLE IN PROHIBITED AREA
LOCATION: SAN MARCO
SUSPECT: A BIRD
WITNESSES: PIGEONS
STATEMENT: REFUSED TO TESTIFY
FINE: 200 EUROS

At the bottom, a rubber date stamp in violet ink, blurred and half off the paper.

Deadpan, damp, faintly absurd. The Chinese characters are the only non-Latin
text in the image. No other text anywhere. No watermark, no logo, no website.
```

## RB-01｜目擊現場 · 證詞（風格 B · the statement）

```
A single photograph taken at night by someone standing in the rain, the way a
witness statement is documented. Shot on a phone, slightly too bright, the
subject a large long-beaked bird on a red bicycle seen from behind, riding away
down a wet road. Streetlight haloes, rain streaks, motion blur on the wheels.

The photo is printed on plain white paper and taped at the corners to a grey
corkboard. Below the photograph, in black ballpoint, a witness statement in
neat block capitals:

I SAW IT LEAVE THE HARBOUR.
NO HAT.
IT DID NOT LOOK BACK.

To the right of the statement, a small decorative mark of two Chinese
characters brushed in red ink, like a seal. The characters are decorative only
and may look hand-lettered or slightly malformed.

Grainy, ordinary, unmistakably amateur. The Chinese characters are the only
non-Latin text in the image. No other text anywhere. No watermark, no logo,
no website.
```

## RB-02｜目擊現場 · 失物（風格 B · lost and found）

```
A photograph taken from above on a wet wooden bench in a ferry terminal at
dusk, as if by someone who found something and photographed it where it lay. On
the bench: an open paper bag, a striped wool hat, a small red bicycle lying on
its side with one wheel still turning, and a folded sheet of paper with
handwriting on it. Rain has started to soak the corner of the paper. The
bench slats are wet and reflective, the harbour out of focus behind.

The handwriting on the folded paper is small, cramped, hurried, the way people
write on a form they are about to lose. It reads:

LOST: ONE ANDEAN WOOL HAT
STRIPED
LAST SEEN: A PLACE THAT IS NOT ON ANY MAP

At the bottom, a rubber stamp reading VILLAGE JEALOUSY OFFICE, faded and
partly smudged by the rain.

Quietly sad, ordinary, unmistakably a real find rather than a design. The
Chinese characters are the only non-Latin text in the image. No other text
anywhere. No watermark, no logo, no website.
```

---

## RA-03｜案件卷宗 · 掛在牆上的通緝令（風格 A）

```
A photograph of a printed wanted notice nailed to a weathered wooden wall
outside a shuttered harbour office, taken on an overcast morning. The paper is
sun-faded at the edges and has curled away from the wall at one corner. Three
different nails hold it. The wall behind is peeling grey-green paint over
boards. A puddle has dampened the lower edge, blurring one line of type. Shot
slightly from below, the paper not quite square to the frame.

Printed across the top in heavy condensed capitals:

WANTED

Below, a woodcut illustration of a long-beaked bird in a tiny top hat riding a
bicycle, drawn with black ink lines like a nineteenth-century engraving. Under
it, in smaller type:

THE GOLDEN PELICAN
LAST SEEN: THE RABBIT HOLE
CHARGE: 24 LOCATIONS, NO PERMIT
REWARD: 200 EUROS

Below that, a rubber stamp in faded red, pressed crooked, the ink patchy.

Bleached, patient, slightly forlorn. The Chinese characters are the only
non-Latin text in the image. No other text anywhere. No watermark, no logo,
no website.
```

## RA-04｜案件卷宗 · 證物袋（風格 A）

```
A photograph of a brown paper evidence bag lying on a steel table under a
single overhead light in an otherwise dim room. The bag is flat, creased shut,
its paper tie wrapped twice. A white label is taped to the front, and someone
has written on it by hand in thick black marker, the writing large and
unhurried. A pair of cotton gloves rests beside it, and a paper evidence seal
sticker is half peeled at one corner of the bag. Tucked under the string
tie, showing, is the item itself: a striped wool hat, and a small red bicycle
no longer than a finger. The steel table has old
scratches and one coffee ring.

The handwriting on the label reads:

ITEM: A HAT
DESCRIPTION: STRIPED WOOL
STATUS: UNRETURNED
CASE: GP-001

Underneath, a hand-lettered line:

DO NOT FILE THIS PROPERLY

Flat, quiet, oddly tender. The Chinese characters are the only non-Latin text in
the image. No other text anywhere. No watermark, no logo, no website.
```

## RA-05｜案件卷宗 · 地圖上的紅線（風格 A）

```
A photograph of a large paper street map pinned to a corkboard, photographed
from slightly to the left so the board is seen at an angle. Red string runs
between pins in a tangled path across the map, the string slack in some places
and taut in others. There are far too many pins. Small numbered labels are
written in ballpoint beside the pins, the numbers crowded and overlapping. A
magnifying glass lies on the board, its handle worn. Struck through one corner
of the map, the head of a long-beaked bird and the front wheel of a small red
bicycle, marked on the map itself in the same ballpoint. The cork is pale and dusty,
the map edges curling.

Handwritten in ballpoint at the top of the map, in a hurried hand:

24 STOPS IN 24 HOURS
I COUNTED TWICE

And in a different, shakier hand, circled:

I COUNTED ONCE

Crowded, obsessive, faintly unhinged. The Chinese characters are the only
non-Latin text in the image. No other text anywhere. No watermark, no logo,
no website.
```

## RA-06｜案件卷宗 · 打字機的一頁（風格 A）

```
A photograph of a single sheet of paper held in the roller of a mechanical
typewriter, the last line still part-fed. The paper is yellowed and thin, with
a faint blue ribbon mark down the centre. The typewriter itself is old, chipped
black enamel, photographed only as a dark shape at the edges of the frame. The
sheet is lit from one side by a desk lamp, the right side falling into shadow.
A pair of reading glasses sits on the machine, one lens catching the light.
Half under the sheet, pressed flat for years, a small pencil sketch of a
long-beaked bird in a top hat on a bicycle.

The typed text, the ribbon slightly uneven as old typewriters are, reads:

THE VILLAGE JEALOUSY OFFICE
CONFIDENTIAL

THE SUBJECT VISITED 24 PLACES
IN 24 HOURS, MOSTLY AT NIGHT

IN EVERY PLACE SOMEBODY
HAD ALREADY GIVEN IT SOMETHING

We do not know where it keeps
the things it was given.

The last line trails off, half-typed, the ribbon fading. The Chinese characters
are the only non-Latin text in the image. No other text anywhere. No watermark,
no logo, no website.
```

## RB-03｜目擊現場 · 貓的證詞（風格 B）

```
A photograph of a hand-drawn sketch on torn notebook paper, the paper creased
and damp at one corner, lying on a wet pavement. It has been left out in the
weather: the pencil is smudged, one corner of the paper is curling, rain has
bled the graphite. Beside the sketch, a pair of cat paws printed in dust on the
pavement, as if the cat stood there, and a single bicycle tyre track cutting
across the paw prints. The photograph is taken from directly
above, phone camera, the pavement filling the frame.

The sketch is done in rough pencil, the way someone draws a thing they only saw
for two seconds. Underneath, in the same rough pencil, unevenly spaced:

SOMETHING BIG
WITH A BIG MOUTH
WENT PAST

CONFUSION: LOW

The lines are shaky and the proportions are wrong. It is a bad drawing by
somebody who was not trying to be good at it. The Chinese characters are the
only non-Latin text in the image. No other text anywhere. No watermark, no logo,
no website.
```

## RB-04｜目擊現場 · 鴿子的版本（風格 B）

```
A photograph of a torn-off page from a spiral notebook, taped at one corner to
a metal railing at a harbour, fluttering slightly. Rain has speckled the page.
Behind it, out of focus: grey water, a moored boat, and a group of pigeons
standing on the quay. The page is shot through the railing, so one vertical
bar crosses the frame. Someone has written on it in biro, pressed hard enough to
score the paper:

WITNESS: PIGEONS
STATEMENT:

and then nothing, the line left blank, the pen still on the page as if the
witness stopped mid-sentence and left. Under that, a small drawing of a bird
shape that is mostly a triangle.

The blank space where the statement should be is the point. The Chinese
characters are the only non-Latin text in the image. No other text anywhere.
No watermark, no logo, no website.
```

## RB-05｜目擊現場 · 滑板上的粉筆字（風格 B）

```
A photograph taken at night, looking down at a concrete kerb where someone has
written in chalk. The chalk is old and smeared, half of it already scuffed
away by feet, and the writing runs off the end of the kerb so the last word is
incomplete. A bicycle is lying on its side in the road beside it, and someone
has also drawn a small circle on the pavement where a wheel came to rest, pressed into the chalk dust. The
streetlight is overhead, the chalk bright in the middle and shadowed at the
edges. Night, damp asphalt, the glow of a phone light at the edge of frame.

The chalk text reads:

SLOW DOWN
SOMEONE IS STILL LOOKING FOR IT

and beneath, added later in shakier chalk:

MOSTLY FOR THE HAT

Urban, quiet, slightly forlorn. The Chinese characters are the only non-Latin
text in the image. No other text anywhere. No watermark, no logo, no website.
```

## RB-06｜目擊現場 · 便利店櫥窗（風格 B）

```
A photograph of a convenience store window at 3am, taken from the pavement.
The window is fogged at the edges, the shelves behind it lit cold and blue, a
half-eaten sandwich on the counter. A handwritten sign has been taped to the
inside of the glass, the tape at one corner curling. The glass reflects the
street behind the camera, so a ghost of a red bicycle is visible in it,
distorted. The clerk is a figure behind the counter, out of focus, not looking
up.

The handwritten sign, on torn masking tape, in thick marker, uneven:

WE HAVE NO
HAT POLICY
FOR BIRDS

Below it, printed in small type on a shelf-edge label behind the glass:

PLEASE DO NOT ASK ABOUT THE BIRD

Late-night, fluorescent, deadpan. The Chinese characters are the only non-Latin
text in the image. No other text anywhere. No watermark, no logo, no website.
```

---

## 產出後

1. OCR 檢查：英文是否有漏字／拼錯、印章是否亂碼
2. 通過的轉 1100×825 JPEG 進 `posters/`
3. 不通過的重跑；同一張最多重跑 5 次，仍不過就記錄下來改用其他角度
4. 四張的品質與耗時確認後，再決定是否照這個模式做滿 24 張


# 混元 Hy Image 3.5 prompts（比賽稿 × 22 版）

來源：Kimi 寫 · 2026-09-26 · 給 GMI Cloud「Hy Week」活動（2026/9/25–10/1，免費七天）
比賽：Hy Image Challenge，Track 1「Type & Layout（海報／資訊圖）」，$1,800，10/1 23:59 PT 截止，10/8 公布。
投遞規則：**一人只能投一份、三軌擇一**；需在 X 公開發文並 tag `@gmi_cloud` 與 `@TencentHunyuan`。
API／MCP：GMI Cloud API（約 20 秒／張，可帶 5 張參考圖，輸出 1K–2K）。

## 通則（每張都適用）

- **參考圖：請上傳 `postcards/moon.png` 或 `postcards/venice.png`**，讓海報上的鵜鶘跟真的一樣
  （剪紙質感、透明頭盔、紅色單車）。
- 海報直式 **2:3**（1024×1536）；橫式分享卡 **1200×630**。
- 每個 prompt 都逐字列出文案，並要求 **不得出現任何其他文字**（生圖模型最常在背景加亂碼英文）。
- 不要水印、不要多餘標語。

---

## A｜鄉民檔案室（★ 推薦投稿 + 網站 hero）

```
A tall narrow printed notice pinned to a dark corkboard in a cluttered amateur archive
room, lit by a single warm desk lamp, with wide empty margins of dark corkboard above
and below and the text block occupying only the middle third of the frame. The paper is cream, slightly
curled at the corners, held by four mismatched push pins, with a faint coffee
stain and a red string crossing the wall behind it. Shot straight-on,
photojournalistic, shallow depth of field, the surrounding room is dark and out
of focus.

The poster is a plain printed notice in a black monospaced typewriter face,
centred, high contrast, very legible. The text reads exactly and only this, in
this order, top to bottom, with no other text anywhere in the image:

WANTED｜黃金鵜鶘
罪名：未經許可環遊 24 個地點
　　（含：在威尼斯違規騎單車；在地下失聯）
特徵：剪紙質感、紅色單車、每站換帽子
最後一次有人看見這隻鵜鶘，是在兔子洞，那裡沒有任何目擊者願意作證。
懸賞：提名下一站者，本中心代付
檔案編號：GP-001
本檔案室由業餘鄉民經營。專業不足，熱情有餘。
黑粉也是粉。

A small red rubber stamp reading "鄉民嫉妒中心" is pressed at the bottom right,
slightly crooked, ink uneven. The Chinese characters are crisp, correct and
perfectly rendered. No English text, no gibberish, no watermark.
```

## B｜西部通緝令（純英文，字型風險最低）

```
A tall narrow weathered western wanted poster on torn parchment, sepia and sun-bleached,
nailed to a rough wooden barn wall, with generous empty parchment above and below the notice. In the centre a crude
woodcut illustration of a large long-beaked pelican wearing a tiny top hat,
riding a bicycle, drawn with heavy black ink lines like a 19th-century engraving.

Above the drawing, in large slab serif letters:  WANTED
Below the drawing, in smaller slab serif:  $200 REWARD
  and under that, one line of smaller monospaced text:

GOLDEN PELICAN — LAST SEEN: THE RABBIT HOLE
CHARGE: TOURING 24 LOCATIONS WITHOUT A PERMIT
FEATURES: PAPER-CUT TEXTURE, RED BICYCLE, A DIFFERENT HAT AT EVERY STOP

Two bullet holes, torn right edge, foxing and age stains. Warm daylight from the
left. Photographed, slight perspective, no modern elements. Only the text
listed above appears on the poster. No other text, no watermark.
```

## C｜機密檔案（把「黑粉也是粉」放進去）

```
An official-looking redacted government document on manila folder paper, shot
flat from above under cool fluorescent light. Heavy black redaction bars cover
most paragraphs; a stamped header reads CONFIDENTIAL in tall condensed type.
Visible, unredacted, in a monospaced type:

SUBJECT: GOLDEN PELICAN
STATUS: AT LARGE
CHARGE: 24 LOCATIONS, NO PERMIT
LAST SEEN: RABBIT HOLE (NO WITNESSES)
FILE: GP-001
NOTE: 黑粉也是粉

The black bars are uneven and clearly hand-placed with a marker, a few
characters peek out from under them. A rubber date stamp in violet ink.
Clinical, deadpan, slightly funny. No other text, no watermark.
```

## D｜404 版（把真實事故變成彩蛋）

```
A browser error page printed on paper and pinned to a corkboard. The page is
plain white with centred grey monospaced system text, the look of a 404 error
screen:

404 — 案件載入失敗
本案共 24 站，其中 1 站（兔子洞）位於地下，伺服器找不到它。
檔案編號：GP-001

Below it, a line of smaller Chinese text: 「請稍後再試，或去書海看看。」
A small red rubber stamp at the corner reads "鄉民嫉妒中心".
The printout is slightly crooked, with a coffee ring. Cool screen glow on
paper, dark room, single lamp. Deadpan and absurd. No other text, no watermark.
```

## E｜案情時間軸（24 站的完整時間軸，README／工程筆記用）

```
A dark corkboard evidence board photographed straight on: 24 small photo
thumbnails connected by red string and pinned at slight angles, forming a loop,
with tiny paper labels under each reading (in legible monospaced type):

小島 20:31 ・ 操場 ・ 夜市 ・ 圓環 ・ 銀閣寺 ・ 登月 ・ 極地 ・ 雨林 ・ 雲海 ・
凱旋門 ・ 深海 21:36 ・ 宇宙 21:44 ・ 家 21:57 ・ 菜市場 22:09 ・ 書海 22:19 ・
雨天 22:31 ・ 黑膠 22:55 ・ 雪花球 23:08 ・ 植物園 23:16 ・ 回家 23:27 ・ 威尼斯 09:39

A handwritten red note pinned at the centre reads: 全部在 24 小時內完成。
A small stamp at the corner reads "鄉民嫉妒中心". Warm lamp, dark room,
everything on one flat plane. No other text, no watermark.
```

## F｜橫式社群分享卡（1200×630，Discord／Devpost／X 用）

```
A wide banner, 1200x630, dark corkboard background with a single large cream
paper notice centred, drop shadow, slight rotation. On the paper, a
right-aligned slab-serif headline in English and one line of monospaced
Chinese, both crisp and perfectly rendered:

GOLDEN PELICAN'S WHEREABOUTS
24 locations in 24 hours. One bicycle. Still at large.
一隻鵜鶘，24 個現場，最後目擊：兔子洞。

A small stamp reads "鄉民嫉妒中心". Everything else is dark and empty.
No other text, no watermark.
```

---

## 產出後的下一步

1. 存到 `~/Desktop/hermes/`，把檔名告訴 Kimi
2. Kimi 會用 macOS OCR 抓圖裡的文字，**檢查有沒有錯字**
3. 挑一張當網站 hero、一張當社群分享卡、進 README
---

## 尺寸：只有五個選項（對應修正版）

Hy Image 可選：**1024×1024 / 1536×1536 / 2048×2048 / 1920×1080 / 1080×1920**

| 版 | 選哪個 | 理由 |
|---|---|---|
| **A 鄉民檔案室（投稿）** | **1080×1920**（直式） | 唯一的直式選項。海報往上長，建構要留白：文字塊放中間，上下留暗色軟木板與燈光 |
| **A 備用（給網站）** | **2048×2048**（方形） | 方形放進網站兩欄版面最不彆扭，也不會糊 |
| **B 西部通緤令** | **1080×1920** | 直式海報；純英文，長版面反而更有「公告」的氣勢 |
| **C 機密檔案** | **1080×1920** | 直式公文紙 |
| **D 404 版** | **1080×1920** | 直式 A4 感；可真的印出來（列印時選「縮放至填滿」） |
| **E 時間軸** | **1920×1080** | 24 個節點橫著排 |
| **F 分享卡** | **1920×1080** | 生成後**裁成 1200×630**（上下各裁掉約 47% → 實作：先裁到 1920×567 再縮到 1200×630），Discord／X 的 OG 標準尺寸 |

**直式（9:16）構圖要注意**：prompt 裡已加一句——「a tall narrow notice, wide empty margins of dark
corkboard above and below, the text block occupying the middle third」。**不然混元會把文字硬塞滿整張，
中文字就會被拉得又長又細。**

**下載後處理**

1. **競賽投稿**：交原檔（1080×1920 的 PNG／JPG），不壓縮。
2. **放進網站**：海報縮到長邊 1200px、JPEG 品質 80 → **< 250KB**（分店「0.2 秒載入」不能被一張大圖毀掉）。
3. **F 分享卡**：裁成 1200×630 後，丟進 `<meta og:image>`（評審從 Discord／X 點進來看到的第一張圖）。
4. **favicon**：另外用 1024×1024 生一張，只有圖釘＋「WANTED」兩字，不要小字。
---

## 修訂版（第一輪 OCR 檢查後重生）

第一輪六版的 OCR 結果：C 版掉了字（SUBJECT: GOLDE）、E 版 24 個標籤太密開始胡言亂語、
F 版掉了「鵜鶘」兩個字。以下三版是針對這些錯誤重寫的 prompt。

## G｜機密檔案 v2（修掉 GOLDE）

```
An official-looking redacted government document on manila folder paper, shot flat
from above under cool fluorescent light. Heavy black redaction bars cover most
paragraphs; a stamped header reads CONFIDENTIAL in tall condensed type. One
visible, unredacted block, in a monospaced type, each line short and widely spaced:

SUBJECT: THE PELICAN
STATUS: AT LARGE
CHARGE: 24 LOCATIONS, NO PERMIT
LAST SEEN: THE RABBIT HOLE
FILE: GP-001
NOTE: 黑粉也是粉

The black bars are uneven and clearly hand-placed with a marker, a few characters
peek out from under them. A violet rubber date stamp in the corner, deliberately
blurred and illegible. Clinical, deadpan, slightly funny. No other legible text,
no watermark.
```

## H｜時間軸 v2（只留時間，24 個標籤減成 12 個）

```
A dark corkboard evidence board photographed straight on: a loop of red string with
twelve small photo thumbnails pinned at slight angles, generous empty corkboard
around them so nothing is crowded. Under each thumbnail, one small paper label in
a legible monospaced type. The labels read, clockwise from the top:

小島 20:31 / 登月 20:31 / 凱旋門 20:31 / 深海 21:36 / 宇宙 21:44 / 家 21:57 /
菜市場 22:09 / 書海 22:19 / 黑膠 22:55 / 雪花球 23:08 / 回家 23:27 / 威尼斯 09:39

A single handwritten red note pinned at the centre reads: 全部在 24 小時內完成。
A small stamp at the corner reads "鄉民嫉妒中心". Warm lamp, dark room, one flat
plane. Only the text listed above appears. No other text, no watermark.
```

## I｜分享卡 v2（補回「鵜鶘」）

```
A wide banner, dark corkboard background with a single large cream paper notice
centred, drop shadow, very slight rotation. On the paper, a centred slab-serif
headline in English, and below it exactly one line of monospaced Chinese:

GOLDEN PELICAN'S WHEREABOUTS
24 locations in 24 hours. One bicycle. Still at large.
一隻鵜鶘，最後目擊：兔子洞。

A small red stamp reads "鄉民嫉妒中心". All text sits within the central
horizontal band of the frame, with generous empty space above and below, so it
survives a wide crop. Everything else is dark and empty. No other text, no watermark.
```
---

## 中英對照版（老闆要求：同一張要有中英兩個版本）

風險筆記：「鵜鶘」是生圖高危字（實測會變成「鷦鯨」），所以中文版一律「短句 + 一次出現」，
英文版則完全不寫中文——除了那枚**永遠是中文的印章**（那是本室的章，不是文案）。

## J｜A 的英文版（英文孿生）

```
A worn paper WANTED notice pinned to a dark corkboard in a cluttered amateur
archive room, lit by a single warm desk lamp. The paper is cream, slightly
curled at the corners, held by four mismatched push pins, with a faint coffee
stain and a red string crossing the wall behind it. Shot straight-on,
photojournalistic, shallow depth of field, the room is dark and out of focus.

The notice is plain printed type in a black monospaced typewriter face, centred,
very legible. The text reads exactly and only this, top to bottom:

WANTED | GOLDEN PELICAN
CHARGES: touring 24 locations without a permit
(incl. cycling illegally in Venice; missing underground)
FEATURES: paper-cut texture, red bicycle, a different hat at every stop
LAST SEEN: the Rabbit Hole (no witnesses)
REWARD: one nomination for the next stop, paid by this office
CASE FILE: GP-001
This office is run by amateurs. Underqualified, over-invested.
Haters are fans too.

A small red rubber stamp with Chinese characters is pressed at the bottom right,
slightly crooked. All lettering crisp and correct. No other text, no watermark.
```

## K｜B 的中文版（西部通緝令・中文）

```
A tall narrow weathered wanted poster on torn parchment, sepia and sun-bleached,
nailed to a rough wooden barn wall, generous empty parchment above and below the
notice. In the centre a crude woodcut of a large long-beaked pelican in a tiny top
hat riding a bicycle, heavy black ink engraving lines.

Above the drawing, large slab serif letters:  通緝令
Below the drawing, in large slab serif:  $200 懸賞
  and under that, three short lines of smaller monospaced text:

黃金鵜鶘 —— 最後目擊：兔子洞
罪名：未經許可環遊 24 個地點
特徵：剪紙質感、紅色單車、每站換帽子

Two bullet holes, torn right edge, foxing and age stains. Warm daylight from the
left. Only the text listed above appears. Chinese characters crisp and correct.
No other text, no watermark.
```

## L｜C 的中文版（機密檔案・全中文）

```
An official-looking redacted government document on manila folder paper, shot flat
from above under cool fluorescent light. Heavy black redaction bars cover most
paragraphs; a stamped header in tall condensed Chinese type reads 機密. One
visible unredacted block, monospaced, short widely spaced lines:

對象：黃金鵜鶘
狀態：下落不明
罪名：24 個地點，未取得許可
最後目擊：兔子洞（無目擊者）
檔案編號：GP-001
附註：黑粉也是粉

The black bars are uneven, clearly hand-placed with a marker. A violet rubber
date stamp in the corner, deliberately blurred and illegible. Clinical, deadpan,
slightly funny. Chinese characters crisp and correct. No other legible text,
no watermark.
```

## M｜分享卡・全英文版（修掉「一隻鷦鯨」）

```
A wide banner, dark corkboard background, a single large cream paper notice
centred with a drop shadow, very slight rotation. Serif headline and three short
lines beneath, all perfectly legible:

GOLDEN PELICAN'S WHEREABOUTS
24 locations in 24 hours. One bicycle. Still at large.
LAST SEEN: THE RABBIT HOLE

A small red stamp with Chinese characters at the corner. All text sits within the
central horizontal band with generous empty space above and below, so it survives
a wide crop. Everything else dark and empty. No other text, no watermark.
```
---

## 第二輪題目（Sol 出公文題、Opus 出素描題、Kimi 寫 prompt）

共同笑點：**一件荒唐事，被所有人極度認真地記錄。**
（不畫潮間帶、魚、花絮——那是還沒公開的站，畫出來等於劇透。）

## N｜威尼斯違規罰單（Sol 第一選擇）

```
An official municipal violation notice on aged cream paper, photographed flat on a
counter. Venetian municipal styling: a red wax seal, an ornate printed border, a
small blurred instant photo of a bicycle at the bottom corner, and a handwritten
line in blue ink. Printed text reads exactly:

COMUNE DI VENEZIA — NOTIZA DI VIOLAZIONE
OFFENCE: BICYCLE OPERATION IN PROHIBITED AREA
LOCATION: SAN MARCO
WITNESSES: PIGEONS
STATEMENT: REFUSED
FINE: €200 (DISPUTED)

Below, handwritten in blue ink: Suspect continued toward the bridge.

The paper is slightly stained, one corner dog-eared, a coffee ring near the seal.
Cool daylight, shallow depth of field, deadpan and utterly serious. No other
legible text, no watermark.
```

## O｜兔子洞出入境管制站（Sol）

```
A photograph of a homemade border-control desk at the entrance of an earthen
rabbit hole: a small wooden table, one warm lamp, a hand-carved wooden stamp, a
bell, a ledger. On the dirt wall behind, a hand-painted sign in uppercase
hand-lettering:

ENTRY PERMIT REQUIRED
BICYCLES DECLARED: 1
PELICANS DECLARED: 0

On the desk, a heavily over-stamped entry card with stamps overlapping each other
illegibly. Cozy lamp light, dust, a little wooden fence. Deadpan bureaucracy, no
other legible text, no watermark.
```

## P｜兔子洞失物招領（Sol）

```
A lost-and-found table in a small archive room, photographed from above at a
slight angle. Laid out neatly with small gaps: a tiny top hat, a small brass key,
a bottle with a handwritten label reading DRINK ME, an open pocket watch, a single
long grey feather, and a small red bicycle parking tag. Warm lamp light, dark
background. A small index card beside the items reads, in neat handwriting:

Items recovered after the incident.
Owner has not returned.

No other legible text, no watermark.
```

## Q｜線人電話線：27 則未證實目擊（Sol）

```
A police-desk surface covered with evidence: dozens of small folded paper notes,
polaroid photos, a hand-drawn map with wrong coastlines, sticky notes and paper
clips, all overlapping. Each note has one short handwritten English line, and the
notes are scattered in no order:

Saw him near the moon.
Definitely not a pelican.
Red bicycle confirmed.
My cousin says Venice.
Please stop calling us.
He has a hat again.

In the centre, one note circled twice in red pen: RABBIT HOLE???
Warm desk lamp, dark room, cluttered but readable. No other legible text,
no watermark.
```

## R｜目擊者素描：三隻貓的版本（Opus）

```
A police sketch artist's drawing on slightly yellowed paper, photographed flat.
Pencil and smudged eraser marks. The sketch shows a large, round, wide-mouthed
creature with a huge bill riding a bicycle — it reads more like a big fish on a
bike than a bird, drawn by someone who only saw it for two seconds at night.
Below the sketch, a typed caption:

WITNESS: THREE CATS (STRAY)
STATEMENT: something big with a very big mouth went past
CONFIDENCE: LOW

Pencil only, no colour, official form margins. No other legible text, no watermark.
```

## S｜目擊者素描：威尼斯鴿子的版本（Opus）

```
A police sketch artist's drawing sheet that is completely blank except for a
rubber stamp at the bottom right, pressed slightly crooked in red ink:

WITNESS: PIGEONS (VENICE)
STATEMENT: REFUSED TO TESTIFY
SKETCH: —

The rest of the page is empty. Straight-on photograph, paper texture visible,
official form margins, a faint coffee ring. Deadpan. No other legible text,
no watermark.
```

## T｜目擊者素描：白兔的版本，畫在懷錶錶面上（Opus）

```
A macro photograph of an open pocket watch face being used as a drawing surface:
a frantic, extremely hurried pencil sketch of a long-beaked bird on a bicycle,
scribbled across the clock face, with the hands of the watch crossing the drawing.
The sketch is rough and impatient, clearly done in seconds. Scribbled beside it in
small hurried capitals: LATE. NO TIME. Below, on the cream dial, printed brand text
that reads: NEVER LATE. The watch lies on a dark wooden table.

No other legible text, no watermark.
```
---

## 第三輪：Opus「嫌犯自白書」＋ 重畫鴿子空畫框

## U｜嫌犯自白書（做完這張封牆）

```
A police statement form on cream paper, photographed flat under a single desk lamp.
The printed form has boxes and lines and a small official header, but the only
handwriting on it is one single line written very large, uneven, and slightly
rotated, as if written by someone in a hurry with a fat marker:

我只是在騎車。

The signature line at the bottom is left completely empty. In the small box beside
it there is a single soft grey webbed-foot print, like a wet stamp, slightly
smudged. A coffee ring near the top corner. Everything else on the page is blank.
No other writing, no other marks, no watermark.
```

## V｜鴿子版素描：重畫成「空畫框」（第一次畫到鳥了）

```
A police sketch sheet lying on a desk, photographed straight from above. In the
centre of the sheet is a printed rectangular frame, like a picture frame or a
placeholder box, and INSIDE THE FRAME THERE IS ABSOLUTELY NOTHING — it is blank
white paper, completely empty, no drawing, no lines, no figure, no outline.
The frame itself is printed in thin black type. Below the frame, a small stamp in
red ink, slightly crooked, reads:

WITNESS REFUSED TO TESTIFY

Around the sheet: a desk, a pencil, an eraser with a worn tip, and nothing else.
Deadpan, funny, quiet. No other text, no watermark.
```
