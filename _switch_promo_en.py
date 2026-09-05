#!/usr/bin/env python3
"""
Sostituisce fetch('content/promo.json'  -->  fetch('content/promo-en.json'
ESCLUSIVAMENTE nei file INGLESE (**index-en.html**).
Tutti i file IT (index.html, sposa, make-up, chi-siamo, prodotti, dove-siamo/index.html) RESTANO invariati.
"""
import os, glob

APP = "/Users/pietro/Desktop/ultima versione sito web zucchini/app"
OLD = "fetch('content/promo.json', { cache: 'no-store' })"
NEW = "fetch('content/promo-en.json', { cache: 'no-store' })"

en_files = []
for root, dirs, files in os.walk(APP):
    for fn in files:
        if fn.endswith("index-en.html"):
            en_files.append(os.path.join(root, fn))

print(f"Found {len(en_files)} index-en.html files:")
for p in en_files:
    with open(p, 'r', encoding='utf-8') as f:
        h = f.read()
    occ = h.count(OLD)
    if occ == 0:
        print(f"   SKIP (0 occorrenze) {os.path.relpath(p, APP)}")
        continue
    h2 = h.replace(OLD, NEW)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(h2)
    print(f"   OK {occ} sostituzioni → {os.path.relpath(p, APP)}")

# Verifica residui IT in EN
print("\n=== VERIFICA: occorrenze 'content/promo.json' SENZA '-en' in EN files ===")
for p in en_files:
    with open(p, encoding='utf-8') as f:
        h = f.read()
    residui = h.count("fetch('content/promo.json'")
    if residui:
        print(f"  ⚠️  {os.path.relpath(p, APP)} → promo.json IT ancora presente ×{residui}")
    else:
        en_ok = h.count("fetch('content/promo-en.json'")
        print(f"  ✅ {os.path.relpath(p, APP)} → promo-en.json ×{en_ok}")
