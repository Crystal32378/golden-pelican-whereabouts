---
doc: prd
status: approved
---

# Golden Pelican's Whereabouts — Product Requirements

A WANTED bulletin and sighting map for a golden pelican that toured 21 locations in 24 hours, for anyone who just saw the main site shared and needs the bird's-eye view. Source: `scope.md > The Unique Kernel`, `scope.md > The Core Loop`.

## The Core Journey

1. **Arrive** from a shared link (chat, social post, or a friend). The page shows a gold-framed WANTED notice for the pelican and a dark world map already covered in red bicycle pins. A one-line explainer under the notice says what this really is — a 3D world where a pelican rides through 21 scenes, each ordered by a different AI — with an **Enter the Main Site** button.
2. **Scan** the map. Earth stations appear as individual bicycle pins; the Taipei area clusters into a single red disc reading "8 sightings". The right-hand **Unlocatable Locations** locker lists moon, deep sea, space, home, library, rain, vinyl, snow globe — each with a postcard photo and a deadpan report.
3. **Inspect a sighting.** Clicking a pin or a locker entry opens a postcard: the real screenshot from that scene, the sighting time (a real git commit timestamp), the one-line incident report, and an **Enter the Scene** button that deep-links into the main site at that exact station (`#venice`, `#moon`, …).
4. **Loop** between map, postcards, and the main site as curiosity strikes.
5. **Nominate.** Press **Nominate the Next Stop**, click any point on the map, and name it (your own alley counts). The nomination appears as an orange 📍 pin with a vote count. Vote for it, nominate more.
6. **Success** = the visitor understands the whole 24-hour pelican story in under a minute, has laughed at least once, and has either entered the main site or nominated a location. The site is read-only about the past (sightings are fixed facts) and personal about the future (nominations live in your own browser).

## Screens and Layout

One page, three regions, no navigation:

- **Header** — title, motto, language toggle (中文 / EN), WANTED notice with the one-line explainer and the Enter the Main Site button.
- **Main region** — the map (large, dark) on the left; the Unlocatable Locations locker on the right (fixed-width column, scrollable).
- **Footer region** — the Nominate the Next Stop button, its one-line instruction, and a small credits footer.

**Mobile (< 700px):** the layout becomes a vertical scroll — map on top at full width, the locker as a horizontally scrolling strip of postcards below it, the ballot button and footer beneath. Pinch/zoom and tapping must still work; the right column never squeezes the map.

## Look and Feel

Deadpan officialness. A dark grey world map (Esri Dark Gray), a black-brown page (#14100C), gold (#E8B860) and red (#C8453A) accents, a gold double-bordered WANTED poster, and typewriter-ish small caps for timestamps. Postcards are the only bright objects: white-bordered prints, tilted ~1°, with a dashed red stamp and handwritten-style date lines. Bilingual throughout (zh-TW / English) via a single toggle; the English keeps the same deadpan bureaucratic tone. Avoid playful cartoon styling, neon, or anything that winks at the camera.

## Features and Behavior

### The sighting map (source: `scope.md > The Core Loop`)

- 21 sightings, each with: scene name (zh + en), coordinates or "unlocatable", sighting time (git commit timestamp), one-line incident report (zh + en), a postcard screenshot, and a deep link into the main site.
- Pins cluster when close together (Taipei reads "8 sightings"); clusters open on click or zoom. Individual pins are red bicycles; nominations are orange map-pins.
- The map is the product: hovering and clicking never block the page.

### Postcards

- Photo-first: the screenshot is the largest element. Enter the Scene opens the main site in a new tab at the right `#hash`.
- Locker entries render inline (no popup) because those locations cannot be pinned.

### The next-stop teaser (source: `scope.md > The Core Loop`; replaces the open "notebook" question)

- Below the map sits a **sealed teaser card**: `NEXT STOP: ?????` with a "nominating" stamp — the suspense element of a WANTED bulletin ("where will the fugitive go next?").
- When the visitor has nominations, the card unseals to show **their own leading nomination** (plurality of their local votes): 「暫定下一站：我家巷口（1 票。票只存在你的瀏覽器裡，所以這是暫定。）」
- No nominations → the card stays sealed: 「還沒有人提名，你就是第一個。」
- A tie → 「本案陷入票數僵局」.
- The card is also where a visitor can tear up ("重新封存") one of their own nominations — the minimal "notebook" affordance, no separate list.
- Visitors are never misled: the card always states that the result is local and provisional.

### The personal ballot box (source: `scope.md > The POC Boundary`)

- "Nominate the Next Stop" arms the map; the next click drops an orange pin and asks for a name.
- Nominations and votes persist in the visitor's own browser only. No server, no global tally, no moderation queue — the UI states this honestly ("this is your detective notebook").
- Empty state: a visitor who has nominated nothing sees no orange pins; the button copy alone invites the first nomination.

### Bilingual copy (source: `scope.md > Inspiration & Identity`)

- Every user-facing string exists in zh-TW and English, including all 21 incident reports. The choice persists across visits.

## States and Boundaries

- **First visit** — map, 12 pins + 8 locker entries, zero nominations; the explainer line is the only explanation offered.
- **After the main site's scenes change** — this site is not auto-synced; sighting data is a hand-maintained list in one array.
- **Deep link to a missing scene** — if a `#hash` no longer exists on the main site, the link still opens the main site; no error handling is built.
- **No network / tiles fail** — the map greys out; the locker and the WANTED notice still work, because every fact lives in the locker too.
- **Nomination with a blank or silly name** — accepted. It is the visitor's own notebook.
- **Teaser card states** — sealed (`?????`, no nominations yet) / unsealed (leading local nomination) / tied ("本案陷入票數僵局") / after tearing up the last nomination, the card re-seals.
- **Privacy boundary** — nominations never leave the browser. The page must not imply otherwise.

## Product Decisions

- **Real world map, not a paper-cut map** — the mundane flight-tracker container is the joke; a cute custom map would be beautiful but expected, killing the contrast.
- **Local-only voting** — the learner said 「不用存票啦」: a global tally would need a backend and buys nothing for the joke. The ballot box is a personal detective notebook, explicitly labeled.
- **Open nominations** — anyone may name any place; "我家巷口" is a feature, not abuse. No moderation layer in the POC.
- **One-line explainer + Enter the Main Site button** — a stranger who lands here from a share link should understand the pelican story in seconds; mystery is for the map's tone, not for the premise.
- **Mobile = vertical scroll with a horizontal postcard strip** — a side-by-side map + locker is unusable on a phone.
- **Postcard tone for incident reports** — chosen by the learner over police-report and pigeon-testimony registers: 「我在月球，這裡沒有風，車痕會留一萬年」 register.
- **Screenshots are official captures** — the main store renders each scene in capture mode (no UI panel) and the learner picks from three moments per scene.
- **A next-stop teaser instead of a "my notebook" list** — the learner replaced the draft's notebook panel with a sealed `NEXT STOP: ?????` card that unseals to the visitor's own leading local nomination. People don't want to review what they voted; they want the suspense of where the fugitive goes next. The card doubles as the minimal way to delete a nomination.

## What We're Building

- Single static page on GitHub Pages; no build step; no backend; no accounts.
- 21 sighting entries with real coordinates, real commit timestamps, official 1280×720 scene captures, bilingual reports, deep links.
- Dark world map with clustering; unlocatable-locations locker with inline postcards.
- Personal ballot box in `localStorage`; share-by-URL is optional and only if time allows.
- Bilingual UI with persisted language choice; explainer line + Enter the Main Site button; mobile vertical-scroll layout.
- Sealed next-stop teaser card (sealed / unsealed / tied states) with a tear-up action for the visitor's own nominations.

## Deferred From the POC

- **Server-side vote totals** — needs a backend or third-party form store; the boss said votes need not be remembered globally.
- **Auto-sync from the main repo's git log** — would make sightings live, but the main repo's commit history is the source of truth manually for now; a build step or API would break "no build".
- **Moderation of nominations** — acceptable risk in a proof of concept; noted as a real-world gap.
- **Draw-your-own-riverside-ride routes** — tracing paths is a different feature from dropping a pin; it waits.

## Possible Later Enhancements

- "I voted for X" share cards. Animated pelican icon hopping between pins when a new station ships. Per-station comment walls. A B-side map for the pelican's unbuilt stations.

## Non-Goals

- User accounts/login — kills the 60-second demo, adds nothing to the joke.
- A custom illustrated world map — the mundane container is the point.
- Editing or modifying the main site in any way — the sibling must stay zero-touch; `#hash` deep links already exist.
- Real-time collaboration between visitors.

## Open Questions

- ~~How the Nominate flow behaves when a visitor has nominated several places~~ — resolved during review: the sealed teaser card shows the leading local nomination and hosts the delete action. No separate list.
- (Can wait) Whether the Enter the Main Site button goes to the main site's default scene or to a specific station.

