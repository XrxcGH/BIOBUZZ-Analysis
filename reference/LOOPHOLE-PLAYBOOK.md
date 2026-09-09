# LOOPHOLE PLAYBOOK — how to hunt, not what was found

### The method for phase R6 of `ANALYSIS-PROTOCOL.md`. Evidence lives in `research/LOOPHOLE-CASEBOOK.md`; this file is the procedure.

**Read the casebook first, once.** It carries 10 flagship cases, the full mid-season modification
ledger (**60 distinct rules edited in INTO THE DEEP across TU00–TU13; 38 in DECODE across TU00–TU30**),
and the **T1–T15 taxonomy** with each type's tell. This file does not repeat any of it. It tells you
what to *do* on kickoff day with a manual nobody has read yet.

**Calibration target.** ~15 students, two registered teams, two robots, modest budget. That shapes the
final judgement: an edge you cannot build twice, or cannot rebuild when it is patched, is not an edge.

---

## 0. The one paragraph that matters

A "loophole" in FTC is almost never a secret exploit. It is **an ambiguity that FIRST has not yet
resolved**, and the ledger above proves FIRST resolves them fast — 60 and 38 rules patched in the two
most recent seasons, several within twelve days of kickoff. So the goal of this phase is *not* to find
a trick and hide it. The goal is to **find the ambiguities before your competitors, decide which way
FIRST will rule, design so that either ruling leaves you standing, and file the question in the Game
Q&A so the ruling comes early and in writing.** A favourable Q&A answer you can show a referee is worth
more than a secret that evaporates on the first Thursday.

---

## 1. Inputs, and the order to read them

| # | Input | From | What you are looking for |
|---|---|---|---|
| 1 | `rules_GAMESPECIFIC.txt` | R1 ingest | The orange-headline rules. **Start here every time** — 17 of 214 in DECODE. New rules are unpatched rules |
| 2 | `rulebodies/G_rules_full.tsv` | R1 ingest | Full G-rule bodies + `Violation:` lines. Ambiguity lives in the body, not the headline |
| 3 | `rulebodies/ORANGE_BOXES.md` | R1 ingest | **Non-binding commentary.** Where the manual *explains* a rule it is often admitting the rule is unclear |
| 4 | `tables/TABLES.md` | R1 ingest | The scoring table by geometry. Never the flat text |
| 5 | `TRIPWIRES.txt` | R1 ingest | ~343 candidate lines on a DECODE-sized manual, pre-grepped by category |
| 6 | `caps_NOVEL.txt` | R1 ingest | Every new defined term. **An undefined new term is T1, the most productive type** |
| 7 | `figures/*.png` | R1 ingest | Zone geometry. T6 boundary questions are invisible in text |

---

## 2. The seven passes

Run them in this order. Each is timeboxed; the whole phase is ~2 hours on kickoff day.

### Pass 1 — Novel terms (15 min) → type T1
For every token in `caps_NOVEL.txt`, ask: **is it defined in Section 16?** Build the list of terms that
appear in binding rule text but are absent from the glossary. In BIOBUZZ V0 this is already non-empty —
`MATCH`, `FIELD`, `SCORING ELEMENT` and `FABRICATED ITEM` are used in binding rules and defined nowhere
(see `RULE-TAXONOMY.md`). Every undefined term is a question you can file on 28 September.

### Pass 2 — The orange rules (25 min)
Read all ~15–20 game-specific rules end to end, bodies included. For each, write one sentence: *what
behaviour is this rule trying to prevent, and what adjacent behaviour does it therefore permit?* The
second half of that sentence is the finding. Case 1 in the casebook (ITD G427) is the canonical shape:
a rule written to protect you becomes a weapon when you enter the protected zone deliberately.

### Pass 3 — Tripwire triage (20 min)
`TRIPWIRES.txt` is grouped by category already. Do not read it linearly — read it **by category against
the taxonomy**:

| Tripwire group | Taxonomy type | The question to ask |
|---|---|---|
| Hedge words (`generally`, `egregious`, `strateg*`, `at the discretion`) | T1, T12 | Who decides, and what evidence do they use in a 2½-minute match? |
| Counting words (`at a time` vs `at any time`, `no more than`) | T2, T4 | Is the limit instantaneous or cumulative? Does releasing and re-acquiring reset it? |
| Timers (`within`, `for more than`, `continuous`, `cumulative`) | T3 | Does the clock reset? Who starts it? Is it symmetric between alliances? |
| Carve-outs (`unless`, `except`, `does not apply`, `provided that`) | T7, T11 | Can you *enter* the exception on purpose? |
| Scored-live vs at-end | T5 | **Highest-value single line in the manual — see Pass 5** |

### Pass 4 — Zone geometry (20 min) → type T6
With `figures/*.png` open. For every named zone: is the boundary **the tape, the projection, or the
volume**? Does "in" mean fully, partially, or contacting? What happens to a robot straddling it? What
happens to a scoring element straddling it? The casebook's Case 4 (R105 expansion, inspection-time vs
match-time) is the recurring version of this and it appeared again in DECODE.

### Pass 5 — The compounding question (10 min) → type T5
Find the sentence that says whether AUTO scoring is evaluated **live** or **at the end of the period**,
and whether AUTO-scored elements are **re-counted** in the final score. `SCORING-PATTERNS.md` documents
that this single sentence inverted AUTO strategy between ITD and DECODE: ITD Q&A Q21 confirmed every
AUTO element doubled (high chamber = 20), DECODE Q&A Q27 confirmed artifacts do **not** double while
Q129 confirmed PATTERN does. **Two manuals that look identical, opposite correct strategies.** If the
manual is not explicit, this is your first Q&A submission, filed 28 September at 12:00 ET.

### Pass 6 — Structural cross-check (20 min)
Different sections are written by different people. Look for the seams:

- A **scoring action in the table with no G-rule governing it** — is it really unregulated?
- A **G-rule referencing a term the glossary never defines** (Pass 1 output)
- An **R-rule permitting a mechanism a G-rule implicitly forbids** (or vice versa) — e.g. R801 permits
  gas shocks; does any G-rule constrain stored-energy launching?
- A **penalty with no defined detection** — if a referee cannot see it, it is not enforced in practice
- An **orange box that contradicts the rule it explains** — the rule governs; the box does not. This is
  a real hazard because the two are typographically identical in flat text (`MANUAL-ANATOMY.md`)

### Pass 7 — Penalty arithmetic (10 min) → type T12
Fouls award points to the *opponent*, so a foul is worth more than its face value in a close match.
Build the table: for each foul tier, what does it cost, does it scale per-occurrence or per-match, and
does it escalate automatically on repetition? Then ask the uncomfortable question honestly: **is there a
rule where the penalty is cheaper than the scoring it prevents?** If yes, note it — and read §5 before
doing anything with it.

---

## 3. Strategy-space analysis

Separate from rule ambiguity, and usually worth more. Feeds `STRATEGY-RANKING-PROTOCOL.md` step D3.

**Points per second, not points.** For each scoring action compute `points ÷ full cycle seconds`,
where the cycle includes acquisition, travel, alignment, scoring and return. Alignment and travel
dominate; the scoring action itself rarely does. Show the operands — `ANALYSIS-PROTOCOL.md` H3 requires it.

**Find the underpriced objective.** In every season one objective pays disproportionately for its
difficulty and gets ignored because it looks unglamorous. `ROBOT-ARCHETYPE-LIBRARY.md` documents the
canonical case: ITD priced HIGH CHAMBER at 10 above HIGH BASKET at 8, while the basket lip sat at
43.0 in — the harder mechanism paid *less*. Ask directly: **which objective has the best
points-per-second that nobody will build for?**

**Is defense rational this season?** Only if the foul structure tolerates it. Compute the expected cost
of the fouls a defensive strategy incurs against the scoring it denies. Note that the casebook shows
pin limits tightening (ITD G423 5 s → DECODE G422 3 s), and that both `ROBOT-ARCHETYPE-LIBRARY.md` and
`AWARD-ALIGNMENT-MATRIX.md` mark dedicated defense **NOT RECOMMENDED** for a two-robot program — it
generates no award evidence and cannot be duplicated meaningfully.

**Stress the endgame clock.** If the endgame action is gated by a time condition, work out the latest
safe commit moment and what happens if you miss it. `SCORING-PATTERNS.md`: endgame absolute value fell
200 → 30 points across eleven seasons, but its premium stayed 6–20 cycles — and since 2021-22 every
season rewards *both* alliance robots doing it.

---

## 4. Two-robot filter

Before promoting any finding, apply the constraint the rest of the FTC internet ignores:

1. **Can we build it twice?** A mechanism needing individual hand-tuning does not duplicate.
2. **Does it survive a patch?** If a Thursday Team Update closes it, what is left of the robot? The
   ledger says assume it *will* be patched — DECODE TU01/TU02 nerfed two low-fabrication strategies
   within twelve days of kickoff.
3. **Does it generate award evidence?** Only Innovate, Control and Design respond to what you build
   (`AWARD-ALIGNMENT-MATRIX.md` §1.1). A clever exploit that produces no portfolio story costs you the
   cheapest advancement points on the board.

A finding that fails all three is a curiosity, not a plan.

---

## 5. Ethics, and the line

This section is not boilerplate. Get it wrong and you lose more than a match.

**Legitimate — do this.** Reading the rules more carefully than your opponent. Finding an objective the
field has underpriced. Noticing that a rule permits something useful and doing it openly. Filing a Q&A
question and playing to the answer. Designing for a rule's actual text rather than its vibe. This is
the game working as intended, and it is what engineering judgement *is*.

**Not legitimate — do not.** Anything whose value depends on a referee not noticing. Anything that
damages another robot or the field. Anything that relies on an opponent's inexperience rather than your
own preparation. Deliberately inducing an opponent to foul (casebook T11/Case 7) sits on this line and
usually over it. And note that BIOBUZZ adds **§1.5 the Competition Integrity Contract (CIC)** — new
this season, binding on every team, and explicitly referenced at V0 line 851 as grounds for mitigation.
Section 1.4 *The Spirit of the Competition* and Gracious Professionalism are not decorations; judges and
referees read them.

**The practical test.** Would you explain this strategy, unprompted, to the referee at the driver's
meeting and to a judge in your interview? If yes, build it. If you would rather they did not ask, you
already know.

**The tactical argument for honesty.** You must be able to explain your robot to win a judged award
anyway. A strategy you cannot describe out loud is a strategy that cannot appear in your portfolio,
which means it cannot earn the 60-point Inspire path. The incentives point the same way as the ethics.

**File it.** The Game Q&A opens **28 September 2026, 12:00 p.m. ET**, accessible through the Lead Coach
1 or 2 account only. Moderators answer from each Monday and close Thursday 5:00 p.m. ET. Q&A answers do
**not** supersede manual text and referees remain the final authority — but a written answer is the
strongest thing you can bring to a rules dispute. Draft submissions with the prompt in
`REVIEW-PROMPTS.md`.

---

## 6. The twenty questions to interrogate the BIOBUZZ manual with

Ordered by expected yield. Work down until the phase timebox ends.

1. Is AUTO scoring evaluated live or at the end, and are AUTO elements re-counted in the final score?
2. Which ALL-CAPS terms are used in binding rules but absent from Section 16?
3. What is the complete list of orange (game-specific) rules, and what does each one *permit*?
4. For every zone: tape, projection, or volume? Fully, partially, or contacting?
5. What is POLLEN's exact scoring action, and is there more than one way to score it?
6. What limits how many POLLEN a robot may control, and is that instantaneous or cumulative?
7. Does releasing and re-acquiring reset any count or timer?
8. What is the expansion limit (R105), when does it apply, and how is it measured?
9. Which fouls scale per-occurrence, and which are once-per-match?
10. Is there any rule whose penalty is cheaper than the scoring it prevents?
11. What exactly may a human player touch, when, and from where?
12. What is randomized, when is it revealed, and what happens if you guess before reveal?
13. Can a scoring element be removed from a scored state, by whom, and does the score revert?
14. What is the endgame time gate, and what is the latest safe commit?
15. Which scoring actions have no governing G-rule?
16. Does any R-rule permit a mechanism a G-rule implicitly forbids?
17. What are the ARENA fault provisions, and what triggers a replay?
18. Which protected zones exist, and can we enter one deliberately to draw a foul on an opponent? *(Ask, then read §5.)*
19. What does the manual say about scoring in the instant the buzzer sounds?
20. Which of these is a Q&A question rather than a reading question?

---

## 7. Output of this phase

A table appended to the R7 pitfall register, one row per finding:

`ID | rule id(s) | taxonomy type | what the text permits | confidence | our exposure | our opportunity | Q&A? | fallback if patched`

Anything marked `Q&A?` goes to the submission drafter. Anything with no fallback does not become a
design commitment.

---

*Method file. Evidence: `research/LOOPHOLE-CASEBOOK.md`. Procedure context: `reference/ANALYSIS-PROTOCOL.md`
phase R6. Ranking: `reference/STRATEGY-RANKING-PROTOCOL.md`. Written 2026-08-22, before kickoff — every
BIOBUZZ-specific example above is drawn from V0 final text or the FIRST game preview, never invented.*

*Produced with AI assistance; per BIOBUZZ A201 any of this reaching a team PORTFOLIO needs the footnote credit.*
