#!/usr/bin/env python3
import re, pathlib
files = list(pathlib.Path("/Users/pietro/Desktop/ultima versione sito web zucchini/app").glob("**/index-en.html"))
for fp in files:
    h = fp.read_text(encoding="utf-8")
    n = h.count("function pageSetLang(l)")
    it_active = 'class="lang-btn active" onclick="pageSetLang(\'it\')"' in h
    en_active = 'class="lang-btn active" onclick="pageSetLang(\'en\')"' in h
    m = re.search(r"function pageSetLang\(l\)\s*\{(.*?)\n\}", h, flags=re.S)
    src = m.group(1) if m else "NONE"
    has_swap = ("window.location.href = 'index.html'" in src) and ("window.location.href = 'index-en.html'" in src)
    print(f"\nFILE: {fp.parent.name}/{fp.name}")
    print(f"  count function pageSetLang(l) = {n}")
    print(f"  lang-btn active → EN? {en_active}  IT? {it_active}")
    print(f"  body pageSetLang(): {src.strip().replace(chr(10),' | ')[:200]}")
    print(f"  contains swap index.html↔index-en.html? {has_swap}")
    # Controlla i link href pulsanti IT/EN nel bottone pagina stessa (NON la home!)
    print("--- HREFs pulsanti IT/EN pagina stessa: ---")
    for mm in re.finditer(r"<button class=\"lang-btn[^\"]*\" onclick=\"pageSetLang\('(it|en)'\)\">(IT|EN)</button>", h):
        print(f"   {mm.group(0)}")
