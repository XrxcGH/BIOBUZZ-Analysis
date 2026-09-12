# R6 — LOOPHOLE HUNT

**Phase:** R6 of `reference/ANALYSIS-PROTOCOL.md` · **Method:** `reference/LOOPHOLE-PLAYBOOK.md` (seven passes, §1–§7)
**Manual under test:** the ingested bundle at `analysis/kickoff/bundle/` (per `STATUS.md`: 188 pp., 214 rules, 53 G-rules, 17 orange)
**Bundle availability:** `tools/RUN-KICKOFF.sh` generated the bundle locally from `DECODE_Competition_Manual_TU32.pdf` (§0.3);
it is not published with this repository, because it is FIRST's manual text. Page, table and figure numbers refer to
the manual itself.
**Run:** beta harness test, 2026-08-23 · **Author:** kickoff review agent

**Sources used (and only these):** `bundle/TABLES.md`, `bundle/rules_full.tsv`, `bundle/VIOLATIONS.tsv`,
`bundle/rules_GAMESPECIFIC.txt`, `bundle/ORANGE_BOXES.md`, `bundle/caps_NOVEL_ranked.txt`,
`bundle/TRIPWIRES.txt`, `bundle/figures/p058–p094`, `bundle/full_layout.txt` (prose only — **no point value in this
document comes from `full_layout.txt`**; every number is from `TABLES.md` or a rule body in `rules_full.tsv`),
plus the method files `LOOPHOLE-PLAYBOOK.md` and `ANALYSIS-PROTOCOL.md`.

**Not consulted:** `research/LOOPHOLE-CASEBOOK.md`, `reference/SCORING-PATTERNS.md`,
`reference/ROBOT-ARCHETYPE-LIBRARY.md`, `reference/PENALTY-AND-ENFORCEMENT.md`,
`research/SCOUTING-AND-AWARDS.md`, `research/BIOBUZZ-PRESEASON.md`, `manuals/_reference_prior_seasons/`,
`manuals/archive/`.

**Labels used throughout:** `[MANUAL]` = quoted or paraphrased binding text with a citation ·
`[DERIVED]` = computed from cited operands, operands shown · `[JUDGMENT]` = my call, no manual basis ·
`[ORANGE — NON-BINDING]` = the finding rests wholly or partly on an orange box, which per the manual's own
front matter does not carry the weight of a rule and loses to the rule text if they conflict.

---

## 0. Honesty section — leakage, declared before the findings

The brief requires me to declare anything I knew that I did not read in the bundle. Three declarations:

**0.1 — The single highest-value answer in this phase was leaked to me by an *allowed* method file.**
`reference/LOOPHOLE-PLAYBOOK.md` §2 Pass 5 states, in the file I was told to read first, that "DECODE Q&A Q27
confirmed artifacts do **not** double while Q129 confirmed PATTERN does." That is Pass 5's answer, pre-supplied.
I did afterwards derive the same conclusion independently from `§10.5 A/B/C` + `Table 10-2` (see **L01**, where
the derivation is shown in full and stands on its own), but I cannot claim the derivation was blind and I have
not marked L01 as an independent find. **L01 is flagged LEAKED-CORROBORATED, not derived.** The same file also
pre-supplied DECODE's pin count ("ITD G423 5 s → DECODE G422 3 s", §3) before I read G422.

**0.2 — I have prior knowledge of this game from training.** I have confined every claim in this document to
something I can point at in the bundle with a rule ID, table reference, section number or figure. Where I could
not find a citation I wrote UNVERIFIED rather than filling the gap from memory. Readers should treat that as a
stated intention, not a guarantee; the citations are auditable and are the actual evidence.

**0.3 — This manual is post-patch, which structurally biases the hunt.** `STATUS.md` records the source file as
`DECODE_Competition_Manual_TU32.pdf`. Playbook §2 Pass 2 rests on "new rules are unpatched rules." In a TU32
document that premise is false: the ambiguities that were live on kickoff day are precisely the ones that have
already been closed, and the residue I can find is biased toward *ambiguities FIRST chose to leave in*. See
Beta feedback item 2 — this materially limits what this run predicts about 2026-09-12.

---

## 1. Pass log (playbook §2, run in order)

| Pass | Timebox | What it produced here |
|---|---|---|
| 1 — Novel terms → T1 | 15 min | Diffed `caps_NOVEL_ranked.txt` against the Section 16 Term column. Glossary coverage is **good**: ARTIFACT, CLASSIFIED, OVERFLOW, PATTERN, MOTIF, DEPOT, GATE, GATE ZONE, RAMP, SQUARE, CLASSIFIER, OBELISK, BASE, BASE ZONE, LOADING ZONE, SECRET TUNNEL ZONE, LAUNCH/LAUNCHING, LAUNCH LINE, LAUNCH ZONE, LEAVE, SPIKE MARK are all defined. Yield: **not the undefined-term type**, but a **definition-collision** type — LAUNCH and CONTROL are defined with identical operative language (**L03**). Bare "SECRET TUNNEL" appears in G425's headline while only "SECRET TUNNEL ZONE" is defined — cosmetic, not exploitable. |
| 2 — Orange rules | 25 min | All 17 read end to end from `rules_full.tsv` (G402, G408, G414–G419, G424–G427, G432–G434, R105, C501). Every finding below traces to one of them except L09 (§10.5.1) and L12 (§10.5). C501 is a da Vinci/Championship rule, out of scope for us. |
| 3 — Tripwire triage | 20 min | Read by category, not linearly. Hedge → **L05, L09** (referee discretion, "egregious"). Counting → **L11, L15**. Timers → **L10, L12, L13**. Carve-outs → **L04, L07**. Scored-live-vs-at-end → **L01** (the highest-yield group, exactly as the playbook predicts). |
| 4 — Zone geometry → T6 | 20 min | Figures 9-2, 9-3, 10-1, 10-3 read. Produced **L08** (the "in a zone" quantifier), **L02** (BASE ZONE sits outside both LAUNCH ZONES), **L07** (blue's GATE ZONE sits inside red's SECRET TUNNEL ZONE). **Blocked** on Figures 11-2/11-3/11-4 (pp. 112–114) and 12-1/12-2 (p. 123) — not rendered into the bundle. See Beta feedback item 5. |
| 5 — Compounding question → T5 | 10 min | Answered: **CLASSIFIED/OVERFLOW is assessed once; PATTERN is assessed twice.** → **L01**. Leaked, see §0.1. |
| 6 — Structural cross-check | 20 min | Three seams found: §10.5.1 (binding) permits DEPOT de-scoring while the G211 orange box calls strategic de-scoring an automatic card (**L09**); the G210 orange box says being *pushed* into your own RAMP is still your foul (**L06**); G402 uses "completely within" where six sibling rules use bare "in" (**L08**). |
| 7 — Penalty arithmetic → T12 | 10 min | MINOR FOUL = 5 pts to the opponent, MAJOR FOUL = 15 pts to the opponent [MANUAL, Table 10-4]. Answered the uncomfortable question honestly: **yes**, G424/G425/G426 are flat 5-point MINOR FOULs with no per-second escalator, unlike G422 and G423 which have one. That is **L14**, and per playbook §5 it is reported as an EXPOSURE, not a plan. |

---

## 2. Findings table (playbook §7 format)

Ranked by value to us. `Conf.` = confidence that the text reads as stated (not that FIRST intends it).
Rows marked **EXPOSURE-ONLY** failed the playbook §5 driver's-meeting test and are recorded as things an
opponent may do to us, never as plans.

| ID | Rule id(s) | Type | What the text permits | Conf. | Our exposure | Our opportunity | Q&A? | Fallback if patched |
|---|---|---|---|---|---|---|---|---|
| **L01** | §10.5 A/B/C, §10.5.2, Table 10-2 | T5 | The same ARTIFACT on the RAMP is assessed for PATTERN **twice** — once at the end of AUTO, once at the end of TELEOP — at 2 pts each, while CLASSIFIED/OVERFLOW is assessed once | HIGH (leak-corroborated, §0.1) | A TELEOP-only robot cannot reach the PATTERN RP as cheaply as a rival with a colour-ordered AUTO | AUTO artifact placed in MOTIF order pays **7**, the same artifact in TELEOP pays **5** (arithmetic §3.1) | **YES — #1 submission** | Build for the 9-artifact ramp, not for 5. If PATTERN is counted once, AUTO artifacts still pay 3+2=5 and the colour-indexed magazine is unchanged |
| **L02** | R101, R105.A/B/C, G415, §10.5.3, G427 *Violation*, Table 10-2, Fig 9-2/9-3 | T6/T7 | The **only** net expansion the game grants is vertical to 38 in, in the final 20 s, outside LAUNCH ZONES — and the BASE ZONE is the one scoring location that satisfies all three. §10.5.3 allows BASE support to be **transitive**, and G427's own penalty text names "any ROBOT fully supported by the contacted ROBOT" | HIGH on text, MED on geometry | If a rival alliance stacks and we do not, we concede 10 pts of endgame bonus per match | Both robots fully returned = **30 pts** = 3.3 launch cycles (arithmetic §3.2). An 18×18 in BASE ZONE cannot hold two 18×18 in robots side by side — transitive support is the *only* route to the bonus | **YES — #2** | Both robots simply park: 10+10 = 20, bonus forfeited. A passive wedge ramp is a cheap part to delete |
| **L03** | Glossary LAUNCH, Glossary CONTROL, G416, G416 orange box | T1 | LAUNCH is defined as "propelled across the floor to a desired location or in a preferred direction"; CONTROL's herding clause uses the *identical* words. Read literally, **herding is LAUNCHING**, and G416 confines LAUNCHING to a LAUNCH ZONE or LAUNCH LINE | MED-HIGH that the collision exists | Our floor-herding intake used outside a LAUNCH ZONE is literally MINOR FOUL **per ARTIFACT**. The only thing saving it is `[ORANGE — NON-BINDING]` | None we should take. Design so we never deliberately move an ARTIFACT across the floor outside a LAUNCH ZONE | **YES — #3** | Intake-and-carry (CONTROL ≤3 per G408) instead of herd. Costs a few inches of approach, no mechanism change |
| **L04** | §9.8.3, §9.3, G425, G424.A, Fig 9-3 | T7 | Our **own** SECRET TUNNEL ZONE is where the **opponent's** RAMP discharges (§9.8.3: the GATE prevents CLASSIFIED ARTIFACTS "exiting the RAMP into the opposing ALLIANCE'S SECRET TUNNEL ZONE"), and it adjoins our own LOADING ZONE. G425 forbids an opponent *in our tunnel* from contacting us — one-way protection | HIGH | Symmetric: every OVERFLOW we launch and every gate-dump we make is delivered to *their* corridor | Park the intake at the mouth of our own tunnel and harvest their discharge. Up to 9 ARTIFACTS at once from one opponent dump = 9 × 3 = **27 pts** of free ammunition at near-zero travel | NO (text is explicit) | Not patchable against us — this is a driving pattern, not a mechanism. If discharge is re-routed we lose a positioning preference only |
| **L05** | §9.8.3, G417.B, G412 orange box, T301 orange box, §10.5.2 | T12 | You may hold your own GATE open, but **may never apply closing force to either GATE** (G417.B, MAJOR FOUL). §9.8.3: after opening the GATE "may or may not stay open." A GATE that sticks open is `[ORANGE]` **not** FIELD damage (G412 box) and `[ORANGE]` **not** an ARENA FAULT (T301 box) | HIGH on the chain, but 2 of 4 links are `[ORANGE — NON-BINDING]` | **EXPOSURE-ONLY.** Dump the ramp late, the gate sticks, PATTERN requires ARTIFACTS "retained by the GATE" → **all PATTERN points gone, no legal fix, no replay** | None. This is a risk to price, not an edge | **YES — #4** ("is a stuck-open GATE that voids PATTERN an ARENA FAULT?") | Set a hard "last dump" clock (§3.5) and design a PATTERN rebuild that fits inside it |
| **L06** | G418, G418 orange box Ex.1–3, G210 orange box A | T11 | `[ORANGE — NON-BINDING]` G210's box says a red ROBOT pushing a blue ROBOT into an ARTIFACT on the **red** RAMP is "standard gameplay" and not a G210 violation — so the **pushed** robot still eats G418 at MAJOR FOUL per ARTIFACT | MED (rests on an orange box) | **EXPOSURE-ONLY.** Loitering beside either RAMP means an opponent can shove us into it and we pay 15 pts per ARTIFACT. G418 Ex.3 prices the worst case at **6 × 15 = 90 pts** | None. Deliberately inducing this on an opponent fails playbook §5 and is not proposed | **YES — #5** ("who is penalised under G418 when contact is caused by an opponent's push?") | Approach the GATE perpendicular, put the gate-pusher on the face away from the RAMP, never idle beside a RAMP |
| **L07** | G424, G424.A, G425, G423 orange box D, Fig 9-3 | T7 | Fig 9-3 shows blue's **GATE ZONE sits inside red's SECRET TUNNEL ZONE**. G424.A strips protection from a robot in its own GATE ZONE while in the opponent's tunnel; G425 restricts only the robot that is *in the opponent's* tunnel. Net: a red robot in **its own** tunnel may legally contest a blue robot at blue's GATE | MED-HIGH | **EXPOSURE-ONLY** for us to receive: our gate access can be legally contested, bounded only by G423 (`[ORANGE]` box D: "completely blocking access to the opponent's GATE") | None taken. Budget time for a contested gate instead of assuming free access | **YES — #6** | Build a gate actuator that works from a shallow angle and needs <1 s of contact — GATE travel is ~2 in (§9.8.3) |
| **L08** | G402.A vs G414/G415.B/G424/G425/G426/G427; §9.3 zone definitions; R101 | T6 | "In a ZONE" is **never quantified**. G402.A says "completely within"; six sibling rules say bare "in". Zones are "infinitely tall volumes" that "include the tape lines" (§9.3) | HIGH that the ambiguity is real | Every boundary call in the match is a referee judgement we cannot appeal (T201: no video review) | The internal-consistency argument settles it *for us*: a GATE ZONE is 2.75 × 10 in and a SECRET TUNNEL ZONE is 6.125 in wide (§9.3), while R101 caps a ROBOT at an 18 in cube — **no ROBOT can ever be "completely within" either**, so G424/G425 must mean *partially*, and by parity so must G415.B (arithmetic §3.4) | **YES — #7, highest single-question yield** | Design margin: treat every zone edge as ±3 in and never park on a line. Costs nothing either way |
| **L09** | §10.5.1 (binding), G419 orange box, G211 orange box D, T201 | T12 | §10.5.1 says in binding prose: "DEPOTS are not protected zones, and either ALLIANCE can remove ARTIFACTS from either DEPOT during the MATCH," and DEPOT points accrue to the owner "without regard to which ALLIANCE placed the ARTIFACTS." But `[ORANGE]` G211 box D makes "descoring SCORING ELEMENTS strategically or REPEATEDLY" an automatic YELLOW/RED | LOW that sweeping is safe | **EXPOSURE-ONLY.** Our DEPOT can be swept at 0:01 and the points simply never exist — DEPOT is assessed after the MATCH (§10.5 D) | Incidental only: a missed shot resting over the DEPOT scores 1 [Table 10-2]. Not worth building for — 3 placed = 3 pts/trip vs 9 pts/trip launched (§3.6) | **YES — #8** | None needed. We do not build for DEPOT; we do not sweep theirs |
| **L10** | G427, Fig 11-4 caption (via G426 orange box) | T3 | G427's BASE ZONE protection exists **only** "during the last 20 seconds." For the first 1:40 of TELEOP the BASE ZONE is an ordinary piece of floor. Separately, the Fig 11-4 caption reads "G426 Examples (**before the last 20 seconds of the match**)" although G426 contains no time clause — an unexplained seam | HIGH on G427; the caption is unresolved | **EXPOSURE-ONLY.** An opponent may sit in our BASE ZONE from 2:00 to 0:20 and we cannot foul them out of it. (We *may* push them — they are not in *their* BASE ZONE, so G427 does not bind us — but G420/G421/G422 still do) | None | **MAYBE — #9** (what the Fig 11-4 caption means) | Plan the endgame approach for 0:20 and assume the zone is occupied; the wedge/park sequence must tolerate a shove |
| **L11** | G434, G434 orange box, §10.3.1, §9.9, §10.5.2 | T4 | G434 is a **storage** cap, not a possession cap: ">6 ARTIFACTS out of play" per ALLIANCE, and the pre-stage is exactly 6 per ALLIANCE AREA (§10.3.1). Greens are scarce — 12 green vs 24 purple (§9.9) — and a 9-index PATTERN needs 3 greens (§10.5.2: MOTIF = 2P + 1G). Withholding ≤6 greens is a PATTERN-denial play the binding text permits | MED | **EXPOSURE-ONLY.** The intent ("prevent an ALLIANCE from starving the FIELD") and the escalation to G211 live **only** in an `[ORANGE — NON-BINDING]` box; the binding text says ">6" and nothing else | None. Fails playbook §5 flatly | **YES — #10** | Defensive design only: build the PATTERN early rather than depending on late green supply |
| **L12** | §10.5 A/B, Glossary MATCH, G403, Table 9-1 | T3/T5 | The 8-second AUTO→TELEOP transition is a **settling window**: "ARTIFACTS that meet scoring criteria prior to the start of TELEOP are assessed as part of AUTO" (§10.5 A), and AUTO PATTERN is assessed when all ARTIFACTS come to rest after AUTO "**or the start of TELEOP, whichever comes first**" (§10.5 B) | HIGH on the window | A robot still rolling an ARTIFACT down the RAMP at TELEOP start gets an **undefined** PATTERN index. G403 makes any powered movement in the transition a MAJOR FOUL and names LAUNCHING and gate operation as escalating to G211 | A shot released at 0:30.0 that clears the SQUARE during the transition scores as **AUTO** — worth +2/artifact via L01 | **YES — #11** (the mid-roll case) | Fire the last AUTO shot by ~0:27 so it settles well inside the window. No mechanism cost |
| **L13** | §10.5 A, G404, G404 orange box | T3 | CLASSIFIED/OVERFLOW assessment "continues until all ARTIFACTS have come to rest **following the conclusion of the MATCH**" (§10.5 A). G404 penalises *LAUNCHING* after the end of TELEOP, not an ARTIFACT already in flight | HIGH | A referee judging release-versus-buzzer by eye, with no video review available (T201) | Keep firing to the buzzer, then cut **all** outputs — a still-powered flywheel is powered movement; the G404 box exempts only inertia, gravity and de-energising | LOW priority | Stop firing at 0:01. Costs at most one shot |
| **L14** | G424/G425/G426 vs G422/G423, Table 10-4, §10.6 | T12 | Playbook §2 Pass 7's uncomfortable question, answered honestly: G424, G425 and G426 are flat **MINOR FOULs (5 pts)** with **no per-3-second escalator**, whereas G422 (PIN) and G423 (shutdown) both carry "an additional MINOR FOUL for every 3 seconds." §10.6 says penalties are assessed "for each instance," and *instance* is undefined for sustained contact | MED (turns on the undefined word "instance") | **EXPOSURE-ONLY.** An opponent who parks against us inside our own LOADING ZONE may pay 5 pts once while denying multiple cycles. Escalation exists (G423 + G211) but is discretionary | None. This is the row that fails the driver's-meeting test hardest and it is recorded so we recognise it being done *to us*, not so we do it | **YES — #12** ("is sustained contact one instance or many under G426?") | Not applicable — no plan attached. Mitigation is to keep LOADING ZONE dwell short so denial has nothing to deny |

---

## 3. Arithmetic (playbook §2 and `ANALYSIS-PROTOCOL.md` H3 — operands shown)

All point values from `TABLES.md` Table 10-2 and Table 10-3 (p. 88). None from `full_layout.txt`, whose rendering
of the same table separates the labels from the values by several rows and is unusable.

### 3.1 L01 — the PATTERN premium
[MANUAL] Table 10-2: CLASSIFIED = 3 (AUTO) / 3 (TELEOP); OVERFLOW = 1 / 1; PATTERN "ARTIFACT matches MOTIF" = 2 (AUTO) / 2 (TELEOP).
[MANUAL] §10.5 A: CLASSIFIED/OVERFLOW assessed once, in the period in which it met criteria.
[MANUAL] §10.5 B and C: **two separate** PATTERN assessments — end of AUTO, and end of TELEOP.
[MANUAL] §10.5.2: "At the end of AUTO **and** TELEOP, ARTIFACTS that are directly on the RAMP score for PATTERN points…"

- [DERIVED] One correctly-indexed ARTIFACT placed in AUTO and left alone: `3 (CLASSIFIED) + 2 (AUTO PATTERN) + 2 (TELEOP PATTERN) = 7`
- [DERIVED] The same ARTIFACT placed in TELEOP: `3 + 2 = 5`
- [DERIVED] Premium for AUTO placement: `7 − 5 = 2 points per ARTIFACT`. Three preloads (§10.3.1 permits up to 3): `3 × 2 = 6 points`
- [DERIVED] PATTERN RP threshold, All Other Events = 18 [Table 10-3]. Under the two-assessment reading, `5 × 2 + 5 × 2 = 20 ≥ 18` — **five** correctly-indexed ARTIFACTS placed in AUTO and retained earn the PATTERN RP outright. Under a one-assessment reading you need `9 × 2 = 18` — **the whole ramp**.
- [JUDGMENT] Design for 9, not 5. That is the "design so either ruling leaves you standing" move from playbook §0.

### 3.2 L02 — the endgame premium and the 18-inch impossibility
[MANUAL] R101: STARTING CONFIGURATION ≤ 18 × 18 × 18 in. R105.A: horizontal expansion must stay "within a fixed 18 in. by 18 in.", **physically constrained, "without the use of software"**. R105.B: normal vertical ≤ 18 in. R105.C + G415: vertical to 38 in only (A) in the final 20 s and (B) not in any LAUNCH ZONE.
- [DERIVED] Starting envelope 18×18×18 and expanded envelope 18×18×18 are the same box. **The game grants exactly one net expansion privilege: 38 in vertical, last 20 s, outside LAUNCH ZONES.**
- [DERIVED, Fig 9-2 + Fig 9-3] Both BASE ZONES sit in the middle band of the FIELD, clear of the 6-tile × 3-tile goal-side LAUNCH ZONE and the 2-tile × 1-tile audience-side one. So the one expansion window is usable precisely where BASE scoring happens. **Confidence MEDIUM — verify against the official FIELD drawings; Figures 12-1/12-2 were not rendered into the bundle.**
- [MANUAL] §10.5.3: "A ROBOT fully returned to BASE must only be supported, **either directly or transitively**, by the TILE in the BASE ZONE."
- [MANUAL] G427 *Violation*: "…opponent ROBOT **and any ROBOT fully supported by the contacted ROBOT** are awarded fully returned to BASE points." The manual's own penalty text contemplates one ROBOT fully supported by another inside a BASE ZONE.
- [DERIVED] BASE ZONE = 18 × 18 in (§9.3); a ROBOT's maximum footprint = 18 × 18 in (R101). `18 × 18 in` cannot contain two `18 × 18 in` footprints side by side. Therefore, for two maximum-size robots, **transitive support is the only route to the "2 ROBOTS fully returned" bonus.**
- [DERIVED] Endgame value: `10 (full) + 10 (full) + 10 (bonus) = 30 TELEOP points` [Table 10-2].
- [DERIVED] One 3-ARTIFACT launch cycle at CLASSIFIED value: `3 × 3 = 9 points`. Endgame premium: `30 ÷ 9 = 3.3 cycles`.
- [DERIVED] MOVEMENT RP threshold, All Other Events = 16 [Table 10-3]; MOVEMENT RP = LEAVE + BASE points. Both robots LEAVE + both partial: `3 + 3 + 5 + 5 = 16` — exactly the threshold. One robot alone at its best: `3 + 10 = 13 < 16`. **MOVEMENT RP is unreachable by a single working robot; a dead partner kills it.**

### 3.3 L04 / the gate-dump economics
[MANUAL] §9.8.2: the RAMP "can fit up to 9 CLASSIFIED ARTIFACTS before newly entered ARTIFACTS will OVERFLOW."
[MANUAL] G418.A: ROBOTS may not remove an ARTIFACT from their own RAMP "**except by operating the GATE**" — the carve-out is explicit and enterable on purpose.
[MANUAL] §10.1: "ROBOTS can then open their GATE to continue CLASSIFYING additional ARTIFACTS."
- [DERIVED] With a full RAMP, the next ARTIFACT is worth 1 (OVERFLOW). After a dump it is worth 3 (CLASSIFIED). Clearing 9 slots is worth `9 × (3 − 1) = 18 points` on the next nine ARTIFACTS.
- [DERIVED] Cost side: those nine dumped ARTIFACTS exit into the **opponent's** SECRET TUNNEL ZONE (§9.8.3), adjacent to the opponent's LOADING ZONE (§9.3, Fig 9-3) — we hand them nine ARTIFACTS worth `9 × 3 = 27` to them if they recover all of them. Plus the L05 stuck-gate risk, plus rebuild time.
- [JUDGMENT] Dump early, never late. See §3.5.
- Note: GOAL RP counts "ARTIFACTS scored **through the SQUARE**" [Table 10-2], and **both** CLASSIFIED and OVERFLOW pass through the SQUARE (§10.5.1). So dumping is not required for GOAL RP and there is **no GOAL-vs-PATTERN RP conflict** — a claim I drafted and then withdrew when I re-read §10.5.1. Recording the retraction because it is the kind of error this method is meant to catch.
- [DERIVED] GOAL RP threshold, All Other Events = 36 [Table 10-3]; total ARTIFACTS in a MATCH = 24 P + 12 G = 36 (§9.9). **The GOAL RP threshold equals the entire ARTIFACT supply**, contested by both alliances. It is only reachable by recycling ARTIFACTS through the SQUARE more than once, which is what the discharge loop in L04 physically is.

### 3.4 L08 — why "in" must mean "partially in"
[MANUAL] §9.3: GATE ZONE = 2.75 in × 10 in infinitely tall volume; SECRET TUNNEL ZONE ≈ 46.5 in × 6.125 in infinitely tall volume. Both "include the tape lines."
[MANUAL] R101: a ROBOT is at most 18 × 18 in.
- [DERIVED] `6.125 in < 18 in` and `2.75 in < 18 in`. No legal ROBOT can be *completely within* either zone. Under a "completely within" reading, **G424 and G425 would be dead letters** — they could never be violated. Therefore the manual must intend "partially in."
- [DERIVED] By parity, G415.B ("when **not in any** LAUNCH ZONES") must also mean *not partially in* — so a ROBOT overlapping a LAUNCH LINE by any amount in the final 20 s may not exceed 18 in vertical. This is the practical consequence we must design to, and it is the reason L02's BASE-ZONE geometry claim needs the official drawings.
- [MANUAL] G402.A is the control case: it says "completely within the opposing ALLIANCE'S side of the FIELD." The drafters used the precise quantifier exactly once, which is what makes its absence elsewhere meaningful.

### 3.5 L05 — the last-dump clock
- [MANUAL] TELEOP = 2:00 (Glossary MATCH; Table 9-1). PATTERN requires ARTIFACTS "retained by the GATE" (§10.5.2). TELEOP PATTERN is assessed only at the end (§10.5 C).
- [DERIVED] Maximum TELEOP PATTERN at stake: `9 × 2 = 18 points`, plus the PATTERN RP (threshold 18 at All Other Events).
- [JUDGMENT — no cycle-time data exists anywhere in the bundle] A 9-ARTIFACT rebuild in MOTIF order requires at minimum three LOADING ZONE reloads of 3 (G408 caps CONTROL at 3) plus nine aimed launches. At an assumed 12 s per 3-ARTIFACT cycle that is ~36 s. **Last safe dump ≈ 0:45**, and any dump after ~0:30 should be treated as forfeiting TELEOP PATTERN. This number is a placeholder until we have measured cycle time — it is `[JUDGMENT]`, not `[DERIVED]`.

### 3.6 L09 — why DEPOT is not worth building for
- [MANUAL] Table 10-2: DEPOT = 1 (TELEOP only). CLASSIFIED = 3.
- [DERIVED] Three ARTIFACTS deposited on one trip = `3 × 1 = 3 points`. The same three launched and CLASSIFIED = `3 × 3 = 9 points`. DEPOT is worth `3 ÷ 9 = 1/3` of the launch value for the same trip.
- [JUDGMENT] DEPOT is a consolation for a robot that cannot launch and a home for missed shots that come to rest over the tape. It is not a strategy.

### 3.7 The GOAL lip — a deliberate, closed door
- [MANUAL] §9.7: "The top lip of the GOAL is 38.75 in. (98.45 cm) from the surface of the TILE."
- [MANUAL] R105.C: maximum legal vertical expansion 38.00 in, and only under G415 (last 20 s, outside LAUNCH ZONES).
- [DERIVED] `38.75 − 38.00 = 0.75 in`. **A legal ROBOT cannot reach over the GOAL lip, by three quarters of an inch, and could not do so before 0:20 in any case.** Placement into the GOAL is designed out. You must LAUNCH. This looks like a loophole for about ninety seconds and is not one — recorded so nobody spends a week on it.

---

## 4. Closed doors (things that look like loopholes and are already shut)

| Idea | Why it is shut |
|---|---|
| Collude with the opposing alliance so both gates get disrupted and **both** alliances take the PATTERN RP | G206 forbids it directly (YELLOW CARD + ALLIANCE ineligible for PATTERN **and** GOAL RPs), and the G206 orange box uses this exact scenario as its worked example. Also G203/G204/G205. |
| Run our two robots as a swap pair at one event | I302: each team may inspect and play MATCHES with **1 ROBOT** at an event, and may participate in 1 concurrent event. I305 allows playing with a *subset of already-inspected MECHANISMS* only. Our two robots are two separately registered teams — that is the legal route, and it is the route `playbook/TWO-ROBOT-PROGRAM.md` already assumes. |
| Dump ARTIFACTS into the opponent's DEPOT to get them out of play | `[ORANGE]` G419's box says "There is no violation for scoring in an opponent's DEPOT" — but §10.5.1 (binding) awards DEPOT points to the **owner** "without regard to which ALLIANCE placed the ARTIFACTS." It is a gift, not a trick. |
| Wedge a SCORING ELEMENT to hold our GATE open so the RAMP self-clears | `[ORANGE]` G405 box example C names it explicitly; G405 is MAJOR FOUL **per SCORING ELEMENT**. |
| Reach over the GOAL lip and place instead of launching | §3.7 above — short by 0.75 in, and time-gated to the last 20 s regardless. |
| Score during the AUTO→TELEOP transition | G403: MAJOR FOUL, and its `[ORANGE]` box names LAUNCHING and gate operation as *strategic* violations escalating to G211 (YELLOW/RED). L12 is the legitimate version — settle a shot fired *before* 0:30. |
| Select an AUTO OpMode after seeing the MOTIF | The OBELISK is randomised **after** DRIVE TEAM setup (§9.6), and G401 bars all OPERATOR CONSOLE interaction from the moment randomisation begins. The MOTIF must be read by on-robot vision (AprilTag IDs 21/22/23, §9.10). Not a loophole — a hard requirement. |

---

## 5. Q&A submission queue (playbook §5 — opens 28 September 2026, 12:00 ET, Lead Coach 1/2 account)

Ordered by expected yield. Send to the submission drafter (`REVIEW-PROMPTS.md`).

1. **L01** — Is an ARTIFACT that is on the RAMP and matching the MOTIF at the end of AUTO *and* at the end of TELEOP awarded PATTERN points under both §10.5 B and §10.5 C?
2. **L02** — Does a ROBOT whose support passes transitively through a partner ROBOT that is itself fully supported by the TILE in the BASE ZONE qualify as "fully returned to BASE" under §10.5.3?
3. **L03** — Is "herding" as defined in the CONTROL glossary entry also "LAUNCHING" under the LAUNCH glossary entry, and therefore restricted by G416?
4. **L05** — If a GATE sticks open after normal ROBOT operation and the ALLIANCE consequently scores zero PATTERN points, is that an ARENA FAULT under T301?
5. **L06** — When an opponent ROBOT pushes our ROBOT into ARTIFACTS on our own RAMP, which ALLIANCE is penalised under G418?
6. **L07** — May a ROBOT positioned in its **own** SECRET TUNNEL ZONE contact an opponent ROBOT that is in that opponent's own GATE ZONE?
7. **L08** — For G415.B, G424, G425, G426 and G427, does "in" a ZONE mean partially in, fully in, or contacting? (G402.A uses "completely within"; these do not.)
8. **L09** — Does removing an opponent's ARTIFACTS from their DEPOT, permitted by §10.5.1, constitute "descoring SCORING ELEMENTS strategically" under the G211 orange box?
9. **L10** — Why is Figure 11-4 captioned "before the last 20 seconds of the match" when G426 contains no time condition?
10. **L11** — Does G434 permit an ALLIANCE to keep 6 ARTIFACTS out of play for the entire TELEOP?
11. **L12** — How is PATTERN index assessed for an ARTIFACT still travelling down the RAMP at the start of TELEOP (§10.5 B, "whichever comes first")?
12. **L14** — Is sustained contact under G426 one "instance" (§10.6) or one instance per unit time?

---

## 6. Two-robot filter (playbook §4) and ethics disposition (playbook §5)

**Calibration:** ~15 students, two registered teams, two robots, modest budget, hand tools + 3D printing, no CNC.
Every mechanism is built twice.

| Finding | Build it twice? | Survives a patch? | Award evidence? | Verdict |
|---|---|---|---|---|
| L01 (colour-ordered 3-slot AUTO magazine) | **Yes** — three indexed slots and three gates; printable, no hand-tuning | Yes — value drops from 7 to 5 per ARTIFACT, mechanism unchanged | **Yes** — Innovate/Control (MOTIF vision → firing order is a clean control story) | **Design commitment** |
| L02 (passive wedge ramp for a partner) | **Yes** if passive. A powered lift does **not** duplicate on our budget | Yes — delete the wedge, both robots still park for 20 pts | **Yes** — Design | **Design commitment, passive only** |
| L03 (never herd outside a LAUNCH ZONE) | n/a — a rule, not a part | n/a | Neutral | **Design constraint** |
| L04 (harvest our own SECRET TUNNEL) | **Yes** — a driving pattern, free to duplicate | Not patchable against us | Weak (strategy, not build) | **Strategy commitment** |
| L05 (last-dump clock) | n/a | n/a | Neutral | **Match-plan rule** |
| L06, L07, L09, L10, L11, L14 | — | — | — | **EXPOSURE-ONLY.** Recorded so we recognise them being done to us. None is proposed as a plan. |

**Ethics test applied.** Playbook §5: *would you explain this, unprompted, to the referee at the driver's meeting
and to a judge in your interview?* L01, L02, L03, L04, L05, L12, L13 — **yes**, all of them, comfortably; they are
reading the manual carefully and designing to its text. L06, L07, L09, L11, L14 — **no**, and they are therefore
reported as exposures rather than plans, exactly as the brief requires. L14 in particular (a flat 5-point foul
being cheaper than the scoring it denies) is the one the playbook §2 Pass 7 tells you to find and then warns you
about; it is written down here and it is going no further.

**The tactical argument, restated for our situation:** everything in the Design-commitment rows is describable out
loud in a portfolio. Nothing in the EXPOSURE-ONLY rows is. Since the Inspire path is the cheapest advancement
points available to a two-team program, the incentives and the ethics point the same way.

---

## 7. What would change all of this

Playbook §0: assume every one of these is patched by a Team Update. The fallback column is populated for every
row that carries an opportunity; the two rows with real design commitments (L01, L02) both degrade to *fewer
points from the same hardware* rather than *hardware we cannot use*. No finding in this document is a design
commitment without a fallback, per playbook §7.

---

## Beta feedback

Ordered by how much they cost me. Items 1 and 2 are structural; the rest are bundle defects.

1. **An allowed method file contains the answer key.** `reference/LOOPHOLE-PLAYBOOK.md` §2 Pass 5 states DECODE's
   Q&A Q27/Q129 outcomes verbatim — that is the single highest-yield finding of the whole phase, handed to me
   before Pass 1 ran. §3 likewise pre-supplies DECODE's G422 3-second pin count. The forbidden-file list is
   therefore incomplete: the leak was inside a file the brief instructed me to read first. **Fix:** strip every
   season-specific example out of the method files into the casebook, and replace them with placeholders
   ("Season A: X doubled; Season B: it did not"). I have flagged L01 as LEAKED-CORROBORATED rather than claiming
   it, but a less scrupulous run would simply have reported it as a find and the test would have scored itself.

2. **The test manual is TU32, i.e. fully patched.** `STATUS.md` discloses the source as
   `DECODE_Competition_Manual_TU32.pdf`. Playbook Pass 2 rests on "new rules are unpatched rules," which is false
   for a post-Team-Update document: the kickoff-day ambiguities are exactly the ones that have already been
   closed and are now invisible. This run therefore **cannot** validate the thing it is meant to predict. On
   2026-09-12 the input will be V0/V1 and I expect substantially more T1 (undefined-term) and T3 (timer) yield
   and far less orange-box guidance, because orange boxes accumulate across the season. **Fix:** re-run this beta
   against the earliest archived version of the same manual and diff the two finding sets — the difference *is*
   the measurement you actually want.

3. **The T1–T15 taxonomy is unavailable to a compliant run.** The §7 output format mandates a "taxonomy type"
   column, but the playbook explicitly puts the taxonomy in `LOOPHOLE-CASEBOOK.md`, which is forbidden. I could
   reconstruct only 8 of 15 types from the playbook's Pass-3 mapping table (T1, T2, T3, T4, T5, T6, T7, T11, T12)
   and deliberately did **not** use T13/T14/T15 rather than invent meanings for them. **Fix:** move the bare
   taxonomy — names and one-line tells, no season examples — into the playbook.

4. **Figures are rendered for pages 58–94 only, which omits every figure the loophole hunt needs.**
   Pass 4 is *"With `figures/*.png` open"*, and the three figures that define the protected-zone boundary cases —
   Figure 11-2 (G424), 11-3 (G425), 11-4 (G426), pp. 112–114 — are not in the bundle, nor are Figure 12-1/12-2
   (R105 expansion limits, p. 123). Those five figures govern five of my twelve findings. **Fix:** render every
   page containing a caption matching `/Figure \d+-\d+/` that is referenced from a rule body, not just §9 and §10.
   My L02 geometry claim is stuck at MEDIUM confidence solely because of this.

5. **`rules_full.tsv` truncates the `violation` column and bleeds bodies across section boundaries.**
   G402's Violation reads `"…MAJOR FOUL per ARTIFACT in"` — the trailing `"G402.B."` was severed and appended to
   the body; G419 is broken identically. `VIOLATIONS.tsv` carries the *same* truncation, so there is no clean
   source for the full penalty sentence and I had to reconstruct it from `full_layout.txt` — the file the brief
   calls a last resort. Separately: G434's body contains the entire 740-word Section 12 preamble; R105's body
   swallows the "12.2 ROBOT Safety" heading; C501's body is **empty** despite `n_words=1973`; and G430/G431 and
   G433/G434 have their headlines and bodies mis-paired. The brief warns that flat text mis-pairs labels and
   numbers — it also mis-pairs **rule IDs**, and that defect has propagated into the structured TSV.

6. **No glossary-coverage artifact, so Pass 1 has to be done by hand.** Pass 1 asks which ALL-CAPS terms appear in
   binding rules but not in Section 16. Nothing in the bundle answers it. I regexed the Term column out of
   `full_layout.txt` and diffed manually. `caps_NOVEL_ranked.txt` is frequency-only and roughly half noise —
   WPI, JST, BNO, NADO, SKU, GPT, CDT, NZS, NMH, HLS, DFR, OAK, `ARTFACTS` (a typo in the manual), `DECODETM`.
   **Fix:** emit `caps_UNDEFINED.txt` = (ALL-CAPS tokens in G/R/I rule bodies) − (Section 16 Term column), with
   the citing rule ID on each line. That is a ten-line script and it *is* Pass 1.

7. **`TABLES.md` has no index and no backlinks.** It recovered Table 10-2 correctly and the house rule about
   never trusting the flat text is fully justified — `full_layout.txt` renders the same table with the labels in
   one block and the values in another, off by several rows, so `LEAVE 3 / ARTIFACT / PATTERN CLASSIFIED 3 3`
   reads as nonsense. But I scanned 100+ `## p.NN` headers to find the two tables that mattered. **Fix:** a
   `tables_INDEX.md` with caption, page and first-column terms.

8. **`TRIPWIRES.txt` gives line numbers with no rule ID and one line of context**, so every hit costs a second
   lookup into `full_layout.txt`. It is the right idea and the categories are well chosen — the scored-live
   category alone produced L01 — but emitting `rule_id ⇥ category ⇥ matched_phrase ⇥ ±2 lines` would make it
   readable linearly instead of forcing ~40 random-access lookups.

9. **`ORANGE_BOXES.md` mis-attributes boxes across section boundaries.** Twelve consecutive boxes spanning
   pp. 70–88 — including the RAMP/OVERFLOW box, the GATE-timing box and the DEPOT-CONTROL box, three of which
   are load-bearing in this document — are all labelled **"after A215"**, an Awards rule twenty sections away.
   Since the entire purpose of that file is knowing *which rule* a piece of non-binding text attaches to, the
   attribution being wrong is not cosmetic. **Fix:** attribute by section number from the page footer
   ("Section 9 ARENA V8") rather than by nearest preceding rule ID.

10. **Nothing in the bundle supports a points-per-second calculation.** The §7 format demands "our exposure /
    our opportunity" and playbook §3 demands points ÷ full cycle seconds, but there is no cycle-time input, no
    travel-distance table and no prior-season baseline available to a compliant run. Every rate number in §3.5
    is `[JUDGMENT]` as a result. **Fix:** either add a game-agnostic `CYCLE-TIME-PRIORS.md` to the method set, or
    drop the rate requirement from R6 and move it wholly into R4/R5 where measurement data exists.

11. **The §7 row spec has nowhere to put the §4 two-robot filter.** Nine columns and none of them is
    "buildable twice?" — so the filter that the playbook calls the thing "the rest of the FTC internet ignores"
    ends up in prose after the table (my §6) where a script parsing the table will not see it. **Fix:** add a
    tenth column, or make §4 an explicit second table in the §7 spec.

---

*R6 output. Feeds the R7 pitfall register. Q&A queue in §5 goes to the submission drafter. Findings marked
EXPOSURE-ONLY are not plans and must not be promoted into R7 as strategy.*

*Produced with AI assistance; per BIOBUZZ A201 any of this reaching a team PORTFOLIO needs the footnote credit.*
