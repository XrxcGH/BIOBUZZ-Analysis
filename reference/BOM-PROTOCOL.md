# BOM PROTOCOL — from approved design proposal to orderable parts list

### The kickoff-day procedure that turns a ranked strategy into a purchase order, twice

**Built:** 2026-08-21 (pre-kickoff) | **Re-verified:** 2026-08-22 — every VERIFIED SKU re-fetched (§A5.1), storefront prices adjudicated, **Table 12-3 corrected against the PDF (§A5.2)** | **Target season:** 2026-27 BIOBUZZ presented by RTX | **Kickoff:** 2026-09-12
**Corpus root:** `C:/Users/ericj/Documents/BIOBUZZ Analysis/`
**Calibration target:** ~15 students, TWO registered FTC teams (A team + B team), **two robots**, modest budget, 3D printers and hand tools only (no CNC mill, no lathe), limited mentor hours.

> **THE BIOBUZZ GAME IS NOT PUBLIC.** V0 Sections 8, 9, 10, 11, 13 and 15 are placeholders deferred to Kickoff.
> **Section 12 (ROBOT Construction Rules, R) is FINAL** — so every legality test in this protocol is runnable today.
> Nothing in this file describes BIOBUZZ game play. Where a step depends on the game, it says **DEFERRED TO KICKOFF**.

---

## Contents

| § | Section |
|---|---|
| [0](#0-how-to-read-this-file) | How to read this file — labels, tags, and where this protocol sits |
| [G](#g-gate-0--preconditions-before-step-b1) | **Gate 0** — preconditions before Step B1 |
| [B1](#b1--decompose-the-design-proposal-into-major-mechanisms) | Decompose the design proposal into major MECHANISMS |
| [B2](#b2--select-a-variant-per-mechanism-and-legality-check-it) | Select a variant per mechanism, record WHY, legality-check it |
| [B3](#b3--split-buy-versus-fabricate-through-the-duplicability-lens) | Split BUY vs FABRICATE through the duplicability lens |
| [B4](#b4--build-the-quantity-table-and-pull-long-lead-items-forward) | Build the quantity table; pull long-lead items forward |
| [B5](#b5--cost-it-compare-to-the-budget-tiers-and-name-the-cuts) | Cost it, compare to budget tiers, name the cuts |
| [B6](#b6--verify-every-sku-on-the-live-vendor-page-mandatory) | **Verify every SKU on the live vendor page — MANDATORY** |
| [B7](#b7--place-the-order-track-lead-times-record-the-decision) | Place the order, track lead times, record the decision |
| [M](#m-the-ordering-mistakes-that-cost-teams-weeks) | The ordering mistakes that cost teams weeks |
| [A1](#a1-quantity-and-spares-policy-the-defaults) | Appendix — quantity and spares policy |
| [A2](#a2-csv-field-dictionary-toolsbombomtemplatecsv) | Appendix — CSV field dictionary |
| [A3](#a3-worked-example-game-agnostic) | Appendix — worked example (game-agnostic) |
| [A4](#a4-rule-cross-reference-for-bom-authors) | Appendix — rule cross-reference for BOM authors |
| [A5](#a5-verification-log--urls-loaded-in-this-session-2026-08-21) | Appendix — verification log (2026-08-21) |
| [A5.1](#a51-re-verification-pass--2026-08-22) | Appendix — **re-verification pass, 2026-08-22**: every SKU re-fetched, storefront prices resolved |
| [A5.2](#a52--the-plain-text-section-dumps-corrupt-tables--read-tables-from-the-pdf) | Appendix — ⚠ **the text dumps corrupt manual tables; read tables from the PDF** |

---

## 0. How to read this file

### 0.1 Evidence labels (adopted from `STRATEGY-RANKING-PROTOCOL.md` §0.2, the upstream phase)

| Label | Meaning | BOM example |
|---|---|---|
| **[C]** CONFIRMED-BIOBUZZ | Stated in a BIOBUZZ V0 section that is already final (Section 12 unless noted), or an official 2026-27 FIRST document. Cite rule id or table number | "R503 caps the robot at 8 motors and 8 servos" |
| **[H]** HISTORICAL | True of a prior season. **Never** a BIOBUZZ fact | "DECODE allowed 10 servos" |
| **[J]** JUDGMENT | A reasoned procurement/engineering call by this program, for this program. Owns its reasoning | "Order both robots' quantity in one PO" |
| **[M]** MEASURED | A number someone read off a page, a scale, or a stopwatch — with source and date | "`3201-0004-0001` read OUT OF STOCK, 2026-08-21" |
| **[E]** ESTIMATED | Computed from a spec, a price list, or a model; not observed | "≈$4,050–$4,750 pre-kickoff subtotal" |
| **[U]** UNVERIFIED | Not known. **Legal to write. Illegal to hide** | "2026-27 storefront prices [U]" |

**[D] DERIVED** is retained as a synonym of **[E]** for continuity with `VENDOR-ECOSYSTEMS.md` and `ROBOT-ARCHETYPE-LIBRARY.md`, whose tables this protocol reads directly.

> **Carried over from the upstream phase and binding here:** *every number in every artifact carries one of `[C] [H] [M] [E] [U]`. An unlabelled number is treated as `[U]`, which means it cannot satisfy a done-criterion.* In a BOM, an unlabelled number is a price or a quantity nobody can defend at the cart.

### 0.2 Parts-row confidence tags (the anti-hallucination contract)

Identical to `VENDOR-ECOSYSTEMS.md` §0.2, plus one tag this file adds:

| Tag | What it guarantees |
|---|---|
| **VERIFIED** | The author loaded that vendor page **in the same session as writing the row** and read name, SKU, price and stock string off it |
| **VERIFIED-UPSTREAM** | The row was copied from a workspace catalog (`VENDOR-ECOSYSTEMS.md`, `LEGAL-PARTS-CONSTRAINTS.md`) that carries its own VERIFIED tag **and a logged URL**. Provenance is one hop away — **still requires B6 before ordering** |
| **MANUAL-SKU** | The part number comes from a **BIOBUZZ V0 manual table** (12-1 motors / 12-2 servos / 12-3 power modules / 12-4 batteries / 12-9 coprocessors). Legality is [C]; **price is separately tagged** |
| **FAMILY-ONLY** | Product *family* and *category URL* verified; the specific SKU is not. Row is stamped **NEEDS-SKU-CHECK** |
| **UNVERIFIED** | Named from context only. **Never order against this row** |

**Three rules that are not negotiable:**

1. **No SKU or price enters a BOM unless it came off a page someone actually loaded, or out of a V0 manual table someone actually grepped.** A verified *family* plus an honest NEEDS-SKU-CHECK beats an invented part number every time.
2. **Every price carries an "as of" date and the stamp VERIFY-BEFORE-ORDER.** FTC vendors reprice at season turnover.
3. **Prefer vendor category/collection URLs** (stable) over deep product URLs (rot). Deep-linked product pages 404'd on us twice in this session alone (§A5).

### 0.3 Interface contract — what the host protocol supplies, and what it gets back

*(Mirrors `STRATEGY-RANKING-PROTOCOL.md` §0.1, so the two files compose without renumbering.)*

| Slot | This file's assumption |
|---|---|
| **Phase name** | **PHASE B — BILL OF MATERIALS & PURCHASING.** Step bodies are name-independent; rename freely |
| **Step ids** | `B1`…`B7`. The **`B`-prefix is deliberate** — it composes with the upstream `D0`…`D8` without collision. Renumber if the host insists, but **keep the order**: it is a dependency chain, not a menu |
| **Runs after** | **PHASE D**, `reference/STRATEGY-RANKING-PROTOCOL.md`. That file's §0.1 states it *"Runs before: BOM / purchasing, CAD, and the portfolio-evidence phase"* and that **`D5` feeds the BOM phase**. Formally: **B1 consumes the D5 ranked recommendation list (§8.4) as filtered by the D8 vote (§11.2)** |
| **Runs before** | Fabrication, build sequencing (`playbook/TWO-ROBOT-PROGRAM.md` §5.3), and event prep |
| **Output root** | `analysis/kickoff/` for run artifacts, **one artifact per step** (`B1-mechanisms.md`, `B2-variants.md`, `BOM-A.csv`, `BOM-B.csv`, `B6-verification-log.md`), and `analysis/DECISION-LOG.md` for the log — **the upstream file's convention, adopted unchanged.** Do not merge steps; the per-step files are the audit trail |
| **Evidence labels** | §0.1 above — adopted from the upstream phase |
| **Scoring instrument (upstream)** | `reference/ACHIEVABILITY-RUBRIC.md` **v1.1** — 12 + 5 + 3 factors, two axes, cuts **A = 65 / V = 55**. This protocol does not re-score; it consumes the result |
| **Companion prompt pack** | `tools/bom/PROMPTS-bom.md` — one copy-paste prompt per step, matching the `REVIEW-PROMPTS-STRATEGY.md` convention. **Prompts reference step ids; renumber both together** |

### 0.3a The other files this protocol depends on

| Upstream — produces the input | Status |
|---|---|
| `reference/STRATEGY-RANKING-PROTOCOL.md` **D5** (§8.4 ranked recommendation list) + **D8** (§11.1 decision brief, §11.2 vote) | **Present.** This is the formal input to B1 |
| `reference/ACHIEVABILITY-RUBRIC.md` §9 | **Present.** The floor, decision rule and tie-breakers the upstream phase applied. If the rubric version changes, the upstream phase re-runs D4 — **and this protocol re-runs from B2** |
| `reference/ROBOT-ARCHETYPE-LIBRARY.md` §0.3 steps 1–6 | **Present.** Its step 4 (the R503 8+8 check) is the same check this protocol re-runs at B2. Running it twice is deliberate |

| Downstream — consumes the output | File |
|---|---|
| The orderable spreadsheet | `tools/bom/BOM.template.csv` |
| The AI prompts that generate and audit BOMs | `tools/bom/PROMPTS-bom.md` |
| The game-independent shelf stock that should already exist | `tools/bom/preseason-standing-order.md` |
| The decision log (B7) | `playbook/TWO-ROBOT-PROGRAM.md` §5.4 ordering calendar + the team's own decision log |

| Sideways — the catalogs this protocol reads, never repeats | What it gives B2/B3 |
|---|---|
| `reference/VENDOR-ECOSYSTEMS.md` | Vendor profiles, the **interoperability map** (§3), procurement reality and the demand-spike evidence (§5), the standing order (§6) |
| `reference/LEGAL-PARTS-CONSTRAINTS.md` | The purchasing envelope: motors §2, the **8+8 budget** §3, servos §4, electronics §5, power §6, pneumatics §7, **fabrication-vs-COTS definitions** §8 |
| `reference/mechanisms/DRIVETRAIN-AND-ODOMETRY.md` | Per-mechanism variant catalogs. **⚠ As of 2026-08-21 `reference/mechanisms/` does not exist** — a parallel Phase B effort is producing it. **Fallback until it lands:** use `VENDOR-ECOSYSTEMS.md` §6.4 (motion) + `ROBOT-ARCHETYPE-LIBRARY.md` §1.3 |
| `reference/mechanisms/INTAKE-AND-MANIPULATION.md` | *(same status)* Fallback: `VENDOR-ECOSYSTEMS.md` §6.4 wheels/intake + §6.7 fab list |
| `reference/mechanisms/EXTENSION-ARMS-LIFTS.md` | *(same status)* Fallback: `VENDOR-ECOSYSTEMS.md` §6.4 Viper-Slide rows + `LEGAL-PARTS-CONSTRAINTS.md` §8 |
| `reference/mechanisms/LAUNCHERS-AND-FEEDING.md` | *(same status)* Fallback: `ROBOT-ARCHETYPE-LIBRARY.md` §3.3 |
| `reference/mechanisms/ELECTRONICS-AND-SENSING.md` | *(same status)* Fallback: `LEGAL-PARTS-CONSTRAINTS.md` §5 |
| `reference/mechanisms/IN-HOUSE-FABRICATION.md` | *(same status)* Fallback: `VENDOR-ECOSYSTEMS.md` §6.7 |
| `reference/ACHIEVABILITY-FACTORS.md` | The weighted factor model, incl. **duplicability**, which B3 operationalises as "can we build/buy this twice?" |
| `research/SMALL-TEAM-ECONOMICS.md` §2 | The three budget tiers B5 compares against |
| `playbook/TWO-ROBOT-PROGRAM.md` §5.2 | The authoritative **shared-vs-duplicated** split B3 and B4 apply |

---

## G. Gate 0 — preconditions before Step B1

**[J] Do not start a BOM until all six are true. A BOM built on an unfrozen design is a shopping list you will throw away.**

| # | Precondition | Evidence it is met |
|---|---|---|
| G0.1 | **PHASE D has completed through D8.** A design proposal is "approved" when it has cleared the `ACHIEVABILITY-RUBRIC.md` §3 gates and §9.1 minimum viable floor, made the **D5 ranked list** above the **A = 65 / V = 55** cuts, and **won the D8 student vote** | The D8 one-page decision brief exists, dated and versioned, and the `analysis/DECISION-LOG.md` entry is appended |
| G0.2 | **Which robot this BOM is for is written down** — A robot, B robot, or "shared architecture, both robots". D8 §11.1 field 1 names both | One line at the top of the CSV: `# BOM FOR: <A / B / BOTH>` |
| G0.2a | **The D7 fallback candidate is known**, with its switch cost in hours, dollars and printed parts | D8 brief field 5. **[J] A BOM whose fallback is unknown cannot answer "what do we stop buying if we switch?"** |
| G0.3 | **The scoring table has been read** and every mechanism traces to a scoring action | `SCORING-PATTERNS.md` §C.2 answers exist |
| G0.4 | **Both vendor discounts are live**: goBILDA FIRST team discount (25%, "active for the life of the team"), REV FTC code (15% on select items, **"Discount codes expire May 31, 2027"** — VERIFIED 2026-08-21 at `revrobotics.com/ftc/discounts/`) | A test cart shows the discounted price for both teams |
| G0.5 | **One buyer, one card, one account** is designated for the program | Named in the decision log |
| G0.6 | **The preseason standing order has already shipped** | `tools/bom/preseason-standing-order.md` rows marked `ordered_status = RECEIVED` |

> **[J] G0.6 is the one people skip and the one that hurts.** If the shelf stock is not already in the building on September 12, the kickoff BOM balloons from "the parts this design needs" to "the parts this design needs *plus every generic part we never bought*," and it competes for the same three-week window as 7,000 other teams.

---

## B1 — Decompose the design proposal into major MECHANISMS

**Input:** the approved design proposal (Gate 0). **Owner:** design lead + BOM owner. **Time-box: [J] 45 min per robot.**

### Procedure

1. **List every MECHANISM the robot needs to execute its scoring plan**, in the order the game piece (or the robot) moves through it. Use the manual's own vocabulary — `KEYWORD-GLOSSARY.md` — so the BOM, the portfolio and the inspection checklist all say the same words.
2. **Use this standard decomposition as the checklist.** [J] It is game-agnostic; every FTC robot in the corpus decomposes into some subset of it:

| # | Mechanism slot | Always present? | Typical motors | Typical servos |
|---|---|---|---|---|
| M1 | **Drivetrain** (chassis, wheels, gearing) | **Yes** | 2–4 | 0 |
| M2 | **Odometry / localization** (dead wheels, IMU, encoders) | Usually | 0 | 0 |
| M3 | **Intake / acquisition** | If the robot handles game elements | 1 | 0–1 |
| M4 | **Transfer / indexing / hopper** | If acquisition and scoring are separated | 0–1 | 0–2 |
| M5 | **Extension / lift / arm** | If scoring is not at floor level | 1–2 | 0–1 |
| M6 | **End effector** (gripper, wrist, deflector, launcher head) | If the robot places rather than dumps | 0–1 | 1–3 |
| M7 | **Endgame mechanism** (climb, park aid, deploy) | Game-dependent — **DEFERRED TO KICKOFF** | 0–1 | 0–2 |
| M8 | **Electrical / control** (Control Hub, wiring, switch, battery mount) | **Yes** | — | — |
| M9 | **Sensing / vision** | Usually | — | — |
| M10 | **Structure & superstructure** (frame, plates, guards, bumper-less perimeter) | **Yes** | — | — |
| M11 | **Compliance items** (ROBOT SIGNS, main switch, grounding strap, wire colours) | **Yes** | — | — |

3. **Do not let M11 be an afterthought.** It is a real mechanism with a real BOM and a real failure mode (§M).
   - **R401\* [C]:** *"Minimum of two ROBOT SIGNS per ROBOT… placed in at least 2 separate locations… on opposite or adjacent surfaces of the ROBOT, 90 degrees apart,"* each *"minimally be 6.5 inches (16.5 cm) wide"* and *"minimally be 2.5 inches (6.4 cm) tall,"* made of *"a robust material"* and *"supported by the structure/frame of the ROBOT."*
   - **R402\* [C]:** each sign must contain a solid red **or** blue opaque rectangle ≥ 6.5 in × 2.5 in, and **"cannot be powered or rely on power from any sources to illuminate/reveal ALLIANCE color."**
   - **[D] That is 2 signs × 2 alliance colours × 2 robots = up to 8 sign faces.** Make them in August.
4. **Write one line per mechanism naming the scoring action it serves.** A mechanism with no scoring action is a cut candidate at B5, not a BOM line.
5. **Flag anything gated on R105.** **R105 [C] verbatim:** *"ROBOTS must stay as one assembly, and there are limits to how much it can expand… After the MATCH has started, ROBOTS may expand beyond the STARTING CONFIGURATION but are still subject to sizing constraints relative to the ROBOT, based on the initial STARTING CONFIGURATION.* ***Sizing Constraints and more details will be released at Kickoff.***" — **the expansion numbers do not exist yet.** Any mechanism whose *size* is the design variable (slide stage count, arm length, telescoping reach) is stamped **DEFERRED-R105** and its length-dependent SKUs are held until the Kickoff manual is read.
   - **R102\* [C] is knowable now:** STARTING CONFIGURATION is limited to an **18 in × 18 in × 18 in (45.70 cm)** cube, fully self-contained and stationary at MATCH start. Packaging density is a today-problem; expansion is a kickoff-problem.
   - **R104\* [C]: there is no ROBOT weight limit in BIOBUZZ.** Do not spend money buying the lighter version of a part for weight reasons. Buy the stiffer one.

### ✅ Done-criterion for B1

> A numbered mechanism list exists for this robot; **every mechanism names the scoring action it serves**; every mechanism is tagged `DEFERRED-R105 = yes/no`; M8, M10 and M11 are on the list even though nobody is excited about them. **The list is pasted into the `mechanism` column of `tools/bom/BOM.template.csv` as the row grouping.**

### ❌ Failure mode this step prevents

A BOM organized by *vendor* instead of by *mechanism*. Vendor-organized BOMs cannot answer "if we cut the endgame mechanism, what do we stop buying?" — which is exactly the question B5 asks.

---

## B2 — Select a variant per mechanism, and legality-check it

**Input:** B1 mechanism list. **Owner:** mechanism owner + rules lead. **Time-box: [J] 30 min per mechanism.**

### Procedure

1. **For each mechanism, open its Phase B catalog** (`reference/mechanisms/…`, or the fallback named in §0.3) and **pick exactly one variant**.
2. **Record WHY in one sentence, against a named factor.** [J] The sentence must contain a comparison, not a preference. Good: *"48 mm omni over 96 mm because the 18-in cube (R102\*) leaves no room under the intake and we already own eight."* Bad: *"omni wheels are better."* Score the choice on the `ACHIEVABILITY-FACTORS.md` factors that discriminate — at minimum **duplicability**, since it is a first-class factor in this workspace.
3. **Record the runner-up and the switch trigger.** [J] *"If `3210-0003-0002` goes out of stock, we use the 4-stage 240 mm kit and shorten stage travel."* Write it now; the substitution decision is much worse under time pressure at 11 p.m. in week 3.
4. **Run the legality check against `reference/LEGAL-PARTS-CONSTRAINTS.md` and cite the rule ID in the `legality_rule_id` column.** The five tests that actually reject parts:

| Test | Rule | The question | Where it bites |
|---|---|---|---|
| **COTS major mechanism** | **R301\* [C]** — *"COTS MAJOR MECHANISMS purposefully designed to complete a game task are prohibited,"* exceptions: **A. COTS drive CHASSIS**, **B. official FIRST StarterBot MECHANISMS**. Also: *"A vendor selling 'build to print' manufacturing of publicly available, purpose-built solutions is against the spirit of this rule."* | Is this a bought thing that does a game task? | A bought chassis (Strafer, BeeLine) is **explicitly legal**. A bought "specimen claw" for this year's game would not be |
| **Single degree of freedom** | **R303\* [C]** — COTS COMPONENTS/MECHANISMS *"must not exceed a single degree of mechanical freedom."* Allowed: **A** linear slide kit, **B** linear actuator kit, **C** single-speed (non-shifting) gearboxes, **D** pulley, **E** turntable, **F** lead screw, **G** single-DoF gripper. Exceptions: **H** ratcheting devices, **I** holonomic wheels (omni or mecanum), **J** dead-wheel odometry kits, **K** motion transfer between misaligned components (U-joints etc.) | Does this bought assembly move in more than one way? | A **bought** multi-DoF gripper is illegal; a **fabricated** one is fine (R302\*) |
| **Actuator allowlist + 8+8 budget** | **R501\* [C]** (closed motor list, Table 12-1: *"The only allowed motor actuators are"*), **R502\* [C]** (servo requirements, Table 12-2), **R503\* [C]** — *"ROBOTS are limited to a total of 8 motors and 8 servos… for all MECHANISMS used in all configurations… If a ROBOT has multiple configurations used at a single event which use different MECHANISMS, the sum total of all motors and servos must be less than or equal to the limit"* | Is this motor on the closed list? Does the robot still fit 8+8? | **[H] DECODE allowed 10 servos — BIOBUZZ allows 8. Any carried-over design with 9–10 servos is now ILLEGAL.** See `LEGAL-PARTS-CONSTRAINTS.md` §3.2 |
| **Power / control** | **R601\* [C]** (exactly 1 approved 12V NiMH main battery, from the **closed Table 12-4 list**; fuse may be replaced with a *"COTS equivalent in-line 20A ATM mini blade fuse"*; connectors may be replaced with *"Anderson Powerpole, XT30, or any connector with a comparable power rating"*), **R701\* [C]** (one ROBOT CONTROLLER: REV Control Hub `REV-31-1595`, **or** an Android smartphone connected to a REV Expansion Hub `REV-31-1153` — the phone path is still legal), **R702\* [C]** (coprocessor software may not be altered except programmable vision coprocessors in Table 12-9) | Is every powered thing on an allowlist? | Table 12-4 is a **closed 7-item list**. Table 12-1 is a **closed** motor list. Table 12-2 is **open** (*"including, but not limited to"*) but spec-tested |
| **Air / vacuum** | **R801\* [C]** — no pneumatic actuators, high-speed blowers, or vacuums; only **sealed COTS closed-air systems pre-charged by the manufacturer** (e.g. gas shocks) | Does this design move air or grip by suction? | **No pneumatic cylinders. No suction/vacuum intakes.** Gas springs and constant-force springs remain fully available |

5. **Fill the mandatory 8+8 worksheet.** [C] R503. **No BOM is complete without it.** Copy this block into the BOM as comment rows or a sibling sheet:

| Mechanism | Motors | Servos | Running motors | Running servos |
|---|---|---|---|---|
| M1 Drivetrain | | | / 8 | / 8 |
| M3 Intake | | | / 8 | / 8 |
| M4 Transfer | | | / 8 | / 8 |
| M5 Lift / extension | | | / 8 | / 8 |
| M6 End effector | | | / 8 | / 8 |
| M7 Endgame | | | / 8 | / 8 |
| **TOTAL** | **≤ 8** | **≤ 8** | | |

   - **[C] The carve-out that buys you slots:** motors integral to an unmodified COTS *sensor* (e.g. LIDAR, scanning sonar) *"provided the device is not modified except to facilitate mounting,"* and vibration/autofocus motors inside COTS computing devices, **"do not count toward the limit in R503."** A scanning LIDAR's motor is free.
   - **[C] The carve-out that costs you slots:** R503 counts **all configurations at an event**, and inspection rule **I302\*** re-checks it — a spare mechanism in the pit counts.
   - **[J] The single highest-leverage move:** every function achievable with a **spring, gas spring, over-centre linkage, ratchet, or passive one-way gate** costs **zero** actuator slots and zero dollars-times-two. R303.H permits ratcheting devices; R801.A permits pre-charged sealed gas shocks. Mine that allowance hard before you spend a motor slot.
6. **[C] Re-gear before you re-buy.** Table 12-1 note: *"Many legal gearmotors are sold with labeling based on the entire assembly. These motors may be used with or without the provided gearbox, and/or with any other compatible gearbox."* Changing a Yellow Jacket's ratio is legal and is cheaper than buying a second motor family — and it protects the two-robot inventory (one motor family, two robots).
7. **Check the interoperability map before mixing vendors.** `VENDOR-ECOSYSTEMS.md` §3 — shaft standards (§3.3), fasteners (§3.4) and **chain/belt (§3.5, "the hard wall")**. [J] A BOM that quietly mixes two structural ecosystems produces two robots that share no spares, which is the exact opposite of why this program runs two teams.

### ✅ Done-criterion for B2

> Every mechanism has **one selected variant, one recorded WHY sentence, one recorded runner-up + switch trigger, and a `legality_rule_id`** citing an R-rule that was **grepped in `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt`**, not recalled. The 8+8 worksheet totals **≤ 8 motors and ≤ 8 servos** with the arithmetic shown. Any DEFERRED-R105 length decision is explicitly parked, not guessed.

### ❌ Failure mode this step prevents

Discovering at inspection that the design is one servo over, or that the bought gripper is a multi-DoF COTS mechanism. Both are unfixable on event morning and both are trivially detectable here.

---

## B3 — Split BUY versus FABRICATE, through the duplicability lens

**Input:** B2 selected variants. **Owner:** BOM owner + fabrication lead. **Time-box: [J] 30 min per mechanism.**

### The decision rule

**[J] Fabricate when the part is geometry; buy when the part is precision, and buy when the part is legality.**

| Fabricate it | Buy it |
|---|---|
| Brackets, mounts, trays, spacers of odd length | Bearings, shafting, hubs, gearboxes |
| Intake rollers, compliant wheels (TPU) | Motors, servos, batteries, control electronics (**allowlisted — R501/R502/R601/R701 [C]**) |
| Gripper fingers/jaws — **a bought multi-DoF gripper is illegal (R303\*), a fabricated one is legal (R302\*)** | Linear slide kits — explicitly legal COTS single-DoF (**R303.A [C]**) and not realistically fabricable without a mill |
| Guards, hoppers, deflectors from polycarbonate sheet — **R302\* [C] names "sheet stock" as a legal raw material** | Chain, belt, sprockets, pulleys (**R303.D [C]** pulley) |
| ROBOT SIGNS (**R401/R402 [C]**) | Omni / mecanum wheels (**R303.I [C]** explicit exception) |
| Cable clips, battery retention | Dead-wheel odometry kits (**R303.J [C]** explicit exception) |

**[C] Your authority to fabricate is R302\*:** *"Allowed raw materials and legal COTS parts can be modified (drilled, cut, painted, etc.) as long as no other rules are violated,"* with raw materials explicitly including **sheet stock, extruded shapes, metals, plastic, rubber, and wood, and magnets.**
**[C] Your authority to start before kickoff is R304\*:** custom software, designs and parts can be reused year-to-year and pre-Kickoff fabricated items are permitted — which is why the preseason chassis build is legal.

### The duplicability lens — apply to EVERY line

**[J] Five questions. Any "no" changes the line.**

| # | Question | If the answer is bad |
|---|---|---|
| D1 | **Can we buy two of this today?** Check the live stock string, not the catalog | If only one is available: it is not in the design. Move to the runner-up (B2 step 3) |
| D2 | **Can we make two of this?** Print time × 2, cut time × 2, jig required? | If a part takes 9 h to print, two robots is 18 h of printer time — see `TWO-ROBOT-PROGRAM.md` §6.3 printer queue |
| D3 | **If we make two, will they be the same?** | Hand-cut one-offs drift. **[J] If two parts must match, build a jig or print them — do not hand-cut them twice** |
| D4 | **Does the B robot actually need this, or is it A-only?** | `TWO-ROBOT-PROGRAM.md` §2.3 — the recommended model is a shared architecture with a simpler B mechanism. Not every line is ×2 |
| D5 | **Does it plug into a robot, or sit on a bench?** | **The organizing principle from `TWO-ROBOT-PROGRAM.md` §5.2: duplicate what plugs into a robot; share what sits on a bench** |

### The shared-vs-duplicated split (authoritative source: `TWO-ROBOT-PROGRAM.md` §5.2)

| Category | Multiplier | Rule / reason |
|---|---|---|
| ROBOT CONTROLLER, OPERATOR CONSOLE | **×2** | **R701\*, R901\* [C]** — per robot, per team |
| Motors, servos, wheels, drivetrain | **×2 sets** | **R503\*, I302\* [C]** — each robot is a separate ROBOT with its own 8+8. A shared pool does **not** create a shared allowance |
| Main battery | **×2 minimum, 5–6 across the program** | **R601\* [C]** 1 per robot; **E511\* [C]** caps chargers at *"a 3-amp average channel current"*, so one charger cannot turn packs around at a two-robot event |
| ROBOT SIGNS | **≥2 per robot, both colours** | **R401/R402\* [C]** |
| **Printed parts** | **×3 full sets** (A, B, spares) | `ACHIEVABILITY-FACTORS.md` F2 — a 25-part design implies 75 prints |
| Practice field, game set, 3D printer, hand tools, CAD/code/scouting seats | **×1** | One shop, time-sliced |
| Bulk stock: channel, plate, fasteners, chain, belt, filament | **×1 bulk order, split** | Buying two half-orders costs more and ships twice |

### ✅ Done-criterion for B3

> Every BOM line carries `buy_or_fab` ∈ {BUY, FAB, HYBRID}; every FAB line names its **method and machine** (3D print / cut polycarb / cut channel) and its **per-part cycle time × 2**; every BUY line has passed D1 (a live stock string, dated). **The line-count of the FAB list has been multiplied by 3 for prints and the printer queue in `TWO-ROBOT-PROGRAM.md` §6.3 has been checked against the calendar.**

### ❌ Failure mode this step prevents

The design that is buildable once. [J] A mechanism the A team can build in a weekend of mentor-supervised hand-fitting is not a mechanism — it is a prototype, and the B robot will never get one.

---

## B4 — Build the quantity table, and pull long-lead items forward

**Input:** B3 split. **Owner:** BOM owner. **Time-box: [J] 60 min per robot.**

### Procedure

1. **Fill `qty_per_robot`, `spares_qty`, `qty_total` for every line.** The formula the CSV assumes:

   ```
   qty_total = (qty_per_robot × 2) + spares_qty
   ```

   Set `qty_per_robot = 0` and put the real number in `qty_total` for shared/bench items (one printer, one belt starter pack, one bulk fastener pack).

2. **Apply the spares policy (§A1).** [J] Spares are not optional depth; they are the difference between "we lost a match" and "we lost a day."
3. **Add the fasteners and bearings pass — a separate, deliberate sweep.** For every mechanism, ask: *what bolts this to the robot, and what does the shaft turn in?* [J] This sweep finds 10–20% more lines than the mechanism-by-mechanism pass does, and those lines are the ones that stop a build at 10 p.m.
4. **Mark `long_lead_flag = Y` on every line meeting any of these tests** and sort them to the top of the first purchase order:

| Long-lead test | Basis |
|---|---|
| The vendor page shows anything other than a clean in-stock string today | [J] |
| The item is a **limit-one-per-registered-team** storefront kit | `VENDOR-ECOSYSTEMS.md` §2.6 |
| The item is a **linear slide kit** | [J] highest stock-out-risk family in FTC |
| The item is a **fastener assortment or a bearing pack** | **VERIFIED 2026-08-21:** goBILDA M4 Socket Head Screw Assortment `3201-0004-0001` reads **"OUT OF STOCK"** — three weeks before kickoff |
| The item is **8 mm chain or a chain tensioner** | `VENDOR-ECOSYSTEMS.md` §3.5 — the chain island has no cross-system substitute |
| The item is a **battery, charger, or 20 A ATM fuse** | **R601\* [C]** items, closed Table 12-4 list |
| The item is a **vision coprocessor** | **R702\* [C]** Table 12-9 — a closed list |
| The item is **AndyMark field / game elements** | **VERIFIED [H] via `VENDOR-ECOSYSTEMS.md` §5.5:** the **2026-08-07 pre-order cutoff has already passed**; sets *"begin shipping… Monday, 14-September, 2026"*; **"All sales are final"** |

5. **The demand spike is measured, not folklore.** `VENDOR-ECOSYSTEMS.md` §5.2 records **six stock-outs and three discontinuations found in a single afternoon on 2026-08-21, three weeks before kickoff** — including a rule-named device (Expansion Hub `REV-31-1153`, Out of Stock) and a rule-named power module (Servo Power Module `REV-11-1144`, **Discontinued** but still legal in Table 12-3: *legal, unbuyable*).
6. **[J] Planning assumption, not a vendor SLA:** 1–2 weeks door-to-door for a normal in-stock US FTC vendor order; **3–6 weeks for anything backordered in September–October.** Confirm at order time. goBILDA and REV shipping-policy pages **404'd** when a prior session tried to read them (`VENDOR-ECOSYSTEMS.md` §5.1).
7. **Backorder discipline** (`VENDOR-ECOSYSTEMS.md` §5.3): never let a backorder hold a shipment (choose ship-partial); **treat "Out of Stock" as "not in the design"** during the kickoff-week decision; second-source commodity lines against ServoCity, whose catalog mirrors goBILDA's.

### ✅ Done-criterion for B4

> `qty_total` is populated and arithmetically consistent on **every** line; a separate fastener/bearing sweep has been run and its lines added; `long_lead_flag` is set; the BOM is **sorted long-lead-first**; **PO #1 (long-lead) and PO #2 (everything else) are drafted as two separate carts.**

### ❌ Failure mode this step prevents

Ordering one of something needed on both robots — the single most expensive clerical error available to this program (§M).

---

## B5 — Cost it, compare to the budget tiers, and name the cuts

**Input:** B4 quantity table. **Owner:** BOM owner + treasurer/mentor. **Time-box: [J] 45 min.**

### Procedure

1. **Compute `extended_cost_usd = unit_cost_usd × qty_total` per line**, then subtotal **by mechanism** (not by vendor). Mechanism subtotals are what makes the cut conversation possible.
2. **Show three totals:** list price → after discounts (goBILDA 25% "nearly every product storewide", REV 15% "select items") → **plus ~10% for shipping and sales tax** (`SMALL-TEAM-ECONOMICS.md` §1.9, §2).
3. **Compare against the tiers** (`SMALL-TEAM-ECONOMICS.md` §2, all-in first-year, incl. ~10% shipping/tax, **Championship excluded**):

| Tier | First-year all-in | Recurring (yr 2+) | What it buys |
|---|---|---|---|
| **A — bare minimum** | **≈ $2,620** | ≈ $900 | Legal, inspectable robot; reliable AUTO; **full access to judged awards incl. Inspire** |
| **B — genuinely competitive** | **≈ $7,240** | ≈ $3,000 | + full tiles, same-day printing, adequate spares |
| **C — well-funded** | **≈ $14,280** | ≈ $6,500 | + a second control system, official field, deep spares |

   > **[J] Two rows from that table are load-bearing for this program:** Tier A and Tier C have *identical* access to the free digital toolchain and to judged awards. And Tier B (~$7,240) is the honest number for a program that intends to advance. **This BOM is one line inside that budget, not the budget.**
   > **[J] Two-team caveat:** the tier table is a *one-team* budget. Registration ($350 [O-FTC]) and the limit-one storefront kits are **per registered team** — which is the genuine financial advantage of running two registrations (`TWO-ROBOT-PROGRAM.md` §5.4), not a penalty.

4. **If over budget, cut in this order** — [J] ranked by savings per unit of performance lost, consistent with `SMALL-TEAM-ECONOMICS.md` §5.1:

| # | Cut | Saves | Costs you |
|---|---|---|---|
| 1 | **The endgame mechanism**, if it is not yet scored in the manual | motors + servos + $$ ×2 | Possibly nothing — **DEFERRED TO KICKOFF**; do not buy against a guess |
| 2 | **Premium servos → workhorse servos** on low-load joints | ~$60–80 per servo ×2 | Speed/torque headroom |
| 3 | **Mecanum → tank/differential**, if the game does not demand strafing | a **$340–600 line ×2 robots**, plus 2 motor slots back | Manoeuvrability. **[C] R303.I** makes both legal; this is a game call |
| 4 | **Buy one belt/pulley starter pack for both robots** instead of two | ~$210–240 | Nothing — it is bench stock (D5) |
| 5 | **Fabricate the bracket instead of buying it** | $5–15 per bracket ×2 | Printer hours (D2) — check the queue first |
| 6 | **Fewer slide stages, not fewer slides** | ~$70 per robot | Reach — **DEFERRED-R105**, so decide after the manual, not before |
| 7 | **Defer the vision coprocessor**; use the webcam that ships in the Driver Kit | ~$189 ×2 | AUTO ceiling. **[C] R702**/Table 12-9 restricts what you may buy later, so keep it on the list |

5. **The three cuts that are false economies** — [J] `SMALL-TEAM-ECONOMICS.md` §5.2. **Never cut: batteries, spare motors/servos, or fasteners.** Each is cheap, each is the direct cause of a lost event day, and each doubles for two robots.
6. **Never cut a compliance item.** M11 (signs, main switch, grounding strap, correct wire colours per **R609/R610 [C]**) is ~$0–40 and is the difference between passing and failing inspection.

### ✅ Done-criterion for B5

> The BOM shows **list → discounted → +10% landed** totals, subtotalled **by mechanism**; the total is compared to a named tier; **if over, the specific cut lines are struck through in the CSV with a `notes` reason — not silently deleted**; and the cut decision is recorded with a name and a date.

### ❌ Failure mode this step prevents

The silent cut. A line deleted without a reason gets re-added by a different student a week later, and the program pays for it twice.

---

## B6 — Verify every SKU on the live vendor page (MANDATORY)

**Input:** the costed BOM. **Owner:** BOM owner, **one person, one sitting**. **Time-box: [J] 60–90 min for a full-robot BOM.**

> **This step is not optional and it is not delegable to memory. The catalogs in `reference/` carry confidence tags precisely because their rows have a shelf life. A price from three weeks ago and a SKU from a search-engine snippet are both wrong until proven otherwise.**

### Procedure — run this per line, in order

1. **Open the vendor's own page.** Prefer the **category/collection page** — it shows name, SKU, price and stock string for many parts at once and it does not rot. (Both deep-product-URL attempts in this session 404'd; every category page loaded — §A5.)
2. **Read four things off the page and write all four into the CSV:** exact `item` name, `sku`, `unit_cost_usd`, and the vendor's **own** `stock_status_string`, copied verbatim (e.g. `"In Stock & Ready To Ship!"`, `"OUT OF STOCK"`, `"Discontinued"`). Stamp `stock_checked_date`.
3. **Set `confidence`** per §0.2. A row may only be **VERIFIED** if the person filling it loaded the page in that sitting. Otherwise it is **VERIFIED-UPSTREAM**, **FAMILY-ONLY (NEEDS-SKU-CHECK)** or **UNVERIFIED**.
4. **Cross-check every allowlisted part against the manual table, not the vendor's marketing.** Motors → Table 12-1 (**closed**). Servos → Table 12-2 (**open**, spec-tested). Power modules → Table 12-3. **Batteries → Table 12-4 (closed, 7 items).** Coprocessors → Table 12-9. Vendors sell many legal-looking parts that are not on the lists.
5. **Resolve every discrepancy before ordering. Discrepancies found in this session, as live worked examples:**

| Discrepancy | What happened | The lesson |
|---|---|---|
| **Search snippet gave the wrong SKU** | A web search returned `3200-4008-2627` as the SKU for the *FTC Starter Kit Upgrade Pack*. The **goBILDA category page** shows the Upgrade Pack is **`3200-0101-2627` ($249.99)** and `3200-4008-2627` is the **FTC Starter Kit 2026-2027 Season ($899.99)**. Both **VERIFIED 2026-08-21** at [gobilda.com/ftc-kits](https://www.gobilda.com/ftc-kits) | **Never take a SKU from a search result.** Two products, adjacent in the catalog, $650 apart |
| **Two workspace files disagree on storefront prices** — ***RESOLVED 2026-08-22*** | `VENDOR-ECOSYSTEMS.md` §6.1 listed Electronics Kit **$325** / Driver Kit **$285**; `SMALL-TEAM-ECONOMICS.md` §2 budgeted **$350** / **$295** / Build Kit **$660**. **Adjudicated against the primary source:** the FIRST storefront options sheet, **Revision 25-26.4, Feb 18 2026**, states verbatim *"Step 2: Select the Driver Kit, **$285**"*, *"Step 3: Select the Electronics Kit, **$325**"*, *"Step 4: Select the Build Kit **$650**"*, each *"(Limit one per register**ed** team per season)"*, plus *"Step 1: Pay your **$325** registration fee."* **VERIFIED 2026-08-22** — PDF fetched, then text-extracted locally with `pdftotext -layout` (WebFetch returned raw binary) | ⚠️ **ADJUDICATION CORRECTED 2026-08-22 (fact-check pass): this was wrong.** `SMALL-TEAM-ECONOMICS.md` §3.1 does **not** carry rounded estimates — it prints a two-column table that explicitly labels **$325 / $285 / $325 / $650 as the *2025-26 storefront-PDF* prices** and **$350 / $295 / $350 / $660 as the *2026-27 firstinspires.org* prices**, and states in terms that *"the official Storefront PDF is stale… The FIRST Cost & Registration page lists the higher 2026-27 prices. Budget from the website, not the PDF."* **Both files were right about different seasons.** `VENDOR-ECOSYSTEMS.md` §6.1's figures are correct **[H] 25-26**; `SMALL-TEAM-ECONOMICS.md` §3.1's are the **26-27** figures. Registration rising $325 → $350 is itself the tell that the kits moved too. Both were nonetheless **[H] 25-26 figures**. **The 26-27 kit prices are still [U]** — but registration has already moved **$325 → $350** ([O-FTC], **VERIFIED 2026-08-22**), so treat the 25-26 kit prices as a **floor, not a forecast**. Do not average two guesses; go find the primary document |
| **A vendor page omits the spec the rule turns on** | REV `REV-31-1302` "12V Slim Battery", $60.00, *"In Stock & Ready To Ship!"*, 3000 mAh, XT30, 16 AWG, 20 A ATM fuse — **VERIFIED 2026-08-21** — but the page **does not state the chemistry**, and **R601\* requires "12V NiMH"** | **Resolved by the manual, not the vendor: `REV-31-1302` is named in Table 12-4 [C]**, so it is legal main power regardless of what the product page omits. *This closes the open NEEDS-VERIFY carried in `VENDOR-ECOSYSTEMS.md` §6.1* |
| **A legal part is unbuyable** | Servo Power Module `REV-11-1144` is named in Table 12-3 **[C]** and is **Discontinued** | **Legality and availability are two different columns.** Check both |
| **A boring part is already gone** | `3201-0004-0001` M4 Socket Head Screw Assortment: **"OUT OF STOCK"**, confirmed twice this session on two different goBILDA category pages | Fasteners stock out first and hurt most |

6. **Where the SKU cannot be verified, ship the honest row:** name the **product family**, link the **category URL you did load**, and stamp **NEEDS-SKU-CHECK**. That row is orderable by a human with a browser; an invented part number is not.
7. **If a vendor site blocks you, say so in `notes`.** [H] Studica's site returned **HTTP 403** to a prior session; goBILDA's and REV's shipping-policy pages returned **404**. "Blocked, family only" is a finding. Silence is a fabrication.

### ✅ Done-criterion for B6

> **Zero lines in the order remain tagged UNVERIFIED.** Every ordered line is **VERIFIED** with a `stock_checked_date` of today or yesterday, or is **FAMILY-ONLY/NEEDS-SKU-CHECK** with a category URL and an explicit human-checks-at-cart note. Every allowlisted part has been matched against its **manual table number**. Every discrepancy is resolved in writing.

### ❌ Failure mode this step prevents

Discovering a part is illegal, discontinued, or the wrong part number **after it arrives** — which costs the return window plus the reorder lead time, i.e. **two to six weeks in the worst month of the year** (§M).

---

## B7 — Place the order, track lead times, record the decision

**Input:** verified BOM. **Owner:** the single designated buyer (G0.5). **Time-box: [J] 30 min to place; 5 min/week to track.**

### Procedure

1. **Order both robots' quantities in ONE order, plus spares.** [J] Never "order A now, B later." If a part goes out of stock between the two orders, **robot B becomes a different robot**, and the shared-BOM advantage that justifies running two teams is gone.
2. **One cart, one buyer, one card, one account.** Split orders across parents and mentors is how a program ends up with two slightly different robots and no receipt trail.
3. **Send PO #1 (long-lead) within 48 hours of kickoff**, before the spike peaks. [J] *A wrong $60 motor that arrives in September beats a right motor that arrives in November.* PO #2 (the rest) can follow the design freeze.
4. **Buy the FIRST storefront kits per registered team immediately** — limit one per item per category per season, and **two registrations means two allocations**. That limit is a large part of why two registrations is financially efficient (`VENDOR-ECOSYSTEMS.md` §2.6).
5. **Choose ship-partial, never ship-complete.**
6. **Track:** set `ordered_status` ∈ {NOT-ORDERED, ORDERED, BACKORDERED, SHIPPED, RECEIVED, RECEIVED-WRONG, RETURNED} and record `po_ref`. **[J] Review the BOM's status column at every weekly meeting** — a backorder discovered in week 5 that was placed in week 1 is a schedule fact nobody noticed.
7. **Receive against the BOM, not against the box.** Tick `RECEIVED` line by line. Count the fasteners. [J] A short-shipped line found at unboxing is a same-day reorder; found in week 6, it is a blocked build.
8. **Record the decision in the decision log — `analysis/DECISION-LOG.md`, append-only.** [C-convention, from `STRATEGY-RANKING-PROTOCOL.md` §11.3] **Never edit a past entry; supersede it.** One entry per BOM, containing:

   | Field | Content |
   |---|---|
   | Date, robot (A/B/both), design proposal ID | |
   | The mechanism list (B1) | |
   | Per mechanism: variant chosen, **WHY sentence**, runner-up + **switch trigger** (B2) | |
   | The **8+8 worksheet totals** (B2) | |
   | Buy/fab split and the duplicability calls (B3) | |
   | Long-lead list and PO split (B4) | |
   | List → discounted → landed totals, tier compared, **cuts made and why** (B5) | |
   | B6 discrepancies and how each was resolved | |
   | PO refs, order dates, promised dates | |
   | **What we would do differently** — filled at first event, not at order time | |

9. **Re-run triggers.** [J] Re-enter this protocol at **B2** if: a **Team Update** changes an R-rule (Team Updates post **every Thursday** from Kickoff to two weeks before Championship — additions highlighted yellow, deletions struck through); a **Game Q&A** answer (Q&A opens **2026-09-28, 12:00 p.m. ET**) changes a legality read; a long-lead item goes to BACKORDER; or the design changes a mechanism. **Watch R501 specifically** — its own note says additional motors may be added to the legal list in future manual updates.
   **Re-enter at B1 — the whole protocol — if the upstream phase re-runs:** the `ACHIEVABILITY-RUBRIC.md` version changes (forcing a D4 re-score), the D7 **kill criterion** fires at its **kill date**, or the D8 vote is re-taken. **[J] A rule change that alters the strategy invalidates the BOM, not just a line of it.** The upstream D7 §10.2 Team Update war-game is the drill that anticipates this — read its output before assuming a BOM survives a Thursday.

### ✅ Done-criterion for B7

> PO #1 placed within 48 h of design approval; every line has an `ordered_status` and a `po_ref`; the decision-log entry exists with the WHY sentences and the 8+8 totals; a weekly status review is on the calendar; and receiving is done **line by line against the BOM**.

---

## M. The ordering mistakes that cost teams weeks

**[J] Every one of these is cheap to prevent at the step named, and expensive to fix anywhere else.**

| # | The mistake | What it actually costs | Prevented at | The countermeasure |
|---|---|---|---|---|
| **M-1** | **Ordering one of something needed on both robots** | The reorder lead time (1–2 wks, or 3–6 wks if it backordered in the meantime) — and if it stocked out, **robot B is now a different robot** and shares no spares with robot A | **B4** | `qty_total = (qty_per_robot × 2) + spares_qty` is a formula in the sheet, not a mental step. **Sort the BOM by `qty_total` and eyeball every "1"** — each one must be justified as bench stock |
| **M-2** | **Forgetting fasteners and bearings** | A build stops at 10 p.m. over a $0.40 screw. **VERIFIED 2026-08-21:** goBILDA's M4 Socket Head assortment `3201-0004-0001` already reads **"OUT OF STOCK"** — so the emergency reorder may not even be possible | **B4** step 3 | The **separate fastener/bearing sweep** is a mandatory pass. Buy the M4 Hardware Starter Pack `3201-0010-0001` (2,625 pcs, **$139.99, in stock, VERIFIED 2026-08-21**) as shelf stock, not per-project |
| **M-3** | **Discovering a part is illegal after it arrives** | The return window (if any) plus the reorder. **[H] AndyMark game-set pre-orders: "All sales are final."** With `REV-11-1144` you can even buy a *legal* part that is discontinued and unsupported | **B2** + **B6** | Cite an R-rule in `legality_rule_id` on **every** line, and match every actuator/battery/coprocessor against its **closed manual table** (12-1 / 12-4 / 12-9) before the cart, not after the box |
| **M-4** | **No spares of the part that breaks** | A lost match, then a lost event day. Servos are the most-replaced actuator in FTC; a dead drive motor between matches ends a **two-robot** day, because both teams are queuing | **B4** + §A1 | The spares policy in §A1 is a floor: **+1 drive motor, +2 servos, +2 batteries, +1 gamepad, one full spare set of every printed part** |
| **M-5** | **Ordering against a guessed expansion limit** | Slides, arm stock and gearing bought for a reach that does not exist. **R105 [C] states the sizing constraints "will be released at Kickoff"** | **B1** step 5 | Stamp `DEFERRED-R105` and hold length-dependent SKUs until the Kickoff manual is read. Buy the *mechanism family*, not the *length*, before kickoff |
| **M-6** | **Carrying over a 9- or 10-servo design from DECODE** | The robot fails inspection under **R503 [C]** (8 servos) and **I302\***, and the fix is a redesign, not a purchase | **B2** step 5 | The 8+8 worksheet is mandatory on every BOM. **[H] DECODE allowed 10 servos; BIOBUZZ allows 8** |
| **M-7** | **Quietly mixing structural ecosystems** | Two robots that share no spares, no jigs and no CAD. The chain/belt boundary is a hard wall (`VENDOR-ECOSYSTEMS.md` §3.5) | **B2** step 7 | Commit to one structural ecosystem and one electrical ecosystem in writing; the deliberate exception (a printed interface tray) is documented in `VENDOR-ECOSYSTEMS.md` §4.3 |
| **M-8** | **Splitting the order across several people** | No receipt trail, duplicate purchases, missed discounts, and two robots built from two different shipments | **B7** step 2 | One cart, one buyer, one card (G0.5) |
| **M-9** | **Letting a backorder hold the whole shipment** | Everything waits on the one line that is late | **B4** step 7 | Always ship-partial. Treat "Out of Stock" as "not in the design" during kickoff week |
| **M-10** | **Skipping the discount paperwork** | ~25% of a goBILDA order. On a $1,800 two-kit line that is **$450** | **G0.4** | Register both teams' goBILDA accounts and both REV codes **before** kickoff — goBILDA activation is *"within the day… or the next business day"* |
| **M-11** | **Leaving compliance parts off the BOM** | Failed inspection over ROBOT SIGNS, a missing grounding strap, or wrong wire colours (**R609/R610 [C]** — colour is an inspection item, not a preference) | **B1** (M11 slot) | M11 is a mechanism with a BOM. Make the four sign faces in August |

---

## A1. Quantity and spares policy — the defaults

**[J] Use these unless the line has a reason not to. Record the reason when you deviate.**

| Class | Per robot | Program total (2 robots) | Rationale |
|---|---|---|---|
| Drive motors | 2–4 | ×2 **+1 spare** | A dead drive motor between matches ends a two-robot day |
| Mechanism motors | per design | ×2 **+1 spare** *(one spare of the family, not of every position)* | Standardize on one motor family across both robots — the saving is inventory, not unit price |
| Servos | per design | ×2 **+2 spares** | Most-replaced actuator in FTC |
| Main battery | 1 installed (**R601\* [C]**) | **5** (2 per robot in rotation + 1 pool) | **E511\* [C]:** charger capped at *"a 3-amp average channel current"* — one charger cannot turn packs around at a two-robot event |
| Chargers | — | **2–3** | One per pit so both teams are independent |
| Gamepads | 2 | **4 +1 spare** | A dead gamepad is a lost match |
| Bearings | per design | **×2 + 50%** | Bearings vanish. The goBILDA FTC Starter Kit includes 20 flanged bearings per kit |
| Fasteners | — | **bulk assortment, shared** | Never per-project |
| Chain / belt | per design | **×2 +1 spare length** | No cross-system substitute exists |
| **Printed parts** | full set | **×3 sets (A, B, spares)** | `ACHIEVABILITY-FACTORS.md` F2 |
| Polycarbonate sheet | 1 | **2 + offcuts** | Hand-tool fabrication wastes material |
| ROBOT SIGNS | 2 (**R401\* [C]**) | **4 faces min, both colours** | Inspection item |
| 20 A ATM fuses | 1 installed | **4–6** | **R601.A [C]**; cheap, tiny, blows at events |

---

## A2. CSV field dictionary (`tools/bom/BOM.template.csv`)

| Column | Type | Meaning / allowed values |
|---|---|---|
| `row_type` | enum | `EXAMPLE` (delete before use) / blank (a real line) / `SUBTOTAL` |
| `line_id` | string | Stable ID, e.g. `M5-004`. Referenced by the decision log |
| `mechanism` | string | The B1 mechanism slot, e.g. `M5 Lift / extension` |
| `item` | string | The vendor's **exact** product name, copied from the page |
| `vendor` | string | goBILDA / REV Robotics / AndyMark / ServoCity / Studica / **FIRST storefront** / other. **[H] Note the change:** the storefront options sheet rev 25-26.4 still routes teams to the *"Pitsco Storefront"*; for 2026-27 a **new FIRST Storefront replaces it**, reached the same way — Team Dashboard → *"team options"* → *"Payment and Product"* → *"Order Products"*. Write `FIRST storefront`, not `Pitsco` |
| `product_family` | string | The family and its **category URL** — required when `sku` is blank |
| `sku` | string | Vendor part number. **Blank is legal; invented is not** |
| `qty_per_robot` | int | 0 for shared/bench items |
| `spares_qty` | int | Per §A1 |
| `qty_total` | int | `= (qty_per_robot × 2) + spares_qty`, or the true count for shared items |
| `unit_cost_usd` | decimal | List price as read off the page |
| `extended_cost_usd` | decimal | `= unit_cost_usd × qty_total` |
| `buy_or_fab` | enum | `BUY` / `FAB` / `HYBRID` |
| `confidence` | enum | `VERIFIED` / `VERIFIED-UPSTREAM` / `MANUAL-SKU` / `FAMILY-ONLY` / `UNVERIFIED` |
| `lead_time_days` | string | Vendor-stated, or `[J] est` — say which |
| `long_lead_flag` | enum | `Y` / `N` — see B4 step 4 |
| `legality_rule_id` | string | The R-rule(s) that make this line legal or constrained, e.g. `R303.A`, `R601+T12-4` |
| `stock_status_string` | string | **The vendor's own words, verbatim** |
| `stock_checked_date` | date | ISO `YYYY-MM-DD` |
| `verify_url` | url | The page actually loaded — **prefer category URLs** |
| `ordered_status` | enum | `NOT-ORDERED` / `ORDERED` / `BACKORDERED` / `SHIPPED` / `RECEIVED` / `RECEIVED-WRONG` / `RETURNED` |
| `po_ref` | string | Purchase-order or vendor order number |
| `notes` | string | WHY sentence, runner-up + switch trigger, `NEEDS-SKU-CHECK`, `DEFERRED-R105`, `VERIFY-BEFORE-ORDER`, cut reasons |

---

## A3. Worked example (game-agnostic)

**[J] Illustrative only. The mechanisms are generic; no BIOBUZZ game task is implied or known.**

A design proposal for a generic **ground-intake cycler** (`ROBOT-ARCHETYPE-LIBRARY.md` §3.1) decomposes at B1 into: **M1** mecanum drivetrain, **M2** 2-pod dead-wheel odometry, **M3** roller intake, **M5** 2-stage vertical slide, **M6** single-servo gripper, **M8** electrical, **M10** structure, **M11** compliance. No M7 (endgame **DEFERRED TO KICKOFF**), no M4 (intake feeds the gripper directly).

**B2 — the 8+8 worksheet [C] R503:**

| Mechanism | Motors | Servos | Running motors | Running servos |
|---|---|---|---|---|
| M1 Drivetrain (mecanum) | 4 | 0 | 4 / 8 | 0 / 8 |
| M3 Intake (roller) | 1 | 0 | 5 / 8 | 0 / 8 |
| M5 Lift (2-stage slide) | 2 | 0 | 7 / 8 | 0 / 8 |
| M6 Gripper + wrist | 0 | 2 | 7 / 8 | 2 / 8 |
| M7 Endgame — **not yet designed** | **1 slot left** | 6 free | **7 / 8** | **2 / 8** |

> **[D] The read:** a 4-motor holonomic drivetrain spends half the motor budget before any scoring happens, and this design leaves exactly **one** motor for whatever the endgame turns out to be. **[J] That is the gate question at concept selection, not a detail** — and it is the reason cut #3 in B5 (mecanum → tank, buying back two motor slots and a $340–600 line ×2) exists.

**B2 legality citations that would appear in `legality_rule_id`:** mecanum wheels → **R303.I** (explicit holonomic exception); dead-wheel odometry kit → **R303.J** (explicit exception); slide kit → **R303.A** (linear slide kit); **gripper → FAB**, because a **bought** multi-DoF gripper violates **R303** while a **fabricated** one is permitted under **R302**; battery → **R601 + Table 12-4**; Control Hub → **R701.A**.

**B3 duplicability calls:** slide kits ×2 (D1 — check the live stock string, this family stocks out first); gripper fingers **printed ×3 sets** (D2/D3 — jig-free repeatability); belt/pulley starter pack **×1, shared** (D5 — bench stock); drivetrain motors **×2 sets +1 spare** (§A1).

**B4 long-lead:** slide kits, storefront kits, batteries + fuses, fastener assortment, chain/tensioners. **B5 cut ladder if over:** endgame first (it does not exist yet), then premium→workhorse servos, then mecanum→tank.

---

## A4. Rule cross-reference for BOM authors

Grep each in `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` before ordering. **All [C].**

| Rule | Line | Buying consequence |
|---|---|---|
| **R102\*** | 169 | 18 in × 18 in × 18 in STARTING CONFIGURATION cube — packaging density drives channel/plate choice **now** |
| **R104\*** | 197 | **No weight limit.** Do not pay for lightness |
| **R105** | 211 | Expansion limits exist; *"Sizing Constraints and more details will be released at Kickoff."* **Stamp DEFERRED-R105; buy the family, not the length** |
| **R201\*** | 220 | Robot must not damage the ARENA or make a mess — constrains wheel/intake materials |
| **R301\*** | 301 | COTS MAJOR MECHANISMS purpose-built for a game task are **prohibited**; **COTS drive CHASSIS** and official **StarterBot** mechanisms are the only exceptions |
| **R302\*** | 319 | Legal COTS parts and raw materials **may be modified** — sheet stock, extruded shapes, metals, plastic, rubber, wood, magnets. **This is your fabrication authority** |
| **R303\*** | 328 | COTS must be **single DoF**; allow-list A–G; exceptions H–K incl. ratchets, holonomic wheels, dead-wheel odometry kits |
| **R304\*** | 381 | Pre-Kickoff fabricated items and reused designs are permitted — the legal basis for the preseason chassis |
| **R401\*/R402\*** | 399 / 421 | ≥2 ROBOT SIGNS per robot, ≥6.5 in × 2.5 in, 90° apart, robust material, solid red/blue rectangle, **unpowered** |
| **R501\*** | 484 | **Closed** motor allowlist, Table 12-1. Re-gearing is explicitly permitted. COTS-sensor motors **do not count** toward R503 |
| **R502\*** | 534 | Servo restrictions + Table 12-2 (**open** list, spec-tested) |
| **R503\*** | 591 | **8 motors + 8 servos, summed across all configurations at an event.** Reinforced at inspection by **I302\*** |
| **R601\*** | 650 | Exactly 1 approved **12V NiMH** main battery from **closed Table 12-4** (7 items); 20 A ATM mini blade fuse; XT30/Powerpole connectors permitted |
| **R602\*** | ~688 | Other batteries only for isolated self-contained peripherals/LEDs |
| **R608** | 783 | Non-actuator active electrical items are restricted — check before buying LEDs/accessories |
| **R609 / R610** | §6.7–6.8 of `LEGAL-PARTS-CONSTRAINTS.md` | Wire sizing (Table 12-8) and **mandated wire colours** — an inspection item; read before buying spools |
| **R701\*** | 911 | One ROBOT CONTROLLER: **A** REV Control Hub `REV-31-1595`, **or B** Android smartphone + REV Expansion Hub `REV-31-1153`. Phone path still legal. **Plus C: *"no more than one additional REV Expansion Hub"*** — one spare hub per robot is the legal ceiling. **⚠ The rule's own note warns the Control Hub *"is the only officially supported ROBOT CONTROLLER device"*** and that teams choosing a smartphone *"are responsible for testing and verifying its compatibility"* — **[J] legal ≠ supported; do not put the B team on the phone path to save money** |
| **R505\*** | ~621 | **Closed list of power regulating devices, Table 12-3.** All actuator control signals must originate from one, except servos/fans/motors integral to sensors or COTS computing devices allowed by R501. **Includes `Studica Servo Power Block 75005`, easily missed. See §A5.2 — the text dump mis-states two limits** |
| **R702\*** | 932 | Coprocessor software may not be altered except programmable vision coprocessors in **Table 12-9**, which are reprogrammable. **Table 12-9 has exactly ONE row: Limelight Vision Limelight 3A `LL_3A`.** Example 6 **prohibits** the **OpenMV Cam, Luxonis OAK-1 and Limelight 3G**. Examples 1–5 **allow** BNO055, SparkFun OTOS, OctoQuad FTC Edition, optical-flow sensors, HuskyLens, Pixy2 as ordinary coprocessors |
| **R704** | 980 | Wi-Fi/bandwidth restrictions on the ROBOT CONTROLLER network — constrains the event-day tuning/telemetry workflow. See `LEGAL-PARTS-CONSTRAINTS.md` §5.5 |
| **R801\*** | 1119 | **No pneumatic actuators, high-speed blowers, or vacuums.** Only sealed, manufacturer-pre-charged COTS closed-air systems (gas shocks). **No suction intakes** |
| **E511\*** | §5, line 362 | Charging: *"Never charge batteries on a battery charger that exceeds a 3-amp average channel current"* — drives charger count for two robots |

---

## A5. Verification log — URLs loaded in this session (2026-08-21)

**Every SKU, price and stock string quoted in this file as VERIFIED came from one of these pages.** All prices are **US list, as of August 2026, VERIFY-BEFORE-ORDER.**

| URL | Loaded OK? | What was read |
|---|---|---|
| [gobilda.com/ftc-kits](https://www.gobilda.com/ftc-kits) | ✅ | FTC Starter Kit 2026-2027 Season **`3200-4008-2627` $899.99 In Stock**; Upgrade Pack **`3200-0101-2627` $249.99 In Stock**; 2-Stage Viper-Slide Kit (Belt-Driven, 336 mm) **`3210-0003-0002` $159.99 In Stock**; 4-Stage 240 mm **`3210-0004-0004` $219.99**; 4-Stage 336 mm **`3210-0003-0004` $229.99**; Linear Actuator Kit 203 mm **`3212-0001-0001` $129.99**; Strafer Chassis Kit **`3209-0001-0007` $699.99**; BeeLine Chassis Kit V2 **`3209-0002-0002` $649.99**; 8 mm REX Shaft Starter Pack **`3201-0008-0001` $199.99**; Intake Wheel Starter Pack **`3201-0014-0001` $159.99**; Servo Starter Pack **`3201-0007-0001` $309.99**; M4 Socket Head Assortment **`3201-0004-0001` $54.99 "OUT OF STOCK"**; channel/standoff/spacer bundles |
| [gobilda.com/hardware-bundles/](https://www.gobilda.com/hardware-bundles/) | ✅ | M4 Hardware Starter Pack (2,625 pcs) **`3201-0010-0001` $139.99 in stock**; M4 Button Head Assortment **`3201-0004-0002` $54.99**; goRAIL Bracket Assortment **`3201-0003-0001` $159.99**; 1501 Standoffs Bundle **`3203-1501-0001` $139.99**; 8 mm REX Standoff Bundle **`3203-1516-0001` $119.99**; 2803 Threaded Plates **`3203-2803-0001` $54.99**; M5 Set-Screw Bundle **`3203-2806-0001` $14.99**; 2807 Shims **`3203-2807-0001` $14.99**; 12-Piece Tool Set for M4 **`3201-0015-0001` $69.99**; 1502 Spacers **`3203-1502-0001` $46.99**; M4 Socket Head **`3201-0004-0001` "OUT OF STOCK"** (2nd confirmation) |
| [gobilda.com/battery-chargers/](https://www.gobilda.com/battery-chargers/) | ✅ | 12V Battery Charger **`3101-0012-0001` $14.99** "NiCad/NiMH, XT30 Connector"; 6V Charger **`3101-0006-0001` $14.99**; Hitec RDX2 200 **`44370` $139.99**; 20V Li-ion **`3101-1020-0001` $29.99**. **Stock strings and charge current not stated on the category page** |
| [gobilda.com/hardware/](https://www.gobilda.com/hardware/) | ✅ (subcategories only) | Subcategory list confirmed (Screws, Washers, Nuts, Springs, Standoffs & Spacers, Collars, Tools, Thread Locker, Hardware Bundles, …). **No product rows rendered — FAMILY-ONLY** |
| [gobilda.com/batteries/](https://www.gobilda.com/batteries/) | ✅ (subcategories only) | Subcategories: 6V / 12V / 20V Batteries, Battery Chargers, Battery Testers, Battery Mounts & Trays. **No product rows rendered — FAMILY-ONLY** |
| [revrobotics.com/rev-31-1595/](https://www.revrobotics.com/rev-31-1595/) | ✅ | **Control Hub `REV-31-1595` $375.00 "In Stock & Ready To Ship!"** |
| [revrobotics.com/rev-31-1302/](https://www.revrobotics.com/rev-31-1302/) | ✅ | **12V Slim Battery `REV-31-1302` $60.00 "In Stock & Ready To Ship!"**, 3000 mAh, XT30, 16 AWG, 20 A ATM fuse. **Chemistry NOT stated on the page — resolved by Table 12-4 [C]** |
| [revrobotics.com/ftc/discounts/](https://www.revrobotics.com/ftc/discounts/) | ✅ | *"15% discount on select items for every registered team"*; *"Only the products listed in this specific discount category are eligible"*; code from the FIRST Dashboard or Team Registration Form; **"Discount codes expire May 31, 2027"** |
| `gobilda.com/gobilda-ftc-starter-kit-2026-2027-season/` | ❌ **HTTP 404** | Deep product URL. **Evidence for the "prefer category URLs" rule (§0.2 rule 3)** |
| Web search for "goBILDA FTC Starter Kit 3200-4008-2627" | ⚠️ **wrong data** | Returned `3200-4008-2627` as the *Upgrade Pack* SKU. **Contradicted by the category page. Never take a SKU from a search snippet (B6 step 5)** |

**Carried forward as VERIFIED-UPSTREAM from `reference/VENDOR-ECOSYSTEMS.md` §5–§6 (which logs its own URLs, read 2026-08-21):** goBILDA 25% FIRST team discount and $50 international flat rate; AndyMark *"Orders received by 7-August-2026 will begin shipping after kickoff, beginning Monday, 14-September, 2026"* and *"All sales are final"*; Expansion Hub `REV-31-1153` **Out of Stock**; Servo Power Module `REV-11-1144` **Discontinued**; goBILDA `3100-0012-0020` 12V NiMH $64.99; Studica site **HTTP 403**; goBILDA/REV shipping pages **HTTP 404**.

### A5.1 Re-verification pass — 2026-08-22

**Every VERIFIED row above was re-fetched one day later. Result: zero SKU changes, zero price changes, zero stock-status changes.** A BOM this stable one day out is *not* evidence it will be stable on kickoff day — re-run B6 anyway (§B6 is mandatory, not advisory).

| URL | Loaded OK? | Result vs 2026-08-21 |
|---|---|---|
| [gobilda.com/ftc-kits](https://www.gobilda.com/ftc-kits) | ✅ | **UNCHANGED.** Starter Kit `3200-4008-2627` $899.99 In stock; Upgrade Pack `3200-0101-2627` $249.99 In stock; Viper-Slide `3210-0003-0002` $159.99, `3210-0004-0004` $219.99, `3210-0003-0004` $229.99; Strafer `3209-0001-0007` $699.99; BeeLine V2 `3209-0002-0002` $649.99 — all In stock. **The 08-21 adjudication of the bad search snippet holds** |
| [gobilda.com/hardware-bundles/](https://www.gobilda.com/hardware-bundles/) | ✅ | **UNCHANGED.** `3201-0010-0001` $139.99 In stock; `3201-0004-0002` $54.99 In stock; `3201-0003-0001` $159.99 In stock; `3201-0015-0001` $69.99 In stock. **`3201-0004-0001` still "OUT OF STOCK"** — third confirmation, now across two days |
| [gobilda.com/battery-chargers/](https://www.gobilda.com/battery-chargers/) | ✅ | **UNCHANGED.** `3101-0012-0001` $14.99; `3101-0006-0001` $14.99; `3101-1020-0001` $29.99; `44370` $139.99. **Amperage still not stated for any of them** — the E511 3 A test remains unresolvable from the category page |
| [revrobotics.com/rev-31-1595/](https://www.revrobotics.com/rev-31-1595/) | ✅ | **UNCHANGED.** `REV-31-1595` **$375.00**, *"In Stock & Ready To Ship!"* |
| [revrobotics.com/rev-31-1302/](https://www.revrobotics.com/rev-31-1302/) | ✅ | **UNCHANGED.** `REV-31-1302` **$60.00**, *"In Stock & Ready To Ship!"*, 3000 mAh / XT30 / 16 AWG / 20 A ATM. **Chemistry still not stated** — still resolved by Table 12-4 **[C]** |
| [revrobotics.com/rev-31-1153/](https://www.revrobotics.com/rev-31-1153/) | ✅ | **NEW PRICE CAPTURED:** Expansion Hub `REV-31-1153` **$275.00**, page schema availability **`OutOfStock`** (no verbatim "Out of Stock" string rendered in the main product area). Prior sessions logged the stock state but **not** the price. Confirms the **[J] "~$550 across two robots"** figure in `preseason-standing-order.md` §9 |
| [firstinspires.org/robotics/ftc/pricing-and-payment](https://www.firstinspires.org/robotics/ftc/pricing-and-payment) | ✅ | **NEW, 2026-27 SEASON:** FTC *"**$350**/season registration"* and supporting materials *"**$1,500**/estimated"*. **[O-FTC]** Page does **not** publish per-kit storefront prices |
| [info.firstinspires.org/…/ftc-storefront-options.pdf](https://info.firstinspires.org/hubfs/web/program/ftc/ftc-storefront-options.pdf) | ✅ **(via `pdftotext`)** | **Revision 25-26.4, Feb 18 2026 — [H] prior season (DECODE).** Registration **$325**; Driver Kit **$285**; Electronics Kit **$325**; Build Kit **$650**; each *"Limit one per register team per season"* (sic). **WebFetch returned raw binary — the text came from local `pdftotext -layout`. Note the technique: a FIRST PDF that WebFetch cannot read is still readable** |

**Rule re-greps run 2026-08-22 against `sections/12_RobotConstruction_R_p64-88.txt` and `sections/05_EventRules_E_p33-42.txt`** — every rule id cited anywhere in this file was confirmed to exist and to say what is claimed: **R102, R104** (*"There is no ROBOT weight limit"*), **R105, R301, R302, R303** (incl. subclauses **A** linear slide kit, **G** single DoF gripper, and the exception **J** *"dead-wheel odometry kits"*), **R401, R402, R501** (both carve-outs: *"These motors do not count toward the limit in R503"*), **R502, R503** (*"limited to a total of 8 motors and 8 servos … for all MECHANISMS used in all configurations"*), **R601** (*"1 and only 1 approved 12V NiMH main battery"*, *"COTS equivalent in-line 20A ATM mini blade fuse"*), **R701** (**A** `REV-31-1595` / **B** Android + `REV-31-1153`, plus **C** *"no more than one additional REV Expansion Hub"*), **R702, R704, R801**, and **E511** (*"Never charge batteries on a battery charger that exceeds a 3-amp average channel current"*). **Table 12-4** confirmed to name both `3100-0012-0020` and `REV-31-1302`.

### A5.2 ⚠ The plain-text section dumps corrupt tables — read tables from the PDF

**This was found on 2026-08-22 and it is the most dangerous thing in this appendix,** because it produces a *confident, plausible, wrong* legality claim — exactly the failure mode §0.2 exists to prevent.

**Table 12-3 (Power Regulators and Limits) is shifted by one row** in `sections/12_RobotConstruction_R_p64-88.txt`. The plain text renders the **REV Robotics Servo Hub `REV-11-1855`** with a load limit of *"2 Motors per Device"* — which is both wrong and semantically absurd for a servo device. Extracted from the PDF with PyMuPDF, the true table is:

| Power Regulating Device | Part Number | Load Limit per Device |
|---|---|---|
| goBILDA 6V Servo Power Injector | `3125-0001-0001` | 2 Servos per Port |
| REV Control Hub or Expansion Hub **Motor** Ports | `REV-31-1153` / `REV-31-1595` | **2 Motors per Port** |
| REV Control Hub or Expansion Hub **Servo** Ports | `REV-31-1153` / `REV-31-1595` | **2 Servos per Port** |
| REV Servo Power Module | `REV-11-1144` | 2 Servos per Port |
| **REV Robotics Servo Hub** | **`REV-11-1855`** | **2 Servos per Port** ← *not "Motors per Device"* |
| **REV SPARKmini** | **`REV-31-1230`** | **2 Motors per Device** ← *the row the limit actually belongs to* |
| **Studica Servo Power Block** | **`75005`** | 2 Servos per Port |

**Two corrections this forces on the workspace:**

1. **`Studica Servo Power Block 75005` is a legal power regulating device and was missing from the expander list** used across this workspace (which carried only the four REV/goBILDA parts). It is now added to `PROMPTS-bom.md` **P3 test 10**. Studica's site returns **HTTP 403**, so it is **MANUAL-SKU** for legality **[C]** and **[U]** for price.
2. The table is **closed**: apart from servos, fans and motors integral to sensors or COTS computing devices permitted in **R501**, *all* actuator control signals must originate from a device in this table.

**Re-derive it yourself before trusting any table in a BOM (Table 12-3 sits on PDF page index 76):**

```bash
python -c "import pymupdf; [print(r) for r in pymupdf.open('manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf')[76].find_tables().tables[0].extract()]"
```

> **[J] Generalise this.** The same shifting is visible around the **R304 / R305** labels, where `R305` renders beside R304's heading and the *"SCORING ELEMENTS are not allowed for ROBOT construction"* body lands under the wrong id. **The section text dumps are reliable for prose and rule bodies, and unreliable for tables and for rule ids at page/table boundaries.** Since Tables **12-1** (motors, closed), **12-2** (servos), **12-4** (batteries) and **12-9** (coprocessors) are all load-bearing for a BOM, **verify any limit or spec column against the PDF before citing it**. `tools/extract-tables.py` exists for this.

**2026-27 FIRST storefront kit prices — partially resolved.** The 25-26 figures are pinned to a revision-stamped primary source (**$325 registration / $285 Driver Kit / $325 Electronics Kit / $650 Build Kit**, limit one each per registered team). The **26-27** figures published on the firstinspires.org Cost & Registration page are **$350 / $295 / $350 / $660** (see `research/SMALL-TEAM-ECONOMICS.md` §3.1, which sets the two seasons side by side). The storefront **PDF** is still stamped Rev 25-26.4 and is stale — **budget from the website, not the PDF**, and confirm on the Team Dashboard, which is login-gated and cannot be fetched here.

---

*End of BOM-PROTOCOL.md. Templates: `tools/bom/BOM.template.csv`, `tools/bom/PROMPTS-bom.md`, `tools/bom/preseason-standing-order.md`.*
