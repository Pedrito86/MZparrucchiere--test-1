#!/usr/bin/env python3
"""
Crea automaticamente /app/content/promo-en.json partendo da promo.json
e un dizionario di traduzioni per i campi testo delle promozioni attuali.
Lascia struttura JSON invariata (chiavi italiane): solo i VALORI testuali sono inglesi.
"""
import json, os, pathlib, re

PROMO_JSON = "/Users/pietro/Desktop/ultima versione sito web zucchini/app/content/promo.json"
PROMO_EN   = "/Users/pietro/Desktop/ultima versione sito web zucchini/app/content/promo-en.json"

# =============================
# TRADUZIONI ISTANZE ATTUALI
# =============================
CURRENT_TRAD = {
    # meseAnno
    "Settembre 2026": {
        "meseAnno": "September 2026",
    },
    # SALONI promo
    "Vitamin Glow": {
        "titolo":      "Vitamin Glow",
        "sottotitolo": "Illuminating & Purifying Treatment",
        "descrizione": (
            "Beautiful hair is not just about length. A single treatment delivers two results: "
            "it purifies and rebalances, giving natural lightness and volume; it smooths and "
            "compacts the hair fibre, seals and illuminates, creating an instant mirror effect. "
            "Discover your glow, ask for it in salon."
        ),
        "pulsanteTesto": "Book on WhatsApp",
        "waMessaggio": (
            "Hello, I would like information about the Vitamin Glow September promotion. "
            "May I have more details or book an appointment?"
        ),
    },
    "Trattamento Illuminante e Purificante": {},
    # BARBER promo
    "Luxury Shave": {
        "titolo":      "Luxury Shave",
        "sottotitolo": "Complete 30-minute beard ritual",
        "descrizione": (
            "Take advantage of our exclusive Luxury Shave service: 30 minutes of pure relaxation "
            "for your beard. Hot towel, premium oils, traditional lather and final massage with "
            "Level3 products."
        ),
        "pulsanteTesto": "Book on WhatsApp",
        "waMessaggio": (
            "Hello, I would like to book the Luxury Shave treatment at the Barber Shop. "
            "Do you have availability this week?"
        ),
    },
    "Rituale barba completo 30 minuti": {},
    # orari sede etichette
    "Lun 10-18 · Mar-Ven 9-19:30 · Mer 21:00 · Sab 8-18":
        "Mon 10-18 · Tue-Fri 9:00-19:30 · Wed 21:00 · Sat 8:00-18:00",
    "Mar-Ven 8:30-19:30 · Mer 20:30 · Sab 8-18":
        "Tue-Fri 8:30-19:30 · Wed 20:30 · Sat 8:00-18:00",
    "Mar-Sab 9:00-18:30 · Mer 20:30":
        "Tue-Sat 9:00-18:30 · Wed 20:30",
    # etichette numeri sede
    "Villanova di Castenaso": "Villanova di Castenaso",
    "Villafontana di Medicina": "Villafontana di Medicina",
    "Imola": "Imola",
    "Barber Shop Medicina": "Barber Shop Medicina",
    "Villanova": "Villanova",
    "Villafontana": "Villafontana",
    "Barber Shop": "Barber Shop",
}


def t(value, ctx=None):
    """Cerca traduzione diretta, altrimenti ritorna value invariato (per numeri, null, strutture)."""
    if value is None or isinstance(value, (int, float, bool)):
        return value
    if isinstance(value, list):
        return [t(x, ctx) for x in value]
    if isinstance(value, dict):
        out = {}
        for k, v in value.items():
            # cerco prima: la combo (titolo corrente) -> { chiave: trad }
            ctx_title = None
            if isinstance(v, str) and ctx and 'titolo' in ctx and ctx['titolo'] in CURRENT_TRAD:
                lookup = CURRENT_TRAD[ctx['titolo']]
                if isinstance(lookup, dict) and k in lookup:
                    out[k] = lookup[k]
                    continue
            # poi: traduzione diretta value -> CURRENT_TRAD[value] = str
            if isinstance(v, str) and v in CURRENT_TRAD and isinstance(CURRENT_TRAD[v], str):
                out[k] = CURRENT_TRAD[v]
                continue
            out[k] = t(v, {**ctx, **({k: v} if isinstance(v, str) else {})})
        return out
    if isinstance(value, str):
        # cerca trad diretta
        if value in CURRENT_TRAD and isinstance(CURRENT_TRAD[value], str):
            return CURRENT_TRAD[value]
        return value
    return value


with open(PROMO_JSON, 'r', encoding='utf-8') as f:
    data = json.load(f)

ctx = {}
if 'meseAnno' in data and data['meseAnno'] in CURRENT_TRAD:
    md = CURRENT_TRAD[data['meseAnno']]
    if isinstance(md, dict) and 'meseAnno' in md:
        data['meseAnno'] = md['meseAnno']

data['promozioni'] = [t(p, {'titolo': p.get('titolo','')}) for p in data.get('promozioni', [])]

with open(PROMO_EN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ {PROMO_EN} written.")
print("=== PREVIEW ===")
with open(PROMO_EN, encoding='utf-8') as f:
    s = f.read()
    # sformatta poche righe salienti
    for line in s.splitlines()[:45]:
        print('  ' + line)
