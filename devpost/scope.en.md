---
doc: scope
status: approved
lang: en
---

# Golden Pelican's Whereabouts

A companion "WANTED bulletin" site for the golden-pelican project: a world map of every place the pelican has been caught riding, plus a vote on where it strikes next. (Chinese original: `scope.md`.)

## The Unique Kernel
The humor engine: **absurd content in a mundane container**. A perfectly ordinary flight-tracker-style world map — except the pins are "月球", "深海", "雪花球", and the sighting records are real git commit timestamps proving 21 scenes were built in ~24 hours. The map looks official; the content is a pelican. This deadpan contrast is the project's comedic DNA (inherited from Astra's 「被你發現了」), and it's what makes a screenshot instantly shareable.

## Who It's For
Someone who just saw a friend share the pelican site and thought "wait, what IS this?" — they open Whereabouts, and within 30 seconds they get the whole joke: 21 crime scenes, one pelican, still at large. Today their only option is reading the README or scrolling 21 scenes one by one; nobody gives them the bird's-eye view.

## The Core Loop
Open the map → scan the pins (and the "unlocatable locations" evidence locker for moon/space/deep-sea/vinyl/snow-globe) → click a sighting card → land directly inside that scene on the main site via `#hash` deep link → come back and vote/propose the next crime scene. Return visits happen every time a new station ships — the map is the pelican's changelog you can read at a glance.

## Inspiration & Identity
- Main site (visual + narrative universe, paper-cut geometric 3D): https://crystal32378.github.io/golden-pelican/
- WANTED-poster tone: "Charges: toured 21 locations without a permit; cycled illegally in Venice. Features: paper-cut texture, red bicycle, a different hat at every stop. Last seen: Venice (pigeons declined to testify)."
- Flight-tracker mundanity as comedy container; paper-cut colors/typography only in the cards, pins, and chrome so the sibling relationship is visible without repainting the world.
- Motto on the homepage: "The pelican is free to go anywhere. The model is free to bring its imagination to the world."

## Why This Matters to the Learner
「從來沒有人問鵜鶘為什麼要騎車？騎去哪裡？」 — this site is the machine that finally asks. The learner built the pelican world in 24 hours with five AI collaborators; now they want the world to see it, and to let anyone answer where the pelican goes next.

## What "Working" Looks Like
A static page on GitHub Pages: real world map with 21 pins + an "unlocatable" evidence locker column. Clicking a pin/card opens the main site at that exact scene. A "next station" ballot box with an open text field (someone WILL write 我家巷口, and that's the final legendary Pokémon) and visible vote counts. The demo-video money shot: the map loads, pins light up, one click → the pelican is suddenly riding through Venice, pigeons scattering.

## The POC Boundary
- Real world map (free tile-based library), 21 station pins with paper-cut-styled sighting cards (name, git commit timestamp as sighting time, one-line "incident report", #hash link).
- "Unlocatable locations" column for stations with no earthly coordinates.
- Open-text next-station proposals + a personal ballot box: each visitor drops a pin, names the place, and casts votes — all stored in their own browser (localStorage). No server, no global counts; your detective notebook is yours.
- Static hosting, no build step, readable on a phone.

## Later
- Auto-syncing station data from the main repo's git log.
- Full draw-your-own-route proposals so someone can nominate their own neighborhood riverside ride.
- Shareable "I voted for X" cards; per-station comment walls.
- Animated pelican icon traveling between pins when a new station ships.
- Multilingual toggle (shipped in the POC: zh-TW + EN).

## Explicitly Cut
- **User accounts / login** — kills the 60-second demo and adds zero to the joke.
- **Paper-cut custom world map** — beautiful but expected; the mundane-container contrast is the punchline, and free map tiles save days.
- **Server-side global vote counts** — the boss said 「不用存票啦」: the ballot box is a personal detective notebook, not an election. Removes the only backend-shaped problem in the project.
- **Editing the main pelican site** — the sibling must require zero changes to golden-pelican; deep links already exist.
