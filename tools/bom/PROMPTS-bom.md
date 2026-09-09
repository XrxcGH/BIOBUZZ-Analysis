# PROMPTS — BOM generation and audit

### Copy-paste prompts for the kickoff-day parts workflow. One prompt per job. Every one is self-contained.

**Built:** 2026-08-21 (pre-kickoff) | **Season:** 2026-27 BIOBUZZ presented by RTX | **Kickoff:** 2026-09-12
**Procedure these implement:** `reference/BOM-PROTOCOL.md` (**PHASE B**, steps B1–B7)
**Upstream prompt pack:** `reference/REVIEW-PROMPTS-STRATEGY.md` (**PHASE D**, steps D0–D8). **This pack starts where that one ends** — D5 feeds B1. Same convention: one copy-paste prompt per step; **if step ids are renumbered, renumber both packs together.**
**Output schema:** `tools/bom/BOM.template.csv` (23 columns — field dictionary in `BOM-PROTOCOL.md` §A2, restated in §0.3 below)
**Artifact root:** `analysis/kickoff/`, one file per step; log appends to `analysis/DECISION-LOG.md` (append-only).

---

## 0. How to use this file

### 0.1 Which prompt for which step

| Prompt | Implements | Use when |
|---|---|---|
| [P1 Decompose a design into mechanisms](#p1--decompose-a-design-into-mechanisms) | **B1** | You have an approved design proposal and no mechanism list |
| [P2 Generate a BOM from a design proposal](#p2--generate-a-bom-from-a-design-proposal) | **B2–B5** | You have a mechanism list and need the parts list |
| [P3 Legality-check this parts list](#p3--legality-check-this-parts-list) | **B2** (re-run) | Before every order; after every Thursday Team Update; after any Q&A answer |
| [P4 Find the cheaper equivalent](#p4--find-the-cheaper-equivalent) | **B5** | The BOM is over budget, or one line is disproportionate |
| [P5 Two-robot quantity check](#p5--two-robot-quantity-check) | **B3–B4** | Before every order, without exception |
| [P6 Verify these SKUs](#p6--verify-these-skus) | **B6** | **Immediately before ordering. Mandatory.** |

### 0.2 The contract every prompt enforces

Each prompt below repeats these rules inline so it works pasted alone into a fresh session. They are restated here so a human reviewing output knows what to check:

1. **No SKU or price may be stated unless a vendor page was actually loaded in that session and read.** No "from memory," no search-result snippets, no "typically around $X."
2. **Unverified parts are named by PRODUCT FAMILY plus the verified CATEGORY URL, and stamped `NEEDS-SKU-CHECK`.**
3. **Every price is date-stamped "as of <date>" and marked `VERIFY-BEFORE-ORDER`.**
4. **Every row carries a confidence tag:** `VERIFIED` / `VERIFIED-UPSTREAM` / `MANUAL-SKU` / `FAMILY-ONLY` / `UNVERIFIED`.
5. **Every legality claim cites an R-rule ID that was grepped from the V0 text**, not recalled.
6. **Blocked or 404 vendor sites are reported explicitly**, never silently skipped.
7. **Prefer vendor category/collection URLs over deep product URLs** — deep links rot.

### 0.3 The CSV schema all prompts emit

```
row_type,line_id,mechanism,item,vendor,product_family,sku,qty_per_robot,spares_qty,
qty_total,unit_cost_usd,extended_cost_usd,buy_or_fab,confidence,lead_time_days,
long_lead_flag,legality_rule_id,stock_status_string,stock_checked_date,verify_url,
ordered_status,po_ref,notes
```

`qty_total = (qty_per_robot × 2) + spares_qty`, except for shared bench items where `qty_per_robot = 0` and `qty_total` is the true count.

---

## P1 — Decompose a design into mechanisms

```text
You are working inside the FTC 2026-27 BIOBUZZ review workspace at
ROOT = "C:/Users/ericj/Documents/BIOBUZZ Analysis".

CONTEXT YOU MUST LOAD FIRST (read these files before answering):
  ROOT/reference/BOM-PROTOCOL.md            <- the procedure; you are executing Step B1
  ROOT/reference/STRATEGY-RANKING-PROTOCOL.md <- the UPSTREAM phase. Your input is its D5 ranked
                                               recommendation list (§8.4) as filtered by the D8
                                               vote (§11.2). Read its §0.2 evidence labels and its
                                               §0.4 honesty rules - they bind this step too.
  ROOT/reference/ROBOT-ARCHETYPE-LIBRARY.md <- archetype profiles and the kickoff workflow
  ROOT/reference/KEYWORD-GLOSSARY.md        <- use the manual's own vocabulary
  ROOT/reference/LEGAL-PARTS-CONSTRAINTS.md <- the purchasing envelope, esp. §3 (the 8+8 budget)
  ROOT/manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt  <- legality source of truth

TEAM CONTEXT: ~15 students, TWO registered FTC teams (A team + B team), TWO robots, modest budget,
3D printers and hand tools only (no CNC mill), limited mentor hours. Every mechanism gets built TWICE.

THE DESIGN PROPOSAL:
<<<PASTE THE D8 DECISION BRIEF, OR THE APPROVED DESIGN PROPOSAL, HERE>>>
ROBOT: <<<A robot / B robot / BOTH>>>
D7 FALLBACK CANDIDATE (if known): <<<candidate id and switch cost>>>

TASK — decompose this proposal into its MAJOR MECHANISMS.

Produce a numbered mechanism list using the standard slots in BOM-PROTOCOL.md §B1 step 2
(M1 drivetrain, M2 odometry, M3 intake, M4 transfer, M5 extension/lift, M6 end effector,
M7 endgame, M8 electrical/control, M9 sensing/vision, M10 structure, M11 compliance).
Omit slots this design genuinely does not need, and say why you omitted each one.
M8, M10 and M11 are ALWAYS present - do not omit them because they are unglamorous.

For each mechanism give a table row with:
  | # | Mechanism | Scoring action it serves | Motors | Servos | DEFERRED-R105? | Notes |

RULES:
- Every mechanism MUST name the specific scoring action it serves. A mechanism that serves no
  scoring action is a cut candidate - flag it as such, do not silently keep it.
- Fill the mandatory R503 8+8 worksheet (BOM-PROTOCOL.md §B2 step 5) and show the running totals.
  R503 limits the ROBOT to 8 motors and 8 servos across ALL MECHANISMS in ALL configurations used
  at a single event. If the design exceeds either, say so plainly and name which mechanism to cut.
  NOTE: DECODE 2025-26 allowed 10 servos; BIOBUZZ allows 8. Carried-over designs may now be illegal.
- Mark DEFERRED-R105 = yes on any mechanism whose SIZE is the design variable (slide stage count,
  arm length, telescoping reach). R105 states the expansion sizing constraints "will be released at
  Kickoff" - do not guess them and do not let a length-dependent choice into the list.
- R102 IS known now: STARTING CONFIGURATION is limited to an 18 x 18 x 18 inch cube.
- R104: there is NO robot weight limit in BIOBUZZ. Do not recommend anything for weight reasons.
- R801: NO pneumatic actuators, NO high-speed blowers, NO vacuums/suction. Only sealed COTS
  closed-air systems pre-charged by the manufacturer (e.g. gas shocks). Do not propose suction
  intakes or pneumatic cylinders.
- Cite a rule ID for every legality claim and confirm it by grepping the Section 12 text. If you
  cannot find the rule text, say "could not confirm" rather than asserting.
- Label every claim [C] CONFIRMED-BIOBUZZ / [H] HISTORICAL / [D] DERIVED / [J] JUDGMENT.

DO NOT name any specific part, SKU or price in this step. That is Step B2/P2's job.

OUTPUT: the mechanism table, then the 8+8 worksheet, then a short "cut candidates" list.
```

---

## P2 — Generate a BOM from a design proposal

```text
You are working inside the FTC 2026-27 BIOBUZZ review workspace at
ROOT = "C:/Users/ericj/Documents/BIOBUZZ Analysis".

CONTEXT YOU MUST LOAD FIRST (read all of these before answering):
  ROOT/reference/BOM-PROTOCOL.md            <- the procedure; you are executing Steps B2-B5
  ROOT/reference/VENDOR-ECOSYSTEMS.md       <- vendor profiles, interoperability map (§3),
                                               procurement reality (§5), standing order (§6)
  ROOT/reference/LEGAL-PARTS-CONSTRAINTS.md <- motors §2, the 8+8 budget §3, servos §4,
                                               electronics §5, power §6, pneumatics §7,
                                               fabrication-vs-COTS §8
  ROOT/reference/mechanisms/DRIVETRAIN-AND-ODOMETRY.md
  ROOT/reference/mechanisms/INTAKE-AND-MANIPULATION.md
  ROOT/reference/mechanisms/EXTENSION-ARMS-LIFTS.md
  ROOT/reference/mechanisms/LAUNCHERS-AND-FEEDING.md
  ROOT/reference/mechanisms/ELECTRONICS-AND-SENSING.md
  ROOT/reference/mechanisms/IN-HOUSE-FABRICATION.md
     ^ if reference/mechanisms/ does not exist yet, SAY SO explicitly and fall back to
       VENDOR-ECOSYSTEMS.md §6 and ROBOT-ARCHETYPE-LIBRARY.md. Do not invent its contents.
  ROOT/reference/ACHIEVABILITY-FACTORS.md   <- the factor model incl. DUPLICABILITY
  ROOT/playbook/TWO-ROBOT-PROGRAM.md        <- §5.2 shared-vs-duplicated BOM (authoritative split)
  ROOT/research/SMALL-TEAM-ECONOMICS.md     <- §2 the three budget tiers
  ROOT/tools/bom/BOM.template.csv           <- the exact output schema
  ROOT/manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt  <- legality source of truth

TEAM CONTEXT: ~15 students, TWO registered FTC teams, TWO robots, modest budget, 3D printers and
hand tools only (no CNC mill, no lathe), limited mentor hours. EVERY mechanism is built TWICE:
quantities, cost and lead time all double, and duplicability is a first-class design factor.

THE DESIGN PROPOSAL / MECHANISM LIST:
<<<PASTE THE APPROVED DESIGN PROPOSAL, OR THE P1 MECHANISM TABLE, HERE>>>
BOM IS FOR: <<<A robot / B robot / BOTH>>>
BUDGET CEILING FOR THIS BOM: <<<$X, or "unstated">>>

TASK — produce an orderable BOM.

STEP B2: for each mechanism select ONE variant from the catalogs above.
  - Record WHY in one sentence containing a COMPARISON, not a preference, and naming the
    ACHIEVABILITY-FACTORS.md factor it turns on (duplicability at minimum).
  - Record the RUNNER-UP and a concrete SWITCH TRIGGER ("if <SKU> is out of stock, use <X>").
  - Legality-check every line and put the rule ID in legality_rule_id. The five tests that
    actually reject parts: R301 (COTS major mechanisms purpose-built for a game task are
    prohibited; exceptions are COTS drive CHASSIS and official StarterBot mechanisms),
    R303 (COTS must be single DoF; allowed A-G incl. linear slide kit, linear actuator kit,
    non-shifting gearbox, pulley, turntable, lead screw, single-DoF gripper; exceptions H-K incl.
    ratchets, holonomic wheels, dead-wheel odometry kits), R501/R502/R503 (closed motor allowlist
    Table 12-1; servo requirements Table 12-2; 8 motors + 8 servos total across ALL configurations),
    R601/R701/R702 (1 approved 12V NiMH main battery from the CLOSED Table 12-4 list; one ROBOT
    CONTROLLER per R701; coprocessors per R702/Table 12-9), R801 (NO pneumatics, blowers or vacuums).
  - Include the mandatory R503 8+8 worksheet with running totals. It must total <= 8 and <= 8.
  - Check the interoperability map (VENDOR-ECOSYSTEMS.md §3) before mixing vendors. Do not
    silently mix structural ecosystems - two robots that share no spares defeats the program.

STEP B3: split BUY vs FABRICATE per line and apply the duplicability lens (D1-D5 in
BOM-PROTOCOL.md §B3): can we buy two today, can we make two, will the two match, does the B
robot need it, does it plug into a robot or sit on a bench. Fabricate geometry; buy precision and
buy legality. A bought multi-DoF gripper is illegal (R303); a fabricated one is legal (R302).

STEP B4: quantities. qty_total = (qty_per_robot x 2) + spares_qty, except shared bench items
(qty_per_robot = 0). Apply the spares policy in BOM-PROTOCOL.md §A1. Run a SEPARATE fastener and
bearing sweep - for every mechanism ask what bolts it on and what the shaft turns in. Set
long_lead_flag = Y per the tests in §B4 step 4 and sort long-lead lines to the top.

STEP B5: cost it. Show three totals - list, after discounts (goBILDA 25% "nearly every product
storewide"; REV 15% "select items"), and +10% for shipping and sales tax. SUBTOTAL BY MECHANISM,
never by vendor. Compare to the SMALL-TEAM-ECONOMICS.md §2 tiers. If over the ceiling, name the
specific cut lines using the ranked cut ladder in §B5 step 4, and NEVER propose cutting batteries,
spare motors/servos, fasteners, or compliance items (§B5 steps 5-6).

ANTI-HALLUCINATION CONTRACT - THIS IS THE MOST IMPORTANT PART OF THIS PROMPT:
- Do NOT state any SKU or price unless you loaded the vendor page with a fetch tool IN THIS SESSION
  and read it. No exceptions and no "from memory". Never take a SKU from a search-result snippet.
- When you have not verified a specific part, name the PRODUCT FAMILY, link the vendor CATEGORY
  page you did verify, leave the sku column BLANK, and mark the row FAMILY-ONLY / NEEDS-SKU-CHECK.
  A verified family plus an unverified SKU is honest; an invented SKU is not.
- Date-stamp every price "as of <today>" and mark it VERIFY-BEFORE-ORDER.
- Prefer vendor category/collection URLs over deep product URLs; deep links rot.
- If a vendor site blocks or 404s, SAY SO explicitly in the notes column and fall back to family only.
- Tag every row: VERIFIED (page read this session) / VERIFIED-UPSTREAM (copied from a workspace
  catalog that logs its own URL) / MANUAL-SKU (from a V0 manual table you grepped) / FAMILY-ONLY /
  UNVERIFIED. Rows tagged UNVERIFIED may not be ordered.
- Label every non-parts claim [C] / [H] / [D] / [J].
- Cover these vendors and say which are official FIRST suppliers vs general suppliers: goBILDA,
  REV Robotics, AndyMark, ServoCity/Actobotics, Studica, and the FIRST Tech Challenge storefront.

OUTPUT, in this order:
  1. The R503 8+8 worksheet with running totals.
  2. The BOM as CSV matching ROOT/tools/bom/BOM.template.csv exactly (23 columns, same order).
  3. A markdown table of the same data grouped by mechanism, for humans to read.
  4. Cost rollup: list -> discounted -> +10% landed, subtotalled by mechanism, tier compared.
  5. The long-lead / order-first list, as PO #1.
  6. An explicit "NEEDS-SKU-CHECK register" listing every line that must be resolved at Step B6.
```

---

## P3 — Legality-check this parts list

```text
You are working inside the FTC 2026-27 BIOBUZZ review workspace at
ROOT = "C:/Users/ericj/Documents/BIOBUZZ Analysis".

CONTEXT YOU MUST LOAD FIRST:
  ROOT/manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt  <- THE SOURCE OF TRUTH.
      Section 12 (ROBOT Construction Rules, R) is ALREADY FINAL for BIOBUZZ. Use this text, never
      prior-season memory. Prior-season manuals in ROOT/manuals/_reference_prior_seasons/ are
      HISTORICAL only and several rules HAVE CHANGED.
  ROOT/reference/LEGAL-PARTS-CONSTRAINTS.md  <- the analysed purchasing envelope
  ROOT/reference/CONSTRUCTION-RULES-R.md     <- full R-rule detail
  ROOT/reference/BOM-PROTOCOL.md             <- §B2 (the five tests) and §A4 (rule cross-reference)

THE PARTS LIST TO CHECK:
<<<PASTE THE BOM OR PARTS LIST HERE>>>

TASK — audit every line for legality and return a verdict per line.

For each line return: | line | verdict | rule ID | quoted rule text | what to do |
Verdicts: LEGAL / ILLEGAL / CONDITIONAL (legal only if X) / CANNOT-CONFIRM.

RUN THESE TESTS IN ORDER, and GREP THE SECTION 12 TEXT TO CONFIRM EACH RULE SAYS WHAT YOU CLAIM:

1. R301 - is this a COTS MAJOR MECHANISM purpose-built to complete a game task? Those are
   PROHIBITED. The only exceptions are (A) COTS drive CHASSIS and (B) COTS major mechanisms
   created as part of the official FIRST StarterBots. Note the rule also targets vendors selling
   "build to print" manufacturing of publicly available purpose-built solutions.
2. R303 - does this COTS component or mechanism exceed a single degree of mechanical freedom?
   Allowed single-DoF examples: A linear slide kit, B linear actuator kit, C single-speed
   (non-shifting) gearboxes, D pulley, E turntable, F lead screw, G single-DoF gripper.
   Exceptions: H ratcheting devices, I holonomic wheels (omni or mecanum), J dead-wheel odometry
   kits, K items transferring motion between misaligned components. A BOUGHT multi-DoF gripper is
   illegal; a FABRICATED one is legal under R302.
3. R501 + Table 12-1 - is every motor on the CLOSED allowlist? The rule says "The only allowed
   motor actuators are". Check the exact part number against the table. Also capture the carve-out:
   motors integral to an unmodified COTS sensor (e.g. LIDAR) and vibration/autofocus motors inside
   COTS computing devices DO NOT count toward R503.
4. R502 + Table 12-2 - does every servo meet the requirements? Table 12-2 is an OPEN list
   ("including, but not limited to") but is spec-tested. Check power/controller requirements too.
5. R503 - total the motors and servos across ALL MECHANISMS in ALL configurations used at a single
   event. The limit is 8 motors and 8 servos. Show the arithmetic. NOTE: DECODE 2025-26 allowed 10
   servos; BIOBUZZ allows 8 - this is a REDUCTION and carried-over designs may now be ILLEGAL.
   Inspection rule I302 re-checks this, including spare mechanisms in the pit.
6. R601 + Table 12-4 - is the main battery on the CLOSED 7-item legal list? Exactly 1 approved 12V
   NiMH main battery, unaltered except (A) the fuse may be replaced with a COTS equivalent in-line
   20A ATM mini blade fuse and (B) connectors may be replaced with Anderson Powerpole, XT30 or
   comparable. R602 governs other batteries for isolated self-contained peripherals only.
7. R701 - exactly one ROBOT CONTROLLER: (A) a REV Control Hub REV-31-1595, or (B) an Android
   smartphone connected to a REV Expansion Hub REV-31-1153. The phone path IS still legal this
   season. R701 also limits additional Expansion Hubs - quote the limit.
8. R702 + Table 12-9 - coprocessor software may not be altered, except programmable vision
   coprocessors natively supported by the FTC SDK. Check the specific device against Table 12-9,
   including any device the table explicitly PROHIBITS.
9. R801 - NO pneumatic actuators, high-speed blowers, or vacuums. Only sealed COTS closed-air
   systems pre-charged by the manufacturer (e.g. gas shocks). Flag any suction intake or pneumatic
   cylinder as ILLEGAL. Springs and constant-force springs are unrestricted.
10. Power regulating devices. Table 12-3 is titled "Power Regulators and Limits" and its third
    column is "Load Limit per Device". The rule that owns it states that, apart from servos/fans/
    motors integral to sensors or COTS computing devices permitted in R501, ALL actuator control
    signals must originate from a power regulating device, and the table is the CLOSED list of the
    only ones permitted on the ROBOT. Verify every expander against the table before approving.
    The table's entries are:
    Table 12-3 verbatim, extracted from the V0 PDF itself with PyMuPDF find_tables()
    (verified 2026-08-22 - see the warning below about the plain-text copy):
      Power Regulating Device                      | Part Number               | Load Limit per Device
      goBILDA 6V Servo Power Injector              | 3125-0001-0001            | 2 Servos per Port
      REV Control Hub or Expansion Hub Motor Ports | REV-31-1153 / REV-31-1595 | 2 Motors per Port
      REV Control Hub or Expansion Hub Servo Ports | REV-31-1153 / REV-31-1595 | 2 Servos per Port
      REV Servo Power Module                       | REV-11-1144               | 2 Servos per Port
      REV Robotics Servo Hub                       | REV-11-1855               | 2 Servos per Port
      REV SPARKmini                                | REV-31-1230               | 2 Motors per Device
      Studica Servo Power Block                    | 75005                     | 2 Servos per Port
    Report the table's actual limits, and note these traps:
      (a) The goBILDA injector is a 6V part - the manual names it "goBILDA 6V Servo Power Injector",
          so do not describe it as voltage-agnostic.
      (b) Studica Servo Power Block 75005 IS in the table and is commonly forgotten; Studica's site
          has returned HTTP 403, so treat its SKU as MANUAL-SKU (legality [C]) and its price as [U].
      (c) REV-11-1144 is in the table but reads Discontinued at REV - legal and unbuyable.
      (d) The Control Hub and Expansion Hub appear as TWO separate rows (motor ports, servo ports)
          with DIFFERENT limits. Cite the right row.
      (e) SPARKmini is the only "per Device" row and the only MOTOR row among the add-on regulators;
          every other add-on is servos-per-port.
    *** DO NOT read Table 12-3 out of the plain-text section dump. *** The pdftotext -layout copy
    in manuals/2026-27_BIOBUZZ/sections/ SHIFTS THIS TABLE BY ONE ROW, which swaps the limits for
    REV-11-1855 and REV-31-1230 - it shows the Servo Hub as "2 Motors per Device", which is wrong.
    The values above came from the PDF via PyMuPDF and are correct. If you need to re-derive them:
      python -c "import pymupdf; [print(r) for r in
        pymupdf.open('manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf')[76]
        .find_tables().tables[0].extract()]"
    Treat every OTHER manual table (12-1 motors, 12-2 servos, 12-4 batteries, 12-9 coprocessors) as
    carrying the same risk: confirm limit/spec columns against the PDF, not the text dump.
11. R401/R402 - are ROBOT SIGNS on the list at all? Minimum two per ROBOT, in at least 2 separate
    locations on opposite or adjacent surfaces 90 degrees apart, min 6.5 in wide x 2.5 in tall,
    robust material, supported by the frame, containing a solid red or blue opaque rectangle, and
    NOT powered. Missing signs is an inspection failure.
12. R609/R610 - wire sizing and MANDATED wire colours for the 12V main bus and +5V auxiliary bus.
    Colour is an inspection item, not a preference. Flag any wire purchase that ignores it.

ALSO REPORT SEPARATELY:
- Anything DEFERRED TO KICKOFF. R105 states expansion sizing constraints "will be released at
  Kickoff" - flag every line whose length or reach is a guess against unreleased numbers.
- Anything LEGAL BUT UNBUYABLE (named in a manual table but discontinued or out of stock).
  Legality and availability are two different columns.
- Anything you CANNOT CONFIRM. Say "could not confirm" rather than asserting.

RULES: quote the rule text verbatim for every verdict. Cite the rule ID and the line number in the
Section 12 file. Do NOT rely on prior-season memory. Do NOT invent SKUs or prices - if you need to
name a part you have not verified, name the family and mark it NEEDS-SKU-CHECK. Label claims
[C] CONFIRMED-BIOBUZZ / [H] HISTORICAL / [D] DERIVED / [J] JUDGMENT.
```

---

## P4 — Find the cheaper equivalent

```text
You are working inside the FTC 2026-27 BIOBUZZ review workspace at
ROOT = "C:/Users/ericj/Documents/BIOBUZZ Analysis".

CONTEXT YOU MUST LOAD FIRST:
  ROOT/reference/VENDOR-ECOSYSTEMS.md       <- vendor profiles, the INTEROPERABILITY MAP (§3),
                                               discounts (§5.4), the standing order (§6)
  ROOT/reference/LEGAL-PARTS-CONSTRAINTS.md <- the legality envelope any substitute must satisfy
  ROOT/research/SMALL-TEAM-ECONOMICS.md     <- §4 where cheap parts come from, §5.1 cuts ranked by
                                               damage, §5.2 THE THREE FALSE ECONOMIES
  ROOT/reference/BOM-PROTOCOL.md            <- §B5 the ranked cut ladder
  ROOT/manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt

TEAM CONTEXT: ~15 students, TWO registered FTC teams, TWO robots, modest budget, 3D printers and
hand tools only (no CNC mill). Every saving is doubled - and so is every compatibility mistake.

THE LINE(S) TO FIND AN ALTERNATIVE FOR:
<<<PASTE THE BOM LINE(S), INCLUDING CURRENT SKU, PRICE, QTY AND THE MECHANISM IT SERVES>>>
TARGET SAVING: <<<$X, or "as much as possible without losing capability">>>

TASK — for each line, propose alternatives ranked by (saving per unit of capability lost).

For each alternative return:
  | option | vendor | family / SKU | unit cost | ext. cost x2 | saving | capability lost |
  | legality rule ID | ecosystem-compatible? | confidence | notes |

CONSIDER THESE LEVERS, IN THIS ORDER:
1. FABRICATE INSTEAD OF BUY. R302 permits modifying legal COTS parts and raw materials (sheet
   stock, extruded shapes, metals, plastic, rubber, wood, magnets). With 3D printers and hand
   tools, brackets, mounts, trays, spacers, rollers, gripper fingers, guards and hoppers are all
   fabricable. State the print/cut time PER PART and multiply by the two-robot quantity - a cheap
   part that costs 40 printer-hours is not cheap for this program.
2. RE-GEAR RATHER THAN RE-BUY. Table 12-1 states legal gearmotors "may be used with or without the
   provided gearbox, and/or with any other compatible gearbox". Changing a ratio is legal and
   cheaper than a second motor family - and it protects two-robot spares commonality.
3. REPLACE A MOTOR WITH A ZERO-SLOT ACTUATOR. Springs, gas springs (R801.A permits sealed
   manufacturer-pre-charged closed-air systems), constant-force springs, over-centre linkages and
   ratchets (R303.H permits ratcheting devices) cost no R503 slot and no recurring dollars.
   Report the R503 slots freed as part of the saving - slots are as scarce as dollars.
4. A CHEAPER PART IN THE SAME ECOSYSTEM. Check the interoperability map first: shaft standards
   (§3.3), fasteners (§3.4) and the chain/belt hard wall (§3.5). A cheaper part that needs an
   adapter is not cheaper.
5. SECOND-SOURCE THE SAME PART. ServoCity's catalogue mirrors goBILDA's - check both domains
   before declaring a part unavailable or overpriced.
6. DISCOUNTS AND KITS. goBILDA gives registered FIRST teams 25% on "nearly every product
   storewide"; REV gives 15% on "select items"; the FIRST storefront sells control equipment,
   electronics and starter kits at negotiated prices with a LIMIT OF ONE PURCHASE PER ITEM PER
   CATEGORY PER SEASON - and TWO registered teams means TWO allocations. Check whether a kit is
   cheaper than the sum of its parts before proposing component substitutions.
7. SHARE INSTEAD OF DUPLICATE. Ask whether the item plugs into a robot (must duplicate) or sits on
   a bench (buy once). See TWO-ROBOT-PROGRAM.md §5.2.

HARD CONSTRAINTS ON ANY SUBSTITUTE:
- It must remain legal. Cite the rule ID and confirm by grepping Section 12. Motors must be on the
  CLOSED Table 12-1 list; batteries on the CLOSED Table 12-4 list; coprocessors in Table 12-9.
- It must not break the ecosystem commitment. Say explicitly if it introduces a second shaft,
  fastener, chain or belt standard.
- REFUSE to propose these three false economies (SMALL-TEAM-ECONOMICS.md §5.2), and say why if
  asked: cutting batteries, cutting spare motors/servos, cutting fasteners. Also refuse to cut
  compliance items (ROBOT SIGNS, grounding strap, main switch, correct wire colours).
- State the capability lost in plain language. "No capability lost" is a claim that needs a reason.

ANTI-HALLUCINATION CONTRACT:
- Do NOT state any SKU or price unless you loaded the vendor page IN THIS SESSION and read it.
  Never take a SKU from a search-result snippet.
- Unverified alternatives are named by PRODUCT FAMILY with the verified CATEGORY URL and marked
  FAMILY-ONLY / NEEDS-SKU-CHECK. An invented cheaper SKU is worse than no answer.
- Date-stamp every price "as of <today>" and mark VERIFY-BEFORE-ORDER.
- Tag every row VERIFIED / VERIFIED-UPSTREAM / MANUAL-SKU / FAMILY-ONLY / UNVERIFIED.
- If a vendor site blocks or 404s, say so explicitly.

OUTPUT: the ranked alternatives table, then a one-paragraph recommendation naming the single
substitution with the best saving-per-capability-lost, then the total saving across two robots,
then any R503 motor/servo slots freed.
```

---

## P5 — Two-robot quantity check

```text
You are working inside the FTC 2026-27 BIOBUZZ review workspace at
ROOT = "C:/Users/ericj/Documents/BIOBUZZ Analysis".

CONTEXT YOU MUST LOAD FIRST:
  ROOT/playbook/TWO-ROBOT-PROGRAM.md        <- §5.2 the AUTHORITATIVE shared-vs-duplicated split,
                                               §5.3 build sequencing, §5.4 ordering and lead times
  ROOT/reference/BOM-PROTOCOL.md            <- §B3 the duplicability lens D1-D5, §A1 spares policy,
                                               §M the ordering mistakes
  ROOT/reference/ACHIEVABILITY-FACTORS.md   <- the duplicability factor
  ROOT/reference/VENDOR-ECOSYSTEMS.md       <- §5.2 the demand-spike evidence, §5.6 the two-robot
                                               ordering protocol
  ROOT/manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt

TEAM CONTEXT: ~15 students, TWO registered FTC teams (A team + B team), TWO robots, modest budget.
EVERY mechanism is built TWICE. This check exists because ordering one of something needed on both
robots is the single most expensive clerical error this program can make.

THE BOM TO CHECK:
<<<PASTE THE BOM CSV OR TABLE HERE>>>

TASK — audit every quantity for the two-robot program and return corrections.

For every line return:
  | line | qty as written | qty it should be | why | multiplier class | verdict |
Verdicts: OK / UNDER-ORDERED / OVER-ORDERED / WRONG-CLASS / MISSING-SPARES / MISSING-ENTIRELY.

APPLY THIS TEST TO EVERY SINGLE LINE:
1. Does it PLUG INTO A ROBOT or SIT ON A BENCH? Duplicate what plugs into a robot; share what sits
   on a bench. This is the organizing principle from TWO-ROBOT-PROGRAM.md §5.2.
2. Check the arithmetic: qty_total = (qty_per_robot x 2) + spares_qty, except shared bench items
   where qty_per_robot = 0 and qty_total is the true count.
3. SORT THE BOM BY qty_total AND EXAMINE EVERY LINE THAT READS "1". Each one must be justified in
   writing as bench stock. An unjustified "1" is the M-1 failure mode.

APPLY THE MULTIPLIER CLASSES:
- MUST DUPLICATE (x2): ROBOT CONTROLLER (R701 - one per robot), OPERATOR CONSOLE (R901), main
  battery (R601 - each robot needs its own; each robot is a separate ROBOT), drivetrain motors and
  wheels, all mechanism motors and servos (R503 and inspection rule I302 - each robot independently
  meets the 8+8 cap; a shared pool does NOT create a shared allowance), ROBOT SIGNS (R401 - minimum
  two per robot, and both alliance colours).
- SHARE (x1): practice field, game set, 3D printer, hand and benchtop tools, CAD/code/scouting
  seats, bulk stock (channel, plate, fasteners, chain, belt, filament) bought as ONE order and split.
- DELIBERATELY OVER-ORDER: printed parts x3 full sets (A robot, B robot, spares); batteries 5-6
  across the program with 2-3 chargers (E511 caps a charger at a 3-amp average channel current, so
  one charger cannot turn packs around at a two-robot event); +1 spare drive motor; +2 spare servos;
  +1 spare gamepad; bearings x2 + 50%.

THEN CHECK FOR MISSING LINES - these are the ones teams forget:
- Fasteners and bearings. Run a separate sweep: for every mechanism, what bolts it to the robot and
  what does the shaft turn in? This sweep typically finds 10-20% more lines.
- Compliance items: ROBOT SIGNS (both colours), main power switch, grounding strap, correctly
  coloured wire per R609/R610, 20A ATM mini blade fuses (R601.A).
- Spare consumables: chain length, zip ties, servo horns, heat shrink.
- Cables: one servo extension per servo, plus spares.

THEN CHECK THE ORDERING SHAPE:
- Is every duplicated line in ONE order? Never "order A now, B later" - if a part stocks out
  between the two orders, robot B becomes a different robot and shares no spares with robot A.
  As of 2026-08-21, three weeks before kickoff, six goBILDA/REV items were already out of stock or
  discontinued (VENDOR-ECOSYSTEMS.md §5.2). This risk is real and measured, not hypothetical.
- Are long-lead lines pulled into a separate PO #1 to be placed within 48 hours of design approval?
- Is there ONE buyer, one cart, one card?

RULES:
- Cite the rule ID for every legality-driven quantity (R601, R701, R901, R503, I302, R401, E511)
  and confirm it by grepping the Section 12 text.
- Do NOT invent SKUs or prices. If a missing line needs a part you have not verified, name the
  PRODUCT FAMILY and mark it NEEDS-SKU-CHECK.
- Label claims [C] / [H] / [D] / [J].

OUTPUT: the corrections table, then a "MISSING ENTIRELY" list, then the corrected total line count
and corrected cost delta for two robots, then a one-line verdict: SAFE TO ORDER / DO NOT ORDER YET.
```

---

## P6 — Verify these SKUs

> **This is the mandatory Step B6 gate. Its entire purpose is to force actual page loads and honest reporting instead of confident assertion.**

```text
You are working inside the FTC 2026-27 BIOBUZZ review workspace at
ROOT = "C:/Users/ericj/Documents/BIOBUZZ Analysis".

CONTEXT YOU MUST LOAD FIRST:
  ROOT/reference/BOM-PROTOCOL.md            <- §B6, which this prompt executes, and §0.2 the tags
  ROOT/reference/VENDOR-ECOSYSTEMS.md       <- §2 vendor profiles, §5.1 what is and is not verified
                                               about shipping, §9 the prior verification log
  ROOT/reference/LEGAL-PARTS-CONSTRAINTS.md <- the manual tables each allowlisted part must match
  ROOT/manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt

THE LINES TO VERIFY:
<<<PASTE THE BOM LINES - SKU, ITEM NAME, VENDOR, PRICE AS CURRENTLY WRITTEN>>>

TASK — verify each line against the LIVE vendor page. You must actually fetch pages. Reporting
what you believe to be true, without a fetch, is a FAILURE of this task, not a shortcut.

PROCEDURE, per line:
1. FETCH the vendor's own page. Prefer the CATEGORY / COLLECTION page - it shows name, SKU, price
   and stock string for many parts at once and it does not rot. Deep product URLs 404 regularly.
2. Read FOUR things off the page and report all four:
     a. the EXACT product name as printed
     b. the SKU / part number as printed
     c. the price as printed
     d. the vendor's OWN stock status string, copied VERBATIM
        (e.g. "In Stock & Ready To Ship!", "OUT OF STOCK", "Discontinued", "Sold Out")
3. Compare against the line as written and classify:
     MATCH / PRICE-CHANGED / SKU-WRONG / RENAMED / OUT-OF-STOCK / DISCONTINUED /
     PAGE-404 / SITE-BLOCKED / NOT-FOUND-ON-CATEGORY-PAGE
4. Cross-check every allowlisted part against the MANUAL TABLE, not the vendor's marketing:
     motors -> Table 12-1 (CLOSED list: "The only allowed motor actuators are")
     servos -> Table 12-2 (OPEN list, but spec-tested)
     servo/motor power expanders -> Table 12-3 (check the per-port limits)
     main batteries -> Table 12-4 (CLOSED list, 7 items)
     vision coprocessors -> Table 12-9 (check for explicitly PROHIBITED devices too)
   Report legality and availability as TWO SEPARATE columns. A part can be legal and unbuyable.
5. Assign a confidence tag:
     VERIFIED         = you loaded that page in THIS session and read all four fields off it
     VERIFIED-UPSTREAM= copied from a workspace catalog that logs its own URL (still needs a fetch)
     MANUAL-SKU       = part number came from a V0 manual table you grepped (price tagged separately)
     FAMILY-ONLY      = family and category URL verified, SKU not - mark NEEDS-SKU-CHECK
     UNVERIFIED       = could not establish. MAY NOT BE ORDERED.

ABSOLUTE RULES - these define the task:
- You may NOT state a SKU or price you did not read off a page in this session. If a fetch fails,
  the correct output is "PAGE-404, could not verify" - NOT your best recollection.
- You may NOT take a SKU from a web search result snippet. Search snippets have been observed to
  return the WRONG SKU for an adjacent product: a search for the goBILDA FTC Starter Kit returned
  3200-4008-2627 as the "Upgrade Pack" SKU, while the goBILDA category page shows the Upgrade Pack
  is 3200-0101-2627 ($249.99) and 3200-4008-2627 is the FTC Starter Kit ($899.99). Two products,
  adjacent in the catalogue, $650 apart. Always confirm on the vendor's own page.
- If a vendor site blocks you or returns an error, SAY SO EXPLICITLY with the status code, and fall
  back to naming the product family only. Studica's site has returned HTTP 403; goBILDA's and REV's
  shipping-policy pages have returned HTTP 404. Silence about a failure is a fabrication.
- Date-stamp every price "as of <today>" and mark VERIFY-BEFORE-ORDER.
- Where the vendor page omits a spec a RULE turns on, say so and check the manual. Worked example:
  REV-31-1302 "12V Slim Battery" does not state its chemistry on the product page, but R601 requires
  a 12V NiMH main battery - the question is resolved by Table 12-4, which names REV-31-1302 as legal.
- Do NOT "fix" a discrepancy by guessing. Report it and say what a human must check at the cart.

OUTPUT:
  1. A verification table:
     | line | as written | as found on page | verbatim stock string | verdict | legality (rule/table)
     | confidence | URL fetched | date |
  2. A "FETCH FAILURES" section listing every URL that 404'd, blocked, or timed out, with the status.
  3. A "MUST RESOLVE BEFORE ORDERING" list - every line that is not MATCH+in-stock+legal.
  4. A one-line gate verdict: CLEARED TO ORDER / NOT CLEARED - and if not cleared, exactly what
     blocks it.
  5. A verification log listing every URL you actually loaded, so the next person can audit you.
```

---

## Appendix — prompt maintenance

**[J] Keep these prompts honest as the season moves:**

| Trigger | What to update |
|---|---|
| `reference/mechanisms/*.md` land | Remove the "if it does not exist yet" fallback clause from **P2** |
| ~~`reference/STRATEGY-RANKING-PROTOCOL.md` lands~~ | **Done 2026-08-21** — it exists (PHASE D, D0–D8) and is wired into **P1**. Its §0.1 confirms *"D5 feeds the BOM phase"* |
| `reference/REVIEW-PROMPTS-STRATEGY.md` step ids are renumbered | Renumber **this pack's** B-ids in the same commit — the two packs are a matched pair |
| `reference/ACHIEVABILITY-RUBRIC.md` version changes | The upstream phase re-runs D4; **re-run P2 from scratch**, not just the changed line |
| A Thursday **Team Update** changes an R-rule | Update the rule text quoted in **P3**. Team Updates post every Thursday from Kickoff to two weeks before Championship; additions highlighted yellow, deletions struck through |
| **Game Q&A** answers land (Q&A opens **2026-09-28, 12:00 p.m. ET**) | Add any parts-relevant ruling to **P3** |
| A motor is added to Table 12-1 | Update **P3** test 3 — R501's own note says additional motors may be added in future manual updates |
| Vendor discount terms change | Update **P4** lever 6. REV codes expire **May 31, 2027** |
