# POWER PLAY (2022-23) — Season Dossier

**Sources.** Game Manual Part 2 – Traditional Events, **Revision 1.3, 10/26/2022** (55 pp) and Game Manual Part 1 – Traditional Events, **Revision 1.2, 10/18/2022** (70 pp), both from `manuals/archive/`. Q&A rulings from `manuals/archive/supplemental/2022-23_POWERPLAY_Complete_QA.html` (375 items) — see §9, this file exists despite the harness brief saying otherwise. Presented by Raytheon Technologies [MANUAL §4.1].

Every claim below is tagged **[MANUAL]** (stated in the manual), **[Q&A]** (forum ruling, which per §4.5 *takes precedence over the manual*), **[DERIVED]** (arithmetic, operands shown), **[JUDGMENT]** (my read), or **UNVERIFIED**.

---

## 1. The game in five sentences

Two two-team Alliances play on a 12 ft × 12 ft field carrying 60 plastic **Cones** (30 red, 30 blue) and a 5 × 5 grid of 25 Alliance-neutral **Junctions** — 9 flat Ground discs, 8 Low poles (13.5"), 4 Medium (23.5") and 4 High (33.5") — plus four corner **Terminals** and two mid-wall **Substations** where a Human Player feeds cones in [MANUAL §4.3 *Junction*, *Cone*, *Terminal*, *Substation*; Fig C-5, C-6]. A Cone is worth 2/3/4/5 points depending on the Junction it is *Secured* on, and 1 point dropped in a Terminal — but at the end of the match an Alliance also earns **3 points for every Junction whose top Cone is theirs**, **10 for a Junction Capped with their team-built Beacon**, and **20 for a Circuit**: an unbroken king-move chain of owned Junctions linking their two diagonally-opposite owned Terminals [MANUAL §4.6 table; §4.4.4; §4.3 *Own*, *Circuit*; Fig F-1]. The 30-second Autonomous Period is dominated by a single randomized **Signal** image, worth 10 points to a robot that parks in the matching two-tile zone using the field-supplied image and **20 points** if it reads the team's own printed **Signal Sleeve** instead [MANUAL §4.4.2(3)]. Because Ownership, Capping and the Circuit are all scored on the *state of the field at rest after the buzzer*, the match is not a race to accumulate cones — it is a fight to be the top cone on as many Junctions as possible when time expires [MANUAL §4.3 *Score/Scoring* (c) *Scored at Rest*; §4.6 preamble]. The Game Design Committee said the quiet part out loud: "the best defensive strategy is to obtain and maintain *Junction Ownership* through offensive *Scoring*" [Q&A #130].

---

## 2. Match structure

| Phase | Length | What it is | Cite |
|---|---|---|---|
| Pre-Match setup | — | Robots placed Completely In Tile **A2/A5** (blue) or **F2/F5** (red), any orientation, touching the wall adjacent to their own Alliance Station; ≤1 **Pre-Loaded Cone**; Beacon staged in Substation Storage; Signal Sleeve placed on the nearest Signal | [MANUAL §4.4.1(2)] |
| Randomization | — | *After* referees signal setup complete, field personnel rotate all four Signals to one of three orientations chosen by the scoring system or a die throw | [MANUAL §4.4.1(3c)] |
| **Autonomous** | **0:30** | Pre-programmed only; one screen touch to start is the sole permitted human input; built-in 30 s timer must stay enabled | [MANUAL §4.4.2; §4.4.1(2e)] |
| Transition | **0:08** | 5 s to pick up Driver Stations, then a "3-2-1 go" countdown. Field personnel do not enter; robots stay hands-off | [MANUAL §4.3 *Match*; §4.4.3; `<G1>`] |
| **Driver-Controlled** | **2:00** | Drivers operate | [MANUAL §4.4.3] |
| ↳ **End Game** | **last 0:30** | Subset of Driver-Controlled. Beacons become eligible; Terminal parking scores | [MANUAL §4.3 *End Game*; §4.4.4] |
| **Total** | **2:30** | | [MANUAL §4.3 *Match*] |

**Unchanged from 2021-22 FREIGHT FRENZY:** period names and lengths are identical, including the 8-second transition [MANUAL, FF Part 2 §4.3 *Match*].

**Changed from 2021-22 — two structural changes that matter more than the timing:**

1. **Penalty direction flipped.** FREIGHT FRENZY: "Penalty points are **subtracted from the offending** Alliance's Score" [MANUAL, FF Part 2 §4.5.6]. POWER PLAY: "Penalty points are **added to the non-offending** Alliance's Score at the End of the Match" [MANUAL §4.4.6]. Magnitudes unchanged — Minor **10**, Major **30**, Warning **0**. This was a mid-preseason edit, landing in Revision 1.1 (8/31/2022) and restated in 1.2 [MANUAL, Part 2 revision history p.3].
2. **Ranking moved from totals to averages.** FREIGHT FRENZY sorted on *Total* Ranking Points / *Total* TBP1 / *Total* TBP2 / random [MANUAL, FF Part 1 §5.1]. POWER PLAY sorts on *Averaged* RP / *Averaged* TBP1 / *Averaged* TBP2 / **Highest Match Score (including Penalties)** / random — a fifth sort level that did not exist the year before [MANUAL, Part 1 §5.1.1].

**Remote variant** (`..._Part2_Remote.pdf`, 51 pp) keeps all period lengths and every point value identical, with three differences spotted: a single Team plays alone; the Circuit becomes a **predefined** path published per Match in Appendix H, and **a Cone Scored on any Junction outside that predefined Circuit negates the Circuit bonus** [MANUAL, Remote §4.4.4(2)]; and `<S2>` (contact outside the field perimeter) carries a Major Penalty rather than an automatic Yellow Card [MANUAL, Remote §4.7 table]. Remote Ranking Points are the Team's own final score after Penalties, not win/tie/loss [MANUAL, Part 1 Remote §3.4].

---

## 3. Scoring table

All values below are read from **§4.6 Scoring Summary, p.28**, recovered by geometry (`tools/extract-tables.py`) and confirmed against the rendered page image *and* independently against the prose in §4.4.2 / §4.4.3 / §4.4.4. Flat `pdftotext -layout` mis-paired this table — see §9.

Every achievement in this game is **Scored at Rest**: the field must come to rest after the period ends before the state is read [MANUAL §4.6 preamble; §4.3 *Score/Scoring* (c)].

| # | Scoring achievement | AUTO | TELEOP | END GAME | Cite |
|---|---|---:|---:|---:|---|
| 1 | Navigating: Robot Parked In Terminal **or** Substation | **2** | — | — | §4.6 tbl; §4.4.2(1) |
| 2 | Placement: Cone placed In a Terminal | **1** | — | — | §4.6 tbl; §4.4.2(2a) |
| 3 | Placement: Cone Secured on **Ground** Junction | **2** | **2** | — | §4.6 tbl; §4.4.2(2b), §4.4.3(1b) |
| 4 | Placement: Cone Secured on **Low** Junction | **3** | **3** | — | ″ |
| 5 | Placement: Cone Secured on **Medium** Junction | **4** | **4** | — | ″ |
| 6 | Placement: Cone Secured on **High** Junction | **5** | **5** | — | ″ |
| 7 | Signal: Robot Parked only on the Signal Zone matching the **field-supplied Signal** image | **10** | — | — | §4.6 tbl; §4.4.2(3a) |
| 8 | Signal: Robot Parked only on the two Tiles matching the **team-supplied Signal Sleeve** image | **20** | — | — | §4.6 tbl; §4.4.2(3b) |
| 9 | Placement: Cone Scored In Terminal | — | **1** | — | §4.6 tbl; §4.4.3(1a) |
| 10 | Navigating: Robot Parked In Terminal | — | — | **2** | §4.6 tbl; §4.4.4(3) |
| 11 | Ownership: Junction Owned **by Cone** (top Scored Cone) | — | — | **3** | §4.6 tbl; §4.4.4(1a) |
| 12 | Ownership: Junction Owned **by Beacon** (Capped) | — | — | **10** | §4.6 tbl; §4.4.4(1b) |
| 13 | Circuit: Completed Circuit (max 1 per Alliance per Match) | — | — | **20** | §4.6 tbl; §4.4.4(2) |
| — | **Minor Penalty** — added to the **non-offending** Alliance | 10 | 10 | 10 | §4.4.6 |
| — | **Major Penalty** — added to the **non-offending** Alliance | 30 | 30 | 30 | §4.4.6 |
| — | Warning | 0 | 0 | 0 | §4.4.6 |

**Scope traps in rows 1, 2, 9, 10, 11, 12** — all [MANUAL]:

- Row 2 (AUTO) is restricted to the Terminal **closest to the Alliance Station**; row 9 (TELEOP) accepts either Terminal [§4.4.2(2a) vs §4.4.3(1a)].
- Row 1 (AUTO park) also names only the *closest* Terminal, but adds the Substation [§4.4.2(1a-b)]. Row 10 (End Game) accepts *either* Terminal [§4.4.4(3)].
- Rows 11 and 12 are **mutually exclusive**; a Beacon takes precedence over the top Cone, so a Capped Junction pays **10, not 13** [§4.4.4(1)].
- Once Capped, further Cones or Beacons on that Junction score **zero** and cannot change Ownership [§4.4.4(1); `<GS7>`d].
- A Terminal is Owned when it holds ≥1 Scored Cone; Terminal Ownership itself pays **no points** — it only feeds the Circuit [§4.3 *Own*].
- Cones scored in Autonomous keep earning at the end of Driver-Controlled if they stay put — i.e. auto cones are counted twice, once in the auto subscore and again in the final field state [§4.4.2, closing line]. This is what makes TBP1 and the final score double-count the same cone.
- The **"Reference" column of §4.6 is published blank** — FIRST filled in no rule cross-references for this season [MANUAL, rendered p.28]. Nothing downstream can join scoring rows to rule tags here.

---

## 4. Bonuses, randomization and ranking

### 4.1 The Signal (the season's randomization)

| Property | Value | Cite |
|---|---|---|
| Signals on field | 4 (2 red, 2 blue), each a modified Cone, 4" base × 5" tall, ~2.55 oz | [MANUAL §4.3 *Signal*] |
| Images per Signal | 3, spaced 120° apart; identical image set on every Signal regardless of colour | [MANUAL §4.3 *Signal*] |
| Initial state | Image 1 facing the closest Alliance Station | [MANUAL §4.4.1(1a)] |
| **Reveal timing** | *After* referees signal setup complete and *before* the Match starts — field personnel rotate the Signals | [MANUAL §4.4.1(3c)] |
| **Reveal method** | One of three orientations, chosen by the **scoring system or a die throw** | [MANUAL §4.4.1(3c); App. E] |
| **Global or per-robot?** | **Global.** All Signals take the same orientation as seen from their Alliance Station; every Robot sees the same image | [MANUAL §4.4.1(3c)] |
| Signal Zones | 3 per Robot, each a **two-Tile** strip on that Alliance's half of the field | [MANUAL §4.3 *Signal Zone*; Fig E-3] |
| Zone boundary | The **solid portion** of the two Tiles — the outer perimeter tabs are excluded | [MANUAL Fig E-4] |
| Park requirement | Robot Parked **Completely In** the zone, and *only* that zone | [MANUAL §4.4.2(3); §4.6 tbl] |
| Value | **10** with the field Signal, **20** with the team Signal Sleeve | [MANUAL §4.4.2(3a-b)] |
| Signal is not a Scoring Element | Scores 0 on a Junction or in a Terminal; may be Herded or Plowed but not otherwise Controlled | [MANUAL §4.3 *Scoring Elements*; `<GS9>`] |
| Forfeit condition | Touching Robot or Driver Station once randomization has begun → Minor Penalty **and** that Robot loses Signal Bonus eligibility; the partner Robot keeps it | [MANUAL `<GS2>`] |

Note the design: the randomization is revealed **before** the match, is the **same for all four robots**, and is **not re-rolled**. It is a vision problem, not a reaction problem.

### 4.2 Ownership, Capping and the Circuit

| Mechanic | Rule | Cite |
|---|---|---|
| **Own a Junction** | Alliance holding the **top Scored Cone**, or a Scored Beacon, on that Junction | [MANUAL §4.3 *Own*] |
| **Own a Terminal** | ≥1 Scored Cone in it | [MANUAL §4.3 *Own*] |
| **Connection** | Formed between two **adjacent** Junctions, or a Terminal–Junction pair, Owned by the same Alliance | [MANUAL §4.3 *Connect*; Fig F-1] |
| **Adjacency** | A Junction Connects to up to **8** adjacent Junctions (orthogonal + diagonal, i.e. king moves). A **Terminal Connects to 3 Junctions** — the corner Junction and the two one step along each wall | [MANUAL Fig F-1] |
| **Circuit** | Continuous path of Connected Alliance-Owned Junctions linking the two matched Alliance-Owned Terminals; **20 pts, one per Alliance per Match** | [MANUAL §4.3 *Circuit*; §4.4.4(2)] |
| **Circuit needs Terminal cones** | Confirmed: a completed Circuit requires **at least one Cone In each of the Alliance's two Terminals**; orientation in a Terminal does not matter | [Q&A #48, #83; `<GS7>`b] |
| **Capping** | Beacon Completely On a Junction, or Completely On a Scored Cone on a Junction, or completely around the pole's circumference | [MANUAL §4.3 *Cap/Capping*] |
| **Beacon eligibility** | A Beacon introduced to the field **before** End Game is not eligible to Score; ≤1 Beacon Scored per Robot (second = Major Penalty + ineligible); colour must match the Alliance | [MANUAL `<GS14>`a-c] |
| **Beacons are protected** | Descoring a Scored Beacon in End Game = **Major Penalty per Beacon** | [MANUAL `<GS5>`c] |
| **Terminal geometry** | Each Alliance's two Terminals sit in **diagonally opposite corners** — one beside its own Alliance Station, one across the field | [MANUAL Fig B-2, Fig C-6] |

**The Junction grid**, read off Fig C-6 (columns V–Z left→right from the blue wall, rows 1–5 audience→back). Blue starts A2/A5 (V-side wall), red F2/F5 (Z-side wall):

| Row | V | W | X (centerline) | Y | Z |
|---|---|---|---|---|---|
| **5** | G | L | G | L | G |
| **4** | L | M | **H** | M | L |
| **3** | G | **H** | G | **H** | G |
| **2** | L | M | **H** | M | L |
| **1** | G | L | G | L | G |

Counts check out against §4.3: 9 Ground, 8 Low, 4 Medium, 4 High = 25 [MANUAL §4.3 *Junction*; Fig C-6] **[DERIVED: 9+8+4+4 = 25]**.

Two structural facts fall straight out of this map **[DERIVED from Fig C-6 + Fig B-2 + Fig F-1]**:

- The four **High** Junctions form a diamond around the centre. Two of them (X2, X4) sit **on the centerline** and are permanently contested; each Alliance gets exactly **one "home" High Junction** two tiles in from its own wall — **W3 for blue, Y3 for red** — with a **Ground Junction (V3 / Z3) directly in front of its own Substation**.
- The **cheapest Circuit needs no High Junction at all.** Blue's terminals sit at the V1 and Z5 corners; the chain **V1(G) → W2(M) → X3(G) → Y4(M) → Z5(G)** is a legal king-move path using only Ground and Medium Junctions. Red mirrors it: V5 → W4 → X3 → Y2 → Z1, same composition. **A robot that reaches 23.5" can build a Circuit.**

**Circuit cost arithmetic [DERIVED]** — Chebyshev distance from a Terminal's 3-Junction neighbourhood to the opposite Terminal's is 3, so the minimum chain is **4 Junctions**:

| Route | Junctions | Placement | Ownership | Terminal cones | Circuit | **Total** | **Cones** | Max reach needed |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Shortest: W1→X2→Y3→Z4 | L,H,H,L | 3+5+5+3 = 16 | 4×3 = 12 | 2×1 = 2 | 20 | **50** | **6** | 33.5" |
| Cheapest reach: V1→W2→X3→Y4→Z5 | G,M,G,M,G | 2+4+2+4+2 = 14 | 5×3 = 15 | 2 | 20 | **51** | **7** | 23.5" |
| Perimeter, no lift: W1→X1→Y1→Z1→Z2→Z3→Z4 | L,G,L,G,L,G,L | 3+2+3+2+3+2+3 = 18 | 7×3 = 21 | 2 | 20 | **61** | **9** | 13.5" |

*(Operands: placement values from §4.6 rows 3–6; ownership 3/Junction from §4.6 row 11; Terminal cones 1 each from §4.6 row 9; Circuit 20 from §4.6 row 13. Junction types from Fig C-6, adjacency from Fig F-1. **[JUDGMENT]** on the Terminal-neighbourhood sets {V1,V2,W1} and {Z5,Z4,Y5}, read from the Fig F-1 arrow diagram.)*

### 4.3 Ranking (Traditional events)

| Element | 2022-23 value | Cite |
|---|---|---|
| **Ranking Points** | Win **2**, Tie **1**, Loss / DQ / no-show **0** | [MANUAL Part 1 §3.4 *Ranking Points*] |
| **TBP1** | The Alliance's **Autonomous Period score** for that Qualification Match | [MANUAL Part 1 §3.4 *TieBreaker Points*] |
| **TBP2** | The Alliance's **End Game specific task score** for that Qualification Match | [MANUAL Part 1 §3.4] |
| **Sort order** | 1. Avg RP → 2. Avg TBP1 → 3. Avg TBP2 → 4. **Highest Match Score (including Penalties)** → 5. Random Electronic Draw | [MANUAL Part 1 §5.1.1] |
| Averaging basis | Matches played; **Surrogate** matches excluded, and a Surrogate is always a Team's 3rd Qualification Match | [MANUAL Part 1 §5.1.1; §3.4 *Surrogate Match*] |
| Surrogate / DQ / no-show | Contribute **zero** score, RP and TBP to the ranking calculation | [MANUAL Part 1 §5.1] |
| League ranking | Top **10** meet Matches (selected by the §5.1 sort order) + all league-tournament Matches; all Teams ranked over the same total (15 or 16) | [MANUAL Part 1 §5.2] |
| Elimination | RP not awarded; win/loss/tie only. Alliances of 2 or 3 Teams; only 2 play any one Match | [MANUAL Part 1 §4.10; §3.4 *Alliance*] |

**The tiebreaker points at the same target the game does. [JUDGMENT]** TBP2 is the "End Game specific task score", and in §4.6 the End Game column contains Terminal park (2), Cone Ownership (3), Beacon Ownership (10) and Circuit (20). An Alliance that plays for end-of-match field state therefore climbs the **third** sort key as well as the first. TBP1 rewards the Signal Sleeve directly: a 20-point sleeve park is 20 TBP1, double a 10-point field-signal park.

---

## 5. The rules that shaped play

Structure: Safety `<S#>` > Game-Specific `<GS#>` > General `<G#>`; Q&A forum rulings outrank all of them [MANUAL §4.5]. Penalty tiers: Minor **10** / Major **30** to the *non-offending* Alliance; Warnings are worth 0; Yellow Cards are additive and a second Yellow auto-converts to Red [MANUAL §4.4.6; §4.3 *Penalty*].

### 5.1 Rules that defined what a robot could physically do

| Rule | Threshold | Consequence | Cite |
|---|---|---|---|
| `<G14>` / `<RG02>` | Starting volume **18" × 18" × 18"**; Pre-Loaded Scoring Element may protrude | Not fixed in **30 s** → Robot removed from the field (no delay-of-game penalty); Team stays RP/TBP eligible if a Drive Team member is in the Station | [MANUAL `<G14>`; Part 1 `<RG02>`] |
| `<G14>` (2nd para) | **"After the start of a Match, the Robot may extend in any direction"** unless a Game-Specific rule says otherwise | — | [MANUAL `<G14>`] |
| — | **No Game-Specific rule restricts extension in POWER PLAY.** Grep of Part 2 for "expand/extend" returns only `<G14>`, `<G15>` and definitional text | Unlimited expansion | [MANUAL, Part 2 full-text scan] |
| `<G15>` | Alignment devices may extend past the 18" cube **only unpowered**; one Drive Team member may sight-align without delaying the Match | Minor per offence | [MANUAL `<G15>`] |
| `<G25>` | May not grab/grasp/attach to **any Game Element other than Scoring Elements** — so no grabbing Junction poles | Warning, then **Major** | [MANUAL `<G25>`] |
| — | A "V"-shaped guide that fully engages a Junction pole is **two points of contact** = illegal grasping under `<G25>` | Major | [Q&A #49] |
| `<G24>` | No deliberate part detachment; tethered parts that move independently count as detached | Minor; **Major + Yellow** if it affects gameplay | [MANUAL `<G24>`] |
| `<G29>` | May not use Game Elements to ease or amplify the difficulty of any scoring activity | **Major**, escalating to Yellow | [MANUAL `<G29>`] |
| — | Capping a Low/Med/High Junction with your own **upside-down Cone** to block opponents is a `<G29>` violation | Major | [Q&A #47] |
| `<G8>` | Field and Game Element tolerance **±1.0 inch**; pole rest angle varies Match to Match and during play | Design for it | [MANUAL `<G8>`; §4.3 *Junction* note; Fig C-5] |

### 5.2 Rules that defined how points were earned and taken away

| Rule | Threshold / trigger | Consequence | Cite |
|---|---|---|---|
| `<GS7>`a | Cone must be **Secured**, large opening toward the floor | No Score; **either** Alliance may remove it | [MANUAL `<GS7>`a; §4.3 *Secured*] |
| `<GS7>`c | Your Cone in the **opposing** Terminal | 0 points, no Ownership | [MANUAL `<GS7>`c] |
| `<GS7>`d | Anything added to a **Capped** Junction | 0 points, no Ownership change | [MANUAL `<GS7>`d] |
| `<GS11>` | Robot must be **Completely Outside** a Substation to Score | Minor per offence | [MANUAL `<GS11>`] |
| `<GS5>`a | Descore an **opposing Cone from a Junction** | **Minor** per Cone | [MANUAL `<GS5>`a] |
| `<GS5>`b | Descore a Cone from an **opposing Terminal** | **Major** per Cone | [MANUAL `<GS5>`b] |
| `<GS5>`c | Descore a Scored **Beacon** during End Game | **Major** per Beacon | [MANUAL `<GS5>`c] |
| — | Descoring **your own** Cone from a Junction or your own Terminal is legal | None | [Q&A #6] |
| — | Descoring in Autonomous is penalised the same as in Teleop | Minor | [Q&A #71] |
| — | A descore that breaks an opponent's Circuit **does not** get refunded; if judged intentional it can escalate to `<G30>` Major + Yellow | — | [Q&A #27] |
| `<GS6>`a | Control/Possess max **1 own Cone + 1 own Beacon** | Immediate Minor per excess element **+ another Minor per excess element every 5 s** | [MANUAL `<GS6>`a] |
| `<GS6>`b | Control/Possess an **opposing** Cone | Minor each + Minor/5 s. Manual's own example: knocking over an opposing unscored stack of 5 = **five Minor Penalties** | [MANUAL `<GS6>`b] |
| `<GS6>`c | Control/Possess an opposing **Beacon** | **Major** + Minor/5 s | [MANUAL `<GS6>`c] |
| `<GS6>`d | Scoring while over the possession limit | Minor per element Scored | [MANUAL `<GS6>`d] |
| `<GS6>`e | Exceptions: **Bracing** Scored Cones of either Alliance while placing; knocking over **your own** unscored stack; **Plowing** through any quantity (pushing an unsecured Cone off a Junction counts as Plowing) | Legal | [MANUAL `<GS6>`e] |
| `<GS10>` | Placing your Cone/Beacon on top of an **unscored** opposing Cone/Beacon | Minor per affected element; illegal placements removable without penalty. Rev 1.3 carved out the upside-down Cone on a Low/Med/High Junction | [MANUAL `<GS10>`; rev history] |
| `<GS9>`a | Controlling a Signal beyond Herd/Plow | Minor + Minor/5 s. Signal Sleeve damage is **not** penalised — bring spares | [MANUAL `<GS9>`a] |
| `<GS4>` | Launching a Scoring Element | Minor each. Rolling/Sliding allowed | [MANUAL `<GS4>`] |
| `<G6>` / `<GS1>`c | Scoring Elements in a Scoring Area **in contact with a Robot of that Alliance** score zero — **except** contact with a Cone in a Terminal, allowed so long as it is not Possessed | No points | [MANUAL `<G6>`, `<GS1>`c] |
| `<G5>` | Robot or Element In two or more Scoring Areas earns **only the highest-value** achievement | — | [MANUAL `<G5>`] |
| `<G27>` | Deliberately removing Game Elements from the field | Minor per element; elements removed *in an attempt to Score* are exempt | [MANUAL `<G27>`] |

### 5.3 Rules that governed contact and defence

| Rule | Threshold | Consequence | Cite |
|---|---|---|---|
| `<G28>` | Pinning / Trapping / Blocking an opposing Robot | **Minor for every 5 seconds**; must immediately retreat **≥3 ft (~1.5 Tiles)**. Not penalised in Autonomous unless part of a deliberate strategy, in which case the first Teleop action must be to retreat | [MANUAL `<G28>`] |
| `<GS8>`a | Impeding/obstructing an opponent scoring a **Cone on a Junction**, once the Cone is **In the Junction Area** | Immediate **Minor** + `<G28>` blocking penalties | [MANUAL `<GS8>`a] |
| `<GS8>`b | Blocking an opponent scoring **In their Terminal** | Immediate **Major** + `<G28>` | [MANUAL `<GS8>`b] |
| `<GS8>`c | Impeding an opponent scoring a **Beacon** on a Junction (protection starts once the Beacon is In the Junction Area) | Immediate **Major** + `<G28>` | [MANUAL `<GS8>`c] |
| — | *Junction Area* = the vertical cylinder of the Junction's own diameter | [MANUAL Fig C-8; Q&A #42] |
| `<GS12>` | Being **In or Blocking access to the opposing Substation** | Warning, then **Major + Minor every 5 s**; ≥3 ft retreat within 5 s; escalates to Yellow Cards "quickly". **Explicitly overrides `<G7>` — a Disabled Robot still earns these** | [MANUAL `<GS12>`; `<GS1>`b] |
| `<GS3>` | Interfering with the opponent's Autonomous scoring | **Major** per occurrence. **Carve-out: interactions at the centerline Junctions (column X) are never Interference** | [MANUAL `<GS3>`; Q&A #129] |
| — | Crossing the centerline in Auto to score a centerline Junction, and staying there for the rest of the period, breaks no rule provided the Robot is Parked at the end | Legal | [Q&A #43] |
| — | Two Robots both bending the same pole while both purely attempting to Score is not `<GS3>` Interference | Legal | [Q&A #129] |
| `<G26>` | Destruction / damage / tipping / entanglement — but robot-to-robot contact and defence are expected | Deliberate or chronic → **Major + Yellow** | [MANUAL `<G26>`] |
| `<G30>` | Egregious behaviour | Major + Yellow and/or Red; repeat → Team disqualification for the competition | [MANUAL `<G30>`] |

### 5.4 The Human Player and the Substation

`<GS13>` is eight clauses, **each a Minor Penalty per offence** [MANUAL `<GS13>`]: no handling Substation Storage elements before the Match starts (Pre-Loads excepted); elements enter the field **only** via the Substation; only during Driver-Controlled; only into your own Substation and never Propelled out; no tools; **only one element in the Substation at a time** (though there is no cap on how many may be *in* it); the Human Player may not break the field-perimeter plane while a Robot is In the Substation; and a Robot may not enter the Substation while the Human Player is placing. A **Disabled** Robot in a Substation is not treated as a safety hazard, so placement continues [MANUAL `<GS13>`g-h notes; `<GS12>` note]. Note the asymmetry this creates: your Human Player is the sole cone supply for 20 of your 30 cones [MANUAL §4.4.1(1d-e)], and `<GS12>` makes camping their doorway a Major-Penalty offence.

---

## 6. Robot archetypes that season

### Build envelope [MANUAL, Part 1 §7]

| Constraint | Value | Cite |
|---|---|---|
| Starting size | 18" cube, self-supported, restraints must stay attached all Match | `<RG02>` |
| Expansion after start | **Unlimited, any direction** | `<G14>`; `<RG02>` |
| Robot weight | **No weight limit appears anywhere in Part 1 §7** | [MANUAL, Part 1 full-text scan] |
| DC motors | **Max 8**, from a closed list (TETRIX, NeveRest, MR/MATRIX, REV HD Hex, REV Core Hex) | `<RE10>` |
| Servos | **Max 12**, ≤6 V, three-wire; VEX EDR 393 counts as a servo | `<RE11>` |
| Control | Control Hub, **or** allowed phone + Expansion Hub; **plus at most one additional Expansion Hub**; unlimited SPARK Mini controllers and Servo Power Modules | `<RE06>`, `<RE08>`, `<RE09>` |
| Sensors | I²C / digital / encoder / analog ports only — **not USB** | `<RE12>`; [Q&A #28] |
| Power | Exactly one 12 V main battery, one main switch | `<RE01>`, `<RE03>` |
| **Beacon** (Team Scoring Element) | Must fit in a **4" cube** and not fit in a **3" cube**; colour must match the Alliance; team number labelled; **no electronics**; must not resemble a COTS scoring element. **Two needed** (one red, one blue) | `<TE01>`–`<TE06>` |
| **Signal Sleeve** | Printed from the FIRST template; **only** the team number and team images may be changed; **no add-ons after printing**; images may not resemble the season's Signal images | `<SS01>`–`<SS03>`; [Q&A #131: the trapezoid may be filled with a solid colour or pattern] |

**The single most consequential line in Part 1 is `<G14>`'s second paragraph.** An 18" cube at the buzzer, unlimited afterwards, with no rule anywhere in Part 2 constraining extension. Everything below follows from that.

### The archetypes

| Archetype | What it needed | Motor budget (of 8) | Where the points came from | Verdict |
|---|---|---|---|---|
| **Home-High cycler ("substation camper")** | Horizontal extension of ~1–2 tiles into the Substation + a lift to 33.5" + a cone gripper. Parks between its Substation and its home High Junction (W3 blue / Y3 red) and **never drives** | 4 drive + 2 lift + 1–2 extension/turret | 5/cone, ~2–4 s cycles, 20–35 cones plausible | **The meta.** Explicitly ruled legal: reaching into the Substation, retracting Completely Outside, then scoring behind you "doesn't violate any rules" [Q&A #42] |
| **Roaming High scorer** | Same lift, plus alignment on a 1"-diameter spring-mounted pole with ±1" field tolerance and a rest angle that drifts during the Match [`<G8>`; Fig C-5] | 4 drive + 2 lift + 1 wrist | 5/cone but with travel time and pole-flex misses | Higher variance; a miss leaves an unsecured cone that **either Alliance may remove** [`<GS7>`a] |
| **Ground/Low spreader** | A drivetrain and a floor-level or 13.5"-capable gripper. **No lift at all** | 4 drive + 1–2 gripper | 2–3/cone placement **but +3 Ownership per fresh Junction**, and can build the perimeter Circuit | Structurally undervalued — see §7 |
| **Medium-reach Circuit builder** | Reach to 23.5" | 4 drive + 2 lift | Can complete the **G/M diagonal Circuit** for 51 points from 7 cones | The best points-per-mechanism ratio in the game **[DERIVED, §4.2]** |
| **Auto specialist** | Camera + Signal Sleeve detection, one preload, dead-reckon to a two-tile zone | shares the above | **25 points from one robot**: 20 sleeve park + 5 preload on a High Junction. Two robots = **50** | **[DERIVED: 20 + 5; 2 × 25]** Highest points-per-dollar in the season |
| **Beacon capper** | Ability to place a ≤4" object on a Junction in the last 30 s | any | **10** per Junction, and it **locks** the Junction: nothing else scores there and descoring it is a Major | Cheap. Every robot could do it; most alliances only had two Beacons to place |

**Two-team-program note [JUDGMENT].** The Beacon rules mean each team needs **two** Team Scoring Elements (red and blue) [`<TE01>`], and the Signal Sleeve is a printed sheet with a re-print cost near zero and no penalty for damage [`<GS9>`a]. A small-budget team's cheapest possible upgrade path in POWER PLAY was: (1) print sleeves and get the auto bonus to 20, (2) build a 4"-cube Beacon, (3) worry about a lift last.

---

## 7. The strategic lesson

**The scoring table advertised a height ladder. The game was actually a graph-colouring problem, and the ladder was its smallest term.**

Look at where the points actually sat, per cone, at the moment of placement **[DERIVED — operands: §4.6 rows 3–6 placement, row 11 Ownership = 3]**:

| Cone placement | Placement | + Ownership if it's the first cone there | **Marginal total** |
|---|---:|---:|---:|
| Into a Terminal | 1 | 0 (Terminal Ownership pays nothing directly) | **1** |
| Onto a **High** Junction **you already own** | 5 | 0 | **5** |
| Onto a fresh **Ground** Junction | 2 | +3 | **5** |
| Onto a fresh **Low** Junction | 3 | +3 | **6** |
| Onto a fresh **Medium** Junction | 4 | +3 | **7** |
| Onto a fresh **High** Junction | 5 | +3 | **8** |
| Beacon onto a Junction you already own by Cone | — | 10 − 3 = **+7** | **7**, and permanent |

**A cone on a bare Ground Junction was worth exactly as much as a cone stacked on your own High Junction.** A cone on a bare Low Junction was worth *more*. The 2/3/4/5 ladder that every kickoff analysis leads with is a **3-point spread**; the Ownership bonus attached to *breadth* is 3 points on its own, and the Circuit is 20.

Run the two strategies over the same 20-cone budget **[DERIVED]**:

| Plan | Composition | Placement | Ownership | Terminals | Circuit | **Total** |
|---|---|---:|---:|---:|---:|---:|
| **A — stack the home High Junction** | 20 cones × High(5), 1 Junction owned | 20 × 5 = 100 | 1 × 3 = 3 | 0 | 0 | **103** |
| **B — spread one cone per Junction** | 9 Ground + 8 Low + 3 Medium = 20 Junctions owned, + 2 Terminal cones | (9×2)+(8×3)+(3×4) = 54 | 20 × 3 = 60 | 2 | 20 | **136** |

*(Plan B's Junction mix comes from the Fig C-6 census: 9 Ground, 8 Low, 4 Medium, 4 High. Plan B needs 22 cones counting the two Terminal cones; Plan A's 20 all go on one pole. Even at 22 vs 20 cones, Plan B is +33.)* **Plan B never reaches above 23.5 inches.**

### What was underpriced

1. **The Signal Sleeve.** Ten extra points per robot, twenty per alliance, for a printed sheet of paper that costs nothing and cannot be penalised if damaged [`<GS9>`a; §4.4.2(3)]. **[DERIVED: 20 − 10 = 10 per robot; ×2 robots = 20 per alliance.]** It also feeds TBP1, the *second* ranking sort key. No mechanism, no motor, no risk.
2. **Ground Junctions.** Nine of them, zero lift required, 5 marginal points each, and three of them (V1, X3, Z5 / V5, X3, Z1) sit on the cheapest Circuit diagonal. They were treated as a consolation prize.
3. **The Circuit's true cost.** 20 points that the scoring table presents as a single line item, achievable with **6–7 cones** on Junctions no taller than a Medium **[DERIVED, §4.2 table]**. Most analyses treated the Circuit as a stretch goal for elite alliances; the field map says otherwise.
4. **The Beacon.** +7 marginal over cone Ownership, and it makes a Junction **permanently yours**: nothing else scores there, and descoring it is a Major Penalty [`<GS7>`d, `<GS5>`c, `<GS8>`c]. A ≤4" plastic cube with no electronics [`<TE03>`, `<TE05>`].

### What was overrated

**The tall stacker.** Every repeat cone on a Junction you already own pays flat placement value with no Ownership attached, buys nothing toward the Circuit, and carries the season's worst cycle risk: a 1"-diameter spring-mounted pole, ±1" field tolerance, and a rest angle that changes *during* the match [`<G8>`; §4.3 *Junction* note]. A near-miss is not a zero — it is an **unsecured cone that the opposing alliance is entitled to remove** [`<GS7>`a].

### The generalizable lesson

**When a game pays for the *state of the field at rest* rather than for *events as they happen*, the last cycle of the match is worth more than any earlier one, and the game stops being a throughput problem.** POWER PLAY paid 5 points for a cone the instant it landed — but 3 per Junction, 10 per Beacon and 20 for the Circuit only for whatever survived to the buzzer [§4.6 preamble; §4.3 *Scored at Rest*]. Ownership is the **top** cone, so it flips for the cost of one opposing cone and depth buys no protection: a 6-cone stack is taken exactly as cheaply as a 1-cone stack. Which is why the GDC's advice was not "play defence" but *"obtain and maintain Junction Ownership through offensive Scoring"* [Q&A #130] — in a state-scored game, the offence **is** the defence, and the winning play is to be spread wide and topping up when the buzzer sounds.

The corollary, and the trap: state-scored breadth is fragile. Plan B's 136 points assume you still hold all 20 Junctions at rest. In practice the last 30 seconds became a re-topping war, which is precisely why the End Game subscore (TBP2) was the tiebreaker that separated otherwise-equal teams.

---

## 8. Signals for BIOBUZZ

1. **First question on 2026-09-12: is this game event-scored or state-scored?** Look for the phrase *Scored at Rest* / *Scored at End of the Period* in the definitions, and for any achievement (Ownership, control, pattern, circuit) evaluated on final field configuration. If state-scored, the endgame decides matches, breadth beats depth, and defence collapses into offence. If event-scored, throughput wins and the analysis is a cycle-time problem.
2. **Compute marginal value before sticker value.** Build the §7 table on day one: for each objective, *(placement) + (first-time bonus, if any)* vs *(placement alone for repeats)*. POWER PLAY's headline 5-point High Junction and its 2-point Ground Junction were worth **the same** on the marginal cone. Rank by marginal points per cycle, never by the biggest number in the table.
3. **Read the Team-manufactured-element rules on day one** (Part 1 §7.4 / §7.5 here; whatever the 2026-27 equivalent is). POWER PLAY hid a **2× multiplier on the auto bonus** behind a printable paper sleeve with a near-zero build cost. Anything the manual lets the *team* fabricate is usually the highest return per dollar in the game.
4. **Map the field graph before you design the robot.** Fig C-6 (which Junction is which type) plus Fig F-1 (what connects to what) tell you the cheapest Circuit needs only 23.5" of reach — a fact the scoring table cannot reveal. Do the equivalent census and adjacency read for BIOBUZZ before committing to a lift height.
5. **Find the zero-travel cycle.** Under an unlimited-expansion rule, locate the (source, sink) pair a stationary robot can serve by extension alone. In POWER PLAY that pair was *(own Substation, home High Junction)* and it defined the meta [Q&A #42]. **Check whether 2026-27 still permits unlimited expansion** — the 2024-25+ manuals reintroduced expansion limits, so this may no longer hold.
6. **Check the penalty direction before trusting any score-derived metric.** POWER PLAY **added** penalty points to the non-offending alliance [§4.4.6]; FREIGHT FRENZY **subtracted** them from the offender [FF §4.5.6]. In an additive season, opponents' fouls inflate *your* final score, so OPR/EPA built on final scores attributes their discipline problems to your robot. Confirm the direction, and prefer penalty-free scores for scouting.
7. **Expect averaged ranking, and check for a fifth sort key.** Averaged RP/TBP arrived in 2022-23 and stayed, along with "Highest Match Score (including Penalties)" ahead of the random draw [Part 1 §5.1.1]. Identify what TBP1 and TBP2 actually measure — in POWER PLAY they pointed at exactly the two objectives (Signal Sleeve, End Game state) a naive read would under-weight.
8. **Budget for the Q&A to reshape the meta in October–November.** §4.5 states forum rulings take precedence over the manual, and POWER PLAY's forum closed two live loopholes (`<G29>` on the upside-down-cone blocker [Q&A #47]; `<G25>` on V-shaped pole guides [Q&A #49]) and *opened* one strategy by blessing the substation-camp cycle [Q&A #42]. Any strategy memo written from the V0 manual alone has a shelf life of about six weeks.
9. **Watch the tolerance clauses.** `<G8>`'s ±1.0" and the "pole rest angle may vary Match to Match and during gameplay" note [§4.3] are the difference between a mechanism that works on your practice field and one that works at a competition. Find the 2026-27 equivalents and design to the worst case.

---

## 9. Extraction notes

*This section feeds the harness-generalization report.*

### Rule census — Part 2 (Traditional, Rev 1.3)

| Prefix | Distinct rules | Numbering | Tag occurrences in body text |
|---|---:|---|---:|
| `S` (Safety) | 3 | `<S1>`–`<S3>` | 6 |
| `G` (General) | 30 | `<G1>`–`<G30>` | 77 |
| `GS` (Game-Specific) | 14 | `<GS1>`–`<GS14>` | 52 |
| **Total** | **47** | — | **135** |

Derived from a full-text scan of `<[A-Z]{1,3}\d{1,3}>` over the `pdftotext -layout` dump of Part 2.

**Violation / consequence coverage**, counted programmatically from the §4.7 Rule Summary table (geometry-extracted, pp. 29–35):

- **66** sub-clause rows in §4.7 (rules are split into lettered clauses: `<G13>`e, `<G16>`b/c, `<GS5>`a/b/c, `<GS6>`a-d, `<GS13>`a-h, `<GS14>`a-c…).
- **46** of the 47 rules appear in §4.7 — only `<GS1>` (General Rule Exceptions) is absent.
- **37** carry a stated Consequence. The 10 that do not are `<G1>`–`<G5>`, `<G7>`–`<G10>` and `<GS1>` — §4.7 bands `<G1>`–`<G10>` as "General Rules – Further definitions, no Penalties earned" (though `<G6>` does carry a scoring consequence).
- **32** specify a Minor and/or Major Penalty marker: `<S3>`, `<G11>`–`<G13>`, `<G15>`–`<G30>`, `<GS2>`–`<GS6>`, `<GS8>`–`<GS14>`. The other 5 consequence-bearing rules resolve to Disable/Card (`<S1>`, `<S2>`), removal from the field (`<G14>`), or "does not Score" (`<G6>`, `<GS7>`).

### Rule census — Part 1 (Traditional, Rev 1.2)

`tools/parse-legacy-manual.py` reported **97 rules across 9 prefixes** over 70 pp, 208 tag occurrences: `C` 28, `DS` 8, `I` 10, `RE` 17, `RG` 8, `RM` 6, `RS` 10, `SS` 4, `TE` 6. **Part 1's count is trustworthy** because Part 1 zero-pads its tags (`<RG01>`, `<RE01>`, `<TE01>`, `<C08>`) — see the defect below.

### What the tooling got wrong on this manual

**1. `parse-legacy-manual.py` silently dropped 45% of Part 2's rules.** Its `RULE_TAG` regex is `<([A-Z]{1,3})(\d{2,3})>` — **two-to-three digits required**. POWER PLAY numbers rules without zero-padding (`<S1>`, `<G9>`, `<GS8>`), so the parser reported `rules=26 (G:21 GS:5)` against an actual **47**. It missed `<S1>`–`<S3>`, `<G1>`–`<G9>` and `<GS1>`–`<GS9>` — **21 rules**, including most of the ones that actually shaped play: `<G5>` (highest-value-only), `<G6>` (contact voids score), `<GS1>` (rule exceptions), `<GS5>` (descoring), `<GS6>` (possession limits), `<GS7>` (Junction/Terminal constraints), `<GS8>` (Junction defence), `<GS9>` (Signal). *A dossier built on the parser's output alone would have omitted the descoring and possession rules entirely.*

   **Scope:** verified the same defect hits **2020-21 ULTIMATE GOAL** and **2021-22 FREIGHT FRENZY** (both use `<G1>`…`<G9>`, `<GS1>`…`<GS9>`, `<S1>`–`<S3>`). **2023-24 CENTERSTAGE is unaffected** (zero-padded `<G01>`). So the bug costs ~21 rules per manual across three of the seven legacy seasons. **Fix: change `\d{2,3}` to `\d{1,3}`.** The docstring already advertises the correct vocabulary (`<[A-Z]{1,3}[0-9]{2,3}>`), so this is a spec bug, not a typo — the spec is wrong about the corpus.

**2. `parse-legacy-manual.py` cannot take `--tsv` and `--json` together.** `parse-legacy-manual.py <pdf> --tsv A.tsv --json B.json` re-entered the *output* path as an input PDF and printed `### pp_p2.json: 0pp rules=0` with a spurious "NO <TAG> RULES FOUND" warning. Pass one output flag at a time.

**3. The documented `--tsv /tmp/<season>.tsv` invocation does not work on this Windows host.** Run under Git Bash it resolved to `C:/Users/.../AppData/Local/Temp/2022-23.tsv` and the tool then reported `### MISSING <that path>` — no readable file. Absolute Windows paths work. The harness README's example invocation should be updated.

**4. The parser's `violation` column is unusable on this manual.** Its `VIOLATION` regex expects a labelled `Violation:` / `Penalty:` line. POWER PLAY states consequences in running prose ("A Minor Penalty will be assessed…"), so the column captured mid-sentence fragments. Worst case, `<GS13>` came out as `for each Perimeter while a offense Robot is in the Substation` — a splice of two unrelated clauses from different sub-rules. It reported `violations=18` for Part 2 and `violations=2` for Part 1; neither number means anything. **The authoritative source for consequences in this era is the §4.7 Rule Summary table, recovered by geometry.**

**5. `extract-tables.py` recovered all 10 Part 2 tables but returned no captions.** Every table was logged "(no caption on page)" because this manual labels its tables with **section headings** (`4.6 Scoring Summary`, `4.7 Rule Summary`) rather than `Table N-M:` captions. Table identity had to be recovered by page number. It also flagged the p.3 revision-history table `SPLIT?` — a false positive (merged header cell, not a page-break split).

**6. The geometry extractor merged the four Junction rows of the scoring table into a single cell** — p.28 came out as `Placement: Cone Secured on Junction: Ground Low Medium High | 2 3 4 5`. Ordering was correct, but the label-to-value pairing had to be confirmed against the rendered page *and* the §4.4.2/§4.4.3 prose. Both confirm **2/3/4/5**.

   **The house rule against flat text was measurably load-bearing here.** `pdftotext -layout` on the *same* table printed `Ground Junction  3 / Low Junction  4 / Medium Junction` — **off by one row** — with the `5` floating free four lines below and the End Game values (2/3) landing inside the Driver-Controlled block. Anyone reading that text builds a scoring model where a Ground Junction is worth 3 and a High Junction is worth nothing.

**7. Not a tool failure, but worth recording: §4.6's "Reference" column is published blank.** FIRST shipped the scoring summary with no rule cross-references for this season, so no scoring row can be joined to a rule tag automatically.

### Corpus note — the brief was wrong about the Q&A archive

The harness brief states there is **no** Q&A archive in the corpus for this season. **There is one:** `manuals/archive/supplemental/2022-23_POWERPLAY_Complete_QA.html` — 388 KB, **375 Q&A items**, dated through the season. Unlike every other season in `supplemental/` it exists **only as `.html`** (no `.pdf` or `.txt` sibling), which is almost certainly why an inventory keyed on extension missed it. Parsed here with a short regex over `<div class="item">` blocks (`name="number"` / `name="question"` / `name="answer"`).

This matters, because §4.5 states forum rulings **take precedence over the manual**, and at least three rulings change how the manual reads:

- **Q&A #48 / #83** — a completed Circuit requires ≥1 Cone in *each* of the Alliance's two Terminals. The §4.3 *Circuit* definition alone does not say this.
- **Q&A #47** — the upside-down-cone Junction blocker is a `<G29>` violation. Rev 1.3 had just carved that case *out* of `<GS10>`, so the manual alone reads as if the strategy were legal.
- **Q&A #49** — a "V"-shaped pole guide is illegal grasping under `<G25>`, which the rule text does not obviously cover.

**Recommendation for the harness:** index `manuals/archive/supplemental/` by **filename stem**, not by extension, and add an HTML branch to the Q&A ingestion path. Also worth confirming whether the 2024-25 and 2025-26 Q&A archives (also `.html`) are being picked up.

### Verification trail

- Rules: full-text tag scan of Part 2 + §4.7 Rule Summary via `tools/extract-tables.py`, cross-read against §4.5 prose.
- Scoring: `tools/extract-tables.py` on p.28, cross-checked against `tools/render-pages.py --pages 28` (image read directly) and against §4.4.2 / §4.4.3 / §4.4.4 prose. Three independent agreements.
- Field geometry: `tools/render-pages.py --pages 38,39,41,42,43,46,48,54` for Fig B-2, C-1/C-2, C-5/C-6, C-7/C-8, C-9/C-10, E-3/E-4, F-1/F-2/F-3, F-24, plus a 300-dpi crop of Fig F-1 to resolve the Terminal→Junction adjacency.
- Part 1: `pdftotext -layout` + targeted reads of `<RG02>`, `<RE05>`–`<RE12>`, `<TE01>`–`<TE06>`, `<SS01>`–`<SS03>`, §3.4, §5.1–5.2.
- Prior-season comparisons: direct greps of the 2020-21, 2021-22 and 2023-24 `.txt` dumps in `manuals/archive/`.
