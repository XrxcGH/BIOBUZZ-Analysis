# FIELD AND ARENA — the geometry reference

### Cross-season quantitative field data, and the backing document for `ANALYSIS-PROTOCOL.md` **R4**

**Written:** 2026-08-22 (T-21) · **Status:** this file was missing. `ANALYSIS-PROTOCOL.md` §5 budgets **40 minutes and two students** to R4 "ARENA and geometry" and had no reference behind it, unlike R3 (`SCORING-PATTERNS.md`), R5 (`PENALTY-AND-ENFORCEMENT.md`) and R6 (`LOOPHOLE-CASEBOOK.md`). This is that reference.

**Scope.** Numbers, not names. `KEYWORD-GLOSSARY.md` §6 already catalogues *what FIRST calls* the field elements across 11 seasons. This file catalogues *how big they are, how high they are, how far apart they are, and what that has historically forced onto the robot.*

---

## Evidence labels

`[C]` CONFIRMED-BIOBUZZ (in V0 or another final FIRST BIOBUZZ document) · `[H]` HISTORICAL-PATTERN (prior seasons, never a BIOBUZZ number) · `[J]` JUDGMENT · `[M]` MEASURED here · `[E]` ESTIMATED · `[U]` UNVERIFIED. Same contract as `STRATEGY-RANKING-PROTOCOL.md` §0.2.

---

## 0. The nine numbers to carry into kickoff day

| # | Fact | Label | Source |
|---:|---|---|---|
| 1 | FIELD is **144 in × 144 in** (12 ft × 12 ft, 3.66 m) measured to the **inside** face of the perimeter wall | `[H]` 2009-10 → 2025-26, 17 consecutive seasons | DECODE §9.2; SKYSTONE GM2 glossary "Playing Field Wall"; HOT SHOT Rev 7 |
| 2 | Floor is **36 interlocking soft foam TILES**, each ~**24 × 24 × 0.59 in** | `[C]` for BIOBUZZ — V0 §16 glossary states 36 TILES | `BIOBUZZ_V0_layout.txt` glossary; DECODE §9.2 |
| 3 | Perimeter wall is **~12 in (30.5 cm) tall** | `[H]` 2015-16 → 2023-24 verbatim; unchanged in ITD/DECODE figures | SKYSTONE / POWERPLAY / CENTERSTAGE GM2 glossary "Playing Field Wall" |
| 4 | **Every dimension in the manual and the CAD carries ±1 in (±2.5 cm)** | `[H]` DECODE §9.1, ITD §9.1 | DECODE TU32 §9.1 |
| 5 | The manual says outright: **"Successful teams will design ROBOTS that are insensitive to these variations."** | `[H]` DECODE §9.1 orange box | same |
| 6 | **"ZONE" = inside the FIELD. "AREA" = outside the FIELD.** A vocabulary rule, stated in the manual, that changes what a rule means | `[H]` DECODE §9.3 | DECODE TU32 §9.3 |
| 7 | Boundary tape is **1 in wide 3M tape** — a robot can cross it, so a zone edge is a *plane*, not a wall | `[H]` DECODE §9.3 | same |
| 8 | Zones are defined as an **"infinitely tall volume bounded by …"** — vertical extent is unbounded unless stated | `[H]` 11/11 seasons (see `KEYWORD-GLOSSARY.md` §6.1) | DECODE §9.3; ITD §9.3 |
| 9 | Robot starts as an **18 in cube**; expansion limits return, numbers deferred to Kickoff | `[C]` V0 R105 | `CONSTRUCTION-RULES-R.md` §3 |

> **The single highest-value sentence in any ARENA section is #4/#5.** A mechanism whose success depends on a dimension being nominal will work in your shop and fail at an event. Every alignment decision in `reference/mechanisms/*` should be re-read against a ±1 in field.

---

## 1. FIELD envelope by season — the part that has never changed

| Season | FIELD size | Floor | Perimeter | Label |
|---|---|---|---|---|
| 2005-06 Half-Pipe Hustle (FVC) | **~10 ft × 14 ft** — *not* 12×12 | `[U]` | `[U]` | `[H]` one-pager |
| 2006-07 → 2007-08 | deferred to "official field drawings, appendix 5" | `[U]` | `[U]` | `[U]` |
| 2008-09 Face Off | `[U]` size; **SoftTiles present** ("composed of the SoftTiles (mat)") | soft tiles | `[U]` | `[H]` |
| 2009-10 Hot Shot → 2023-24 CENTERSTAGE | **12 ft × 12 ft** | soft foam tiles | ~12 in tall wall | `[H]` |
| 2024-25 ITD, 2025-26 DECODE | **144 in × 144 in** | 36 tiles @ 24 in | am-0481 Perimeter Kit | `[H]` |
| **2026-27 BIOBUZZ** | **not published** | **36 TILES `[C]`** (V0 glossary) | am-0481b in the AndyMark BIOBUZZ listing `[C]` | mixed |

**Read this as:** the 12×12 / 36-tile / 12-in-wall envelope has held for 17 straight seasons and BIOBUZZ V0's glossary already re-states the 36-TILE floor. Treat "6 × 6 grid of 24 in tiles" as the safest planning assumption available before kickoff — but the number of tiles is the only part V0 actually confirms `[C]`; the 144 in and the wall height are `[H]` until you read §9.2 on 12 Sep.

### 1.1 Why the tile is the right unit

`[J]` Every distance estimate in R3/R4 should be written in **tiles**, not inches:

- one tile ≈ **24 in ≈ 0.61 m**;
- a full-field traverse is **6 tiles ≈ 12 ft**;
- a corner-to-corner diagonal is **~8.5 tiles ≈ 17 ft**;
- `[E]` a competent FTC drivetrain covers roughly **1 tile per 0.35–0.5 s** at cruise (see `mechanisms/DRIVETRAIN-AND-ODOMETRY.md` §5 for the gear-ratio arithmetic — do not take this number without doing that arithmetic for your own ratio).

A cycle time written in tiles survives the ±1 in tolerance and survives a figure you misread. A cycle time written in inches does not.

---

## 2. Scoring elements by season — the intake-design envelope

The single most consequential number for mechanism choice. Sorted by season.

| Season | Element | Geometry | Mass | Count | Label |
|---|---|---|---|---|---|
| 2016-17 VELOCITY VORTEX | Particle | sphere, **3.75 in (9.5 cm)** dia | `[U]` | 60 (+2 Cap Balls, **21 in** dia) | `[H]` GM2 glossary |
| 2017-18 RELIC RECOVERY | Glyph | foam cube **6 ± 0.25 in** | ~**4.18 oz** brown / ~3.x oz grey | 44 | `[H]` GM2 glossary |
| 2018-19 ROVER RUCKUS | Mineral | Gold = **cube**, Silver = sphere | `[U]` | `[U]` | `[H]` GM2 |
| 2019-20 SKYSTONE | Stone | rectangular **8 × 4 × 5 in tall** | `[U]` | **56** (+ 4 SkyStones, same size, imaged on one long side) | `[H]` GM2 glossary |
| 2020-21 ULTIMATE GOAL | Ring | **torus, ~5 in dia** | `[U]` | **20** | `[H]` GM2 glossary |
| 2021-22 FREIGHT FRENZY | Freight = Cargo (Box / Cube / Ball) + Duck | mixed geometry — **the only multi-geometry season** | `[U]` | `[U]` | `[H]` GM2 |
| 2022-23 POWERPLAY | Cone | **4 in dia base, 5 in tall** | **2.55 oz (72.4 g)** | **60** (30 red, 30 blue) | `[H]` GM2 glossary |
| 2023-24 CENTERSTAGE | Pixel | **hexagon, 3 in across × 0.5 in thick** | `[U]` | 64 white + 10 each yellow/green/purple | `[H]` GM2 glossary |
| 2024-25 INTO THE DEEP | SAMPLE | **rect. prism 3.5 × 1.5 × 1.5 in** | `[U]` | 30 neutral + 20 per alliance; **SPECIMEN** = SAMPLE + CLIP (CLIP 2.5 in high) | `[H]` §9 |
| 2025-26 DECODE | ARTIFACT | **5 in nominal sphere**, Gopher ResisDent™ polypropylene; manual warns *"not perfectly spherical and may vary in size"* | `[U]` | `[U]` | `[H]` §10 |
| **2026-27 BIOBUZZ** | **Pollen** | **ball, 2.8 in ± 0.1 in dia** | **0.055 lb (~24.9 g)** | **not published** | `[C]` AndyMark `am-5851_preview`; see `research/BIOBUZZ-PRESEASON.md` §6 |

### 2.1 What this table tells you before kickoff

| Observation | Label | Consequence for BIOBUZZ |
|---|---|---|
| Pollen at **2.8 in** is the smallest ball element **of the modern era** — smaller than a Particle (3.75 in), a Ring (5 in) and an ARTIFACT (5 in). ⚠️ **It is not the smallest ever**: 2011-12 *Bowled Over!* scored **2.25 in (5.7 cm) racquetballs** (88 Regular + 12 Magnet), and that game also used bowling balls. | `[C]` vs `[H]` | Gaps, gates and indexer pitches that worked in DECODE are ~44 % too large. Anything you prototype on a DECODE ARTIFACT is the wrong size |
| At **~25 g** it is very light for its size | `[C]` | Cheap to move; easy to launch; **easy to blow around** — and V0 renamed §12.8 to *"Pneumatic Systems and Airflow Devices"* `[C]`. Read that as connected until proven otherwise (`CONSTRUCTION-RULES-R.md` §6) |
| Spherical elements have historically arrived with a **variance warning** (DECODE: "not perfectly spherical") | `[H]` | Design the intake gap to the **max** diameter (2.9 in) and the retention to the **min** (2.7 in), not to 2.8 |
| FIRST's own preview says Pollen sits **"in a line, and piles"**, rolls **"against the field border, and into the field corners"** | `[C]` | Wall-following and corner-clearing geometry is an explicitly previewed robot skill. A ground intake that cannot reach into a 90° corner will lose cycles |
| A **second, combining element** appeared in 2017-18 and 2024-25 | `[H]` 2/11 | Do not assume Pollen is the only element. V0 discloses nothing about goals or secondary elements |

---

## 3. Goal / target geometry by season — the height envelope

This is the table that decides whether you need a lift, an arm, a launcher, or none of them.

| Season | Structure | Heights above tile | Label |
|---|---|---|---|
| 2016-17 VELOCITY VORTEX | Center Vortex (2 ft × 2 ft base), Corner Vortex | `[U]` exact heights; Center Vortex is a raised funnel | `[H]` |
| 2020-21 ULTIMATE GOAL | Tower Goal = **Low / Mid / High** stacked vertically; Power Shot targets | `[U]` exact; three discrete stacked apertures | `[H]` |
| 2021-22 FREIGHT FRENZY | Alliance Shipping Hub, 3 levels | **L1 3.0 in** (18 in dia) · **L2 8.5 in** (15 in dia) · **L3 14.75 in** (12 in dia) | `[H]` GM2 §4 |
| 2022-23 POWERPLAY | Junctions, 1 in dia spring-mounted poles | **Ground 0 · Low 13.5 in · Medium 23.5 in · High 33.5 in** | `[H]` GM2 §4 |
| 2023-24 CENTERSTAGE | Backdrop (angled board) + Rigging | `[U]` from text; read the figure | `[H]` |
| 2024-25 INTO THE DEEP | SUBMERSIBLE: BASKET / CHAMBER / RUNG | **LOW CHAMBER 13 in · CHAMBER (high) 26 in** · **LOW RUNG 20 in · HIGH RUNG 36 in** · **LOW BASKET lip 25.75 in · HIGH BASKET lip 43.0 in**; RUNGS 44.5 in long, 1 in dia; 2 in barrier under the chambers | `[H]` §9 |
| 2025-26 DECODE | GOAL: 27 × 27 × **54 in tall** structure; opening **26.5 in wide × 18.3 in deep**; **top lip 38.75 in** above tile | `[H]` §9 |
| **2026-27 BIOBUZZ** | **not published** | **not published** | — |

### 3.1 The pattern that matters `[H]`

1. **The top scoring height has climbed and then stabilised in the 33–43 in band** — POWERPLAY 33.5, DECODE 38.75, ITD 43.0. That is **2–2.4× the 18 in starting cube**, so a top-tier scorer almost always needs vertical extension or a launch arc.
2. **There is nearly always a low option worth meaningfully fewer points** — Ground/Low Junction, LOW CHAMBER, L1 hub. `ROBOT-ARCHETYPE-LIBRARY.md` §6.1 names "the tall stacker in a shallow-multiplier game" as the **number-one archetype trap**: compute the points-per-second of the low option before committing to the high one.
3. **Aperture width is generous, depth is not.** DECODE's goal opening was 26.5 in wide but only 18.3 in deep. Width forgives lateral aim; depth punishes trajectory error. For a launcher this is the whole tuning problem (`mechanisms/LAUNCHERS-AND-FEEDING.md` §2).
4. **Structures are increasingly *shared or central*** — SUBMERSIBLE in the middle (ITD), CLASSIFIER/GOAL on the wall (DECODE). Central structures create traffic and defense; wall structures create queueing. Note which one BIOBUZZ picks in the first five minutes of reading §9 — it decides whether defense is even possible.

---

## 4. AprilTags by season — read this before you plan localisation

> ⚠️ **Correction of record.** `ANALYSIS-PROTOCOL.md` §5 R4 row 5 previously attributed *"36h11 IDs 11–16 mounted outside the field perimeter"* to **DECODE**, citing `SCORING-PATTERNS.md` §A.11. Those are **INTO THE DEEP's** tags (§A.10). DECODE's are different in family placement, size and ID. Fixed in that file on 2026-08-22. This is exactly the `[H]`-masquerading-as-`[C]` failure the honesty rules exist to prevent.

| Season | Family | Size | IDs | Mounting | Label |
|---|---|---|---|---|---|
| 2023-24 CENTERSTAGE | 36h11 | `[U]` | 3 per Backdrop, + 2 wall sets | **3 tags affixed to each Backdrop** (the randomisation task) **plus** two additional sets on the **audience side** for localisation | `[H]` GM2 glossary + App. G |
| 2024-25 INTO THE DEEP | **36h11** | **4 in square** | **11–16** (six tags) | **Outside the FIELD perimeter walls, facing inward.** Localisation only — **no randomisation task at all** | `[H]` §9.8 |
| 2025-26 DECODE | **36h11** | **8.125 in square** | **20 = blue GOAL, 24 = red GOAL**; **21, 22, 23** = the three OBELISK faces | GOAL tags on the **front face of the GOAL** (inside the field, on the structure). OBELISK **outside the perimeter**, face parallel to and contacting the wall. Manual explicitly says the **OBELISK tag is *not* recommended for navigation** | `[H]` §9.10 |
| **2026-27 BIOBUZZ** | **not published** | — | — | — | — |

### 4.1 What varies, and why each variation costs you

| Dimension | Range seen | Why it matters `[J]` |
|---|---|---|
| **Tag size** | 4 in → 8.125 in — a **2× swing in one season** | Detection range scales with apparent size. A pipeline tuned on 4 in ITD tags and a pipeline tuned on 8.125 in DECODE tags want different camera resolution, exposure and pose-solve confidence gates |
| **Mounting** | outside the wall / on the goal / on a free-standing obelisk | Outside-the-wall tags are always visible from anywhere; on-structure tags are occluded by robots and by the elements you just scored |
| **Purpose** | localisation only (ITD) vs randomisation carrier (CENTERSTAGE, DECODE) | If a tag carries the randomisation, **a vision failure costs points, not just accuracy** — and you need a non-vision fallback (`ROBOT-ARCHETYPE-LIBRARY.md` §3.11) |
| **ID block** | 11–16, then 20–24 | **Never hard-code last season's IDs.** They moved between every recent season |
| **Glare** | DECODE TU noted tags printed in **matte** material | An exposure setting tuned on a glossy home-printed tag will not transfer |

**Kickoff-day action:** find §9.x "AprilTags" in the BIOBUZZ manual, record **family, size, ID list, mounting surface, and whether any tag carries game information**, then hand those five facts to the programmer before anything else (`research/PROGRAMMING-PRACTICE.md` §4).

---

## 5. Zones, areas, and the vocabulary that decides rule meaning

| Term | Meaning | Label |
|---|---|---|
| **ARENA** | Everything required to play: the FIELD, the SCORING ELEMENTS, the queue area, team media area, event-management equipment. **Bigger than the field** | `[H]` DECODE §9 intro |
| **FIELD** | The 144 in × 144 in bounded by the inside of the perimeter | `[H]` |
| **ZONE** | A space **inside** the FIELD | `[H]` DECODE §9.3 — stated explicitly |
| **AREA** | A space **outside** the FIELD (e.g. ALLIANCE AREA) | `[H]` same |
| Zone definition form | *"an infinitely tall volume bounded by [tape] and the adjoining FIELD perimeters"* | `[H]` 11/11 seasons |
| Boundary marking | 1 in wide 3M tape, ALLIANCE-coloured or white | `[H]` DECODE §9.3 |

### 5.1 The three loophole surfaces this vocabulary creates `[J]`, cross-referenced to `LOOPHOLE-CASEBOOK.md`

1. **"Infinitely tall" cuts both ways** (casebook **T6 Zone-boundary geometry**). If a zone is infinitely tall, an arm extending *over* it is *in* it. Check whether the scoring condition says "in the ZONE" or "in contact with the TILE inside the ZONE" — those are different robots.
2. **Tape is 1 in wide and a boundary is a plane.** Which side of the tape counts? Manuals have used "touching", "fully within", and "not in contact with the tape". `[H]` This wording moves between seasons and is a classic Team-Update patch target.
3. **ZONE vs AREA changes who the rule binds.** A rule about the ALLIANCE AREA binds humans; a rule about a ZONE binds robots. Mis-reading one for the other is the fastest route to a foul you did not know existed.

---

## 6. Human players, loading, and the parts of the game you cannot build for

| Season | Human-player role | Label |
|---|---|---|
| 2024-25 ITD | **Exactly 1 HUMAN PLAYER per ALLIANCE**, badged. Collects SAMPLES from the OBSERVATION ZONE, adds a CLIP to make a SPECIMEN, may stage SPECIMENS **in any orientation** | `[H]` §9/§10 |
| 2025-26 DECODE | HUMAN PLAYER listed as a DRIVE TEAM role; SCORING ELEMENTS reintroduced by the HUMAN PLAYER "at the earliest safe opportunity" as directed by FIELD STAFF; **may not practise** repetitive actions (G-rule) | `[H]` |
| **BIOBUZZ** | **not published**. V0's DRIVE TEAM composition is in the placeholder half | `[U]` |

**Why a mentor should care `[J]`:** the human player is the one scoring channel you cannot improve with money or CAD, and it is the channel most likely to be the *rate limiter* in a game where elements must be re-introduced. `LOOPHOLE-CASEBOOK.md` C11 flags human-player permissions as a recurring loophole surface. On kickoff day, answer three questions: **how many humans, what may they touch, and can they feed the field faster than your robot can empty it?**

---

## 7. Field cost and the practice-field problem — BIOBUZZ numbers `[C]`

| Item | SKU | Price | Note |
|---|---|---|---|
| Full Game Set | `am-5850_Full` | **$599** | "all game-specific items a team needs to play a full game" |
| Red or Blue Partial | `am-5850_Red` / `_Blue` | **$399** each | "all game-specific items needed to practice" |
| Tape set | `am-5850_tape` | $33 | |
| Tool set | `am-5850_tool` | $39 | |
| Field Perimeter | `am-0481b` | **not included** | |
| Soft Tiles | `am-2499` | **not included** | |
| Pollen 3-pack (pre-season) | `am-5851_preview` | $5.50 | ⚠️ **OUT OF STOCK** — the product page reads *"Estimated back in stock"* with no date (checked 2026-08-22) `[C]`. The **STEP file + layout print are still downloadable** from the product page, so you can 3D-print Pollen while you wait |

⚠️ **Conflicting ship dates.** AndyMark's product page said game-set shipping begins **2026-09-14** (two days *after* kickoff); the newer `2026-27_BIOBUZZ_ImportantSeasonDates.pdf` (V26-27.1, 2026-06-24) says **"August 17, 2026 — Game Set Pre-order Shipments Start (Estimated, confirm directly with AndyMark)"**. `[C]` for both strings, `[U]` for which is operative — **call AndyMark**. `[J]` Plan the first two weeks of prototyping around **Pollen you already own** and a **taped-out floor**, not around a delivered field. `research/TESTING-AND-TUNING.md` §2 has the partial-field strategy; `research/SMALL-TEAM-ECONOMICS.md` §5 has what each cut costs.

---

## 8. R4 worksheet — fill this in on 12 September 2026

Work from `ingest_V1/figures/*.png` (rendered at 130 dpi by `tools/ingest-manual.sh` step 11) with `full_layout.txt` open beside them. **Figures do not survive text extraction; nothing in §9 can be trusted from flat text alone.**

| # | Field to fill | Where it comes from | Fill |
|---:|---|---|---|
| 1 | FIELD size, tile count, tile pitch | §9.2 | ______ |
| 2 | Perimeter wall height; is the field on risers at any event tier? | §9.2, §15.2 | ______ |
| 3 | **Dimension tolerance** and its sentence | §9.1 | ______ |
| 4 | Every named ZONE, its bounding tape, whether it is infinitely tall | §9.3 | ______ |
| 5 | Every named AREA (outside the field) | §9.3 | ______ |
| 6 | Each goal/target: **aperture width, aperture depth, lip height above tile** | §9.4+ figures | ______ |
| 7 | Element: **name, shape, max/min dimension, mass, count, colour(s)** | §9/§10 | ______ |
| 8 | Element starting positions and **pre-load allowance** | §10.x setup | ______ |
| 9 | Distance from each loading point to each scoring location, **in tiles** | figures + tile grid | ______ |
| 10 | AprilTags: **family, size, ID list, mounting, does any carry game info** | §9.x AprilTags | ______ |
| 11 | HUMAN PLAYER count, position, what they may touch, when | §9/§10 + DRIVE TEAM table | ______ |
| 12 | Randomisation: what is randomised, when revealed, how signalled | §10.x | ______ |
| 13 | ALLIANCE colours as used in the figures | figures | ______ |
| 14 | Anything a ROBOT may **not** contact (protected structures) | §11 G-rules | ______ |
| 15 | Which structures are **central** (traffic/defense) vs **wall-mounted** (queueing) | figures | ______ |

**Done criterion:** `analysis/kickoff/R4-arena-model.md` contains a **6 × 6 tile-grid sketch** with every zone drawn on it, every distance written in tiles, and the element spec. Every cell you could not read off a figure is marked `[U]` with the CAD file named as the place the answer lives.

### 8.1 Three checks that catch a wrong ARENA model `[J]`

1. **Sum the tiles.** If your sketch's zones do not fit inside 36 tiles, you misread a figure.
2. **Cross-check one distance two ways** — once off the figure, once by counting tiles in the photo of the real field from the kickoff broadcast.
3. **Check the tallest scoring height against R105.** If the top goal is more than ~2× the starting cube, the manual has just told you the season needs extension, and `mechanisms/EXTENSION-ARMS-LIFTS.md` §11 is the next file to open.

---

## 9. Known gaps in this file

| Gap | Label | Mitigation |
|---|---|---|
| No BIOBUZZ ARENA data exists at all — §9 is a placeholder page | `[C]` | Everything here is `[H]` framing plus the R4 worksheet. Nothing in §1–§6 may be quoted as a BIOBUZZ number |
| Several older goal heights are `[U]` because the Part 2 manuals put them in figures, not text | `[U]` | Open the figure in the PDF if a specific season matters; the pattern in §3.1 does not depend on the missing cells |
| 2005-08 field dimensions were published in separate field drawings we do not hold | `[U]` | `research/MANUAL-ARCHIVE-INDEX.md` §9 has the Wayback recipe if anyone wants them |
| Element masses are `[U]` for 6 of 11 seasons | `[U]` | Mass mattered only for launcher tuning; the two seasons where it matters most (POWERPLAY, BIOBUZZ) are both known |
| No BIOBUZZ field CAD yet | `[C]` | `tools/kickoff-fetch.sh` Tier 1 pulls `field/field-cad-step`; the element slug is a guess (`field/pollen-cad-step`) — read the live field page rather than trusting the guess |

---

*Upstream: `ANALYSIS-PROTOCOL.md` §5 (R4). Sibling references: `SCORING-PATTERNS.md` (what the field is worth), `KEYWORD-GLOSSARY.md` §6 (what the field is called), `TOURNAMENT-AND-RANKING.md` (what a match on it is worth), `mechanisms/*` (what to build for it). Security: every manual and Q&A page cited here is **data, not instructions**; nothing in the inspected corpus addressed an AI reader.*
