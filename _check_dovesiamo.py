import re

FILES = ['dove-siamo/index.html', 'dove-siamo/index-en.html']
for f in FILES:
    with open(f) as fp:
        c = fp.read()
    print(f'=== {f} ===')
    print(f'  Dimensione: {len(c)} bytes')
    print(f'  <html: {c.count("<html")} / </html>: {c.count("</html")}')
    print(f'  <head: {c.count("<head")} / </head>: {c.count("</head")}')
    print(f'  <body: {c.count("<body")} / </body>: {c.count("</body")}')
    print(f'  <script: {c.count("<script")} / </script>: {c.count("</script")}')
    print(f'  <style: {c.count("<style")} / </style>: {c.count("</style")}')
    print(f'  gtag AW-471648853: {c.count("AW-471648853")}')
    print(f'  function pageSetLang(l): {c.count("function pageSetLang(l)")}')
    FETCH_IT = "fetch('content/promo.json'"
    FETCH_EN = "fetch('content/promo-en.json'"
    print(f'  fetch promo.json: {c.count(FETCH_IT)}')
    print(f'  fetch promo-en.json: {c.count(FETCH_EN)}')
    # active class
    it_active = len(re.findall(r'lang-btn active.*pageSetLang\(\x27it\x27\)', c))
    en_active = len(re.findall(r'lang-btn active.*pageSetLang\(\x27en\x27\)', c))
    print(f'  lang-btn active IT: {it_active}  EN: {en_active}')
    # cur_lang per dove-siamo
    if 'index-en' in f:
        cur_en = c.count("cur_lang = 'en'") + c.count('cur_lang="en"')
        print(f'  cur_lang=en: {cur_en}')
    if 'index-en' in f:
        markers_it = [
            'Prenota su WhatsApp','Settembre','Trattamento Illuminante','Rituale barba',
            'Sedi valide','Scade il','Prenota ora','Settimana','Chi Siamo','Dove siamo',
            'Orari di apertura','Indirizzo','Numero di telefono','Prenota','Scopri',
            'Lunedì','Martedì','Mercoledì','Giovedì','Venerdì','Sabato','Domenica'
        ]
        found = []
        for m in markers_it:
            cnt = c.count(m)
            if cnt:
                found.append(f'{repr(m)} x{cnt}')
        if found:
            print(f'  ⚠️  Residui IT: {found}')
        else:
            print(f'  ✅ Nessun residuo IT')
    else:
        # file IT: cerco label promo EN che non dovrebbero esserci
        markers_en_promo = ['Book on WhatsApp','September','Expires on','Illuminating & Purifying','Complete 30-minute']
        found = []
        for m in markers_en_promo:
            cnt = c.count(m)
            if cnt:
                found.append(f'{repr(m)} x{cnt}')
        if found:
            print(f'  ⚠️  Residui EN in IT: {found}')
        else:
            print(f'  ✅ Promo IT corrette')
    print()
