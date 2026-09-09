# REVIEW PROMPTS — copy-paste pack for kickoff day

### One prompt per phase of `ANALYSIS-PROTOCOL.md` (R0–R8), plus utilities. Strategy ranking has its own pack: `REVIEW-PROMPTS-STRATEGY.md`.

Every prompt below is **self-contained** — it names the files to read, the output format, and the
honesty rules. Paste one at a time. Do not paste two phases at once; R3 is the critical path and
deserves a clean context.

---

## KICKOFF DAY RUNBOOK — Saturday 12 September 2026

| When | Do | Time |
|---|---|---|
| Manual drops | `bash tools/kickoff-fetch.sh` — pulls manual, per-section PDFs, Team Update 00, field docs | 5 min |
| Then | `bash tools/ingest-manual.sh <manual.pdf> V1` — text, rules, tables, rule bodies, figures, tripwires | 10 min |
| **Gate** | Check `rules_UNPAIRED.txt` is **empty** and page count is sane. Non-empty ⇒ layout changed ⇒ stop and read the PDF | 2 min |
| Team reads | Everyone reads Sections 8–10 on paper while the machine works. No laptops | 40 min |
| R1→R3 | Prompts P1, P3 below. **Build the scoring table before any opinion is formed** | 90 min |
| R2, R4, R5 | Prompts P2, P4, P5 — parallel if you have the people | 90 min |
| R6 | Prompt P6 with `LOOPHOLE-PLAYBOOK.md` | 2 h |
| R7, R8 | Prompts P7, P8 → the written brief | 60 min |
| Sunday | Strategy ranking: `REVIEW-PROMPTS-STRATEGY.md` D1–D8, ending in a team vote | half day |

**Three hours, not eight?** Run P1, P3, P6, P8. Never skip P3 — everything downstream is arithmetic on it.

**Path warning — the ingest label.** Every path below says `ingest_V1/`, which is correct only if you
ran `tools/ingest-manual.sh <manual.pdf> V1` by hand as the runbook says. If you instead ran
`tools/RUN-KICKOFF.sh` (what the `/kickoff` skill does), the label defaults to `KICKOFF`, the ingest
lands in `manuals/2026-27_BIOBUZZ/ingest_KICKOFF/`, and the same files are also copied flat into
`analysis/kickoff/bundle/`. Substitute the label you actually used before pasting any prompt.

**What to upload, in this order** (from `ANALYSIS-PROTOCOL.md` §10.1): `tables/TABLES.md` first, then
`rules_GAMESPECIFIC.txt`, then `rulebodies/G_rules_full.tsv`, then `figures/*.png`, then `full_layout.txt`
last. **Do not open by pasting the whole manual and asking "review this"** — it buries the scoring table
under 100k tokens of event logistics.

---

## The five standing instructions

Paste this block **once per session**, before the first phase prompt.

```
Standing rules for this whole session:

1. CITE. Every factual claim about the game gets a rule ID (e.g. G414) or a table
   reference (e.g. Table 10-2). No citation = you are guessing, and you must say so.
2. SEPARATE. Mark every statement [MANUAL] (the text says it), [DERIVED] (arithmetic
   from the text — show the operands), or [JUDGMENT] (your opinion). Never blur them.
3. NO PRIOR SEASONS. This is BIOBUZZ 2026-27. If you catch yourself using a fact from
   DECODE, INTO THE DEEP or any earlier season, label it [HISTORICAL] and say why it
   might not hold. A prior-season number stated as a BIOBUZZ number is the worst error
   you can make here.
4. SHOW ARITHMETIC. Any points-per-second, cycle-time or score estimate must show the
   operands and the assumption behind each one. A number with no working is rejected.
5. FLAG UNKNOWNS. If the manual does not say, write UNVERIFIED and add it to the Q&A
   list. Do not fill gaps with plausible inference.

Files I will refer to are in C:\Users\ericj\Documents\BIOBUZZ Analysis.
```

---

## P1 · R1 — Prove the ingest did not lie

```
Read manuals/2026-27_BIOBUZZ/ingest_V1/parse_new.log, rules_UNPAIRED.txt,
rules_ADDED.txt, rules_REMOVED.txt and section_versions.txt.

Report, as a short table:
 - page count, total rules, evergreen count, game-specific count, unpaired count
 - every rule ID added since V0, and every one removed
 - every section whose version stamp is no longer V0 (those sections changed even if
   they were "already final" pre-season)

Then answer explicitly: is there ANY sign the parser mis-read this manual? Specifically
— is rules_UNPAIRED.txt empty? Does the game-specific count look plausible (DECODE had
17 of 214)? Are there G-rules at all? If anything looks wrong, say STOP and tell me what
to check by hand. Do not proceed to analysis.
```

## P2 · R2 — Diff what was already final

```
Read section_versions.txt and DIFF_vs_V0.patch.

For every section whose version moved off V0, tell me what substantively changed versus
the pre-season manual — not typography. Focus on Sections 3 (I), 5 (E), 6 (A) and 12 (R),
which we treated as final and built plans on.

Output: a table of section | old V | new V | what changed | does it invalidate anything
in reference/CONSTRUCTION-RULES-R.md, reference/AWARD-CATALOG-BIOBUZZ.md or
reference/LEGAL-PARTS-CONSTRAINTS.md?

Flag loudly any change to: motor/servo counts (R503), expansion (R105), the motor and
servo allowlists (R501/R502), the vision-coprocessor allowlist (R702 and Table 12-9
"Supported programmable vision coprocessors"), or award criteria.
```

## P3 · R3 — The scoring model (critical path)

```
Use manuals/2026-27_BIOBUZZ/ingest_V1/tables/TABLES.md as the ONLY source for point
values. Do not read point values out of full_layout.txt — the flat text mis-pairs
labels and numbers (measured on DECODE p.88).

Build:
1. The complete scoring table: every scoring action, its value in AUTO, its value in
   TELEOP, and any bonus or ranking-point condition. Cite the table number.
2. The single most important question, answered explicitly with a quote: is AUTO scoring
   evaluated LIVE or AT THE END of the period, and are AUTO-scored elements RE-COUNTED
   in the final score? If the manual is not explicit, say UNVERIFIED and mark it as
   Q&A question #1.
3. A points-per-second estimate for each scoring action. Cycle = acquire + travel +
   align + score + return. State every time assumption in seconds and label it
   [JUDGMENT]. Show the division.
4. The AUTO / TELEOP / endgame point budget: how many points are theoretically
   available in each, and what fraction of a realistic match each represents.
5. The ranking-point conditions and the tiebreaker ladder.

Finish with: which scoring objective has the best points-per-second, and which one is
underpriced relative to its difficulty?
```

## P4 · R4 — ARENA and geometry

```
Work from manuals/2026-27_BIOBUZZ/ingest_V1/figures/*.png with the Section 9 text open.
Figures do not survive text extraction, so describe what you actually see in the images.

For every named zone or field element, tell me:
 - its dimensions and position, cited to a figure or table
 - whether its boundary is TAPE, PROJECTION, or VOLUME
 - what "in" means for a ROBOT: fully / partially / contacting
 - what "in" means for a SCORING ELEMENT
 - which alliance owns or is protected in it

Then: what are the travel distances between the acquisition point and each scoring
location, in tiles and inches? Those distances drive every cycle-time estimate in P3.
```

## P5 · R5 — G-rules and penalty exposure

```
Read ingest_V1/rulebodies/G_rules_full.tsv and rules_GAMESPECIFIC.txt.

1. Tabulate every G-rule: id | headline | what it forbids | Violation tier | is it
   game-specific (orange) or evergreen (green)?
2. Cross-check against reference/PENALTY-AND-ENFORCEMENT.md: which recurring G-rule
   archetypes appear this season (protected zones, pinning limit, control limit,
   expansion, interference, human-player limits), and what are BIOBUZZ's specific
   numeric thresholds for each?
3. Which fouls scale per-occurrence and which are once-per-match?
4. Which fouls escalate automatically on repetition?
5. Our penalty exposure: given the strategies we are considering, which three rules are
   we most likely to violate, and what would it cost?

Cite every rule ID. Where a rule's body has exceptions, quote the exception.
```

## P6 · R6 — The loophole hunt

```
Read reference/LOOPHOLE-PLAYBOOK.md and run its seven passes in order against this
manual. Your inputs are ingest_V1/: rules_GAMESPECIFIC.txt, rulebodies/G_rules_full.tsv,
rulebodies/ORANGE_BOXES.md, TRIPWIRES.txt, caps_NOVEL.txt and figures/*.png.

Use the T1–T15 taxonomy in research/LOOPHOLE-CASEBOOK.md §3 to classify each finding.

Output exactly the table format in LOOPHOLE-PLAYBOOK.md §7:
ID | rule id(s) | taxonomy type | what the text permits | confidence | our exposure |
our opportunity | Q&A? | fallback if patched

Rules for this pass:
 - An orange box is NOT binding. If a finding rests on an orange box, say so.
 - Apply the two-robot filter in §4 before calling anything an opportunity.
 - Apply §5 before recommending anything. If a finding fails the "would you explain it
   to the referee" test, report it as an EXPOSURE (something an opponent might try
   against us), not as a plan.
 - Assume anything you find WILL be patched by a Thursday Team Update. Every
   opportunity needs a fallback or it is not a design commitment.
```

## P7 · R7 — Pitfall register

```
Synthesize P1–P6 into a pitfall register: the things that could cost us the season if we
get them wrong. Categories: rules we will trip over, design traps (an archetype the game
appears to reward but punishes), inspection risks against Section 12, schedule risks
against research/SEASON-CALENDAR.md, and strategy risks (what beats us).

For each: what it is, how likely, what it costs, the early warning sign, and the
countermeasure. Rank by expected cost. Be blunt — this is the section that earns its
keep by being uncomfortable.
```

## P8 · R8 — The review brief

```
Write the one-page brief the team votes on Monday. Audience: high-school students who
have read the manual once and a mentor who has not.

Structure:
 - The game in five sentences
 - The scoring table, simplified, with points-per-second alongside
 - The three or four viable strategies, one line each
 - What we recommend and why, in plain language
 - The top three pitfalls
 - The Q&A questions we are filing on 28 September
 - What we need to decide this week, and what can wait

No jargon that the manual does not use. Every number traceable to P3. Mark anything
still UNVERIFIED clearly — an honest gap is better than a confident guess the team
builds on.
```

---

## Utility prompts

### U1 · Diff a Thursday Team Update
```
A new Team Update landed. Run: bash tools/ingest-manual.sh <new manual.pdf> TU<n>
Then compare ingest_TU<n>/ against the previous ingest:
 - which section version stamps moved?
 - which rule IDs were added or removed?
 - in DIFF, what text actually changed? Remember: additions are highlighted yellow and
   deletions are struck through in the PDF, and struck text still appears in extracted
   text — so verify anything that looks deleted against the rendered page.
Then the only question that matters: does this change invalidate our chosen strategy,
our robot design, or any finding in our loophole register? If yes, say so first.
```

### U2 · Draft a Game Q&A submission
```
Take finding <ID> from our loophole register and draft a Game Q&A question.

Format it as FIRST expects: cite the specific rule, quote the exact phrase that is
ambiguous, state the two readings neutrally, and give one concrete match scenario that
distinguishes them. Do NOT argue for the answer we want — a leading question invites a
narrow ruling. Keep it under 150 words.

Note: Q&A opens 28 Sep 2026 12:00 ET, Lead Coach 1 or 2 account only; moderators answer
from Mondays and close Thursdays 5:00 pm ET.
```

### U3 · Red-team our strategy
```
You are the best team in our region and we are your opponent. Read our chosen strategy
brief. Tell me exactly how you beat us: which rule you use, which of our assumptions you
break, what you build instead, and what our failure looks like on the field.

Then tell me the cheapest change we could make that removes your advantage. Be specific
and be harsh — a comfortable answer here is a wasted prompt.
```

### U4 · Sanity-check a scoring claim
```
Someone claimed: "<claim>".
Verify it against ingest_V1/tables/TABLES.md and the G-rule bodies. Quote the governing
text. If the claim is right, say so in one line. If it is wrong, show the correct number
and where the error came from. If the manual does not settle it, say UNVERIFIED and
draft it as a Q&A question.
```

### U5 · Scouting sheet generator
```
Read the scoring table from P3 and research/SCOUTING-AND-AWARDS.md.
Produce a one-page match scouting sheet for BIOBUZZ: the 6–8 observations that actually
predict alliance value this season, each recordable in under 3 seconds by one person
watching one robot. No field that requires judgement calls a stressed 15-year-old cannot
make consistently. Output as a printable table.
```

---

*Prompt pack for `reference/ANALYSIS-PROTOCOL.md` phases R0–R8. Strategy ranking: `REVIEW-PROMPTS-STRATEGY.md`.
BOM generation: `tools/bom/PROMPTS-bom.md`. Written 2026-08-22, pre-kickoff — paths assume the ingest label `V1`.*
