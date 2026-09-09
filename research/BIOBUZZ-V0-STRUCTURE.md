# BIOBUZZ Pre-Season V0 — Annotated Structure Map & DECODE Diff

**Purpose.** This is the kickoff-day baseline. On 12 Sep 2026 the Kickoff Competition Manual gets diffed against
*this* document, not against DECODE. Everything below is sourced to file + page + rule ID.

**Evidence labels used throughout**

| Label | Meaning |
|---|---|
| **[V0]** | Stated in the BIOBUZZ Pre-Season V0 manual. Binding baseline unless FIRST changes it at Kickoff. |
| **[HIST]** | Historical pattern from prior seasons (DECODE / ITD). **Not** a BIOBUZZ fact. |
| **[INFER]** | My reasoning from V0 text/art. Explicitly flagged; not a quote. |
| **[SPEC]** | Speculation. Low confidence. Do not build on it. |
| **[UNVERIFIED]** | Could not confirm from the corpus. |

**Primary sources**

- `C:/Users/ericj/Documents/BIOBUZZ Analysis/manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf` (93 pp)
- `C:/Users/ericj/Documents/BIOBUZZ Analysis/manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_TU32.pdf` (188 pp)
- `C:/Users/ericj/Documents/BIOBUZZ Analysis/manuals/archive/supplemental/2026-27_BIOBUZZ_ImportantSeasonDates.pdf` (V26-27.1, dated 24 Jun 2026)
- `C:/Users/ericj/Documents/BIOBUZZ Analysis/manuals/archive/supplemental/2026-27_BIOBUZZ_RobotSign_USLetter.pdf` (V26-27.1, created 18 Jun 2026)

---

## 0. Text-extraction warnings (read before trusting any grep of V0)

The V0 PDF **silently drops digits in some table cells and rule bodies** under both `pdftotext` and `pymupdf`.
Verified instances — the rendered page is correct, the text layer is not:

| Location | Text layer says | Rendered PDF actually says | Verified how |
|---|---|---|---|
| p.76, R502 Table 12-2 | `≤   amps @6V` | `≤ 4 amps @6V` | rasterised crop |
| p.48, A201.C | `US Letter (8. ” x   ”) or A  (  0 x  97 mm)` | `8.5" x 11"` / `A4 (210 x 297 mm)` | matches DECODE A201.C |
| p.86, R710.B | `IEC/EN    7  “Exempt,”` | `IEC/EN 62471 "Exempt"` | matches DECODE R717.B |
| p.27–28, Figure 4-2 | `ualifying`, `S T`, `LM` | `Qualifying`, `SQT`, `LM` | figure text, Q glyph dropped |
| p.46, Figure 6-3 | `  Mins or more` / `  Mins or less` | `10 Mins or more` / `5 Mins or less` | inferred from A205/A207 |

**Harness rule: any numeric limit that matters must be confirmed by rasterising the page, not by reading the .txt.**
`R503` (8 motors / 8 servos) was re-verified this way. Every numeric claim below marked ✅ was rasterised or
cross-checked against DECODE.

---

## 1. Document identity

| Field | Value |
|---|---|
| Title block | "2026-2027 *FIRST*® Tech Challenge Competition Manual — BIOBUZZ™ Presented by RTX – Pre-Season V0" |
| Version marker | `V0` in every page footer and on the cover |
| Pages | 93 (`x of 93` footers) |
| PDF creation date | `D:20260731125257-04'00` (31 Jul 2026, 12:52 ET) — Microsoft Word for Microsoft 365 |
| Season umbrella brand | **FIRST® CANOPY™** (header of every page, `firstinspires.org/robotics/ftc`) |
| Presenting sponsor | RTX (§7, p.59) |
| Revision-history table | **Absent.** DECODE TU32 carries per-section version stamps (`V2`, `V6`, `V10`…) in footers; V0 stamps every section `V0`. Kickoff manual will restart per-section versioning. |
| PDF outline (TOC) entries | 88 |

---

## 2. Section-by-section map

Page ranges are printed-page numbers, which equal PDF page indices (no roman front matter).

| § | Title | Pages | Status | Rules | Notes |
|---|---|---|---|---|---|
| — | Cover | 1 | LOCKED | — | BIOBUZZ wordmark only. **No game artwork.** |
| — | Contents | 2–3 | LOCKED | — | |
| — | (blank) | 4 | — | — | |
| **1** | Introduction | 5–20 | **LOCKED** | — | Heavily rewritten vs DECODE. See §5.1. |
| 1.1 | About FIRST® | 5 | LOCKED | | |
| 1.2 | FIRST® Tech Challenge | 5–6 | LOCKED | | Rewritten: Scale / Skill Level / Complexity / Flexibility / Student Ownership |
| 1.3 | FIRST Ethos and Core Values | 6–9 | LOCKED | | 1.3.1 Gracious Professionalism, 1.3.2 Coopertition, 1.3.3 Core Values, 1.3.4 Why Embrace… |
| 1.4 | The Spirit of the Competition | 10–13 | LOCKED | | **NEW section.** 1.4.1 Note from FIRST Staff, 1.4.2 Framework of Behaviors, 1.4.3 Role of Mentors, 1.4.4 "The Sprit of FIRST Volunteer" *(typo in original)* |
| 1.5 | **Competition Integrity Contract (CIC)** | 14–16 | LOCKED | | **NEW.** 1.5.1 Sporting Ethics Code, 1.5.2 Behavior Guidelines, 1.5.3 Infractions, Mitigations & Escalation |
| 1.6 | Accessibility and Inclusion | 16 | LOCKED | | Verbatim carry-over from DECODE 1.5 |
| 1.7 | Understanding & Using the Competition Manual | 16–20 | LOCKED | | New wrapper heading over DECODE 1.6–1.9 |
| **2** | FIRST Season Overview | 21 | **LOCKED** | — | FIRST CANOPY branding page |
| **3** | Competition Eligibility and Inspection (I) | 22–26 | **LOCKED** | I101–I103, I301–I304 (7) | Was 11 rules in DECODE |
| **4** | Advancement | 27–32 | **LOCKED** | — | Points math **unchanged** |
| **5** | Event Rules (E) | 33–42 | **LOCKED** | 35 E-rules | Was 39 |
| **6** | Awards (A) | 43–58 | **LOCKED** | A201–A215 (15) | Same count, heavy rewrite |
| **7** | Game Sponsor Recognition | 59 | **LOCKED** | — | RTX logo + 3 photos, all from the **DECODE** season |
| **8** | Game Overview | 60 | **PLACEHOLDER** | — | |
| **9** | ARENA | 61 | **PLACEHOLDER** | — | DECODE had 12 subsections here |
| **10** | Game Details | 62 | **PLACEHOLDER** | — | DECODE had 8 subsections |
| **11** | Game Rules (G) | 63 | **PLACEHOLDER** | — | DECODE had ~60 G-rules |
| **12** | ROBOT Construction Rules (R) | 64–88 | **LOCKED** *(one hole)* | 52 R-rules | R105 sizing constraints deferred to Kickoff |
| **13** | Tournament (T) | 89 | **PLACEHOLDER** | — | DECODE had 8 subsections + brackets |
| **14** | League Play Tournaments (L) | 90 | **LOCKED** | — | ⚠️ **NOT a placeholder.** Full text, verbatim from DECODE §14 |
| **15** | FIRST Championship (C) | 91 | **PLACEHOLDER** | — | ⚠️ Placeholder despite not being commonly listed as one |
| **16** | Glossary | 92–93 | **LOCKED** *(pruned)* | — | 22 terms, down from ~77 |

**Placeholder count: 6 sections — 8, 9, 10, 11, 13, 15.** Sections 12 and 14 are *not* placeholders.

### 2.1 The placeholder sentence (exact, quoted once)

> "This section will be updated with the Kickoff Competition Manual release on September 12, 2026"

Appears verbatim six times: pp. 60, 61, 62, 63, 89, 91. No terminal period. Each placeholder page carries only the
section heading, this sentence, and the standard header/footer.

### 2.2 Forward references from LOCKED text into PLACEHOLDER sections

These are the **constraints the Kickoff manual is already bound by**. If a Kickoff section contradicts one of these,
that is a genuine error worth a Q&A on 28 Sep.

| From (locked) | Points at (placeholder) | What it presupposes |
|---|---|---|
| §4.1.1 p.29 | §13.6.3 Qualification Ranking | An EMS-reported qualification rank exists; `R` feeds the InvERF formula |
| §4.1.3 p.30, Table 4-1 | §13.7.2 Playoff MATCH Bracket | Playoffs award 1st/2nd/3rd/4th place |
| Table 4-1 p.28; A211 p.51 | §13.8 Dual Division Events | Dual-division events exist with modified advancement + award tables |
| §14 p.90 | §13.6 Qualification MATCHES | League Meets play **5–6 quals/team**; min **10** League Meet matches |
| §14 p.90 | **Table 13-1** | A ranking sort-order table will exist in §13 |
| §14 p.90 | §10.6.1 | Its future title is quoted as "**YELLOW and RED CARDS, VERBAL WARNINGS, and CARDS**" |
| §12 intro p.64 | §11 Game Rules (G) | MATCH-play consequences live in G-rules |
| R201 orange box p.68 | **`GXXX`** | A G-rule will govern damaging SCORING ELEMENTS in-MATCH |
| §1.7.1 p.17 | §13 (T), §14 (L), §15 (C) | T-, L-, and C-prefixed rules will exist |
| §3.3 p.23 | Practice MATCHES / filler line | §13.5.1 Filler Line concept survives |
| Table 4-2 p.29 | AUTO scoring | An **AUTO** period exists and is separately scored (tiebreaker #7) |
| §6.3.7 p.56 | AUTO and TELEOP | Both periods exist in BIOBUZZ |
| §4.1.4 p.30 | "Safety Animation Award" | ⚠️ **Inconsistency:** §6.6 no longer names this award |

---

## 3. Dates, deadlines and cadences stated in V0

All rows below are **[V0]** unless the Source column says otherwise.

| Date / cadence | What | Source |
|---|---|---|
| **12 Sep 2026** | Kickoff Competition Manual release; §§8–11, 13, 15 published | V0 pp.60–63, 89, 91 |
| **Every Thursday**, from Kickoff day through **two weeks before FIRST Championship** | Team Update cadence, posted on the Game and Season Materials page | §1.7.3 p.19 |
| — | ⚠️ V0 **dropped** DECODE's "generally posted by 1pm Eastern." No posting time is now promised. | vs DECODE §1.8 p.12 |
| **Driver's meeting** at an event | **NEW:** "Team Updates that are published after the driver's meeting at an event will not apply to that event." | §1.7.3 p.19 |
| **28 Sep 2026, 12:00 p.m. ET** | Game Q&A opens (Lead Coach 1 / Lead Coach 2 dashboard access) | §1.7.4 p.19 |
| **Mondays → Thursdays 5:00 p.m. ET** | Q&A moderator answer window each week | §1.7.4 p.19 |
| **1 Jan 2026** | Start of the "current season" for judging. PORTFOLIO content and all judged accomplishments must postdate this. | §6.1.1 p.45; A201.E p.48 |
| **1 September** (annual) | STUDENT eligibility cutoff: "has not completed high-school… as of September 1st" | Glossary p.93 |
| **17 Nov 2026** | Team-registration cutoff date used for FIRST Championship / Premier Event advancement allocation | §4.2 p.31 |
| **Early December 2026** | Regional advancement-slot allocations published on FTC-Events | §4.2 p.31 |
| **45 minutes before Qualification MATCHES** | Adult must complete event check-in at Pit Admin (unless Event Director specifies otherwise) | I102 p.22 |
| **48 hours before event start** | Deadline for Event Directors to communicate extra pit restrictions | §5.5 p.38 |
| **10-minute grace period** when the venue opens each day | Safety-glasses exemption window | E101.A p.33 |
| **≥10 minutes** | Minimum Initial Interview length, equal for all teams | A205 p.49 |
| **First 5 minutes** | Uninterrupted team presentation inside the Initial Interview | A207 p.50 |
| **2–5 extra minutes** | Translator/interpreter accommodation, requested in advance | A209 p.50 |
| **40–60 seconds** (max 60 s incl. credits) | Compass Award video | §6.5.2 p.58 |
| Deadline set by Event Director / PDP | PORTFOLIO submission (A202) and Compass Award submission | A202 p.49; §6.5.2 p.58 |
| No later than ALLIANCE selection | Deadline to publish minimum advancement numbers | §4.2 p.31 |

### 3.1 Dates from the companion "Key Season Dates" sheet (not in the manual)

| Date | Item |
|---|---|
| 1 Aug 2026 | FTC-Events defaults to BIOBUZZ season; **CM Preview Release** (this V0) |
| 17 Aug 2026 | Last date for regions to be counted for FCMP/FPE capacity-based advancement |
| **4 Sep 2026** | **Early Game Preview Information — privacy agreements required for all viewers** |
| 11 Sep 2026 | Last 2025-26 DECODE off-season event |
| 12 Sep 2026 | FTC Kickoff; FTC Scoring event configuration opens |
| Kickoff week | FTC SDK release; FTC Live preview (beta) |
| 14 Sep 2026 | FIRST Leadership Award nominations open |
| 28 Sep 2026 | Team **and Volunteer** Q&A open for BIOBUZZ |
| 2–4 Oct 2026 (proposed) | Preseason Testing Event |
| 15 Oct 2026 | FTC Live official release; **earliest League Meet / Qualifying Tournament date** |
| **16 Nov 2026** | Region Size Snapshot for FCMP advancement calculation |
| 19 Nov 2026 | FCMP + Premier Event advancement allocations released |
| 30 Nov 2026 | Earliest Dual Division and Regional Championship events |
| 15 Dec 2026 | FIRST Leadership Award nominations due |
| 21 Mar 2027 | Last RCMP date to receive FCMP/Premier advancement |
| 28 Apr – 1 May 2027 | **FIRST Championship** → Team Update cadence therefore ends ~**16 Apr 2027** |

> ⚠️ **Conflict to resolve at Kickoff:** V0 §4.2 says the registration cutoff is **November 17th, 2026**; the Key Season
> Dates sheet says the Region Size Snapshot is **November 16, 2026**. Two official BIOBUZZ documents, one day apart.
> Worth a Q&A on 28 Sep. **[V0 vs supplemental]**

---

## 4. Rule-count delta at a glance

| Section | DECODE TU32 | BIOBUZZ V0 | Δ |
|---|---:|---:|---:|
| 3 — Inspection (I) | 11 | 7 | −4 |
| 5 — Event (E) | 39 | 35 | −4 |
| 6 — Awards (A) | 15 | 15 | 0 |
| 12 — ROBOT Construction (R) | **73** | **52** | **−21 (−29%)** |
| **Total (comparable sections)** | **138** | **109** | **−21%** |
| Manual length | 188 pp | 93 pp | (§§8–11/13/15 removed) |
| Glossary terms | ~77 | 22 | −55 |

---

## 5. Full diff: BIOBUZZ V0 vs DECODE TU32

### 5.1 Section 1 — Introduction (the biggest structural change in the manual)

**Renumbering crosswalk**

| DECODE | BIOBUZZ V0 | Change |
|---|---|---|
| 1.3 Core Values → 1.3.1 Core Values, 1.3.2 GP, 1.3.3 Coopertition | 1.3 FIRST Ethos and Core Values → 1.3.1 **Gracious Professionalism**, 1.3.2 Coopertition, 1.3.3 Core Values, **1.3.4 Why Embrace the FIRST Ethos…** | Reordered (GP promoted to first); 1.3.4 is new |
| 1.4 Spirit of Volunteering | **1.4.4** "The Sprit of FIRST Volunteer" *(sic)* | Demoted to a sub-subsection under new 1.4 |
| — | **1.4 The Spirit of the Competition** (1.4.1–1.4.3) | **NEW** |
| — | **1.5 Competition Integrity Contract (CIC)** | **NEW** |
| 1.5 Accessibility and Inclusion | 1.6 Accessibility and Inclusion | Renumbered, text verbatim |
| 1.6 This Document & Its Conventions | 1.7.1 | Demoted under new 1.7 wrapper |
| 1.7 Translations & Other Versions | 1.7.2 | Demoted |
| 1.8 Team Updates | 1.7.3 | Demoted |
| 1.9 Question and Answer System | 1.7.4 **Question & Answer System** | Demoted + renamed |

#### 1.4.1 A Note from the FIRST Staff — **the single most important prose in V0**

This is FIRST openly announcing a change of rules-writing philosophy. Paraphrasing (p.11):

- Prior manuals "focused on covering exact circumstances and details, removing flexibility in favor of attempting to
  cover all scenarios."
- BIOBUZZ "emphasizes the 'spirit of the rule' and empowers event volunteers to make good-faith judgement calls."
- Rules are written so volunteers "watch for larger behaviors and strategies that run counter to the spirit of the
  competition, rather than be required to watch for and record every action or incident."
- Stated goal: make it easier to volunteer and produce "a more consistent competition experience."
- The change is explicitly conditional: "This change can only be possible if we all commit ourselves to the ethical
  standards described by the FIRST Ethos and FIRST Core Values."
- Games will "include familiar themes from the past… while also including new dynamics which shift the 'meta'."

**Why this matters for a rules-loophole review:** the entire enforcement model is shifting from
*enumerated-and-countable* to *judgement-based*. Strategies that were legal-because-unenumerated under DECODE are now
exposed to a "spirit of the competition" call. Conversely, REFEREE consistency risk goes **up**, which raises the value
of Q&A entries and of designing strategies that are obviously within intent.

#### 1.5 Competition Integrity Contract (CIC) — NEW, and it has teeth

Structure: **1.5.1 Sporting Ethics Code** (4 certifications) + **1.5.2 Behavior Guidelines** (8 certifications) +
**1.5.3 Infractions, Mitigations, & Escalation**.

Sporting Ethics Code headings, p.14: *We Don't Cheat* · *We Always Behave with Integrity* · *We Play the Game as
Intended* · *We Know Our Team Doesn't Enforce the Rules*.

Load-bearing clauses for a rules review:

| Clause | Consequence |
|---|---|
| "We Play the Game as Intended… Our team will not try to gain an advantage using any 'loopholes' in the rules." (p.14) | **Loophole exploitation is now itself a written violation**, not merely bad form. |
| "If there is ever ambiguity in the specific wording of a rule, we will look to the intent of the rule and spirit of the competition to guide our behavior." (p.14) | Directly reverses DECODE's textualist instruction (see 1.7.1 below). |
| "We understand that teams need to abide by all the regulations, even the ones that are not checked." (p.14) | Paired with I301's "Inspection is not comprehensive" note — self-policing is now contractual. |
| "We Know Our Team Doesn't Enforce the Rules… not appropriate for us to accuse, investigate, publicly call-out, or persecute anyone" (p.14) | Constrains how you may raise an opponent's violation. Route it to event staff, quietly. |
| Behavior Guidelines include *We Respect Property and Facilities*, *We Build a Positive Culture of Safety*, **We Make Healthy Choices** (anti-crunch language), *We're All on the Same Team* (pp.15–16) | Aspirational, but §1.5.3 makes violations escalatable. |
| §1.5.3: escalation to LRI / Head REFEREE / FTA; serious violations (esp. Sporting Ethics Code) → Event Director and/or FIRST HQ; possible sanction, DQ from current **and/or future** events, suspension or permanent removal. Escalation Guidelines document "(coming soon)". | A team-level, season-spanning penalty ladder that sits **outside** the G-rule card system. |

#### 1.6 Accessibility and Inclusion — verbatim carry-over from DECODE §1.5. No change.

#### 1.7 Understanding & Using the Competition Manual

| Item | DECODE | BIOBUZZ V0 | Significance |
|---|---|---|---|
| **Interpretation doctrine** | "The intent of this manual is that the text means exactly, and only, what it says. Please avoid interpreting the text based on assumptions about intent… There are no hidden requirements or restrictions." (§1.6 p.10) | **DELETED.** Replaced by: the Manual is the "source of truth"; in cases of discrepancy with supporting documents, the Manual takes precedence. (§1.7.1 p.17) | **The textualist safe harbour is gone.** The plain-meaning instruction survives only in the Glossary preamble ("Competition rules mean what they plainly say"), while the CIC pulls the other way toward intent. Expect this tension to drive Q&A. |
| **Evergreen rule definition** | "rules which are expected to go relatively unchanged from season to season… game specific terms may be updated (e.g., changing Pixels to Samples in a rule about what DRIVE COACHES may not contact)" | "rules which are expected to be **present each season with only their specific details changing**… (e.g., changing game specific terms, or **changing the specific details around ROBOT expansion within an Evergreen rule about expansion limits, or changing the quantity of allowed motors within an Evergreen actuator rule**)" (p.18) | **Direct signal**: expansion limits and actuator counts are on the table this season. R503 already moved (10→8 servos ✅) and R105 is explicitly deferred. |
| Rule-letter map | I/E/A/G/R/T/L/C | Identical | |
| Team resources | list includes "and award descriptions" | "and award descriptions" **removed** | Award descriptions are now manual-only, season-specific |
| AI Chatbot | "a FIRST Tech Challenge AI Chatbot are provided" | "AI Chatbot **(coming soon)**" | Being rebuilt for BIOBUZZ |
| Team Updates | posted "generally by 1pm Eastern" | time promise **removed**; **new** clause: updates after the driver's meeting don't apply to that event | Operationally significant |
| Q&A | opens 22 Sep 2025; separate view-only account instructions; "FTC 1000" volunteer-question paragraph | opens **28 Sep 2026 12:00 pm ET**; account instructions **removed**; **FTC 1000 paragraph removed**; the two "may not be answered" lists merged into one | Loss of the FTC 1000 channel disclosure is worth watching |
| Figure numbering | Figure 1-2 = rule numbering | Figure **1-3** = rule numbering | Figures 1-1 (Woodie Flowers) and 1-2 (GP word cloud) shifted |

---

### 5.2 Section 2 — FIRST Season Overview

| DECODE | BIOBUZZ V0 |
|---|---|
| "Uncover the Future" · **FIRST® AGE™ presented by Qualcomm** · inspired by **archaeology** | "Engineer a Thriving Planet with FIRST" · **FIRST® CANOPY™** · "our 2026-2027 robotics season **inspires by nature**" *(typo for "inspired")* |
| — | Thematic copy: "Every gene, species, and ecosystem is part of a rich web of biological diversity that powers clean air, fresh water, and food." Tagline: "Building. Problem solving. Growing stronger through teamwork." (repeated twice — layout artefact) |
| Link: firstinspires.org/firstage | Link: `https://www.firstinspires.org/first-canopy` |
| Season art: AGE program lockups | **CANOPY art (p.21) shows all three program games: BIOGLOW (green, leaf-on-circuit icon) · BIOBUZZ presented by RTX (yellow, honeycomb icon) · BIOCORE presented by HAAS (blue).** Background is topographic contour lines. |

No Qualcomm branding appears anywhere in V0; RTX is the FTC presenting sponsor (unchanged from DECODE).

---

### 5.3 Section 3 — Competition Eligibility and Inspection (I)

**Rule crosswalk**

| DECODE | BIOBUZZ V0 | Disposition |
|---|---|---|
| I101 Teams must be registered | I101 | Same; sub-item punctuation fixed |
| I102 Check-in on time (deferred to event schedule / E105) | **I102** — now carries the concrete "**no later than 45 minutes before Qualification MATCHES**" text that DECODE kept in **E105** | Merged; **E105's Violation line ("may result in a team not participating in the event") was dropped** |
| I103 Responsible adult present | I103 | Adults-follow-same-rules sentence **removed**; "Responsible adults **must** be listed on the team roster" → "**are recommended** to be listed" (weakened) |
| I301 *It is your team's ROBOT* | → **R101** | **Moved into Section 12** |
| I302 *Enter only 1 ROBOT* (Violation: VERBAL WARNING, RED CARD if uncorrected) | → **E117** | **Moved into Section 5; explicit Violation line deleted** |
| I303 *Get inspected before playing* (Violation: DQ / RED CARD) | → **prose only**, §3.3 p.23 | **Downgraded from a numbered rule with penalties to narrative** |
| I304 Bring complete ROBOT | **I301** | Renumbered; sub-item C (electronics totals) split out |
| I304.C electronics total | **I302** *Certain limits apply to all configurations* | Promoted to its own rule |
| I305 Re-inspect any change (Violation: RED CARD) | **I303** *Request re-inspection for most changes* | Renumbered; **Violation line deleted**; "must request" → "**should** request" |
| I306 Do not exploit re-inspection | **I304** | Renumbered, unchanged |
| I307 ROBOTS may be powered on | → prose, §3.3.1 p.23 | Downgraded to narrative |
| I308 STUDENTS present during inspection (Violation) | → prose, §3.3.1 p.23 | **Downgraded**; the explicit "at least 1 STUDENT must accompany" requirement and its Violation are gone |

**Other §3 changes**

- **Zero `Violation:` lines remain in Section 3.** DECODE had four. This is the "spirit of the rules" shift made concrete.
- **NEW orange box (p.24):** "Inspection is not comprehensive. Teams are expected to adhere to the spirit of the rules in
  Section 12… even if INSPECTORS do not check every part of the ROBOT. Teams that strategically circumvent ROBOT
  construction rules to gain a competitive advantage are not adhering to the Competition Integrity Contract (CIC) and may
  be subject to mitigation." **This is the CIC hooking directly into inspection.**
- **NEW:** Practice MATCH policy is now explicit and two-tier — teams may play **scheduled** Practice MATCHES before
  passing inspection, but **not** unscheduled/"filler line" ones (§3.3 p.23).
- **REMOVED:** DECODE's definition "A team has participated in a MATCH if any member of their DRIVE TEAM is in the
  ALLIANCE AREA…", and the whole DISABLED-robot-still-earns-points paragraph. **[INFER]** these move to §10 or §13 at Kickoff.
- §3.2 now names **A201** (PORTFOLIO) and **A203** (Initial Interview) and adds a pointer to **A213/A214** for multi-event
  and out-of-region teams. DECODE §3.2 cited A202 for the PORTFOLIO — a stale reference now corrected.

---

### 5.4 Section 4 — Advancement

**The math is unchanged.** Verified identical between DECODE TU32 and BIOBUZZ V0:

| Element | Value (identical in both) |
|---|---|
| Qualification Phase Performance | Normal distribution, **2 to 16** points, from the InvERF equation |
| Formula | `QualificationPoints(R,N,α) = ⌈InvERF((N−2R+2)/(αN)) · (7 / InvERF(1/α)) + 9⌉` |
| Alpha (α) | **1.07** |
| ALLIANCE lead | `21 − lead number` (e.g. 18 pts for ALLIANCE #3) |
| Draft Order Acceptance | `21 − draft position` |
| Playoff Advancement | **40 / 20 / 10 / 5** for 1st / 2nd / 3rd / 4th |
| Inspire Award | **60 / 30 / 15** for 1st / 2nd / 3rd |
| All other awards | **12 / 6 / 3** for 1st / 2nd / 3rd |
| Table 4-2 tiebreakers | Identical 10-level sort, incl. #6 Avg Qual MATCH Points (excl. FOULS), #7 Avg Qual **AUTO** Points |
| Table 4-3 sample | Rank 1→16, 2→15, 3→14, 4→14 … 28→4 (28-team event) |

**What did change**

| Change | Where | Significance |
|---|---|---|
| "home region" → **HOME REGION** (now a Glossary term) | throughout §4 | Formalised |
| **Clarified:** "Teams may participate in more than three entry-level events but **are eligible to advance from the first three chronological events**." DECODE said "…but are **not** eligible to advance from them." | p.27 | **Materially different reading.** DECODE's wording was ambiguous about whether events 4+ are excluded or the whole team is. V0 fixes it in teams' favour. |
| **NEW: Pilot events.** "Teams in a few specific geographical regions may advance from a Pilot event — the highest tier of competition within a new or emerging region — to FIRST Championship and/or a FIRST Premier Event." | p.28 | New advancement pathway |
| Figure 4-2 gains a **"Non Advancement Pilot"** node and footnotes 5 (optional event) and 6 (select new/emerging regions) | p.27 | |
| **REMOVED** from §4.1.2: the rationale about ALLIANCE selection supporting "come-from-behind teams", "late bloomer" recognition, unique-strategy niches, and "an additional minor benefit… allows teams who would traditionally not be a top ranked team the opportunity to be an ALLIANCE lead" | p.30 | Prose only; no scoring effect |
| **REMOVED** from §4.1.2: qual rankings "are designed to eliminate ties in rank" | p.30 | **[INFER]** possibly deliberate — a new ranking scheme may tolerate ties. Watch §13.6.3 at Kickoff. |
| §4.1.4 trimmed: "In many ways, the team's experience in being selected for awards… is beyond measure" removed | p.30 | Cosmetic |
| §4.2 factor list **reordered** — global/regional representation now first, team-count last | p.31 | May reflect allocation-priority change **[SPEC]** |
| Registration cutoff now dated: "**November 17th, 2026** for the BIOBUZZ season" | p.31 | See conflict note in §3.1 |
| "the FIRST Championship" → "FIRST Championship" throughout | | Cosmetic |

---

### 5.5 Section 5 — Event Rules (E)

#### Enforcement model changed at the top of the section (p.33)

| | DECODE §5 intro | BIOBUZZ V0 §5 intro |
|---|---|---|
| Universal Violation | "will result in **a warning from event volunteers**. Egregious or repeated violations **will be addressed with a VERBAL WARNING** from the Head REFEREE / LRI / Event Director. **Subsequent** violations may result in escalation to FIRST HQ and/or disqualification…" | "A violation of any Event Rules (E) will result in **a VERBAL WARNING**. **Egregious or subsequent** violations may result in escalation to FIRST Headquarters and/or disqualification for the team from MATCHES and awards." |

**Net effect: the informal first warning is gone. First E-rule violation = VERBAL WARNING immediately.** That is a
one-step escalation for every event rule. Also removed: the DECODE orange box "The Event Director has the final decision
authority for all safety-related issues within a venue." and "Safety is always paramount…".

#### Full E-rule crosswalk

| DECODE | BIOBUZZ V0 | Change |
|---|---|---|
| E101 Personal safety | E101 | **A. changed:** safety glasses "while in and around the playing FIELD and in the pit area" → "**in specified areas**" (now event-defined). Grace period simplified to "**10-minute grace period when the venue opens each day**". **Footwear blacklist deleted** (Crocs, slides, sandals, flip-flops, Birkenstocks, clogs). |
| E102 ***Be Nice*** | E102 ***Be Respectful*** | Now anchored to §1.4 Framework of Behaviors. **Item D rewritten:** DECODE's "jamming or interfering with the remote sensing capabilities of a ROBOT or the FIELD while in open-access spectator seating areas" **plus the AprilTag-mimicry-in-the-stands note** → V0's generic "**anything that interferes with a ROBOT or the ARENA operations**". Items E–K (assault, threat, harassment, bullying, insulting, swearing, yelling) unchanged. |
| E103 Children with adults | E103 | Unchanged |
| E104 Respect the venue | E104 | **+ "or items thrown from the stands"** (absorbs DECODE E802) |
| **E105 Teams must check in** | → **I102** | Moved; Violation line dropped |
| E106 Event resources | **E105** | −1 |
| E107 Practice only when/where permitted | **E106** | −1, text identical |
| E108 Work in designated areas | **E107** | −1, identical |
| E109 Some things do not belong | **E108** | **`walkie-talkies` REMOVED from the ban list.** **NEW item G: "any item with bright lights which flash faster than approximately 5 times per second."** |
| E110 additional utilities | **E109** *…additional **services** or utilities* | −1, retitled |
| E111 Do not sell stuff | **E110** | −1 |
| E112 ***Make FIRST loud, but with restrictions*** | **E111 *No Loud Music*** | **Retitled from permissive to prohibitive.** Body unchanged. |
| E113 Hang banners | **E112** | −1 (25 ft² banner limit retained) |
| E114 Flag/flagpole size | **E113** | −1 (3×5 ft, <2 lb; pole ≤8 ft, <3 lb retained) |
| E115 No firearms | **E114** | −1 |
| E116 Inspection required for practice FIELD | **E115** | −1 |
| E117 Do not record | **E116** | −1 |
| **(I302)** | **E117 *Enter only 1 ROBOT in the tournament*** | **Imported from Section 3.** All three orange boxes retained. **Violation line deleted.** |
| **E801** No saving seats | **E118** | Moved out of §5.8 |
| **E802** No throwing items from the stands | **DELETED** | Absorbed into E104 |
| **§5.8 In the Stands** | **DELETED** | Section removed entirely |
| E301, E302 Wireless | E301, E302 | Unchanged |
| E501 Pits closed | E501 | Unchanged |
| E502 ***Stay in your pit*** | **E502 *Pit set ups should be self-contained…*** | **Expanded with new prohibitions:** A. no running power/internet lines outside your pit; B. **no swapping pits with other teams**; C. **no moving into empty pits without Event Director approval.** |
| E503 Keep aisles clear | E503 *Keep aisles **and exit pathways** clear* | Broadened |
| E504 ***No sparks or flames*** | **E504 *Open flames and spark emitting devices must be limited and carefully controlled*** | **LOOSENED.** Now "generally prohibited, **except in limited and safely controlled instances**." Explicitly permits a lighter to melt strap ends and a sander to shorten a bolt with sparks directed safely. Welders, bench/angle grinders, gas torches still prohibited. |
| E505 ***Nothing too big*** | **E505 *Only small benchtop machinery is permitted in team pits*** | Retitled + defined: "'Small' machinery… can be easily lifted by one person" — 3D printers, small band saws, small drill presses, **desktop CNC mills**, sanders allowed. |
| E506 No brazing/welding | E506 | Unchanged |
| E507 Solder | E507 | Unchanged |
| E508 Structures must be safe | E508 *Pit structures must be safe* | **+ new popup-tent guidance** (allowed per E502, but coverings may violate if they interfere with fire suppression) |
| **E509 Secure team identification assets** | **DELETED** | Signs/flags/displays no longer required to be securely mounted to the pit structure |
| E510 Aerosols/noxious fumes | **E509** | −1 |
| — | **E510 *Don't heat or cool ROBOT components to gain an advantage*** | **BRAND-NEW RULE.** No DECODE analogue anywhere in the manual. Bans thermal manipulation for competitive advantage. Named violations: **cooling fuses so they take longer to trip**, **heating batteries to increase performance**, **freezing heatsinks**. Explicitly OK: heat-shrink installation, a battery warm from its normal charge cycle, components warm from prior use. Stated intent: "ROBOTS should compete as if they were left alone for an extended period of time in the competition venue at ambient temperature." |
| R603 + R604 (battery charging, in §12) | **E511 *Charge batteries in a safe and fair manner*** | **Moved from Section 12 to Section 5.** Consolidates: safe rate per manufacturer, **never exceed 3-amp average channel current**, polarized connectors only, never alligator clips. |
| E601–E605 (5 cart rules) | **E601 *Carts must not be a nuisance*** | **Consolidated 5 → 1**, six lettered sub-clauses. All substance retained: easy to control, no bystander risk, **fits a standard 30-inch (762 mm) door**, stays in the pit, no sound generators, **no powered propulsion**. |
| E701–E703 Ceremonies | E701–E703 | Unchanged (5-person pit limit during ceremonies retained) |
| §5.2 Machine Shops, §5.4 Load-In, §5.5 Pits narrative | Same | 10×10×10 ft pit, 48-hour notice for extra restrictions |

---

### 5.6 Section 6 — Awards (A)

#### Structural changes

| Change | DECODE | BIOBUZZ V0 |
|---|---|---|
| **Award categories** | Two categories (MCI, TA) + Think + Judges' Choice + Inspire | **Three categories: MCI, TA, and *Documentation*** + Judges' Choice + Inspire (p.43) |
| **Interview name** | "**structured interview**" (everywhere) | "**Initial Interview**" (everywhere) — §6.1.2, A203–A207, A210, A212 |
| **Interview formats** | One format, scheduled, in a dedicated space | **Three formats: Scheduled in-person · Unscheduled in-person (JUDGES come to your pit) · Remote.** "All three types… have the same rules." Event Director + JA + regional planning committee choose; all teams at an event use the same format. (p.46) |
| **JUDGE Advisor role** | "oversee the judging processes and procedures" | **+ "but they do not select who wins the awards"** (p.43) |
| **JUDGE definition** | interacts "during the interview process, and in the pits" | interacts "**in the pits and sometimes in dedicated judging spaces**" (p.43) — pit-first framing |
| **Volunteer feedback as an input** | "JUDGE Advisors may **also accept feedback about teams at the event from other volunteers** to help inform their understanding of the team." | **DELETED** (p.45) — **[INFER]** referee/queuer impressions are no longer a sanctioned judging input |
| **Season boundary** | implied via A201.E | **Explicit: "For the purposes of judging, the current season begins on January 1, 2026."** (p.45) |
| **Disallowed sources** | narrative paragraph | **Explicit bullet list** (p.45), and it **adds "ROBOT penalties during gameplay"** as a category JUDGES cannot consider |
| **FIRST Championship judging modifications** | §6.2 opened with a pointer to §15.1; §6.1.2 had an orange box pointing to §15.1.2 | **Both pointers deleted** (§15 is a placeholder) |
| **§6.6 Project-Based Global Awards** | Named **6.6.1 Digital Animation Award sponsored by WPI** and **6.6.2 Safety Animation Award sponsored by UL Solutions**, with the 2025-26 theme "Unearth Safety!" | **Both subsections DELETED.** Replaced with "More information about Project-Based Global Awards coming soon!" (p.58) |

⚠️ **Residual inconsistency:** §4.1.4 (p.30) still cites "(e.g., Safety Animation Award)" as an example of a non-event-judged
award, but that award no longer appears in §6. Either a stale reference or a hint it survives. **[V0 internal conflict]**

#### A-rule diffs (numbering is unchanged, A201–A215)

| Rule | Change |
|---|---|
| **A201** PORTFOLIO limits | Structure identical: 1 cover page, **≤15 pages of content**, US Letter or A4 ✅, **<15 MB** digital, content only since **1 Jan 2026**. **PII tightened:** DECODE "Teams are **encouraged to limit** PII… **optionally** last initials… Photographs including images of STUDENT team members are acceptable" → V0 "Teams **must strictly minimize** PII… use only first names **and** last initials. While student photographs are permitted, **full names must not be disclosed**." **Links:** DECODE's separate sentence retained but tightened to "JUDGES will not click on links, websites, or videos in a PORTFOLIO." **AI credit clause retained** ("Portfolio created by Team XXXXX and ChatGPT"). |
| **A202** submission | "during the **structured interview**" → "during the **Initial Interview**". Otherwise identical. |
| **A203** | "must **attend their assigned** structured interview session" → "must **participate in an** Initial Interview session" — necessary because unscheduled/pit interviews have no assigned slot. Orange-box guidance moved inline. |
| **A204** resources | B. "a **printed** copy of their team PORTFOLIO (**optional**, submit as instructed)" → "**a copy** of their team PORTFOLIO **for reference during the interview**" (no longer marked optional). Orange box on ROBOT demos: DECODE "unless explicitly disallowed by the Event Director… All teams should have the same demonstration restrictions" → V0 "**but may not cause significant delays during the interview.**" |
| **A205** | ✅ "at least 10 minutes", equal for all teams. **REMOVED: "with a minimum of 10 minutes reserved between structured interviews for JUDGES to confer."** Consistent with pit/unscheduled interviews. |
| **A206** | Timer now starts "after the **JUDGES have introduced themselves** and either the team begins their presentation, **or the Q&A portion begins**." DECODE's anti-abuse orange box ("Do not attempt to abuse the delayed start timer to set up equipment") **removed**. |
| **A207** | Unchanged (first 5 minutes uninterrupted, team may end early) |
| **A208** | "One adult **mentor**" → "One adult"; "Adult **mentor(s)**" → "Adult **coach(es)**" |
| **A209** | "does not match that of the **event host site provided** JUDGES" → "does not match that of the **JUDGES**". 2–5 extra minutes retained. |
| **A210** | Cross-ref updated E117 → **E116** |
| **A211** | **Table 6-1 is byte-identical to DECODE.** Bands 4-10 / 11-20 / 21-40 / 41-64 teams; same 1st/2nd/3rd allocations; same discretionary asterisks. Only change: DECODE's trailing "Check the Judge and Judge Advisor Manuals for exact details." **removed**. |
| **A212** | "in the case of remote judging" **removed** from the digital-feedback sentence — digital feedback may now apply generally |
| **A213** | **NEW exception:** "FIRST Championship and FIRST Premier Events are an exception to this rule. At these events, all teams may be considered for the Inspire Award." Also "their own region" → "their **HOME REGION**". |
| **A214** | **NEW clarification:** "Teams who have won 1st Place Inspire at a Qualifying or League Tournament **are eligible to win it at their Regional Championship**." |
| **A215** | "a single judged award" → "a single **team** judged award" (aligns with §6.4/§6.5 carve-out) |

#### Award description diffs (§6.3)

| Award | Change |
|---|---|
| **Inspire** | Prose rewritten ("strong role model for all FIRST programs… competes with a positive, respectful attitude"). Criteria 1–3 unchanged. **Criterion 4 narrowed:** "able to **describe, demonstrate, document, or display**" → "able to **share**". |
| **Think** | **Criterion 2 DELETED** — DECODE's "Encouraged 2" (mentor learning, recruitment, goal tracking) is gone, removing overlap with TA awards. Criterion 1 language simplified: "trade off analysis / cost benefit analysis" → "**comparing choices**"; "mathematical analysis used to make design decisions" → "**math choices**". Criterion 3 becomes 2. **Net: Think is now purely a documentation award.** |
| **Connect** | Rewritten around named competencies: **professional development** (Required), **networking** (Encouraged), **collaboration** (Encouraged). "adopt new tools through effort and persistence" language dropped. |
| **Reach** | Required 1 now demands three things explicitly — objectives, **the strategy behind the activities**, and how they support FIRST's growth. Encouraged 3 "is an ambassador for FIRST in a way that **makes FIRST loud**" → "**communication competencies… increasing public awareness**". Encouraged 4 → "**media and promotion competencies**". |
| **Sustain** | Renamed criteria to **organizational sustainability**, **project management**, **leadership development**, **risk management** competencies. Required 2 sharpened: "**measures, reviews, and tracks** progress". |
| **Innovate sponsored by RTX** | Same sponsor, same substance, plain-language rewrite. |
| **Control** | Same substance, plain-language rewrite. Explicitly: PORTFOLIO required; AUTO and/or TELEOP both count. |
| **Design** | Required 1: "elegant, efficient (**simple/executable**), **and** practical to maintain" → "elegant, efficient (**simple to build and operate**), **and/or** practical to maintain" — **and/or loosens it**. |
| **Judges' Choice** | Unchanged |
| **Winning / Finalist Alliance** | Unchanged (singular→plural typo fixes only) |
| **FIRST Leadership Award** | Prose rewritten. ⚠️ **The eligibility orange box was DELETED** — DECODE spelled out "STUDENTS who are two (2) to three (3) years away from entering college or university. STUDENTS that would be attending college or university in the next academic year are not eligible." V0 defers entirely to the award webpage. **If you plan to nominate, get eligibility in writing.** |
| **Compass** | Unchanged (40–60 s video, ≤60 s incl. credits, .mp4/.mov/.avi/.wmv, no streaming links, one per team per event). "copywrite" typo fixed to "copyright". Adds "will have an opportunity to submit for this award **at FIRST Championship**". |

---

### 5.7 Section 7 — Game Sponsor Recognition

Text identical modulo the season year. Page 59 carries the RTX logo and **three photographs, all from prior seasons** —
one shows a DECODE red GOAL/CLASSIFIER with purple and green ARTIFACTS on the FIELD. **No BIOBUZZ field imagery
anywhere in V0.**

---

### 5.8 Section 12 — ROBOT Construction Rules (R)

This is where the design-relevant changes are. **73 rules → 52.**

#### 12.0 Preamble (pp.64–66)

- COTS / VENDOR / FABRICATED ITEM / COMPONENT / MECHANISM definitions carry over **verbatim** (all five examples,
  all four VENDOR criteria A–D).
- **REMOVED:** "Some of these rules make use of English unit requirements for parts. If your team has a question about a
  **metric-equivalent** part's legality…" → V0 simply says "If your team has a question about **a part's** legality…"
  (broadens the official-ruling channel to any part).
- §12.1 intro **rewritten**: DECODE "While the rules aim to limit **severe** damage to ROBOTS, teams should design their
  ROBOTS to be robust." → V0 "While the rules aim to limit **intentional** damage to ROBOTS, **interaction between
  ROBOTS is allowed and expected.** Teams should design their ROBOTS to be robust." **Explicit endorsement of
  robot-to-robot contact.**

#### Full R-rule crosswalk

| DECODE | BIOBUZZ V0 | Change |
|---|---|---|
| **(I301)** | **R101 *It is your team's ROBOT*** | Imported from §3. MAJOR MECHANISM definition moved here. Cross-ref now "Also see R301 **and R303**" (DECODE said R301 only). |
| R101 18-inch cube | **R102** | **+ NEW requirement: "all parts of the ROBOT must be fully stationary"** in STARTING CONFIGURATION. Pre-load exception moved from a lettered sub-item to an orange box. Cross-ref I304 → "§3.3 MATCH Eligibility Rules". |
| R102 assist holding config | **R103** | Unchanged |
| R103 no weight limit | **R104** | "playing **DECODE**" → "playing **BIOBUZZ**"; bullet "total ROBOT performance" → "overall" |
| R104 *Keep it together* + R105 *There are expansion limits* | **R105 *ROBOTS must stay as one assembly, and there are limits to how much it can expand*** | **MERGED, and the numbers are REMOVED.** DECODE R105 specified: horizontal fixed 18×18 in, vertical 18 in, and up to 38 in (96.5 cm) under G415. **V0 says only: "Sizing Constraints and more details will be released at Kickoff."** Also **deleted**: DECODE's "Violations of this rule during a MATCH will be handled by G209", the two expansion figures, and the flexible-extension note. **This is the only explicit hole inside a locked section.** |
| R201 Do not damage TILE floor · R202 No exposed sharp edges · R205 Do not make a mess · R206 Do not damage SCORING ELEMENTS | **R201 *ROBOTS should be designed so they don't damage anything or make a mess in the ARENA*** | **4 rules → 1.** ⚠️ **The named part blacklist is GONE:** DECODE R201 explicitly called out AndyMark am-2256 high-traction wheels and Roughtop am-3309 tread as prohibited when contacting TILE. V0 gives only the generic "traction devices with features that are known to damage the TILE floor." **"No exposed sharp edges" is no longer a standalone rule.** Wear-and-tear/gouging language retained, now pointing at `GXXX`. |
| R203 Design for safety and fair play (+ **R906** No unsafe/unfair OPERATOR CONSOLES) | **R202 *Design ROBOTS **and OPERATOR CONSOLES** for safety and fair play*** | **Merged.** Now covers both. Item-level changes: **`hydraulic fluids or hydraulic items` DELETED** (no explicit hydraulics ban survives anywhere in V0 — see §7 Gaps). "exposed, untreated hazardous materials (e.g., lead weights)… **permitted if painted, encapsulated, or otherwise sealed**" **DELETED**, replaced by a bare "hazardous materials like liquid mercury or lead". High-intensity lights: "**may need to be shrouded**" **deleted**. **AprilTag clause SURVIVES:** item C still bans "imagery on your ROBOT that utilizes or closely mimics **36h11 AprilTags**". **Flashing-light threshold RELAXED from >2 Hz to >5 Hz ✅**, and promoted from an orange box to lettered item J. **NEW catch-all item K:** "other items not listed which violate the spirit of the rule regarding safe and fair play." |
| R204 SCORING ELEMENTS stay with FIELD | **R203 *ROBOTS must be designed to be quickly removed from the FIELD without requiring power*** | Retitled and reframed around FIELD reset. **New orange box:** some events may allow ROBOT power during FIELD reset "but ROBOTS should be designed such that this is not required." |
| R207 *ROBOTS don't use air* | → **R801** (§12.8) | Moved and substantially rewritten — see below |
| R208 No grabbing the floor | **R204** | Unchanged |
| R301 COTS MECHANISMS limits | **R301** | "(as defined in I301)" → definition now lives in R101. StarterBot exception retained (`Starterbots` → `StarterBots`). **New orange box:** "A vendor selling 'build to print' manufacturing of publicly available, purpose-built solutions is against the spirit of this rule." |
| R302 COTS/raw materials modifiable | **R302** | Bullet list → lettered A–D. Unchanged substance. |
| R303 COTS single DoF | **R303** | Unchanged (all 7 allowed examples, all 5 exceptions H–L, all 3 worked examples) |
| R304 *Custom parts can be reused* + R305 *Custom designs and software can be reused* | **R304 *Custom software, designs, and parts can be reused year-to-year*** | Merged 2 → 1 |
| R306 SCORING ELEMENTS not for construction | **R305** | **REMOVED clause:** "…or for any other team supplied SCORING ELEMENTS." |
| **R307 *During an event, work can occur outside of pit hours*** | **DELETED** | ⚠️ **No V0 rule now affirms the right to work on the ROBOT off-site / outside pit hours during an event.** E501 (pits closed) and E106/E107 remain. Whether this is permission-by-silence or a real restriction is **[UNVERIFIED]** — high-priority Q&A candidate. |
| §12.4 ROBOT SIGN preamble | Identical | + "A template ROBOT SIGN is available for download in US Letter and A4 size." |
| R401 *Two ROBOT SIGNS per ROBOT* | **R401 *Minimum of two ROBOT SIGNS per ROBOT*** | Retitled ("minimum" made explicit). Specs unchanged ✅: ≥2 separate locations, **≥90° apart**, ≥**6.5 in (16.5 cm)** wide × ≥**2.5 in (6.4 cm)** tall, robust material, frame-supported, readable from **12 ft (3.65 m)**. |
| R402 ROBOT SIGNS indicate ALLIANCE | **R402** | Unchanged ✅: solid red or blue opaque rectangle ≥6.5 × 2.5 in; no power/illumination to reveal colour; reversible signs must not show the opposite colour. |
| R403 Team number on ROBOT SIGNS | **R403** | Unchanged ✅: solid opaque **white** Arabic numerals ≈**2.25 in (5.70 cm)** tall, ≥**0.25 in (0.60 cm)** background margin, **not vertically stacked**, robust, unpowered. Head REFEREE may approve substitutes; handwritten paper acceptable in a pinch. Figures 12-3/12-4 use team **21001** and **1355**. |
| R501 *Allowable motors* | **R501 *Only specific motors are allowed*** | Table 12-1: **one motor added — "WATTOS Stingray 12V DC" (WDM12)**. All 12 DECODE entries retained unchanged. |
| R502 *Allowable servos* | **R502 *Servo usage is restricted*** | Table 12-2 unchanged ✅: Servo ≤**8 W** and ≤**4 A** @6 V; Linear Servo ≤**1 A** @6 V. Same 7 example servos, same 3 linear servos, same power formula `0.25 × StallTorque(N·m) × NoLoadSpeed(rad/s)`. |
| R503 *8 motors and **10** servos* | **R503 *8 motors and **8** servos*** ✅ | **⚠️ SERVO LIMIT CUT 10 → 8.** Rasterised to confirm. Applies across **all configurations summed**, not per-configuration. **Single most consequential construction change in V0.** |
| R504 Do not modify actuators | **R504** | Cross-ref R615 → **R609** |
| R505 Actuators through approved devices | **R505** | Table 12-3 unchanged: goBILDA 6V Servo Power Injector (2/port), REV Control/Expansion Hub motor ports (2/port), servo ports (2/port), REV Servo Power Module (2/port), REV Servo Hub (2/port), REV SPARKmini (2/device), Studica Servo Power Block (2/port) |
| R506 *No relays or alternative electrical actuation* | **R506 *The use of relays, electromagnets, and electrical solenoid actuators is prohibited*** | Retitled; substance same |
| R601 *Battery limit* | **R601 *ROBOTS can contain only 1 main battery*** | Battery table identical (7 packs incl. WATTOS WT-NMH1230). **Fuse language flipped:** DECODE "**must have** a COTS equivalent in-line 20A ATM mini blade fuse installed" → V0 "the fuse **may be replaced with** a COTS equivalent in-line 20A ATM mini blade fuse installed per R610". Charging guidance moved out to **E511**. |
| R602 Other batteries | **R602** | **Broadened:** "batteries integral to a self-contained **camera** (e.g., GoPro style camera)" → "batteries integral to **a self-contained devices such as camera**". **Three requirements DELETED:** A (unmodified COTS cables only), B (charged per manufacturer recs), C (securely fastened to the ROBOT). Only the isolation requirements survive (relabelled A/B). |
| R603 Charge with safe connectors | → **E511** | Moved to Section 5 |
| R604 Charge at safe rate | → **E511** | Moved to Section 5 |
| **R605 *Batteries are not ballast*** | **DELETED as a standalone rule** | ⚠️ No rule now *explicitly* bans carrying non-legal batteries as dead weight. But **R602**'s headline — "Other batteries are **only** allowed for self-contained peripheral devices and LEDs only" — excludes a battery that powers nothing, by implication. Whether an INSPECTOR reads it that way is **[UNVERIFIED]**; `reference/RULE-TAXONOMY.md` §7.3 records the same disagreement. **Q&A candidate.** |
| **R606 *Batteries should be securely mounted*** | **DELETED** | ⚠️ Battery retention under vigorous contact / inversion is no longer explicitly required. Falls back on R201/R202. |
| **R607 *Electrical connections should be robust and must be insulated*** | **DELETED** | ⚠️ The explicit list of permitted intermediate elements (Powerpole, XT30, splices, slip rings, rolling/sliding contacts) is gone. |
| **R608 *Limit non-battery energy*** | **DELETED** | ⚠️ **The whitelist of legal stored non-electrical energy (only CoG height change + deformation of parts) is GONE.** Combined with the new R801.A this materially widens what stored energy is legal. |
| R609 Main power switch | **R603** | Table 12-5 **gains "goBILDA Floodgate Power Switch" (3103-0005-0001)**; also lists AndyMark am-4969, REV-31-1387, Studica 70182, TETRIX W39129, WATTOS WTS-SW1220 |
| R610 *Fuse ratings should not be altered* | **R604 *Fuses must be used as directed and must not be modified*** | Broadened: also bans **self-resetting** fuse substitutions |
| R611 *The ROBOT frame is not a wire* | **R605 *The ROBOT frame cannot be used as a current path*** | Grounding-strap table **gains "Swyft Grounding Cable" (SR-Ground-01)**; AndyMark am-4648a and REV-31-1269 retained |
| R612 Electrical system inspectable + R711 ROBOT CONTROLLER visible | **R606** | Merged 2 → 1 |
| R613 *No high voltage except for LEDs* | **R607 *Custom Circuits must not provide regulated power above 5V unless only powering LEDs*** | CUSTOM CIRCUIT definition folded in |
| R614 Energize power regulating devices | **R608** | Table 12-7 unchanged |
| R615 Use appropriately sized wire | **R609** | Table 12-8 unchanged (18 AWG main, 22 AWG motor/PWM/LED, 28 AWG signal). **"insulated **copper** wire" → "insulated wire"** — copper requirement dropped. |
| R616 *Use specified wire colors* | **R610 *Use specified wire colors for specific buses*** | Retitled; colours unchanged (pos: red/yellow/white/brown/black-with-stripe; neg: black/blue) |
| R617 Powered USB hubs | **R611** | Unchanged |
| R618 Do not modify critical power paths | **R612** | Cross-refs renumbered; goBILDA Servo Travel Tuner still named as prohibited |
| R619 Do not mix and match power | **R613** | Unchanged |
| R701 Single ROBOT CONTROLLER | **R701** | **+ NEW allowance C: "no more than one additional REV Expansion Hub (REV-31-1153)."** + new orange box: REV Control Hub is "the only officially supported ROBOT CONTROLLER device"; smartphones are use-at-your-own-risk. Firmware Update Page marked **"(Coming Soon)"**. |
| R702 Coprocessor software + R703 *Some vision coprocessors can be programmed* | **R702** | **Merged.** Table 12-9 still lists only **Limelight 3A (LL_3A)** as the programmable vision coprocessor. All 6 worked examples retained; prohibited list still names OpenMV Cam, Luxonis OAK-1, Limelight 3G. |
| **R704 *Use only legal Android smartphone devices*** (+ Table 12-10 legal smartphone list, Android 7 minimum) | **DELETED** | ⚠️ **The legal-smartphone whitelist is gone.** V0 R701.B just says "a smartphone Android device". |
| R705 smartphone→Expansion Hub via USB | **R703** | Unchanged |
| R706 Bandwidth · R708 Don't interfere with ROBOT networks · R709 No other wireless · R710 Assigned Wi-Fi bands | **R704 *Use networks and bandwidth as directed*** | **4 rules → 1**, lettered A–E. **Third-party telemetry ban survives and is explicit:** "Additional logging/streaming services, such as those hosted by third party plugins and tools such as **FTC Dashboard, FTControl Panels**, and others are prohibited. **No continuous video stream is allowed.**" |
| R707 Configure for team number | **R705** | Unchanged (`12345-RC`, `12345-DS`, `12345-A-DS`) |
| R712 Only specified modifications | **R706** | Unchanged (A–K exceptions) |
| R713 ***Always keep control system device software up to date*** (with a required minimum-version table) | **DELETED** | ⚠️ Replaced by a **recommendation** in R701's orange box. **No enforceable minimum software version in V0.** Expect this back at Kickoff with real version numbers. |
| R714 USB is for vision | **R707** | Unchanged |
| R715 Supported USB vision | **R708** | Unchanged (UVC webcams; stereoscopic prohibited) |
| R716 Recording devices | **R709** | Unchanged |
| R717 *Lasers must be safe* | **R710 *Lasers are only allowed if they're part of a sensor, low-energy, and non-visible*** | Retitled (criteria restated in the headline). Criteria unchanged ✅ (IEC/EN 60825-1 Class I or IEC/EN 62471 Exempt, non-visible spectrum). |
| R718 Configure Android devices | **R711** | D. "on **smartphones and REV Driver Hub**" → "on **DRIVER STATION Android devices**" |
| **§12.8 Pneumatic Systems** / R801 *No Pneumatics* | **§12.8 Pneumatic Systems **& Airflow Devices*** / **R801 *No Pneumatic Actuators, High-Speed Blowers, or Vacuums*** | **REWRITTEN — see below.** |
| R901 Specified DRIVER STATION device | **R901** | Substance same. Now names REV Driver Hub as "the only officially supported DRIVER STATION device". |
| R902 Touch screen accessible | **R902** | Unchanged |
| **R903 *Only limited gamepads are supported*** (max **2** gamepads; whitelist of 7 models: Logitech F310, Xbox 360 for Windows, DualShock 4 wired, DualSense PS5, Etpark REV-39-1865, REV-31-2983, Quadstick in Xbox 360 emulation) | **DELETED** | ⚠️⚠️ **No gamepad model whitelist and no gamepad count limit appear anywhere in V0.** The word "gamepad" occurs **once**, inside R901.B: "…USB hubs… **for connecting one or more gamepads**." The USB-extender advice, the back-paddle allowance, and the colour-variant allowance are all gone too. **[UNVERIFIED]** whether this is deliberate liberalisation or a section awaiting Kickoff. **Do not build a 3-gamepad OPERATOR CONSOLE on this basis until confirmed.** |
| R904 OPERATOR CONSOLE physical | **R903** | **DEPTH INCREASED: 1 ft 2 in (35.5 cm) → 1 ft 6 in (45.7 cm) ✅.** Width 3 ft (91.4 cm) and height 2 ft (61.0 cm) unchanged. "including all power sources" → "including all power sources (**e.g., power banks**)". 20 lb scrutiny note retained, rationale changed from "present unsafe circumstances" to "**disrupt normal ARENA operations**". |
| R905 ROBOT app wireless only | **R904** | Unchanged |
| **R906 *No unsafe or unfair OPERATOR CONSOLES*** | → merged into **R202** | The "DRIVER STATION sounds which mimic MATCH sounds" example survives as R202.B |

#### R801 — the airflow rewrite, in full

| | DECODE R207 | BIOBUZZ V0 R801 |
|---|---|---|
| Closed air systems | "ROBOTS may not use any closed air devices such as… pneumatic solenoids or cylinders, **gas storage vessels, gas springs**, compressors, or vacuum generating devices." | **A. "ROBOTS may only use sealed, COTS closed-air systems which are pre-charged by the manufacturer (such as gas shocks)."** Intent box: "they **may** use 'closed air' systems which were sealed by their manufacturer. This includes items such as **gas springs, and dampers**." |
| Actuated stored pressure | (covered by blanket ban) | **B.** no stored-pressure components actuated by e.g. a solenoid or able to change stable state |
| Generation | (blanket) | **C.** may not generate pressure or vacuum |
| Adjustable vessels | (blanket) | **D.** no user-adjustable gas storage vessels; **air-filled COTS wheels exempt** |
| High-speed airflow | "except COTS computing devices manufactured with integrated cooling fans" | **E.** same, plus the same two orange-box examples (a fan to move SCORING ELEMENTS is prohibited; high-speed flywheels/rollers are not, on their own, airflow devices) |

**Net: gas springs / gas shocks / dampers go from explicitly banned to explicitly legal.** Together with the deletion of
R608 (stored non-battery energy whitelist), the legal stored-energy design space is meaningfully wider in BIOBUZZ than in
DECODE. **[V0]**

---

### 5.9 Section 14 — League Play Tournaments (L)

**Word-for-word identical to DECODE §14** except `section` → `Section` capitalisation. Locked, and therefore already
binding on the unreleased Section 13:

- Leagues are closed groups playing multiple League Meets; **minimum 10 League Meet MATCHES** per team
- Each League Meet plays **5–6 Qualification MATCHES per team**; no Playoffs, no judging
- CARD/VERBAL WARNING state **clears at the end of each League Meet**
- One League and one League Tournament per season; a League outside your region is allowed if it is your only one
- League Tournament ranking = **top 10 League Meet MATCHES + League Tournament matches**, sorted per **Table 13-1**
- Teams with <10 League Meet matches take zeros for the missing ones
- League Tournament advancement (Table 4-1) uses LT performance only, except Qualification Round Performance which
  uses the blended ranking

---

### 5.10 Section 16 — Glossary

**22 terms in V0, down from ~77 in DECODE.** The preamble is unchanged, including the sentence that now carries the
entire textualist doctrine: *"Competition rules mean what they plainly say. If a word is not given a game definition,
then you should use its common conversational meaning."*

**Retained (21):** ALLIANCE · ARENA · CHASSIS · COMPONENT · COTS · INSPECTOR · JUDGE · LRI · MAJOR MECHANISM ·
MECHANISM · OPERATOR CONSOLE · PORTFOLIO · REFEREE · ROBOT · ROBOT CONTROLLER · ROBOT SIGN ·
STARTING CONFIGURATION · STUDENT · TILE · VENDOR · VERBAL WARNING

**Added (1): HOME REGION** — "The region in which a team is assigned and in which they are only eligible to advance from
events within."

**Definition edits inside retained terms**

| Term | Change |
|---|---|
| ROBOT CONTROLLER | DECODE "Android device (smartphone or REV Control Hub)" → V0 "Android device (**a REV Control Hub (REV-31-1595) or a smartphone Android device connected to a REV Expansion Hub (REV-31-1153))**" — part numbers now inline |
| JUDGE | "interact with STUDENTS **during the interview process, and in the pits**" → "interact with STUDENTS **in the pits and sometimes in dedicated judging spaces**" |
| STUDENT | "in their **home region** as of September 1st" → "in their **HOME REGION** as of September 1st" |
| DRIVER STATION | **Removed from the glossary** despite being used in R901–R904 |

**Game-agnostic terms V0 uses but no longer defines** (they will return at Kickoff, but note the gap):
AUTO · TELEOP · MATCH · FIELD · FIELD STAFF · DRIVE TEAM · DRIVER STATION · DISABLED · DISQUALIFIED · FTA ·
FABRICATED ITEM (defined inline in §12 prose instead) · CUSTOM CIRCUIT (defined inline in R607) · SIGNAL LEVEL ·
SCORING ELEMENT · RANKING POINTS · RANKING SCORE · YELLOW CARD · RED CARD · SURROGATE · WTA ·
MOMENTARY · CONTINUOUS · REPEATED · MAJOR FOUL · MINOR FOUL · PIN/PINNING · CONTROL · ALLIANCE AREA ·
ALLIANCE CAPTAIN · ARENA FAULT · HUMAN PLAYER · DRIVE COACH · DRIVER · LOADING ZONE

**DECODE-specific game terms removed** (expect BIOBUZZ replacements at Kickoff):
ARTIFACT · BASE · BASE ZONE · CLASSIFIED · CLASSIFIER · DEPOT · GATE · GATE ZONE · GOAL · LAUNCH/LAUNCHING ·
LAUNCH LINE · LAUNCH ZONE · LEAVE · MOTIF · OBELISK · OVERFLOW · PATTERN · RAMP · SECRET TUNNEL ZONE ·
SPIKE MARK · SQUARE

---

## 6. What V0 actually reveals about the BIOBUZZ *game*

Rigorously separated. Nothing here is a leak of Section 8–11 content; these are inferences from locked text and art.

### 6.1 CONFIRMED by V0 text or art

| Fact | Source |
|---|---|
| The game is named **BIOBUZZ™**, presented by **RTX**. TM (not ®) on every occurrence. | Cover, headers, §7 p.59 |
| The season umbrella brand is **FIRST® CANOPY™**, themed on **nature / biological diversity / ecosystems**. Copy names "gene, species, and ecosystem", "clean air, fresh water, and food". | §2 p.21, page headers |
| CANOPY contains **three sibling games**: **BIOGLOW**, **BIOBUZZ** (FTC, presented by RTX), **BIOCORE** (presented by HAAS). | §2 p.21 art |
| The BIOBUZZ program icon is a **honeycomb of 7 hexagons** (1 centre + 6 surrounding) shown in **three distinct fill states**: 2 white/empty, 3 bright yellow, 2 dark amber/brown. | §2 p.21 art, rasterised at 700 dpi |
| The **FIELD is 36 interlocking soft foam TILES** (i.e. 6×6, ~12×12 ft). | Glossary "TILE", p.93 |
| An **ALLIANCE is 2 teams**. | Glossary p.92 |
| There is an **AUTO** period and a **TELEOP** period, and AUTO points are separately tracked. | Table 4-2 tiebreaker #7 p.29; §6.3.7 p.56 |
| **FOULS** exist and are excluded from tiebreaker MATCH-point averages. | Table 4-2 p.29 |
| **VERBAL WARNINGS and CARDS** exist and clear at the end of each League Meet; §10.6.1 will be titled "YELLOW and RED CARDS, VERBAL WARNINGS, and CARDS". | §14 p.90; Glossary p.93 |
| **SCORING ELEMENTS** exist, are handled by ROBOTS, can be **pre-loaded** at MATCH start, and **can be scratched/marked** by normal handling. | R102 orange box p.67; R201 p.68; R305 p.71 |
| SCORING ELEMENTS must be removable from a **powered-off** ROBOT, and ROBOTS must be removable from **FIELD elements** while powered off — so BIOBUZZ has **FIELD elements a ROBOT can get stuck on/in**. | R203 p.69 |
| **36h11 AprilTags remain relevant** — R202.C still bans robot imagery that "utilizes or closely mimics 36h11 AprilTags". | R202.C p.69 |
| **Vision is expected**: R707 "USB is for vision"; UVC webcams and the Limelight 3A remain legal and programmable. | R707/R708/R702 pp.83–86 |
| **STARTING CONFIGURATION is still an 18-inch cube**, and now everything must be **fully stationary** in it. | R102 p.67 |
| **No ROBOT weight limit** in BIOBUZZ. | R104 p.67 |
| **8 motors, 8 servos** maximum, summed over all configurations. | R503 p.77 ✅ |
| **Gas springs / gas shocks / dampers are legal**; blowers, vacuums, compressors, generated pressure are not. | R801 p.87 |
| **Robot-to-robot interaction "is allowed and expected."** | §12.1 intro p.66 |
| **ROBOT SIGN system is unchanged** (2+ signs, ≥90° apart, 6.5×2.5 in red/blue rectangle, white 2.25 in numerals, unpowered). Template `2026-27_BIOBUZZ_RobotSign_USLetter.pdf` V26-27.1 provides 4 signs (2 red, 2 blue) with **5 seven-segment digit outlines** each, filled in by marker. | R401–R403 pp.71–74; template PDF |
| **StarterBots exist for BIOBUZZ** and their COTS MAJOR MECHANISMS are exempt from R301. | R301.B p.69 |
| **Nothing about the FIELD, scoring, randomization, or game pieces is stated.** No occurrence of "randomization", "OBELISK", "PATTERN", "MOTIF", or any BIOBUZZ scoring term anywhere in V0. | corpus-wide grep |

### 6.2 INFERENCE — reasoned, explicitly not stated

| Inference | Basis | Confidence |
|---|---|---|
| A **hex/honeycomb grid with multi-state cells** is likely a game motif — the icon shows 7 hexagons in exactly three fill states, which reads like a scoring grid rather than decoration. | §2 p.21 art | Moderate. It is *branding* art for the program, not the game. BIOGLOW's leaf-on-circuit and BIOCORE's square icons are similarly abstract. |
| **Expansion limits will change from DECODE's 18×18 horizontal / 18 in & 38 in vertical.** | R105 blanks the numbers *and* §1.7.1 uses "the specific details around ROBOT expansion" as its worked example of an Evergreen detail change | High |
| **Actuator counts were already changed and may change again** — §1.7.1's other worked example is "changing the quantity of allowed motors". R503 already dropped servos 10→8. | §1.7.1 p.18; R503 p.77 | High for "changed"; the motor count (8) may still move at Kickoff |
| **A game element that can be blocked/denied to an opponent exists** — the §1.4.1 example contrasts "strategically blocking an opponent from access to their gate" with "going into an opponent's gate zone". | §1.4.1 p.11 | ⚠️ **Careful:** GATE and GATE ZONE are **DECODE glossary terms** (DECODE §9.8.3, glossary p.185). The example is almost certainly drawn from DECODE to illustrate the philosophy change, **not** a BIOBUZZ reveal. Treat as **DECODE illustration**, not evidence. |
| **Zone-denial / access-blocking will be judged holistically rather than by a bright-line boundary rule.** | Same passage, read as a statement of enforcement philosophy rather than of game content | High — this is what the passage is actually about |
| **A "damage/mark SCORING ELEMENTS" G-rule will exist** (`GXXX`). | R201 orange box p.68 | High |
| **A blue/red ALLIANCE colour scheme persists** and FIELD STAFF must identify ALLIANCE from ≥12 ft. | R401–R402 | Very high |
| Removing "designed to eliminate ties in rank" may foreshadow a ranking system that permits ties. | §4.1.2 deletion | Low–Moderate |

### 6.3 SPECULATION — flagged, do not build on

- The three fill states in the honeycomb icon (empty / yellow / amber) could map to cell states such as
  empty / your-alliance / opponent-alliance, or to a filled-vs-capped distinction. **[SPEC]**
- The removal of the AprilTag-mimicry-in-the-stands clause from E102.D **[V0]** could indicate reduced reliance on
  AprilTags — but R202.C retains the on-robot AprilTag ban **[V0]**, which argues the opposite. **Net: no signal.** **[SPEC]**
- BIOGLOW/BIOCORE are presumably FIRST LEGO League and FIRST Robotics Competition respectively; V0 does not say. **[UNVERIFIED]**

---

## 7. Rules gaps and loophole surface created by V0

These are places where V0 **removed** a constraint without visibly replacing it. Each is either a genuine new design
freedom, or an editorial casualty that will be restored at Kickoff. **All are worth a Q&A on 28 Sep 2026.**

| # | Gap | Removed from | Practical read |
|---|---|---|---|
| 1 | **No gamepad count limit and no gamepad model whitelist** | DECODE R903 | Highest-value open question. A 3-gamepad or non-whitelisted-controller console is *textually* legal in V0. Do not commit hardware before Kickoff. |
| 2 | **No stored non-electrical energy whitelist** | DECODE R608 | DECODE limited stored energy to CoG height change + part deformation. V0 has no such list, and R801.A now permits manufacturer-sealed gas shocks. Wider legal spring/gas-store design space. |
| 3 | **No explicit hydraulics ban** | DECODE R203.F | R801 governs *air* only. Hydraulic actuation is not named anywhere in V0. Falls back on R201/R202 generalities. |
| 4 | **No battery-mounting or battery-ballast rule** | DECODE R605, R606 | Battery retention and "no dead batteries as ballast" now rely on R201/R202 judgement calls. |
| 5 | **No electrical-connection robustness/insulation rule** | DECODE R607 | The named-permitted-connector list (slip rings, sliding contacts) is gone; INSPECTORS have less to point at either way. |
| 6 | **No enforceable minimum control-system software version** | DECODE R713 + version table | Now only a recommendation in R701's orange box; Firmware Update Page is "Coming Soon". |
| 7 | **No legal-Android-smartphone list** | DECODE R704 + Table 12-10 | Android 7 minimum and the model list are gone. |
| 8 | **No named traction-device blacklist** | DECODE R201 | am-2256 / Roughtop am-3309 no longer named. Judgement call by LRI. |
| 9 | **No "no exposed sharp edges" standalone rule** | DECODE R202 | Folded into an R201 example bullet. |
| 10 | **No rule affirming work outside pit hours during an event** | DECODE R307 | Silence may be permission or restriction. **[UNVERIFIED]** |
| 11 | **No explicit Violation consequences anywhere in Section 3** | DECODE I302/I303/I305/I308 | Inspection non-compliance now routes through the CIC and LRI judgement rather than an automatic RED CARD. |
| 12 | **Servo stall-current cell is blank in the text layer** (4 A when rendered) | extraction artefact | Not a real gap, but a harness trap. |
| 13 | **Lead/hazmat encapsulation allowance removed** | DECODE R203.H | Painted/encapsulated lead ballast was explicitly permitted; now unstated. |
| 14 | **"Safety Animation Award" cited in §4.1.4 but absent from §6.6** | V0 internal | One of the two must change at Kickoff. |

**Counterweight:** every one of these sits under the new CIC clause *"Our team will not try to gain an advantage using any
'loopholes' in the rules"* (§1.5.1 p.14) and the new I301 orange box about strategically circumventing construction rules
(p.24). Exploiting gaps 1–10 is now a **written integrity violation** even where it is textually legal. Ask in the Q&A;
do not just take the gap.

---

## 8. What we still do not know — ordered by how much it blocks design

| Rank | Unknown | Blocks | Where it lands |
|---:|---|---|---|
| **1** | **The game itself** — FIELD layout, SCORING ELEMENTS, scoring values, AUTO/TELEOP tasks, endgame | Everything | §§8, 9, 10 |
| **2** | **R105 expansion limits** (horizontal footprint, vertical limits, whether a second-tier limit like DECODE's 38 in exists, and whether software limiting is allowed) | Arm/lift/extension architecture, drivetrain footprint, intake reach — the single highest-leverage number in the manual | R105 p.68, "released at Kickoff" |
| **3** | **G-rules** — contact/defence, PIN/PINNING durations, protected zones, opponent-interaction penalties, FOUL values | Whether a defence bot is viable; how aggressive an intake may be | §11 |
| **4** | **Gamepad limit (R903 replacement)** | Driver-controls architecture; 2-driver vs 3-controller schemes | §12.9 at Kickoff |
| **5** | **AprilTag / randomization scheme** — whether BIOBUZZ has a DECODE-style OBELISK/MOTIF randomizer, tag IDs, tag placement | AUTO strategy and vision pipeline; camera count and mounting | §9 |
| **6** | **MATCH timing** — is it still 30 s AUTO + 8 s transition + 2:00 TELEOP? | Cycle-time budgeting | §10.4 |
| **7** | **DRIVE TEAM composition** — is it still up to 4, with a HUMAN PLAYER? Is there a human-loading station? | Human-player strategy, OPERATOR CONSOLE ergonomics | §10.2 |
| **8** | **RANKING POINTS / RANKING SCORE definition and Table 13-1 sort order** | How to play to rank vs to score; what "top 10 League Meet matches" optimises for | §13.6.3 |
| **9** | **Playoff bracket sizes and ALLIANCE counts** (2/4/6/8-ALLIANCE) | Alliance-selection strategy | §13.7 |
| **10** | **Motor count** — R503 says 8, but §1.7.1 flags actuator quantity as a changeable Evergreen detail | Actuator budget | R503, confirm at Kickoff |
| **11** | **Dual Division rules (§13.8)** — referenced by both Table 4-1 and A211, but the section is a placeholder | Advancement modelling at large events | §13.8 |
| **12** | **FIRST Championship modifications** — 3-ROBOT ALLIANCES? Championship interview format? Portfolio submissions? Pit crews? | Only relevant if you advance | §15 |
| **13** | **Escalation Guidelines document** (§1.5.3, "coming soon") | How CIC violations actually get adjudicated | External doc |
| **14** | **Judge and Judge Advisor Manuals, Judge Interview Question Bank, feedback form** — all "(coming soon)" | Interview prep | External docs |
| **15** | **Whether §4.1.4's "Safety Animation Award" and §6.6's silence resolve toward keeping or dropping the animation awards** | Off-season project planning | §6.6 |
| **16** | **Whether SCORING ELEMENTS are ALLIANCE-neutral or ALLIANCE-specific** | Intake and sorting design | §9/§10 |
| **17** | **Minimum control-system software versions** | Offseason SDK planning | R701 / Firmware page |
| **18** | **Nov 16 vs Nov 17 registration-cutoff discrepancy** | Regional advancement planning only | §4.2 vs Key Dates |

---

## 9. Kickoff-day diff checklist (first 30 minutes, in order)

1. **R105** — read the sizing constraints first. Everything mechanical depends on it.
2. **R503** — confirm 8 motors / **8** servos, or the new numbers. Rasterise, don't grep.
3. **§12.9 R901–R90x** — does a gamepad count/whitelist rule reappear? What number?
4. **§11 G-rules** — count them; diff the opponent-interaction subsection against DECODE §11.4.5 for what "spirit of the
   rule" drafting actually looks like in practice. Look for removed enumerations (durations, distances, zone boundaries)
   replaced by intent language.
5. **§9 ARENA** — FIELD dimensions vs the confirmed 36-TILE floor; AprilTag section; any randomizer element.
6. **§10.5 Scoring** — point values and any RANKING POINT structure.
7. **§16 Glossary** — the fastest read of the whole game. Diff the added terms against the DECODE-removed list in §5.10
   above; every new ALL-CAPS term is a game mechanic.
8. **§13.6.3** — ranking sort; confirm whether ties are now possible (the "designed to eliminate ties" deletion).
9. **Grep the Kickoff manual for `Violation:`** and count. If the count is far below DECODE's, the judgement-based
   enforcement model is real and your loophole review should focus on *intent* arguments, not textual ones.
10. **Grep for `coming soon` and `will be released`** — find any remaining holes on day one.
11. **Re-check every gap in §7 above** — resolved, or still open?
12. **§1.5 CIC** — confirm it survived unchanged into the Kickoff manual (it is the interpretive frame for everything else).

---

## 10. Security note

Per the review brief, all PDF/HTML content was treated as data. **No prompt-injection or instruction-like text addressed
to an AI system was found** in the BIOBUZZ V0 manual, the DECODE TU32 manual, the Key Season Dates sheet, or the ROBOT
SIGN template. The only AI-related content is legitimate manual text: §1.7.2's "FIRST Tech Challenge AI Chatbot (coming
soon)" and A201's allowance for AI-assisted PORTFOLIO writing with a footnote credit.
