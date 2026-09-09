"""Tested reference parser for FTC Competition Manuals (BIOBUZZ V0 / DECODE / INTO THE DEEP)."""
import pymupdf, re, json, io
RULE_ID  = re.compile(r'^([IEAGRTLC])\d{3}$')
PAGENUM  = re.compile(r'^\d+ of \d+$')
SUPER_TM = {"TM", "®", "™", "SM"}
# Footer/header are identified by BLOCK bottom edge, not a fixed y: a two-line wrapped
# section title grows the footer UPWARD to ~734, so a fixed y-cut silently misses line 1.
HEAD_Y = 88
# Body-text point size is NOT a constant across releases. Rule ids and headlines are 11.0 pt in
# BIOBUZZ V0 / DECODE (both releases) / ITD V14, but 10.56 pt for every E-rule and R-rule in the
# 2024-25 ITD KICKOFF export -- Word shrink-to-fit inside the two-column rule table. An exact
# `== 11.0` test silently dropped all 39 E-rules and all 72 R-rules there. Use a tolerant band;
# bold + black + x0<40 + the id regex already carry the discrimination.
def BODY_PT(sz): return 9.5 <= sz <= 12.5
def hexs(i): return "#%06X" % (i & 0xFFFFFF)
def hexd(c): return "#%02X%02X%02X" % tuple(int(round(x*255)) for x in c[:3]) if c else None

# --- Font-name normalisation -------------------------------------------------
# CRITICAL, and the reason this function exists at all:
# FIRST ships the SAME manual through two different PDF export paths.
#   * Kickoff-day releases  -> comma style:  "Roboto", "Roboto,Bold", "Roboto,Italic"
#   * Later revisions (V14 / TU32 / BIOBUZZ V0) -> hyphen style:
#                              "Roboto-Regular", "Roboto-Bold", "Roboto-Italic"
# Measured across the corpus (2024-25 ITD kickoff, 2025-26 DECODE kickoff vs ITD V14,
# DECODE TU32, BIOBUZZ V0).  A parser hard-coded to the hyphen style returns ZERO rules
# on BOTH kickoff-day manuals -- and reports unpaired=0, so the failure looks like success.
# The BIOBUZZ manual arriving 2026-09-12 IS a kickoff-day release, so this normalisation
# is what makes the parser work on the one document it exists for.
# Also strips PDF subset prefixes ("ABCDEF+Roboto-Bold").
_FONT_ALIAS = {"roboto": "Roboto-Regular", "roboto,regular": "Roboto-Regular",
               "roboto,bold": "Roboto-Bold", "roboto,italic": "Roboto-Italic",
               "roboto,bolditalic": "Roboto-BoldItalic", "robotobold": "Roboto-Bold",
               "robotoitalic": "Roboto-Italic", "robotoregular": "Roboto-Regular"}
def font(name):
    n = (name or "").split("+", 1)[-1]
    return _FONT_ALIAS.get(n.lower(), n)

def parse(path):
    doc = pymupdf.open(path)
    out = {"pages": doc.page_count, "sections": {}, "rules": [], "orange_box_lines": 0, "violations": []}
    for pno, page in enumerate(doc, 1):
        bands = [g["rect"] for g in page.get_drawings() if hexd(g.get("fill")) == "#F4B083"]
        d = page.get_text("dict")
        ids, heads, footer = [], [], []
        # Identify the footer by CONTENT ("<n> of <N>"), never by a fixed y-threshold: a
        # two-line wrapped section title raises the footer to ~734 AND splits it into two
        # blocks, so anchor on the page-number block and sweep every block at or below it.
        anchor = min((b["bbox"][1] for b in d["blocks"] if b["type"] == 0
                      and any(PAGENUM.match(s["text"].strip())
                              for l in b["lines"] for s in l["spans"])), default=1e9)
        for b in d["blocks"]:
            if b["type"] != 0: continue
            if b["bbox"][1] >= anchor - 2:
                footer += [s for l in b["lines"] for s in l["spans"] if s["text"].strip()]
                continue
            for l in b["lines"]:
                sp = [s for s in l["spans"] if s["text"].strip()]
                if not sp: continue
                y0, x0 = l["bbox"][1], round(sp[0]["bbox"][0])
                if y0 < HEAD_Y: continue
                if any(r.y0 - 1 <= y0 <= r.y1 + 1 for r in bands):
                    out["orange_box_lines"] += 1; continue      # non-binding orange-box commentary
                keep = [s for s in sp if not (s["flags"] & 1 and s["text"].strip() in SUPER_TM)]
                if not keep: continue
                s0, txt, c = keep[0], "".join(s["text"] for s in keep), hexs(keep[0]["color"])
                # A rule id is ALWAYS: Roboto-Bold ~11pt BLACK, near the left margin, text == e.g. "G402".
                # Layout (a): id alone in its own table cell/block  (Section 3 I-rules only, in BIOBUZZ V0)
                # Layout (b): id is span[0] of the headline line    (Sections 5/6/11/12/13 -- 102 of 109)
                # x0 TOLERANCE: the id normally sits at x0=36.0, but when a rule table breaks across a
                # page the first id on the new page can be indented -- BIOBUZZ V0 `A202` is at x0=67.6.
                # An `x0 < 40` test silently DROPS it and still reports unpaired=0, so the miscount
                # looks like a clean run (V0 then reports 108 rules instead of the true 109).
                # Body text starts at x0=72, so <70 is still unambiguous.
                is_id = (font(s0["font"]) == "Roboto-Bold" and BODY_PT(s0["size"])
                         and c == "#000000" and x0 < 70 and RULE_ID.match(s0["text"].strip()))
                if is_id:
                    ids.append((y0, s0["text"].strip()))
                    # the Evergreen leading "*" is sometimes its OWN regular-black span,
                    # so skip a lone asterisk before looking for the coloured bold headline
                    rest = [s for s in keep[1:] if s["text"].strip() != "*"]
                    if rest and font(rest[0]["font"]) == "Roboto-Bold" and hexs(rest[0]["color"]) in ("#06844B","#ED7D31"):
                        heads.append((y0, hexs(rest[0]["color"]) == "#06844B",
                                      rest[0]["text"].strip().lstrip("*"),
                                      "".join(s["text"] for s in rest[1:]).strip()))
                elif font(s0["font"]) == "Roboto-Bold" and c in ("#06844B", "#ED7D31") and BODY_PT(s0["size"]):
                    heads.append((y0, c == "#06844B", s0["text"].strip().lstrip("*"),
                                  "".join(s["text"] for s in keep[1:]).strip()))
                elif font(s0["font"]) == "Roboto-Italic" and c == "#767171":
                    out["violations"].append((pno, txt.strip()[:110]))
        # footer = 3 fields keyed by x: label(~36) | version(~296-311) | "n of N"(~490-545)
        lab = " ".join(s["text"].strip() for s in footer if s["bbox"][0] < 250)
        ver = next((s["text"].strip() for s in footer if 250 < s["bbox"][0] < 400), None)
        if lab and ver: out["sections"][lab] = ver
        # pair each rule id with the headline on the SAME baseline (blocks are unordered)
        for y, rid in ids:
            m = min(heads, key=lambda h: abs(h[0] - y), default=None)
            if m and abs(m[0] - y) <= 3:
                out["rules"].append({"id": rid, "page": pno, "evergreen": m[1],
                                     "headline": m[2], "text": m[3][:150]})
            else:
                out["rules"].append({"id": rid, "page": pno, "evergreen": None, "headline": None, "text": ""})
    doc.close(); return out

if __name__ == "__main__":
    import sys, os

    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
    DEFAULTS = [
        ("manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf", "BIOBUZZ_V0"),
        ("manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_TU32.pdf", "DECODE_TU32"),
        ("manuals/_reference_prior_seasons/2024-25_INTO_THE_DEEP_Competition_Manual.pdf", "ITD_V14"),
    ]
    USAGE = """usage: ftc_parse.py [manual.pdf ...] [--tsv OUT.tsv] [--json OUT.json]

With no PDF argument, re-runs the three validated baselines (BIOBUZZ V0, DECODE TU32, ITD V14).
--tsv / --json write per-manual output; with several PDFs the name is suffixed with the manual name."""

    argv = sys.argv[1:]
    if "-h" in argv or "--help" in argv:
        print(USAGE); sys.exit(0)

    def take(flag):
        """Pull '--flag VALUE' out of argv, returning VALUE."""
        if flag not in argv:
            return None
        i = argv.index(flag)
        val = argv[i + 1] if i + 1 < len(argv) else None
        del argv[i:i + (2 if val else 1)]
        return val

    tsv_out, json_out = take("--tsv"), take("--json")
    pdfs = [a for a in argv if not a.startswith("-")]

    targets = ([(p, os.path.splitext(os.path.basename(p))[0]) for p in pdfs]
               or [(ROOT + p, n) for p, n in DEFAULTS])

    def suffixed(path, name):
        if path is None or len(targets) == 1:
            return path
        stem, ext = os.path.splitext(path)
        return f"{stem}_{name}{ext}"

    rc = 0
    for path, name in targets:
        if not os.path.exists(path):
            print(f"### {name}: MISSING -> {path}"); rc = 1; continue
        r = parse(path)
        rules = r["rules"]
        unpaired = [x["id"] for x in rules if x["headline"] is None]
        evergreen = sum(1 for x in rules if x["evergreen"])
        gamespec = [x["id"] for x in rules if x["evergreen"] is False]
        print(f"### {name}: {r['pages']}pp rules={len(rules)} evergreen={evergreen} "
              f"game-specific={len(gamespec)} unpaired={len(unpaired)} "
              f"orange-box lines={r['orange_box_lines']} penalty lines={len(r['violations'])}")
        print("   sections:", len(r["sections"]),
              json.dumps(r["sections"], ensure_ascii=False)[:230])
        print("   GAME-SPECIFIC (orange) ids -- read every one of these first:",
              " ".join(gamespec) or "(none)")
        if unpaired:
            rc = 1
            print("   !! unpaired ids:", unpaired[:12])
            print("   !! A non-zero unpaired count means FIRST changed the rule layout.")
            print("   !! Inspect the PDF before trusting anything downstream. See MANUAL-ANATOMY.md 0.6 / 13.10.")

        t, j = suffixed(tsv_out, name), suffixed(json_out, name)
        if t:
            with io.open(t, "w", encoding="utf-8", newline="\n") as fh:
                fh.write("id\tpage\tclass\theadline\n")
                for x in rules:
                    cls = ("EVERGREEN" if x["evergreen"]
                           else "GAMESPEC" if x["evergreen"] is False else "UNPAIRED")
                    fh.write(f"{x['id']}\t{x['page']}\t{cls}\t{x['headline'] or ''}\n")
            print("   wrote", t)
        if j:
            with io.open(j, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(r, fh, ensure_ascii=False, indent=1)
            print("   wrote", j)
    sys.exit(rc)
