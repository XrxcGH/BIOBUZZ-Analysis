#!/usr/bin/env python3
"""parse-html-manual.py -- parse the HTML edition of an FTC Competition Manual.

WHY THIS EXISTS
    FIRST publishes the Competition Manual twice: as a PDF (`game/manual`) and as a
    Word-filtered HTML export (`game/cm-html`).  Every hard problem in the PDF pipeline
    -- pairing a rule id to its rule text, telling a binding rule from a non-binding
    orange box, telling an Evergreen rule from a season-specific one, reading the
    scoring table -- is solved *by name* in the HTML, because Word writes its paragraph
    style names straight into `class=` attributes:

        class=RuleNumber-Game        -> a G-rule paragraph (id + headline + body)
        class=Headline-Evergreen     -> green headline  (carries over between seasons)
        class=Headline-SeasonSpecific-> orange headline (new/changed this game)
        class=Violation              -> the enforcement clause
        class=OrangeBox*             -> NON-BINDING commentary
        <table><tr><td>              -> real table cells, no geometry guessing

    Measured on the two prior-season HTML manuals held in this corpus; see
    reference/HTML-MANUAL-PARSING.md for the full anatomy and the validation numbers.

WHAT THE HTML CANNOT GIVE YOU (still use the PDF for these)
    * per-section version stamps and page numbers -- Word drops headers/footers entirely
    * figures -- <img src> points at a sidecar `*_files/` folder that is NOT downloaded
      when you fetch the single .html, so ARENA diagrams must come from the PDF render

USAGE
    python tools/parse-html-manual.py <manual.html> [--out DIR] [--quiet]

OUTPUTS (in DIR, default: alongside the input as <stem>_html/)
    rules_html.tsv        id, letter, kind, headline, body, violation      (one row per rule)
    rules_full_html.md    every rule, full body, violation, orange boxes tagged NON-BINDING
    rules_GAMESPECIFIC_html.txt   orange-headline rules only  <- READ THESE FIRST
    rules_EVERGREEN_html.txt      green-headline rules
    violations_html.tsv   every enforcement clause, by rule id
    orangeboxes_html.md   all non-binding commentary, with the rule/section it sits under
    tables_html.md        every table as GitHub-flavoured Markdown  <- the scoring table
    outline_html.txt      h1/h2/h3 section tree
    caps_html.txt         ALL-CAPS token frequency (names the new game nouns)
    report_html.txt       counts + self-check
"""
from __future__ import annotations

import argparse
import collections
import os
import re
import sys
from html.parser import HTMLParser

# --- paragraph classes that introduce a rule ---------------------------------------
# Word style names observed in the 2024-25 and 2025-26 HTML manuals.  The trailing
# letter of the rule id is authoritative; these classes only tell us "a rule starts here".
RULE_CLASSES = {
    "RuleNumber-Inspection",
    "RuleNumber-Event",
    "RuleNumber-Game",
    "RuleNumber-Robot",
    "RuleNumber-Human",
    "RulesNumbering-awards",
    "TRules-Evergreen",
    "TRules-SeasonSpecific",
    "C-ChampsRules",
    "L-LeagueRules",
}
HEADLINE_EVERGREEN = "Headline-Evergreen"
HEADLINE_SEASON = "Headline-SeasonSpecific"
# Fallback signal: ~2% of rules set the headline colour inline instead of using the style
# (measured: 4/214 in DECODE TU32 -- G417, G418, G419, C501).  Same two hexes as the PDF.
GREEN, ORANGE = "#06844b", "#ed7d31"
COLOR_RE = re.compile(r"color:\s*(#[0-9A-Fa-f]{6})")
VIOLATION_CLASS = "Violation"
ORANGE_PREFIXES = ("OrangeBox", "BlueBox", "OB-")
# Continuation paragraphs that belong to the rule that opened above them.
CONT_PREFIXES = ("Rule-LetteredList", "Rule-SubsequentParagraph", "PlainBullets", "NormalText")

RULE_ID = re.compile(r"^([IEAGRTLC]\d{3})\b")
CAPS = re.compile(r"[A-Z]{3,}(?:'S)?")


def sniff_decode(raw: bytes) -> tuple[str, str]:
    """Return (text, charset).  Word writes the charset into a <meta> tag and it is NOT
    always windows-1252: the 2024-25 manual in this corpus declares `macintosh`."""
    head = raw[:2048].decode("ascii", errors="replace")
    m = re.search(r"charset=([\w\-]+)", head, re.I)
    charset = (m.group(1) if m else "windows-1252").lower()
    aliases = {"macintosh": "mac_roman", "mac": "mac_roman", "windows-1252": "cp1252"}
    codec = aliases.get(charset, charset)
    try:
        return raw.decode(codec, errors="replace"), charset
    except LookupError:
        return raw.decode("cp1252", errors="replace"), charset + " (unknown, fell back to cp1252)"


class Block:
    """One paragraph / heading / table cell, with the class that produced it."""

    __slots__ = ("cls", "tag", "text", "spans")

    def __init__(self, cls: str, tag: str) -> None:
        self.cls = cls
        self.tag = tag
        self.text: list[str] = []
        self.spans: list[tuple[str, str, str]] = []  # (class, inline-colour, text)

    def flat(self) -> str:
        return re.sub(r"\s+", " ", "".join(self.text)).strip()


class ManualParser(HTMLParser):
    """Streams the document into an ordered list of Blocks, plus a table model.

    Word's filtered HTML is tolerant-parser territory: unquoted attributes, unclosed
    <p>, spans nested three deep.  html.parser copes; we only need the class of the
    nearest enclosing block and of each inline span.
    """

    BLOCK_TAGS = {"p", "h1", "h2", "h3", "h4", "li", "td", "th", "div"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[Block] = []
        self.tables: list[list[list[str]]] = []
        self._stack: list[Block] = []
        self._span_cls: list[str] = []
        self._span_col: list[str] = []
        self._in_style = False
        self._tbl: list[list[str]] | None = None
        self._row: list[str] | None = None
        self._cell: list[str] | None = None
        self._table_depth = 0
        self._colspan = self._rowspan = 1
        self._carry: dict[int, tuple[str, int]] = {}

    def _fill_carry(self) -> None:
        """Insert cells inherited from a rowspan above, so columns stay aligned."""
        if self._row is None:
            return
        while len(self._row) in self._carry:
            self._row.append(self._carry[len(self._row)][0])

    # -- helpers
    def _cls(self, attrs) -> str:
        for k, v in attrs:
            if k == "class" and v:
                return v.split()[0]
        return ""

    def handle_starttag(self, tag, attrs):
        if tag == "style":
            self._in_style = True
            return
        if self._in_style:
            return
        if tag == "table":
            self._table_depth += 1
            if self._table_depth == 1:
                self._tbl = []
                self._carry = {}
            return
        if tag == "tr" and self._tbl is not None:
            self._row = []
            self._fill_carry()
            return
        if tag in ("td", "th") and self._tbl is not None:
            self._cell = []
            self._colspan, self._rowspan = 1, 1
            for k, v in attrs:
                if k in ("colspan", "rowspan"):
                    try:
                        n = max(1, int(v))
                    except ValueError:
                        n = 1
                    setattr(self, "_" + k, n)
            self._fill_carry()
        if tag == "br":
            if self._stack:
                self._stack[-1].text.append(" ")
            if self._cell is not None:
                self._cell.append(" ")
            return
        if tag == "span":
            self._span_cls.append(self._cls(attrs))
            col = ""
            for k, v in attrs:
                if k == "style" and v:
                    m = COLOR_RE.search(v)
                    if m:
                        col = m.group(1).lower()
            self._span_col.append(col)
            return
        if tag in self.BLOCK_TAGS:
            self._stack.append(Block(self._cls(attrs), tag))

    def handle_endtag(self, tag):
        if tag == "style":
            self._in_style = False
            return
        if self._in_style:
            return
        if tag == "table" and self._tbl is not None:
            self._table_depth -= 1
            if self._table_depth == 0:
                if self._tbl:
                    self.tables.append(self._tbl)
                self._tbl = None
            return
        if tag == "tr" and self._tbl is not None and self._row is not None:
            self._fill_carry()
            self._tbl.append(self._row)
            self._row = None
            for c in list(self._carry):
                txt, rem = self._carry[c]
                if rem <= 1:
                    del self._carry[c]
                else:
                    self._carry[c] = (txt, rem - 1)
            return
        if tag in ("td", "th") and self._cell is not None:
            cell = re.sub(r"\s+", " ", "".join(self._cell)).strip()
            if self._row is not None:
                col = len(self._row)
                self._row.append(cell)
                # A colspan cell must occupy its full width or every later column shifts
                # left -- which is exactly how a point value ends up under the wrong header.
                self._row.extend([""] * (getattr(self, "_colspan", 1) - 1))
                # A rowspan cell owns the same column in the rows below it; without this,
                # the next row starts one column too far left (measured on DECODE's
                # Table 10-2, where BASE spans two rows).
                if getattr(self, "_rowspan", 1) > 1:
                    for c in range(col, col + getattr(self, "_colspan", 1)):
                        self._carry[c] = (cell if c == col else "", self._rowspan - 1)
            self._cell = None
            self._colspan = self._rowspan = 1
        if tag == "span":
            if self._span_cls:
                self._span_cls.pop()
            if self._span_col:
                self._span_col.pop()
            return
        if tag in self.BLOCK_TAGS:
            # close the most recent block with this tag
            for i in range(len(self._stack) - 1, -1, -1):
                if self._stack[i].tag == tag:
                    blk = self._stack.pop(i)
                    if blk.flat():
                        self.blocks.append(blk)
                    break

    def handle_data(self, data):
        if self._in_style or not data.strip():
            if self._stack and data and not data.strip():
                self._stack[-1].text.append(" ")
            if self._cell is not None and data and not data.strip():
                self._cell.append(" ")
            return
        if self._stack:
            self._stack[-1].text.append(data)
            # innermost non-empty colour wins: Word nests <span class=X><span style=color:...>
            col = next((c for c in reversed(self._span_col) if c), "")
            self._stack[-1].spans.append((self._span_cls[-1] if self._span_cls else "", col, data))
        if self._cell is not None:
            self._cell.append(data)


class Rule:
    __slots__ = ("rid", "kind", "headline", "body", "violations", "boxes", "section")

    def __init__(self, rid, kind, headline, section):
        self.rid, self.kind, self.headline, self.section = rid, kind, headline, section
        self.body: list[str] = []
        self.violations: list[str] = []
        self.boxes: list[str] = []


def build(blocks: list[Block]):
    rules: list[Rule] = []
    outline: list[tuple[str, str]] = []
    loose_boxes: list[tuple[str, str]] = []  # (section, text) not attached to a rule
    section = ""
    cur: Rule | None = None
    for b in blocks:
        cls, txt = b.cls, b.flat()
        if not txt:
            continue
        if b.tag in ("h1", "h2", "h3"):
            outline.append((b.tag, txt))
            section = txt
            cur = None
            continue
        if cls in RULE_CLASSES or (RULE_ID.match(txt) and cls.startswith(("RuleNumber", "TRules", "C-", "L-", "RulesNumbering"))):
            m = RULE_ID.match(txt)
            if not m:
                continue
            rid = m.group(1)
            kind = "UNKNOWN"
            headline = ""
            for scls, scol, stext in b.spans:
                # An inline colour always overrides the class: Word reuses
                # class=Headline-Evergreen inside orange boxes with color:black.
                eff = scol or (GREEN if scls == HEADLINE_EVERGREEN
                               else ORANGE if scls == HEADLINE_SEASON else "")
                if eff == GREEN:
                    kind = "EVERGREEN"
                    headline += stext
                elif eff == ORANGE:
                    kind = "SEASON"
                    headline += stext
            rest = txt[m.end():].strip()
            if kind == "UNKNOWN":
                # Last resort, and it is FIRST's own convention rather than a guess:
                # §1.7.1 says an Evergreen headline carries a leading asterisk.  Two ITD
                # rules (I101, G414) set no headline colour at all but do carry the '*'.
                if rest.lstrip().startswith("*"):
                    kind = "EVERGREEN"
                if not headline:
                    headline = re.split(r"(?<=[.?!])\s", rest.lstrip("* "), 1)[0]
            headline = re.sub(r"\s+", " ", headline).strip().lstrip("*").strip()
            if headline and headline in rest:
                rest = rest.split(headline, 1)[1].strip()
            cur = Rule(rid, kind, headline, section)
            if rest:
                cur.body.append(rest)
            rules.append(cur)
            continue
        if cls == VIOLATION_CLASS:
            (cur.violations if cur else loose_boxes).append(txt) if cur else loose_boxes.append((section, "VIOLATION(orphan): " + txt))
            continue
        if cls.startswith(ORANGE_PREFIXES):
            if cur:
                cur.boxes.append(txt)
            else:
                loose_boxes.append((section, txt))
            continue
        if cur and cls.startswith(CONT_PREFIXES):
            cur.body.append(txt)
    return rules, outline, loose_boxes


def md_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    out = ["| " + " | ".join(c.replace("|", r"\|") for c in rows[0]) + " |",
           "|" + "---|" * width]
    for r in rows[1:]:
        out.append("| " + " | ".join(c.replace("|", r"\|") for c in r) + " |")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--out", default=None)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    raw = open(a.html, "rb").read()
    text, charset = sniff_decode(raw)
    out = a.out or os.path.join(os.path.dirname(os.path.abspath(a.html)),
                                os.path.splitext(os.path.basename(a.html))[0] + "_html")
    os.makedirs(out, exist_ok=True)

    p = ManualParser()
    p.feed(text)
    rules, outline, loose = build(p.blocks)

    # de-duplicate: a rule id repeated (Word sometimes splits a paragraph) keeps the first
    seen, dedup = set(), []
    for r in rules:
        if r.rid in seen:
            prev = next(x for x in dedup if x.rid == r.rid)
            prev.body.extend(r.body)
            prev.violations.extend(r.violations)
            prev.boxes.extend(r.boxes)
            continue
        seen.add(r.rid)
        dedup.append(r)
    rules = dedup

    w = lambda n: open(os.path.join(out, n), "w", encoding="utf-8")

    with w("rules_html.tsv") as f:
        f.write("id\tletter\tkind\theadline\tbody\tviolation\n")
        for r in rules:
            f.write("\t".join([r.rid, r.rid[0], r.kind, r.headline,
                               " ".join(r.body).replace("\t", " "),
                               " ".join(r.violations).replace("\t", " ")]) + "\n")

    with w("rules_full_html.md") as f:
        f.write("# Rules, full text (from the HTML manual)\n\n"
                "> Orange-box text is **NON-BINDING commentary**. If it conflicts with the rule, the rule wins.\n\n")
        for r in rules:
            f.write(f"## {r.rid} — {r.headline}   `[{r.kind}]`\n\n")
            if r.section:
                f.write(f"*section:* {r.section}\n\n")
            for b in r.body:
                f.write(b + "\n\n")
            for v in r.violations:
                f.write(f"**{v}**\n\n")
            for b in r.boxes:
                f.write(f"> *(NON-BINDING orange box)* {b}\n\n")

    with w("rules_GAMESPECIFIC_html.txt") as f:
        for r in rules:
            if r.kind == "SEASON":
                f.write(f"{r.rid}  {r.headline}\n")
    with w("rules_EVERGREEN_html.txt") as f:
        for r in rules:
            if r.kind == "EVERGREEN":
                f.write(f"{r.rid}  {r.headline}\n")
    with w("violations_html.tsv") as f:
        f.write("id\tviolation\n")
        for r in rules:
            for v in r.violations:
                f.write(f"{r.rid}\t{v}\n")
    with w("orangeboxes_html.md") as f:
        f.write("# Non-binding commentary (orange boxes)\n\n")
        for r in rules:
            for b in r.boxes:
                f.write(f"- **{r.rid}** — {b}\n")
        for sec, b in loose:
            f.write(f"- *({sec})* — {b}\n")
    with w("tables_html.md") as f:
        f.write("# Tables (real cells, straight from the HTML)\n\n")
        for i, t in enumerate(p.tables, 1):
            f.write(f"\n## table {i}  ({len(t)} rows)\n\n{md_table(t)}\n")
    with w("outline_html.txt") as f:
        for tag, t in outline:
            f.write("  " * (int(tag[1]) - 1) + t + "\n")

    plain = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text[text.lower().find("</style>"):]))
    caps = collections.Counter(CAPS.findall(plain))
    with w("caps_html.txt") as f:
        for term, n in caps.most_common():
            f.write(f"{n}\t{term}\n")

    by_letter = collections.Counter(r.rid[0] for r in rules)
    kinds = collections.Counter(r.kind for r in rules)
    report = [
        f"source          : {a.html}",
        f"declared charset: {charset}",
        f"blocks parsed   : {len(p.blocks)}",
        f"tables          : {len(p.tables)}",
        f"rules           : {len(rules)}   by letter: {dict(sorted(by_letter.items()))}",
        f"kinds           : {dict(kinds)}",
        f"violations      : {sum(len(r.violations) for r in rules)}",
        f"orange boxes    : {sum(len(r.boxes) for r in rules)} attached + {len(loose)} loose",
        f"outline         : {sum(1 for t, _ in outline if t == 'h1')} h1 / "
        f"{sum(1 for t, _ in outline if t == 'h2')} h2 / {sum(1 for t, _ in outline if t == 'h3')} h3",
        "",
        "SELF-CHECK (red = investigate before trusting anything downstream):",
        f"  [{'ok ' if kinds.get('UNKNOWN', 0) == 0 else 'RED'}] every rule got a headline kind "
        f"(UNKNOWN={kinds.get('UNKNOWN', 0)})",
        f"  [{'ok ' if sum(1 for t, _ in outline if t == 'h1') == 16 else 'RED'}] 16 top-level sections",
        f"  [{'ok ' if len(rules) > 150 else 'RED'}] rule count looks like a full manual, not a placeholder",
        "",
        "NOT AVAILABLE FROM HTML -- use the PDF: per-section version stamps, page numbers, figures.",
    ]
    with w("report_html.txt") as f:
        f.write("\n".join(report) + "\n")
    if not a.quiet:
        print("\n".join(report))
        print(f"\n-> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
