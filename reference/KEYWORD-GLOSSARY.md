# BIOBUZZ Keyword & Defined-Term Reference

**Purpose:** kickoff-day (2026-09-12) vocabulary weapon. Everything FIRST defines is set in ALL CAPS.
This file (a) locks down what BIOBUZZ V0 already defines, (b) shows which glossary slots DECODE/ITD
vacated — that is exactly where BIOBUZZ's new game nouns will land — and (c) gives a tested one-liner
that enumerates every new BIOBUZZ game noun from the Kickoff manual in about five seconds.

**Companion file:** `C:/Users/ericj/Documents/BIOBUZZ Analysis/reference/known_caps_stoplist.txt` (341 tokens, 3 tiers).

**Evidence labels used throughout**

| Label | Meaning |
|---|---|
| **[C]** CONFIRMED-FOR-BIOBUZZ | Present in the BIOBUZZ V0 manual (2026-07-31), which is final for the sections it publishes |
| **[H]** HISTORICAL-PATTERN | Observed in prior-season manuals in this corpus; not stated for BIOBUZZ |
| **[S]** SPECULATION | Inference. Flagged as such. Do not act on it as fact |
| **UNVERIFIED** | Could not be checked against the corpus |

**Source shorthand**
`V0` = `manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf` (93 pp) ·
`DEC` = `manuals/archive/2025-26_DECODE_Competition_Manual_TU32.pdf` (188 pp) ·
`ITD` = `manuals/archive/2024-25_INTO_THE_DEEP_Competition_Manual_V14.pdf` (146 pp).
Plain-text mirrors of all three live in `manuals/archive/*.txt`.

---

## 0. Kickoff-day 60-second workflow

```bash
cd "C:/Users/ericj/Documents/BIOBUZZ Analysis"
K="manuals/2026-27_BIOBUZZ/BIOBUZZ_Kickoff_Manual.pdf"     # <- the file you download 2026-09-12
S="reference/known_caps_stoplist.txt"

# 1. flatten
pdftotext -layout "$K" - > /tmp/k.txt

# 2. NEW GAME NOUNS, frequency-ranked  <-- the money shot
grep -oE "\b[A-Z]{3,}('S)?\b" /tmp/k.txt | grep -vxF -f "$S" | sort | uniq -c | sort -rn | head -40

# 3. NEW MULTI-WORD NOUNS (rebuilds "<NEWWORD> ZONE" style phrases)
grep -oE "\b[A-Z]{3,}('S)?\b" /tmp/k.txt | grep -vxF -f "$S" | sort -u > /tmp/novel.txt
grep -oE "\b[A-Z]{3,}( [A-Z]{3,}){1,3}\b" /tmp/k.txt \
  | sort | uniq -c | sort -rn | grep -wFf /tmp/novel.txt | head -30

# 4. FIRST SIGHTING of each new noun = almost always its heading or its definition
grep -oE "\b[A-Z]{3,}\b" /tmp/k.txt | grep -vxF -f "$S" | sort | uniq -c | sort -rn | head -25 \
  | awk '{print $2}' \
  | while read w; do printf "%-22s %s\n" "$w" "$(grep -m1 -F "$w" /tmp/k.txt | sed 's/^ *//' | cut -c1-100)"; done

# 5. read the real glossary
sed -n '/^16 Glossary/,$p' /tmp/k.txt

# 6. S9/S10 sub-headings = the game-noun taxonomy and the scoring-category count
grep -oE "^ *(9|10)\.[0-9]+(\.[0-9]+)? +[A-Za-z][^.]{0,45}" /tmp/k.txt | sed 's/^ *//' | sort -u
```

Steps 2–4 were **dry-run against DECODE and ITD** using this exact stoplist. Results in §4.4 — the
top ~20 hits are the complete game-noun vocabulary of each season, with essentially zero noise.

---

## 1. BIOBUZZ V0 Section 16 Glossary — complete (22 terms)

Source: `V0` pp. 92–93 (`sections/14-16_League_Glossary_p90-93.txt`).

> **Extraction warning:** the flat-text extraction of pp. 92–93 **de-interleaves the two columns and
> mis-pairs term↔definition** (e.g. it appears to define ARENA as "a cooperative of 2 FIRST Tech Challenge
> teams"). The table below is rebuilt from PDF block geometry via pymupdf and is correct. Do not trust
> `sections/14-16_League_Glossary_p90-93.txt` for term↔definition pairing.

V0 states the convention on p.92: *"Defined terms are in ALL CAPITAL LETTERS throughout the manual"*,
plus the fallback that undefined words carry ordinary conversational meaning. Restated on p.17 (§1 Introduction).

"Where used" = occurrence counts per V0 section (term + plural/possessive forms), computed over
`manuals/2026-27_BIOBUZZ/sections/*.txt`. Section 16 self-references omitted.

| # | TERM | Definition (paraphrase) | Where used in V0 | Status |
|---|---|---|---|---|
| 1 | **ALLIANCE** | A cooperative of 2 FTC teams. | S4 Advance x17, R x9, A x4, S1 x1 | [C] evergreen (identical in DEC/ITD) |
| 2 | **ARENA** | All game infrastructure needed to run the game: FIELD, SCORING ELEMENTS, queue area, team media area, plus FIELD/ROBOT control and scorekeeping gear. | R x6, E x3, S1 x1 | [C] evergreen; wording identical to DEC |
| 3 | **CHASSIS** | The ROBOT's MAJOR MECHANISM that moves it around a FIELD. | R x2 | [C] evergreen |
| 4 | **COMPONENT** | A part in its most basic configuration; cannot be taken apart without damaging it or changing its function. | R x21, I x6, A x4 | [C] evergreen; the atom of the R-rule hierarchy |
| 5 | **COTS** | Standard, non-custom-order part commonly purchasable from a VENDOR by all teams. | R x44 | [C] evergreen; heaviest-used term in Section 12 |
| 6 | **HOME REGION** | The region a team is assigned to; the only region they may advance from. | S4 Advance x4, I x2, A x1 | **[C] NEW IN BIOBUZZ** — 0 hits in DEC or ITD |
| 7 | **INSPECTOR** | Volunteer role; assesses legality of a part or a whole ROBOT. | I x10, R x2, S2 x1 | [C] evergreen |
| 8 | **JUDGE** | Volunteer role; meets teams, evaluates against award criteria, collectively decides awards. | A x70, E x2 | [C] evergreen. Wording changed vs DEC: "in the pits and sometimes in dedicated judging spaces" replaces DEC's "during the interview process, and in the pits" |
| 9 | **LRI** | Lead ROBOT INSPECTOR. | I x4, R x2, S2 x1 | [C] evergreen |
| 10 | **MAJOR MECHANISM** | Group of COMPONENTs/MECHANISMs addressing at least 1 game challenge: ROBOT movement, SCORING ELEMENT manipulation, FIELD element manipulation, or a scorable task without another ROBOT's help. | R x7 | [C] evergreen. **Names SCORING ELEMENT — a term V0 never defines** |
| 11 | **MECHANISM** | Assembly of COMPONENTs giving specific ROBOT functionality; reversibly disassemblable. | R x28, I x4, A x2 | [C] evergreen |
| 12 | **OPERATOR CONSOLE** | The COMPONENTs/MECHANISMs the DRIVE TEAM uses to send commands to the ROBOT. | R x18, I x2, S1 x1 | [C] evergreen. **Names DRIVE TEAM — also undefined in V0** |
| 13 | **PORTFOLIO** | Judging document; requirements set out in A201. | A x40, I x2 | [C] present in DEC, **absent from ITD** (added 2025-26) |
| 14 | **REFEREE** | FIRST-certified official enforcing the current season's rules. | R x3, I x3, S2 x2 | [C] evergreen |
| 15 | **ROBOT** | Electromechanical assembly built by an FTC team to play the season's game; has power, comms, control, movement about the FIELD. | R x217, I x42, A x28, E x25, S2 x10 | [C] evergreen; most-used defined term in the manual |
| 16 | **ROBOT CONTROLLER** | Android device running the RC app per R701 — a **REV Control Hub (REV-31-1595)**, or an Android phone connected to a **REV Expansion Hub (REV-31-1153)**. | R x25 | [C] **NARROWED vs DEC/ITD**, which said only "smartphone or REV Control Hub". BIOBUZZ names part numbers and requires a phone to be paired with an Expansion Hub |
| 17 | **ROBOT SIGN** | Simultaneously shows a ROBOT's team number and its ALLIANCE affiliation to FIELD STAFF. | R x22, S1 x1 | [C] evergreen; see the ROBOT SIGN doc in `manuals/archive/supplemental/` |
| 18 | **STARTING CONFIGURATION** | The physical configuration a ROBOT is in at the start of a MATCH. | R x9 | [C] evergreen; the hook every sizing/expansion rule hangs on |
| 19 | **STUDENT** | Has not completed high school / secondary school or the equivalent **in their HOME REGION** as of September 1. | A x12, I x2 | [C] **REWORDED**: DEC said "their home region" (lower case, undefined); ITD said only "as of September 1 prior to Kickoff" |
| 20 | **TILE** | FIELD flooring: 36 interlocking soft foam TILES. | R x2 | [C] **DIMENSIONS DROPPED** vs ITD, which specified 24 in. x 24 in. x 5/8 in. DEC had already dropped them |
| 21 | **VENDOR** | Legitimate business source for COTS items meeting Section 12 criteria. | R x19 | [C] evergreen |
| 22 | **VERBAL WARNING** | Warning issued by event staff or the Head REFEREE. | E x1 | [C] present in DEC, **absent from ITD** (added 2025-26) |

### 1.1 The single most useful line in the whole glossary

**HOME REGION is the only genuinely new defined term in V0.** [C] Verified: `grep -c "HOME REGION"` returns
**0** for both `2025-26_DECODE_Competition_Manual_TU32.txt` and `2024-25_INTO_THE_DEEP_Competition_Manual_V14.txt`,
and **9** for `2026-27_BIOBUZZ_Competition_Manual_V0.txt`. It is a *tournament-structure* noun, not a game noun —
it formalises region-locked advancement (V0 §4 Advancement, p.27–28: teams may be invited to compete outside
their HOME REGION but are not advancement-eligible from those events; teams look their region up on FTC-Events).
Every other V0 glossary term is inherited verbatim or near-verbatim.

---

## 2. Terms V0 **uses in ALL CAPS but does not define** — the pre-marked glossary slots

These are the highest-confidence predictions in this document. V0's finalized sections use these caps
terms; V0's glossary omits them; DEC **and** ITD both define them. They are near-certain to reappear in
the Kickoff glossary. Counts are from `manuals/archive/2026-27_BIOBUZZ_Competition_Manual_V0.txt`.

| Term | Uses in V0 | Where it surfaces | Confidence |
|---|---|---|---|
| **MATCH** | 76 | S4 Advancement tables, S5 Event, S12 R, S14 League | [C] used / [H] will be defined |
| **FIELD** | 36 | R rules; the ARENA, CHASSIS and ROBOT definitions | [C] used / [H] will be defined |
| **DRIVER STATION** | 22 | R901-adjacent R rules | [C] used / [H] will be defined |
| **SCORING ELEMENT(S)** | 12 | ARENA and MAJOR MECHANISM definitions, R rules | [C] used / [H] will be defined |
| **FIELD STAFF** | 9 | ROBOT SIGN definition, E rules | [C] used / [H] will be defined |
| **FABRICATED ITEM** | 9 | R construction rules | [C] used / [H] will be defined |
| **FTA** | 5 | E rules | [C] used / [H] will be defined |
| **CUSTOM CIRCUIT** | 4 | R5xx electrical rules | [C] used / [H] will be defined |
| **DRIVE TEAM** | 3 | OPERATOR CONSOLE definition, E rules | [C] used / [H] will be defined |
| **FOULS** | 3 | **Table 4-2 Advancement Sorting Criteria** (V0 p.28) | [C] FOULS exist in BIOBUZZ |
| **AUTO** | 2 | Table 4-2 tiebreaker #7; §6.3.7 Control Award (p.~53) | [C] AUTO period exists in BIOBUZZ |
| **TELEOP** | 1 | §6.3.7 Control Award | [C] TELEOP period exists in BIOBUZZ |
| **RED CARD / YELLOW / VERBAL WARNINGS** | 1–2 | §14 League Play cites "Section 10.6.1 YELLOW and RED CARDS…" | [C] card system + §10.6.1 heading confirmed |
| **RANKING POINTS** | 1 | §14 League Play, p.90 | [C] RP exist in BIOBUZZ |

**Two hard scoring facts fall out of Table 4-2 (V0 §4 Advancement, p.28) — both [C]:**

1. Tiebreakers 6, 8 and 9 are *"Average / Highest individual / Second Highest individual Qualification MATCH
   Points **(excluding FOULS)**"*. → BIOBUZZ has FOULS, they contribute to a MATCH point total, and they are
   excluded from advancement tiebreakers.
2. Tiebreaker 7 is *"Average Qualification AUTO Points"*.
   → **AUTO points are tracked as a separate, named scoring column in BIOBUZZ.** Confirmed before we have
   seen a single game rule. A team that ignores AUTO loses a tiebreaker lane, not just points.

Terms defined in DEC **and** ITD that V0 does **not** even use (0 hits): ALLIANCE AREA, ALLIANCE CAPTAIN,
ARENA FAULT, CONTINUOUS, CONTROL, DISABLED, DISQUALIFIED, DRIVE COACH, HUMAN PLAYER, LAUNCH/LAUNCHING,
MAJOR FOUL, MINOR FOUL, MOMENTARY, PIN/PINNING, RANKING SCORE, REPEATED, SIGNAL LEVEL, SPIKE MARK,
SURROGATE, WTA, YELLOW CARD. [H] These live in Sections 9/10/11/13, all placeholders in V0 — expect
them back essentially verbatim.

---

## 3. Three-way glossary diff — BIOBUZZ V0 vs DECODE vs INTO THE DEEP

Term counts: **BIOBUZZ V0 = 22**, **DECODE = 76**, **ITD = 70**. Term lists extracted from bold spans in
the term column (x < 150 pt) of each Section 16 — this is exact, unlike the flat text.

### 3.1 List A — EVERGREEN (defined in all three seasons) — 19 terms

`ALLIANCE · ARENA · CHASSIS · COMPONENT · COTS · INSPECTOR · JUDGE · LRI · MAJOR MECHANISM · MECHANISM ·
OPERATOR CONSOLE · REFEREE · ROBOT · ROBOT CONTROLLER · ROBOT SIGN · STARTING CONFIGURATION · STUDENT ·
TILE · VENDOR`

[C]/[H] These are the *stable spine*. None of them will change meaning at kickoff. Anything in a Kickoff
game rule that turns on one of these words can be reasoned about **today**, before the manual drops.

Plus two 2-season-old additions carried into BIOBUZZ: **PORTFOLIO** and **VERBAL WARNING** (present in DEC,
absent from ITD).

### 3.2 List B — NEW in BIOBUZZ V0 — 1 term

`HOME REGION` — see §1.1. [C]

### 3.3 List C — vacated by V0 but present in **both** DEC and ITD — 35 terms

*(evergreen game/tournament vocabulary temporarily missing because Sections 8–11, 13 and 15 are placeholders)*

`ALLIANCE AREA · ALLIANCE CAPTAIN · ARENA FAULT · AUTO · CONTINUOUS · CONTROL · CUSTOM CIRCUIT · DISABLED ·
DISQUALIFIED · DRIVE COACH · DRIVE TEAM · DRIVER · DRIVER STATION · FABRICATED ITEM · FIELD · FIELD STAFF ·
FTA · HUMAN PLAYER · LAUNCH/LAUNCHING · MAJOR FOUL · MATCH · MINOR FOUL · MOMENTARY · PIN/PINNING ·
RANKING POINTS (RP) · RANKING SCORE (RS) · RED CARD · REPEATED · SCORING ELEMENT · SIGNAL LEVEL ·
SPIKE MARK · SURROGATE · TELEOP · WTA · YELLOW CARD`

[H] Expect nearly all 35 back on 2026-09-12. Note that **LAUNCH/LAUNCHING** and **SPIKE MARK** survived from
ITD into DECODE even though ITD had no launching game — FIRST keeps *verb* and *marking* definitions in the
glossary regardless of whether the season uses them, because G-rules reference them. [S] Therefore the mere
presence of LAUNCH/LAUNCHING in the BIOBUZZ glossary will **not** by itself prove BIOBUZZ has a shooter.

### 3.4 List D — DECODE-only game nouns, now **vacated** — 20 terms

`ARTIFACT · BASE · BASE ZONE · CLASSIFIED · CLASSIFIER · DEPOT · GATE · GATE ZONE · GOAL · LAUNCH LINE ·
LAUNCH ZONE · LEAVE · LOADING ZONE · MOTIF · OBELISK · OVERFLOW · PATTERN · RAMP · SECRET TUNNEL ZONE · SQUARE`

### 3.5 List E — ITD-only game nouns, now **vacated** — 16 terms

`ALLIANCE SPECIFIC · ASCEND/ASCENDED/ASCENT · ASCENT ZONE · BASKET (LOW and HIGH) · CHAMBERS · CLIP · LEVEL ·
NET ZONE · OBSERVATION ZONE · PARK · PLOWING · RUNG (LOW and HIGH) · SAMPLE · SPECIMEN · SUBMERSIBLE ·
SUBMERSIBLE ZONE`

### 3.6 Reading the vacated slots — what the shape of Lists D and E predicts

[S] but structurally strong. Both seasons filled the *same functional slots*:

| Slot | DECODE filled it with | ITD filled it with | BIOBUZZ slot count to expect |
|---|---|---|---|
| Scoring element (primary) | ARTIFACT | SAMPLE | 1–2 |
| Scoring element (derived / state) | CLASSIFIED, OVERFLOW | SPECIMEN (= SAMPLE + CLIP) | 0–2 |
| Scoring element (secondary physical) | — | CLIP | 0–1 |
| Goal / target structure | GOAL, CLASSIFIER (SQUARE, RAMP, GATE) | SUBMERSIBLE (BASKET, CHAMBER, RUNG) | 1 parent + 2–3 named sub-parts |
| Info / randomisation object | OBELISK → MOTIF → PATTERN | — | 0–1 (**[S]** an AprilTag-bearing prop; see AprilTag docs in `manuals/archive/supplemental/`) |
| ZONE nouns | BASE, GATE, LAUNCH, LOADING, SECRET TUNNEL | ASCENT, NET, OBSERVATION, SUBMERSIBLE | **4–5 ZONE nouns**, plus ALLIANCE AREA |
| Tape / marking noun | LAUNCH LINE, DEPOT, SPIKE MARK | SPIKE MARK | 1–3 |
| AUTO-only accomplishment | LEAVE | — | 0–1 |
| End-of-MATCH accomplishment | BASE | ASCENT (LEVEL 1/2/3) | 1, probably tiered |
| Ownership adjective | *(used "ALLIANCE specific" un-capitalised)* | ALLIANCE SPECIFIC | 0–1 |

**Expected BIOBUZZ new-noun count: 16–20**, based on DECODE=20 and ITD=16 game-specific terms. Given the
"BIOBUZZ" bee-and-biology theming [S], candidate lexical fields to watch for: hive/comb/cell, pollen/nectar/
honey, flower/bloom/blossom, colony/swarm/apiary, larva/brood, gene/sequence/strand, specimen/culture.
**Do not assume any of these.** They are a priming list, not a prediction.

---

## 4. The ALL-CAPS convention and how to weaponise it

### 4.1 The convention

[C] Stated twice in V0: §1 Introduction, p.17 — key words with special FTC/BIOBUZZ meaning are defined in
Section 16 and shown in ALL CAPS throughout the document; and the §16 preamble, p.92 — defined terms are in
all capitals, and any word without a game definition takes its ordinary conversational meaning.

[H] **The convention is only three seasons old.** It arrived with the single-document *Competition Manual*
in 2024-25 (ITD). Verified across this corpus: `End Game` appears 12–20x in every Part 2 manual from
2015-16 RES-Q through 2023-24 CENTERSTAGE and **0x** in ITD and DECODE; `Driver-Controlled` likewise
26–40x through CENTERSTAGE and **0x** after. Legacy manuals used Title Case for game nouns
(`Pixel`, `Backdrop`, `Cone`, `Junction`, `Stone`, `Foundation`) and had **no Section 16 glossary at all**
(`grep -i glossary` returns nothing in either CENTERSTAGE part). So the caps trick works on ITD, DECODE
and BIOBUZZ, and **not** on 2015–2024 manuals.

### 4.2 Why it is exploitable

FIRST capitalises a defined term **everywhere, including headings and the table of contents**. Every scoring
element, goal, zone, period and scoring accomplishment is therefore a token that (a) is uppercase, (b) has
never appeared in V0, and (c) has never appeared in DECODE or ITD. Set-subtract and you have the game's
entire new vocabulary before you have read a single rule.

### 4.3 The stoplist

`reference/known_caps_stoplist.txt` — 341 tokens in 3 commented tiers. `#` header lines are inert under
`grep -vxF` (whole-line fixed matching), so the file is safe to use directly as a pattern file.

| Tier | Contents | n |
|---|---|---|
| 1 | Every ALL-CAPS token present anywhere in BIOBUZZ V0 — includes REV part numbers, ANSI/CSA/IEC standards, DIO/I2C/PWM/RS485, RTX, BIOBUZZ itself | 178 |
| 2 | Caps tokens present in **both** DECODE and ITD but absent from V0 — the evergreen game/tournament vocabulary (ZONE, AREA, FOUL, CARD, PIN, CONTROL, LEVEL, MARK, LAUNCH, HUMAN, PLAYER, SURROGATE, RP, RS, SPIKE, MOMENTARY, CONTINUOUS, REPEATED …) | 80 |
| 3 | Generic English / typography noise picked up from headings and emphasis (THE, AND, NOT, TABLE, FIGURE, APPENDIX, VERSION …) | 83 |

**Deliberate trade-off in Tier 2:** head-nouns `ZONE / AREA / LEVEL / MARK / CONTROL / LAUNCH` are
suppressed. A new `POLLEN ZONE` still surfaces, because `POLLEN` is not on the list — you just see the
modifier, not the whole phrase. That is what the **bigram pass (step 3 in §0)** is for; it reconstructs the
full phrase for every novel token. If you want maximum recall on a first pass, run the single-token pass
with Tier 1 only:

```bash
sed -n '/TIER 1/,/TIER 2/p' reference/known_caps_stoplist.txt | grep -v '^#' > /tmp/t1.txt
grep -oE "\b[A-Z]{3,}('S)?\b" /tmp/k.txt | grep -vxF -f /tmp/t1.txt | sort | uniq -c | sort -rn | head -60
```

**Why `[A-Z]{3,}` and not `[A-Z][A-Z0-9'-]{2,}`:** requiring 3+ consecutive letters and no digits kills
rule IDs (`G301`, `R505`, `T206`), version tags (`V10`, `V15`) and revision markers (`M10`, `M11`) without
needing extra filters. Tested — it removed every one of them from the DECODE dry run.

### 4.4 Validation — dry runs against DECODE and ITD

The stoplist was built to contain **zero** DECODE-only or ITD-only game nouns, so running the §0 commands
against those manuals simulates kickoff day exactly.

**vs DECODE**, top 20 hits of step 2, verbatim:

```
87 ARTIFACTS   70 ARTIFACT   65 GATE       58 GOAL     50 RAMP      40 BASE       32 LAUNCH
31 PATTERN     25 DECODE     23 OBELISK    22 LOADING  21 SQUARE    19 CLASSIFIED 17 MOTIF
16 DEPOT       15 OVERFLOW   11 TUNNEL     11 SECRET   10 LINE       9 CLASSIFIER
```

That is **DECODE's entire game vocabulary, in frequency order, with no rule-ID or part-number noise**.

**vs ITD**, top hits:

```
63 SUBMERSIBLE  56 SAMPLES  47 OBSERVATION  45 ASCENT  39 SAMPLE  35 SPECIMEN  26 NET
24 SPECIMENS    23 CHAMBERS 22 DEEP         20 RUNGS   20 CLIP    19 BASKETS   16 BASKET
14 RUNG         12 CHAMBER  10 ASCEND        6 PARK     5 PARKING   5 CLIPS
```

Again complete, again clean. Note how frequency rank alone tells you the game's centre of gravity:
DECODE is an ARTIFACT/GOAL/RAMP game; ITD is a SUBMERSIBLE/SAMPLE/SPECIMEN game.

**Bigram pass vs DECODE** correctly recovered `LOADING ZONE`, `BASE ZONE`, `LAUNCH LINE`,
`SECRET TUNNEL ZONE`, `LAUNCH ZONE`, `GATE ZONE`, `CLASSIFIED ARTIFACTS`, `OVERFLOW ARTIFACTS`.

**First-sighting pass** is the sleeper. The first occurrence of a novel token is almost always its
Section 9/10 heading or the one-sentence game summary. For DECODE it returned:

```
ARTIFACTS   In DECODE presented by RTX 2 competing ALLIANCES of 2 teams each score purple and green …
ARTIFACT    10.5.1 ARTIFACT Scoring Criteria …
GATE        9.8.3 GATE …
GOAL        9.7 GOAL …
RAMP        9.8.2 RAMP …
BASE        their GOAL, build PATTERNS, and race back to their BASE before time runs out.
```

Field taxonomy and the object of the game, in one command.

### 4.5 Section-heading pass (the structural twin of the caps pass)

Sections 9 (ARENA) and 10 (Game Details) put every field element in its own numbered sub-heading.
DECODE's, for reference [H] — expect BIOBUZZ's to be the same skeleton with different nouns:

```
9.1 Dimensions and Accuracy   9.2 FIELD       9.3 Areas, Zones, & Markings   9.4 TILE Coordinates
9.5 ALLIANCE AREA             9.6 OBELISK     9.7 GOAL                       9.8 CLASSIFIER
    9.8.1 SQUARE   9.8.2 RAMP   9.8.3 GATE
9.9 SCORING ELEMENTS          9.10 AprilTags  9.11 FIELD STAFF               9.12 Event Management System

10.1 MATCH Overview  10.2 DRIVE TEAM  10.3 Setup  10.4 MATCH Periods  10.5 Scoring  10.6 Violations
    10.3.1 SCORING ELEMENTS  10.3.2 DRIVE TEAMS  10.3.3 OPERATOR CONSOLES  10.3.4 ROBOTS
    10.5.1/.2/.3 <NOUN> Scoring Criteria   10.5.4 Point Values
    10.6.1 YELLOW and RED CARDS  10.6.2 …application  10.6.3 …during Playoff MATCHES  10.6.4 Violation Details
10.7 Head REFEREE  10.8 Other Logistics
```

`9.5 ALLIANCE AREA` / `9.9 SCORING ELEMENTS` / `10.5.x <NOUN> Scoring Criteria` are the slots to read first:
**the number of `10.5.x` sub-headings equals the number of independent scoring categories in BIOBUZZ**, and
`10.5.4 Point Values` is the single table that decides your entire strategy.

---

## 5. Structural cross-references already frozen in V0 [C]

V0's *finalized* sections cite section numbers that live inside the *placeholder* sections. Those citations
are promises about the Kickoff manual's structure.

| V0 location | Forward reference | What it proves about the Kickoff manual |
|---|---|---|
| §14 League Play, p.90 | "Section 10.6.1 YELLOW and RED CARDS, VERBAL WARNINGS" | §10.6.1 exists with that title; cards and verbal warnings clear at the end of each League Meet |
| §14 League Play, p.90 | "Section 13.6 Qualification MATCHES" | §13.6 title unchanged from DECODE |
| §4 Advancement, p.29 | "Section 13.6.3 Qualification Ranking" | §13.6.3 title unchanged; qualification rank feeds the advancement equation |
| §4 Advancement, p.30 | "Section 13.7.2 Playoff MATCH Bracket" | §13.7.2 title unchanged; ALLIANCE selection + bracket retained |
| §4 Advancement, p.28 and §6 Awards | "Section 13.8 Dual Division Events" | Dual Division events retained for BIOBUZZ |
| §14 League Play, p.90 | "Table 13-1" sort order; top-10 League Meet MATCHES fold into ranking | §13 ranking table exists; League ranking math unchanged |

All five §13 sub-section titles match DECODE's §13 headings **exactly**. [S] Section 13 is therefore likely
to be a near-verbatim carry-over — worth diffing first on kickoff day precisely because it is the section
where a small change is easiest to miss.

**Two minor documentation notes worth flagging to your team [C]:**

- V0 Table 4-2 (p.28) calls tiebreaker 5 *"Qualification Phase Performance Points"* while V0 §14 (p.90)
  calls the same quantity *"Qualification Round Performance Points"*. Same thing, two names.
- V0 contains **no unresolved `[G###]` cross-links** anywhere outside the p.17 worked example — meaning the
  already-final R / E / A / I rules make **zero** forward references into the unreleased game rules. Read
  Section 12 now; nothing in it is waiting on kickoff.

---

## 6. Naming archetypes across 11 seasons

Sources: `manuals/archive/wayback/*_Part2*.txt` (2015-16 → 2019-20), `manuals/archive/*_Part2_Traditional.*`
(2020-21 → 2023-24), `manuals/archive/2024-25_*`, `manuals/archive/2025-26_*`. Counts below are occurrences
in the game-rules half of each manual. **Title Case through 2023-24; ALL CAPS from 2024-25.**

| Season | Scoring element(s) | Goal / target structure | Zone / area nouns | End-of-match stunt | Info / randomiser |
|---|---|---|---|---|---|
| 2015-16 RES-Q | Debris (Particles, Cubes) | Floor Goal, Rescue Beacon, Mountain | Cliff Zone, Low/High Zone, Climbing Area, Beacon Repair Zone | Climb the Mountain, Zip Line, Shelter | Beacon state |
| 2016-17 VELOCITY VORTEX | Particle, Cap Ball | Center Vortex, Corner Vortex, Beacon | Base Area, Alliance Area, Competition Area | Cap the Center Vortex, park on Ramp | Beacon |
| 2017-18 RELIC RECOVERY | Glyph, Relic, Jewel | Cryptobox, Recovery Zone | Recovery Zone, Safe Zone | Balance on Balancing Stone, place Relic | Jewel + VuMark |
| 2018-19 ROVER RUCKUS | Mineral (Gold, Silver) | Lander, Cargo Hold, Depot | Crater, Depot | Latch onto the Lander | Sampling / Gold position |
| 2019-20 SKYSTONE | Stone, SkyStone, Capstone | Foundation, Skybridge | Building Zone, Loading Zone, Depot | Capstone, park under Skybridge, move Foundation | SkyStone position |
| 2020-21 ULTIMATE GOAL | Ring, Wobble Goal | Tower Goal (High/Mid/Low), Power Shot | Launch Zone, Target Zone, Drop Zone, Start Line | Power Shots, deliver Wobble Goal, park | Starter Stack ring count |
| 2021-22 FREIGHT FRENZY | Freight (Box/Cube/Ball), Duck, Team Shipping Element | Alliance Shipping Hub, Shared Shipping Hub, Carousel | Warehouse, Storage Unit | Capping, park in Warehouse, Duck delivery | Barcode + Team Shipping Element |
| 2022-23 POWER PLAY | Cone, Signal Cone/Sleeve | Junction (Ground/Low/Medium/High), Terminal, Substation | Signal Zone, Scoring Area, Junction Area, Substation Storage Area | Beacon cap, Circuit, park in Signal Zone | Signal Sleeve |
| 2023-24 CENTERSTAGE | Pixel (Purple/Yellow), Drone | Backdrop, Backstage, Rigging, Stage Door, Truss | Backstage, Wing, Landing Zone, Spike Mark | Launch the Drone, hang from Rigging | Team Prop on Spike Mark |
| 2024-25 INTO THE DEEP | **SAMPLE, CLIP, SPECIMEN** | **SUBMERSIBLE** (BASKET low/high, CHAMBER low/high, RUNG low/high) | **NET ZONE, OBSERVATION ZONE, ASCENT ZONE, SUBMERSIBLE ZONE, ALLIANCE AREA** | **ASCENT (LEVEL 1/2/3)**, PARK | — |
| 2025-26 DECODE | **ARTIFACT** (states: CLASSIFIED, OVERFLOW) | **GOAL**, **CLASSIFIER** (SQUARE, RAMP, GATE), DEPOT | **BASE ZONE, GATE ZONE, LAUNCH ZONE, LOADING ZONE, SECRET TUNNEL ZONE, ALLIANCE AREA** | **BASE** (return to BASE ZONE) | **OBELISK → MOTIF → PATTERN** |

### 6.1 Rules extracted from the table

| Archetype | Pattern | Evidence strength |
|---|---|---|
| **Scoring-element noun** | Always a short, concrete, thematic **singular noun** that pluralises cleanly. 11/11 seasons. Two elements that **combine** into a third appeared in ITD (SAMPLE+CLIP→SPECIMEN) and 2017-18 (Glyph/Cryptobox). | [H] very strong |
| **Goal / target noun** | A single named **parent structure** with 2–3 named **sub-parts** at different heights or processing stages. 9/11 seasons. DECODE: GOAL + CLASSIFIER{SQUARE, RAMP, GATE}. ITD: SUBMERSIBLE{BASKET, CHAMBER, RUNG}. | [H] very strong |
| **Zone noun** | `<MODIFIER> ZONE` or `<MODIFIER> AREA`, defined as an *"infinitely tall volume bounded by …"* with tape or field-perimeter boundaries. 11/11. ITD and DECODE each ran **4–5** distinct ZONE nouns plus ALLIANCE AREA. | [H] very strong |
| **Period names** | **AUTO** and **TELEOP** only, since 2024-25. `End Game` and `Driver-Controlled` were retired after CENTERSTAGE and appear **0x** in ITD and DECODE. **[C] V0 uses AUTO and TELEOP and never uses ENDGAME (0 hits).** | [C] for BIOBUZZ |
| **Endgame stunt noun** | Still exists as a *scoring accomplishment*, but **is no longer a named period**. ITD gated it with an explicit clock window ("last 30 seconds of a MATCH", audio cue "Train Whistle" at 0:30); DECODE gated it only with "at the end of the MATCH". | [H] strong — **this is the single most likely thing a student gets wrong.** Do not write "endgame" on a strategy board; write the actual gating condition |
| **Ownership vocabulary** | ITD defined `ALLIANCE SPECIFIC` as an adjective; DECODE dropped it to lower case. Both use `ALLIANCE colored tape` for zone boundaries and `ALLIANCE neutral` for shared elements. Legacy used `Alliance Station`; ITD/DECODE use **ALLIANCE AREA**. | [H] moderate |
| **Bonus / RP vocabulary** | `RANKING POINTS (RP)` + `RANKING SCORE (RS)` in both ITD and DECODE, and **RANKING POINTS is used in V0 §14** [C]. ITD awarded RP for winning/tying; DECODE moved to per-accomplishment RP. The game-specific bonus nouns (DECODE's PATTERN, ITD's LEVEL) are the ones to hunt at kickoff. | [C] RP exists / [H] structure |
| **Verb definitions** | FIRST defines *verbs* as caps terms too: CONTROL, LAUNCH/LAUNCHING, PIN/PINNING, PLOWING, PARK, ASCEND, LEAVE. These carry the G-rule penalty logic. | [H] strong |
| **Duration adjectives** | `MOMENTARY` (fewer than ~3 s), `CONTINUOUS` (more than ~10 s), `REPEATED` (more than once per MATCH) — identical wording in ITD and DECODE. These three words silently set nearly every penalty threshold in Section 11. | [H] very strong |

### 6.2 Practical consequence for kickoff day

The **highest-value 10 minutes** of kickoff-day reading is not Section 11. It is:

1. the Section 16 glossary **verb** entries (CONTROL, LAUNCH, PIN, PARK, and whatever BIOBUZZ adds), and
2. the three duration adjectives (MOMENTARY / CONTINUOUS / REPEATED),

because nearly every G-rule in Section 11 is written as `<verb> + <duration adjective> + <zone noun>`, and
the exploitable gaps are between those definitions, not in the rule text. A student reads G-rules; the
glossary is where the rules actually live.

Second-highest value: `10.5.4 Point Values` plus the count of `10.5.x` sub-headings. That is the whole
scoring model on one screen.

---

## 7. Files written by this pass

| Path | Contents |
|---|---|
| `C:/Users/ericj/Documents/BIOBUZZ Analysis/reference/KEYWORD-GLOSSARY.md` | this document |
| `C:/Users/ericj/Documents/BIOBUZZ Analysis/reference/known_caps_stoplist.txt` | 341-token, 3-tier known-caps stoplist; safe as a `grep -vxF -f` pattern file |

---

## 8. Security note

Nothing in `BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf`, the DECODE / INTO THE DEEP manuals, or the
archived Part 1 / Part 2 manuals inspected for this pass contained text addressed to an AI assistant or any
attempt to issue instructions. All content was treated as data.

---

## 9. Known limitations

- **DECODE (76) and ITD (70) term lists** were extracted from bold spans in the term column and are exact.
  `RUNG (LOW and HIGH)` and `BASKET (LOW and HIGH)` are single ITD glossary rows covering two structures each.
  Definition *wording* for a handful of DECODE/ITD rows with very tall cells may have bled between adjacent
  rows during extraction — **term lists are trustworthy; DECODE/ITD definition wording quoted from this file
  should be re-checked against the PDF before being used in a rules argument.** BIOBUZZ V0's 22 rows were
  verified individually against page geometry and are exact.
- The stoplist is built from three manuals only. Caps tokens unique to one *older* season (2015–2024) are
  not suppressed — but those manuals barely used caps at all, so the practical false-positive rate is near
  zero (see the dry runs in §4.4).
- Team Update documents (`manuals/_reference_prior_seasons/*_TeamUpdates_Combined.pdf`) were **not** mined
  for late-season glossary additions. DECODE's `WTA` sits out of alphabetical order at the very end of its
  glossary, which is the signature of a Team-Update insertion — expect BIOBUZZ Team Updates to append terms
  the same way, out of alphabetical order. **Re-run the §0 novelty scan after every Team Update, not just at
  kickoff**, and pay particular attention to the bottom of the glossary table.
- Page numbers cited for V0 §4 and §6 are from the 93-page V0 PDF and will shift in the Kickoff release.
