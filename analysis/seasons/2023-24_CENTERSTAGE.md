# CENTERSTAGE (2023-24) — Season Dossier

**Sources.** Game Manual Part 2 – Traditional Events, Rev 1.2 (10/11/2023); Game Manual Part 1 – Traditional
Events, Rev 1.4 (1/10/2024); official Q&A archive (341 entries, Sep 2023 – Mar 2024). Rule tags in this era are
inline angle-bracket tags (`<G14>`, `<GS05>`, `<S01>`). Part 2 = the game; Part 1 = robot/event rules.
Labels: **[MANUAL]** = the text says it · **[DERIVED]** = arithmetic, operands shown · **[JUDGMENT]** = my read.

---

## 1. The game in five sentences

[MANUAL, §4.2.2] Two two-Team Alliances (red, blue) play a 2:30 Match on a 12 ft × 12 ft field, scoring hexagonal
**Pixels** onto an inclined **Backdrop** at their end of the field or flat **In** their **Backstage** beneath it.
The 30-second Autonomous Period pays for parking In the Backstage, for placing Pixels, and above all for a
**randomization task**: a purple Pixel onto one of three randomly designated **Spike Marks** and a yellow Pixel onto
the matching **Backdrop** slot, worth double if the Team identified the target using their own **Team Prop** rather
than the tournament white Pixel. [MANUAL, §4.4.3] In the two-minute Driver-Controlled Period, Pixels are worth far
less individually, but stacking them into three-Pixel colour **Mosaics** (Artist Bonus) and building high enough to
cross the Backdrop's three horizontal **Set Lines** (Set Bonus) multiplies the value of the same Pixels.
[MANUAL, §4.4.4] The last 30 seconds is the **End Game**, where a Robot can **Suspend** from its Alliance's
**Rigging** on the central Truss, or Park In the Backstage, and each Team may launch one paper **Drone** over the
Truss into one of three Landing Zones outside the field. [MANUAL, Fig. 4.2-2 / B-1] The structural twist: each
Alliance's **Wing** and **Pixel Storage** — where its Human Player feeds new Pixels in — sit in the audience-side
corner *diagonally opposite* that Alliance's own Backstage, so every teleop cycle is a full cross-field run past a
height-restricting **Stage Door**.

---

## 2. Match structure

| Period | Length | Notes |
|---|---|---|
| Pre-Match setup | — | [MANUAL, §4.4.1] Robots Completely In Tile A2/A4 (blue) or F2/F4 (red), touching the Wall adjacent to their Alliance Station; may Pre-Load exactly one yellow and/or one purple Pixel, plus one Drone. |
| Randomization | — | [MANUAL, §4.4.1.4.c] After referees signal setup complete, the Scoring System picks left/center/right; field personnel move the Randomization Object. Drive Teams are hands-off from this moment (`<GS02>`). |
| **Autonomous** | 0:30 | [MANUAL, §4.4.2] Pre-programmed only; the built-in 30-second timer must remain enabled (§4.4.1.3.f). |
| Transition | 0:08 total (5 s hands-on + "3-2-1-go") | [MANUAL, §4.3 *Match*, `<G01>`] Field personnel do not enter the field. |
| **Driver-Controlled** | 2:00 | [MANUAL, §4.4.3] |
| **End Game** | final 0:30 of Driver-Controlled | [MANUAL, §4.4.4] Not a separate period — teleop scoring continues throughout. |
| **Total** | **2:30** | [MANUAL, §4.3 *Match*] |

**Vs. the prior season.** [JUDGMENT] The 2:30 skeleton, the 0:08 transition and the 30-second End Game are the
standard 2020-21→2023-24 shape; nothing in the Part 2 revision history (Rev 1 → 1.2) touches period lengths.
CENTERSTAGE is the **last** season of the split Part 1 / Part 2 manual and of the Traditional/Remote fork — 2024-25
consolidated into a single "Competition Manual". A Part 2 – Remote Events edition shipped (41 rules: G:26, GS:12,
S:3) in which Teams play Matches as a single Team and Ranking Points are the Team's own final Match score rather
than 2/1/0 for win/tie/loss (Part 1 §3.4). [MANUAL]

---

## 3. Scoring table

Source: §4.6 Scoring Summary table, recovered **by geometry** (`tools/extract-tables.py`, PDF p.30) and
independently cross-checked line-by-line against the prose in §4.4.2 / §4.4.3 / §4.4.4. The `pdftotext -layout`
rendering of this same table is scrambled — row labels and values land on different lines (see §9).

| Scoring achievement | AUTO | TELEOP | END GAME | Cite |
|---|---:|---:|---:|---|
| Navigating: Robot Parked In its Alliance's Backstage | **5** (per Robot) | — | — | §4.6 tbl; §4.4.2.1 |
| Placement: Pixel On its Alliance's Backdrop (recessed scoring area) | **5** /Pixel | **3** /Pixel | — | §4.6 tbl; §4.4.2.3.a; §4.4.3.1.a |
| Placement: Pixel In its Alliance's Backstage | **3** /Pixel | **1** /Pixel | — | §4.6 tbl; §4.4.2.3.b; §4.4.3.1.b |
| Randomization: purple Pixel On designated Spike Mark — **white Pixel** used | **10** | — | — | §4.6 tbl; §4.4.2.2.a.i |
| Randomization: purple Pixel On designated Spike Mark — **Team Prop** used | **20** | — | — | §4.6 tbl; §4.4.2.2.a.ii |
| Randomization: yellow Pixel On matching Backdrop location — **white Pixel** used | **10** | — | — | §4.6 tbl; §4.4.2.2.b.i |
| Randomization: yellow Pixel On matching Backdrop location — **Team Prop** used | **20** | — | — | §4.6 tbl; §4.4.2.2.b.ii |
| Artist Bonus: completed Mosaic | — | **10** /Mosaic | — | §4.6 tbl; §4.4.3.2 |
| Set Bonus: Scored Pixels extend In a Backdrop Set Line | — | **10** /Set Line (max **30**) | — | §4.6 tbl; §4.4.3.3 |
| Robot Location: Suspended from its Alliance's Rigging | — | — | **20** | §4.6 tbl; §4.4.4.1.a |
| Robot Location: Parked In its Alliance's Backstage | — | — | **5** | §4.6 tbl; §4.4.4.1.b |
| Drone Launch — Landing Zone 1 / 2 / 3 | — | — | **30 / 20 / 10** | §4.6 tbl; §4.4.4.2.a–c |
| Minor Penalty (to the **non-offending** Alliance) | 10 | 10 | 10 | §4.4.6 |
| Major Penalty (to the **non-offending** Alliance) | 30 | 30 | 30 | §4.4.6 |

**Timing method.** [MANUAL, §4.3 *Score*; §4.6] Everything is **Scored at Rest** (position after the field settles at
the end of the period) *except* End Game Robot Location, which is **Scored at End of the Period**.

### Stacking rules that change the arithmetic

- **Auto Pixels are paid twice.** [MANUAL, §4.4.2.3] "Pixels that are Scored in the Autonomous Period will earn
  additional points at the end of the Driver-Controlled Period if they remain in place." [DERIVED] An auto Backdrop
  Pixel left in place = 5 (auto) + 3 (teleop) = **8**; an auto Backstage Pixel = 3 + 1 = **4**.
- **The randomization yellow Pixel stacks with placement.** [MANUAL, Q&A Q58, Q208] Placement 5 + Randomization 20
  (Team Prop) = **25 in Autonomous** for a single Pixel, plus 3 more at the end of teleop if it stays → **28 points
  from one Pixel** [DERIVED: 5 + 20 + 3].
- **`<G05>` collapses overlaps.** [MANUAL, `<G05>`; Q&A Q58] Where two achievements apply, only the highest counts.
  The three CENTERSTAGE cases named by the GDC: a Pixel both On the Backdrop and In the Backstage (Backdrop wins);
  a Robot both Suspended and Parked In the Backstage (Suspend wins, 20 > 5); a Drone In two Landing Zones.
- **Descoring is multi-count.** [MANUAL, `<GS04>`; Q&A Q88/Q99] Each Pixel descored from an opponent's
  Backdrop/Backstage = one Minor Penalty, **plus one additional Minor Penalty per affected Mosaic and per affected
  Set Line**. Two Pixels that also break one Mosaic and one Set Line = 4 Minor Penalties = 40 points.

### Ceiling arithmetic [DERIVED]

- Autonomous, pre-loads only, both Robots perfect with Team Props:
  2 × 5 (Navigate) + 2 × 20 (purple/Spike) + 2 × (20 + 5) (yellow/Backdrop) = **100**. Every additional white Pixel
  moved to the Backdrop in auto adds 5.
- End Game ceiling per Alliance: 2 × 20 (Suspend; `<GS06>`c caps one Robot per Rigging, and each Alliance has two
  Riggings) + 2 × 30 (two Drones, one per Team) = **100**.
- Mosaic ceiling per Alliance: Pixel Storage holds 5 purple + 5 yellow + 5 green = 15 non-white Pixels → at most
  5 Mosaics → **50** Artist Bonus points. (Pixel inventory checks out: 2 × 15 non-white = 30 = 10 + 10 + 10 ✓;
  2 × 15 white in storage + 6 stacks × 5 on field + 4 randomization = 64 white ✓ — §4.3 *Pixel*, §4.4.1.2.)

---

## 4. Bonuses, randomization and ranking

### The randomized objective

[MANUAL, §4.4.1.2.c, §4.4.1.4.c, §4.3 *Randomization Object* / *Spike Mark*]
Four **Randomization Objects** start centred on the **center** Spike Mark, one opposite each Robot (Spike Marks live
in Tiles B2, B4, E2, E4 — three per Tile: left, center, right from that Alliance Station's view). After Robots are
set and Drive Teams are hands-off, the Scoring System selects left / center / right and **field personnel physically
move the object** to the chosen mark. The reveal is therefore *physical and pre-Match*, not mid-Match — the Robot
must detect it with vision or sensors during Autonomous.

The clever part: [MANUAL, §4.4.1.3.d] a Team may swap the tournament white Pixel for its **own Team Prop** (a
Team-built 3–4 in. cube, `<TE04>`, entirely red or blue, no fiducial markers or retroreflective material, `<TE02>`/
`<TE03>`) — and doing so **doubles** both randomization awards (10 → 20 each). [JUDGMENT] This is a rare FTC design
where a Team *pays for its own detection problem to be easier* and is paid 20 extra points per task for the
privilege. [MANUAL, §4.2.3] The manual offers built-in TensorFlow for decoding the task and AprilTags (three per
Backdrop, plus two wall sets) for localisation.

[MANUAL, Q&A Q53] Each Spike Mark location (left/center/right) has **two** valid Backdrop slots, so both Robots on
an Alliance can score the yellow randomization task at the same designated location. [MANUAL, Q&A Q131/Q217] A yellow
Pixel balanced on the crest *between* two slots is not touching a valid AprilTag scoring surface — no randomization
points, only the 5-point placement. [MANUAL, Q&A Q243] The Randomization Object itself has no end-of-Autonomous
position requirement; knocking your own Team Prop off the tape does not void the purple Pixel.

### Bonus mechanics

- **Artist Bonus / Mosaic** [MANUAL, §4.3 *Mosaic*, §4.4.3.2, Fig. F-2/F-3]: three non-white Pixels On a Backdrop,
  either all one colour or one each of green/purple/yellow; each Pixel must touch the other two; the completed
  Mosaic must not touch any other non-white Pixel. 10 points each. [MANUAL, Q&A Q245] Pixels need not be tessellated
  — angled contact counts. [MANUAL, Q&A Q222] A Mosaic does not need to be surrounded by white Pixels.
- **Set Bonus** [MANUAL, §4.4.3.3, §4.3 *Set Line*, Fig. F-4]: three horizontal Set Lines on each Backdrop at
  approximately **12⅜ in, 19 in and 25¾ in** vertically off the Tile surface (Fig. C-3). Scored Pixels that
  *vertically cross* a Set Line earn 10 — once per line regardless of how many Pixels cross it — capped at 30.
- **No ownership / multiplier mechanic.** [MANUAL] CENTERSTAGE has no zone ownership, no score multiplier and no
  end-of-match multiplier. The only multiplier-like levers are Mosaic, Set Bonus and the Team Prop doubling.

### Ranking (Part 1 §3.4, §5.1.1)

| | Traditional Events |
|---|---|
| **Ranking Points (RP)** | Win 2 · Tie 1 · Loss / DQ / no-show 0 |
| **TBP1** | Alliance's **Autonomous Period** score for that Qualification Match |
| **TBP2** | Alliance's **End Game specific task** score for that Qualification Match |
| **Sort order** | 1. Avg RP ↓ 2. Avg TBP1 ↓ 3. Avg TBP2 ↓ 4. Highest Match Score (incl. Penalties) 5. Random electronic draw |

[MANUAL] Averages are over Matches played; Surrogate / DQ / no-show Matches contribute zero and Surrogates are
excluded from the average. [JUDGMENT] Note what this rewards: **both tiebreakers are the two 30-second windows**,
not the two-minute teleop. A Team that maxes Autonomous and End Game and does nothing else ranks above a teleop
cycling machine at equal RP. Remote Events instead used the Team's own final Match score as RP (Part 1 §3.4).

---

## 5. The rules that shaped play

Full inventory: 47 game-side rules — Safety `<S01>`–`<S04>`, General `<G01>`–`<G30>`, Game-Specific
`<GS01>`–`<GS13>`. Penalty tiers (§4.4.6): **Minor = 10 pts to the opponent, Major = 30 pts to the opponent**;
Warnings score nothing. Table key from §4.7: `W` warning · `D` disable · `1x` single-cost · `1x+` single cost every
5 s · `YC`/`RC` cards · `*` optional.

### Game-Specific rules (the ones that defined CENTERSTAGE)

| Rule | Threshold / mechanic | Consequence [§4.7 rule-summary table] |
|---|---|---|
| `<GS02>` | Touching Robot/Driver Station after randomization begins | Minor + that Robot ineligible for **all** Randomization Task points (partner unaffected) |
| `<GS03>`a | Interfering with an opponent Robot In the opponent's half during Auto (A/B/C = blue, D/E/F = red; C-D tabs neutral) | **Major** per offense |
| `<GS03>`b | Interfering with opponent randomization setup or scoring | **Major** per offense |
| `<GS03>`c | Moving pre-placed white Pixel stacks in the opponent's half so as to impede their Auto scoring *(added Rev 1.2)* | **Major** |
| `<GS04>`a/b | Descoring from opponent Backdrop/Backstage | Minor **per Pixel**, **plus** an extra Minor per affected Mosaic and per affected Set Line |
| `<GS05>`a | Control/Possess > **2 Pixels** or > **1 Drone** | Minor per excess element, **repeating every 5 s** (`1x+`) |
| `<GS05>`b | Scoring while over the limit | Minor per Pixel scored |
| `<GS05>`c | Exemptions: knocking a stack over; Inadvertent stack movement (moving 3+ stacked Pixels *Completely Off* the tape is consequential); Plowing; Pixels In the Backstage supported by the floor; **Pixels On the Backdrop** | — |
| `<GS06>`a | Grasp only one of your own Riggings; other Truss contact allowed for stabilisation only | **Zero score for the Suspend** (no penalty) |
| `<GS06>`b | Grasping/Suspending from any other Truss part | Minor per occurrence |
| `<GS06>`c | One Supported Robot per Rigging | **Major** for the second Robot |
| `<GS06>`d | Impeding an opponent's Suspend during End Game | Immediate **Major** + `<G28>` blocking penalties |
| `<GS06>`e | Contacting a Suspended opponent | Minor per occurrence (the Suspend still counts) |
| `<GS07>`a/b | Grasping the Stage Door; preventing its normal operation | **Major** each |
| `<GS07>`c | Transit: audience-side→back has **priority**; back→audience must yield | `<G28>` handling: Minor every 5 s, escalating to YC |
| `<GS08>`a/b | Impeding a Robot In the Backstage / Blocking access to opponent Backstage or Backdrop | Minor each / **Major + Minor every 5 s** until 3 ft (≈1.5 Tiles) away |
| `<GS08>`c | A **Disabled** Robot In the opponent's Backstage still earns `<GS08>` penalties — explicit exception to `<G07>` | — |
| `<GS08>`d | **Robots In Tile rows 1, 2 or 3 may not Score into the Backstage or Backdrop** | Minor per offense |
| `<GS09>`a/b/d | Wing: impeding (Minor); being In / Blocking the opponent's Wing (**Major** + Minor every 5 s); **max 6 Pixels In a Wing** (Minor per excess) | as noted |
| `<GS10>` | **Pixels may not be Propelled** | Minor per offense |
| `<GS11>` | Drones: launched before End Game score 0 (no penalty); must pass over a Rigging or the Stage Door top pole **per attempt**; may be launched from a Suspended Robot; must be in inspected configuration; must Park **Completely Outside** the Playing Field Perimeter *(h added Rev 1.2)*; possessing another Team's Drone = **Major** | as noted |
| `<GS11>`g | Interference: knocking down an opponent's Drone flying above Wall height (~11.5 in) → **that Drone is awarded Landing Zone 1 (30)**, no penalty points; a Drive Team affecting its own Drone → 0 for that Drone; a Drone touching field personnel In a Landing Zone → LZ1 value, Outside a Landing Zone → 0 | as noted |
| `<GS12>` | Human Player: place only In the Wing, only during teleop; **max 2 Pixels or 1 Drone per action**; no repositioning once placed; no propelling; no tools; may not break the field plane while a Robot is In the Wing; a Robot may not enter an occupied Wing | Minor each |
| `<GS13>` | Drive Team stepping/jumping over Truss or Stage Door | Warning → YC → `<G30>` |

### General rules that mattered

- `<G14>` **18 in × 18 in × 18 in starting volume**; flexible materials may exceed by 0.25 in; a Pre-Loaded Scoring
  Element may protrude. Unfixed in 30 s → Robot removed from the field (no delay-of-game penalty, RP still earned).
  **After the Match starts the Robot may extend in any direction** unless a GS rule says otherwise. [MANUAL]
- `<G28>` Pin/Trap/Block: Minor **every 5 seconds** until the offender has moved 3 ft (≈1.5 Tiles) away. During
  Autonomous it is only penalised if the referee judges it a deliberate strategy — but the offender's *first*
  teleop action must be to move away. [MANUAL]
- `<G29>` Illegal use of Game Elements to ease or amplify a scoring activity: **Major**, escalating to YC.
  [MANUAL, Q&A Q86] The GDC used `<G29>` to make it illegal to place a Pixel On the **opponent's** Backdrop, on the
  grounds that it amplifies the difficulty of their Mosaic — closing an obvious griefing hole that `<GS04>`
  (descoring) did not cover.
- `<S02>` Contact Outside the Playing Field Perimeter = immediate YC + optional Disable — except
  [MANUAL, Q&A Q101] when applying `<S02>`, **the Perimeter is treated as extended outward to include the Backdrop
  boundary**, because the upper Backdrop physically overhangs the wall and is otherwise unreachable.
- `<G07>` Disabled Robots earn no points and no penalties — with three explicit GS carve-outs (`<GS07>`,
  `<GS08>`c, `<GS09>`c), so a dead Robot parked in the opponent's Backstage or Wing is still penalised. [MANUAL]

---

## 6. Robot archetypes that season

Build envelope [MANUAL, Part 1 §7]: `<RG02>` 18-inch cube at start (expansion unlimited after the start,
`<G14>`); `<RE09>` **max 8 DC motors**; `<RE10>` **max 12 servos** (≤6 V); `<RE03>` exactly one 12 V battery with a
20 A in-line fuse; `<RG06>`/`<G24>` no detaching parts; `<RG07>` a propelled scoring element must not travel more
than 18 ft in the air or rise more than 5 ft. No robot weight limit appears anywhere in Part 1 §7 — and the GDC
confirmed the Truss was designed for a "maximum weight" Robot [MANUAL, Q&A Q38].

Field geometry the mechanism had to hit [MANUAL, Figs. C-1..C-6]:

| Target | Dimension |
|---|---|
| Backdrop inclination | ~30° from vertical, ~35 in tall face (C-2) |
| Lowest / highest Pixel row centre | ~7¼ in / ~29¾ in above the Tile (C-2) |
| Set Lines | ~12⅜ in, ~19 in, ~25¾ in above the Tile (C-3) |
| Rigging | ~23½ in Tile-to-top, 1 5/16 in OD pipe (C-6) |
| Stage Door (lowest position) | ~14 in Tile-to-bottom-of-pipe; opens toward the field rear; ~46¼ in span (C-5, C-6) |
| Backstage | ~23⅛ in deep × ~72 in long (§4.3, C-1) |
| Playing Field Wall | ~12 in tall (§4.3) |

**Archetypes [JUDGMENT], each tied to the rule that forces it:**

1. **The two-Pixel cycler (the baseline everyone built).** `<GS05>`a caps Control at 2 Pixels, so intake capacity
   beyond two is wasted; the workable design was a shallow two-slot intake plus a wrist/arm able to present two
   Pixels flat against a 30°-tilted surface. Because `<GS10>` bans propelling and Q&A Q152/Q158 hold that you may
   only eject "with no more energy than needed to gently place" a Pixel that is already touching the Backdrop, a
   shooter was never viable — deposition had to be contact-based.
2. **The tall placer.** Reaching Set Line 3 at ~25¾ in and the top Pixel row at ~29¾ in from an 18-inch cube means
   a lift or 4-bar with ~12+ in of travel *and* the ability to tip the payload to ~30°. `<G14>`'s post-start
   unlimited extension made this cheap; the real constraint was reaching over a ~12 in wall onto an overhanging
   Backdrop without tripping `<S02>` (resolved in the Team's favour by Q101).
3. **The under-the-door chassis.** The Stage Door's lowest pipe sits ~14 in off the Tile. A robot that fits under
   it, or can nose the hinged door up, crosses the field on the short diagonal; a tall one must go around the Truss
   ends. Combined with the Wing sitting *diagonally opposite* your own Backstage, drivetrain speed and door-transit
   behaviour were worth more than they look — and `<GS07>`c hands right-of-way to whoever is travelling
   audience-side→back, so yielding discipline was a real driver skill.
4. **The suspender.** 20 points for hooking a 1 5/16 in OD pipe at ~23½ in. Q&A Q94/Q271/Q348 policed this hard:
   bracing on the yellow height-restricting bars is legal *only if the Rigging bears the primary vertical load* —
   a robot that would fall to the floor if the yellow bar vanished scores zero (`<GS06>`a). Passive hooks that
   engaged as the robot drove or lifted under the Rigging were the low-risk answer.
5. **The drone launcher.** A paper airplane (`<DR05>`: one continuous sheet ≤ 8½×11 / A4, ≤ 20 lb paper, no card
   stock, pen/marker/printer colour only) fired over the Truss into LZ1 for 30 points. Cheap in motors — typically
   one servo-released rubber-band or spring latch — and the highest points-per-gram mechanism in the game.
   Constraints: `<RG07>` ≤ 18 ft flight, `<GS11>`e must clear a Rigging or the Stage Door top pole, `<GS11>`f the
   Drone must fly in its inspected configuration (Q220: folded wings are fine in the launcher **only if** they
   deploy on release), `<GS11>`h must Park completely outside the Perimeter.
6. **The Team Prop vision stack.** A 3–4 in solid red or blue cube (`<TE04>`, `<TE02>`), deliberately unlike any
   COTS game element (`<TE07>`), no fiducials or retroreflectors (`<TE03>`). Teams built a prop their colour-blob
   or TensorFlow pipeline could resolve at range in three positions — 40 extra points per Alliance for a build
   task with no motors in it.

---

## 7. The strategic lesson

**The 30-second windows were mispriced against the two-minute one, and the manual told you so twice.**

[DERIVED] Do the per-second arithmetic from §3. A perfect two-Pixel Backdrop cycle in teleop pays 3 + 3 = **6
points**. One Robot's End Game — Suspend (20) + Drone into LZ1 (30) — pays **50 points**, and neither task is
contested for time because teleop scoring continues around them. That is **8.3 perfect cycles** [50 ÷ 6] to match
what one robot earns in the last 30 seconds. Meanwhile a single Autonomous yellow Pixel, delivered by a Team-Prop
pipeline into the correct Backdrop slot, is worth **28** [5 + 20 + 3 — MANUAL Q&A Q58/Q208], i.e. **4.7 teleop
cycles** [28 ÷ 6] for one Pixel placed in the first ten seconds of the Match. Both ranking tiebreakers
(TBP1 = Autonomous, TBP2 = End Game) point at exactly the same two windows.

**The underpriced objective: the Team Prop.** [JUDGMENT] It doubles both randomization awards — 40 points per
Alliance — for a build that consumes no motors, no servos, no size budget and no match time, and whose only cost is
a vision pipeline you needed anyway to find the white Pixel. Teams that treated the Team Prop as optional
decoration left the single cheapest 40 points in the game on the table.

**The "obvious" strategy that underperformed: Mosaic-chasing.** [JUDGMENT, arithmetic MANUAL] A Mosaic pays 10 for
three non-white Pixels: 3 × 3 + 10 = **19** versus 9 for three plain Pixels — a real 10-point gain, but it demands
(a) that all three touch each other, (b) that the finished cluster touch **no other non-white Pixel** (§4.3
*Mosaic* cl. 2), and (c) placement precision on a 30° inclined hex grid under time pressure. The whole strategy is
inventory-capped at 5 Mosaics = 50 points per Alliance [DERIVED: 15 non-white Pixels in Pixel Storage ÷ 3]. Worse,
it is fragile: `<GS04>` compensates you 10 points per broken Mosaic, but a Mosaic you *never complete* because a
partner's Pixel landed against it pays nothing at all. Set Bonus is the better-behaved sibling — capped at 30, but
earned once per line by *any* Pixel crossing it, with no colour or adjacency conditions.

**The genuine ambiguities, measured by Q&A volume.** Of 341 archived Q&A entries, the rules that generated the most
distinct threads were `<GS05>` (22), `<GS03>` (18), `<GS10>` (12), `<GS11>` (11), `<GS06>` (10), `<GS09>` (9). Two
deserve to be recorded:

- **`<GS05>` possession, 22 threads.** The 2-Pixel limit collided with a field pre-set with 5-Pixel stacks. The GDC
  had to build, by ruling, a whole exemption lattice: a third Pixel briefly intaken and immediately ejected is
  excused under `<G10>` **only if** the Robot stops playing the game while ejecting it (Q2); knocking Pixels off a
  stack is free in any quantity (Q5); moving 3+ stacked Pixels *Completely Off* the tape is a violation but moving
  one is not (Q5); Pixels On the Backdrop are exempt (Q150) — but **lift one back off the Backdrop while holding
  two and you are instantly at three**, with a Minor every 5 s (Q124); a claw that grabs the top and bottom of a
  stack is Controlling all five (Q190). [JUDGMENT] A possession limit whose edge cases need 22 rulings is a limit
  set below the granularity the field naturally hands the robot.
- **`<GS03>` Autonomous interference, 18 threads — and an admitted exploit.** The GDC ruled that *indirect*
  interference counts: knocking over the opponent's Pixel stacks (Q32), pushing your Team Prop into their half
  (Q173), even placing a Pixel that later obstructs them — all Major, no robot-to-robot contact required. Rev 1.2
  added `<GS03>`c to say so in the manual. But in **Q353 (Mar 2024)** a team pointed out that one Major Penalty is
  **30 points** while wrecking a strong opponent Autonomous denies **45+**, and that intent versus a software bug
  is unprovable. The GDC's answer: the single penalty is correct, additional consequences based on what the victim
  *might* have scored are not possible, and they consider the balance fair. [JUDGMENT] That is an acknowledged,
  unfixed negative-EV asymmetry — at the top of the field a "misprogrammed" auto that crossed the centre line was
  mathematically cheaper than letting the opponent run theirs. Note what actually deterred it: not the point math
  but `<G30>` egregious-behaviour cards, i.e. referee judgment rather than the score sheet.

---

## 8. Signals for BIOBUZZ (2026-27)

1. **Price the periods before the tasks.** Build the points-per-second table for Auto / one teleop cycle / End Game
   on kickoff day. CENTERSTAGE's End Game paid ~50 pts/robot in 30 s against ~6 pts per teleop cycle; if BIOBUZZ
   shows a similar gap, the End Game mechanism is the first thing to prototype, not the last.
2. **Read the tiebreakers as the GDC's own strategy hint.** TBP1 = Autonomous score and TBP2 = End Game score told
   teams exactly where FIRST thought the value was. Extract the ranking sort order on day one and check whether the
   tiebreakers point somewhere the scoring table does not obviously reward.
3. **Hunt for the "pay us to make your task easier" lever.** The Team Prop doubled a scoring achievement in
   exchange for a Team-built, motorless object. Whenever a manual lets a Team substitute its own element for a
   tournament-provided one, check the multiplier — that is usually the season's best points-per-effort ratio.
4. **Look for double-paid scoring.** "Autonomous Pixels will earn additional points at the end of the
   Driver-Controlled Period if they remain in place" is one sentence in §4.4.2.3 that changes every auto-versus-
   teleop trade-off. Grep the new manual for any achievement scored in one period and re-scored in another.
5. **Count the possession limit against the field inventory.** A 2-element cap on a field seeded with 5-element
   stacks generated 22 Q&A threads. On kickoff day, compare the control/possession limit to the natural granularity
   of the scoring elements as pre-set; a mismatch predicts both a mechanism constraint and a referee-risk zone.
6. **Find the diagonal.** CENTERSTAGE put each Alliance's Human Player feed in the corner diagonally opposite its
   own scoring zone, with a height-restricted door in between. Map source→sink travel distance early; it decides
   whether the season rewards drivetrain speed or manipulator throughput.
7. **Model penalty EV explicitly, including where it favours the offender.** Compute (Major Penalty value) versus
   (points denied) for every interference rule. Where the penalty is smaller, expect the behaviour at high-level
   events and expect the manual not to fix it mid-season — Q353 is the precedent.
8. **Bank the geometry numbers before the first CAD.** Scoring-surface heights, inclinations and any
   height-restricting barrier come out of the appendix *figures*, not the text — `tools/render-pages.py` on the
   appendix pages is a five-minute job that de-risks the whole mechanical design.

---

## 9. Extraction notes

**Tooling used.** `tools/parse-legacy-manual.py` (angle-bracket tags — correct for this era; `reference/ftc_parse.py`
returns rules=0 on this manual), `tools/extract-tables.py` (pymupdf geometry) for §4.6 and §4.7,
`tools/render-pages.py` for the Appendix B/C/F figures.

### Rule counts by prefix

| Manual | Rules | By prefix | Tag occurrences | Bodies with a Violation/Penalty line |
|---|---:|---|---:|---:|
| Part 2 – Traditional (57 pp) | **47** | `G`:30 · `GS`:13 · `S`:4 | 153 | 20 |
| Part 2 – Remote (for contrast) | **41** | `G`:26 · `GS`:12 · `S`:3 | — | 22 |
| Part 1 – Traditional (76 pp) | **98** | `C`:29 · `RE`:16 · `I`:10 · `RS`:10 · `DS`:8 · `RG`:7 · `TE`:7 · `RM`:6 · `DR`:5 | 222 | 1 |

**Completeness check: clean.** Part 2's 47 tags are exactly `S01`–`S04`, `G01`–`G30`, `GS01`–`GS13` — no gaps, no
false positives. Part 1's prefix runs are likewise contiguous (`RG01`–`RG07`, `RE01`–`RE16`, `RM01`–`RM06`,
`RS01`–`RS10`, `TE01`–`TE07`, `DR01`–`DR05`).

**The violation-line count is a bad proxy — use §4.7 instead.** The parser's 20/47 undercounts badly: its
`VIOLATION` regex only searches the ≤400-character body window, so rules whose consequence sits past a bullet break
or a blank line are missed. `G12`, `G15`, `G26`, `G28`, `G30`, `GS04`, `GS05`, `GS06`, `S01` and `S03` all carry
explicit consequences in the manual but scored empty. The **§4.7 Rule Summary table**, recovered by geometry
(PDF pp. 31–36), is the reliable source: **74 rows covering all 47 rule tags, of which 68 carry a Consequence
cell**. The 6 rows with no consequence are genuinely definitional: `G01`, `G02`, `G04`, `G08`, `G09`, `GS01`.

### Things the tooling got wrong on this manual

1. **`parse-legacy-manual.py --tsv` never writes the file.** `pdfs = [a for a in argv if not a.startswith("-")]`
   is evaluated *before* `take("--tsv")` strips the flag, so the TSV path is swallowed into the PDF list; the run
   reports `### MISSING <tsv path>` and, because `len(pdfs) != 1`, silently skips the TSV write. This is not
   path-specific — any TSV/JSON path not beginning with `-` triggers it, so `--tsv` / `--json` are broken for all
   inputs. Worked around by importing `parse()` / `report()` directly. **Fix: move the `take()` calls above the
   `pdfs` construction.**
2. **`<GS05>`'s body was captured from the wrong occurrence.** The dedup heuristic keeps the occurrence with the
   longest trailing text; for `GS05` that selected a row of the §4.7 summary *table*, yielding the 52-character
   fragment `"b setup or Scoring. Autonomous Period Scoring actions. 1x"` instead of the real §4.5.3 rule text. Any
   rule whose summary-table row is longer than its manual paragraph's first 400 characters is at risk.
   **Suggested fix: prefer the earliest occurrence followed by prose, or skip pages the table extractor has already
   claimed as tables.**
3. **`pdftotext -layout` scrambles the §4.6 Scoring Summary exactly as the tooling docs warn.** In the flat text,
   the values migrate into the wrong columns — `20`, `5`, `30`, `20`, `10` float in the Reference column while the
   Drone Launch and Suspend/Park rows have no numbers beside them at all. Geometry extraction of PDF p.30 recovered
   every row correctly, and all 13 values were verified a second time against the §4.4.2 / §4.4.3 / §4.4.4 prose.
   **Anyone reading this season from flat text will build a wrong scoring model.**
4. **`extract-tables.py` found no captions.** All 9 tables reported "(no caption on page)". Pre-2024 manuals do not
   use "Table N-M:" captions — tables are untitled and sit under a numbered section heading, while *figures* use a
   different scheme ("Figure 4.2-1", "C-3", "F-4"). The `CAPTION` regex `Table\s+\d+-\d+` cannot match.
   **Suggested fix: fall back to the nearest preceding section heading (e.g. "4.6 Scoring Summary").**
5. **The Drone Launch row merged in geometry extraction.** Row 14 of the p.30 table came out as a single cell pair
   `"Zone 1 Zone 2 Zone 3"` / `"30 20 10"` — correct in order but not split into rows, because the source uses one
   merged cell with three lines. Verified against §4.4.4.2.a–c prose (LZ1 = 30, LZ2 = 20, LZ3 = 10). Any automated
   parse of that cell needs a line-splitting fallback.
6. **The §4.7 rule-summary tables carry phantom empty columns.** On PDF pp. 31–33 the extractor emitted 9–11
   columns where the printed table has 7, inserting an empty column after `Rule #` plus trailing empties. Harmless
   after dropping empty cells, but a naive positional read of column 2 as "Rule" returns blanks.
7. **Revision history is itself a useful table.** The p.3 geometry extraction recovered the Part 2 revision log
   cleanly (flagged `SPLIT?` for an empty first cell — a false alarm; it is a merged header). Rev 1.1 (9/9/23) added
   the Human Player Station to `<G16>` and inserted a new `<GS01>`f; Rev 1.2 (10/11/23) added `<GS03>`c and
   `<GS11>`h, expanded the `<GS04>` descoring examples, corrected the Mosaic definition's figure references, and
   limited Teams to one Drone per Match. Part 1 reached Rev 1.4 (1/10/24). Worth extracting on every manual — it is
   a free list of the season's real ambiguities.
8. **Q&A archive.** 341 entries, Sep 2023 – Mar 2024, extracted cleanly with `pdftotext -layout`. Two caveats: the
   source is an HTML-to-PDF print, so page furniture (timestamp, source URL, "n/52") interleaves with answer text
   and must be filtered; and non-ASCII apostrophes are mojibaked (`Alliance�s`). Entries are delimited by
   `^Q<number> <title>` and split reliably on that pattern.
9. **Figure-only appendices.** Appendices B–G of Part 2 contain no extractable text beyond captions — every
   dimension in §6 of this dossier came from rendering pages at 130 dpi and reading the drawings. A text-only
   pipeline recovers *zero* field geometry for this season.
