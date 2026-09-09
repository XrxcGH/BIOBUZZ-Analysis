#!/usr/bin/env python3
"""rule-bodies.py -- extract the FULL text of every rule, one record per rule id.

WHY THIS EXISTS
    `reference/ftc_parse.py` is the validated *inventory* parser: it answers "which rule ids
    exist, and is each one green (evergreen) or orange (new this game)". It deliberately keeps
    only the headline plus the first 150 characters of body text.

    A loophole hunt needs the opposite: the COMPLETE body of each rule, with its `Violation:`
    line, its lettered sub-clauses, and -- separately -- the non-binding orange-box commentary
    that sits next to it. `pdftotext` cannot give you that: rule ids live in their own table
    cell and detach from their bodies (MANUAL-ANATOMY.md 11.3), and orange-box commentary is
    typographically identical to rule text in flat text (MANUAL-ANATOMY.md 8).

    This walks the PDF in reading order by geometry, so every character between one rule id and
    the next belongs to that rule, and the orange-box lines are separated out rather than
    silently quoted as if they were binding.

USAGE
    python tools/rule-bodies.py <manual.pdf> [--out DIR] [--prefix G] [--min-words N]

    python tools/rule-bodies.py manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V1.pdf
    python tools/rule-bodies.py <manual.pdf> --prefix G      # just the game rules

OUTPUT  (in <out>, default <manual-dir>/rulebodies_<stem>/)
    rules_full.md      every rule: id, page, class, headline, body, sub-clauses, Violation:,
                       and its adjacent orange-box commentary, clearly separated
    rules_full.tsv     id / page / class / headline / n_words / n_clauses / violation / body
    ORANGE_BOXES.md    every orange box in the manual, with the rule it follows
    VIOLATIONS.tsv     id / penalty-sentence, for the penalty-ladder pass

CAVEAT
    Body text is captured between consecutive rule ids in geometric reading order. Text that
    belongs to a section *heading* between two rules is attached to the earlier rule. Check the
    tail of a body before quoting it. If `class=UNPAIRED` appears, FIRST changed the layout --
    stop and read the PDF (see MANUAL-ANATOMY.md 13).

    Line joins are not word-perfect: a handful of wrapped phrases lose their space
    ("eligible toparticipate"). Fine for reading and grepping; re-read the PDF page before
    quoting a rule verbatim to a referee or in a Q&A submission.

    Tables inside a rule body are flattened. For the scoring and motor tables use
    `tools/extract-tables.py`, which reads them by geometry.
"""
import argparse, io, os, re, sys

try:
    import pymupdf
except ImportError:
    sys.exit("pymupdf is required:  python -m pip install pymupdf")

RULE_ID = re.compile(r"^([IEAGRTLC])\d{3}$")
PAGENUM = re.compile(r"^\d+ of \d+$")
SUPER_TM = {"TM", "®", "™", "SM"}
HEAD_Y = 88
GREEN, ORANGE, GREY = "#06844B", "#ED7D31", "#767171"
BOX_FILL = "#F4B083"
_FONT_ALIAS = {"roboto": "Roboto-Regular", "roboto,regular": "Roboto-Regular",
               "roboto,bold": "Roboto-Bold", "roboto,italic": "Roboto-Italic",
               "roboto,bolditalic": "Roboto-BoldItalic", "robotobold": "Roboto-Bold",
               "robotoitalic": "Roboto-Italic", "robotoregular": "Roboto-Regular"}


def font(name):
    n = (name or "").split("+", 1)[-1]
    return _FONT_ALIAS.get(n.lower(), n)


def hexs(i):
    return "#%06X" % (i & 0xFFFFFF)


def hexd(c):
    return "#%02X%02X%02X" % tuple(int(round(x * 255)) for x in c[:3]) if c else None


def body_pt(sz):
    return 9.5 <= sz <= 12.5


def joinviol(parts):
    """Join the grey-italic penalty lines and drop FIRST's own 'Violation:' label so the
    output does not read 'Violation: Violation: MINOR FOUL.'"""
    s = " ".join(parts).strip()
    return re.sub(r"^Violation:\s*", "", s)


def clean(s):
    """Normalise the glyphs that break naive greps (MANUAL-ANATOMY.md 11.4, 11.9)."""
    return (s.replace("−", "-").replace("–", "-").replace("—", "--")
             .replace("‘", "'").replace("’", "'")
             .replace("“", '"').replace("”", '"')
             .replace("�", "-"))


def lines_in_reading_order(page):
    """Yield (y, x, text, first_span, in_orange_box) for every body line, top-to-bottom."""
    bands = [g["rect"] for g in page.get_drawings() if hexd(g.get("fill")) == BOX_FILL]
    d = page.get_text("dict")
    anchor = min((b["bbox"][1] for b in d["blocks"] if b["type"] == 0
                  and any(PAGENUM.match(s["text"].strip())
                          for l in b["lines"] for s in l["spans"])), default=1e9)
    out = []
    for b in d["blocks"]:
        if b["type"] != 0 or b["bbox"][1] >= anchor - 2:
            continue
        for l in b["lines"]:
            sp = [s for s in l["spans"] if s["text"].strip()]
            if not sp:
                continue
            y0, x0 = l["bbox"][1], round(sp[0]["bbox"][0])
            if y0 < HEAD_Y:
                continue
            boxed = any(r.y0 - 1 <= y0 <= r.y1 + 1 for r in bands)
            keep = [s for s in sp if not (s["flags"] & 1 and s["text"].strip() in SUPER_TM)]
            if not keep:
                continue
            out.append((y0, x0, clean("".join(s["text"] for s in keep)), keep, boxed))
    out.sort(key=lambda t: (round(t[0], 1), t[1]))
    return out


def parse(path):
    doc = pymupdf.open(path)
    records, boxes, cur, box_cur = [], [], None, None
    for pno, page in enumerate(doc, 1):
        for y0, x0, text, spans, boxed in lines_in_reading_order(page):
            s0 = spans[0]
            c = hexs(s0["color"])
            is_id = (font(s0["font"]) == "Roboto-Bold" and body_pt(s0["size"])
                     and c == "#000000" and x0 < 70
                     and RULE_ID.match(s0["text"].strip()) and not boxed)
            if boxed:
                if box_cur is None:
                    box_cur = {"after": cur["id"] if cur else "(before first rule)",
                               "page": pno, "lines": []}
                box_cur["lines"].append(text)
                continue
            if box_cur is not None:
                boxes.append(box_cur)
                if cur is not None:
                    cur["boxes"].append(" ".join(box_cur["lines"]))
                box_cur = None
            if is_id:
                rest = [s for s in spans[1:] if s["text"].strip() != "*"]
                klass, headline = "UNPAIRED", ""
                if rest and font(rest[0]["font"]) == "Roboto-Bold" and hexs(rest[0]["color"]) in (GREEN, ORANGE):
                    klass = "EVERGREEN" if hexs(rest[0]["color"]) == GREEN else "GAMESPEC"
                    headline = clean(rest[0]["text"].strip().lstrip("*"))
                    tail = clean("".join(s["text"] for s in rest[1:]).strip())
                else:
                    tail = clean("".join(s["text"] for s in spans[1:]).strip())
                cur = {"id": s0["text"].strip(), "page": pno, "class": klass,
                       "headline": headline, "body": [tail] if tail else [],
                       "violation": [], "boxes": []}
                records.append(cur)
                continue
            if cur is None:
                continue
            if font(s0["font"]) == "Roboto-Italic" and c == GREY:
                cur["violation"].append(text)
            elif font(s0["font"]) == "Roboto-Bold" and c in (GREEN, ORANGE) and body_pt(s0["size"]):
                # Layout (a): the rule id sits alone in its own table cell and the coloured
                # headline is the NEXT line (all Section 3 I-rules do this). If the current
                # record is still empty, this line is that rule's headline, not stray text.
                # Getting this wrong reports every I-rule as UNPAIRED, which reads as
                # "FIRST changed the layout" and would abort a kickoff-day run for no reason.
                if cur["class"] == "UNPAIRED" and not cur["headline"] and not cur["body"]:
                    cur["class"] = "EVERGREEN" if c == GREEN else "GAMESPEC"
                    cur["headline"] = clean(s0["text"].strip().lstrip("*"))
                    tail = clean("".join(s["text"] for s in spans[1:]).strip())
                    if tail:
                        cur["body"].append(tail)
                else:
                    # a coloured headline mid-rule: keep it, flagged, rather than lose it.
                    cur["body"].append("[headline] " + text)
            else:
                cur["body"].append(text)
    doc.close()
    if box_cur is not None:
        boxes.append(box_cur)
    return records, boxes


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--out", default=None)
    ap.add_argument("--prefix", default=None, help="only rules starting with this letter, e.g. G")
    ap.add_argument("--min-words", type=int, default=0, help="warn on rules shorter than this")
    a = ap.parse_args()

    if not os.path.exists(a.pdf):
        sys.exit("no such file: " + a.pdf)
    stem = os.path.splitext(os.path.basename(a.pdf))[0]
    outdir = a.out or os.path.join(os.path.dirname(os.path.abspath(a.pdf)), "rulebodies_" + stem)
    os.makedirs(outdir, exist_ok=True)

    records, boxes = parse(a.pdf)
    if a.prefix:
        records = [r for r in records if r["id"].startswith(a.prefix.upper())]

    n_unpaired = sum(1 for r in records if r["class"] == "UNPAIRED")
    print("== %s: %d rules (%d unpaired), %d orange boxes"
          % (stem, len(records), n_unpaired, len(boxes)))
    if n_unpaired:
        print("   !! %d rule ids had no coloured headline. FIRST may have changed the layout." % n_unpaired)
        print("   !! Verify against the PDF before trusting any body text. See MANUAL-ANATOMY.md 13.")

    md = os.path.join(outdir, "rules_full.md")
    with io.open(md, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# %s - full rule bodies\n\n" % stem)
        fh.write("Generated by `tools/rule-bodies.py`. Orange-box text is **non-binding "
                 "commentary** (BIOBUZZ V0 1.7.1) and is kept in its own block.\n\n")
        for r in records:
            body = " ".join(r["body"]).strip()
            fh.write("## %s  (p.%d, %s)\n\n" % (r["id"], r["page"], r["class"]))
            if r["headline"]:
                fh.write("**%s**\n\n" % r["headline"])
            if body:
                fh.write(body + "\n\n")
            if r["violation"]:
                fh.write("> **Violation:** " + joinviol(r["violation"]) + "\n\n")
            for b in r["boxes"]:
                fh.write("> _[orange box - non-binding]_ " + b.strip() + "\n\n")

    tsv = os.path.join(outdir, "rules_full.tsv")
    with io.open(tsv, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("id\tpage\tclass\theadline\tn_words\tn_clauses\tviolation\tbody\n")
        for r in records:
            body = " ".join(r["body"]).strip()
            nw = len(body.split())
            nc = len(re.findall(r"(?:^|\s)[a-hA-H][.)]\s", body))
            fh.write("%s\t%d\t%s\t%s\t%d\t%d\t%s\t%s\n"
                     % (r["id"], r["page"], r["class"], r["headline"], nw, nc,
                        joinviol(r["violation"]).replace("\t", " "),
                        body.replace("\t", " ")))

    vio = os.path.join(outdir, "VIOLATIONS.tsv")
    with io.open(vio, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("id\tpage\tviolation\n")
        for r in records:
            if r["violation"]:
                fh.write("%s\t%d\t%s\n" % (r["id"], r["page"],
                                           joinviol(r["violation"]).replace("\t", " ")))

    ob = os.path.join(outdir, "ORANGE_BOXES.md")
    with io.open(ob, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# %s - orange boxes (NON-BINDING commentary)\n\n" % stem)
        fh.write("If a rule and its orange box conflict, the rule wins (BIOBUZZ V0 1.7.1).\n\n")
        for b in boxes:
            fh.write("- **after %s** (p.%d): %s\n" % (b["after"], b["page"], " ".join(b["lines"]).strip()))

    if a.min_words:
        short = [r["id"] for r in records if len(" ".join(r["body"]).split()) < a.min_words]
        if short:
            print("   short rules (< %d words), check for extraction loss: %s"
                  % (a.min_words, " ".join(short[:20])))

    print("== wrote %s" % outdir)
    for f in (md, tsv, vio, ob):
        print("     %s  (%.1f KB)" % (os.path.basename(f), os.path.getsize(f) / 1024))


if __name__ == "__main__":
    main()
