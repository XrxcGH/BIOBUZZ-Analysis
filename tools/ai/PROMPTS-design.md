# PROMPTS — Design, CAD and Fabrication

Copy-paste prompt library for the mechanical workstream. Every prompt is
self-contained. Fill the `<…>` placeholders and paste the whole block.

**The hard boundary in this workstream.** AI is good at *constraint checking,
arithmetic, part lookup and documentation*. It is bad at *geometry it cannot
see*. It cannot look at your robot, it cannot measure your bracket, and it has
no idea whether two parts actually clear each other. Treat every dimension it
produces as a hypothesis to be checked in CAD or with calipers.

**Judging note.** BIOBUZZ A201 permits AI assistance with credit, but Design
criterion 4 and Think criterion 1 both test whether *students* can defend the
decision. AI-generated geometry is a genuine grey area — see
`research/AI-IN-FTC-POLICY.md` §7 GREY 1. **Our rule: AI may compute, check,
compare and document. Students draw.**

**Companion files**
- Legal parts, motor/servo budget, COTS DoF limit: `reference/LEGAL-PARTS-CONSTRAINTS.md`, `reference/CONSTRUCTION-RULES-R.md`
- Archetypes and what they cost: `reference/ROBOT-ARCHETYPE-LIBRARY.md`
- Vendor comparison and part numbers: `reference/VENDOR-ECOSYSTEMS.md`
- BOM discipline and ordering: `reference/BOM-PROTOCOL.md`, `tools/bom/PROMPTS-bom.md`, `tools/bom/BOM.template.csv`
- Money: `research/SMALL-TEAM-ECONOMICS.md`

---

## Contents

| # | Prompt | When | Risk if unverified |
|---|---|---|---|
| D1 | Rule-check a mechanism concept | before CAD | **High** |
| D2 | Actuator & port budget ledger | weekly in build season | **High** |
| D3 | Mechanism arithmetic (torque, speed, ratio) | per mechanism | **High** |
| D4 | Part lookup with part numbers and prices | per order | **High** |
| D5 | Design decision matrix (Think Award input) | per major choice | Medium |
| D6 | Failure-mode pre-mortem | before committing to a build | Medium |
| D7 | Convert a sketch into a build plan | per mechanism | Low |
| D8 | Fabrication method chooser | per part | Low |
| D9 | Tolerance and fit sanity check | per printed/machined part | Medium |
| D10 | Weight, CG and tip-over check | per major addition | Medium |
| D11 | Onshape / CAD workflow help | as needed | Low |
| D12 | Design-review checklist against the manual | before each event | **High** |

---

## D1 — Rule-check a mechanism concept *(do this BEFORE you CAD it)*

```
I am designing a mechanism for FTC BIOBUZZ 2026-27. Check it against the rules
BEFORE we spend build time on it.

The concept, in plain language:
<describe it: what it does, roughly how, what it touches, how it deploys>

Read these local files for the actual rule text — do NOT rely on your memory of
prior FTC seasons, the rules were renumbered for BIOBUZZ:
  reference/CONSTRUCTION-RULES-R.md
  reference/LEGAL-PARTS-CONSTRAINTS.md
  manuals/2026-27_BIOBUZZ/BIOBUZZ_V0_layout.txt

Give me a table: rule id | what it says | how my concept interacts | verdict
(LEGAL / ILLEGAL / DEPENDS / DEFERRED-UNTIL-KICKOFF) | what I would have to
change.

Cover at minimum: R101 (we must build the major mechanisms), R102 (18 in cube
starting configuration, all parts stationary), R103 (self-supported),
R105 (single assembly, no intentional detachment, expansion envelope — NOTE
the sizing constraint is DEFERRED to Kickoff in V0), R201 (no field damage,
no sharp edges), R202 (safety list incl. AprilTag-mimicking imagery),
R203 (must release scoring elements and detach from the field UNPOWERED),
R204 (no downforce/suction), R301 (no COTS major mechanisms), R303 (COTS
components limited to 1 degree of freedom), R501-R506 (motor/servo legality
and the 8 motor + 8 servo cap), R801 (only manufacturer-sealed closed-air
systems; no generated pressure or vacuum).

Rules for you:
- Quote the rule id in every row. If a rule is marked DEFERRED or ERRATA in
  our reference file, say so explicitly rather than guessing a number.
- If my description is too vague to judge a rule, say "need more detail: <what>"
  instead of assuming.
- End with the ONE rule most likely to kill this concept, and the cheapest
  design change that removes the risk.
```

---

## D2 — Actuator and port budget ledger

**Why this matters:** BIOBUZZ R503 caps the robot at **8 motors + 8 servos across
all configurations used at an event** (R503 + I302 — it is summed over every
swappable mechanism, not per match). With a four-motor holonomic drive you have
four motors for the entire rest of the robot.

```
Maintain our actuator budget ledger for FTC BIOBUZZ.

Current committed actuators:
<list every motor and servo we have committed to, with what it does and which
mechanism it belongs to. Include spares/alternates we would bring to an event.>

Proposed addition:
<what we want to add>

Produce:
1. A ledger table: mechanism | motors | servos | hub | ports used | notes.
2. Totals against the caps: motors n/8, servos n/8 (BIOBUZZ R503).
   Remember I302: the count includes every configuration we bring to an event,
   even if they are never on the robot at the same time.
3. Port feasibility: with at most 2 hubs (R701), do we have enough motor ports
   (8 total) and servo ports (12 total)? Flag if we are near the 5 V / 5 A hub
   servo budget — the manual's helper text on this was deleted for BIOBUZZ but
   the electrical limit is physical, not editorial.
4. If the proposal breaks a cap, give me three ways to get the same function for
   fewer actuators, ranked by how much build time each costs. Consider: gas
   springs (R801.A explicitly permits manufacturer-sealed closed-air systems and
   they cost ZERO motor, servo and electrical budget), ratchets, one motor
   driving two linked mechanisms, and passive/gravity mechanisms.

Cite R503, R701 and I302 by id. Do not invent port counts — state them from the
reference file and say if you are unsure.
```

---

## D3 — Mechanism arithmetic

```
Do the mechanism arithmetic for <mechanism>. Show every step so a student can
check it by hand — I want to be able to redo this on paper in a judge interview.

Given:
- Motor: <e.g. goBILDA 5203-2402-0019 Yellow Jacket, 19.2:1, 312 rpm,
  24.3 kg-cm stall torque, 537.7 ticks/rev>  <-- I will supply the real spec
  sheet numbers; do NOT look them up from memory
- Additional reduction: <belt/chain/gear ratio>
- Load: <mass in kg or lb, moment arm, spool/pulley diameter>
- Required: <travel distance, target time, or required holding force>

Compute, showing units at every step:
1. Output speed and output torque after all reductions.
2. Force or torque available at the point of use, vs. what is required.
3. Safety factor. State plainly whether it is adequate and against what
   criterion (I want >= 2x for a lift holding a load, >= 1.5x for a driven axis
   — tell me if you disagree and why).
4. Travel time for the required motion, ignoring and then including
   acceleration.
5. Current draw estimate at the worst case, against the 10 A continuous /
   20 A peak per Control Hub motor port.
6. Encoder ticks per unit of travel — the number that will go in Constants.java.

Then: state the ONE assumption in this calculation most likely to be wrong, and
how to measure the real value in under 15 minutes.

Rules for you: use only the numbers I supplied plus g = 9.81 m/s^2. If you need
a number I did not give you, ask for it — do not substitute a typical value.
```

---

## D4 — Part lookup with real part numbers and prices

```
Find real, currently-purchasable parts for: <what I need, with the constraint
that matters — bore size, length, load, mounting pattern>.

Search the actual vendor sites: goBILDA, REV Robotics, AndyMark, Studica,
McMaster-Carr, and Amazon only as a last resort. Fetch the product pages.

For each candidate give me: vendor | part number (SKU) | exact product title |
price in USD | in stock? | the URL you fetched | the one spec that decides it.

Hard rules:
- Do NOT invent a SKU or a price. If you cannot fetch the page, write
  UNVERIFIED and give me the search URL to check myself.
- Date-stamp every price as "as of <today's date>" and remind me prices move.
- Flag anything on the BIOBUZZ legal-parts lists (Tables 12-1 through 12-8 in
  reference/CONSTRUCTION-RULES-R.md) — for motors, servos, batteries, switches,
  grounding straps and power regulators, ONLY parts on those tables are legal.
- For servos, check the R502 gate: mechanical output power <= 8 W at 6 V and
  stall current within the cap. Show the calculation
  P = 0.25 * stall_torque_Nm * no_load_speed_rad_per_s, using the datasheet
  numbers you actually found. If the datasheet does not give a 6 V spec, say so.
- Note shipping cost and lead time if the page shows them. For a small team,
  a $4 part that ships in 8 days may be worse than a $9 part that ships in 2.

End with the recommended pick, one sentence on why, and the row to paste into
tools/bom/BOM.template.csv.
```

---

## D5 — Design decision matrix *(Think Award input)*

**This is the highest-value documentation artefact in the mechanical workstream.**
Its output goes straight into `tools/ai/decision-log.template.md` and then into
the portfolio. See `research/SCOUTING-AND-AWARDS.md` §16.

```
Help me BUILD (not write) a design decision matrix. I supply the judgement, you
supply the structure and the arithmetic.

Decision: <what we are choosing between>
Options we have identified: <list them>
What matters to us and roughly how much: <criteria and rough weights>
Constraints that are non-negotiable: <e.g. actuator budget, our machine shop is
a drill press and a 3D printer, we have 6 weeks>

Do this:
1. Challenge my option list: is there an obvious option I have missed, or an
   option that is really two options? Name it and stop.
2. Challenge my criteria: is any criterion actually a consequence of another?
   Is any criterion unmeasurable as stated? Rewrite unmeasurable criteria into
   measurable ones.
3. Build the matrix with my weights. Leave every score BLANK — I will fill them
   in with my team. Do not score for me.
4. For each criterion, tell me what evidence would justify a high vs low score,
   so my scores are defensible when a judge asks.
5. After I fill in scores, sanity-check my arithmetic and tell me if the result
   is sensitive to any single score (i.e. would flip if one cell moved by 1).

Never tell me which option to pick. If I ask you to, remind me that a judge will
ask a student why we chose it, and the answer cannot be "the AI said so."
```

---

## D6 — Failure-mode pre-mortem

```
Pre-mortem this mechanism. Assume it is now March, we are at our last event, and
this mechanism has failed catastrophically. Work backwards.

The mechanism: <description, materials, fasteners, loads, duty cycle>
Matches it will see before then: roughly <N>.

Produce a table: failure mode | what physically breaks | early warning sign we
could observe | likelihood (H/M/L) for an FTC robot | consequence | cheapest
mitigation | can we test for it in the shop?

Cover at least: fastener loosening under vibration, 3D-printed part layer
delamination at the load path, bearing/bushing wear, belt or chain skip,
string/cable fraying or unspooling, wire chafing at a moving joint, connector
back-out, gear tooth shear, structural fatigue at a stress riser, thermal
shutdown of a stalled motor, and the mechanism jamming with a game element in it.

Then tell me the TWO failure modes that are both likely and not currently
mitigated, and what to do about each this week.

Be blunt. A polite pre-mortem is a useless pre-mortem.
```

---

## D7 — Sketch to build plan

```
Turn this design into a build plan a two-person team can execute.

The design: <describe, or point me at a CAD screenshot/photo you want me to read>
Available tools: <e.g. drill press, hand tools, one Bambu A1 printer, no mill,
no lathe>
Available stock: <what we already have>
People: <N> students, <hours/week>
Deadline: <date>

Produce:
1. Exploded parts list: part | make or buy | material | qty | source | est cost
2. Fabrication order, with dependencies marked, so nothing waits on nothing.
3. For each fabricated part: the process, the setup, and the ONE dimension that
   must be right or the assembly fails.
4. An hour estimate per step, and a total. Compare the total to the hours we
   actually have between now and the deadline, and tell me plainly if it does
   not fit.
5. The three steps most likely to take 3x longer than estimated, and why.
6. What we can do in parallel while parts are on order.

If the plan does not fit the deadline, say so in the first line of your answer,
and propose the smallest scope cut that makes it fit.
```

---

## D8 — Fabrication method chooser

```
I need to make <part>. It carries <load / has this function>. Quantity <n>.

Compare these methods for THIS part: 3D print (PLA / PETG / ABS / nylon-CF),
laser-cut acrylic or plywood, hand-cut and drilled aluminium extrusion or
sheet, water-jet or send-out CNC, and buy-a-COTS-equivalent.

Table: method | material | est. cost | est. hours incl. setup | strength at the
load path | tolerance achievable | risk | verdict for this part.

Constraints:
- Our tools are: <list>. If a method needs a tool we do not have, price the
  send-out option with a real vendor and a real URL, or say UNVERIFIED.
- Print orientation matters: for any 3D-printed option, state the orientation
  and where the layer lines fall relative to the load. If the load is normal to
  the layer lines, say so loudly.
- Check R301 and R303 before recommending "buy a COTS equivalent" — COTS major
  mechanisms are prohibited and COTS components are capped at 1 degree of freedom.

End with a recommendation and the one thing that would change it.
```

---

## D9 — Tolerance and fit sanity check

```
Check the fits in this assembly before I print or cut anything.

Parts and nominal dimensions: <list, with units>
Process for each: <FDM print at 0.4 mm nozzle / laser cut / drilled aluminium>
Fit intended at each interface: <clearance / transition / press / threaded>

For each mating interface, tell me:
- the nominal clearance and whether it is right for the intended fit
- the realistic process tolerance for that process (state your source or say
  "rule of thumb, verify on a test coupon")
- whether the stack-up of tolerances across the assembly can go out of spec, and
  at which interface it bites first
- the recommended dimension change, in the same units I gave you

Specifically check: shaft-to-bore fits for <5 mm / 6 mm / 8 mm> hex and round
shafts, bearing seats, screw clearance holes vs tap sizes, and any slot that
needs to slide.

Then tell me the ONE test coupon I should print or cut first, and what to
measure on it, so I do not waste a 6-hour print.
```

---

## D10 — Weight, CG and tip-over check

**Context:** BIOBUZZ R104 sets **no weight limit**. That makes mass cheap and
*reach* expensive — the binding constraint is R105's expansion envelope
(deferred until Kickoff) and tip-over, not the scale.

```
Estimate mass, centre of gravity and tip-over margin for our robot.

Components with mass and approximate position (x, y, z from the frame's
front-left-bottom corner, in inches):
<table — I will supply real weighed masses where I have them and estimates
flagged as such>

Compute:
1. Total mass, and CG in x, y, z. Show the arithmetic.
2. CG height as a fraction of the wheelbase and of the track width.
3. Static tip-over angle in each direction.
4. The tipping acceleration in each direction, and how that compares to what
   our drivetrain can actually produce.
5. Redo (1)-(4) with the mechanism at FULL extension, worst case. This is the
   number that matters.
6. If we added <N> lb of ballast at <location>, what happens to (3) and (4)?

Rules: mark every input I flagged as an estimate, and tell me which single
estimate the answer is most sensitive to. Note that R202.E lists hazardous
materials as prohibited and that DECODE's explicit carve-out permitting sealed
lead ballast was REMOVED for BIOBUZZ — so do not recommend lead ballast without
flagging that as an open rules question.
```

---

## D11 — CAD workflow help

```
I am using <Onshape / Fusion / SolidWorks> for FTC. Help me with: <the task>.

Constraints:
- Explain in terms of the feature tree and sketch relations, not just click
  paths, so I understand why it works.
- Assume I am a student who has used CAD for <N> months.
- Our parts come from goBILDA/REV, so builds are on a <8 mm / 96 mm goBILDA |
  0.5 in REV> hole pattern — respect that grid in anything you suggest.
- If your answer depends on a specific version or a paid feature, say so.
- If there is a way to do this that is more robust to later edits (fully
  constrained sketches, mate connectors on the pattern rather than on faces),
  show me that way and explain the failure it prevents.

Then tell me one thing I should do differently in how I structured this model,
if you can see one.
```

---

## D12 — Design review against the manual *(before every event)*

```
Run a full design review of our robot against the BIOBUZZ inspection criteria.

Read:
  reference/CONSTRUCTION-RULES-R.md
  tools/ai/inspection-checklist.template.md

Our robot: <describe every mechanism, every actuator, wiring approach, signs,
operator console>

For every line in the inspection checklist, tell me: PASS / FAIL /
NEEDS-PHYSICAL-CHECK, with the rule id and what specifically to look at.

Then rank the top 5 things most likely to fail us at inspection, using the
historical failure-frequency table in reference/CONSTRUCTION-RULES-R.md section 7.

Be explicit about which items you CANNOT judge from a text description and that
a human must physically check with a ruler, a multimeter or their hands. Do not
mark something PASS that you cannot actually see.
```

---

## Anti-prompts

| Don't ask | Why | Ask instead |
|---|---|---|
| "Design a mechanism to do X" | You get a plausible-sounding assembly with invented dimensions and no clearance checking, and no student can defend it | D5 to structure the choice, then draw it yourself |
| "What size motor do I need?" | Depends on numbers only you have | D3, with the real spec sheet |
| "Give me the goBILDA part number for X" | It will produce a well-formed SKU that does not exist | D4, which forces a fetched URL |
| "Is my CAD good?" | It cannot see your CAD | D9 / D12 with explicit dimensions |
| "What's the best drivetrain?" | Sycophantic, and the answer depends on the game, which is not public until 12 Sep 2026 | `reference/ROBOT-ARCHETYPE-LIBRARY.md`, then D5 |
