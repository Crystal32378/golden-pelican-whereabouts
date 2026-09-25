---
doc: spec
status: draft
---

# Golden Pelican's Whereabouts — Technical Spec

## How This Works, In Plain Language

It is one single HTML file. When a visitor opens it, their browser reads three things: a list of 21 sightings (name, where on Earth it is or why it can't be located, when it happened, one sentence about it, a photo, and a link back to the main site), a dictionary of every piece of text in two languages, and a few instructions for the map. The map itself is a free library (Leaflet) that draws a dark world map and puts a small red bicycle on top of each sighting; when several sightings sit on top of each other (Taipei has eight), they fold into one red disc showing the count, and clicking or zooming spreads them back out. Clicking any sighting opens a postcard with the photo and a button that jumps straight into that scene on the main site. The ballot box is a small trick: when a visitor nominates a place or votes for one, the site writes it into that visitor's own browser (localStorage) and nowhere else — no server, no database, no account. The sealed teaser card reads that same browser storage to show the visitor their own leading nomination as the "provisional" next stop.

Why this shape: the whole point is a joke that looks official, and official things are simple. A single file that a stranger can open, read, and trust is more convincing than an app with a backend behind it. The only moving parts are two free map libraries and the visitor's own browser storage.

## The Core Journey Through the System

PRD ref: `prd.md > The Core Journey`.

1. Visitor opens the page → the browser loads `index.html` → the WANTED notice and explainer line render immediately (no map needed to read them).
2. Leaflet initializes a map centered on East Asia; Esri's dark tiles arrive over the network; the 12 locatable sightings are added to a cluster group; the 8 unlocatable ones render as postcards in the locker column.
3. Visitor clicks the Taipei cluster → it opens into 8 bicycle pins; clicking one opens a popup containing a postcard (photo, sighting time, report, "Enter the Scene" link).
4. Visitor clicks "Enter the Scene" → a new tab opens the main site at `https://crystal32378.github.io/golden-pelican/#<id>` → Leaflet's `hashchange`-free deep link means the main site (not this one) handles the switch.
5. Visitor presses "Nominate the Next Stop" → the button arms the map → the next map click asks for a name → a new entry is written to `localStorage` and an orange pin is added.
6. Visitor presses "+1" on any nomination → the vote count in that entry increments → the teaser card re-renders and, if this visitor has any nominations, unseals to show their own leading one.
7. Language toggle → `LANG` flips → every string, all 21 names, and all 21 reports re-render in the chosen language; the choice is stored.

## Stack

- **Plain HTML + CSS + JavaScript in one file** — no framework, no build step. The proof of concept must be openable by double-clicking a file and deployable by pushing to GitHub. Framework/build tooling would add nothing to a single-page map.
- **Leaflet 1.9.4** (https://leafletjs.com) — the map itself, pinned via unpkg CDN. AGPL-2.0, free for this use.
- **Leaflet.markercluster 1.5.3** (https://github.com/Leaflet/Leaflet.markercluster) — folds overlapping pins ("8 sightings"). Pinned via CDN.
- **Esri World Dark Gray Canvas tiles** (https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer) — the dark map. No API key; attribution displayed on the map.
- **localStorage** — the ballot box and the language choice. Two keys: `gpw-proposals` (array of nominations) and `gpw-lang` (`zh` or `en`).
- **GitHub Pages (legacy branch deploy from `main`)** — hosting, already live at https://crystal32378.github.io/golden-pelican-whereabouts/.
- No package manager, no dependencies to install, no keys, no cost.

## Where It Runs and How Someone Tries It

- **Runtime:** any modern browser (the build was verified in Firefox and Chrome on macOS). Nothing to install.
- **Local:** `cd golden-pelican-whereabouts && python3 -m http.server 8000`, then open http://localhost:8000. (Opening `index.html` directly also works; some tile providers are stricter about requests without a Referer header — see Failure Modes.)
- **Live:** https://crystal32378.github.io/golden-pelican-whereabouts/
- **Demo recording:** screen-capture the live URL — no build step, no setup, so the recording is the site itself.

## Look and Feel

Deadpan officialness, as settled in `prd.md > Look and Feel`: near-black brown page (#14100C), dark grey map, gold (#E8B860) accents for structure and the WANTED frame, red (#C8453A) for pins and the "Nominate" button's armed state, off-white text (#F4EBD2). Postcards are the only bright, warm objects: #FFFDF4 paper, ~1° tilt, a dashed red stamp, handwritten-style date lines. Interface copy is bureaucratic and calm in both languages; nothing winks. Mobile keeps the same palette and swaps the layout (see Components).

## Components

### WANTED notice and explainer
The static header: title, motto, language toggle, gold-framed notice, one-line explainer ("This is a 3D world where a pelican rides a bicycle through 21 scenes, each ordered by a different AI"), and an "Enter the Main Site" button linking to the main site root. Renders with zero network. Implements `prd.md > The Core Journey` step 1.

### Sighting data (the single source of truth)
A hand-maintained array of 21 rows, each: `[id, name_zh, name_en, lat, lon, time, report_zh, report_en]`; `lat === null` means "unlocatable". The map pins, the locker, and every postcard are generated from this one array — adding a new station is one row. Times are copied from the main repo's git log. Implements `prd.md > The sighting map`, `prd.md > Postcards`, `prd.md > Bilingual copy`.

### Map and cluster group
Leaflet map + Esri tiles; locatable sightings go into a `markerClusterGroup` with a custom red "N 起目擊" disc icon; each marker keeps a reference to its row index so its popup can be re-rendered on language change. Implements `prd.md > The sighting map`.

### Postcards
A shared HTML template (photo, stamp, "目擊時間/Sighted" line) rendered two ways: inside map popups (locatable) and inline in the locker (unlocatable). Implements `prd.md > Postcards`.

### Unlocatable-locations locker
Right-hand column listing the 8 sightings with no coordinates, each with its postcard, name, time, report, and a link into the main site. Becomes a horizontally scrolling strip on mobile. Implements `prd.md > The sighting map`.

### Personal ballot box
Button arms the map; the next click prompts for a name; the entry `{lat, lon, name, votes}` is pushed into `gpw-proposals` in localStorage; each nomination renders as an orange pin with a "+1 / 投這裡一票" button. Implements `prd.md > The personal ballot box`.

### Next-stop teaser card *(to build)*
Below the map: a sealed card showing `NEXT STOP: ?????` when the visitor has no nominations, unsealing to the plurality of their own local nominations (tie → 「本案陷入票數僵局」), with a "tear up / 重新封存" action to delete one nomination (deleting the last one re-seals the card). Bilingual. Implements `prd.md > The next-stop teaser`.

### Language layer
A `STR` dictionary of every UI string in zh/en, a `LANG` variable persisted to `gpw-lang`, and one `applyLang()` that re-renders header, locker, popups, ballot, and teaser. Implements `prd.md > Bilingual copy`.

### Mobile layout *(to build)*
A single `@media (max-width: 700px)` block: map full-width at a fixed height, locker becomes a horizontal scroll strip of postcards beneath it, ballot and footer stack. No JavaScript changes.


## Data Model

| Data | Where it lives | Updated by | Survives revisit? |
|---|---|---|---|
| 21 sightings | `SIGHTINGS` array in `index.html` | hand edits (new station = one row) | yes (it's in the file) |
| UI copy (zh/en) | `STR` object in `index.html` | hand edits | yes |
| Nominations + votes | `localStorage["gpw-proposals"]` | visitor actions (nominate, vote, tear up) | yes, per browser |
| Language | `localStorage["gpw-lang"]` | toggle | yes |

No server, no database, no analytics, no cookies.

## File Structure

```
golden-pelican-whereabouts/
├── index.html            # the entire site: markup, styles, data, logic
├── postcards/            # 21 official 1280×720 scene captures (named <id>.png)
├── devpost/              # this planning workspace (scope, prd, spec, profile)
│   ├── learner-profile.md   # private, gitignored
│   ├── scope.md / scope.en.md / scope.html
│   ├── prd.md
│   └── spec.md
├── README.md             # public readme
├── .nojekyll             # lets GitHub Pages serve the folder as-is
└── .gitignore
```

## External Services and Dependencies

- **Esri tile server** — `GET https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}` → PNG tile. No key, no account, attribution required (displayed on the map). Free at this scale; no published hard rate limit.
- **unpkg CDN** — Leaflet 1.9.4 and Leaflet.markercluster 1.5.3, version-pinned URLs. Free, no key. https://unpkg.com
- **OpenStreetMap data** — used by Esri's basemap; credited on the map.
- **Main site** — deep-link target only: `https://crystal32378.github.io/golden-pelican/#<id>`. No API, read-only, zero changes to that repo.

## Important Failure Modes

- **Tile provider blocks us** (already happened twice: OpenStreetMap returned 403 "Access blocked" for `file://` requests; CARTO demanded an API key) → the map greys out; the WANTED notice, locker, and teaser still work because every sighting also exists as a card. Swapping providers is a one-line change — this is how we landed on Esri.
- **CDN unreachable / offline** → the map does not initialize; same fallback. Not bundling local copies of the libraries for a PoC.
- **localStorage unavailable** (private mode, storage disabled) → the ballot box and language choice degrade to in-memory for the session. Wrapped in try/catch.

## What Was Simplified and Why

- **localStorage instead of a backend** — the boss said 「不用存票啦」. Votes are personal and provisional by design; a real global tally would need accounts, a database, and moderation, none of which this joke requires.
- **Hand-maintained sightings instead of auto-syncing the main repo's git log** — a sync would need a build step or a GitHub API token; both break the "one file, no build" promise that makes the site trivially verifiable and recordable.
- **One HTML file instead of modular source** — nothing here warrants a bundler; the file stays readable for reviewers.
- **Legacy Pages deploy instead of an Actions workflow** — fewer moving parts, already live, and the repo needs no build to be inspectable.

## Decisions and Open Issues

- **Esri Dark Gray over OSM/CARTO** (agreed after both blocked us) — the dark map fits the surveillance tone and needs no key. Tradeoff accepted: the provider could change its policy again; the fix is a one-line URL swap.
- **Uncertainty discussed with the learner:** tile-provider policies are opaque and have already bitten this project twice. Small investigation during the build: confirm Esri's terms allow a hobby public demo (they do, with attribution), and keep the provider name + attribution line in the README so a future maintainer knows exactly what to change.
- **Open (carried from `prd.md > Open Questions`):** whether the "Enter the Main Site" button targets the main site's default scene or a specific station — default behavior for now; trivially changeable.
- **Contract to remember:** if the main site renames a scene id, the matching row's id must change with it — the deep link is the contract.

