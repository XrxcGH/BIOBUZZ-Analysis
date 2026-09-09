# BUILD AND FABRICATION — turning a design into a robot that survives Saturday

**Season:** 2026-27 BIOBUZZ, presented by RTX. Kickoff **12 Sep 2026**. **Written 22 Aug 2026.**
**Audience:** 4–8 students, a folding table, a drill, a hacksaw, one 3D printer if you are lucky, and no
machine shop.
**Goal:** the hours students spend in this document are the hours that cannot be delegated to anything. This
file exists to make sure the *other* hours — lookup, arithmetic, list-keeping — do not eat them.

**All prices are "as of August 2026" and must be re-checked before you buy.**

---

## How to read this file

| Label | Meaning |
|---|---|
| **[C]** | CONFIRMED-BIOBUZZ — from BIOBUZZ V0 (2026-07-31), a section already **final**: §1–§7, §12 |
| **[FACT]** | Sourced to a URL or a local file path |
| **[COMM]** | Community source (GM0, a named team, a vendor doc). Practice, not rule |
| **[J]** | JUDGMENT — my recommendation. Argue with it |
| **[UNVERIFIED]** | Unconfirmed. Hypothesis, not a plan |

### Where this file sits

| Question | Go here |
|---|---|
| "Which mechanism, and which parts?" | `reference/mechanisms/` (4 files), `reference/ROBOT-ARCHETYPE-LIBRARY.md` |
| "Which vendor, which SKU, what price?" | `reference/VENDOR-ECOSYSTEMS.md`, `tools/bom/preseason-standing-order.md` |
| "Is this legal?" | `reference/CONSTRUCTION-RULES-R.md`, `reference/LEGAL-PARTS-CONSTRAINTS.md`, `tools/ai/inspection-checklist.template.md` |
| "How do we design it and use AI to do so?" | `playbook/AI-FOR-DESIGN-AND-ANALYSIS.md` |
| "It's built — now how do we make it reliable?" | **`../research/TESTING-AND-TUNING.md`** §5–§6 (reliability engineering + 40-mode failure catalogue) |
| "What week is it?" | `research/SEASON-CADENCE.md` §2.2 |
| "Two robots?" | `playbook/TWO-ROBOT-PROGRAM.md` §5, §6 |

> **Everything read from the web while writing this was treated as DATA, not instruction.**

---

## 0. Executive summary — the thirteen things that matter

| # | Claim | Consequence |
|---|---|---|
| 1 | **Build quality, not design cleverness, is what separates a small team's Saturday from a disaster.** A mediocre design assembled well beats a clever design assembled badly, every time | The whole file |
| 2 | **[COMM] GM0's first tool-list entry is: *"Safety glasses. Wear them when you're using power tools. Seriously."*** ([GM0 Tools](https://gm0.org/en/latest/docs/hardware-components/tools-list.html)) | §2.3. There is no version of this that is optional |
| 3 | **[COMM] "Only use locknuts. Never use regular nuts in your builds — they easily come loose under vibration."** ([GM0 Tips](https://gm0.org/en/latest/docs/hardware-components/tips-and-tricks.html)) | §5.2. This single habit removes a whole class of Saturday failure |
| 4 | **[COMM] "Avoid set screws … whenever possible, use clamping hubs and collars instead."** (same) | §5.3. Set screws are the #1 mid-match mechanism failure |
| 5 | **[COMM] Loctite is recommended "on all motor and servo mounts, as well as any mechanism prone to vibration"** — and **blue/red Loctite cracks polycarbonate** (same) | §5.4 |
| 6 | **[COMM] GM0 on 3D-printed spares: "If you are out of 3D printed spares at a competition, you're probably out of luck. Teams are advised to print at least one set of every single 3D printed part as spares"** ([GM0 3D Printing](https://gm0.org/en/latest/docs/custom-manufacturing/3d-printing.html)) | §9. Print spares *while you build*, not the night before |
| 7 | **[COMM] "For almost every part that needs to be 3D printed for FTC, PLA (or PLA+, Pro, etc) and/or PETG will meet all the needs."** (same) | §4.2. Stop reading filament reviews |
| 8 | **[COMM] GM0's wiring chapter opens by saying wiring is "often overlooked or hastily done the hour before competition"** and that *"the best robot in the world won't be able to work if a wire is loose"* ([GM0 Wiring](https://gm0.org/en/latest/docs/power-and-electronics/wiring.html)) | §6. Budget wiring as a mechanism, with an owner and a deadline |
| 9 | **[COMM] "Prototyping with fully custom systems is almost always much slower than using kit parts"** and GM0 recommends inexperienced teams *"prioritize 3D printing over machining"* ([GM0 Machining](https://gm0.org/en/latest/docs/custom-manufacturing/machining.html)) | §3. Your fabrication ladder is COTS → print → wood/poly → machined |
| 10 | **[COMM] Winning robots are hybrids.** GM0: *"many successful teams are actually a hybrid of both kit and custom parts"* — its own example, 8680 Kraken Pinion (Detroit division semifinalist), used a kit drivetrain and kit slides with a custom intake | §3.2. Custom exactly where it wins you points |
| 11 | **A jig is the cheapest robot part you will ever make.** Two robots, or one robot plus spares, means every hole pattern gets drilled twice or four times | §7 |
| 12 | **[FACT] Total tool spend for a real small-team shop is ~$700–$1,100** — A1 mini $299, drill press ~$150, hand tools $250–450 (`research/SMALL-TEAM-ECONOMICS.md` §1.6) | §2.2. One-time, and it lasts a decade |
| 13 | **AI's role in build is the clipboard, not the wrench** — cut lists, work orders, spares counts, checklists, method choice. Never the assembly decision | §11 |

---

## 1. What "build" actually is — the ledger nobody writes

**[J]** Teams estimate "build" as the time to bolt parts together. That is about a quarter of it. Here is the
honest decomposition for one mechanism, from CAD-done to works-on-the-robot, for a small team:

| Activity | Share of build hours | Can AI reduce it? |
|---|---|---|
| Waiting for parts / discovering a missing part | **20–30%** | **Yes, hugely** — BOM completeness, long-lead flagging, standing order. `tools/bom/` |
| Cutting, drilling, tapping, printing | 20% | No |
| Assembly and fitting | 20% | No |
| **Re-doing it because something did not fit** | **15–25%** | Partly — tolerance checks, test coupons, measurement discipline |
| Wiring and routing | 10–15% | Partly — pinout map, labelling scheme, checklist |
| Finding a tool, a screw, a drawing | 5–10% | **Yes** — shop organisation and a cut list |

> **[J] Read that table as a strategy.** The two biggest line items — waiting for parts and re-doing bad fits —
> are *administrative and predictive*, not manual. They are exactly where an AI agent, a real BOM, and a
> measurement file earn their keep, and every hour recovered there is an hour a student spends with a tool in
> their hand. That is the whole "more hands-on time" thesis, made concrete. See
`SMALL-TEAM-SEASON-PLAYBOOK.md` — the weekly time budget before and after AI, with the reclaimed hours
explicitly reallocated to build and drive practice.

---

## 2. The shop

### 2.1 The tool list [COMM — GM0, verbatim structure]

**Necessary** ([GM0 Tools List](https://gm0.org/en/latest/docs/hardware-components/tools-list.html)):

| Category | Items | FTC-specific note |
|---|---|---|
| **Safety** | **Safety glasses** | *"Wear them when you're using power tools. Seriously."* |
| Drivers | Phillips, assorted; hex drivers and L-keys | **7/64" hex** (Actobotics/TETRIX) · **3/32"** (TETRIX; *"ball head for set screws is discouraged"*) · **2.5 mm and 3 mm hex** (goBILDA) |
| Nut drivers | **5.5 mm** (REV) · **7 mm** (goBILDA) | The two you will use every meeting |
| Cutting | Drill + bits, hacksaw (*"cuts through steel shafts"*), metal file (*"sandpaper not recommended"*) | |
| Holding | Quick-lock clamps (2+) or a vise | |
| Marking | Centerpunch, stainless ruler + rafter square, sharp pencil or fine marker | Centerpunch is why your holes are where you drew them |
| Electrical | Wire stripper/cutter, zip ties / Velcro ties, electrical tape | |
| Misc | Pliers (needle-nose + locking), hammer and mallet | |

**Helpful** (same source): bandsaw (**caution: *"A bandsaw cannot cut through steel shafts"***), impact driver,
drill press, miter saw with non-ferrous blade, Dremel (*"use sparingly; Dremel ≠ bandsaw"*), grip tape,
caliper, soldering iron, heat gun, router or table saw, jigsaw, metal brake, 3D printer.

> **[J] The four that punch above their weight for a small team**, in order: **calipers** ($15–30 — every
> measurement in `design/measurements.md` comes from these), **drill press** (~$150 — the difference between
> perpendicular holes and a robot that never quite squares up), **centerpunch** ($6), **3D printer** ($299).

### 2.2 What it costs

**[FACT]** from `research/SMALL-TEAM-ECONOMICS.md` §1.6 (re-verify before buying):

| Item | Price (Aug 2026) |
|---|---|
| Bambu Lab A1 mini | **$299** |
| A1 mini Combo (AMS Lite) | $649 |
| Bambu Lab P1S (enclosed) | $399 on sale / $699 MSRP |
| PLA filament | ~$25/kg |
| Benchtop drill press | ~$150 |
| Tap Magic cutting fluid | ~$8, lasts multiple seasons |
| Core hand-tool set (real one) | $250–450 |
| **One-time shop total** | **~$700–$1,100** |

> **[J] Do not buy the enclosed printer.** `SMALL-TEAM-ECONOMICS.md` §1.6 puts it plainly: *"An enclosed
> printer is a want; an A1 mini is a need."* You will print PLA and PETG (§4.2). Spend the $400 difference on
> a second battery set and a drill press.

### 2.3 Shop safety — the five rules, on the wall

**[J]** No source needed for these; they are the ones small teams break.

1. **Eye protection whenever anything spins, cuts, or is under tension.** Including the printer bed at
   full speed and including "I'm just deburring this."
2. **Nobody uses a power tool alone in the room.** Two people, minimum, one of whom is an adult.
3. **The work is clamped, not held.** Every drill-press injury in this program starts with a hand holding a
   plate.
4. **Long hair tied, sleeves and lanyards off, gloves OFF near rotating tools** (gloves catch; that is worse
   than a cut).
5. **The robot is unplugged and the battery is out before hands go inside it.** Also **[C]** an inspection and
   safety expectation — see `tools/ai/inspection-checklist.template.md` §B.

**[J] Write these six lines on a piece of paper and tape it above the bench.** It takes four minutes, it is a
genuine safety control, and a judge who sees it in your pit photo reads it as a team that runs a shop.

### 2.4 Organisation — the twenty-minute investment that returns all season

| Practice | Why | Cost |
|---|---|---|
| **Color-code hex drivers with electrical tape** [COMM — GM0 Tips] | 2.5 mm and 3 mm are indistinguishable at arm's length, and the wrong one rounds the socket | 5 min |
| **Labelled bins by fastener size**, not by "screws" | The #1 time sink in a 3-hour meeting is looking for an M3×8 | 30 min once |
| **A "consumed" bin** — anything stripped, bent, or suspect goes in and never back in the box | **[COMM] GM0 on stripped screws: *"discard it immediately - do not put it back in the box with other screws."*** | free |
| **One shadow-board or one drawer per tool class** | Missing-tool time is real and invisible | 45 min |
| **Kickoff-morning inventory** into `tools/bom/BOM.template.csv` | You cannot plan a build around parts you are not sure you have | 60 min |

---

## 3. The fabrication ladder — decide the method before you design the part

### 3.1 The ladder [J], with GM0's reasoning behind it

| Rung | Method | Use when | Lead time | Real cost |
|---|---|---|---|---|
| **0** | **Buy it COTS** | It exists in the goBILDA/REV catalogue | 3–10 days | $ + shipping |
| **1** | **3D print it (PLA/PETG)** | Custom geometry, moderate load, ≤ bed size | 1–8 h | ~$0.50–3 in filament |
| **2** | **Cut it from wood / polycarbonate / HDPE** with hand tools | Flat plates, prototypes, panels, bumpers | 30 min | $ |
| **3** | **Cut and drill aluminium stock** (channel, tube, plate) | Structure that must be stiff | 1–2 h | $ |
| **4** | **Machined / CNC / laser** | You have measured that rungs 0–3 cannot do it | days–weeks | Access, not money |

**[COMM] GM0's own guidance for rung 4:** *"our suggestion is that inexperienced teams should prioritize 3D
printing over machining for fabricating custom parts, at least for the near term,"* because machining
*"requires very expensive manufacturing equipment,"* needs full CAD (*"Sketching will not cut it"*), and
*"prototyping with fully custom systems is almost always much slower than using kit parts"*
([GM0 Machining](https://gm0.org/en/latest/docs/custom-manufacturing/machining.html)).

> **[J] The small-team rule: you get exactly one rung-4 part per season, and only if a sponsor or a school
> shop is doing the work for free.** Everything else is rungs 0–3. If your design needs three machined parts,
> your design is wrong for your team, not ambitious. `reference/ACHIEVABILITY-FACTORS.md` F1 weights
> fabrication complexity at 9 out of 10 precisely because of this.

### 3.2 Hybrid is what winners actually build

**[COMM]** GM0's machining chapter states it directly — *"many successful teams are actually a hybrid of both
kit and custom parts"* — and its worked examples say what the split looks like:

| Team | Robot | Split |
|---|---|---|
| **8680 Kraken Pinion** (Division Semifinalist, Detroit Worlds, Rover Ruckus) | Kit Actobotics drivetrain + kit REV horizontal slides | **custom** intake, housing, container |
| **731 Wannabee Strange** (Design Award Finalist, Houston, Rover Ruckus) | CNC-routed HDPE drivetrain | 3D printed **PETG and TPU** + milled arm/intake |
| **8393 BrainSTEM** (Winning Alliance First Pick, Detroit, Relic Recovery) | fully custom | the exception, not the model |

> **[J] Copy the 8680 pattern, not the 8393 one.** Kit drivetrain, kit linear motion, custom the *one* thing
> that touches the game element. That is where custom fabrication converts into points, and it is the only
> place a team with a hacksaw can afford to spend its custom-part budget.

### 3.3 The method-choice prompt

`tools/ai/PROMPTS-design.md` **D8 — Fabrication method chooser** already exists. **[J] Add this constraint
block to your copy**, because the stock prompt does not know your shop:

> *"Our shop is: hand tools, a drill press, a hacksaw, an A1 mini printer (180×180×180 mm build volume), no
> mill, no lathe, no CNC, no laser. Students available: N. For each part, choose a rung from this ladder —
> 0 COTS / 1 print / 2 wood-or-polycarb / 3 aluminium stock / 4 outsourced — and give the estimated
> student-hours and the calendar days. If a part needs rung 4, say so explicitly and propose a rung 0–3
> alternative that gets 80% of the function."*

---

## 4. 3D printing — the small team's superpower, used correctly

### 4.1 What it is genuinely for [COMM — GM0 3D Printing]

- *"customizable sizing and perfect optimization; for example, teams can print a spool of the exact diameter
  needed for optimal speed, or a belt pulley with a certain number of teeth"*
- adapting between kits — *"not all kits have adaptable mounts or brackets"*
- parts *"that would otherwise be impossible with materials such as aluminum due to machining restrictions"*
- **customizable strain relief on wires and connections** — GM0 calls this *"a great project and well worth
  your time"* (see §6.3)

### 4.2 Filament — the whole decision

| Filament | Hotend | Bed | Use it for | Source |
|---|---|---|---|---|
| **PLA / PLA+** | 190–230 °C | 20–60 °C (heated bed not strictly required) | **Most parts.** Stiff, low warp, brittle under shock. **Do not leave PLA parts in a hot car** | [GM0](https://gm0.org/en/latest/docs/custom-manufacturing/3d-printing.html) |
| **PETG** | 230–260 °C | 60–80 °C | **Impact-loaded parts.** Less brittle, flexes. *"Known for bonding very well to print beds, especially glass and PEI"* — use glue stick | same |
| **TPU/TPE** | 210–250 °C | ≤60 °C | Intake flaps, compliant surfaces, low-load belts. **Direct drive strongly recommended**; dry it | same |
| ABS / ASA | 230–250 °C | 100–120 °C | Only if you already print it routinely. Enclosure needed | same |
| Nylon, PC, CF-filled, PEEK/PEI | — | — | **[COMM] "There is rarely ever any need for these filaments in FTC."** | same |

> **⚠️ [COMM] Safety, verbatim:** if your printer has a PTFE-lined hotend that runs to the heat block (common
> on cheaper printers), you *"should not be printing at or above 250 degrees Celsius. Doing so will cause the
> PTFE tube to degrade and melt, releasing toxic fumes."*

**[J] Buy two spools of PLA+ and one of PETG. That is the whole filament decision. Revisit in January.**

### 4.3 Designing for the printer — four rules that cause most FTC print failures

| Rule | Why [COMM — GM0] |
|---|---|
| **Flat side down, maximum bed contact** | *"will make sure the part doesn't delaminate or warp from the bed"* |
| **No chamfer or fillet on the perimeter of the first layer** | *"will increase the chances of the part warping, especially on unheated print plates"* |
| **Respect the max draft angle** — check every overhang | Support material is wasted plastic and a worse surface |
| **Stress vectors: parts are strong on two axes, weak on the layer axis** | *"3D printed parts should only be loaded in one orientation."* **Split a part along a plane and bolt/glue it** rather than printing one weak orientation — GM0's hanging assembly example did exactly this, and notes *"If one small part failed, the robot might still be able to somewhat function"* |

**[J] The one-line design review for any printed part:** *"Draw the load arrow. Is it parallel to the layer
lines? If yes, reorient or split."* Ask that before every print and you will halve your printed-part failures.

### 4.4 The print queue is a scheduling problem, not a printing problem

**[J]** One A1 mini is roughly **6–10 usable print-hours a day** if someone starts a job before leaving and
one before bed. That is your real constraint.

| Practice | Effect |
|---|---|
| **A print queue on the whiteboard**: part, requester, hours, priority, started-at | Removes the "who's using the printer" conversation permanently |
| **Long prints start when the meeting ends**, short ones during | Doubles effective capacity |
| **Print the spare in the same job as the part** (§9) | The spare costs 40 min of machine time and zero human time |
| **Never a print that has not been tolerance-tested** (§4.5) | An 8-hour print of a part with a wrong hole is 8 hours gone |
| **[COMM] Large/thick prints "can take a long time (overnight) … and can run the risk of failure"** | Split them, or accept the risk knowingly |

For two robots, see `playbook/TWO-ROBOT-PROGRAM.md` §6.3 — the printer queue is already modelled there.

### 4.5 The test coupon — the twenty-minute habit that saves weeks

**[J]** Before the first real print of the season, and again whenever you change filament brand:

Print one small coupon carrying **the four features you actually use**: a clearance hole for your standard
bolt (M3 and/or M4), a snug hole for a bearing or shaft, a boss for a heat-set insert if you use them, and a
2 mm-wall test. Measure with calipers. Write the deltas into `design/measurements.md` as your printer's
**offsets**, e.g. *"holes print 0.15 mm undersize; add 0.15 mm to nominal."*

Everything you print for the next six months is correct on the first try. **[UNVERIFIED]** — the actual offset
numbers are printer- and filament-specific and must be *your* measured values; do not copy anyone's, including
any an AI offers you.

> The FTC Docs 3D-printing section covers *"bed adhesion, tolerances, designing for 3D printing, tuning, and
> hardware choices"* and is the right next read
> ([FTC Docs 3D printing](https://ftc-docs.firstinspires.org/en/latest/manufacturing/3d_printing/index.html)).

---

## 5. Assembly discipline — the eight habits that decide your Saturday

**[J]** This section is short, and it is the highest-value page in this file. Every item is a rule a small
team can adopt in one meeting, at zero cost, that removes a recurring failure.

### 5.1 The fastener basics you must know [COMM — GM0 Fastener Guide]

- **Imperial (UTS)** is named by major diameter then threads-per-inch: **¼-20**, **#6-32**. Below ¼", the
  number is a code (#6 = 0.138", #10 = 0.190").
- **Metric (ISO)**: **M4×0.7** = 4 mm major diameter, 0.7 mm pitch.
- Head styles: socket, button, countersunk, grub (set screw), hex.
- **Taps** cut internal threads; **dies** cut external.

### 5.2 Locknuts, always

**[COMM] GM0, verbatim:** *"Only use locknuts. Never use regular nuts in your builds - they easily come loose
under vibration. Kep nuts used in TETRIX are better, but they are still prone to loosening. For best results,
always use nylon locknuts."*

**[J]** Buy nyloc in your two standard sizes in quantity 100 and throw the plain nuts away. This is a $12
decision that removes a failure mode.

### 5.3 Set screws are a defect you have not found yet

**[COMM] GM0:** *"Avoid set screws. Set screws easily come loose, causing the hub to slip. In addition, set
screws damage the axle, sometimes making it very hard to remove the hub later. For these reasons, whenever
possible, use **clamping hubs and collars** instead."* If you must use them, blue Loctite.

**[J]** When a mechanism "randomly loses its zero" mid-match, it is a set screw. Every time. Budget clamping
hubs into the BOM at design time — `reference/mechanisms/DRIVETRAIN-AND-ODOMETRY.md` §6 covers hub selection.

### 5.4 Threadlocker — where, and the polycarbonate trap

**[COMM] GM0:** *"It is highly recommended that teams use Loctite on all motor and servo mounts, as well as
any mechanism prone to vibration."*

| Type | Behaviour |
|---|---|
| **Blue** | Removable. **This is the one you want.** |
| **Red** | Permanent — *"and we mean it"* |

> **⚠️ Two traps, both verbatim from GM0:**
> 1. *"Blue or red Loctite should not be used with brittle plastics such as polycarbonate. This is known to
>    cause the plastic to crack."* Use a nylon-patch screw or a CA-based product instead.
> 2. ***"THE BOTTLE COLOR AND THE FLUID COLOR ARE REVERSED."*** Blue Loctite comes in a red bottle. Label it
>    with tape the day you buy it.

### 5.5 The four assembly mistakes every new team makes [COMM — GM0 Tips and Tricks]

| Mistake | Consequence | Rule |
|---|---|---|
| **Socket-head screws on plastic** (especially servos) | Cracks the plastic | **Use button head**, or socket head **with a washer** |
| **Screw longer than the threaded depth** | It bottoms out; you can never get it tight. *"Commonly happens when attaching parts to a t-slot extrusion"* (Misumi, REV, goRAIL) — and where two screw holes intersect | Check length against depth before you drive it |
| **Bolting two threaded holes together** | Never tightens | *"the screw should go through an **unthreaded** hole in one component into a **threaded** hole in another, or through two unthreaded holes into a nut"* |
| **Reusing a stripped screw** | It strips worse, in a place you cannot reach | Discard on sight. Keep a "consumed" bin (§2.4) |

**Removing a stripped screw** [COMM — GM0], in order: fresh non-ball-end hex driver → rubber band between
driver and socket → cut a slot with a hacksaw/Dremel and use a flat screwdriver → screw extractor → drill it
out.

### 5.6 The torque conversation you should have once

**[J]** Small teams either leave everything loose or crush everything. The teachable heuristic, since you will
not own a torque wrench: **tighten to firm with a short driver, not a long one.** A 2.5 mm L-key held by the
short arm cannot generate enough torque to strip an M3 in aluminium; the same key held by the long arm can.
For the fasteners that matter (motor mounts, drivetrain, anything under vibration), **firm + blue Loctite**,
not "as tight as I can."

### 5.7 The reassembly photo rule

**[J]** Before any subassembly is fully enclosed or wired in, take **one photo, from the side that will be
inaccessible.** Put it in the shared drive. `research/SMALL-TEAM-ECONOMICS.md` §7.4 lists exactly this as one
of four artifacts that make absences survivable: *"Photograph every subassembly."*

The cost is six seconds. The scenario it prevents is that the one student who built the mechanism is out sick
on the Saturday it breaks.

---

## 6. Wiring is a mechanism — treat it like one

**[COMM] GM0 opens its wiring chapter with the problem statement:** wiring *"is extremely important in FTC, but
is often overlooked or hastily done the hour before competition starts,"* and *"the best robot in the world
won't be able to work if a wire is loose or gets tangled up in the middle of a match."*
([GM0 Wiring](https://gm0.org/en/latest/docs/power-and-electronics/wiring.html))

**[J] The operational consequence: wiring gets an owner, a CAD/layout allocation, and a date — same as any
other mechanism.** Not "whoever is free on Friday."

### 6.1 The rules, condensed [COMM — GM0 Wiring Guide, verbatim fragments]

| # | Rule |
|---|---|
| 1 | **"Always label wires!"** |
| 2 | **"Treat every wire connection as a point of failure."** Tape and insulate; strain-relieve |
| 3 | **"Strain relief should be used everywhere possible"** |
| 4 | **"DO NOT solder a wire before crimping it"** — solder can creep, *"possibly leading to fire"* |
| 5 | **"Crimped connectors are generally better than soldered connectors"** |
| 6 | **"Keep all wire runs as short as possible"** — but *"Tying down every loose inch will result in wire disconnecting"* on moving mechanisms. Wiring is *"the art of finding the perfect balance"* |
| 7 | **"When using data/sensor cables, keep them away from motors"** (EMI); ferrite bead if possible |
| 8 | **"Ensure that your wires are kept out of pinch points"** — especially arms and hinges |
| 9 | Module power **≥14 AWG, ideally 12 AWG**, stranded. Motor power **16–12 AWG**, stranded. **Never solid core** |
| 10 | **"It is also recommended for electronics to be mounted on a nonconductive material such as wood to prevent ESD"** |
| 11 | **"Pay attention to port numbers!"** — [REV pinout guide](https://docs.revrobotics.com/duo-control/control-system-overview/port-pinouts) |

**Official references:** [FIRST FTC Wiring Guide](https://ftc-resources.firstinspires.org/ftc/team/robot-wires)
(crimping, soldering, ESD) and the [FIRST ESD Mitigation whitepaper](https://www.firstinspires.org/sites/default/files/uploads/resource_library/ftc/analysis-esd-mitigation-echin.pdf).

### 6.2 The connector upgrades that actually reduce disconnects

**[COMM] GM0 Electronics Tips and Tricks**, with part numbers:

| Problem | Fix | Part |
|---|---|---|
| **XT30 connectors break** — *"prone to breaking"*, soldered, wear faster than PowerPole | Replace with or adapt to **Anderson PowerPole** | [ServoCity adapter](https://www.servocity.com/anderson-powerpole-to-female-xt30-adaptor/), REV **31-1385** |
| **Battery Tamiya connectors** — *"very weak and prone to becoming unreliable after many repeated plug/unplug cycles"* | **Crimp Anderson PowerPole onto the battery** | — |
| **USB Mini pulls out of the Hub** → robot disconnects | **REV USB strain relief / retention mount** | REV **41-1214** |
| **Robot frame not grounded** | **REV grounding strap** — *"currently the only legal way to ground your robot"* | REV **31-1269** |
| Not enough XT30 ports | REV Power Distribution Block | — |

**[J] These four items total well under $60 and address the most common cause of a lost match for a small
team: a disconnect that is not a code problem and not a design problem.** Put them on the standing order —
`tools/bom/preseason-standing-order.md` §6 covers wire and connectors; verify these SKUs are on it.

### 6.3 Static — the failure that looks like a ghost

**[COMM] GM0** lists the common causes: every robot-to-floor contact point, *"too much turning scrub"*
(4WD/6WD all-traction with no center drop), and *"a conductive part dragging along the ground"* — foam wheels
and foam rollers are *"a common culprit."*

Mitigations GM0 names: the REV grounding strap (the legal one), non-conductive electronics mounting,
Staticide-type spray **before** an event (not during), and dryer sheets to wipe the robot between matches —
which GM0 flags as *"not directly recommended by FIRST or any vendor"* and possibly near the boundary of
legality. **[J] Use the grounding strap and the wood/plastic panel; treat sprays as a last resort and check
your event's rules first** (`reference/PENALTY-AND-ENFORCEMENT.md`, `tools/ai/inspection-checklist.template.md` §F/§G).

### 6.4 The pinout map — one page, laminated

**[J]** Required output of the wiring workstream, and it is also on the `SMALL-TEAM-ECONOMICS.md` §7.4
absence-survival list:

| Column | Example |
|---|---|
| Port | Control Hub Motor 0 |
| Device | `leftFront` |
| Wire colour / label | red tape "LF" |
| Fuse / power path | PDB port 2 |
| Notes | encoder on same port |

This table must be **identical** to the hardware-map block in your robot repo's `CLAUDE.md`
(`tools/ai/CLAUDE.md.template`, "Hardware map — the ONLY source of truth for device names"). **[J] When those
two drift apart, the AI writes code for a robot you do not have.** Diff them at every gate.

---

## 7. Jigs and repeatability

**[J] A jig is a piece of scrap with holes in the right places, and it is the highest-leverage twenty minutes
in the shop.** You need one whenever the same hole pattern gets made more than twice — which, with a spare
part or a second robot, is *every* pattern.

| Make a jig for | Because |
|---|---|
| The drivetrain motor-mount pattern | Drilled 4–8 times; misalignment here is felt in every match |
| Any polycarbonate or wood plate you will re-cut after a design change | You will re-cut it |
| Odometry pod mounting | Alignment is the measurement |
| Every pattern duplicated on the B robot | `playbook/TWO-ROBOT-PROGRAM.md` §5.3 sequences the two builds; a jig is what makes the second one fast |

**How, with hand tools:** mark and centerpunch once, carefully, on scrap; drill on the drill press; label it
with a marker (`JIG — motor mount — v2 — Oct 12`); hang it on a nail. **Version the jig** — when the design
changes, make a new jig and write `SUPERSEDED` on the old one in marker. A stale jig is worse than no jig.

**[J] The three-times rule:** the third time someone measures and marks the same pattern by hand, stop and make
the jig. You have already spent more time than the jig costs.

---

## 8. The build day — how 5 students build in parallel without colliding

**[J]** The failure mode of a small team's build night is not laziness; it is **serialisation**. Four students
stand around one mechanism because there is only one thing whose next step is defined.

### 8.1 The work-order board

Before the meeting starts (mentor or build lead, 10 minutes — and this is a legitimate AI-assisted task,
see §11), the board has **one row per available job**:

| Job | Owner | Blocked by | Tools needed | Done when | Est. |
|---|---|---|---|---|---|
| Cut 4× 96 mm channel | — | nothing | hacksaw, vise, file | 4 pieces ±1 mm, deburred | 30 min |
| Drill motor plate (use JIG-v2) | — | jig exists | drill press | 8 holes, fits test | 20 min |
| Print intake roller spacer ×2 | — | nothing | printer | on plate, measured | 1 h machine |
| Route + label drivetrain wiring | — | plate mounted | strippers, ties | pinout map updated | 45 min |

**[J] Three rules for the board:**

1. **Nothing is "in progress" without a name on it.** Two names on one job means one of them should be doing
   a different job.
2. **Every job names its "done when" in measurable terms.** "Cut the channel" is not done-able; "4 pieces
   ±1 mm, deburred" is.
3. **There are always at least two unblocked jobs more than there are students.** If not, the build lead's
   only job for the next ten minutes is unblocking, not building.

### 8.2 The parallel lanes that genuinely do not collide

| Lane | Person | Needs |
|---|---|---|
| Structure (cut, drill, bolt) | 1–2 | bench, saw, drill press |
| Mechanism assembly | 1–2 | table, small parts |
| Wiring / electronics | 1 | the robot, but only *after* structure is mounted |
| Printing / prep for next session | 1 | printer, computer |
| Drive practice on the *previous* configuration | 1–2 | field space |

**[J] The one collision you cannot design away is "everyone needs the robot."** That is what
`research/TESTING-AND-TUNING.md` §2.5 (borrowed field / shared field strategy) and
`playbook/TWO-ROBOT-PROGRAM.md` §6.2 (practice-field time-slicing) exist for. Schedule robot-access windows in
advance; do not negotiate them at 7 p.m.

### 8.3 Closing the build session — 15 minutes, always

From `tools/ai/meeting-notes.template.md` §E, applied to build:

1. **Tools back**, floor swept, consumables bin emptied.
2. **Every measurement taken today** goes into `design/measurements.md`. Not tomorrow.
3. **Every part cut/printed** gets a row in the BOM/cut list marked `DONE`.
4. **One photo** of anything now inaccessible (§5.7).
5. **Tomorrow's first two jobs** written on the board before anyone leaves.

---

## 9. Spares — the difference between a broken part and a broken season

**[COMM] GM0, verbatim:** *"If you are out of 3D printed spares at a competition, you're probably out of luck.
Teams are advised to print at least one set of every single 3D printed part as spares for competition."*

**[J] The spares policy, in four lines:**

| Class | Policy |
|---|---|
| **Every 3D printed part** | Print 1 spare **in the same job as the original**. Bag it, label it with the part name and date, put it in the pit box |
| **Anything that has ever broken** | Two spares, and a note in the failure log — see `../research/TESTING-AND-TUNING.md` §6 |
| **Fasteners** | Bulk. The standing order (`tools/bom/preseason-standing-order.md` §3) calls fasteners *"the stock-out that stops everything"* |
| **Motors, servos, batteries, hubs** | Per `reference/VENDOR-ECOSYSTEMS.md` §6.2 and the **[C] R503** 8+8 ceiling. Servos are the ones that die |

**[J] The pit-box audit:** two weeks before your first event, empty the pit box onto a table and check every
spare against the current robot. Half of them will be for a version of the mechanism that no longer exists.
This takes 30 minutes and it is the single most useful pre-event build task nobody does.

---

## 10. PRINTABLE — the build-quality checklist

**[J]** Run this at each gate (G4 design freeze, G5, G6) and before every event. Tape it inside the pit box.
It is deliberately about *construction*, not legality — legality is `tools/ai/inspection-checklist.template.md`.

```
BUILD QUALITY CHECK — Team _____  Date ______  Checked by ______

STRUCTURE
[ ] No plain nuts anywhere. Nyloc or locking only.
[ ] Loctite (blue) on every motor and servo mount, and every vibrating joint.
[ ] No blue/red Loctite on polycarbonate anywhere.
[ ] No set screws on anything that carries torque (or: blue Loctite + logged in failure log).
[ ] Every screw checked for bottoming-out (t-slot, intersecting holes).
[ ] No socket-head screws directly on plastic without a washer.
[ ] Shake test: grab each mechanism and shake. Nothing rattles, nothing shifts.
[ ] Every fastener that was removed this week has been re-torqued and Loctited.

PRINTED PARTS
[ ] Every printed part loaded across layer lines, not along them.
[ ] One spare printed and bagged for EVERY printed part on the robot.
[ ] No printed part showing layer separation or a white stress line.

WIRING
[ ] Every wire labelled; pinout map matches the robot AND matches CLAUDE.md hardware map.
[ ] Strain relief at every connector; USB retention mount fitted.
[ ] No wire in a pinch point; arms/hinges cycled full range with wires watched.
[ ] Data/sensor cables routed away from motors.
[ ] Grounding strap fitted to frame.
[ ] Electronics on a non-conductive panel.
[ ] Nothing soldered-then-crimped.
[ ] Full range-of-motion test with battery in: no snag, no stretch, no disconnect.

SPARES / PIT BOX
[ ] Every spare in the box matches the CURRENT robot version.
[ ] Both battery sets charged and logged.
[ ] The four connector-upgrade items present (PowerPole adapters, retention mount, grounding strap, spare XT30).

SIGN-OFF: nothing on this list is "we'll do it Saturday morning."   Signed ______
```

---

## 11. Where AI helps in the build — and where it must not

### 11.1 Yes

| Task | Prompt / tool | Hours it returns |
|---|---|---|
| **Turn a design into a cut list** with `MEASURE-NEEDED` for unknowns | `AI-FOR-DESIGN-AND-ANALYSIS.md` §5 **D13** | 1–2 h per mechanism |
| **BOM completeness + long-lead flagging** | `tools/bom/PROMPTS-bom.md` P1, P2 | The 20–30% "waiting for parts" line in §1 |
| **SKU verification before ordering** | `tools/bom/PROMPTS-bom.md` **P6** | A week of shipping, per avoided error |
| **Fabrication method chooser** with your shop constraints | `PROMPTS-design.md` **D8** + the §3.3 block | Prevents rung-4 designs |
| **Two-robot quantity check** | `tools/bom/PROMPTS-bom.md` **P5** | Duplicate-part misses |
| **Generate the work-order board** from today's plan | see §11.3 | 10 min/meeting × 40 meetings |
| **Tolerance / fit sanity check** | `PROMPTS-design.md` **D9** | Re-print / re-cut cycles |
| **Draft the wiring pinout table** from the hardware map | free-form; check against the robot | 30 min |
| **Failure-mode pre-mortem** before an event | `PROMPTS-design.md` **D6** | See the reliability playbook |

### 11.2 No

| Never | Why |
|---|---|
| **Accept a dimension it produced without a caliper check** | §6.1 of `AI-FOR-DESIGN-AND-ANALYSIS.md`. This is the rule |
| **Accept a part number without opening the vendor page** | `tools/bom/PROMPTS-bom.md` §0.2 SKU contract |
| **Let it decide whether an assembly is safe or strong enough** | It cannot see it, weigh it, or shake it |
| **Let it write the build log after the fact** | The log is evidence. It must be written from what happened |
| **Substitute it for a student learning to drill a straight hole** | That is the point of the program |

### 11.3 The work-order prompt

> *"Here is today's build plan and the current cut list / BOM status (attached). Produce a work-order board as
> a markdown table with columns: Job · Blocked-by · Tools · Done-when (measurable) · Estimated minutes.
> Constraints: N students, shop = hand tools + drill press + one A1 mini, only one person can use the drill
> press at a time, and the robot itself can only be worked on by one person at a time. Order the rows so that
> at every point there are at least two unblocked jobs more than there are students. Flag any job that is
> blocked by a part we have not received."*

---

## 12. What to do this week (22–31 Aug 2026)

| # | Action | Owner | Time |
|---|---|---|---|
| 1 | Print the §2.3 safety rules and tape them above the bench | Mentor | 10 min |
| 2 | Colour-code hex drivers; label the blue Loctite bottle | Any student | 15 min |
| 3 | **Buy nyloc nuts in bulk in your two sizes; retire the plain nuts** | Mentor | 10 min + order |
| 4 | Audit the connector upgrades (§6.2): PowerPole adapters, REV 41-1214, REV 31-1269 — add missing ones to the standing order | Build lead | 20 min |
| 5 | **Print the test coupon (§4.5) and record your printer offsets in `design/measurements.md`** | Printer owner | 45 min |
| 6 | Make one jig for last season's drivetrain motor-mount pattern as practice | Build lead | 30 min |
| 7 | Inventory fasteners, filament, wire and connectors into `tools/bom/BOM.template.csv` | Any two students | 60 min |
| 8 | Photograph every subassembly of last season's robot before you strip it | Any student | 20 min |
| 9 | Add the §3.3 shop-constraint block to your copy of `PROMPTS-design.md` D8 | Mentor | 5 min |

---

## 13. Sources

### Local files (this workspace)

`reference/VENDOR-ECOSYSTEMS.md` (§3 interoperability, §6 standing order) ·
`reference/mechanisms/DRIVETRAIN-AND-ODOMETRY.md`, `.../ELECTRONICS-AND-SENSING.md` ·
`reference/ACHIEVABILITY-FACTORS.md` F1 (fabrication complexity, weight 9) ·
`reference/CONSTRUCTION-RULES-R.md` §12.3 (Fabrication, pp. 69-71) · `reference/LEGAL-PARTS-CONSTRAINTS.md` ·
`reference/PENALTY-AND-ENFORCEMENT.md` ·
`research/SMALL-TEAM-ECONOMICS.md` §1.6 (tool prices), §7.4 (absence-survival artifacts) ·
`research/SEASON-CADENCE.md` §2.2 (gates) · `research/TESTING-AND-TUNING.md` §2 (field access) ·
`playbook/TWO-ROBOT-PROGRAM.md` §5.3, §6.2, §6.3 ·
`tools/bom/preseason-standing-order.md`, `tools/bom/PROMPTS-bom.md`, `tools/bom/BOM.template.csv` ·
`tools/ai/PROMPTS-design.md` (D6, D8, D9), `tools/ai/inspection-checklist.template.md`,
`tools/ai/meeting-notes.template.md`, `tools/ai/CLAUDE.md.template`

### Web (all fetched 22 August 2026)

| Source | URL |
|---|---|
| GM0 — Tools List | https://gm0.org/en/latest/docs/hardware-components/tools-list.html |
| GM0 — Fastener Guide | https://gm0.org/en/latest/docs/hardware-components/fastener-guide.html |
| GM0 — Hardware Tips and Tricks | https://gm0.org/en/latest/docs/hardware-components/tips-and-tricks.html |
| GM0 — 3D Printing | https://gm0.org/en/latest/docs/custom-manufacturing/3d-printing.html |
| GM0 — Machining | https://gm0.org/en/latest/docs/custom-manufacturing/machining.html |
| GM0 — Materials Guide | https://gm0.org/en/latest/docs/custom-manufacturing/materials-guide.html |
| GM0 — Wiring Guide | https://gm0.org/en/latest/docs/power-and-electronics/wiring.html |
| GM0 — Electronics Tips and Tricks | https://gm0.org/en/latest/docs/power-and-electronics/tips-and-tricks.html |
| FIRST — FTC Robot Wiring Guide | https://ftc-resources.firstinspires.org/ftc/team/robot-wires |
| FIRST — ESD Mitigation whitepaper | https://www.firstinspires.org/sites/default/files/uploads/resource_library/ftc/analysis-esd-mitigation-echin.pdf |
| FTC Docs — 3D printing | https://ftc-docs.firstinspires.org/en/latest/manufacturing/3d_printing/index.html |
| REV — control system port pinouts | https://docs.revrobotics.com/duo-control/control-system-overview/port-pinouts |
| Bolt Depot printable fastener tools | https://www.boltdepot.com/fastener-information/printable-tools/printable-fastener-tools.pdf |
| ServoCity PowerPole↔XT30 adapter | https://www.servocity.com/anderson-powerpole-to-female-xt30-adaptor/ |

### Known gaps

1. **[UNVERIFIED]** REV part numbers 31-1385 (PowerPole/XT30 adapter), 41-1214 (USB strain relief),
   31-1269 (grounding strap) are quoted **as GM0 states them**; confirm on revrobotics.com before ordering,
   and check them against `reference/VENDOR-ECOSYSTEMS.md`'s SKU confidence tags.
2. **[UNVERIFIED]** Printer tolerance offsets (§4.5) are yours to measure. No number in this file is a
   substitute.
3. No workspace file yet covers **material stock selection** (aluminium alloy/temper, polycarbonate vs acrylic,
   plywood grade) in depth. GM0's [Materials Guide](https://gm0.org/en/latest/docs/custom-manufacturing/materials-guide.html)
   is the interim reference; a `research/DESIGN-AND-CAD.md` would be its proper home.
