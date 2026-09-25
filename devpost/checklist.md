---
doc: checklist
status: approved
---

# Build Checklist

Build mode: **learn** (chosen by the learner — explanation after each step, learner checks, code pointers)

Context: the site already exists and is live (`golden-pelican-whereabouts`). This build covers the three rooms the PRD added after the prototype: the explainer + main-site button, the next-stop teaser card, and the mobile layout.

## Slices

- [x] **1. A stranger can understand the page in one line and jump to the moon**
  Becomes usable: under the WANTED notice there is a one-line explainer ("This is a 3D world where a pelican rides a bicycle through 21 scenes, each ordered by a different AI") and an "進入本店 →" button that opens the main site at `#moon`. Bilingual.
  Why now: it is the first thing a first-time visitor reads; the map can't help them if they don't know what they are looking at.
  PRD ref: `prd.md > The Core Journey` (step 1), `prd.md > Product Decisions` (one-line explainer)
  Spec ref: `spec.md > Components > WANTED notice and explainer`, `spec.md > Components > Language layer`
  Build: Add one element under `.wanted` with a `data-i18n`-style id; add zh/en strings to `STR`; wire it into `applyLang()`; style to match the poster (small, dim gold, not shouty).
  Verify (mechanical): Screenshot the page headless and confirm the explainer line and button are visible; confirm the button's href ends in `#moon`; switch language and confirm both texts change.
  Learner check: 打開 https://crystal32378.github.io/golden-pelican-whereabouts/（或本機檔案），看通緝令下面有沒有一行字說明＋按鈕；按下去確認跳到月球場景；再按右上角 EN 確認英文版也在。
  Commit: `Explain the page in one line and send visitors to the moon`

- [ ] **2. The next-stop teaser card**
  Becomes usable: a sealed card below the map showing `NEXT STOP: ?????`; after the visitor nominates a place, it unseals to their own leading local nomination; a tie shows 「本案陷入票數僵局」; a "tear up" action deletes one nomination and re-seals the card if it was the last. Bilingual.
  Why now: it is the suspense payoff of the whole ballot box — without it, nominations are write-only.
  PRD ref: `prd.md > The next-stop teaser`, `prd.md > States and Boundaries` (teaser card states)
  Spec ref: `spec.md > Components > Next-stop teaser card`
  Build: Add the card markup under the ballot; a `renderTeaser()` that reads `props`, computes plurality, and sets sealed/unsealed/tied state; a tear-up button per revealed nomination; strings in `STR`; call it from `applyLang()` and after every vote/nominate/tear-up.
  Verify (mechanical): Headless check with a seeded `localStorage` proposal list shows the unsealed state; with an empty list shows `?????`; tie list shows the deadlock line; the tear-up action removes the entry and re-seals.
  Learner check: 打開網站，看地圖下面有沒有「NEXT STOP: ?????」的封緘卡；提名「我家巷口」再看卡片有沒有揭開；再投一票給另一個地方，看它怎麼變；按撕掉看會怎樣。
  Commit: `Add the sealed next-stop teaser card`

- [ ] **3. The phone layout**
  Becomes usable: under 700px the map goes full width, the locker becomes a horizontally scrolling strip of postcards, and the ballot/footer stack below.
  Why now: it is the last surface a real visitor might be holding; the demo will be viewed on phones.
  PRD ref: `prd.md > Screens and Layout` (mobile)
  Spec ref: `spec.md > Components > Mobile layout`
  Build: One `@media (max-width: 700px)` block; no JavaScript changes.
  Verify (mechanical): Headless screenshot at 390×844 shows a full-width map, a horizontal locker strip, and no sideways overflow; the nominate button still reachable.
  Learner check: 用手機開那個網址（或 Mac 上把視窗縮窄），看地圖是不是滿版、明信片是不是橫著滑、投提名還能不能用。
  Commit: `Make the bulletin readable on a phone`

## Hands-on Checkpoints

- [ ] Early usable behavior explored — after slice 1
- [ ] Final kick-the-tires exploration and feedback completed

## Final Review

- [ ] Final review complete — feedback resolved and learner confirms ready to ship

## Code Tour and App Map

- [ ] Learning activity complete — guided route, focused alternative, prior practice connected, or brief recap
- [ ] Optional edit and transfer reflection addressed — offered/declined/already covered/not applicable as appropriate
- [ ] `devpost/app-map.html` generated from finished code, checked, and shown, including a project-grounded practice to reuse

Activity and evidence:
Route and stops:
Edit outcome:
Reflection:
Activity mode:

## Revisions

