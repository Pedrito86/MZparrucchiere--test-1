#!/usr/bin/env python3
"""Generatore pagine landing ADS per MZ Parrucchieri.
Legge index.html / index-en.html come template CSS + JS, produce 6 directory
con index.html autonomo, senza modificare minimamente i file originali."""

import os, re, json, html, shutil

ROOT = "/Users/pietro/Desktop/ultima versione sito web zucchini/app"
INDEX_IT = os.path.join(ROOT, "index.html")
INDEX_EN = os.path.join(ROOT, "index-en.html")

with open(INDEX_IT, "r", encoding="utf-8") as f: src_it = f.read()
with open(INDEX_EN, "r", encoding="utf-8") as f: src_en = f.read()

def between(src, start, end):
    a = src.find(start); assert a!=-1, f"start marker not found: {start[:80]}"
    b = src.find(end, a+len(start)); assert b!=-1, f"end marker not found: {end[:80]}"
    return src[a+len(start):b], a, b

def get_page_content(src, page_id):
    """Return innerHTML of <div id="page-{page_id}" class="page">..."""
    marker_open = f'<div id="page-{page_id}" class="page'
    a = src.find(marker_open); assert a!=-1, f"page not found: {page_id}"
    # Cerca chiusura <div>
    open_i = src.find(">", a) + 1
    depth = 1; i = open_i
    while i < len(src) and depth > 0:
        if src.startswith("<div", i) or src.startswith("<DIV", i):
            depth += 1
            i += 4
        elif src.startswith("</div>", i) or src.startswith("</DIV>", i):
            depth -= 1
            if depth == 0:
                break
            i += 6
        else:
            i += 1
    return src[open_i:i]

# Mappa navigateTo('X') → URL reale per navbar e link interni nelle nuove pagine
NAV_MAP_IT = {
    "home":         "../index.html?skipintro=1#home",
    "chi-siamo":    "../chi-siamo/",
    "servizi":      "../index.html?skipintro=1#servizi",
    "make-up":      "../make-up/",
    "prodotti":     "../prodotti/",
    "sposa":        "../sposa/",
    "galleria":     "../index.html?skipintro=1#galleria",
    "contatti":     "../index.html?skipintro=1#contatti",
    "cookie-policy":"../index.html?skipintro=1#cookie-policy",
}
NAV_MAP_EN = {
    "home":         "../index-en.html?skipintro=1#home",
    "about-us":     "../index-en.html?skipintro=1#about-us",
    "services":     "../index-en.html?skipintro=1#services",
    "make-up":      "../index-en.html?skipintro=1#make-up",
    "products":     "../index-en.html?skipintro=1#products",
    "bridal":       "../bridal/",
    "gallery":      "../index-en.html?skipintro=1#gallery",
    "contact":      "../index-en.html?skipintro=1#contact",
    "cookie-policy":"../index-en.html?skipintro=1#cookie-policy",
}

# ---- Estrazione blocchi condivisi da index.html ----
HEAD_START = '<!DOCTYPE html>'
STYLE_START = '    <style>\n'
# Fine <style>: prima di </head> o di <!-- ===== INTRO VIDEO ===== -->
HEAD_END_MARKER = '</head>'
_ , _, style_end_pos = between(src_it, STYLE_START, '</head>')
STYLE_BLOCK_END = style_end_pos + len('</head>')
FULL_HEAD_SRC = src_it[:src_it.find('<body')]  # include DOCTYPE a <body escluso
BODY_CLOSE_POS = src_it.rfind('</body>')
SCRIPTS_RAW = src_it[src_it.find('<script type="application/ld+json">'): BODY_CLOSE_POS]
# Prendi tutti i <script> prima di application/ld per l'HTML (no INTRO), e tutta la porzione
# Eseguiamo estrazione più intelligente:
# Troviamo inizio <nav> e fine COOKIE BANNER per riprendere lightbox + script
NAV_HTML_START = src_it.find('<!-- ===== NAVIGATION ===== -->')
NAV_HTML_END   = src_it.find('<!-- ===== HOME ===== -->', NAV_HTML_START)
NAV_TEMPLATE_IT = src_it[NAV_HTML_START:NAV_HTML_END].strip()
FOOTER_START = src_it.find('<!-- ===== FOOTER ===== -->')
FOOTER_END   = src_it.find('<!-- ===== COOKIE BANNER ===== -->', FOOTER_START)
FOOTER_HTML = src_it[FOOTER_START:FOOTER_END].strip()
AFTER_FOOTER_SHARED = src_it[src_it.find('<!-- ===== COOKIE BANNER ===== -->') : src_it.rfind('</body>')]
# Rimuoviamo application/ld da AFTER_FOOTER_SHARED per essere sicuri (lo inseriamo per pagina):
AFTER_FOOTER_SHARED = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', AFTER_FOOTER_SHARED, count=1, flags=re.DOTALL)

# Toglie INTRO VIDEO block completamente (non serve nuove pagine)
# E strappa le funzioni JS di navigateTo INTRO e mzHashInit / setLang: rimpiazzeremo alla fine
JS_START_FULL = src_it[src_it.find('<script>') : src_it.rfind('</script>')+9]  # TUTTO inline script

def build_navbar(lang, active_page):
    """Crea navbar con link reali, nessun navigateTo. Lang: 'it' o 'en'."""
    if lang == "it":
        items = [
            ("Home",         NAV_MAP_IT["home"],         "home"),
            ("Chi Siamo",    NAV_MAP_IT["chi-siamo"],    "chi-siamo"),
            ("Servizi",      NAV_MAP_IT["servizi"],      "servizi"),
            ("Make Up",      NAV_MAP_IT["make-up"],      "make-up"),
            ("Prodotti",     NAV_MAP_IT["prodotti"],     "prodotti"),
            ("Sposa",        NAV_MAP_IT["sposa"],        "sposa"),
            ("Galleria",     NAV_MAP_IT["galleria"],     "galleria"),
            ("Contatti",     NAV_MAP_IT["contatti"],     "contatti"),
        ]
        cta_label, cta_href = "Prenota", NAV_MAP_IT["servizi"]
    else:
        items = [
            ("Home",         NAV_MAP_EN["home"],         "home"),
            ("About Us",     NAV_MAP_EN["about-us"],     "about-us"),
            ("Services",     NAV_MAP_EN["services"],     "services"),
            ("Make Up",      NAV_MAP_EN["make-up"],      "make-up"),
            ("Products",     NAV_MAP_EN["products"],     "products"),
            ("Bridal",       NAV_MAP_EN["bridal"],       "bridal"),
            ("Gallery",      NAV_MAP_EN["gallery"],      "gallery"),
            ("Contact",      NAV_MAP_EN["contact"],      "contact"),
        ]
        cta_label, cta_href = "Book Now", NAV_MAP_EN["services"]
    logo_href = NAV_MAP_IT["home"] if lang=="it" else NAV_MAP_EN["home"]
    html_links = []
    for label, href, key in items:
        cls = "active " if key == active_page else ""
        html_links.append(f'            <li><a class="{cls.rstrip()}" href="{href}">{label}</a></li>')
    lang_it_cls = "active" if lang=="it" else ""
    lang_en_cls = "active" if lang=="en" else ""
    lang_switch = f'''<div class="lang-switch">
                <button class="lang-btn {lang_it_cls}" onclick="pageSetLang('it')">IT</button>
                <button class="lang-btn {lang_en_cls}" onclick="pageSetLang('en')">EN</button>
            </div>'''
    nav = f'''<!-- ===== NAVIGATION ===== -->
<nav id="mainNav">
    <div class="nav-container">
        <a href="{logo_href}" class="logo">
            <img src="../logo-site.png" alt="MZ Parrucchieri"/>
            <span>Parrucchieri</span>
        </a>
        <ul class="nav-links" id="navLinks">
{chr(10).join(html_links)}
        </ul>
        <div class="nav-right">
            <a class="nav-cta" href="{cta_href}"><i class="fas fa-calendar-check"></i>{cta_label}</a>
            {lang_switch}
            <button class="hamburger" id="hamburger" onclick="toggleMenu()">
                <span></span><span></span><span></span>
            </button>
        </div>
    </div>
</nav>
'''
    return nav

def fix_paths(html_str, src_lang):
    """Fix percorsi immagini per pagine in sottocartella (aggiungi ../ davanti a path relativi)."""
    rules = [
        ('href="index.html"',              'href="../index.html?skipintro=1#home"'),
        ('href="index-en.html"',           'href="../index-en.html?skipintro=1#home"'),
        ('href="admin.html"',              'href="../admin.html"'),
        ('src="logo-mz.png"',              'src="../logo-mz.png"'),
        ('src="logo-site.png"',            'src="../logo-site.png"'),
        ('src="hero-luxury.png"',          'src="../hero-luxury.png"'),
        ('src="hero-monogram.png"',        'src="../hero-monogram.png"'),
        ('src="marmo-bianco.jpg"',         'src="../marmo-bianco.jpg"'),
        ('src="maurizio.jpg"',             'src="../maurizio.jpg"'),
        ('src="maurizio2.jpg"',            'src="../maurizio2.jpg"'),
        ('src="intro.mp4"',                'src="../intro.mp4"'),
        ('src="barber-icon-original.png"', 'src="../barber-icon-original.png"'),
        ('src="logo-barber-shop.jpg"',     'src="../logo-barber-shop.jpg"'),
        ('src="wedding-awards-2025.jpg"',  'src="../wedding-awards-2025.jpg"'),
        ('src="villanova-panorama.jpg"',   'src="../villanova-panorama.jpg"'),
        ('src="villafontana-panorama.jpg"','src="../villafontana-panorama.jpg"'),
        ('src="imola-panorama.jpg"',       'src="../imola-panorama.jpg"'),
        ('src="barber-panorama.jpg"',      'src="../barber-panorama.jpg"'),
        ('src="barber-bg.jpg"',            'src="../barber-bg.jpg"'),
        ('src="hero-bg.jpg"',              'src="../hero-bg.jpg"'),
        ('src="galleria/',                 'src="../galleria/'),
        ('src="makeup/',                   'src="../makeup/'),
        ('src="prodotti/',                 'src="../prodotti/'),
        ('src="sposa/',                    'src="../sposa/'),
        ('src="staff/',                    'src="../staff/'),
        ('href="salone-villanova-castenaso/"',  'href="../salone-villanova-castenaso/"'),
        ('href="salone-villafontana-medicina/"','href="../salone-villafontana-medicina/"'),
        ('href="salone-imola/"',           'href="../salone-imola/"'),
        ('href="barber-shop/"',            'href="../barber-shop/"'),
        ('data-fallback="prodotti/',       'data-fallback="../prodotti/'),
    ]
    for old, new in rules:
        html_str = html_str.replace(old, new)
    return html_str

def replace_navigates_to_links(inner, lang):
    """Sostituisce onclick='navigateTo("id")' con onclick='location.href="URL"'."""
    m = NAV_MAP_IT if lang=="it" else NAV_MAP_EN
    def sub(mo):
        pid = mo.group(1).strip()
        url = m.get(pid) or m.get("home")
        return f"location.href='{url}'"
    return re.sub(r"navigateTo\(\s*['\"]([A-Za-z0-9_-]+)['\"]\s*\)", sub, inner)

def build_common_inline_js(lang, current_page_tag):
    """Costruisce JS inline condiviso: toggleMenu, reveal, lightbox, setCookieConsent
    MA SENZA navigateTo / mzHashInit e con pageSetLang proprio."""
    # Leggo lo script da index.html e tolgo navigateTo, mzHashInit, setLang originale, INTRO
    raw = src_it[src_it.find("<script>")+8 : src_it.rfind("</script>")]
    # Rimuovo INTRO IIFE e sue funzioni helper
    cuts = [
        # (start marker, end marker)  escluso
        (r"// ===== INTRO VIDEO START =====", r"// ===== INTRO VIDEO END ====="),
        (r"// ===== NAVIGATION =====", r"// ===== COLLEGAMENTO TITOLI SEDI"),
        (r"// ===== DEEP LINK ADS", r"// ===== FOTO PRODOTTI"),
        (r"// ============ LANGUAGE SWITCH ============", r"// ============ CONTACT FORM ============"),
    ]
    # Cerca con regex multiline
    for a_pat, b_pat in cuts:
        a = re.search(a_pat, raw)
        b = re.search(b_pat, raw)
        if a and b and a.start() < b.start():
            raw = raw[:a.start()] + raw[b.start():]
    # Rimuovo startVideo() se rimasto
    raw = re.sub(r"\bstartVideo\s*\([^)]*\);?", "", raw)
    # Aggiungo pageSetLang personalizzato (mappa solo Sposa<->Bridal noto, resto home EN/IT)
    if lang == "it":
        lang_map_js = {
            "chi-siamo": {"en": "../index-en.html?skipintro=1#about-us",     "it": "../chi-siamo/"},
            "make-up":   {"en": "../index-en.html?skipintro=1#make-up",      "it": "../make-up/"},
            "prodotti":  {"en": "../index-en.html?skipintro=1#products",     "it": "../prodotti/"},
            "sposa":     {"en": "../bridal/",                                 "it": "../sposa/"},
            "dove-siamo":{"en": "../index-en.html?skipintro=1#about-us",     "it": "../dove-siamo/"},
        }
    else:
        lang_map_js = {
            "bridal":    {"en": "../bridal/",                                 "it": "../sposa/"},
        }
    jmap = json.dumps(lang_map_js[current_page_tag], ensure_ascii=False, indent=16)
    page_set_lang = f'''
// ===== PAGE LANGUAGE SWITCH (solo nuove pagine, non tocca home) =====
function pageSetLang(l) {{
    try {{ localStorage.setItem('mz_lang', l); }} catch(e) {{}}
    var MAP = {jmap};
    window.location.href = MAP[l] || (l==='en' ? '../index-en.html?skipintro=1#home' : '../index.html?skipintro=1#home');
}}
(function() {{
    try {{
        var saved = localStorage.getItem('mz_lang');
        if (!saved) return;
        var MAP = {jmap};
        var cur_lang = {"'it'" if lang=='it' else "'en'"};
        if (saved !== cur_lang && MAP[saved]) {{
            // Utente ha lingua diversa salvata: vai alla versione corretta o home equivalente
            window.location.replace(MAP[saved]);
        }}
    }} catch(e) {{}}
}})();
'''
    # Per sicurezza inizializzo toggleMenu se è stato rimosso
    return "<script>\n" + raw + "\n" + page_set_lang + "\n</script>"

def page_boilerplate(lang, page_id, title, meta_desc, canonical, hreflang_it, hreflang_en, main_content, og_image):
    """Assembla la pagina HTML completa."""
    og_image = og_image or "../hero-luxury.png"
    lang_attr = lang
    locale     = "it_IT" if lang=="it" else "en_US"
    hreflang_xdef = hreflang_it if lang=="it" else hreflang_en
    head = f'''<!DOCTYPE html>
<html lang="{lang_attr}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title)}</title>
    <meta name="description" content="{html.escape(meta_desc)}">
    <meta name="keywords" content="MZ Parrucchieri, {html.escape(title)}">
    <meta name="author" content="MZ Parrucchieri - Maurizio Zucchini">
    <meta name="robots" content="index, follow">
    <meta name="theme-color" content="#1a1a1a">
    <meta name="format-detection" content="telephone=no, address=no, email=no">
    <link rel="canonical" href="{canonical}">
    <link rel="alternate" hreflang="it" href="{hreflang_it}">
    <link rel="alternate" hreflang="en" href="{hreflang_en}">
    <link rel="alternate" hreflang="x-default" href="{hreflang_xdef}">
    <meta http-equiv="X-Frame-Options" content="SAMEORIGIN">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta name="Referrer-Policy" content="strict-origin-when-cross-origin">
    <meta name="Permissions-Policy" content="camera=(), microphone=(), geolocation=(self), payment=()">
    <link rel="icon" type="image/png" href="../logo-mz.png">
    <link rel="apple-touch-icon" href="../logo-mz.png">
    <meta property="og:title" content="{html.escape(title)}">
    <meta property="og:description" content="{html.escape(meta_desc)}">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="{locale}">
    <meta property="og:image" content="{og_image}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{html.escape(title)}">
    <meta name="twitter:description" content="{html.escape(meta_desc)}">
    <meta name="twitter:image" content="{og_image}">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&family=Inter:wght@200;300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
'''
    # Estraggo <style> da index.html
    style_text = src_it[src_it.find('<style>')+8 : src_it.find('</style>')]
    # Tolgo da INTRO start a INTRO end (non serve):
    style_text = re.sub(r"\s*/\* ===== INTRO VIDEO ===== \*/.*?\n\s*/\* ===== NAV ===== \*/",
                        "\n        /* ===== NAV ===== */",
                        style_text, count=1, flags=re.DOTALL)
    # Rimango classi .intro-overlay .intro-video (non servono, ma non danneggiano)
    head += style_text + "    </style>\n</head>\n<body>\n"

    nav = build_navbar(lang, page_id)
    # Fix paths footer
    footer_html = fix_paths(replace_navigates_to_links(FOOTER_HTML, lang), lang)
    # Cookie banner content in IT o EN? Per le pagine EN riusiamo quello in index-en.html
    if lang == "it":
        banner_html = src_it[src_it.find('<!-- ===== COOKIE BANNER ===== -->') : src_it.find('<script type="application/ld+json">')]
    else:
        banner_html = src_en[src_en.find('<!-- ===== COOKIE BANNER ===== -->') : src_en.find('<script type="application/ld+json">')]
    banner_html = fix_paths(replace_navigates_to_links(banner_html, lang), lang)

    # Lightbox e struttura post-footer
    lightboxes = src_it[src_it.find('<!-- ===== STAFF LIGHTBOX ===== -->') : src_it.find('<!-- ===== COOKIE POLICY ===== -->')]
    cookie_policy_page = src_it[src_it.find('<!-- ===== COOKIE POLICY ===== -->') : src_it.find('<!-- ===== FOOTER ===== -->', src_it.find('<!-- ===== COOKIE POLICY ===== -->'))]
    cookie_policy_page = fix_paths(cookie_policy_page, lang)
    # Application ld+json lasciamo fuori dalle landing, il SEO della home rimane quello.

    # JS
    js_inline = build_common_inline_js(lang, page_id)

    body_tail = "\n" + footer_html + "\n\n" + banner_html + "\n\n" + lightboxes + "\n\n" + cookie_policy_page + "\n\n" + js_inline + "\n\n" + AFTER_FOOTER_SHARED
    # Chiudi body/html
    body_tail += "</body>\n</html>"

    return head + nav + "\n<main>\n" + main_content + "\n</main>\n" + body_tail

# ---------- PAGINE ----------
TARGETS = []

# 1) chi-siamo
content_chi_siamo = get_page_content(src_it, "chi-siamo")
content_chi_siamo = replace_navigates_to_links(content_chi_siamo, "it")
content_chi_siamo = fix_paths(content_chi_siamo, "it")
TARGETS.append({
    "slug": "chi-siamo", "lang": "it", "page_id": "chi-siamo",
    "title": "Chi Siamo | MZ Parrucchieri — Hair Studio",
    "desc": "MZ Parrucchieri: la storia, il fondatore Maurizio Zucchini, le quattro sedi e il team di parrucchieri e hairstylist tra Villanova Castenaso, Villafontana Medicina, Imola e Barber Shop.",
    "canonical": "https://www.mzparrucchieri.it/chi-siamo/",
    "hreflang_it": "https://www.mzparrucchieri.it/chi-siamo/",
    "hreflang_en": "https://www.mzparrucchieri.it/index-en.html#about-us",
    "content": content_chi_siamo,
    "og_img": "../maurizio.jpg",
})

# 2) make-up
content_makeup = get_page_content(src_it, "make-up")
content_makeup = replace_navigates_to_links(content_makeup, "it")
content_makeup = fix_paths(content_makeup, "it")
TARGETS.append({
    "slug": "make-up", "lang": "it", "page_id": "make-up",
    "title": "Make Up Professionale | MZ Parrucchieri",
    "desc": "Make up sposa, cerimonia, eventi e shooting fotografico con prodotti Make Up For Ever. Trucco personalizzato firmato MZ Parrucchieri in 4 saloni tra Bologna e Imola.",
    "canonical": "https://www.mzparrucchieri.it/make-up/",
    "hreflang_it": "https://www.mzparrucchieri.it/make-up/",
    "hreflang_en": "https://www.mzparrucchieri.it/index-en.html#make-up",
    "content": content_makeup,
    "og_img": "../makeup/makeup-hero.jpg",
})

# 3) prodotti
content_prod = get_page_content(src_it, "prodotti")
content_prod = replace_navigates_to_links(content_prod, "it")
content_prod = fix_paths(content_prod, "it")
TARGETS.append({
    "slug": "prodotti", "lang": "it", "page_id": "prodotti",
    "title": "Marchi e Prodotti Professionali | MZ Parrucchieri",
    "desc": "I marchi professionali scelti da MZ Parrucchieri: Nashi Argan, Make Up For Ever, ghd e Level 3 per Barber Shop. Qualità per il trattamento dei capelli e make up.",
    "canonical": "https://www.mzparrucchieri.it/prodotti/",
    "hreflang_it": "https://www.mzparrucchieri.it/prodotti/",
    "hreflang_en": "https://www.mzparrucchieri.it/index-en.html#products",
    "content": content_prod,
    "og_img": "../prodotti/prodotti-hero.jpg",
})

# 4) sposa
content_sposa = get_page_content(src_it, "sposa")
content_sposa = replace_navigates_to_links(content_sposa, "it")
content_sposa = fix_paths(content_sposa, "it")
TARGETS.append({
    "slug": "sposa", "lang": "it", "page_id": "sposa",
    "title": "Acconciature Sposa e Bridal | MZ Parrucchieri",
    "desc": "Acconciature da sposa, make up bridal e prova acconciatura personalizzata. MZ Parrucchieri vincitore Wedding Awards 2025 per le acconciature sposa a Bologna.",
    "canonical": "https://www.mzparrucchieri.it/sposa/",
    "hreflang_it": "https://www.mzparrucchieri.it/sposa/",
    "hreflang_en": "https://www.mzparrucchieri.it/bridal/",
    "content": content_sposa,
    "og_img": "../sposa/sposa-bouquet-interno.jpg",
})

# 5) bridal  (EN, da page-bridal in index-en.html)
content_bridal = get_page_content(src_en, "bridal")
# Per la navbar EN, active page = "bridal"
# translate_navigates: usiamo mappa EN
def rpl_en(s): return replace_navigates_to_links(s, "en")
content_bridal = fix_paths(rpl_en(content_bridal), "en")
TARGETS.append({
    "slug": "bridal", "lang": "en", "page_id": "bridal",
    "title": "Bridal Hairstyles & Make Up | MZ Parrucchieri",
    "desc": "Bridal hairstyles, wedding make up and personalised hair trial. MZ Parrucchieri: winner of Wedding Awards 2025 near Bologna and Imola, Italy.",
    "canonical": "https://www.mzparrucchieri.it/bridal/",
    "hreflang_it": "https://www.mzparrucchieri.it/sposa/",
    "hreflang_en": "https://www.mzparrucchieri.it/bridal/",
    "content": content_bridal,
    "og_img": "../sposa/sposa-bouquet-interno.jpg",
})

# 6) dove-siamo (estratto da page-chi-siamo: sezione "Dove trovarci" e 4 cards sedi)
# Prendo da chi-siamo content già path sistemato, la porzione dal marcatore sezione-header
# "Dove trovarci" alla fine delle cards sedi.
a = content_chi_siamo.find('<div style="margin-top:120px">')
b = content_chi_siamo.find('<div class="staff-section">', a)
sedi_block = content_chi_siamo[a:b]
# Hero iniziale per dare una pagina piena invece che direttamente cards (come home ha hero)
hero_dove_siamo = '''<section class="hero">
        <div class="hero-luxury-bg"></div>
        <div class="hero-luxury-overlay"></div>
        <div class="hero-grid"></div>
        <div class="hero-content">
            <p class="hero-eyebrow">Dove trovarci</p>
            <h1>Quattro Sedi,<br>una sola <span>eccellenza</span></h1>
            <p>Villanova di Castenaso, Villafontana di Medicina, Imola e Barber Shop Medicina: quattro atelier MZ Parrucchieri tra Bologna e Imola, facilmente raggiungibili.</p>
            <div class="hero-buttons">
                <a class="btn-primary" href="../salone-villanova-castenaso/">Villanova di Castenaso</a>
                <a class="btn-secondary" href="../salone-villafontana-medicina/">Villafontana Medicina</a>
            </div>
            <div class="hero-salon-label">
                <a href="../salone-villanova-castenaso/" style="color:inherit;text-decoration:none">Villanova di Castenaso</a>
                <span class="sep">•</span>
                <a href="../salone-villafontana-medicina/" style="color:inherit;text-decoration:none">Villafontana di Medicina</a>
                <span class="sep">•</span>
                <a href="../salone-imola/" style="color:inherit;text-decoration:none">Imola</a>
                <span class="sep">•</span>
                <a href="../barber-shop/" style="color:inherit;text-decoration:none">Barber Shop Medicina</a>
            </div>
        </div>
    </section>
'''
dove_body = f'''{hero_dove_siamo}
    <section class="section marble-section" style="padding:100px 0">
        <div class="container">
            {sedi_block}
        </div>
    </section>
'''
TARGETS.append({
    "slug": "dove-siamo", "lang": "it", "page_id": "dove-siamo",
    "title": "Dove Siamo | MZ Parrucchieri - 4 Saloni tra Bologna e Imola",
    "desc": "Trova il salone MZ Parrucchieri più vicino: Villanova di Castenaso, Villafontana di Medicina, Imola e Barber Shop Medicina. Orari, telefoni, WhatsApp e mappe Google.",
    "canonical": "https://www.mzparrucchieri.it/dove-siamo/",
    "hreflang_it": "https://www.mzparrucchieri.it/dove-siamo/",
    "hreflang_en": "https://www.mzparrucchieri.it/index-en.html#about-us",
    "content": dove_body,
    "og_img": "../villanova-panorama.jpg",
})

# ---------- SCRIVI FILE ----------
os.makedirs(ROOT, exist_ok=True)
for t in TARGETS:
    slug_dir = os.path.join(ROOT, t["slug"])
    os.makedirs(slug_dir, exist_ok=True)
    out_path = os.path.join(slug_dir, "index.html")
    full_html = page_boilerplate(
        lang=t["lang"], page_id=t["page_id"],
        title=t["title"], meta_desc=t["desc"],
        canonical=t["canonical"], hreflang_it=t["hreflang_it"], hreflang_en=t["hreflang_en"],
        main_content=t["content"], og_image=t["og_img"]
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print("OK →", out_path)

print("\nGenerazione completata. 6 pagine create.")
