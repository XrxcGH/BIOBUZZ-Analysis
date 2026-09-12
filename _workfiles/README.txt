_workfiles/: local scratch for intermediate extracts. Only this README is published with the repository.
Nothing in reference/ or research/ depends on these paths; they are raw inputs, not deliverables.

The files listed below are excluded by .gitignore and exist only on a machine that made them. The three
*_text.txt files are plain text of FIRST's own publications (a Q&A archive and two Team Updates), each
generated locally with the pdftotext command below from a PDF downloaded from FIRST. The JSON file is a
raw Chief Delphi API response that carries forum members' post excerpts and usernames.

  2023-24_CENTERSTAGE_QA_text.txt      plain text of the CENTERSTAGE official Q&A archive
  2025-26_DECODE_TeamUpdate32_text.txt plain text of DECODE Team Update 32 (the final one)
  2024-25_ITD_TeamUpdate16_text.txt    plain text of INTO THE DEEP Team Update 16
  chiefdelphi_category_list.json       Chief Delphi forum category index (community source map)

Regenerate with:  pdftotext -enc UTF-8 -layout <source.pdf> <out.txt>
Sources are the PDFs in manuals/archive/supplemental/, which is local only; download them from FIRST.
