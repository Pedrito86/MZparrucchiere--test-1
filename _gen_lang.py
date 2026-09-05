#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Crea 5 nuove pagine EN (4 saloni + dove-siamo) e fix IT lang-switch + goToSede EN."""
import os

APP = "/Users/pietro/Desktop/ultima versione sito web zucchini/app"

# ====== STANDARD REPLACE ======
TRANSL_SALON_COMMON = {
    # html lang
    '<html lang="it">': '<html lang="en">',
    # meta
    'Salone MZ Parrucchieri Villafontana di Medicina · Orari e Contatti': 'MZ Parrucchieri Salon Villafontana di Medicina · Opening Hours & Contact',
    'Salone MZ Parrucchieri Villanova di Castenaso · Orari e Contatti': 'MZ Parrucchieri Salon Villanova di Castenaso · Opening Hours & Contact',
    'Salone MZ Parrucchieri Imola · Orari e Contatti': 'MZ Parrucchieri Salon Imola · Opening Hours & Contact',
    'MZ Barber Shop Medicina · Taglio Uomo, Barba e Barber Tradizionale': 'MZ Barber Shop Medicina · Men\'s Haircut, Beard & Traditional Barbering',
    # description + keywords EN
    '<meta name="description" content="MZ Parrucchieri a Villafontana di Medicina (BO): taglio, colore, pieghe, styling, trattamenti Nashi Argan, meches, make up e acconciature sposa. Prenota per WhatsApp o telefono.">': '<meta name="description" content="MZ Parrucchieri salon in Villafontana di Medicina (Bologna): cutting, colouring, blow-dries, styling, Nashi Argan treatments, highlights, make up and bridal hairstyling. Book by WhatsApp or phone.">',
    '<meta name="keywords" content="parrucchiere Villafontana di Medicina, parrucchiere Medicina Bologna, taglio capelli, colore capelli, Villafontana di Medicina, Nashi Argan, meches, make up, acconciature sposa">': '<meta name="keywords" content="hairdresser Villafontana di Medicina, salon Medicina Bologna, haircut, hair colour, Villafontana di Medicina, Nashi Argan, highlights, make up, bridal hairstyling">',
    '<meta name="description" content="MZ Parrucchieri a Villanova di Castenaso (BO): taglio, colore, pieghe, trattamenti Nashi Argan, meches, make up e acconciature sposa. Prenota ora per telefono o WhatsApp.">': '<meta name="description" content="MZ Parrucchieri salon in Villanova di Castenaso (Bologna): cutting, colouring, blow-dries, Nashi Argan treatments, highlights, make up and bridal hairstyling. Book now by phone or WhatsApp.">',
    '<meta name="keywords" content="parrucchiere Villanova di Castenaso, Villanova Castenaso, taglio capelli, colore capelli, Nashi Argan, acconciature sposa, make up, MZ Parrucchieri">': '<meta name="keywords" content="hairdresser Villanova di Castenaso, Villanova Castenaso, haircut, hair colour, Nashi Argan, bridal hairstyling, make up, MZ Parrucchieri">',
    '<meta name="description" content="MZ Parrucchieri Imola (BO): taglio, colore, trattamenti, styling, Nashi Argan, pieghe, make up e acconciature sposa. Prenota per telefono o WhatsApp.">': '<meta name="description" content="MZ Parrucchieri salon in Imola (Bologna): cutting, colouring, treatments, styling, Nashi Argan, blow-dries, make up and bridal hairstyling. Book by phone or WhatsApp.">',
    '<meta name="keywords" content="parrucchiere Imola, MZ Parrucchieri Imola, taglio capelli Imola, colore capelli Imola, Nashi Argan Imola, acconciature sposa Imola, make up Imola, Piazza Gramsci Imola">': '<meta name="keywords" content="hairdresser Imola, MZ Parrucchieri Imola, haircut Imola, hair colour Imola, Nashi Argan Imola, bridal hairstyling Imola, make up Imola, Piazza Gramsci Imola">',
    '<meta name="description" content="MZ Barber Shop Medicina (BO). Taglio uomo, ragazzo, bimbo, rifiniture barba, Barba Spa e rasature tradizionali con asciugamani caldi. Prenota per WhatsApp o telefono.">': '<meta name="description" content="MZ Barber Shop Medicina (Bologna). Men\'s, teen and kids\' haircuts, beard trims, Beard Spa and traditional hot-towel shaves. Book by WhatsApp or phone.">',
    '<meta name="keywords" content="barber shop Medicina, barbiere Medicina, taglio uomo, barba Medicina, rasatura tradizionale, MZ Barber Shop, Zucchini Maurizio">': '<meta name="keywords" content="barber shop Medicina, barber Medicina, men\'s haircut, beard Medicina, traditional shave, MZ Barber Shop, Zucchini Maurizio">',
    # canonical EN
    'https://www.mzparrucchieri.it/salone-villafontana-medicina/">': 'https://www.mzparrucchieri.it/salone-villafontana-medicina/index-en.html">',
    'https://www.mzparrucchieri.it/salone-villanova-castenaso/">': 'https://www.mzparrucchieri.it/salone-villanova-castenaso/index-en.html">',
    'https://www.mzparrucchieri.it/salone-imola/">': 'https://www.mzparrucchieri.it/salone-imola/index-en.html">',
    'https://www.mzparrucchieri.it/barber-shop/">': 'https://www.mzparrucchieri.it/barber-shop/index-en.html">',
    '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-villafontana-medicina/">': '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-villafontana-medicina/"><link rel="alternate" hreflang="en" href="https://www.mzparrucchieri.it/salone-villafontana-medicina/index-en.html">',
    '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-villanova-castenaso/">': '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-villanova-castenaso/"><link rel="alternate" hreflang="en" href="https://www.mzparrucchieri.it/salone-villanova-castenaso/index-en.html">',
    '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-imola/">': '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-imola/"><link rel="alternate" hreflang="en" href="https://www.mzparrucchieri.it/salone-imola/index-en.html">',
    '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/barber-shop/">': '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/barber-shop/"><link rel="alternate" hreflang="en" href="https://www.mzparrucchieri.it/barber-shop/index-en.html">',
    'MZ Parrucchieri Villafontana di Medicina | Parrucchiere': 'MZ Parrucchieri Villafontana di Medicina | Hairdresser',
    'MZ Parrucchieri Villanova di Castenaso | Parrucchiere': 'MZ Parrucchieri Villanova di Castenaso | Hairdresser',
    'MZ Parrucchieri Imola | Parrucchiere': 'MZ Parrucchieri Imola | Hairdresser',
    # navbar EN
    '<li><a href="../index.html?skipintro=1#home">Home</a></li>': '<li><a href="../index-en.html?skipintro=1#home">Home</a></li>',
    '<li><a href="../index.html?skipintro=1#chi-siamo">Chi Siamo</a></li>': '<li><a href="../index-en.html?skipintro=1#about-us">About Us</a></li>',
    '<li><a href="../index.html?skipintro=1#servizi">Servizi</a></li>': '<li><a href="../index-en.html?skipintro=1#services">Services</a></li>',
    '<li><a href="../make-up/">Make Up</a></li>': '<li><a href="../index-en.html?skipintro=1#make-up">Make Up</a></li>',
    '<li><a href="../index.html?skipintro=1#galleria">Galleria</a></li>': '<li><a href="../index-en.html?skipintro=1#gallery">Gallery</a></li>',
    '<li><a href="../index.html?skipintro=1#contatti">Contatti</a></li>': '<li><a href="../index-en.html?skipintro=1#contact">Contact</a></li>',
    # lang switch IT->EN active
    '                <a href="../index.html?skipintro=1" class="lang-btn active">IT</a>\n                <a href="../index-en.html?skipintro=1" class="lang-btn">EN</a>': '                <button class="lang-btn" onclick="pageSetLang(\'it\')">IT</button>\n                <button class="lang-btn active" onclick="pageSetLang(\'en\')">EN</button>',
    # CTA WhatsApp "Prenota"
    '<i class="fab fa-whatsapp"></i>Prenota': '<i class="fab fa-whatsapp"></i>Book Now',
    # Menu
    'Menu': 'Menu',
    'Orari di oggi': 'Today\'s hours',
    'Chiuso': 'Closed',
    'Ora aperti': 'Open now',
    'Chiude alle': 'Closes at',
    'Riapre alle': 'Reopens at',
    'Contatti': 'Contact',
    'Indirizzo': 'Address',
    'Telefono': 'Phone',
    'Orari': 'Opening Hours',
    'Lunedì': 'Monday',
    'Martedì': 'Tuesday',
    'Mercoledì': 'Wednesday',
    'Giovedì': 'Thursday',
    'Venerdì': 'Friday',
    'Sabato': 'Saturday',
    'Domenica': 'Sunday',
    'chiuso': 'closed',
    # 'a': 'to',  — RIMOSSO: corrompeva "var" → "vtor", "location" → "loctotion", "catch" → "ctotch", "lang" → "ltong"
    'Passa a trovarci': 'Come & Visit Us',
    'Prenota ora': 'Book Now',
    'Chiamaci': 'Call Us',
    'Scrivici su WhatsApp': 'WhatsApp Us',
    'I servizi del salone': 'Our Services',
    'Cosa rende questo salone speciale': 'What Makes This Salon Special',
    'Nostro Team': 'Our Team',
    'Listino Servizi': 'Price List',
    'Taglio & Piega': 'Cut & Blow-dry',
    'Solo Taglio Donna': 'Ladies\' Cut Only',
    'Piega': 'Blow-dry',
    'Meches / Colpi di sole': 'Highlights / Balayage',
    'Colore': 'Colour',
    'Trattamento Nashi Argan': 'Nashi Argan Treatment',
    'Taglio Uomo': 'Men\'s Cut',
    'Acconciatura Sposa': 'Bridal Hairstyle',
    'Make Up Sposa': 'Bridal Make Up',
    'Taglio Ragazzo 13-17': 'Teens 13-17 Cut',
    'Taglio Bimbo 0-12': 'Kids 0-12 Cut',
    'Taglio Senior 65+': 'Senior 65+ Cut',
    'Rifinitura Barba': 'Beard Trim',
    'Barba Spa': 'Beard Spa',
    'Rasatura Tradizionale': 'Traditional Shave',
    'Rasatura + Barba': 'Shave + Beard',
    'Riconoscimenti e Premi': 'Awards & Recognition',
    'Il Fondatore': 'The Founder',
    'Il Salone': 'The Salon',
    'Panoramica 360°': '360° Overview',
    'Guarda il Virtual Tour': 'Take the Virtual Tour',
    'Taglio Donna': 'Ladies\' Cut',
    'Colore & Meches': 'Colour & Highlights',
    'Styling & Piega': 'Styling & Blow-dry',
    'Make Up': 'Make Up',
    'Trattamenti Capelli': 'Hair Treatments',
    'Acconciature Eventi': 'Event Hairstyling',
    'Taglio Uomo & Ragazzo': 'Men\'s & Boys\' Cut',
    'Barba & Rasature': 'Beard & Shaves',
    'Scopri tutti i servizi': 'Discover all services',
    'Torna alla Home': 'Back to Home',
    # Dove Siamo
    'Dove Siamo | MZ Parrucchieri - 4 Saloni tra Bologna e Imola': 'Find Us | MZ Parrucchieri - 4 Salons between Bologna and Imola',
    'Trova il salone MZ Parrucchieri più vicino: Villanova di Castenaso, Villafontana di Medicina, Imola e Barber Shop Medicina. Orari, telefoni, WhatsApp e mappe Google.': 'Find your nearest MZ Parrucchieri salon: Villanova di Castenaso, Villafontana di Medicina, Imola and Barber Shop Medicina. Opening hours, phones, WhatsApp and Google maps.',
    'MZ Parrucchieri, Dove Siamo | MZ Parrucchieri - 4 Saloni tra Bologna e Imola': 'MZ Parrucchieri, Find Us | MZ Parrucchieri - 4 Salons between Bologna and Imola',
    'Dove trovarci': 'Where to Find Us',
    'Quattro Sedi,': 'Four Locations,',
    'una sola': 'one',
    'eccellenza': 'excellence',
    'Villanova di Castenaso, Villafontana di Medicina, Imola e Barber Shop Medicina: quattro atelier MZ Parrucchieri tra Bologna e Imola, facilmente raggiungibili.': 'Villanova di Castenaso, Villafontana di Medicina, Imola and Barber Shop Medicina: four MZ Parrucchieri ateliers between Bologna and Imola, all easy to reach.',
    'Le nostre sedi': 'Our Locations',
    'Scopri il salone': 'Discover the Salon',
    'Raggiungici': 'Get Directions',
    'Recensisci': 'Leave a Review',
    'Cookie Policy': 'Cookie Policy',
    'Questo sito utilizza cookie tecnici per il corretto funzionamento. Proseguendo accetti la nostra Cookie Policy.': 'This website uses technical cookies for proper operation. By continuing you accept our Cookie Policy.',
    'Accetta': 'Accept',
    'Tutti i diritti riservati.': 'All rights reserved.',
    'P.IVA': 'VAT No.',
    'REA': 'Business Register',
    'Capitale Sociale': 'Share Capital',
    'Privacy Policy': 'Privacy Policy',
    'Termini di servizio': 'Terms of Service',
    # hero eyebrow salon individuale
    'Il Salone Villafontana': 'Villafontana Salon',
    'Il Salone Villanova': 'Villanova Salon',
    'Il Salone Imola': 'Imola Salon',
    'Barber Shop Medicina': 'Barber Shop Medicina',
    'MZ Parrucchieri': 'MZ Parrucchieri',
    'Medicina · Bologna': 'Medicina · Bologna',
    'Castenaso · Bologna': 'Castenaso · Bologna',
    'Imola · Bologna': 'Imola · Bologna',
    'Esperienza lusso, team, prodotti top e location esclusiva.': 'Luxury experience, team, premium products and exclusive location.',
    'Servizi e listino': 'Services & Price List',
    'Taglio, colore, styling, make up e trattamenti.': 'Cuts, colour, styling, make up and treatments.',
    'Servizi uomo, tagli classici e moderni, barba e rasature tradizionali.': 'Men\'s services, classic and modern cuts, beard and traditional shaves.',
    'Recensioni vere dei nostri clienti.': 'Genuine reviews from our customers.',
    'Dicono di noi': 'What They Say',
}

TRANSL_HERO_BY_FOLDER = {
    "salone-villafontana-medicina": {
        'Villafontana di Medicina · Dal 2004 nel cuore di Villafontana': 'Villafontana di Medicina · Since 2004 in the heart of Villafontana',
        'L\'eccellenza del parrucchiere': 'Hairdressing excellence',
        ' a Bologna': ' in Bologna',
    },
    "salone-villanova-castenaso": {
        'Villanova di Castenaso · Salone MZ dal 2019': 'Villanova di Castenaso · MZ Salon since 2019',
        'L\'eccellenza del parrucchiere': 'Hairdressing excellence',
        ' a Castenaso': ' in Castenaso',
    },
    "salone-imola": {
        'Imola · MZ Parrucchieri in Piazza Gramsci': 'Imola · MZ Parrucchieri on Piazza Gramsci',
        'L\'eccellenza del parrucchiere': 'Hairdressing excellence',
        ' a Imola': ' in Imola',
    },
    "barber-shop": {
        'Barber Shop Medicina · L\'arte tradizionale del barbiere': 'Barber Shop Medicina · The traditional art of barbering',
        'Rifiniture barba, rasature e taglio uomo.': 'Beard trims, shaves and men\'s haircuts.',
    },
}

# ========= 1) Copia IT -> index-en.html in ogni folder + replace =========
def create_salon_en(folder, title_prefix, og_desc):
    src_path = os.path.join(APP, folder, "index.html")
    dst_path = os.path.join(APP, folder, "index-en.html")
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()
    for it, en in TRANSL_SALON_COMMON.items():
        if it in html:
            html = html.replace(it, en)
    for it, en in TRANSL_HERO_BY_FOLDER.get(folder, {}).items():
        if it in html:
            html = html.replace(it, en)
    # OG
    html = html.replace(
        'property="og:description" content="MZ Parrucchieri: eccellenza nel taglio, colore, make up e acconciature sposa dal 2004. Quattro saloni a Villanova di Castenaso, Villafontana di Medicina, Imola e Barber Shop Medicina."',
        f'property="og:description" content="{og_desc}"'
    )
    # Aggiungi funzione pageSetLang in coda prima di </body>
    lang_js = f"""
<script>
function pageSetLang(l) {{
    try {{ localStorage.setItem('mz_lang', l); }} catch(e) {{}}
    if (l === 'it') window.location.href = 'index.html';
    else if (l === 'en') window.location.href = 'index-en.html';
    else window.location.href = 'index.html';
}}
</script>
"""
    html = html.replace("</body>", lang_js + "\n</body>")
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ {folder}/index-en.html")

# ===== DOVE SIAMO =====
def create_dovesiamo_en():
    src = os.path.join(APP, "dove-siamo", "index.html")
    dst = os.path.join(APP, "dove-siamo", "index-en.html")
    with open(src, 'r', encoding='utf-8') as f:
        html = f.read()
    for it, en in TRANSL_SALON_COMMON.items():
        if it in html:
            html = html.replace(it, en)
    # Navbar dove-siamo è leggermente diversa
    html = html.replace('<li><a href="../dove-siamo/" class="active">Dove siamo</a></li>',
                        '<li><a href="../dove-siamo/index-en.html" class="active">Find Us</a></li>')
    html = html.replace('<li><a href="../sposa/">Sposa</a></li>',
                        '<li><a href="../bridal/">Bridal</a></li>')
    html = html.replace('<li><a href="../chi-siamo/">Chi Siamo</a></li>',
                        '<li><a href="../index-en.html?skipintro=1#about-us">About Us</a></li>')
    html = html.replace('<li><a href="../index.html?skipintro=1#servizi">Servizi</a></li>',
                        '<li><a href="../index-en.html?skipintro=1#services">Services</a></li>')
    html = html.replace('<li><a href="../make-up/">Make Up</a></li>',
                        '<li><a href="../index-en.html?skipintro=1#make-up">Make Up</a></li>')
    html = html.replace('<li><a href="../prodotti/">Prodotti</a></li>',
                        '<li><a href="../index-en.html?skipintro=1#products">Products</a></li>')
    html = html.replace('<li><a href="../index.html?skipintro=1#galleria">Galleria</a></li>',
                        '<li><a href="../index-en.html?skipintro=1#gallery">Gallery</a></li>')
    html = html.replace('<li><a href="../index.html?skipintro=1#contatti">Contatti</a></li>',
                        '<li><a href="../index-en.html?skipintro=1#contact">Contact</a></li>')
    html = html.replace('<a class="nav-cta" style="text-decoration:none" href="../index.html?skipintro=1#contatti"><i class="far fa-calendar-check"></i>Prenota</a>',
                        '<a class="nav-cta" style="text-decoration:none" href="../index-en.html?skipintro=1#contact"><i class="far fa-calendar-check"></i>Book Now</a>')
    # hreflang canonical
    html = html.replace(
        '<link rel="canonical" href="https://www.mzparrucchieri.it/dove-siamo/">',
        '<link rel="canonical" href="https://www.mzparrucchieri.it/dove-siamo/index-en.html">'
    )
    html = html.replace(
        '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/dove-siamo/">',
        '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/dove-siamo/"><link rel="alternate" hreflang="en" href="https://www.mzparrucchieri.it/dove-siamo/index-en.html">'
    )
    # lang btn
    html = html.replace(
        '<button class="lang-btn active" onclick="pageSetLang(\'it\')">IT</button>\n                <button class="lang-btn " onclick="pageSetLang(\'en\')">EN</button>',
        '<button class="lang-btn" onclick="pageSetLang(\'it\')">IT</button>\n                <button class="lang-btn active" onclick="pageSetLang(\'en\')">EN</button>'
    )
    # pageSetLang per EN
    html = html.replace(
        '                "en": "../index-en.html?skipintro=1#about-us",\n                "it": "../dove-siamo/"',
        '                "en": "./index-en.html",\n                "it": "./index.html"'
    )
    html = html.replace('window.location.href = MAP[l] || (l===\'en\' ? \'../index-en.html?skipintro=1#home\' : \'../index.html?skipintro=1#home\');',
                        "window.location.href = MAP[l] || (l==='en' ? '../index-en.html?skipintro=1#home' : '../index.html?skipintro=1#home');")
    # OG desc EN
    html = html.replace(
        'property="og:description" content="Dove Siamo MZ Parrucchieri: 4 saloni tra Bologna e Imola. Indirizzi, orari, telefoni, WhatsApp e mappe per raggiungerci."',
        'property="og:description" content="Find MZ Parrucchieri: 4 salons between Bologna and Imola. Addresses, opening hours, phone numbers, WhatsApp and directions."'
    )
    html = html.replace(
        '<meta property="og:locale" content="it_IT">',
        '<meta property="og:locale" content="en_US">'
    )
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ dove-siamo/index-en.html")

# ========= ESECUZIONE CREAZIONE ==========
create_salon_en("salone-villafontana-medicina",
                "MZ Parrucchieri Salon Villafontana di Medicina",
                "MZ Parrucchieri salon Villafontana di Medicina: luxury cuts, colour, Nashi Argan, bridal. Book now.")
create_salon_en("salone-villanova-castenaso",
                "MZ Parrucchieri Salon Villanova di Castenaso",
                "MZ Parrucchieri salon Villanova di Castenaso: luxury cuts, colour, Nashi Argan, bridal. Book now.")
create_salon_en("salone-imola",
                "MZ Parrucchieri Salon Imola",
                "MZ Parrucchieri salon Imola: luxury cuts, colour, Nashi Argan, bridal. Book now.")
create_salon_en("barber-shop",
                "MZ Barber Shop Medicina",
                "MZ Barber Shop Medicina: traditional men's haircuts, beard trims and hot towel shaves.")
create_dovesiamo_en()

# ========= 2) FIX 4 SALONI IT: lang btn pageSetLang invece href a HOME EN =========
print("\n=== Fix IT pages ===")
PAGE_SET_LANG_JS_SALON = """
<script>
function pageSetLang(l) {
    try { localStorage.setItem('mz_lang', l); } catch(e) {}
    if (l === 'it') window.location.href = 'index.html';
    else if (l === 'en') window.location.href = 'index-en.html';
    else window.location.href = 'index.html';
}
</script>
"""
for folder in ["salone-villafontana-medicina", "salone-villanova-castenaso", "salone-imola", "barber-shop"]:
    path = os.path.join(APP, folder, "index.html")
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    old = '                <a href="../index.html?skipintro=1" class="lang-btn active">IT</a>\n                <a href="../index-en.html?skipintro=1" class="lang-btn">EN</a>'
    new = '                <button class="lang-btn active" onclick="pageSetLang(\'it\')">IT</button>\n                <button class="lang-btn" onclick="pageSetLang(\'en\')">EN</button>'
    if old in html:
        html = html.replace(old, new)
        # Aggiungi script pageSetLang
        html = html.replace("</body>", PAGE_SET_LANG_JS_SALON + "\n</body>")
        # Aggiungi alternate hreflang EN
        if folder == "salone-villafontana-medicina":
            html = html.replace(
                '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-villafontana-medicina/">',
                '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-villafontana-medicina/"><link rel="alternate" hreflang="en" href="https://www.mzparrucchieri.it/salone-villafontana-medicina/index-en.html">'
            )
        elif folder == "salone-villanova-castenaso":
            html = html.replace(
                '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-villanova-castenaso/">',
                '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-villanova-castenaso/"><link rel="alternate" hreflang="en" href="https://www.mzparrucchieri.it/salone-villanova-castenaso/index-en.html">'
            )
        elif folder == "salone-imola":
            html = html.replace(
                '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-imola/">',
                '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-imola/"><link rel="alternate" hreflang="en" href="https://www.mzparrucchieri.it/salone-imola/index-en.html">'
            )
        elif folder == "barber-shop":
            html = html.replace(
                '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/barber-shop/">',
                '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/barber-shop/"><link rel="alternate" hreflang="en" href="https://www.mzparrucchieri.it/barber-shop/index-en.html">'
            )
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {folder}/index.html (pageSetLang IT↔EN)")

# ========== 3) FIX dove-siamo IT pageSetLang('en') = ./index-en.html invece home about-us ==========
path = os.path.join(APP, "dove-siamo", "index.html")
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace(
    '"en": "../index-en.html?skipintro=1#about-us",\n                "it": "../dove-siamo/"',
    '"en": "./index-en.html",\n                "it": "./index.html"'
)
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("✅ dove-siamo/index.html pageSetLang fixed")

# ========== 4) FIX index-en.html goToSede -> VAI a PAGINA DEDICATA EN ==========
path = os.path.join(APP, "index-en.html")
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()
old = """function goToSede(sedeId) {
    navigateTo('about-us', { sedeId: sedeId });
}"""
new = """function goToSede(sedeId) {
    var URLS = {
        'sede-villanova':    './salone-villanova-castenaso/index-en.html',
        'sede-villafontana': './salone-villafontana-medicina/index-en.html',
        'sede-imola':        './salone-imola/index-en.html',
        'sede-barber':       './barber-shop/index-en.html'
    };
    if (URLS[sedeId]) {
        window.location.href = URLS[sedeId];
        return;
    }
    navigateTo('about-us', { sedeId: sedeId });
}"""
if old in html:
    html = html.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ index-en.html goToSede fixed")
else:
    print("❌ index-en.html: pattern goToSede non trovato")
