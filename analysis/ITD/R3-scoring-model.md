# R3 — Scoring Model

**Game under test:** INTO THE DEEP (Competition Manual V14, 146 pp) — treated as an unseen game.
**Bundle:** `analysis/ITD/bundle/`. **Ingest gate:** GREEN (`analysis/ITD/STATUS.md`).
**Written:** 2026-08-23. **Protocol:** `reference/ANALYSIS-PROTOCOL.md` §3, arithmetic conventions from
`reference/STRATEGY-RANKING-PROTOCOL.md` §6.2–6.3.

## How to read the labels

| Label | Means |
|---|---|
| `[MANUAL]` | Read directly out of the bundle. Cite is a table number or a rule/section id. |
| `[DERIVED]` | Arithmetic or logic on `[MANUAL]` facts. Operands shown. |
| `[JUDGMENT]` | A time, effort or difficulty estimate I made up. No manual authority. Argue with it. |
| `[UNVERIFIED]` | The bundle does not answer this. Never invented; goes to the Q&A queue. |

**Point values in this file come from `bundle/TABLES.md` (Table 10-3) and were re-read off the rendered
page `bundle/figures/p066_s10-game-details.png` to confirm row/value alignment. No point value was taken
from `full_layout.txt`.** Orange boxes are quoted only where marked, and are **not binding**.

---

## 1. The complete scoring table

### 1.1 Match clock `[MANUAL]`

| Segment | Length | Cite |
|---|---|---|
| AUTO | 30 s | Glossary "MATCH"; §10.4 |
| AUTO→TELEOP transition | 8 s | Glossary "MATCH"; §10.4 — "*There is an 8-second delay between AUTO and TELEOP for scoring purposes*" |
| TELEOP | 120 s (2:00) | Glossary "TELEOP"; §10.4 |
| **Total play** | **150 s** | `[DERIVED]` 30 + 120 = 150 (the 8 s transition is dead time — see §2) |
| Audio cues | start 2:30 · AUTO ends 2:00 · TELEOP begins 2:00 · "final 30 seconds" at 0:30 · end 0:00 | Table 9-1 |

**There is no named ENDGAME.** `[DERIVED]` — the string "endgame" occurs **0** times in the manual text
(`grep -ci endgame full_layout.txt` → 0). The last 30 s is a *de facto* endgame created by two things:
Table 9-1 fires a distinct cue ("Train Whistle") at 0:30, and **G427** protects ASCENT ZONES only "*in the
last 30 seconds of the MATCH*". Treat 0:30 as the endgame boundary for planning, but do not cite it as one.

### 1.2 Table 10-3: point values — every row `[MANUAL]`

| Achievement | AUTO | TELEOP | Per what | Cap | Assessment | Cite |
|---|---:|---:|---|---|---|---|
| **PARK** — OBSERVATION ZONE | 3 | 3 | per ROBOT, per period | 1 per ROBOT per period | at end of period +3 s | Table 10-3; §10.5.3 |
| **SAMPLE** — NET ZONE | 2 | 2 | per SAMPLE | limited by element count | at rest, end of period | Table 10-3; §10.5.1 |
| **SAMPLE** — LOW BASKET | 4 | 4 | per SAMPLE | limited by element count | at rest, end of period | Table 10-3; §10.5.1 |
| **SAMPLE** — HIGH BASKET | 8 | 8 | per SAMPLE | limited by element count | at rest, end of period | Table 10-3; §10.5.1 |
| **SPECIMEN** — LOW CHAMBER | 6 | 6 | per SPECIMEN | limited by element count | at rest, end of period | Table 10-3; §10.5.2 |
| **SPECIMEN** — HIGH CHAMBER | 10 | 10 | per SPECIMEN | limited by element count | at rest, end of period | Table 10-3; §10.5.2 |
| **ASCENT** — LEVEL 1 | 3 | 3 | per ROBOT, per period | 1 per ROBOT per period | end of period +3 s | Table 10-3; Table 10-2 |
| **ASCENT** — LEVEL 2 | *(blank)* | 15 | per ROBOT | once | end of MATCH +3 s | Table 10-3; Table 10-2 |
| **ASCENT** — LEVEL 3 | *(blank)* | 30 | per ROBOT | once | end of MATCH +3 s | Table 10-3; Table 10-2 |
| **Tie** | — | — | per team | — | post-MATCH | Table 10-3 → **1 RANKING POINT** |
| **Win** | — | — | per team | — | post-MATCH | Table 10-3 → **2 RANKING POINTS** |

**The blanks are load-bearing.** `[DERIVED]` ASCENT LEVEL 2 and LEVEL 3 have **empty AUTO cells** in
Table 10-3 (confirmed on the rendered page image, not just the extract). There is **no AUTO climb** in this
game. Table 10-2 reinforces it: LEVEL 2 and LEVEL 3 are defined "*at the end of the MATCH*", while LEVEL 1
is defined "*at the end of a MATCH period*".

**There are no other bonuses.** `[MANUAL]` Table 10-3 has no multiplier row, no ownership row, no
set-completion row, no coopertition row, and no threshold-based RANKING POINT. Answering
`ANALYSIS-PROTOCOL.md` §3.3 Q7: **this season has no multiplier or set mechanic at all.** Naive per-element
arithmetic is safe here — which is itself unusual and worth noting for BIOBUZZ.

### 1.3 Table 10-2: ASCENT LEVEL criteria `[MANUAL]` (§10.5.3)

| LEVEL | Definition (manual's own words, condensed) | Height involved |
|---|---|---|
| **1** | ROBOT is **in contact with the LOW RUNG** at the end of a MATCH period | LOW RUNG top = **20.0 in** (§9.5.2) |
| **2** | ROBOT is **fully supported by the HIGH and/or LOW RUNGS** at the end of the MATCH | LOW RUNG alone qualifies → **20.0 in** |
| **3** | ROBOT is **fully supported by the HIGH RUNG and completely above the top of the LOW RUNG** at the end of the MATCH | HIGH RUNG = **36.0 in**, and whole ROBOT above 20.0 in |

Additional binding conditions (§10.5.3 A–D):
- **A.** Own ALLIANCE SPECIFIC RUNGS only.
- **B.** ASCENT must start with the CHASSIS **completely outside the SUBMERSIBLE ZONE** (also **G420**;
  violating it is a MAJOR FOUL *and* forfeits the ASCENT credit).
- **C.** *LEVEL 3 only* — may not contact the HIGH RUNG while supported by the TILES (directly or
  transitively) or while grasping any non-LOW-RUNG part of the SUBMERSIBLE. **This constraint does not
  apply to LEVEL 1 or LEVEL 2.**
- **D.** A ROBOT eligible for multiple ASCENTS, or for ASCENT *and* PARKING, **earns only the highest**.
  `[DERIVED]` So PARK and ASCENT never stack within a period: per ROBOT per period you bank
  `max(PARK 3, L1 3, L2 15, L3 30)`.

> Non-binding orange box (§10.5.3), quoted only as referee-intent colour: lateral contact with non-RUNG
> SUBMERSIBLE elements is allowed for stabilisation, and *incidental* contact does not void an ASCENT.
> **Not a rule. Do not design against it.**

### 1.4 Scoring criteria that change what counts `[MANUAL]`

| Rule | Consequence |
|---|---|
| §10.5.1 | A SAMPLE scores in the NET ZONE when **fully or partially inside** it. |
| §10.5.1 | A SAMPLE scores in a BASKET when **fully or partially contained** in the inside volume, **or fully supported by the BASKET directly or transitively through other SAMPLES**. → BASKETS can overflow and keep scoring. |
| §10.5.1 | A SAMPLE in a BASKET counts **only** as a BASKET, not also as NET ZONE. No double-dipping. |
| §10.5.1 | SAMPLES count for **the ALLIANCE that owns that NET or BASKET** — colour of the SAMPLE is irrelevant to the BASKET/NET. |
| §10.5.1 | A **neutral SAMPLE with a CLIP attached** in a NET ZONE or BASKET has **no score value**. `[DERIVED]` This is a de-scoring trap you can walk into by accident: clip a yellow SAMPLE, drop it in your own HIGH BASKET, score **0** instead of 8. |
| §10.5.2 | A SPECIMEN scores if **fully supported by a corresponding ALLIANCE SPECIFIC CHAMBER**, directly or **transitively through other SPECIMENS** → CHAMBERS also stack. |
| §10.5.2 | SPECIMENS in the NET ZONE or BASKETS have **no score value**. |
| §10.5.3 | PARK = ROBOT **fully or partially inside** the OBSERVATION ZONE at the end of a MATCH period. |
| **G410** | A ROBOT may **not CONTROL more than 1 SAMPLE or 1 SPECIMEN at a time**. Exceptions: MOMENTARY excess while collecting inside the SUBMERSIBLE ZONE; already-scored elements are exempt. **No limit on CLIPS.** → This is the hard ceiling on every cycle model: one element per trip. |
| §10.3.1 | Each ROBOT may **pre-load 1 SAMPLE or 1 SPECIMEN**, drawn from the outside-the-field stock (D and E). |

### 1.5 Table 10-4: the foul price list `[MANUAL]`

| Penalty | Value |
|---|---|
| MINOR FOUL | **a credit of 5 points** toward the opponent's MATCH point total |
| MAJOR FOUL | **a credit of 15 points** toward the opponent's MATCH point total |
| YELLOW CARD | warning; a second in the same tournament phase → RED CARD |
| RED CARD | DISQUALIFIED for the MATCH |
| DISQUALIFIED | 0 MATCH points **and** 0 RANKING POINTS in a qualification MATCH |

`[DERIVED]` Priced against Table 10-3: **1 MAJOR FOUL = 15 = one full ASCENT LEVEL 2 = 1.5 HIGH CHAMBER
SPECIMENS = 7.5 NET ZONE SAMPLES.** A foul is a *credit to the opponent*, not a subtraction from you — so it
never shows up in your own score and is easy to under-weight in the drive-team's head. **G412** (de-scoring
an opponent's scored element) is a MAJOR FOUL *per element*: de-scoring one HIGH BASKET SAMPLE costs the
opponent 8 and costs you 15. Never profitable. **G404** (AUTO interference) is a MAJOR FOUL *each
occurrence* — the single most expensive thing a bad AUTO path can do.

### 1.6 Element inventory `[MANUAL]` §10.3.1 / §9.7 — and it balances

| Element | Total | Where |
|---|---:|---|
| Blue SAMPLES | 20 | 15 in SUBMERSIBLE + 3 on SPIKE MARKS (tile **B1**) + 2 outside the wall |
| Red SAMPLES | 20 | 15 in SUBMERSIBLE + 3 on SPIKE MARKS (tile **E6**) + 2 outside the wall |
| Neutral SAMPLES | 40 | 30 in SUBMERSIBLE + 3 on **B6** + 3 on **E1** + 2 per ALLIANCE outside the wall |
| CLIPS | 40 | 20 per ALLIANCE, outside the wall |

`[DERIVED]` The accounting closes exactly (15+3+2 = 20 ✓, 30+3+3+2+2 = 40 ✓), which is a useful check that
the extract did not drop a line.

**Two supply ceilings fall straight out of this** `[DERIVED]`:
- **SPECIMEN branch: 20 per ALLIANCE, ever.** A SPECIMEN needs one *ALLIANCE SPECIFIC* SAMPLE (Glossary,
  §9.7.3). You own exactly 20. At HIGH CHAMBER that is a hard **200-point** lifetime cap.
- **SAMPLE branch: 60 per ALLIANCE.** 40 neutral + your own 20 all score in your BASKETS/NET (§10.5.1). At
  HIGH BASKET that is a **480-point** cap — but the 40 neutral are shared with the opponent and contested.

---

## 2. Is AUTO scored live or at the end — and is it RE-COUNTED?

### 2.1 Live or at the end? — **AT THE END OF THE PERIOD.** `[MANUAL]`

The governing sentence, §10.5 Scoring, quoted in full:

> "All accomplishments are tracked live by FIELD STAFF and certified at the end of the MATCH.
> Accomplishments are officially scored at the end of each MATCH period based on the status of the FIELD,
> when all ROBOTS and SCORING ELEMENTS have come to rest, except as follows:"

Two exceptions follow, both §10.5:

> "**A.** assessment of ASCENT and PARKING points is made 3 seconds after the ARENA timer reaches the end
> of the MATCH period following AUTO and TELEOP, or when all ROBOTS have come to rest following the
> conclusion of the MATCH period, whichever happens first."

> "**B.** scoring achievements that occur after the end of the AUTO period and before the start of the
> TELEOP period will count in the TELEOP period but may violate G403."

**Answer:** *tracked* live, *scored* at the end of each period, off a **snapshot of field state at rest**.
Not live. The **8-second transition exists precisely so the AUTO snapshot can settle** (§10.4: "*There is an
8-second delay between AUTO and TELEOP for scoring purposes as described in Section 10.5 Scoring*").

`[DERIVED]` Three design consequences:
1. **A SAMPLE still in flight at 0:30 of AUTO scores in TELEOP, not AUTO** (item B) — and if your AUTO
   OpMode was still driving to make it happen, **G403** upgrades from MINOR to **MAJOR FOUL** "*if actions
   result in a scoring achievement*". An AUTO that finishes at 29.8 s is a 15-point liability.
2. **Nothing has to stay put during AUTO** — only at the instant the period ends. An element knocked out of
   a BASKET at t=25 s was never scored.
3. **PARK and ASCENT get a 3-second grace** (item A). A ROBOT that coasts into the OBSERVATION ZONE after
   the buzzer still PARKS. `[JUDGMENT]` Worth exploiting: aim the last motion of your AUTO/TELEOP at the
   zone and let momentum finish it.

### 2.2 Are AUTO-scored elements RE-COUNTED in the final score? — **YES, on the plain reading.** `[DERIVED]` — *and this is the single number I most want confirmed.*

There is **no sentence in the manual that says AUTO achievements are excluded from the TELEOP
assessment**, and no sentence that says scored elements are removed, reset, or credited once. What the
manual does say is that scoring is "*officially scored at the end of **each** MATCH period **based on the
status of the FIELD***".

`[DERIVED]` Applied literally: a SPECIMEN hung on the HIGH CHAMBER at t=10 s of AUTO is (a) on the field at
rest at the end of AUTO → **10 AUTO points**, and (b) still on the field at rest at the end of TELEOP →
**10 TELEOP points**. Total **20 for one action**. Table 10-3 supports this structurally: it prints an AUTO
column *and* a TELEOP column with **identical values** for every element row (2/2, 4/4, 8/8, 6/6, 10/10) —
which is exactly what you would print if the same physical element is assessed twice, and a strange thing
to print if it were only ever credited once.

Corroborating: **PARK is unambiguously assessed twice** (3 AUTO + 3 TELEOP, "at the end of *a* MATCH
period", §10.5.3), and **G412** forbids opponents from removing your scored elements — a protection that
only has teeth if their continued presence keeps earning.

**The counter-reading, stated fairly:** "based on the status of the FIELD" could describe a *delta* — i.e.,
the TELEOP column scores only what was added after AUTO. The manual does not adjudicate between the two.

> **`[UNVERIFIED]` — queued for Game Q&A.** "Is a SCORING ELEMENT that was scored during AUTO and remains
> in place also credited in the TELEOP assessment under §10.5?" Everything in §4's budget is written both
> ways until this is answered. **If AUTO re-counts, an AUTO HIGH CHAMBER SPECIMEN is worth 20 points and
> AUTO is the highest-leverage 30 seconds in the game.**

> **LEAK FLAG (harness honesty).** I have a background recollection about how this resolved in the real
> INTO THE DEEP season. **I did not read it in this bundle and I have not used it.** Everything above is
> derived from the three quoted §10.5 sentences and the shape of Table 10-3. Flagging it rather than
> silently using it, per the run rules.

---

## 3. Points per second, per action

### 3.1 The assumptions, all `[JUDGMENT]`, all arguable

**Drive speed.** goBILDA 5203 Yellow Jacket 312 RPM (Table 12-1 legal) on 96 mm wheels:
- 312 ÷ 60 = **5.2 rev/s**
- circumference = π × 96 mm = 301.6 mm = **11.87 in**
- free speed = 5.2 × 11.87 = **61.7 in/s**
- × **0.7** realism factor (accel, turns, traffic — the factor is mandated by `STRATEGY-RANKING-PROTOCOL.md`
  §6.2) = **43.2 → 43 in/s**

**Travel legs, in tiles.** TILE = 24 in; FIELD = 6 × 6 tiles = 144 in (§9.1). From the ARENA geometry
(Figure 9-2, Figure 10-2) `[DERIVED]`:

| Leg | Distance | Time @ 43 in/s |
|---|---:|---:|
| OBSERVATION ZONE ↔ own CHAMBER (corner → centre face) | ~60 in (2.5 tiles) | **1.4 s** |
| SUBMERSIBLE ↔ own BASKETS/NET ZONE (centre → corner) | ~50 in (2.1 tiles) | **1.2 s** |

**Per-term estimates.** `t_acq` inside the SUBMERSIBLE is deliberately expensive: the SUBMERSIBLE ZONE is
27.5 × 42.75 in (Glossary), the elements are *randomly* placed (§10.3.1 F), there is a 2 in barrier
(§9.5.1), the RUNGS are overhead at 20 in, and up to four ROBOTS reach in at once.

### 3.2 The cycle table — value ÷ (t_acq + t_out + t_align + t_deliver + t_back)

Per `STRATEGY-RANKING-PROTOCOL.md` §6.2 pessimism rule, every un-stopwatched `t_cycle` is reported raw
**and × 1.3**. Use the ×1.3 column for decisions until someone measures a mock-up.

| Cycle | pts | t_acq | t_out | t_align | t_deliver | t_back | **t_cycle** | ×1.3 | **pts/s raw** | **pts/s ×1.3** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **SPECIMEN → HIGH CHAMBER**, fed (HP has a queue staged) | 10 | 1.5 | 1.4 | 1.0 | 2.0 | 1.4 | **7.3** | 9.5 | **1.37** | **1.05** |
| **SPECIMEN → LOW CHAMBER**, fed | 6 | 1.5 | 1.4 | 1.0 | 1.5 | 1.4 | **6.8** | 8.8 | 0.88 | 0.68 |
| **SPECIMEN → HIGH CHAMBER**, self-supplied *(includes fetching the next ALLIANCE SAMPLE from the SUBMERSIBLE: +1.0 reposition +3.5 acquire)* | 10 | 2.5 | 1.4 | 1.0 | 2.0+4.5 | 1.4 | **12.8** | 16.6 | **0.78** | **0.60** |
| **SAMPLE → HIGH BASKET** | 8 | 3.5 | 1.2 | 1.2 | 3.0 | 1.2 | **10.1** | 13.1 | **0.79** | **0.61** |
| **SAMPLE → LOW BASKET** | 4 | 3.5 | 1.2 | 1.0 | 2.0 | 1.2 | **8.9** | 11.6 | 0.45 | 0.34 |
| **SAMPLE → NET ZONE** | 2 | 3.5 | 1.2 | 0.3 | 0.5 | 1.2 | **6.7** | 8.7 | 0.30 | 0.23 |

Arithmetic shown for the two rows that decide the season:
- HIGH CHAMBER fed: 1.5+1.4+1.0+2.0+1.4 = **7.3 s**; 10 ÷ 7.3 = **1.37**; 7.3 × 1.3 = 9.5; 10 ÷ 9.5 = **1.05**
- HIGH BASKET: 3.5+1.2+1.2+3.0+1.2 = **10.1 s**; 8 ÷ 10.1 = **0.79**; 10.1 × 1.3 = 13.1; 8 ÷ 13.1 = **0.61**
- HIGH CHAMBER self-supplied: 2.5+1.4+1.0+2.0+4.5+1.4 = **12.8 s**; 10 ÷ 12.8 = **0.78**

### 3.3 One-shot achievements — priced in seconds of surrendered cycling

These are not cycles. Price them as *how much TELEOP throughput you give up.* `[JUDGMENT]` on the times.

| Achievement | pts | seconds surrendered | pts/s of surrendered time | ×1.3 | Break-even vs a 0.78 pts/s cycler |
|---|---:|---:|---:|---:|---|
| PARK (per period) | 3 | ~2 (your cycle already ends near the OBSERVATION ZONE) | 1.50 | 1.15 | Always worth it |
| ASCENT LEVEL 1 | 3 | ~3 | 1.00 | 0.77 | Marginal on points — **but see §5, it feeds tiebreak #3** |
| **ASCENT LEVEL 2** | **15** | ~12 (position 2 + engage 2 + lift/settle 4 + margin 4) | **1.25** | **0.96** | Worth it if you can do it in **< 19 s** (15 ÷ 0.78) |
| ASCENT LEVEL 3 | 30 | ~20 (two-stage climb forced by condition C) | 1.50 | 1.15 | Worth it if you can do it in **< 38 s** (30 ÷ 0.78) |

### 3.4 Rule V-a — the match-averaged number, which is the honest one

`STRATEGY-RANKING-PROTOCOL.md` §6.3 Rule V-a: **PPS is points ÷ the full 150 s of play, never ÷ the seconds
the action took.** Two single-robot builds, both a modest two-team program can actually make:

**Build A — SPECIMEN cycler, self-supplied, LEVEL 2 ASCENT**
```
usable_teleop = 120 − t_startup 4 − t_ascent 12               = 104 s
N_cycles      = floor(104 ÷ 12.8)                             = 8
P_teleop      = 8 × 10                                        = 80
P_auto        = pre-load HIGH CHAMBER 10 + PARK 3             = 13
P_oneshot     = ASCENT LEVEL 2                                = 15
P_robot                                                       = 108
PPS_match     = 108 ÷ 150                                     = 0.72 pts/s
```

**Build B — SAMPLE cycler to the HIGH BASKET, LEVEL 2 ASCENT**
```
usable_teleop = 120 − 4 − 12                                  = 104 s
N_cycles      = floor(104 ÷ 10.1)                             = 10
P_teleop      = 10 × 8                                        = 80
P_auto        = pre-load HIGH BASKET 8 + PARK 3               = 11
P_oneshot     = 15
P_robot                                                       = 106
PPS_match     = 106 ÷ 150                                     = 0.71 pts/s
```

**They tie.** 0.72 vs 0.71. This is the most important honest result in the file and it is *not* what the
raw point values suggest. Read §6 for what actually separates them.

---

## 4. Point budget: AUTO / TELEOP / endgame

### 4.1 AUTO — 30 s, 2 ROBOTS, per ALLIANCE

**The pre-load trap** `[DERIVED]`, §10.3.1 D + E. Each ALLIANCE has, outside the wall: **2 neutral SAMPLES,
2 ALLIANCE SPECIFIC SAMPLES, 20 CLIPS** — and pre-loads must come from that stock. **If both your ROBOTS
pre-load SPECIMENS, you consume both ALLIANCE SPECIFIC SAMPLES and your HUMAN PLAYER starts the MATCH
holding 18 CLIPS and nothing legal to clip them to.** Neutral + CLIP is still a SAMPLE (§9.7.1) and scores
**zero** in a NET or BASKET (§10.5.1). This is a genuine kickoff-day trap and it is invisible from Table 10-3.

**The designed AUTO loop** `[DERIVED]` from §9.2 + §10.3.1 A/B/C + Figure 10-2: your **3 ALLIANCE-coloured
SPIKE MARK SAMPLES sit on the tile in front of your own OBSERVATION ZONE** (B1 for blue, E6 for red — §9.2:
the ALLIANCE-coloured marks are "in front of the OBSERVATION ZONES", the white ones "in front of each NET
ZONE"). Your **3 neutral SPIKE MARK SAMPLES sit in front of your own NET ZONE/BASKETS** (B6, E1). The field
pre-stages SPECIMEN feedstock next to the SPECIMEN loading point and BASKET feedstock next to the BASKETS.
That is a deliberate design and it tells you where a 30-second AUTO should go.

| Scenario | Arithmetic | AUTO points |
|---|---|---:|
| Supply-bounded ceiling, SPECIMEN AUTO `[DERIVED]` | 2 pre-load SPECIMENS + at most 1 fetch-and-clip per ROBOT in 30 s (12.8 s round trip) = 4 × 10 = 40, plus 2 × PARK 3 = 6 | **46** |
| Aggressive but real `[JUDGMENT]` | per ROBOT: pre-load HIGH CHAMBER 10 + one more cycle 10 + PARK 3 = 23; × 2 | **46** |
| Our program, drilled `[JUDGMENT]` | per ROBOT: pre-load HIGH CHAMBER 10 + deliver a SPIKE MARK SAMPLE to the HP (0 pts, sets up TELEOP) + PARK 3 = 13; × 2 | **26** |
| Our program, week 1 `[JUDGMENT]` | 2 × (PARK 3) + 1 pre-load scored | **~14** |

**With the §2.2 re-count reading, every AUTO element doubles.** The 46-point ceiling becomes **86**
(40 re-counted + 46). This is why §2.2 is the highest-value Q&A question of the season.

### 4.2 TELEOP — 120 s, 2 ROBOTS, per ALLIANCE

| Scenario | Arithmetic | TELEOP points |
|---|---|---:|
| Two self-supplied SPECIMEN ROBOTS `[DERIVED]` | 2 × 8 cycles × 10 | **160** |
| Two HIGH BASKET ROBOTS `[DERIVED]` | 2 × 10 cycles × 8 | **160** |
| Mixed (1 SPECIMEN + 1 BASKET) `[DERIVED]` | 80 + 80 | **160** |
| Our program `[JUDGMENT]` (5 cycles/ROBOT, dropped elements, traffic) | 2 × 5 × 10 | **100** |

**The SPECIMEN branch saturates.** `[DERIVED]` 2 AUTO pre-loads + 16 TELEOP cycles = 18 ALLIANCE SPECIFIC
SAMPLES consumed, against a lifetime supply of exactly **20**. A perfect two-ROBOT SPECIMEN ALLIANCE runs
out of feedstock at almost exactly the final buzzer. That is a tuned cap, not an accident, and it means
**the marginal 19th and 20th scoring action of a dominant ALLIANCE must be a BASKET, not a CHAMBER.**

### 4.3 Endgame — the last 30 s

No named ENDGAME `[MANUAL]`. ASCENT LEVEL 2/3 are TELEOP-only and assessed at the end of the MATCH.

| Scenario | Arithmetic | Points |
|---|---|---:|
| Ceiling | 2 × LEVEL 3 (30) | **60** |
| Realistic strong | 1 × L3 + 1 × L2 | 45 |
| Our program `[JUDGMENT]` | 2 × LEVEL 2 (15) | **30** |
| Our program, fallback | 2 × LEVEL 1 (3) | 6 |

### 4.4 Whole-match roll-up `[DERIVED]`

| | AUTO | TELEOP | Endgame | **Total** |
|---|---:|---:|---:|---:|
| Ceiling, single-count reading | 46 | 160 | 60 | **266** |
| Ceiling, re-count reading (§2.2) | 86 | 160 | 60 | **306** |
| Our program, drilled `[JUDGMENT]` | 26 | 100 | 30 | **156** |
| Our program, week 1 `[JUDGMENT]` | 14 | 60 | 6 | **80** |

> **Sanity check, per `ANALYSIS-PROTOCOL.md` §3.4.** A rookie-legal ROBOT does *not* win by a factor of
> three here: 80 vs a 266 ceiling. The model passes. `[UNVERIFIED]` I have **no** historical
> score-inflation curve available — `SCORING-PATTERNS.md` §B.11 holds it and is a forbidden file for this
> run. Treat "a realistic winning score" as `[JUDGMENT] ≈ 150–200` and replace it with real event data.

---

## 5. RANKING POINTS and the tiebreaker ladder

### 5.1 The RP formula `[MANUAL]`

| Outcome | RANKING POINTS | Cite |
|---|---:|---|
| Win | **2** | Table 10-3 |
| Tie | **1** | Table 10-3 |
| Loss | **0** `[DERIVED]` — the table lists no loss row | Table 10-3 |
| DISQUALIFIED | 0 MATCH points **and** 0 RP; contributes 0 to **all** sort criteria | Table 10-4; §13.5.3 |

**RANKING SCORE (RS) = the average RP a team earns across its qualification MATCHES**, excluding SURROGATE
MATCHES (§13.5.3, Glossary).

> **The 60-second test** (`ANALYSIS-PROTOCOL.md` §3.3 Q5): *is there any way to earn RP other than
> winning?* **No.** `[MANUAL]` Table 10-3's RANKING POINTS column has exactly two rows — Tie and Win.
> **There are no RP thresholds, no bonus RP, and no per-tier RP variation.** Answering Q6: nothing to
> check. **RP-farming is not a strategy this season.** Every ranking decision collapses to "win the match",
> which means *your* score only matters relative to your opponent's, and a 10-point win ranks exactly like
> a 200-point win.

### 5.2 The tiebreaker ladder `[MANUAL]` — Table 13-1

| Sort | Criterion |
|---:|---|
| 1st | **RANKING SCORE (RS)** |
| 2nd | **Average ALLIANCE AUTO Points** |
| 3rd | **Average TELEOP ALLIANCE ASCENT Points** |
| 4th | **Highest MATCH Score (including FOULS)** |
| 5th | Random sort by the FIRST event management software |

`[DERIVED]` **This ladder is where the real strategy hides, and it is not in Table 10-3.** Because RP is
only ever 0/1/2, RS is a coarse quantity — at a 30-team qualifier with 5–6 matches, RS takes only a handful
of distinct values and **ties on sort 1 are the normal case, not the exception.** So sorts 2 and 3 decide
seeding for most of the field:

- **AUTO points are worth more than their face value.** Sort 2 is average ALLIANCE AUTO points. A reliable
  13-point AUTO does not just add 13 to a match — it is your primary seeding currency. Combined with §2.2
  (if AUTO re-counts, AUTO elements are worth double in MATCH points *and* feed sort 2), **AUTO is the
  highest-leverage 30 seconds of the season.**
- **ASCENT points are worth more than their face value.** Sort 3 is average **TELEOP ALLIANCE ASCENT**
  points — note it counts *ASCENT only*, not PARK. This rescues **ASCENT LEVEL 1**: 3 points is
  near-worthless for winning a match (§3.3 says it barely breaks even against cycling), but it is
  **non-zero on sort 3 where PARK scores nothing.** `[DERIVED]` A ROBOT that cannot climb should still
  touch the LOW RUNG rather than PARK when the match outcome is already decided — 3 = 3 in MATCH points,
  but 3 > 0 on the ranking ladder.
- **Sort 4 rewards one big score**, not consistency. Running up the score in a match you are already
  winning has ranking value only at this depth.

### 5.3 Playoffs `[MANUAL]` §13.6
No RP in playoffs — teams advance on wins in a double-elimination bracket. A DISQUALIFICATION in playoffs
applies to the **entire ALLIANCE** (0 MATCH points for all).

---

## 6. THE KEY QUESTION — what is underpriced, and does anything cheap outprice something dear?

I use "underpriced" as `STRATEGY-RANKING-PROTOCOL.md` Rule V-b uses it: **an objective whose point value is
high relative to the engineering it demands.** A bargain to buy, not a design error to avoid.

### 6.1 The effort ledger — points against ARENA geometry `[MANUAL]` heights, `[DERIVED]` ratios

| Objective | pts | **Required delivery height** | Target window | **pts per inch of lift** | Acquisition |
|---|---:|---|---|---:|---|
| SAMPLE → NET ZONE | 2 | 0 in (floor) | corner triangle, 22.75 in along the wall; *partial* counts | — | SUBMERSIBLE scrum |
| PARK | 3 | 0 in (floor) | 36.6 × 13.1 in zone; *partial* counts | — | none |
| ASCENT L1 | 3 | touch LOW RUNG, top **20.0 in** | 44.5 in wide bar | 0.15 | none |
| SAMPLE → LOW BASKET | 4 | lip at **25.75 in** | **8.85 × 5.5 in** opening | **0.16** | SUBMERSIBLE scrum |
| SPECIMEN → LOW CHAMBER | 6 | bar top at **13.0 in** | **26.5 in wide** bar, 1.05 in dia | **0.46** | own OBSERVATION ZONE |
| SAMPLE → HIGH BASKET | 8 | lip at **43.0 in** | **8.85 × 5.5 in** opening | **0.19** | SUBMERSIBLE scrum |
| SPECIMEN → HIGH CHAMBER | 10 | bar top at **26.0 in** | **26.5 in wide** bar | **0.38** | own OBSERVATION ZONE |
| ASCENT L2 | 15 | LOW RUNG **20.0 in**, whole ROBOT's weight | 44.5 in bar | **0.75** | none |
| ASCENT L3 | 30 | HIGH RUNG **36.0 in**, whole ROBOT above 20.0 in | 44.5 in bar | **0.83** | none |

Heights: §9.5.1 (CHAMBERS 13.0 / 26.0 in), §9.5.2 (RUNGS 20.0 / 36.0 in), §9.6 (BASKET lips 25.75 / 43.0 in),
§9.6 (BASKET opening 8.85 × 5.5 in), Glossary (OBSERVATION ZONE 36.6 × 13.1 in; NET ZONE 22.75 in at the
wall; SAMPLE 3.5 × 1.5 × 1.5 in). **R104: there is no vertical height limit** — the horizontal boundary is
20 × 42 in. So height is never *rule*-limited in this game, only mechanically expensive. Every inch you
choose to build, you pay for twice: this is a **two-robot program**.

### 6.2 FINDING 1 — **YES. The price ladder is inverted. Both CHAMBERS outprice the BASKET above them in difficulty.**

**HIGH CHAMBER pays 25% MORE than HIGH BASKET for 60% of the lift.**
- 10 ÷ 8 = **1.25×** the points.
- 26.0 ÷ 43.0 = **0.60×** the delivery height.
- Per inch of required lift: 0.385 ÷ 0.186 = **2.07× better.**

**LOW CHAMBER pays 50% MORE than LOW BASKET for 50% of the lift.**
- 6 ÷ 4 = **1.50×** the points; 13.0 ÷ 25.75 = **0.50×** the height.
- Per inch: 0.462 ÷ 0.155 = **2.98× better.**

And the tolerance runs the same way. A CHAMBER is a **26.5 in wide, 1.05 in diameter horizontal bar** —
one forgiving axis, and gravity finishes the placement for you. A BASKET is an **8.85 × 5.5 in hole 43
inches in the air** — two tight axes, at the top of a mast, with a 3.5 in payload you must not tip out on
the way up.

**Stated loudly, because this is the kind of finding that decides a season: the cheapest tall mechanism in
INTO THE DEEP is also the highest-paying one. The LOW CHAMBER — a 13-inch lift, the lowest scoring height
of any non-floor objective in the game — pays 6, half again what a 25.75-inch LOW BASKET lift pays.**

### 6.3 FINDING 2 — the trap: **HIGH BASKET is the most expensive mechanism in the game and it is not the best-paying objective.**

To score a HIGH BASKET you must clear a **43.0 in lip** and tip a 3.5 in SAMPLE *in*, so the mechanism needs
roughly **48+ inches of usable vertical travel** — a multi-stage cascade or a virtual four-bar, bought
linear-slide kits, real tolerance work, and a high CG on a 12 × 12 ft field full of contact. The HIGH
CHAMBER needs about **30 inches** and a hook.

`[JUDGMENT]` For **~15 students, two teams, two ROBOTS, modest budget, hand tools + 3D printing, no CNC**,
those are not comparable projects. A 48-inch cascade built twice, tuned twice, and repaired twice at
competition is the single largest schedule risk a program of this size can take on — and it buys you the
**second**-best objective. **If your team builds exactly one tall mechanism this season, build it 26 inches
tall, not 43.**

### 6.4 FINDING 3 — the underpriced row: **ASCENT LEVEL 2, at 15 points.**

Table 10-2 LEVEL 2: "*ROBOT is fully supported by the **HIGH and/or LOW RUNGS** at the end of the MATCH.*"
**"and/or"** — `[DERIVED]` **the LOW RUNG alone qualifies.** LOW RUNG top = **20.0 in** (§9.5.2). And
condition **C**, the constraint that forces the hard two-stage climb, is written "*for a LEVEL 3 ASCENT*"
only. **LEVEL 2 has no such constraint.** Condition B is satisfied for free — the ASCENT ZONE lies outside
the SUBMERSIBLE ZONE by construction (Glossary).

So LEVEL 2 reduces to: **hang your whole ROBOT off a 1-inch-diameter, 44.5-inch-wide bar that is 20 inches
off the floor, once, at the end of the match.** One hook. One motor. One axis. No sensing. `[JUDGMENT]`
~12 seconds.

Price it against Table 10-3 `[DERIVED]`:
- **15 points = 1.5 HIGH CHAMBER SPECIMENS = 7.5 NET ZONE SAMPLES = 5 PARKS = 1 MAJOR FOUL.**
- 0.75 pts per inch of lift — **4× the HIGH BASKET's 0.19** and **2× the HIGH CHAMBER's 0.38.**
- It is the **highest points-per-unit-of-build-complexity row in the entire table** for a hand-tools team,
  and it is duplicable: the same hook and motor go on both ROBOTS with no tuning.

By contrast **LEVEL 3 is the one row where price honestly tracks difficulty**: 2× the points (30) for the
HIGH RUNG at 36.0 in, *plus* getting the entire ROBOT above 20.0 in, *plus* condition C forcing a
low-rung-then-transfer two-stage climb. That is roughly **3× the mechanism for 2× the points.** Fairly
priced, arguably *over*-priced in effort — and the right thing for our program to attempt in season 2, not
in week 3.

### 6.5 FINDING 4 — the asymmetry no point value shows: **one supply lane is rule-protected and the other is a scrum.**

| | SPECIMEN branch | SAMPLE branch |
|---|---|---|
| Feedstock lives | your own **OBSERVATION ZONE**, restocked by your HUMAN PLAYER | inside the **SUBMERSIBLE ZONE**, 27.5 × 42.75 in, randomly placed (§10.3.1 F) |
| Protected? | **Yes — G426**: "*A ROBOT may not be in the opposing ALLIANCE'S OBSERVATION ZONE*" (MINOR FOUL, plus MINOR per 5 s, plus MINOR per element contacted) | **No.** All four ROBOTS reach into the same volume, under RUNGS at 20 in, over a 2 in barrier |
| Colour discrimination | **Required** — only *ALLIANCE SPECIFIC* SAMPLES make SPECIMENS (§9.7.3). 15 of the 60 elements in the SUBMERSIBLE are yours | **Not required** — own *or* neutral both score (§10.5.1). 45 of 60 are legal for you |
| Lifetime supply | **20** | **60** |
| Extra step | HUMAN PLAYER must attach a CLIP | none |

`[DERIVED]` The SPECIMEN branch is higher-paying, lower-lifting, and its *delivery-side* logistics run
through a zone the rules keep opponents out of. But it needs **colour sensing in the worst possible
lighting position** and it runs out of ammunition. The SAMPLE branch is cheaper to feed and never runs out,
but every acquisition happens in the most contested cubic foot on the field.

### 6.6 The honest counterweight — why §3.4 came out a tie

Per-cycle, once you charge the SPECIMEN branch for the CLIP round trip, **HIGH CHAMBER (0.78 pts/s) and
HIGH BASKET (0.79 pts/s) are throughput-identical.** The CHAMBER's advantage is **not** speed. It is:

1. **Mechanism cost** — 26 in vs 43 in, forgiving bar vs tight hole. Same points per second from a
   mechanism roughly half as tall and far more duplicable. For a two-robot program that is the whole game.
2. **Ceiling with a queue** — if the HUMAN PLAYER has SPECIMENS staged, the hanger's cycle drops to 7.3 s
   → **1.37 pts/s**, which beats the BASKET by 73%. `[DERIVED]` But dedicating your second ROBOT to
   feeding is *worse* than running both independently: split roles give the pair 10 pts per 8 s = 1.25
   pts/s, while two independent self-supplied cyclers give 2 × 0.78 = **1.56 pts/s.** **Do not build a
   dedicated feeder ROBOT.** The OBSERVATION-ZONE trip is shared work, not a job.
3. **Saturation** — §4.2: the SPECIMEN branch runs dry at ~20 hangs.

`[JUDGMENT]` **The two-ROBOT plan this implies:** one SPECIMEN cycler (26 in lift, CHAMBERS, own
OBSERVATION ZONE) + one SAMPLE cycler (BASKETS, own NET ZONE corner). Equal throughput, opposite corners of
the field so they never queue behind each other, and they draw on **different supply pools** — so neither
runs dry. Both get the same LOW-RUNG LEVEL 2 hook, built once and duplicated.

### 6.7 Summary answer

- **Is anything cheap outpricing something dear? YES, twice.** HIGH CHAMBER (10 pts, 26.0 in) outprices
  HIGH BASKET (8 pts, 43.0 in). LOW CHAMBER (6 pts, 13.0 in) outprices LOW BASKET (4 pts, 25.75 in). Every
  rung of the SPECIMEN ladder beats the SAMPLE rung above it on both points *and* height.
- **The single most underpriced objective is ASCENT LEVEL 2 at 15 points** — a 20-inch, one-motor,
  one-axis, end-of-match hang that pays more than one and a half HIGH CHAMBER cycles and requires no
  sensing, no precision and no supply chain.
- **The trap is the HIGH BASKET.** It demands the tallest, most precise, least duplicable mechanism in the
  game and pays 20% less than the objective at 60% of its height.
- **The hidden multiplier is Table 13-1**, not Table 10-3: AUTO points and TELEOP ASCENT points are the
  2nd and 3rd sort criteria, so they buy seeding on top of their face value.

---

## What this game rewards — in plain language

This game pays you to **carry small things a short distance, over and over, and to hang your robot on a
low bar at the end.** It does *not* pay you to build tall. The two highest-value repeatable actions —
hanging a SPECIMEN on the HIGH CHAMBER for 10 and on the LOW CHAMBER for 6 — happen at 26 and 13 inches,
onto a two-foot-wide bar you can slam into, while the flashy 43-inch HIGH BASKET pays 8 into a hole the
size of a paperback. The single best points-per-effort item on the whole sheet is the LEVEL 2 ASCENT: 15
points for hooking a bar 20 inches off the floor once, which is one motor and one hook and no sensor. So a
team with hand tools, a printer and two robots to build should aim low and cycle fast: a modest ~30-inch
lift that hooks a bar, a drivetrain that gets across two and a half tiles in a second and a half, a
practiced 30-second AUTO, and a climb hook bolted to both robots. What separates good from great is not
height — it is **AUTO reliability and cycle count**, because ranking is decided by wins, and when wins tie
(which they usually do) the tiebreakers are AUTO points and ASCENT points, in that order. Build the
boring thing, build it twice, and drive it a lot.

---

## Beta feedback

1. **`bundle/TABLES.md` is missing Table 10-2 (ASCENT LEVEL Criteria) entirely.** It is the second-most
   important table in the manual — it defines the 15- and 30-point rows of Table 10-3 — and the geometry
   extractor did not recover it. Worse, the file *appears* to contain it: there is a heading
   `## p.143 - Table 10-2` which is actually the **glossary**, so a reader who greps for "Table 10-2" gets
   a false positive. In `full_layout.txt` the same table is scrambled (LEVEL 1/2/3 labels on one line, the
   three definitions on later lines and off by one) — exactly the pdftotext failure mode
   `ANALYSIS-PROTOCOL.md` §3.1 warns about, but the harness's own gate says "Scoring tables recovered:
   PASS". **I recovered Table 10-2 only by reading `figures/p065_s10-game-details.png`.** For BIOBUZZ the
   gate should verify that *every* `Table 10-x` referenced in Section 10 prose has a matching heading in
   TABLES.md, not just that some tables parsed.

2. **The allowed method file points straight at forbidden files.** `ANALYSIS-PROTOCOL.md` §3.3 instructs
   "answer the pre-written 18 questions in `SCORING-PATTERNS.md` §C.2", §3.4 requires the historical
   inflation curve from `SCORING-PATTERNS.md` §B.11 to sanity-check a realistic winning score, and the
   post-R3 step requires `TOURNAMENT-AND-RANKING.md` §6. All three are on the answer-key list. I answered
   §3.3's seven inline questions and skipped the 18, and I could not sanity-check my winning-score estimate
   against anything. **The method files need the season-specific reference material factored out of them**,
   or the harness will keep leaking the answer key through its own protocol.

3. **`caps_NOVEL_ranked.txt` is noisy in a way that would mislead on an unseen game.** It ranks
   `SUBMERSIBLE 63` above `SAMPLE 39`, but also lists `VEX 6`, `HIPS 4`, `BILDA 4`, `EDR 3`, `JST 1`,
   `NZS 1`, `IEC 1`, `FOR 2`, `COMPLETE 2` — vendor names, materials and stopword fragments mixed in with
   real game vocabulary. On a game nobody has seen, the top-20 of this list is the first thing a reader
   trusts. It needs the Section 12 vendor tables excluded before ranking.

4. **`rules_GAMESPECIFIC.txt` gives headlines only — no page, no body, no violation.** It is 16 lines of
   bare `id + headline`. To do anything with it I had to re-join against `rules_full.tsv` myself. Two extra
   columns (page, violation) would make it usable standalone, which is what a 16-line orange-rule list is
   *for* on kickoff morning.

5. **Nothing in the bundle answers the re-count question (§2.2), and nothing flags it as open.**
   Whether AUTO-scored elements are counted again at the end of TELEOP moves the ceiling by 40 points
   (266 → 306) and changes whether AUTO is worth 13 points or 26. `ANALYSIS-PROTOCOL.md` §3.3 Q2 correctly
   calls this "the single distinction [that] moves points-per-second by more than any mechanism choice" —
   but `TRIPWIRES.txt` is gated to R6, so the R3 analyst has no tool pointing them at the sentence.
   **Recommendation: surface scored-live/at-end language in a tiny `SCORING_TIMING.txt` available at R3**,
   not buried in the R6 tripwire dump.

6. **Minor: the figures MANIFEST says "read the scoring PROSE in the text extract, not off the image",
   which is the opposite of what this run needed.** The prose extract for §10.5.3 is the part that was
   scrambled; the image was correct. Given house rule "never take point values from `full_layout.txt`",
   the manifest's advice puts those two instructions in direct tension.

7. **Worked fine and should be kept:** `rules_full.tsv` (headline + body + violation in one row) was the
   single most useful file in the bundle; the `figures/*.png` at 130 dpi were legible enough to read
   dimension callouts directly; `section_versions.txt` is a good cheap diff key; and the element-inventory
   arithmetic in §10.3.1 closing exactly (20/20/40/40) was a useful independent check that the extract had
   not silently dropped a line.
