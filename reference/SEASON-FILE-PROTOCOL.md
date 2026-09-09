# SEASON FILE PROTOCOL: the last mile from the manual review to a file Trellis loads

### PHASE S (S1-S9): from `analysis/kickoff/` to a validated `2026-biobuzz.json`, in about an hour

**Written:** 2026-09-04, eight days before kickoff. **Status:** the skeleton exists and has been run
through Trellis's own validator. The path below has been walked with what V0 allows; the steps that
need the real manual have not, because it does not exist yet.

---

## 0. What this is

`ANALYSIS-PROTOCOL.md` takes you from FIRST publishing the manual to a written review. It stops
there. This file takes that review and turns it into one JSON file that the Trellis suite loads, so
the scouting form, the picklist, the simulator, Cycle Economics and the printed brief all describe
BIOBUZZ instead of describing nothing.

**PHASE S is transcription, not analysis.** Every number it asks for was already read, cited and
labeled in PHASE R. If you find yourself deciding something here, stop: the decision belongs in
`R3-scoring-model.md`, where it gets a citation and a label, and this file copies it.

| | |
|---|---|
| **Input** | `analysis/kickoff/D0-scoring-table.md` (R3), `R4-arena.md` (R4), the R3b ranking answers |
| **Worksheet** | `tools/trellis/2026-biobuzz.json`, already filled in as far as V0 allows |
| **Output** | `analysis/kickoff/2026-biobuzz.json`, complete, validated, then copied into an FTC Trellis checkout |
| **Budget** | ~60 min `[E]`, unvalidated. Run it after R4 and before PHASE D, or in parallel with D1 |
| **Who** | one person who has read R3. Not the person writing the brief |

### 0.1 The one thing to get right

The evidence convention in this workspace and the `_source` and `_note` convention in a Trellis
season file are the same discipline. **Every value you write carries a note saying where it came
from, and every value you cannot fill stays empty with a note saying which section fills it.** A
gap gets filled. A wrong number gets trusted, printed on a brief, and read out at an event.

Trellis's own documents use `[V]` and `[L]`, defined in `<trellis>/docs/00-INDEX.md`, but its
configuration files carry no labels at all. So keep this workspace's, inside the `_note` string:
`[C]`, `[H]`, `[J]`, `[M]` and `[U]`, plus the suffixed forms the skeleton declares in its own
`_evidence` field. The skeleton already does this throughout, so match what is there.

### 0.2 The firewall, and how Trellis changed under it

**This section was rewritten on 2026-09-04. The rule it described is no longer the rule.**

It used to say that an FTC season file must never share `config/season/` with an FRC one, because
`pickSeason` took the highest `year` and broke a tie by glob order, and BIOBUZZ and FRC REBUILT are
both year 2026. That was true and the loser was silent.

Trellis now scores the program before it looks at the year. `chooseSeason` in
`src/lib/config/bundled.ts` reads an optional `program` key on each season file: **claims the
program in force scores 2, claims nothing scores 1, claims a different program is ineligible.** A
file that names its program therefore wins on a matching install and is refused outright on any
other, whatever order the glob returns.

`[M]` Measured 2026-09-04 against the real `chooseSeason`, both glob orders, with the two real
files:

| `2026-biobuzz.json` | FTC install loads | FRC install loads |
|---|---|---|
| **with** `"program": "ftc"` | `2026-biobuzz` | `2026-rebuilt` |
| **without** it | `2026-rebuilt` | `2026-rebuilt` |

The bottom row is the old failure, and it is worse than a coin flip in practice: the FTC install
silently got the FRC game.

**So the rule is now one line in the file, not one checkout per program.** `tools/trellis/2026-biobuzz.json`
carries `"program": "ftc"` as of 2026-09-04, and `validate-season.sh` checks for it: it warns loudly
when the key is missing and confirms the clash is handled when it is there. A separate FTC checkout
still works and is no longer required.

**What has not changed.** Shipping this file while it is still a skeleton is worse now, not better:
with the program key it *wins* on an FTC install rather than losing a coin flip, so a stray copy in
`config/season/` gets loaded. See `_notLoadable` in the file itself.

Validating from this workspace, which is what S9 does, installs nothing and is safe against any
checkout.

---

## 1. Before you start (5 min)

- [ ] R3 is done and `analysis/kickoff/D0-scoring-table.md` exists with every row carrying value,
      period, per-what, cap and a quoted assessment sentence. **If R3 is not done, stop.** This
      protocol has no way to invent a scoring table and neither do you.
- [ ] R4 is done, or at least the field envelope from Section 9.2 is written down.
- [ ] `cp tools/trellis/2026-biobuzz.json analysis/kickoff/2026-biobuzz.json` and edit the copy.
      Editing in place loses the diff of what kickoff day actually changed, and the validation
      script in S9 looks in `analysis/kickoff/` first, so the copy is also what it checks.
- [ ] Open `<trellis>/config/season/README.md`. It is the authoring checklist for the file itself,
      written for FRC, and everything in it about keys, notes and stability is true here.
- [ ] Confirm the Trellis checkout you will validate against exists and its dependencies are
      installed. `npm run validate` in it should print a list of ok lines. **Do this now, not at
      step S9**, because `npm install` on a venue network is not a five-minute problem.

---

## 2. The steps

Each step names what to read, which field it fills, and when it is done.

### S1. Identity (2 min)

| Field | Source |
|---|---|
| `gameName` | The manual cover and Section 8. Write the game name as FIRST writes it |
| `id` | `2026-biobuzz`, matching the filename without the extension. Already set |
| `year` | `2026`. Already set. This is the FTCScout season number, which is the first of the two years in `2026-2027` |
| `program` | `ftc`. Already set, and do not remove it. It is what stops an FTC install from silently loading the FRC game when both season files are year 2026. §0.2 has the measurement |

**Done:** nothing in the file says BIOBUZZ where the manual says something else, and `program` still
reads `ftc`.

### S2. Match structure (5 min), Section 10.4

The seven-question list in `ANALYSIS-PROTOCOL.md` §3.3 opens with exactly this. Copy its answer.

| Field | Source |
|---|---|
| `phases.auto` | The AUTO length in seconds |
| `phases.teleop` | The TELEOP length in seconds. **A length, not a mark on the clock** |
| `phases.endgame` | Trellis's own window, counted back from the end of TELEOP. Set it only if Section 10 pays for something that is only scorable in the last N seconds. `[C]` V0 uses the word ENDGAME zero times, so 0 may well be the right answer |
| `phases.transition` | **Usually leave it out.** For FTC the transition arrives from the event profile in `config/program/ftc.json`, and `phaseMarks` takes the profile's number ahead of this file's. Set it here only if Section 10.4 gives a number the program file does not carry, and tell whoever maintains the program file |

**Done:** the three lengths are read off Section 10.4, not off DECODE. Get this wrong and every
timer, cycle estimate and break-even figure in the suite is wrong by the same amount.

### S3. Game pieces (2 min), Sections 8, 9 and the Section 16 glossary

| Field | Source |
|---|---|
| `gamePieces` | The manual's exact names for the SCORING ELEMENTS, capitalized as the manual capitalizes them. Scouts read these strings |

`[C]` Pollen is already in the file. Add a second element only if the manual names one. Update the
note if the manual confirms or contradicts the 2.8 in and 0.055 lb figures, which today come from a
vendor listing and not from FIRST.

**Done:** every element the manual names is listed, and nothing else is.

### S4. Scoring locations (15 min), Section 10 scoring table, via `bundle/TABLES.md`

The longest step and the one every screen downstream depends on. This is a straight transcription
of `D0-scoring-table.md`, one entry per row.

| `D0-scoring-table.md` column | Season file |
|---|---|
| Achievement | `label`, plus a `key` in `snake_case` you will never rename |
| AUTO value | `points.auto`. **Omit the key entirely when the action does not score in AUTO.** Not `0` |
| TELEOP value | `points.teleop`, same rule |
| Endgame value | `points.endgame`, only if S2 gave you an endgame window |
| Per what | a `_note`. The schema has nowhere to put it and it is the most commonly mis-read field |
| Cap | a `_note`. An alliance-level cap cannot be expressed in a per-robot value |
| Assessment | a `_note`, with the quoted sentence and its section number |
| Label | keep `[C]` and the table number inside the note |

Three rules that are not obvious and each of which has burned this file's FRC sibling:

- **An action paid for in AUTO and nowhere else gets an `auto` value and no other.** That shape is
  what tells the simulator it is a one-time action rather than somewhere to cycle to. Give it a
  teleop value it does not have and every simulated robot spends the match feeding it.
- **A structure with levels gets one entry per level.** Three levels is three entries, not one
  entry with a level field. That is what lets Picklist compare a level 3 robot to a level 1 robot
  with no code knowing what a level is.
- **Never read a point value out of `bundle/full_layout.txt`.** Flat text mis-pairs labels with
  numbers, measured on DECODE p.88. `bundle/TABLES.md` is the only correct source.

**Done:** every row of `D0-scoring-table.md` has an entry, every entry has a note carrying its
per-what and its cap, and no entry has a value that is not in the table.

### S5. Ranking (8 min), Section 13.6.3 and Table 13-1, and the RP table in Section 10

Two fields, and the first one is the one that is different from FRC.

**`rankingColumns`. FTC ranking columns arrive positionally, not by name.** There is no published
header to copy. FTCScout sends exactly three sort orders, `rp` then `tb1` then `tb2`, and the season
file claims a position with `sortOrder` rather than a name with `published`.

| Position | What it is | What to write |
|---|---|---|
| 1 | RANKING SCORE. The thing the table is sorted by | **Nothing.** Baseline reads position 1 as the ranking score directly |
| 2 | The first tiebreaker | **Nothing.** Baseline falls back to position 2 for Avg Match |
| 3 | The second tiebreaker | One entry with `sortOrder: 3`, a stable `key`, and a `label` naming what Table 13-1 says the second tiebreaker measures |

Read §5 of this file before you argue with the warning Trellis prints about positions 1 and 2.

`[U]` If Table 13-1 sorts on more than three keys, positions past 3 do not exist in this feed.
DECODE sorted on four plus random and FTCScout published three of them. Write the fourth in a note
and do not invent a position for it.

**`rankingPoints`.** One entry per RP condition, including win and tie. `description` is display
text a drive coach reads between matches, so write a sentence and not a formula. Where a threshold
differs by event tier, use `thresholdsByTier` keyed by the tier keys in `config/program/ftc.json`,
which today are `championship` and `regional_championship`. `[H]` DECODE published three values per
RP and said the Championship numbers would move in Team Updates, so expect to revisit this twice.

**Done:** position 3 is claimed or explicitly noted as absent, positions 1 and 2 are unclaimed, and
every RP threshold that varies by tier is written as a tier map rather than as one number.

### S6. Match fields (10 min), derived from S4 and from Section 11

The scouting form. Derive it from the scoring table. Do not invent it.

Start from the nine game-independent fields already in the skeleton and add:

- One counter per thing worth counting in AUTO and in TELEOP, with `points` equal to the matching
  `scoringLocations` value. Cycle Economics reads it and the Collect screen prints it beside the
  label, so a mismatch teaches every scout the wrong number.
- A `choice` for starting position, once Section 9 gives you the real zone names for its options.
- If Section 10 has an end-of-match structure: **three fields, not one.** Attempted, succeeded, and
  the level reached. The gap between attempted and succeeded is the number no published column
  carries and it is the one that separates a robot that never tries from one that tries and falls.
- Do not put `points` on a choice field whose value depends on which option was picked. The
  scoring locations carry those values.

**Collect only what free data cannot supply.** FTCScout already gives rank, ranking points, two
tiebreakers, record, DQ, matches played and OPR. A field that re-derives one of those spends a
student's attention to reproduce a number that is free and does it less accurately. This is why the
form is under 20 fields.

`[U]` before writing a defense field, check Section 11. Defense has been legal in every prior FTC
season `[H]`, and a contact restriction would make `defense_seconds` collect nothing.

**Done:** every counter's `points` equals its scoring location, every counter, timer and rating has
`min` and `max`, and `notes` is last in the form.

### S7. Pit fields (5 min), Section 12 and this season's nouns

Six fields are already in the skeleton and are correct as they stand. Add two:

| Field | Source |
|---|---|
| `scoring_locations` | A `choice` whose options are **this season's own nouns**, taken off the Section 10 scoring table. A pit form offering a word nobody at the event uses teaches a scout the wrong vocabulary in the week the team is naming its own subsystems |
| `climb_levels` or its equivalent | Only if Section 10 has an end-of-match structure with levels. Otherwise leave it out |

Do not add a weight question. `[C]` R104 says there is no weight limit for a BIOBUZZ robot, and
`config/program/ftc.json` carries `weightLimited: false` for exactly this reason.

Mark everything outside the express subset `"fullOnly": true`. The express four are drivetrain,
scoring locations, climb levels and known weaknesses. Keep `known_weaknesses` last: it is the
highest value question in the pits and it is answered honestly only after the photographs.

**Done:** every option string is a word the manual uses, and `known_weaknesses` is last.

### S8. Field (5 min), Section 9.2 and the field drawings

| Field | Source |
|---|---|
| `field.lengthM`, `field.widthM` | Section 9.2, in meters. The skeleton carries 3.658 square, which is `[H]` across 17 seasons and not a BIOBUZZ measurement |
| `field.zones`, `structures`, `lines` | The R4 worksheet in `FIELD-AND-ARENA.md` §8, once drawings are posted. Optional, and the schema keeps whatever measurement names you write |

**Do not delete the `field` block if you have no numbers.** `[M]` Measured against
`src/lib/sim/engine.ts` on 2026-09-04: with `field` absent the simulator falls back to 16.46 by
8.23 meters, which is the FRC carpet, and the 3 meter floors in the FTC program file cannot catch
it because 16.46 is above them. A missing field block does not produce a blank simulator, it
produces a confident FRC-sized one. Leave the `[H]` numbers and their note.

`[M]` Second trap in the same place: an FTC season file loaded **without** the FTC program file gets
the FRC floor of 4 meters, and a 3.658 meter field is silently clamped up to 4. If the simulator
prints 4 by 3.658, the program axis is not loaded.

**Done:** the two numbers are from Section 9.2 with a note saying so, or they are still the `[H]`
pair with the note that says they are.

### S9. Validate, then hand off (5 min)

```bash
bash tools/trellis/validate-season.sh
```

The script runs Trellis's own validator against the file. It takes the season file path and the
Trellis checkout path as optional arguments, so it also works on a copy or against a second
checkout. `TRELLIS_ROOT` in the environment overrides the default.

Then, and only then:

- [ ] Confirm the file still carries `"program": "ftc"`, then copy it into the Trellis checkout at
      `config/season/2026-biobuzz.json`. §0.2 has the measurement: with that key the FRC file at the
      same year is no longer a problem, and without it an FTC install silently loads the FRC game.
      `validate-season.sh` tells you which of the two you have.
- [ ] Run `npm run validate` there with no arguments, so the file is checked in the place it will
      actually load from and beside the program file it will load with.
- [ ] Open the app and the scouting form on a phone-sized window. Read every label and every help
      line as though you had never seen the game. **This catches more real problems than the
      validator does**, and it is the step people skip.
- [ ] Check no two keys collide across `matchFields`, `pitFields` and `scoringLocations`. A field
      key is also the name of the metric computed from it, so two fields sharing a key is two
      measurements landing in one number.
- [ ] Tell whoever maintains `config/team/*.json` which field keys are new. Their pick weights name
      those keys, and a weight naming a key you renamed silently stops counting.
- [ ] Commit. After this the file is the season's contract, and renaming a key costs more than
      living with a name you dislike.

---

## 3. What the validator does and does not check

It checks the shape. It does not check your reading of the manual. Both halves matter on a day when
somebody is writing JSON under time pressure.

**It catches** a missing required field; a `key` that is not lower case letters, digits and
underscores; a negative phase length; a ranking column that gives neither a published header nor a
position; a `year` that is not a competition year; a threshold that is not a number; malformed JSON,
which on kickoff day is usually a trailing comma.

**It cannot catch** a point value copied off the wrong row; a phase length copied from DECODE; a
counter whose `points` disagrees with its scoring location; an option string using last season's
noun; a ranking column claiming the wrong position; an endgame window invented for a game that has
none; or the file being loaded beside an FRC season file of the same year.

Everything in the second list is caught by a person reading the form on a phone, which is why S9
has that step in it and why it is written as a checkbox rather than as advice.

---

## 4. Timebox

| Step | What | Clock |
|---|---|---:|
| S0 | Prerequisites, checkout ready | 5 min |
| S1 | Identity | 2 min |
| S2 | Match structure, Section 10.4 | 5 min |
| S3 | Game pieces | 2 min |
| S4 | **Scoring locations, from `D0-scoring-table.md`** | 15 min |
| S5 | Ranking columns and ranking points | 8 min |
| S6 | Match fields | 10 min |
| S7 | Pit fields | 5 min |
| S8 | Field | 5 min |
| S9 | Validate and hand off | 5 min |
| | | **≈ 60 min** `[E]` |

`[E]` Unvalidated, like every other timebox in this workspace. S4 is the one that will overrun,
because it is the step whose length is set by how many rows the scoring table has.

**If you have 20 minutes, not an hour:** S2, S4 and S9. A file with the right clock and the right
scoring table and nothing else is usable. A file with a perfect pit form and a guessed clock is not.

---

## 5. Two Trellis defects to expect, both measured

Neither is a reason to change the file. Both are reasons not to be talked out of it.

### 5.1 The ordinal column resolver will tell you to do the wrong thing

`[M]` Measured against `src/lib/baseline/columns.ts` on 2026-09-04 with the skeleton's own columns.

A correctly authored FTC file claims position 3 and leaves 1 and 2 alone. Loading an event then
prints:

```
The rankings carried columns no season column claims: Sort Order 1, Sort Order 2.
Give a column that position in season.json to use it.
```

**Do not do what it says.** Claiming positions 1 and 2 silences the warning and makes the file
worse: the ranking score and the average match score then render twice, once as the table's own
columns and once as season columns of your own.

The cause is an asymmetry between the two resolvers. The named resolver used for FRC has a
`STRUCTURAL_HEADERS` set that recognizes `Ranking Score` and `Avg Match` as belonging to the table
rather than to the season. `discoverColumnsByOrdinal` has no equivalent, so positions 1 and 2 come
back as unclaimed rather than as structural. The second visible effect is cosmetic and confusing:
the FTC rankings table prints `Sort Order 1` and `Sort Order 2` as headers where the FRC table
prints `Ranking Score` and `Avg Match`.

Reported to the Trellis maintainer. Until it is fixed, the warning is noise and the header row is
wrong; the numbers under it are right.

### 5.2 The app still reads FTC event keys against The Blue Alliance

`[M]` Read out of `src/lib/baseline/baseline.ts` and `src/ui/screens/useEventData.ts` on 2026-09-04.
`createFtcScoutBaselineSource` is complete and covered by `tests/ftcscout.test.ts`, and nothing
outside those tests constructs it. `useEventData` calls `buildBaseline(eventKey, config, {
eventProfile })` with no `source`, and `resolveSource` defaults to the TBA source when none is
passed. **So an FTC install queries The Blue Alliance with an FTC event key**, and The Blue Alliance
covers FRC only.

That does not change anything in this protocol, and it is not a reason to delay writing the file.
It changes what to promise the team. A validated FTC season file makes the scouting form, the
simulator, Cycle Economics and the printed brief describe BIOBUZZ, all of which read the season file
and no network. Live rankings, the match schedule and the picklist's strength figure will not work
until the Trellis side selects the source from the program axis, which is `docs/08-FTC.md` §6.1
items 4 and 5 and is a Trellis change rather than a season file change.

Related, and worth knowing before somebody asks: FTCScout also publishes per-season statistics
addressed by name, such as an average AUTO points figure, and the season file has nowhere to declare
them. They are a constructor option today. If the team wants one of those as a column, it is a
Trellis change and not a season file change.

---

## 6. After kickoff day

- Re-read S4 and S5 after every Team Update. Those two sections carry almost all of the churn, and
  Team Updates land every Thursday from kickoff until two weeks before Championship.
- Re-check S5 against a real rankings page the first time the team plays an event, the same way the
  FRC checklist says to re-check column headers in week 1. Position matching survives a rename and
  does not survive a column being inserted ahead of it.
- **Never rename a key mid-season.** Add a new field and leave the old one in place. Stored records
  refer to the old key and renaming makes them unreadable.
- If a Team Update changes a point value, change it in `scoringLocations` **and** in the matching
  `matchFields` entry's `points`. They are two copies of one number and only a person keeps them
  equal.

---

## 7. Known gaps in this protocol

| Gap | Consequence |
|---|---|
| PHASE S has never been run against a real manual, only against the V0 skeleton | The 60 minute budget is `[E]` and S4 is the step most likely to overrun |
| The scoring table to season file mapping in S4 is a table in this document, not a script | A transcription error is possible and the validator cannot see it. A second person reading S4 against `D0-scoring-table.md` is the only check |
| No FTC ops file exists | `config/ops/*.json` still carries FRC defaults, including a scout rotation sized for a 6-robot match. `docs/08-FTC.md` §6.2 item 11 calls out FTC ops defaults derived from a 5-or-6-match event as unwritten work |
| The event profile is never assigned to an event | `config/program/ftc.json` authors two event tiers and says plainly that nothing writes an assignment yet, so Championship values are unreachable today |
| Nothing here covers League Tournament ranking | An FTC league team's ranking spans four to six event codes plus a league code, and no season file closes that. `[C]` Section 14 is **final text in V0**, verbatim from DECODE, so this rule is readable today rather than at kickoff. Note that `<trellis>/docs/08-FTC.md` §2.1 lists Section 14 among the V0 placeholders and is wrong about that; `research/BIOBUZZ-V0-STRUCTURE.md` §2 has the section-by-section status and counts six placeholders, 8, 9, 10, 11, 13 and 15. The consequence is in the team's favor: the League Tournament ranking rule is `[C]` rather than `[H]` |

---

*Method: `ANALYSIS-PROTOCOL.md` R0-R8 produces the inputs. `<trellis>/config/season/README.md` is
the authoring checklist for the file itself. `<trellis>/docs/08-FTC.md` §2 is why FTC differs.
`<trellis>/config/program/ftc.json` is the program axis this file sits beside.*
