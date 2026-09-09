# Running Two FTC Teams Out of One Organization — Rules & Realities (BIOBUZZ 2026-27)

**Scope:** one organization, two registered FIRST Tech Challenge teams ("A team" / "B team"), ~15 students
total, two robots, shared mentors, shared build space, modest budget.

**Why this file exists:** every rule below is in a BIOBUZZ V0 section FIRST has already **finalized**
(Section 3 Eligibility & Inspection (I), Section 4 Advancement, Section 5 Event Rules (E), Section 6
Awards (A), Section 12 ROBOT Construction (R)). None of it changes at Kickoff on **2026-09-12**. This is
the part of the season you can lock down *now*.

**Evidence labels**

| Label | Meaning |
|---|---|
| **[C]** CONFIRMED-BIOBUZZ | Quoted from the BIOBUZZ V0 Competition Manual (2026-07-31), in a section already final for BIOBUZZ |
| **[O-FTC]** OFFICIAL-FIRST-FTC | Official FIRST *FTC* publication outside the Competition Manual (current revision is 2025-26; BIOBUZZ revision not yet published) |
| **[O-FRC]** OFFICIAL-FIRST-FRC | Official FIRST publication scoped to **FIRST Robotics Competition**, not FTC. Persuasive, **not binding on FTC** |
| **[H]** HISTORICAL | Prior-season FTC manual text (DECODE 2025-26 / INTO THE DEEP 2024-25). Not a BIOBUZZ fact |
| **[COMM]** COMMUNITY | Named person on a public forum. Opinion / lived experience, not rule |
| **[J]** JUDGMENT | My inference from cited rules. Flagged as inference |
| **UNVERIFIED** | Could not be confirmed from the corpus or the open web |

**Primary sources**

- `manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf` (93 pp)
- `manuals/2026-27_BIOBUZZ/sections/03_Eligibility_Inspection_I_p22-26.txt`, `04_Advancement_p27-32.txt`, `05_EventRules_E_p33-42.txt`, `06_Awards_A_p43-58.txt`, `12_RobotConstruction_R_p64-88.txt`
- `manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_TU32.pdf` (DRIVE TEAM definition only)
- FIRST Tech Challenge **Judging Process Guide**, Rev. 25-26.3 — <https://ftc-resources.firstinspires.org/ftc/archive/2026/event/judging-guide>
- FIRST **Guidelines for Sibling Teams**, Rev. June 2026 (FRC-scoped) — <https://info.firstinspires.org/hubfs/web/program/frc/reg/sibling-teams-guidelines.pdf>

> ⚠️ **Rule-ID warning.** `pdftotext -layout` mis-aligns the rule-ID margin column in Section 5 by up to
> four rules (it will tell you `E109` is "in another team's pit area"; it is not). Every E-rule ID in this
> file was re-derived from PDF text coordinates, where the ID and the rule title sit on the **same** line.
> Verified mapping: **E105** = Event resources are for competing teams only · **E106** = Practice only
> when/where permitted · **E107** = Work in designated areas only · **E115** = Inspection required for
> practice FIELD access · **E117** = Enter only 1 ROBOT in the tournament.

---

## 0. TL;DR — the 14 things that matter

1. **Two teams from one org is fully legal and needs no permission from anyone.** [C] There is no rule in
   BIOBUZZ V0 capping teams per organization, per school, or per coach. The only gate is I101: each team
   independently registers, pays, and puts two YPP-screened adults in the Lead Coach 1 / Lead Coach 2 slots.
2. **Each team must have its own physical ROBOT. You cannot inspect one robot twice.** [C] E117 +
   R101 + I301. See §3 for the full derivation — no single BIOBUZZ rule says it in one sentence, so this is
   the one place you should file a Game Q&A question on 2026-09-28.
3. **But the two robots may be *identical*.** [O-FRC] "Teams may design multiple copies of the same ROBOT
   if they wish, but each team must have their own unique physical ROBOT." Nothing in BIOBUZZ V0 forbids
   twin robots. [C] E117's stated intent is only about *swapping robots between MATCHES*.
4. **Sharing parts, fabrication, software and strategy between your two teams is explicitly blessed.** [C]
   R101's own note: assistance from other teams — "fabricating elements, supporting construction, writing
   software, developing game strategy, contributing COMPONENTS, and/or MECHANISMS" — is *not* prohibited or
   discouraged. The only thing that must be yours is your **MAJOR MECHANISMS**.
5. **FIRST has a name for you: "Sibling Teams," and FTC judges are trained on it.** [O-FTC] The FTC Judging
   Process Guide has a section "Judging Teams with Close Affiliations (Sibling Teams)" that tells judges to
   expect "multiple teams have a similar design for their robot or claim the same outreach activities" and
   to **probe with clarifying questions**. Assume your judges have read it.
6. **Sibling teams are judged separately for *all* awards in FTC — including Inspire.** [O-FTC] "Sibling
   Teams are considered separately for all awards." Note this is **stricter-in-your-favour than FRC**: FRC
   makes sibling teams pick one Impact Award submission *or* two different ones. FTC's published guidance
   has **no** such carve-out for Inspire. [J] Do not import the FRC rule; do assume judges will notice
   duplicate content.
7. **Both teams can win awards at the same event.** [C] A215 caps *each team* at one team judged award; it
   says nothing about organizations. There is no anti-sweep rule anywhere in Section 6.
8. **Both teams can advance from the same event.** [C] Section 4 advancement is a pure per-team point
   ranking (Table 4-1 / Table 4-2). No organizational cap, no "one per school" clause.
9. **The Competition Manual does not cap team size. FIRST's website does: 15.** [C] Zero occurrences of a
   roster size limit in V0. [O-FTC] `ftc-docs`: "teams (up to 15 team members, grades 7-12)". FIRST's get-started
   page says "there is **no ideal number** of students on a team, we find many teams include 8-12 students."
   **15 students split 2 ways puts both your teams at ~7-8 — below FIRST's own observed typical band**, though
   FIRST explicitly declines to set a floor. This is the single biggest structural risk in your plan. See §6.
10. **Nothing in V0 says a student may not be on both rosters.** [C] Silent. [O-FRC] Current FIRST sibling
    guidance (Rev. June 2026) explicitly permits dual rostering — "Students should be listed on team
    roster(s) that they are an active participant on" — with **one** exception: "students speaking to judges
    must be distinguished for each event."
11. **Nothing in V0 restricts shared mentors.** [C] I101.A.iii requires 2 YPP-screened Lead Coaches *per
    team*; it does not say they must be different people. UNVERIFIED whether the FIRST Dashboard permits one
    person in a Lead Coach slot on two teams — confirm before you register.
12. **You cannot merge pits without the Event Director.** [C] E502.B/E502.C: no swapping assigned pits, no
    moving into empty pits without ED approval. You *can* ask; large multi-team programs report EDs often
    seat siblings adjacently. [COMM]
13. **You *can* legally work in each other's pit.** [C] E107.B — FABRICATED ITEMS may be produced "in
    another team's pit area with permission from that team." Your two teams grant each other that permission.
14. **The classic failure mode is not a rules problem, it's a resourcing problem.** [COMM] Every multi-team
    program write-up in §9 names the same three: mentors spread thin, doubled logistics, and the junior team
    treated as a farm/parts pool. §10's DO/DON'T list is built to defuse exactly that.

---

## 1. Fast answers, with citations

| Question | Answer | Authority |
|---|---|---|
| May one org register 2+ FTC teams? | **Yes.** No cap exists. | [C] no rule in V0; I101 sets the only requirements |
| May a student be on both rosters? | **Not prohibited by V0.** FIRST's sibling guidance permits it. | [C] silent · [O-FRC] Sibling Guidelines FAQ |
| Must the two teams have different students at judging? | **Yes, effectively.** Students must be distinguished per event when speaking to judges. | [O-FRC] Sibling Guidelines FAQ · [O-FTC] Judging Process Guide |
| May the two teams share ONE robot? | **No.** Each team inspects and plays with its own 1 ROBOT. | [C] E117 + R101 + I301 · [O-FRC] "each team must have their own unique physical ROBOT" |
| May one robot be inspected for both teams? | **No.** | [J] from E117 + R101 + I301 (§3) — *file a Q&A question* |
| May the two robots be identical? | **Yes.** | [C] nothing forbids it · [O-FRC] explicitly allowed |
| May the teams share parts / fabrication / code? | **Yes**, so long as each team built its own MAJOR MECHANISMS. | [C] R101 + its note |
| May A team's students build B team's MAJOR MECHANISM? | **No** — that mechanism must be built by the team that registered and will use it. | [C] R101 |
| May they share a pit? | **Only with Event Director approval.** | [C] E502.B, E502.C |
| May A team's students work in B team's pit? | **Yes, with that team's permission.** | [C] E107.B |
| May they share tools, spare parts, a cart at an event? | **Yes** — nothing restricts it; helping other teams is encouraged. | [C] E107.B; no prohibiting rule · [O-FRC] "Sharing scouts or having Sibling Teams help each other at the event is still allowed" |
| May they share a practice field at an event? | **Only as a registered team, after passing inspection.** | [C] E105, E115, E106 |
| May they reuse the same PORTFOLIO? | **Not prohibited, but it is the fastest way to lose both awards.** | [C] A201 (no originality clause) · [O-FTC] judges probe duplicate claims |
| May they claim the same outreach activity? | **Yes, and judges are trained to ask who actually did it.** | [O-FTC] Judging Process Guide, Sibling Teams |
| May they share mentors? | **Yes.** Each team needs 2 YPP-screened Lead Coaches. | [C] I101.A.iii · UNVERIFIED whether Dashboard allows the same person twice |
| May one adult be silent observer at both interviews? | **Yes — but only 1 adult per session**, and simultaneous slots make it physically impossible. | [C] A208 |
| May both teams win awards at the same event? | **Yes.** A215 is a per-team cap only. | [C] A215, A211 |
| Is there an anti-sweep rule? | **No.** | [C] no such rule in Section 6 |
| May both teams advance from the same event? | **Yes** — advancement is a per-team point ranking. | [C] §4, Table 4-1, Table 4-2 |
| Is there a team-size cap? | **Not in the manual.** FIRST's website says 15 max, 8-12 typical. | [C] silent · [O-FTC] ftc-docs / get-started |

---

## 2. Registration & eligibility — Section 3 (I)

Both teams must independently clear **I101** *"Teams must be registered with FIRST."* Everything here is
**per team**, not per organization:

| I101 requirement (North America) | Two-team consequence |
|---|---|
| I101.A.i — complete annual registration on the FIRST Dashboard | Two registrations |
| I101.A.ii — pay annual registration fee | Two fees. **$350/season** for 2026-27 [O-FTC, firstinspires.org Cost & Registration] |
| I101.A.iii — 2 adults in **Lead Coach 1 / Lead Coach 2** roles, YPP screened | 4 Lead Coach slots to fill. Rule does **not** say they must be 4 distinct people |
| I101.A.iv — any additional regional Youth Protection screening | Region-dependent |
| I101.A.v — register **all youth team members** on the Dashboard | Each student appears on the roster(s) they actively participate on |

> **Money warning.** [O-FTC] "Season registration does **NOT** include participation at official FIRST Tech
> Challenge events. Event availability varies by region and fees are set by local FIRST Program Delivery
> Partners." Robot build kits and control hardware are also **not** included. FIRST's own starting estimate
> is "around $1,800" per team for registration + initial robotics set. Two teams ⇒ roughly **2× everything**,
> plus 2× per-event fees at every Qualifier. Get your PDP's per-event fee in writing before committing.

**I102 — check-in.** Per team, no later than 45 minutes before Qualification MATCHES, "by a team adult and
at least one STUDENT... present at the venue." [C] With one adult and two teams, you check in twice, and the
window is the same 45 minutes for both. Plan two adults.

**I103 — responsible adult present for the whole event.** "At least 1, preferably 2, adult(s)... must be
present at all times during the event." [C] Read literally this is per team: two teams at one event means
**at minimum two responsible adults, and realistically four** if you want I103's "preferably 2."

**Team registration mechanics.** [O-FRC] In FRC, a sibling team is registered as a **New Veteran Team**, not
a rookie, and must email FIRST Support to get a veteran number reassigned. **UNVERIFIED whether FTC applies
the same rookie/veteran logic** — no FTC-scoped equivalent of the "Newly Formed Teams" page was found. Ask
FIRST Support at `customerservice@firstinspires.org` *before* you create the second team, because it affects
rookie-grant eligibility. [O-FTC] For 2026-27, organizations buying multiple registrations should set up a
**financial guarantor** under Team/Account Finances using the organization EIN.

---

## 3. The ROBOT question — can two teams share one robot?

**Short answer: no.** There is no single BIOBUZZ rule that says "a ROBOT may only be inspected for one
team," so here is the actual chain. Each link is [C]; the conclusion is [J].

| # | Rule | Text (abridged) | What it forecloses |
|---|---|---|---|
| 1 | **E117** | "At a given FIRST Tech Challenge event, each team may only inspect and play MATCHES with **1 ROBOT**. FIRST Tech Challenge teams may only participate in **1 concurrent event** at a time." | Caps robots-per-team at 1. Does **not** by itself cap teams-per-robot |
| 2 | **R101** | "The ROBOT and its MAJOR MECHANISMS must be built by the FIRST Tech Challenge team **that has registered for the event and intends to use the ROBOT** to participate in MATCHES or as part of judged awards." | This is the load-bearing one. One physical robot cannot simultaneously have been built by team A *and* by team B unless both genuinely built it |
| 3 | **I301** | "Teams should present the ROBOT and OPERATOR CONSOLE with **all** COMPONENTS... that will be used during MATCHES... should not add any un-inspected COMPONENTS to the ROBOT without re-inspection." | Inspection is an act performed by *a team* on *its* robot, with *its* students present ("student team members present their ROBOT", §3.3.1) |
| 4 | **R401/R403** | "Minimum of two ROBOT SIGNS per ROBOT"; "**Team number** on ROBOT SIGNS" | A robot on the FIELD carries exactly one team number |
| 5 | **Glossary** | ROBOT = "an electromechanical assembly built by **a** FIRST Tech Challenge team..." | Singular team, by definition |
| 6 | **§1.5.1 CIC** | "We Don't Cheat... Our team will not try to gain an advantage using any 'loopholes' in the rules." | Closes the residual gap |

**The loophole you must not take.** [C] **I303.C** lists "addition, relocation, or replacement of the team
SIGN" as a change that does **not** require re-inspection. So physically, swapping robot signs and running
one robot under two team numbers would pass unnoticed. Nothing but R101, E117 and the CIC stands in the way.
[J] Treat this as the bright line of your program's integrity: **one robot, one team, all season.**

**Q&A action item.** [C] The Game Q&A opens **2026-09-28, 12:00 p.m. ET**. Submit: *"May two teams from the
same organization present the same physical ROBOT for inspection at different events?"* Note [C] Q&A answers
do not supersede manual text and REFEREES/INSPECTORS remain final authority — but a public answer is the
cheapest way to settle it with your LRI.

### 3.1 What you *can* share on the robot side

[C] **R101's own note** is unusually permissive and is the most valuable rule in this document for a
resource-poor two-team org:

> "This rule requires that the ROBOT and its MAJOR MECHANISMS were built by its team **but is not intended to
> prohibit or discourage assistance from other teams** (e.g., fabricating elements, supporting construction,
> writing software, developing game strategy, contributing COMPONENTS, and/or MECHANISMS)."

| Shared item | Legal? | Rule |
|---|---|---|
| CAD files, drawings, design concepts | **Yes** | [C] R101 note ("developing game strategy") |
| Software / autonomous code | **Yes**, explicitly named | [C] R101 note ("writing software") |
| Machining / 3D printing done by A team for B team | **Yes**, explicitly named | [C] R101 note ("fabricating elements") |
| Individual COMPONENTS and sub-MECHANISMS | **Yes**, explicitly named | [C] R101 note ("contributing COMPONENTS, and/or MECHANISMS") |
| A gearbox assembly | **Yes** — explicitly *not* a MAJOR MECHANISM | [C] R101.A |
| A COTS part or COTS drive chassis | **Yes** | [C] R101.C, R301.A |
| A whole **MAJOR MECHANISM** (drivetrain, intake, scoring arm) built by the other team | **No** | [C] R101 |
| The whole robot | **No** | [C] R101 + E117 |

**MAJOR MECHANISM** = [C] "a group of COMPONENTS and/or MECHANISMS assembled together to address at least 1
game challenge: ROBOT movement, SCORING ELEMENT manipulation, FIELD element manipulation, or performance of
a scorable task without the assistance of another ROBOT."

[J] Practical reading for a 7-student team: **share the pattern, not the part.** A team designs and prints
an intake; B team prints its own copy from the same file and assembles it themselves. That is squarely
inside R101. B team receiving A's assembled intake and bolting it on is not.

### 3.2 Sharing parts *at an event*

| Situation | Rule | Effect |
|---|---|---|
| B team hands A team a spare, identical motor mid-event | [C] **I303.E** "replacement of a COMPONENT with an identical COMPONENT" | **No re-inspection needed** |
| B team hands A team an identical spare MECHANISM | [C] **I303.F** "replacement of a MECHANISM with an identical MECHANISM (size, weight, material)" | **No re-inspection needed** |
| B team hands A team a *non-identical* mechanism never inspected on A's robot | [C] **I301** + **I303** | **Re-inspection required** |
| A team reconfigures using a subset of already-inspected MECHANISMS | [C] **I303.G** | No re-inspection needed |
| Shared pool of motors/servos across two robots | [C] **I302** | Each team's total electronics across **all** its configurations must independently meet the Section 12 caps. A shared pool does not create a shared allowance |

[C] **I304** *"Do not exploit re-inspection. Teams may not use the re-inspection process to circumvent any
other rules."* [J] Cannibalising the B robot mid-event to keep the A robot alive is legal on the parts side
(I303.E/F) but is the single most visible way to look like a one-robot program with a decoy. See §9.

---

## 4. At the event — Section 5 (E)

| Rule | Text | Two-team consequence |
|---|---|---|
| **E105** | "Event resources are for competing teams only. Only teams registered for an event may use that event's competition FIELD, practice FIELD, and inspection..." | Both your teams must be **registered for that event** to touch the practice field. A B-team student "helping" on the practice field while B isn't registered is out |
| **E106** | "Teams may only practice with their ROBOT in their pit space, in the designated event practice areas, or while in a Practice MATCH." | You cannot set up a shared practice rig in the aisle between your two pits |
| **E107** | FABRICATED ITEMS only: **A.** in their pit area, **B.** "in another team's pit area **with permission from that team**", **C.** while queued, **D.** areas designated by staff, **E.** provided machine shops available to all teams | **E107.B is your friend.** Your two teams grant each other standing permission and you effectively get a two-pit workshop — without violating E502 |
| **E115** | "A team may only use a practice FIELD with a ROBOT that has passed an initial, complete inspection." (events without scheduled inspection times) | Each robot needs its own pass. B's robot cannot ride on A's inspection |
| **E117** | See §3 | One robot per team; **and** "may only participate in 1 concurrent event at a time" — a team cannot be entered at two events on the same weekend |
| **E501** | Pits unavailable when closed | — |
| **E502** | "Pit set ups should be self-contained within the space assigned." Teams may not: **A.** run power or internet lines from their pit to any other area, **B.** "swap team pits with other teams if pits have assigned team numbers", **C.** "move themselves to empty team pits without Event Director approval" | **You may not build yourself a mega-pit unilaterally.** Ask the ED in advance for adjacent assignment |
| **E503** | Aisles and exit pathways clear | Two teams' worth of totes in one aisle is the classic violation |
| **E505** | Only small benchtop machinery in pits | Same limit whether you have 1 pit or 2 |
| **E511** | Charge batteries safely and fairly | Two robots ⇒ double the battery charging load; [C] "Power may not be available overnight for a multi-day event" (§5.5) |
| **E702** | "No more than 5 team members may be in the pits during ceremonies" | Per team. With ~7 students each, that means ~2 in the stands per team, and you need coverage of both pits |

[C] §5.5: a pit is "typically a 10 ft. by 10 ft. by 10 ft. area... Each team is assigned a pit space typically
marked with their team number." [C] "Team pits may or may not have a table and power outlet."

---

## 5. Awards — Section 6 (A)

### 5.1 Can both teams win?

**Yes, and nothing prevents an organizational sweep.** [C]

- **A215** *"Teams can only get one judged award. Teams are only eligible to win or be a runner-up for a
  single team judged award at the event."* — the cap is **per team**. Two teams ⇒ two award slots available
  to your organization.
- **A211** scales the award pool to event size. At a **4-10 team** event only one of {Connect, Reach,
  Sustain} and one of {Innovate, Control, Design} is given at all — so at a small Qualifier your two teams
  are competing against each other for a very small pool. At **21-40 teams** there are 1st and 2nd places in
  most categories plus 3rd-place Inspire. [J] **Your two teams' realistic joint award ceiling is much higher
  at a mid-size event than at a tiny one.**
- **A213** — Inspire only in your **HOME REGION**. **A214** — a team can win 1st Place Inspire only once per
  season from any Qualifying/League Tournament (2nd/3rd still available afterwards, and Regional Championship
  Inspire is still available). Both are **per team**; if A team wins Inspire 1st at Qualifier #1, B team is
  entirely unaffected.
- **No anti-sweep rule exists** anywhere in Section 6. [C]

### 5.2 Portfolios and shared engineering work

| Question | Answer | Authority |
|---|---|---|
| Is there a rule against two teams submitting similar portfolios? | **No.** A201 sets format limits only (1 cover page, ≤15 pages of content, US Letter or A4, <15 MB digital, content only from **on or after January 1, 2026**) | [C] A201 |
| Can they cite the same outreach event? | Yes — and judges are trained to unpick it | [O-FTC] Judging Process Guide |
| Does FTC require one Inspire submission per org, like FRC's Impact Award rule? | **No such FTC rule exists.** FRC's sibling guidance requires either one submission or "different submissions and presentations"; FTC's Judging Process Guide instead says "Sibling Teams are considered separately for **all** awards" | [O-FRC] vs [O-FTC] |
| Can AI be used to draft the portfolios? | Yes, with credit | [C] A201: "Teams may use AI and research aids to compose their portfolios, provided they respect intellectual property rights and include a footnote or endnote credit." Example given: *"Portfolio created by Team XXXXX and ChatGPT"* |
| Can prior seasons be referenced? | Only to show growth; emphasis must be the current season | [C] A201 note |

[C] **A201.E** — content must be "progress, challenges, and accomplishments which have taken place since
**January 1, 2026**", and §6.1.1 confirms "the current season begins on January 1, 2026."

[J] **The real portfolio risk is not a rule violation, it's a scoring one.** Judges "cannot consider
information from outside of what they have seen or heard at the current event" ([C] §6.1.1), and one of the
explicitly disallowed inputs is *"Personal knowledge of a team."* That protects B team from being marked
down for being new — but it also means **B team gets zero credit for anything it does not say in its own
interview and its own portfolio.** Two near-identical portfolios do not double your odds; they halve the
distinctiveness of both.

### 5.3 Judging logistics with two teams

| Rule | Constraint | Two-team consequence |
|---|---|---|
| **A203** | Must participate in an Initial Interview to be considered for any judged award | Two interviews, possibly overlapping slots |
| **A204.A** | "no fewer than 2 STUDENT representatives for teams of 2 STUDENTS and larger" | Each team needs ≥2 of its own students in its own interview, simultaneously if slots collide |
| **A205** | Same length interview for all teams, "at least 10 minutes" | — |
| **A207** | First 5 minutes reserved for uninterrupted prepared presentation | Two presentations to write, not one |
| **A208** | "**One** adult may attend the judging session" as silent observer; may not coach | If interviews are concurrent you need **two** available adults, and neither may speak |
| **A209** | Translator accommodations must be arranged with the ED in advance | Per team |
| **A210** | No photo/video/audio recording during the Initial Interview | You cannot record A's interview to prep B |
| **A202** | Portfolio submitted on time as instructed; "1 printed copy... during the Initial Interview" if no other instruction | Two printed portfolios |
| **A212** | Every team gets a feedback form | Two feedback forms — a genuine advantage of running two teams |

---

## 6. Team size

**The Competition Manual is silent.** [C] A full-text search of BIOBUZZ V0 returns **no** roster size limit,
minimum, or maximum. The only student-count rule anywhere is **A204.A** ("no fewer than 2 STUDENT
representatives for teams of 2 STUDENTS and larger"), which implies a 1-student team is legal.

**FIRST's published guidance, outside the manual:**

| Source | Statement | Label |
|---|---|---|
| `ftc-docs.firstinspires.org` overview | "*FIRST* Tech Challenge teams (**up to 15 team members, grades 7-12**)" | [O-FTC] |
| `firstinspires.org/programs/ftc/get-started` | "Students ages 12-18 (grades 7-12)"; "**Many teams include 8-12 students**"; "no ideal number of students on a team"; "Each team needs **two adult lead coaches**" | [O-FTC] |
| BIOBUZZ V0 Glossary | **STUDENT** = "a person who has not completed high-school, secondary school, or the comparable level in their HOME REGION as of **September 1st**" | [C] |

**Applied to ~15 students across two teams:**

- Each team lands at **~7-8 students — below FIRST's own typical band of 8-12.** [J] This is legal and
  common, but it is the structural fact that should drive every other decision in the program.
- [H] DECODE §10.2: "A DRIVE TEAM is a set of **up to 4 people** from the same FIRST Tech Challenge team...
  no more than 1 member of the DRIVE TEAM is allowed to be a non-STUDENT" (1 DRIVE COACH who may be an adult,
  plus up to 3 STUDENT DRIVER/HUMAN PLAYER). BIOBUZZ Sections 9-11 are placeholders, so the BIOBUZZ DRIVE
  TEAM size is **not yet knowable** — but if it holds, a 7-student team fields a drive team of 3 students +
  1 adult coach and has **4 students left** to run the pit, talk to judges, and scout. That is tight but
  workable.
- [H] Note the DECODE intent language, which is the closest thing FTC has ever published to a statement on
  people belonging to two teams: the DRIVE TEAM "consists of people who arrived at the event affiliated with
  that team and are responsible for their team's and ROBOT'S performance at the event (**this means a person
  may be affiliated with more than 1 team**)." It also says the intent is *not* to let teams "adopt" members
  of other teams for strategic advantage. [J] Read together: dual affiliation is contemplated; using it to
  parachute your best driver onto the other team's controls for playoffs is not.
- [COMM] `n3rdchik` on Chief Delphi: "In my experience, FTC teams are way better at a 10-12 person size and
  half are at least veterans of a season." — <https://www.chiefdelphi.com/t/rethinking-our-ftc-team-s/433836>

---

## 7. Advancement — Section 4

**Both teams advance, or don't, entirely independently.** [C] There is no organizational cap anywhere in
Section 4.

| Mechanic | Text | Two-team consequence |
|---|---|---|
| HOME REGION | "Teams are only eligible to advance from events within their HOME REGION." Glossary: HOME REGION = "The region in which a team is assigned and in which they are only eligible to advance from events within." | Both teams should be assigned the same HOME REGION; verify each team number on FTC-Events |
| Entry-level events | "Teams can advance from any of their first three entry-level events: Qualifying Tournaments (QT) and League Tournaments (LT)... eligible to advance from the **first three chronological events**" | Counted **per team**. If A team plays 4 QTs, its 4th doesn't count for A — B team's count is unaffected |
| Leagues | "Teams may only participate in **one League per season**" | Per team. Both teams may join the same League |
| SQT | "A team may only participate in one Super Qualifying Tournament (SQT)" | Per team |
| Ranking | Advancement points = Qualification Phase Performance (2-16, inverse-erf normal distribution, α=1.07) + ALLIANCE Selection Results (21 − lead/draft number) + Playoff Advancement (40/20/10/5) + Team Judged Awards (Inspire 60/30/15; all other awards 12/6/3) | Two independent point totals in the same ranked list |
| Ties | Table 4-2, 10 tiebreakers, ending in "Random Selection by Event Management System" | Your two teams can tie each other; the tiebreaker chain is neutral |
| Slots | "The local Program Delivery Partner determines the advancement numbers from each tournament in their region" | Ask your PDP how many slots your Qualifier gets — that number, not any rule, decides whether both can advance |

[C] Advancement to FIRST Championship / Premier Events is decided by FIRST HQ; **regional registration cutoff
for BIOBUZZ is November 17, 2026** and regional slot allocations publish on FTC-Events "starting in early
December."

[J] **A genuine two-team advantage:** judged-award points are large (Inspire 1st = 60; any other 1st = 12)
and are the **2nd tiebreaker** in Table 4-2. Two teams means two shots at the award pool from one program's
outreach and documentation work — provided each team's story is genuinely its own (§5.2).

[COMM] A cautionary note from a two-FTC-team org whose teams split at the advancement line:
<https://www.chiefdelphi.com/t/ftc-two-teams-one-qualified-for-regionals-one-did-not/140977> — plan in advance
for what the non-advancing team does with its season, and say it out loud to the students *before* the
Qualifier, not after.

---

## 8. Judging independence and the "satellite team" risk

### 8.1 What the rules guarantee you

[C] BIOBUZZ V0 §6.1.1 is the strongest protection B team has:

> "JUDGES are strictly instructed to only consider information from the current event and the current
> season... JUDGES cannot consider information from outside of what they have seen or heard at the current
> event."

Explicitly disallowed inputs include "Past performance (good or bad) of a team," "**Personal knowledge of a
team**," "External sources such as websites and/or social media," and "A team's ranking in the tournament."

[O-FTC] Judge conflict-of-interest handling: the Judging Process Guide has judges declare their team
affiliations on arrival and ensures judges "are not assigned to a panel scheduled to interview those teams."
[J] Relevant if one of your mentors or parents also volunteers as a judge — they will be walled off from
**both** your teams.

### 8.2 What FIRST actually tells FTC judges about you

[O-FTC] FTC **Judging Process Guide**, Rev. 25-26.3, §"Judging Teams with Close Affiliations (Sibling Teams)"
— quoted at length because this is the single most decision-relevant document outside the manual:

> "This section defines multiple teams associated with one organization as Sibling Teams... Sibling Teams are
> considered separately for all awards, and Judges will use the information provided to them by each team
> individually to assess the team against the award criteria. Each team should be prepared to cover all
> relevant information with the Judges.
>
> Teams have the opportunity to collaborate with one another on a number of items that are judged at a FIRST
> Tech Challenge event. Although this approach is welcome, it can provide a challenge when judging Sibling
> Teams. When judging Sibling Teams, for example, it is possible to find that multiple teams have a similar
> design for their robot or claim the same outreach activities.
>
> The simplest way to address Sibling Teams is to judge each team on their own, and to ask clarifying
> questions that may help identify how one team may stand out amongst other Sibling Teams."

The **exact questions judges are told to ask**:

1. "How did you decide who did what?" → "Were there any specific roles or tasks that each team member took
   ownership of?" (applies to "coordinating outreach activities **or coming up with a robot design used by
   Sibling Teams**")
2. "Who contacted __________ to coordinate your outreach activity?"
3. "How did you ensure the outreach activity, or robot design, aligned with your team plan?"

[J] **Drill these three questions with both teams.** A B-team student who answers "the A team came up with
it" has just confirmed the satellite hypothesis in one sentence. A B-team student who answers "we adapted
their intake geometry but changed the compliance because our drivetrain is slower, and I ran that test"
has just won the room.

Also relevant: [O-FRC] "If the Sibling Teams share apparel, it is recommended that the students specify to
the judges which team they are talking on behalf of." [J] With matching org shirts this is a real hazard —
add a team-number badge or a differently-coloured accessory.

### 8.3 The perception risk, per the community

Label everything in this subsection **[COMM] — community opinion, not rule.** Reddit's r/FTC was not
reachable to this tooling; sources below are Chief Delphi, quoted with usernames and thread URLs. Most
detailed multi-team write-ups on Chief Delphi are **FRC** programs; the organizational dynamics transfer,
the specific rules do not.

| Concern | What people actually say | Source |
|---|---|---|
| "Two teams is pay-to-win" | `MachoStoopid`: "I personally think its strange and unhealthy for the community as a whole as it makes FIRST more pay to win as it gives you 2 times the chance to pick or be picked on a winning alliance." He later reversed: "my feelings towards this have shifted and I can now see the merit in having multiple teams" | [Thoughts on teams with multiple teams with the same robot](https://www.chiefdelphi.com/t/thoughts-on-teams-with-multiple-teams-with-the-same-robot/406178) |
| The counter-argument | `BryceHanson`: "If that was one team, odds are good that each student would be getting less hands-on time with the robot and its parts... this topic only comes up if the robots are good." | same thread |
| Two *different* robots reads better | `Andrew_L`: "I'd much rather they build two different robots and explore how the different solutions compare... Also more kids get to design robots!" | same thread |
| The engagement question judges are really probing | `ngreen`: "My main concern... is that there is opportunity for as many students to be engaged in the design process, including a stake in it being something that they came up with and built. And it is less clear that a joint project allows for those opportunities when the teams are already the same." | same thread |
| Sibling teams are a known, named category to FIRST | `Lil_Lavery` listing real sibling pairs: "494 & 70, 11 & 193, 4653 & 4652, 1923 & 1914, 2234 & 2095, 288 & 244 & 216, and 2468 & 2687 & 2689... that tend to operate out of the same build spaces, with the same or overlapping mentors, some degree of financial and fundraising overlap, and sometimes even twin robots." | [FRC Blog Sibling Teams thread](https://www.chiefdelphi.com/t/frc-blog-sibling-teams-and-an-expanded-district/414433) |
| Effect of the guidance on already-separate teams | `Bmongar`: "If your teams already operate as fully separate teams this would have no impact as all these rules do is force some separation onto those teams." | same thread |

[J] **Bottom line on perception:** the rules protect you; the interview does not. Judges have an explicit,
published script for detecting a satellite team. Build the program so the honest answers to those three
questions are good ones.

---

## 9. Operational realities

All of §9 is [COMM] unless a rule is cited. These are named practitioners describing their own programs.

### 9.1 Money

| Line item | 2026-27 figure | Source / label |
|---|---|---|
| FTC season registration | **$350 / season / team** | [O-FTC] firstinspires.org Cost & Registration |
| What registration includes | Team management + career readiness resources; access to discounted control system components and build kits via FIRST Storefront; eligibility for team awards and FIRST Leadership Award nominations | [O-FTC] same |
| What it does **not** include | "Season registration does NOT include participation at official FIRST Tech Challenge events"; "Robot build kits, control system hardware are NOT included" | [O-FTC] same |
| Event registration | Set by your local Program Delivery Partner, varies by region | [O-FTC] same — **UNVERIFIED for your region** |
| FIRST's own "start a team" estimate | "around $1,800, which includes the yearly registration fee and initial robotics set investment" | [O-FTC] get-started |
| 2026-27 purchasing change | All FTC teams now buy registration and materials through the new **FIRST Storefront** (replacing the previous arrangement); sales-tax exemption / PO users must set up a **financial guarantor** by EIN, which can "purchase registrations for multiple teams/Class Packs at one time" | [O-FTC] FIRST community blog, Key Changes to FTC Registration |

[J] For a modest-budget org the honest arithmetic is: **two registrations, two control systems, two
drivetrains' worth of structure, two sets of consumables, two event fees per event weekend, and one shared
practice field.** The practice field is the one thing that does not double — which is exactly why it becomes
the scarcest resource (§9.3).

### 9.2 Mentors

- `Mr.Dave6327`, a two-team community program: "During build and meetings, the mentors share support to both
  teams. Over the years, we have tried having both teams in the same event, and also staggering the teams
  across 4 weeks. Logistically, it is easier to have both teams at the same event (moving, time off, etc.),
  **however there is less available time for the mentors to support both teams.**"
  — <https://www.chiefdelphi.com/t/one-school-with-multiple-teams-requirements/412189>
- `paulonis`: "I assume that most 2-team organizations have a lot of the mentor/teacher support in common
  between the 2 teams." — same thread
- `EricH` on why splitting can *help* mentor load: "If you split the team, you can possibly keep the mentor
  ratio the same, but the involvement level for the students goes through the roof because now there's a
  second robot to build. Depending how you do it, **you can also get experienced students as mentors for the
  second team.**" — <https://www.chiefdelphi.com/t/1-or-2-teams/436355>
- `MOCTA1189`, small program: "As someone on a team with currently 15-20 students and 6-8 mentors, I could
  never imagine splitting into two teams anytime soon." — same thread
- `geekygirlsarah`, FTC coach: "it exhausts me a little trying to teach everything to 15-20 rookie students.
  I love doing it, but they're never set up to be very successful."
  — <https://www.chiefdelphi.com/t/rethinking-our-ftc-team-s/433836>

[J] With limited mentor hours the binding constraint is **simultaneity**, not total hours. Two teams meeting
on the same night with one mentor is worse than two teams meeting on alternate nights with the same mentor.
`NatsirtD` describes exactly this: "Meetings are generally on alternating days, with some overlap at the
start of [the] build season." (same thread)

### 9.3 The practice field and the build space

- `gartaud`: FRC 1089 and FTC 3944 "are based in the same high school, share the same storage room, are
  supervised by the same head coach, **but are run independently**."
  — <https://www.chiefdelphi.com/t/rethinking-our-ftc-team-s/433836>
- [C] At the event, field access is regulated: **E105** (registered teams only), **E115** (inspected robot
  only), **E106** (practice only in your pit, designated practice areas, or a Practice MATCH). Nothing
  regulates your home practice field — so home scheduling is a pure program-policy problem.
- [J] With one field and two robots, write the schedule down. Ad-hoc field allocation is how the B team
  learns it is second in line.

### 9.4 Doubled logistics at events

- `Marlinvx`, mentor of an FRC varsity/JV pair, on what actually hurt: "Transporting two pits to events is
  tough... We are still working on **doubling up on tools**. For regionals, we have been fortunate that they
  put both teams together and we have mega-pit! At [Championship], we had one team on Newton and one on
  Curie... as far away as we could be. Poor parents were ran ragged going back and forth. As mentioned, we
  normally co-scout, but at [Championship], that was not possible. **By far, the experience for the JV team
  is well worth the inconveniences.**" — <https://www.chiefdelphi.com/t/1-or-2-teams/436355>
- `BBelnap88`, student on the JV team of a sibling pair: "at worlds, scouting was difficult because we were
  in different fields. **It is a little hard to share all the materials we have between the teams** as well,
  but in my opinion, the pros heavily outweigh the cons." — same thread
- [C] The mega-pit is **not yours to arrange**: E502.B forbids swapping assigned pits and E502.C forbids
  moving into empty pits without Event Director approval. Email the ED in advance.

### 9.5 The B-team-as-parts-donor failure mode

This is the specific failure the brief asks about. No FTC rule prohibits it; several structural facts make it
easy and one makes it lethal.

**Why it's easy** — [C] I303.E and I303.F let you move identical COMPONENTS and identical MECHANISMS between
robots at an event with **no re-inspection**, and I303.C lets you swap the team SIGN with no re-inspection.
The mechanical path of least resistance genuinely is "strip the B robot."

**Why it's lethal** — [C] §6.1.1: judges may only use what they see and hear from **that team** at **that
event**. A B team that spent the season donating parts has, by definition, less of its own engineering story
to tell, and there is no mechanism by which the org's overall success rubs off on it. [O-FTC] And the three
sibling-team probe questions in §8.2 are precision-engineered to surface exactly this.

**What practitioners say about keeping the junior team real:**

- Differentiate the *goal*, not just the roster. `saatb`: "4766 opts to build a more simple bot and 4522 goes
  all out. this year **4766 beat 4522** at both of their regionals that they shared!"
  — <https://www.chiefdelphi.com/t/1-or-2-teams/436355>
- Make the junior team the ownership venue. `Zach.Chang-9316`: "it allows freshmen to really get into robotics
  and get a much more hands-on learning experience than if they were just watching the upperclassman work...
  **underclassmen get a chance at a leadership position** and they learn much more." — same thread
- Deliberately distinct design goals. `AndrewFRC135`: "**Students can ONLY be committed to one team**, though
  assisting and coopertition is highly-encouraged between them... Given the different students and
  constraints, [the junior team's] strategy and design goals for this season were **distinctly different**...
  Neither bot looks anything like the other." (a *program policy*, not a FIRST rule) — same thread
- Beware the "it's just a waiting room" narrative. `geekygirlsarah`: "the team's vibe is always that FTC
  doesn't really matter because they're just going to FRC later, and I don't want them thinking their work on
  this doesn't matter or that they are just killing a year's time."
  — <https://www.chiefdelphi.com/t/rethinking-our-ftc-team-s/433836>
- `ElectraLucky5413` on the same dynamic: "FTC feels like the 'middle child' that students typically don't
  like to deal with." — same thread
- The thin-program warning. `SARAH_B`: "you definitely need kids to fully sustain a program, with only enough
  kids for 2 drive teams is nice because you get to work more on the bot, **it puts more stress and anxiety on
  those kids**." — <https://www.chiefdelphi.com/t/1-or-2-teams/436355>

### 9.6 The upside your award strategy should exploit

[C] The **Sustain Award** (§6.3.5) criteria read like they were written for a two-team org:

> Required 1 — "organizational sustainability competency by explaining its plans for long-term success,
> including one or more of: A. financial sustainability, B. season planning, and/or C. long-term team
> sustainability objectives."
> Required 3 — "leadership development competency through **clearly defined team roles and an intentional
> process for preparing future student leaders**."
> Encouraged 4 — "risk management competency by identifying organizational constraints, implementing
> mitigation strategies, and adapting plans when challenges arise."

[C] The **Reach Award** (§6.3.4) Required 2 — "successful recruitment of new teams, coaches, mentors, or
volunteers who have not previously participated in the FIRST community."

[J] A well-run A/B structure is *literally* leadership development + recruitment of a new team + an
organizational constraint being mitigated. Both teams can tell this story truthfully, from their own side of
it — the A team as the org that built a pipeline, the B team as the team the pipeline built. That is
distinct content from the same fact, which is exactly what §8.2's probe questions reward.

---

## 10. DO / DON'T for a two-team organization

### DO

| # | Do | Tied to |
|---|---|---|
| D1 | Register both teams fully and separately: 2 registrations, 2 fees, 4 Lead Coach slots with YPP screening, every student on the roster(s) they actually work on | [C] I101.A.i-v |
| D2 | Build **two physically distinct robots** and keep them distinct all season | [C] E117, R101, I301; [O-FRC] "each team must have their own unique physical ROBOT" |
| D3 | Share CAD, code, fabrication labour, COTS parts and sub-mechanisms freely between teams | [C] R101 note — explicitly permitted |
| D4 | Make each team assemble its own MAJOR MECHANISMS, even from a shared design | [C] R101 |
| D5 | Give the two teams **different design goals** — e.g. B team targets a simpler, more reliable scoring path | [COMM] `saatb`, `AndrewFRC135`, `Andrew_L`; [O-FTC] judges probe "similar design... used by Sibling Teams" |
| D6 | Grant each other standing permission to fabricate in each other's pits, and say so to event staff if asked | [C] E107.B |
| D7 | Email the Event Director ahead of every event asking for adjacent pit assignment | [C] E502.B, E502.C (you may not self-assign); [COMM] `Marlinvx` "they put both teams together and we have mega-pit!" |
| D8 | Bring **two responsible adults minimum** (four if you can), because check-in, judging observers and pit coverage are all per-team | [C] I102, I103, A208, E702 |
| D9 | Rehearse the three sibling-team judge questions with both teams until every student can answer for their own team | [O-FTC] Judging Process Guide, Sibling Teams |
| D10 | Add a visible team-number badge to the shared org shirt | [O-FRC] "students specify to the judges which team they are talking on behalf of" |
| D11 | Write two genuinely different portfolios; if an outreach event was joint, each team writes **its own role** in it | [C] A201, §6.1.1; [O-FTC] "Who contacted ___ to coordinate your outreach activity?" |
| D12 | Credit AI assistance with a footnote in **both** portfolios if you use it | [C] A201 — "include a footnote or endnote credit" |
| D13 | Target **Sustain** and **Reach** deliberately — a two-team pipeline is on-criteria evidence for both | [C] §6.3.4 Reach Req. 2, §6.3.5 Sustain Req. 1/3 |
| D14 | Publish a written home practice-field schedule before the season starts | [J] §9.3; the field is the one resource that does not double |
| D15 | Stagger meeting nights rather than splitting one mentor across two simultaneous teams | [COMM] `NatsirtD`, `Mr.Dave6327` |
| D16 | Confirm both team numbers show the **same HOME REGION** on FTC-Events, and ask your PDP for the advancement slot count at each event | [C] §4, Fig. 4-1; "The local Program Delivery Partner determines the advancement numbers" |
| D17 | Decide and announce, before the first Qualifier, what happens if only one team advances | [COMM] <https://www.chiefdelphi.com/t/ftc-two-teams-one-qualified-for-regionals-one-did-not/140977> |
| D18 | File the "one robot, two teams?" question on the Game Q&A when it opens **2026-09-28, 12:00 p.m. ET** | [C] Q&A dates; note answers do not supersede the manual |
| D19 | Confirm with FIRST Support whether FTC treats your second team as a rookie or a new-veteran team **before** creating it | [O-FRC] sibling registration rules; **UNVERIFIED for FTC** — affects grant eligibility |
| D20 | Set up the organization's **financial guarantor** by EIN so both registrations can be purchased together | [O-FTC] FIRST 2026-27 registration changes |

### DON'T

| # | Don't | Tied to |
|---|---|---|
| X1 | Don't inspect or play one physical robot under two team numbers | [C] E117, R101, I301, R403; [C] §1.5.1 CIC "We Don't Cheat" |
| X2 | Don't use the SIGN-swap exemption to run one robot as two | [C] I303.C permits sign changes without re-inspection — this is a loophole, and [C] §1.5.1 forecloses it |
| X3 | Don't have A team's students build B team's drivetrain, intake or scoring mechanism | [C] R101 (MAJOR MECHANISM must be built by the registered team) |
| X4 | Don't strip the B robot to keep the A robot running at an event | Legal per [C] I303.E/F, but see [C] §6.1.1 — B team gets judged only on what it can show; [COMM] §9.5 |
| X5 | Don't move an un-inspected mechanism from one team's robot to the other's without re-inspection | [C] I301, I303 (only *identical* component/mechanism swaps are exempt) |
| X6 | Don't assume a shared parts pool creates a shared electronics allowance | [C] I302 — limits apply to each team's total across all configurations |
| X7 | Don't merge, swap or spill into an adjacent pit without ED approval | [C] E502.B, E502.C, E503 |
| X8 | Don't let the unregistered team use the event's practice field | [C] E105, E115 |
| X9 | Don't set up a shared practice rig outside your pit | [C] E106 |
| X10 | Don't submit the same portfolio, or the same outreach narrative, for both teams | [C] A201 sets no originality rule, but [O-FTC] judges are told to probe duplicated claims and to assess each team "individually" |
| X11 | Don't send the same students to both Initial Interviews | [C] A204.A (≥2 student reps each, often concurrent); [O-FRC] "students speaking to judges must be distinguished for each event" |
| X12 | Don't plan on one adult silent-observing both interviews | [C] A208 — one adult per session, and slots may collide |
| X13 | Don't record an interview to prep the other team | [C] A210, E116 |
| X14 | Don't expect an org-level Inspire strategy — Inspire is per-team, and A214 only blocks the team that won it | [C] A213, A214, A215 |
| X15 | Don't count on a small event to reward two teams — at 4-10 teams only one MCI and one TA award exist | [C] A211, Table 6-1 |
| X16 | Don't enter either team at two events on the same weekend | [C] E117 — "may only participate in 1 concurrent event at a time" |
| X17 | Don't lose track of the 3-event advancement window per team | [C] §4 — "eligible to advance from the first three chronological events" |
| X18 | Don't let the B team be framed internally as a waiting room for the A team | [COMM] `geekygirlsarah`, `ElectraLucky5413` §9.5 |
| X19 | Don't split 15 students without checking mentor simultaneity first | [COMM] `MOCTA1189`, `Mr.Dave6327`; [O-FTC] FIRST's *observed typical* band is 8-12/team (FIRST states there is "no ideal number") |
| X20 | Don't import FRC sibling rules as if they were FTC rules | FRC's Impact Award one-submission rule has **no** FTC counterpart; FTC says siblings are judged separately for *all* awards |

---

## 11. Open questions — resolve these before or at Kickoff

| # | Question | Where to ask | Why it matters |
|---|---|---|---|
| Q1 | May two teams from one org present the same physical ROBOT for inspection at *different* events? | Game Q&A, opens 2026-09-28 12:00 p.m. ET | Settles §3 in writing with your LRI |
| Q2 | Does FTC classify a second team from an existing organization as a rookie or a "new veteran" team? | `customerservice@firstinspires.org` | Rookie grants, team number |
| Q3 | Can one person occupy a Lead Coach slot on two FTC teams in the FIRST Dashboard? | FIRST Support / Dashboard | Determines whether you need 4 screened adults or 2 |
| Q4 | What is your PDP's per-event registration fee, and its advancement slot count per Qualifier? | Local Program Delivery Partner | The real cost and the real advancement math |
| Q5 | Will the ED assign your two teams adjacent pits? | Event Director, per event | E502 makes this their call, not yours |
| Q6 | Does the BIOBUZZ Judging Process Guide keep the Sibling Teams section unchanged? | Re-download after Kickoff | §8.2 is quoted from Rev. 25-26.3; V0 §6 says the Judge Manual is "coming soon" |
| Q7 | What is the BIOBUZZ DRIVE TEAM size? | Kickoff manual, Section 10 | §6's 7-students-per-team math depends on it; DECODE's "up to 4" is [H] only |

---

## 12. Source list

**Local corpus**

- BIOBUZZ V0 Competition Manual (2026-07-31), 93 pp — `manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf`
  - §1.5 Competition Integrity Contract · §3 Eligibility & Inspection (I101-I103, I301-I304) · §4 Advancement
    (Tables 4-1, 4-2, 4-3) · §5 Event Rules (E101-E118, E301-E302, E501-E511, E601, E701-E703) · §6 Awards
    (A201-A215, §6.1-§6.3) · §12 ROBOT Construction (R101-R105, R301-R303, R401-R403) · §16 Glossary
- DECODE 2025-26 Competition Manual TU32 — `manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_TU32.pdf`, §10.2 DRIVE TEAM (HISTORICAL only)

**Official FIRST, web**

- FIRST Tech Challenge Judging Process Guide, Rev. 25-26.3 — <https://ftc-resources.firstinspires.org/ftc/archive/2026/event/judging-guide>
- FIRST Guidelines for Sibling Teams, Rev. June 2026 (FRC-scoped) — <https://info.firstinspires.org/hubfs/web/program/frc/reg/sibling-teams-guidelines.pdf>
- About the FIRST Tech Challenge (team size, grades) — <https://ftc-docs.firstinspires.org/en/latest/overview/ftcoverview.html>
- How to Get Started with FIRST Tech Challenge — <https://www.firstinspires.org/programs/ftc/get-started>
- Cost & Registration — <https://www.firstinspires.org/programs/cost-and-registration>
- Key Changes to FIRST Tech Challenge Registration — <https://community.firstinspires.org/key-changes-to-first-tech-challenge-registration-whats-new>
- 2026-2027 Season Pricing and Registration Updates — <https://community.firstinspires.org/2026-2027-season-pricing-and-registration-updates>

**Community (Chief Delphi — opinion, not rule)**

- Rethinking our FTC team(s) — <https://www.chiefdelphi.com/t/rethinking-our-ftc-team-s/433836>
- 1 or 2 teams? — <https://www.chiefdelphi.com/t/1-or-2-teams/436355>
- One school with multiple teams requirements — <https://www.chiefdelphi.com/t/one-school-with-multiple-teams-requirements/412189>
- Thoughts on teams with multiple teams with the same robot — <https://www.chiefdelphi.com/t/thoughts-on-teams-with-multiple-teams-with-the-same-robot/406178>
- [FRC Blog] Sibling Teams and an Expanded District — <https://www.chiefdelphi.com/t/frc-blog-sibling-teams-and-an-expanded-district/414433>
- [FTC] Two-Teams, One Qualified for Regionals, One Did Not — <https://www.chiefdelphi.com/t/ftc-two-teams-one-qualified-for-regionals-one-did-not/140977>

**Not reachable:** reddit.com/r/FTC (blocked to this tooling) and the legacy FTC Forum threads on team size
and students-on-multiple-teams (`ftcforum.firstinspires.org` → 404 after migration). Community evidence in
§8.3 and §9 is therefore Chief Delphi only, and skews FRC. Treat FRC program dynamics as transferable and
FRC *rules* as not.
