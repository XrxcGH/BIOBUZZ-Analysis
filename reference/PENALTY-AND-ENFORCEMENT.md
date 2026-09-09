# BIOBUZZ Penalty & Enforcement Reference

**Purpose:** kickoff-day reference for reading Section 11 (Game Rules) of the BIOBUZZ Kickoff Competition Manual (releases **September 12, 2026**). Everything below is either already locked for BIOBUZZ, or is the prior-season baseline you should diff the new Section 11 against.

**Evidence labels used throughout:**

| Label | Meaning |
|---|---|
| **[CONFIRMED-BIOBUZZ]** | Present in the BIOBUZZ V0 Pre-Season manual (2026-07-31), in a section FIRST has already finalized |
| **[BASELINE]** | Verbatim from DECODE (2025-26) and/or INTO THE DEEP (2024-25). The most likely starting point for BIOBUZZ, but **not** a BIOBUZZ number |
| **[HISTORICAL-PATTERN]** | Repeats across 3+ seasons; strong prior, no BIOBUZZ evidence |
| **[SPECULATION]** | Reasoned inference. Treat as a hypothesis to test against the real manual |
| **UNVERIFIED** | Could not be confirmed from the corpus |

**Primary sources** (all paths relative to `C:/Users/ericj/Documents/BIOBUZZ Analysis/`):

- `manuals/2026-27_BIOBUZZ/BIOBUZZ_V0_layout.txt` + `manuals/2026-27_BIOBUZZ/sections/*.txt` — BIOBUZZ V0
- `manuals/_reference_prior_seasons/2025-26_DECODE_Section11_text.txt` — DECODE Section 11 V15
- `manuals/archive/2025-26_DECODE_Competition_Manual_TU32.txt` — DECODE full manual (final, TU32)
- `manuals/_reference_prior_seasons/2024-25_ITD_Section11_text.txt` — ITD Section 11 V12
- `manuals/archive/2024-25_INTO_THE_DEEP_Competition_Manual_V14.txt` — ITD full manual
- `manuals/archive/**` + `manuals/archive/wayback/**` — 2015-16 .. 2023-24 Part 1 / Part 2 manuals
- `manuals/archive/supplemental/2025-26_DECODE_Complete_QA.html` — official DECODE Q&A archive

---

## 0. TL;DR — the 12 things that matter

1. **A FOUL is a *credit to your opponent*, not a deduction from you.** [BASELINE: DECODE §10.6 Table 10-4] A MAJOR FOUL does not reduce your score; it raises theirs by 15. The margin swings by the full face value.
2. **But foul points you *receive* are stripped out of the ranking tiebreakers.** [CONFIRMED-BIOBUZZ] Advancement Table 4-2 sorts on "Average Qualification MATCH Points (**excluding FOULS**)". Fouls decide *who won*; they do not pad your average.
3. **BIOBUZZ Section 11 will be written differently from DECODE.** [CONFIRMED-BIOBUZZ] FIRST says so explicitly in §1.4.1 — fewer bright-line thresholds, more "spirit of the rule," and the example they chose is **exactly the protected-zone archetype**: "strategically blocking an opponent from access to their gate vs. going into an opponent's gate zone."
4. **A brand-new enforcement instrument exists: the Competition Integrity Contract (CIC).** [CONFIRMED-BIOBUZZ §1.5] Zero occurrences in DECODE or ITD. It creates a *non-referee*, *non-in-match* escalation path running to FIRST HQ, with team suspension/removal as the ceiling.
5. **"Escalation Guidelines (coming soon)"** [CONFIRMED-BIOBUZZ §1.5.3] — a **separate document outside the Competition Manual** will govern escalations. Watch for it; it may carry enforcement rules that historically lived in Section 10.6.
6. **The BIOBUZZ Inspection (I) rules carry no stated violations at all.** [CONFIRMED-BIOBUZZ] DECODE I303/I305 each carried RED CARD / DISQUALIFICATION. BIOBUZZ I301–I304 have zero `Violation:` lines. See §5.4 — this is either a deliberate softening or the penalties moved to Section 11.
7. **`Verbal warning` became a capitalized, defined penalty tier in DECODE.** ITD uses the phrase 0 times in caps; DECODE 26 times; BIOBUZZ V0 keeps `VERBAL WARNING` in the glossary. [CONFIRMED-BIOBUZZ Glossary]
8. **YELLOW CARDS are additive and convert to RED on the second one** — including two in one match. [HISTORICAL-PATTERN, unbroken since 2016-17]
9. **In Playoffs, cards attach to the whole ALLIANCE**, not the team. [HISTORICAL-PATTERN since 2016-17]
10. **Referees do not track *which rule* each foul came from.** [BASELINE: DECODE §13.4] Only counts are recorded. Question-box appeals of individual foul calls are near-hopeless; ask about interpretation instead.
11. **Deliberately forcing an opponent into a foul is itself a foul, and there is no "no call" outcome** — somebody gets penalized. [BASELINE: DECODE G210 + Q&A #80]
12. **The most expensive rules are never the point values** — they are the ones that hand the opponent a RANKING POINT or award them a scoring achievement outright.

---

## 1. The current enforcement ladder (full)

### 1.1 Penalty tiers — definitions and point values

Source: DECODE §10.6 Table 10-4 (`manuals/archive/2025-26_DECODE_Competition_Manual_TU32.txt` ~L2873) and DECODE Glossary; ITD §10.6 Table 10-4 (~L2379).

| Tier | Point effect | Who assesses | Scope | Persists? |
|---|---|---|---|---|
| **VERBAL WARNING** | none | Event staff **or** Head REFEREE | Team | Cleared after Practice MATCHES; **persists** from Qualification through subsequent tournament phases unless stated otherwise [BASELINE: DECODE §10.6.1] |
| **MINOR FOUL** | **+5** to the *opponent's* MATCH point total | REFEREE (any) | Assessed against the **ALLIANCE** | Match only |
| **MAJOR FOUL** | **+15** to the *opponent's* MATCH point total | REFEREE (any) | Assessed against the **ALLIANCE** | Match only |
| **YELLOW CARD** | none directly | **Head REFEREE only** | Team (Quals) / whole ALLIANCE (Playoffs) | Carried into subsequent MATCHES within the phase; cleared at end of Practice, Qualification, and division Playoff MATCHES |
| **RED CARD** | → DISQUALIFIED for that MATCH | **Head REFEREE only** | Team (Quals) / whole ALLIANCE (Playoffs) | Team still carries a YELLOW forward |
| **DISABLED** | ROBOT dead for rest of MATCH | REFEREE (declared per T202) | ROBOT | Match only |
| **DISQUALIFIED** | 0 MATCH points **and 0 RANKING POINTS** in a Qual MATCH; 0 MATCH points for the ALLIANCE in a Playoff MATCH | consequence of RED CARD or specific rules | Team / ALLIANCE | Match only |
| **ALLIANCE ineligible for [named] RP** | Forfeits a specific RANKING POINT | REFEREE | ALLIANCE | Match only |

Notes:

- The last two rows (`VERBAL WARNING`, `ALLIANCE is ineligible for RP`) were **added to Table 10-4 in DECODE**; ITD's Table 10-4 has only six rows. [BASELINE, verified by diff of the two tables]
- **DISABLED ≠ DISQUALIFIED.** DISABLED costs you the rest of the match's scoring; DISQUALIFIED zeroes the match *and* the RP. A DISABLED robot can still earn fouls for its alliance — Q&A #104 confirms it explicitly.
- Only the **Head REFEREE** may issue cards. Field referees call fouls. [BASELINE: DECODE §10.6.1, §10.7]

### 1.2 Duration vocabulary (the hidden thresholds)

[BASELINE: DECODE §10.6 and ITD §10.6, identical wording]

| Term | Meaning | Why it matters |
|---|---|---|
| **MOMENTARY** | fewer than ~3 seconds | The universal grace window. Many rules are only violated if the state is *greater-than-MOMENTARY* |
| **CONTINUOUS** | more than ~10 seconds | Usually the RED CARD trigger on ROBOT-behavior rules |
| **REPEATED** | more than once **within a MATCH** | The automatic escalation trigger. Note the scope is the *match*, not the event |

"Subsequent violations occur during the event" is a **different and broader** clock than REPEATED — it spans matches and phases. Do not conflate them.

### 1.3 How violation wording compounds — the grammar of `Violation:` lines

This is the single most under-read table in the manual. Source: DECODE §10.6.4 Table 10-6; ITD §10.6.4 Table 10-6.

| Written as | What actually happens | Worked example |
|---|---|---|
| `MINOR FOUL` | One MINOR against the ALLIANCE | +5 opp |
| `MAJOR FOUL and YELLOW CARD` | MAJOR to the ALLIANCE **plus** a card to the *team*, presented after the match | +15 opp, team carries YELLOW |
| `MINOR FOUL per SCORING ELEMENT over the limit` | One MINOR **per element** beyond the cap | 3 over the cap = +15 opp |
| `MINOR FOUL. MAJOR FOUL if REPEATED.` | **Both**, cumulatively. The repeat does not *replace* the minor | 2 violations in one match = 5 + 15 = **+20 opp** |
| `MINOR FOUL and an additional MINOR FOUL for every 3 seconds in which the situation is not corrected` | 1 + ⌊duration ÷ interval⌋ | DECODE: 15 s = **6 MINOR FOULS = +30 opp**. ITD's 5-s version: 15 s = 4 fouls |
| `MAJOR FOUL plus YELLOW CARD if REPEATED.` | 2nd violation earns a *second* MAJOR **and** the card | 2 violations = +30 opp + YELLOW |
| `VERBAL WARNING. YELLOW CARD if subsequent violations occur during the event.` | Warning first; the card lands on **any** later violation of that rule anywhere in the event, including later in the same match | — |
| `MAJOR FOUL and the opposing ALLIANCE is awarded the [X] RP.` | RP is granted **regardless** of whether they earned it on the field | Overrides normal play |
| `MAJOR FOUL and YELLOW CARD. MAJOR FOUL and RED CARD if opponent ROBOT is unable to drive.` | Only **one** MAJOR per violation; the card severity is what changes | +15 opp + RED |

The **cumulative** reading of `X. Y if REPEATED.` is the single most common student misreading. It is not "upgrade the penalty" — it is "add another penalty."

### 1.4 Card mechanics

[BASELINE: DECODE §10.6.1–10.6.3; substantively unchanged since 2016-17]

- YELLOW CARDS are **additive**: a second YELLOW auto-converts to a RED, *including two in a single MATCH*.
- Any team holding a YELLOW or RED continues to **carry a YELLOW** into subsequent matches (within the phase), shown as a yellow background behind their team number on the audience screen — including replays.
- Escalation beyond the event: egregious behavior the Head REFEREE / Event Director cannot resolve locally goes to FIRST HQ, which may DISQUALIFY the team from **all subsequent MATCHES** and **remove them from awards consideration**.
- **Clearing:** DECODE clears all YELLOW CARDS at the conclusion of **Practice**, **Qualification**, and **division Playoff** MATCHES. ITD's wording omitted Practice — a genuine DECODE change.
- **League Play** [CONFIRMED-BIOBUZZ, §14]: BIOBUZZ V0 states VERBAL WARNINGS **and** CARDS clear at the end of **each League Meet event**, and it cross-references "Section 10.6.1 YELLOW and RED CARDS" by name — proving that section number survives into BIOBUZZ.

**Card application timing** [BASELINE: DECODE Table 10-5]:

| Earned | Applied to |
|---|---|
| Before Qualification MATCHES | Referees may not be present; Head REFEREE *may* perpetuate a VERBAL WARNING or YELLOW to the first Qual MATCH for particularly egregious behavior |
| During Qualification MATCHES | The team's current (or just-completed) MATCH in which they are **not** a SURROGATE. For a SURROGATE MATCH, applied to their **previous** Qual MATCH |
| Between Quals and Playoffs | The ALLIANCE's **first Playoff MATCH** |
| During Playoff MATCHES | The ALLIANCE's current (or just-completed) MATCH |

A MATCH stops being "current" once results are posted **or** the Head REFEREE signals robot retrieval — whichever is later.

### 1.5 Effect on ranking

[BASELINE: DECODE §13.6.3 + Table 13-1; **the "excluding FOULS" rule is CONFIRMED-BIOBUZZ** via Advancement Table 4-2]

- Rankings sort on **RANKING SCORE (RS)** = average RANKING POINTS across non-SURROGATE Quals.
- First tiebreaker: **"Average ALLIANCE MATCH points, not including MINOR FOULS and MAJOR FOULS."**
- **"A MATCH in which a team is DISQUALIFIED contributes 0 to all sort criteria."**
- YELLOW/RED CARDS issued to a **SURROGATE** still carry forward to that team's subsequent matches, even though the surrogate match itself doesn't count.
- BIOBUZZ Advancement Table 4-2 tiebreakers 6th, 8th, 9th all read "(excluding FOULS)". **[CONFIRMED-BIOBUZZ]**

**Consequence:** fouls you commit can flip a WIN (worth 3 RP in DECODE) into a LOSS. Fouls you draw *cannot* improve your tiebreakers. This is a strictly one-sided instrument — it hurts the fouler more than it helps the fouled.

### 1.6 Effect on elimination play

[BASELINE: DECODE §13.7, T601, T705; ITD equivalent]

| Situation | Result |
|---|---|
| Qual DQ | Affects only the DQ'd team; the partner is unharmed (T601) |
| Playoff DQ | Applies to the **entire ALLIANCE**; all teams get 0 MATCH points |
| Playoff cards | Assigned to the whole ALLIANCE. **2 YELLOWS on an ALLIANCE = RED for the ALLIANCE = DQ for that MATCH** |
| One ALLIANCE DQ'd | That ALLIANCE loses (T705.A) |
| Both DQ'd | The one DQ'd **first chronologically** loses (T705.B) |
| Both DQ'd simultaneously (Head REFEREE judgment) | MATCH is a **tie** (T705.C) |

### 1.7 Where else penalties bite

- **Awards:** [CONFIRMED-BIOBUZZ §6.1.1] "ROBOT penalties during gameplay" is on the list of things JUDGES **cannot consider**. Fouls do not cost you the Inspire Award. But the *CIC / egregious-behavior* channel explicitly can remove a team from awards consideration.
- **Event Rules (E):** [CONFIRMED-BIOBUZZ §5 preamble] "A violation of any Event Rules (E) will result in a **VERBAL WARNING**. Egregious or subsequent violations … may result in escalation to FIRST Headquarters and/or disqualification for the team from MATCHES **and awards**." Note DECODE had an extra intermediate step ("warning from event volunteers" → VERBAL WARNING from Head REFEREE/LRI/ED); **BIOBUZZ deleted that step**, going straight to VERBAL WARNING.
- **ROBOT Construction (R) rules carry no `Violation:` lines** in any of ITD / DECODE / BIOBUZZ V0. R-rule non-compliance becomes a penalty only through the pre-match G-rule (`DECODE G303.B/C` → **RED CARD** if a non-compliant or un-re-inspected robot participates). Watch for the BIOBUZZ analogue.

---

## 2. Historical evolution of the penalty vocabulary

### 2.1 Master timeline

| Season | Manual structure | Terminology | Minor | Major | Points go… | Cards? |
|---|---|---|---|---|---|---|
| 2015-16 RES-Q | Part I + Part II | Penalty / Minor Penalty / Major Penalty | **10** | **40** | awarded to the non-offending ALLIANCE | **No cards at all** — only DISABLED and DISQUALIFICATION |
| 2016-17 VELOCITY VORTEX | Part 1 + Part 2 | same | 10 | 40 | to non-offending ALLIANCE | **YELLOW/RED CARDS introduced.** Trigger: egregious behavior *or* "repeated (3 or more) violations" |
| 2017-18 RELIC RECOVERY | Part 1 + Part 2 | same | 10 | 40 | to non-offending ALLIANCE | yes |
| 2018-19 ROVER RUCKUS | Part 1 + Part 2 | same | 10 | 40 | to non-offending ALLIANCE | yes |
| 2019-20 SKYSTONE | Part 1 + Part 2 | same | **5** | **20** | to non-offending ALLIANCE | yes |
| 2020-21 ULTIMATE GOAL | Part 1 + Part 2, **Traditional & Remote editions** | same | **10** | **30** | **SUBTRACTED from the offending ALLIANCE** | yes |
| 2021-22 FREIGHT FRENZY | Part 1 + Part 2, Trad & Remote | same | 10 | 30 | **SUBTRACTED from the offender** | yes |
| 2022-23 POWERPLAY | Part 1 + Part 2, Trad & Remote | same | 10 | 30 | **flipped back to "added to the opposing ALLIANCE"** for Traditional in **rev 1.3, 2022-10-26**; Remote still deducted | yes |
| 2023-24 CENTERSTAGE | Part 1 + Part 2, Trad & Remote | same | 10 | 30 | added to non-offending ALLIANCE | yes |
| **2024-25 INTO THE DEEP** | **Single Competition Manual**; rules re-lettered E/I/R/G/T/A/L; G-rules become G1xx–G5xx | **MINOR FOUL / MAJOR FOUL** | **5** | **15** | credit to opponent | yes |
| 2025-26 DECODE | Single Competition Manual | MINOR FOUL / MAJOR FOUL | 5 | 15 | credit to opponent | yes |
| **2026-27 BIOBUZZ** | Single Competition Manual | **"FOULS" confirmed** [Advancement Table 4-2]; MINOR/MAJOR split **UNVERIFIED** | **TBD** | **TBD** | **TBD** | `VERBAL WARNING` confirmed in glossary; cards confirmed by §14 cross-ref to §10.6.1 |

Citations for the values: `wayback/2015-16_RESQ_GameManual_PartII.txt` L310; `wayback/2016-17_VELOCITYVORTEX_GameManual_Part2.txt` L421; `wayback/2017-18_RELICRECOVERY_GameManual_Part2.txt` L401; `wayback/2018-19_ROVERRUCKUS_GameManual_Part2.txt` L391; `wayback/2019-20_SKYSTONE_GameManual_Part2.txt` L380; ULTIMATE GOAL Part 2 Traditional §4.4.6 (extracted, L718-719); `2021-22_FREIGHTFRENZY_GameManual_Part2_Traditional.txt` L769-770; `2022-23_POWERPLAY_GameManual_Part2_Traditional.txt` L721-722 + revision history L20; `2023-24_CENTERSTAGE_GameManual_Part2_Traditional.txt` L735-736; ITD & DECODE glossaries.

### 2.2 The four inflection points

1. **2016-17 — cards arrive.** RES-Q (2015-16) had no YELLOW/RED CARD concept whatsoever; the only escalation was DISABLED / DISQUALIFIED. VELOCITY VORTEX introduced the card system essentially in its modern form (additive yellows, alliance-wide in eliminations, chronological tiebreak on double reds). That structure has survived unchanged for ten seasons.
2. **2020-21 to 2021-22 — the direction flip.** With Remote events, penalties became a **deduction from the offender** so a single team could be scored in isolation. This is the *only* era where a foul reduced your own score. If you find a strategy essay or a coach's memory from this era, it is describing a different rule than today's.
3. **2022-23 (mid-season, rev 1.3, 2022-10-26) — the flip back.** POWERPLAY moved Traditional events back to "added to the opposing ALLIANCE" a month into the season. Note the *mid-season* nature: penalty math is exactly the kind of thing FIRST revises after seeing real matches.
4. **2024-25 — the PENALTY → FOUL rewrite.** INTO THE DEEP collapsed Part 1 + Part 2 into one Competition Manual, replaced `<G28>`-style bracketed rule tags with G1xx–G5xx, renamed Minor/Major **Penalty** to MINOR/MAJOR **FOUL**, and **halved the values** (10/30 → 5/15). The point of the halving was to reduce the swing a single referee call could produce.

### 2.3 The DECODE-era refinements worth knowing (ITD → DECODE deltas)

These are the changes FIRST made *most recently*, so they are the most likely to persist into BIOBUZZ. [BASELINE]

| Change | ITD 2024-25 | DECODE 2025-26 |
|---|---|---|
| `VERBAL WARNING` as a formal, capitalized tier | not used (0 occurrences in caps) | defined in Table 10-4 + glossary; 26 occurrences |
| `ALLIANCE is ineligible for RP` as a formal tier | absent | added to Table 10-4 |
| Violation-line grammar | `Verbal warning **plus** YELLOW CARD if…` | `VERBAL WARNING**.** YELLOW CARD if…` (sentence-separated tiers) |
| YELLOW CARD clearing | cleared at end of Qual + division Playoff | **+ Practice MATCHES** added |
| PIN count | **5 seconds**, +1 MINOR per 5 s | **3 seconds**, +1 MINOR per 3 s |
| CONTROL limit | 1 SAMPLE **or** 1 SPECIMEN | 3 ARTIFACTS |
| Match-throwing / collusion | VERBAL → **YELLOW** | VERBAL → **RED CARD** (escalated) |
| Collusion for RPs | absent | **new G206** — YELLOW + both RPs forfeited |
| Encouraging a team to sit out | absent | **new G212** — YELLOW; RED if the robot doesn't play |
| Vertical expansion rule | absent | **new G415** (time-gated expansion window) |
| Explicit auto-card triggers in the catch-all | general | **G211 enumerates**: reaching into the FIELD; a **single PIN over 15 seconds**; strategic or REPEATED descoring |
| Referee foul bookkeeping | — | §13.4 states refs are instructed **not** to self-track foul details |

---

## 3. The recurring G-rule ARCHETYPES

These reappear every season regardless of game. **Expect all of them in BIOBUZZ Section 11 in some form**, with game-specific nouns swapped in and — per §1.4.1 — possibly *merged* into broader judgment-based rules.

Column key: **DECODE** = 2025-26 rule id, **ITD** = 2024-25 rule id, **Threshold** = the tunable number, **Tier** = penalty. All rule text paraphrased.

### 3.1 Safety & personal conduct (G1xx / G2xx)

| # | Archetype | DECODE | ITD | Threshold | Tier |
|---|---|---|---|---|---|
| A1 | Humans stay off the FIELD during a MATCH | G101 | G101 | n/a | DECODE: VERBAL WARNING (entering *during* a match escalates to G211). ITD: verbal + YELLOW if subsequent |
| A2 | Don't climb / hang from / deform / damage ARENA elements | G102 | G102 | n/a | VERBAL WARNING → YELLOW on subsequent |
| A3 | Be a good person (civility) | G201 | G201 | n/a | VERBAL WARNING → YELLOW; contemptible behavior → ARENA ejection |
| A4 | No distracting / taunting the opposing DRIVE TEAM | G202 | G202 | n/a | VERBAL WARNING → YELLOW |
| A5 | No asking others to throw a MATCH | G203 | G203 | n/a | DECODE **VERBAL → RED**; ITD verbal → YELLOW |
| A6 | No accepting coercion to throw a MATCH | G204 | G204 | n/a | DECODE **VERBAL → RED** |
| A7 | No throwing your own MATCH / manipulating rankings | G205 | G205 | n/a | DECODE **VERBAL → RED** |
| A8 | No colluding to break rules for RPs | **G206** | — | n/a | YELLOW **+ both ALLIANCES ineligible for the affected RPs** |
| A9 | No coaching/signalling from restricted ARENA areas | G207 | G206 | n/a | VERBAL → YELLOW |
| A10 | Show up to your MATCHES | G208 | G207 | ≥1 DRIVE TEAM member | **DISQUALIFIED** from that MATCH |
| A11 | Keep your ROBOT together (no intentional detachment) | G209 | G209 | n/a | **RED CARD** |
| A12 | Don't force opponents into rule violations | G210 | G210 | ">1 TILE away" push = intentional | MINOR; MAJOR if REPEATED. **Target is not penalized** |
| A13 | **Catch-all:** egregious or exceptional violations | G211 | G211 | see below | **YELLOW or RED**, Head REFEREE discretion |
| A14 | All teams can play (no pressuring a team to sit out) | **G212** | — | n/a | YELLOW; **RED** if the robot doesn't participate |

**G211 is the rule that swallows everything.** DECODE's enumerated automatic triggers: inappropriate behavior per G201; **reaching into the FIELD and grabbing a ROBOT**; **a single PIN in excess of 15 seconds**; **descoring strategically or REPEATEDLY**. "Teams should be aware that any rule in this manual could escalate to a YELLOW or RED CARD."

### 3.2 Pre-MATCH (G3xx)

| # | Archetype | DECODE | ITD | Threshold | Tier |
|---|---|---|---|---|---|
| B1 | Be prompt / don't delay MATCH start | G301 | G301 | Qual: sched. time or ~3 min after prior match; Playoff: 8 min. **2-minute** grace timer after the warning | VERBAL WARNING → **MAJOR FOUL on the upcoming MATCH** for a repeat in-phase → **DISABLED** after 2 min |
| B2 | Limit what you bring to the FIELD (incl. no jamming, no AprilTag mimicry, height cap) | G302 | G302 | DECODE: 6 ft 6 in (~198 cm) height cap on ALLIANCE-AREA items | MATCH won't start; **YELLOW** if discovered/used during a MATCH |
| B3 | ROBOT is match-ready (safe, inspected, correct SIGN, motionless post-INIT) | G303 | G303 | n/a | MATCH won't start / **DISABLED** / **RED CARD if an uninspected or un-re-inspected ROBOT participates** |
| B4 | ROBOT set up in a legal start position & STARTING CONFIGURATION, ≤ pre-load limit | G304 | (in G303) | game-specific | MATCH won't start; DISABLED if not quickly remedied |
| B5 | An OpMode must be selected & INIT'd | G305 | G304 | n/a | MATCH won't start; DISABLED |

### 3.3 AUTO & period transitions (G4xx)

| # | Archetype | DECODE | ITD | Threshold | Tier |
|---|---|---|---|---|---|
| C1 | Hands off the ROBOT / console during AUTO | G401 | G401 | MOMENTARY reaction to press start | **MAJOR FOUL** (+ DECODE: ALLIANCE loses AUTO PATTERN point eligibility). Strategic violation → G211 |
| C2 | **No crossing into the opponent's half during AUTO** / no disrupting their staged elements | G402 | G404 | field halves by column | **MAJOR FOUL per instance of ROBOT contact** and **MAJOR FOUL per disrupted element** |
| C3 | ROBOTS motionless during the AUTO→TELEOP transition | G403 | G405 | 8-second transition | DECODE **MAJOR FOUL** (strategic → G211); ITD MAJOR + YELLOW if subsequent |
| C4 | ROBOTS motionless at end of TELEOP | G404 | G406 | n/a | **MINOR FOUL**; **MAJOR per element** that scores after the buzzer |

### 3.4 SCORING ELEMENT handling

| # | Archetype | DECODE | ITD | Threshold | Tier |
|---|---|---|---|---|---|
| D1 | Don't use SCORING ELEMENTS as tools / blockers / to hold field mechanisms | G405 | G407 | n/a | **MAJOR FOUL per SCORING ELEMENT** |
| D2 | Keep SCORING ELEMENTS in bounds (no intentional ejection) | G406 | G408 | n/a | **MAJOR FOUL per SCORING ELEMENT** |
| D3 | Don't damage SCORING ELEMENTS | G407 | G409 | n/a | VERBAL WARNING → **MAJOR if REPEATED**; **DISABLED** if more damage likely; re-inspection possible |
| D4 | **CONTROL limit — "no more than N at a time"** | G408 | G410 | **DECODE: 3**; **ITD: 1** | **MINOR FOUL per element over the limit**; **YELLOW if excessive** |
| D5 | Don't CONTROL the opponent's dedicated elements | — | G411 | MOMENTARY allowed | MINOR per element + MINOR per element per 5 s; **MAJOR per element scored while controlled** |
| D6 | **No descoring the opponent's scored elements** | (via **G211** + G418) | G412 | n/a | ITD **MAJOR per element descored**; DECODE folds strategic/REPEATED descoring into G211 (YELLOW/RED) |
| D7 | **No launching** (or: launch only from a designated zone) | G416 | G417 | DECODE: only inside a LAUNCH ZONE / on a LAUNCH LINE; ITD: never | **MINOR per element LAUNCHED**; **MAJOR per element if it scores** |

**"Excessive" (D4) is defined, not vibes.** DECODE: simultaneous CONTROL of **5 or more**, *or* **3+ separate greater-than-MOMENTARY violations of 4+** in a match. ITD: **3 or more** simultaneous, or greater-than-MOMENTARY control of 2+ **more than twice**. Repeated excessive violations do **not** stack extra YELLOWs unless they reach G211.

### 3.5 ROBOT behaviour

| # | Archetype | DECODE | ITD | Threshold | Tier |
|---|---|---|---|---|---|
| E1 | **Don't extend outside the FIELD / no undue hazard** | G409 | G413 | n/a | DECODE: **DISABLED + VERBAL WARNING**; YELLOW if REPEATED or subsequent. ITD: **YELLOW + DISABLED** if unsafe/CONTINUOUS |
| E2 | Stop when a REFEREE instructs | G410 | G414 | greater-than-MOMENTARY delay | **MAJOR FOUL**; **RED CARD if CONTINUOUS** |
| E3 | ROBOT must stay identifiable (signs, alliance colour) | G411 | G415 | n/a | DECODE VERBAL → **MINOR**; ITD verbal → YELLOW |
| E4 | Don't damage the FIELD | G412 | (R-rules + G413) | n/a | VERBAL WARNING; **DISABLED** if more damage likely; **YELLOW for any subsequent damage during the event** |
| E5 | **No grabbing / grasping / attaching to / entangling with / suspending from ARENA elements** | G413 | G416 | greater-than-MOMENTARY | DECODE: **MAJOR FOUL** + YELLOW if REPEATED or >MOMENTARY; **DISABLED** if damage likely. ITD: verbal → YELLOW |
| E6 | Horizontal expansion limit | G414 | G418 | per R105 / R104 | **MINOR FOUL**; **MAJOR if the over-expansion gives strategic benefit** (incl. impeding or enabling a scoring action) |
| E7 | Vertical expansion limit, time- and place-gated | **G415** | — | DECODE: >18 in only in the **final 20 s** and **not in a LAUNCH ZONE**; cap 38 in | **MINOR FOUL**; **MAJOR if strategic** |
| E8 | No grabbing the floor / suction downforce | *(construction)* R208 | UNVERIFIED | n/a | inspection-side; see **BIOBUZZ R204** |

### 3.6 Opponent interaction — the high-stakes cluster

| # | Archetype | DECODE | ITD | Threshold | Tier |
|---|---|---|---|---|---|
| F1 | **This is not combat robotics** — no deliberate damage / functional impairment | G420 | G421 | n/a | **MAJOR FOUL + YELLOW CARD**; **MAJOR + RED if the opponent ROBOT is unable to drive** |
| F2 | **No tipping or entangling** | G421 | G422 | n/a | **MAJOR + YELLOW**; **MAJOR + RED if CONTINUOUS or the opponent can't drive** |
| F3 | **PIN count** | G422 | G423 | **DECODE 3 s / ITD 5 s.** Escape = 2 ft separation, or 2 ft travel from the pin origin, or the pinner gets pinned | **MINOR FOUL + an additional MINOR every 3 s (DECODE) / 5 s (ITD)**. A single PIN **>15 s** is a listed G211 auto-card trigger |
| F4 | **No shutting down major parts of gameplay** (blocking, quarantining, isolating) | G423 | G424 | greater-than-MOMENTARY | **MINOR FOUL + an additional MINOR every 3 s (DECODE) / 5 s (ITD)** |
| F5 | **Protected-zone contact — loading / element-intake access** | **G426** (LOADING ZONE), **G425** (SECRET TUNNEL) | **G426** (OBSERVATION ZONE) | "either ROBOT is in the zone, **regardless of who initiates contact**" | DECODE: **MINOR FOUL** for both. ITD: MINOR + MINOR per 5 s + an extra MINOR per element contacted in the zone |
| F6 | **Protected-zone contact — access to a scoring structure** | **G424** (GATE ZONE) | **G425** (NET ZONE) | as above | DECODE **MINOR FOUL**; ITD **MAJOR FOUL per occurrence** — same archetype, **3× the price** one season apart |
| F7 | **ENDGAME asset protection** — don't touch an opponent doing their endgame scoring task | **G427** (BASE ZONE, **last 20 s**) | **G427** (ASCENT ZONE, **last 30 s**) | time-gated | **MAJOR FOUL** *and* **the opponent is awarded the scoring achievement outright** (DECODE: fully-returned-to-BASE points, incl. any robot they support; ITD: a **LEVEL 3 ASCENT**) |
| F8 | Restrictions on operating shared/opponent field mechanisms | G417 (GATE), G418 (RAMP artifacts), G419 (own GOAL only) | G420 (start ASCENT outside the zone) | n/a | **MAJOR FOUL per element**, plus **RP awarded to the opponent** or **RP forfeited by you** |

**Mutual-exclusion note** [BASELINE: DECODE §11.4.5 preamble]: G420 and G421 are mutually exclusive — a single ROBOT-to-ROBOT interaction that violates more than one yields **only the most punitive** penalty. ITD had an equivalent non-stacking note for G419/G431/G432. **Ask on kickoff day which BIOBUZZ rules are declared non-stacking** — this materially changes defensive risk math.

### 3.7 Human / DRIVE TEAM

| # | Archetype | DECODE | ITD | Threshold | Tier |
|---|---|---|---|---|---|
| H1 | No wandering — stay in your ALLIANCE AREA | G428 | G428 | breaking the plane is not itself a foul | VERBAL WARNING → **MINOR** on subsequent |
| H2 | Only DRIVERS drive; COACHES may only do listed console tasks | G429 | G429 | greater-than-MOMENTARY | **MAJOR FOUL**; **YELLOW if >MOMENTARY** |
| H3 | DRIVE COACHES: hands off SCORING ELEMENTS | G430 | (via G431) | safety exception | **MINOR FOUL** |
| H4 | **Watch your reach** — no contacting a ROBOT / disrupting scoring from outside | G431 | G430 | inadvertent + MOMENTARY + inconsequential is exempt | **MAJOR + YELLOW** for contacting a ROBOT; **RED CARD + opponent awarded the RP** for disrupting scoring |
| H5 | Humans may only handle elements inside a designated zone, during TELEOP, without tools | G432 | G431 / G434 | zone- and phase-gated | **MINOR per element**; **MAJOR per element that scores** |
| H6 | Humans may only enter *game* elements onto the FIELD | G433 | — | n/a | **MINOR FOUL per non-game item entered** (Q&A: safety glasses, badges count) |
| H7 | **Off-field hoarding / storage cap** | **G434** | — | DECODE: **6 ARTIFACTS** during TELEOP | **MINOR per element over the limit + an additional MINOR per element over every 3 s**. Deliberately losing access → G211 |
| H8 | Humans may not launch/"yeet" elements | (via G432) | G433 | n/a | ITD **MAJOR FOUL per element** |
| H9 | Robots must watch out for humans | (via G409/G431) | G419 / G432 | n/a | ITD MINOR per occurrence + **YELLOW if the ROBOT contacts the HUMAN PLAYER** |

### 3.8 Post-MATCH

| # | Archetype | DECODE | ITD | Tier |
|---|---|---|---|---|
| J1 | Leave promptly; don't delay FIELD reset | folded into G101 | **G501** | verbal → YELLOW on subsequent |
| J2 | Stop the ROBOT before entering the FIELD | folded into G101/G404 | **G502** | verbal → YELLOW on subsequent |

DECODE **deleted** the standalone §11.5 Post-MATCH block that ITD had. If BIOBUZZ follows its stated simplification philosophy, expect further consolidation of this kind.

### 3.9 Inspection & construction enforcement

| # | Archetype | DECODE | ITD | BIOBUZZ V0 | Tier |
|---|---|---|---|---|---|
| K1 | Enter only 1 ROBOT per event | **I302** | G208 | **E117** (moved to Event Rules) | DECODE VERBAL → **RED CARD**; ITD verbal → RED. **BIOBUZZ: no stated violation — falls back to the E-rule ladder (VERBAL WARNING → HQ escalation)** |
| K2 | Get inspected before playing | **I303** | I302 | **§3.3 prose only** | DECODE: **DISQUALIFIED** if caught pre-match, **RED CARD** if caught after the match starts. **BIOBUZZ V0 states no penalty** |
| K3 | Re-inspect after changes | **I305** | I304 | **I303** | DECODE: **RED CARD**. **BIOBUZZ I303 states no penalty** |
| K4 | Don't exploit re-inspection | I306 | I305 | **I304** | none stated in any |
| K5 | Bring the whole ROBOT to inspection | I304 | I303 | **I301** | none stated |
| K6 | Electronics count across all configurations | I304.C | I303.C | **I302** | none stated |
| K7 | Team-built ROBOT | I301 | I301 | **moved to R101** | none stated |

**This is one of the biggest V0 signals.** Every `Violation:` line in the Inspection section is gone in BIOBUZZ V0. Either (a) inspection enforcement will be restated in Section 11 at kickoff, or (b) FIRST is deliberately moving inspection integrity from a card-based regime to the **CIC / "we don't cheat" / LRI-mitigation** regime described in §1.5.3. **[SPECULATION — verify on kickoff day; item #1 on the checklist.]**

---

## 4. Strategically important asymmetries

### 4.1 A foul is a gift, not a tax — and gifts don't count for everything

| Mechanism | Effect |
|---|---|
| Fouls **credit the opponent's MATCH point total** [BASELINE Table 10-4] | Your own score is untouched. The *margin* moves by the full value |
| Foul points are **excluded** from "Average MATCH Points" tiebreakers [CONFIRMED-BIOBUZZ Table 4-2] | Drawing fouls does **not** help your ranking tiebreakers |
| Fouls **do** change WIN/LOSS, which is worth **3 RP** in DECODE (TIE = 1 RP) [BASELINE Table 10-2] | One MAJOR FOUL in a 10-point game costs the full 3 RP |
| Foul points do **not** count toward threshold-based bonus RPs | Those are keyed to specific scoring categories, not total points |

**The practical rule:** in a close match, a MAJOR FOUL is worth far more than 15 points, because it can convert a 3-RP win into a 0-RP loss. In a blowout it is worth almost nothing. **Defensive risk tolerance should be a function of the projected margin, not a fixed policy.**

### 4.2 Fouls that scale, vs. fouls that are one-and-done

| Scaling mode | Formula | DECODE examples | Worst case |
|---|---|---|---|
| **Per-match, flat** | 1 penalty | G403, G404 (base), G410 | bounded |
| **Per-occurrence** | 1 per event of the act | G402.A, G431 | unbounded in principle |
| **Per SCORING ELEMENT** | 1 per element | G405, G406, G416, G418, G419, G432 | **very large** — DECODE Q&A #89: opening the opponent's GATE with a full RAMP = **1 G417 MAJOR + 9 G418 MAJORS = 10 MAJOR FOULS = 150 points**, plus the PATTERN RP handed to the opponent |
| **Per element over a limit** | 1 per excess element | G408, G434 | bounded by hardware |
| **Per time interval** | **1 + ⌊t ÷ interval⌋** | **G422 (pin), G423 (blocking), G434 (hoarding)** — all on a **3-second** clock in DECODE | 15 s = 6 MINORS = 30 pts; **and >15 s pinning is a G211 auto-card trigger** |

The per-element class is where matches are actually lost. A single bad decision touching N elements costs 15N.

### 4.3 What escalates automatically

| Escalation phrase | Clock | Effect |
|---|---|---|
| `… if REPEATED` | **within the MATCH** | Adds a second, higher-tier penalty on top of the first |
| `… if subsequent violations occur during the event` | **whole event, across phases** | Later violations of the same rule earn the card |
| `… if greater-than-MOMENTARY` | ~3 s | Tier bump |
| `… if CONTINUOUS` | ~10 s | Usually the RED CARD line |
| `… if the opponent ROBOT is unable to drive` | outcome-based | **YELLOW → RED** (G420/G421). Defined as: the DRIVER can no longer drive to a desired location in reasonable time (e.g., only moves in circles, or extremely slowly) |
| `… if excessive` | defined numerically per rule | YELLOW |
| YELLOW + YELLOW | anywhere in the phase, **including the same match** | **RED CARD → DISQUALIFICATION** |

**The unavoidable consequence:** a robot with a design flaw that trips a rule twice per match will accumulate cards over an event even if each individual call is small. Design out the *repeatable* fouls first; the one-off fouls are cheap by comparison.

### 4.4 The rules whose thresholds create deliberate-risk decisions

These are the rules where "take the penalty" is a live strategic option, and where the manual's numbers determine whether it's rational.

| Decision | Rule (DECODE) | The math |
|---|---|---|
| **Pin an opponent through the endgame** | G422 | 3-s clock. Holding a pin for 12 s = 5 MINORS = 25 pts. If it denies a 30-pt endgame score, it's profitable — **until 15 s, when G211 makes it a card.** The 15-s line is the real ceiling, not the point cost |
| **Camp in a protected zone** | G424/G425/G426 | MINOR (5 pts) **per contact**, regardless of who initiated. Denial of a loading zone for a whole match can cost the opponent far more than 5. **Q&A confirms it's the intruding robot that pays** even if the defender drives into them. But G423 (blocking, 3-s scaling) is the enforcement backstop |
| **Block the opponent's field mechanism** | G423 vs. G417/G424 | Whether it's a 5-pt MINOR or a 15-pt MAJOR + RP forfeiture depends entirely on which rule the ref reaches for. **This is precisely the choice FIRST says BIOBUZZ will resolve toward the judgment-based rule** (§1.4.1) |
| **Descore / disrupt an opponent asset** | G418/G419 + G211 | Point cost is per element, but the **RP transfer** is the real price, and G211 makes strategic or REPEATED descoring a **card** — an unbounded penalty |
| **Contact an opponent during their endgame task** | G427 | **MAJOR FOUL AND they are awarded the score anyway.** Never rational. This archetype is deliberately designed to have no profitable violation |
| **Over-expand for one crucial scoring cycle** | G414/G415 | MINOR (5) if incidental, **MAJOR (15) if it "impedes or enables a scoring action"** — i.e. exactly when you'd want to do it. The exception clause is written to kill the strategy |
| **Force an opponent into a protected-zone foul** | G210 | Q&A #80: pushing from **more than one TILE away** into your own protected zone = G210 on **you**, and the target is **not** penalized. Within ~half a tile, the target still eats the foul. **The "one TILE" line is the whole game here** |
| **"Farm" fouls off a DISABLED robot** | G210 + Q&A #104 | A DISABLED robot **can still earn penalties**, but repeatedly contact-backup-contact to harvest them is a **G210 violation** |
| **Draw a foul by entering your own protected zone** | G427 + Q&A #107 | Leaving your protected position for no purpose other than to force the opponent into a foul = **G210 on you, no foul on them** |
| **Hoard elements off-field** | G434 | 6-element cap, then MINOR **per element over, every 3 s** — compounding on two axes simultaneously. Deliberately losing access → G211 |

**The doctrine to internalize (DECODE Q&A #80):** *"A G210 violation requires the forcing team to receive a penalty. There is **no 'no call'** scenario."* One alliance always pays. The referee's only decision is **which one**.

### 4.5 Penalties that are worth more than their points

Rank-ordered by true cost, ignoring face value:

1. **RED CARD** → DISQUALIFICATION → **0 MATCH points AND 0 RANKING POINTS**, and the match "contributes 0 to all sort criteria." In Playoffs it takes the whole alliance down.
2. **RP awarded to the opponent / forfeited by you** (DECODE G417, G418, G419, G431.C, G206). Overrides on-field performance entirely.
3. **Opponent awarded a scoring achievement outright** (DECODE G427; ITD G427 LEVEL 3 ASCENT). Unlike foul points, these are *real* scoring-category points and therefore **do** feed threshold RPs and the "excluding FOULS" tiebreakers.
4. **YELLOW CARD** — worth 0 points but converts your next infraction into a RED.
5. **DISABLED** — costs you the remainder of the match's scoring, which in a late-match endgame can exceed any foul total.
6. **G211 escalation to FIRST HQ** — DQ from all subsequent matches **and removal from awards consideration**.
7. **CIC / Sporting Ethics Code violation** [CONFIRMED-BIOBUZZ §1.5.3] — sanction, DQ from current **and future** events, up to permanent removal from the program.

### 4.6 Procedural asymmetries you can actually exploit

- **Referees do not record which rule produced each foul** [BASELINE: DECODE §13.4]. The event software tracks *counts* only. Disputing "that third minor foul at 1:12" will fail. Asking "how are you calling loading-zone contact today?" will succeed.
- **No video review, ever** [BASELINE: DECODE §10.7] — "No event staff, including the Head REFEREE, will review video, photos, artistic renderings, etc. of any MATCH, from any source, under any circumstances."
- **Question box has a clock** [BASELINE: T402]: Quals — any time before ALLIANCE selection begins. Playoffs — **before the next Playoff round starts**; for the last match, immediately after. Practically: within 3 matches.
- **One STUDENT + at most 1 silent observer** [BASELINE: T401]. Violation: the Head REFEREE simply won't address the extra people.
- **Damage-based calls can be reversed post-match** [BASELINE: DECODE G420] — the Head REFEREE may visually inspect a robot after the match and **remove** the violation if damage can't be verified. If you're accused of G420, ask for the inspection.
- **Cards issued to SURROGATES still carry forward** even though the surrogate match doesn't count for ranking.

---

## 5. What BIOBUZZ V0 already tells us

### 5.1 Confirmed carry-overs

| Item | Where | Note |
|---|---|---|
| The term **FOULS** | Advancement Table 4-2, tiebreaks 6/8/9 | `(excluding FOULS)` — identical phrasing to DECODE |
| **VERBAL WARNING** as a defined term | Section 16 Glossary | "a warning issued by event staff or the Head REFEREE" — verbatim DECODE definition |
| **YELLOW and RED CARDS** exist, and live in **§10.6.1** | Section 14 League Play | Explicit cross-reference to "Section 10.6.1 YELLOW and RED CARDS" |
| Cards + VERBAL WARNINGS clear **at the end of each League Meet** | Section 14 | Consistent with DECODE |
| Event Rules universal violation = **VERBAL WARNING** | Section 5 preamble | **Simplified** from DECODE's two-step warning ladder |
| Judged awards **cannot** consider "ROBOT penalties during gameplay" | Section 6.1.1 | Same as prior seasons |
| Head REFEREE / LRI / FTA authority over safety and lighting | R202.F, R202.J, §3.3 | Same discretionary hooks |
| **RED CARD-adjacent construction rules still exist**: no intentional detachment (R105), no floor-grabbing (R204), no AprilTag mimicry (R202.C), no flip-designed devices (R202.H) | Section 12 | These are the construction halves of G-rule archetypes A11, E8, B2 |

### 5.2 Confirmed *new* for BIOBUZZ

| Item | Where | Why it matters for penalties |
|---|---|---|
| **Competition Integrity Contract (CIC)** — Sporting Ethics Code + Behavior Guidelines | §1.5 (new; 0 hits in DECODE/ITD) | A parallel enforcement track. "We Play the Game as Intended… Our team will not try to gain an advantage using any 'loopholes' in the rules." Explicitly targets rules-lawyering |
| **§1.5.3 Infractions, Mitigations & Escalation** | §1.5.3 | Names LRI / Head REFEREE / FTA as *mitigation* authorities, Event Director + FIRST HQ as *escalation*. Ceiling: team **sanctioned, DQ'd from current and/or future events**, individuals **suspended or permanently removed** |
| **"Escalation Guidelines (coming soon)"** | §1.5.3 | A **separate document** will define escalations for competition-regulation violations. **Not yet released as of V0** |
| **Declared rewrite philosophy** | §1.4.1 | "The BIOBUZZ manual emphasizes the 'spirit of the rule' and empowers event volunteers to make good-faith judgement calls… rather than be required to watch for and record every action or incident that occurs (e.g., **strategically blocking an opponent from access to their gate vs. going into an opponent's gate zone**)" |
| **Interpretive canon in the Glossary** | §16 preamble | "Competition rules mean what they plainly say. If a word is not given a game definition, then you should use its common conversational meaning." A textualist instruction aimed at loophole arguments |
| **Inspection section stripped of all `Violation:` lines** | §3.3.1–3.3.2 | See §3.9 above |
| **Inspection non-comprehensiveness made explicit** | §3.3.1 orange box | "Teams that strategically circumvent ROBOT construction rules to gain a competitive advantage are not adhering to the **Competition Integrity Contract (CIC)** and may be subject to mitigation." First time an R-rule bypass is tied to a non-referee sanction |
| **1-ROBOT rule moved from I302 to E117** | §5 | Enforcement drops from **RED CARD** to the Event Rules ladder |
| **R105 exists but is deliberately blank**: "Sizing Constraints and more details will be released at Kickoff" | §12.1 | The G414/G415 expansion-penalty archetypes are pending on this number |
| **A `GXXX` placeholder cross-reference survives in R201** | §12.2 | Proves a BIOBUZZ G-rule about damaging SCORING ELEMENTS is already planned (archetype D3) |

### 5.3 Still completely unknown (Section 11 placeholders)

Sections **8 (Game Overview), 9 (ARENA), 10 (Game Details), 11 (Game Rules G), 13 (Tournament T)** all read "This section will be updated with the Kickoff Competition Manual release on September 12, 2026."

Therefore **UNVERIFIED for BIOBUZZ**: MINOR/MAJOR FOUL point values; whether the two-tier foul split survives at all; PIN count length; CONTROL limit; every protected-zone rule; RP structure; T-rule DQ handling; §10.6 table contents.

**[SPECULATION]** Given §1.4.1's explicit example, the most likely structural change is **consolidation of the protected-zone family (DECODE G424/G425/G426) into a single judgment-based "don't block the opponent's access" rule** in the G423 mould, with a scaling time-interval penalty rather than a per-contact MINOR. Second most likely: **fewer numeric thresholds overall**, replaced by MOMENTARY / CONTINUOUS / REPEATED language.

---

## 6. Kickoff-day penalty checklist

Work this list in order against the new Section 10.6 and Section 11. Timeline anchors [CONFIRMED-BIOBUZZ, `2026-27_BIOBUZZ_ImportantSeasonDates.pdf`]: **Kickoff Sept 12** → **Team Q&A opens Sept 28** → **earliest League Meets / Qualifiers Oct 15**. Expect Team Update 00 on or about kickoff day and roughly weekly updates thereafter (DECODE ran TU00 on kickoff day — Sat Sep 6, 2025 — and TU01 five days later on Thu Sep 11, which already revised three G-rules and R105).

### A. The ladder itself

1. **Does §10.6 Table 10-4 still list MINOR FOUL and MAJOR FOUL — and at what point values?** Do not assume 5/15. The values have changed in 4 of the last 11 seasons.
2. Are **VERBAL WARNING** and **ALLIANCE is ineligible for RP** still formal tiers, or did the simplification pass remove them?
3. Has a **new tier** appeared (e.g. anything tied to the CIC, or a "mitigation" instrument)?
4. Are the **MOMENTARY / CONTINUOUS / REPEATED** definitions still 3 s / 10 s / once-per-match?
5. Is **§10.6.4 Violation Details** (the compounding-grammar table) still present? If it was cut, the compounding semantics become ambiguous — **this is a top Q&A question**.
6. **When do YELLOW CARDS clear?** Practice / Qual / division Playoff, as in DECODE?
7. Do **VERBAL WARNINGS** still persist across tournament phases?
8. Has the **Playoff = alliance-wide cards** rule survived?
9. Does **DISQUALIFIED** still zero **both** MATCH points and RANKING POINTS?

### B. Ranking and elimination coupling

10. Confirm **RANKING SCORE** definition and whether the "**excluding FOULS**" exclusion still applies to the *first* tiebreaker (V0's Advancement table already says yes at the advancement level — check the *event ranking* level too).
11. What is a **WIN worth in RP**? That number sets the true cost of every foul.
12. Are there **threshold RPs**, and can a rule violation **hand them to the opponent** (DECODE G417/G418/G419) or **strip them from you** (G206/G418.A)? Enumerate every such rule — these are the most expensive fouls in the manual.
13. Does any rule **award the opponent an actual scoring achievement** (the G427 archetype)? Those points feed RPs and tiebreakers; foul points do not.
14. Confirm **T601 / T705 analogues**: Qual DQ isolated to the team; Playoff DQ alliance-wide; both-DQ tiebreak by chronology; simultaneous = tie.

### C. The archetypes — go through §3 line by line

15. **PIN count: how many seconds?** (5 → 3 over the last two seasons.) What ends the count, and at what separation distance?
16. **CONTROL limit: how many elements?** What counts as CONTROL, what's exempt (bulldozing/deflecting), and what is the numeric definition of **"excessive"** that triggers the YELLOW?
17. **Protected zones: do they still exist as discrete rules, or were they merged into a blocking rule?** (This is FIRST's own example of what they're changing.) If discrete: MINOR or MAJOR? Per-contact or per-interval? Does "regardless of who initiates contact" survive?
18. **Endgame protection:** what's the protected zone, what's the time window (20 s? 30 s?), and is the opponent still **awarded the score outright**?
19. **Expansion limits:** what does R105 actually say, and what are the G-rule penalties for exceeding it? Is there still a **"MAJOR if used for strategic benefit"** clause?
20. **Launching:** is launching restricted to a zone, banned outright, or unrestricted? Per-element penalty? Extra penalty if the launch scores?
21. **AUTO cross-the-line rule:** is contact/disruption on the opponent's half a MAJOR **per instance** and **per element**?
22. **Descoring:** is there a dedicated rule (ITD G412) or is it folded into the egregious catch-all (DECODE G211)?
23. **Blocking/shutdown rule:** what's the interval on the compounding count?
24. **Catch-all rule (G211 analogue):** what behaviours are enumerated as **automatic** card triggers? DECODE listed reaching into the field, a single pin >15 s, and strategic/repeated descoring.
25. **Non-stacking declarations:** which rules are declared mutually exclusive or non-stacking? This changes defensive risk math more than any single point value.
26. **Forcing-a-violation rule (G210 analogue):** does it survive, and is the "**more than one TILE away**" heuristic still in the orange box? Is the "no no-call" doctrine restated?
27. **Human/DRIVE TEAM rules:** storage cap, zone limits, tool prohibition, reach-into-field penalties.
28. **Post-MATCH rules:** did DECODE's consolidation hold, or did G501/G502 come back?

### D. The BIOBUZZ-specific unknowns

29. **Do the Inspection (I) rules regain `Violation:` lines?** If not, what enforces re-inspection and playing-while-uninspected? Is it Section 11, or is it now purely CIC/LRI mitigation? *(Top question of the day.)*
30. **Has the "Escalation Guidelines" document been released?** If yes, read it — it may contain enforcement mechanics that used to live in §10.6.
31. **Does the CIC create any in-match consequence**, or is it purely a post-event/HQ instrument? Can a referee cite the CIC during a match?
32. **How many G-rules are there?** Both DECODE and ITD had exactly **53** (DECODE: G101–G102, G201–G212, G301–G305, G401–G434; ITD: G101–G102, G201–G211, G301–G304, G401–G434, G501–G502). A large drop confirms the consolidation thesis and means **more referee discretion, less predictability** — plan defensive strategy conservatively at the first events of the season.
33. **Count the numeric thresholds.** If bright-line numbers largely disappear, the correct competitive response is to build robots that are *obviously* compliant rather than *technically* compliant.
34. **Does the manual restate the "spirit of the rule" instruction inside Section 11 itself**, or only in §1.4.1? If it's inside Section 11, referees will cite it in the question box.
35. **Check the Glossary** for the new definitions of MINOR FOUL, MAJOR FOUL, PIN, CONTROL, LAUNCH, MOMENTARY — the Glossary is where the real thresholds hide.

### E. Ongoing (post-kickoff)

36. Diff **Team Update 00** against the Kickoff manual immediately — TU00 is historically a changelog of evergreen changes from the prior season *plus* changes from the V0 preview.
37. Track every Team Update for Section 10.6 / Section 11 edits. Penalty values and thresholds have been revised mid-season before (POWERPLAY rev 1.3 flipped the entire direction of penalty scoring on 2022-10-26).
38. From **Sept 28**, mine the Q&A for penalty rulings. In DECODE, the Q&A produced the most valuable enforcement doctrine of the season (forced-foul thresholds, penalty-farming, disabled-robot penalties) — none of which was in the manual text.
39. Before your first event (**earliest Oct 15**), build a one-page driver card of: every per-element rule, every compounding-interval rule, and every rule that transfers an RP or a scoring achievement.

---

## 7. Provenance & security note

**Security scan:** All source PDFs, HTML archives, and extracted text in this corpus were read as data. **No document contained text addressed to an AI system, instructions to take actions, or attempts to alter these instructions.** The one piece of "instruction-like" text encountered — the BIOBUZZ §1.5 Competition Integrity Contract — is addressed to *teams* and is reported above as manual content, not followed as a directive.

**Extraction caveat:** DECODE §10.6 Table 10-4 and ITD §10.6 Table 10-4 both extract with the penalty names and their descriptions offset by one row in `pdftotext` output (a two-column table artifact). The mapping used in §1.1 above was cross-validated against the **DECODE Glossary entries** for MINOR FOUL ("a credit of 5 points towards the opponent's MATCH point total") and MAJOR FOUL ("a credit of 15 points…") in `manuals/archive/2025-26_DECODE_layout.txt` L6892 and L6910. Treat any table read directly out of the raw `.txt` with the same suspicion.

**Not verified in this pass:** ULTIMATE GOAL Part 1 penalty wording (Part 2 was used instead); whether ITD had an equivalent of DECODE R208 (no-floor-grabbing); the exact POWERPLAY revision that first introduced the Traditional/Remote penalty-direction split.
