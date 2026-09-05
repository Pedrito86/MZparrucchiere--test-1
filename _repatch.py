#!/usr/bin/env python3
import os
APP = "/Users/pietro/Desktop/ultima versione sito web zucchini/app"
FILES = [
    'index.html', 'index-en.html',
    'salone-villanova-castenaso/index.html', 'salone-villanova-castenaso/index-en.html',
    'salone-villafontana-medicina/index.html', 'salone-villafontana-medicina/index-en.html',
    'salone-imola/index.html', 'salone-imola/index-en.html',
    'barber-shop/index.html', 'barber-shop/index-en.html',
    'chi-siamo/index.html', 'make-up/index.html', 'prodotti/index.html',
    'sposa/index.html', 'bridal/index.html',
    'dove-siamo/index.html', 'dove-siamo/index-en.html',
]
START_MARKER = "        /* ===== MOBILE LANDSCAPE FIX:"
END_MARKER = "        /* ===== REVEAL ON SCROLL ===== */"
NEW_PATCH = """
        /* ===== MOBILE LANDSCAPE FIX: navbar overflow e pulsanti mancanti ===== */
        @media (max-width: 1024px) and (orientation: landscape), (min-width: 740px) and (max-width: 1024px) {
            .navbar { padding: 10px 24px; }
            .hamburger { display: flex; }
            .nav-links {
                display: none !important;
                position: fixed;
                top: 0; right: 0;
                width: min(420px, 86vw);
                height: 100vh; height: 100svh;
                background: rgba(18,18,18,0.98);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border-left: 1px solid rgba(255,255,255,0.06);
                flex-direction: column;
                align-items: flex-start;
                justify-content: flex-start;
                padding: 96px 36px 36px;
                margin: 0;
                gap: 4px;
                z-index: 999;
                overflow-y: auto;
            }
            .nav-links.active {
                display: flex !important;
                animation: slideInRight 0.35s var(--ease-out-expo) both;
            }
            @keyframes slideInRight { from { transform: translateX(100%); opacity: 0.2; } to { transform: translateX(0); opacity: 1; } }
            .nav-links li { width: 100%; border-bottom: 1px solid rgba(255,255,255,0.05); }
            .nav-links li a { font-size: 0.78rem; letter-spacing: 2.2px; padding: 16px 4px; display: block; width: 100%; }
            .nav-right { gap: 12px; }
            .nav-right > .nav-cta {
                display: inline-flex !important;
                visibility: visible !important;
                padding: 10px 18px;
                font-size: 0.62rem;
                letter-spacing: 1.8px;
            }
            .nav-right > .nav-cta i { font-size: 0.7rem; }
            #navLinks { display: none !important; }
            #navLinks.active { display: flex !important; }
            .nav-right > .lang-switch { padding: 3px; }
            .nav-right > .lang-switch .lang-btn { padding: 5px 10px; font-size: 0.58rem; letter-spacing: 1.1px; }
        }
        @media (max-width: 740px) and (orientation: landscape) {
            .navbar { padding: 8px 18px; }
            .nav-right > .nav-cta { padding: 9px 14px; font-size: 0.58rem; letter-spacing: 1.5px; }
            .nav-right > .lang-switch .lang-btn { padding: 4px 8px; font-size: 0.55rem; }
        }

"""
for rel in FILES:
    p = os.path.join(APP, rel)
    with open(p, 'r', encoding='utf-8') as f: h = f.read()
    s = h.find(START_MARKER)
    e = h.find(END_MARKER, s)
    if s < 0 or e < 0:
        print(f"  SKIP markers not found: {rel}")
        continue
    h2 = h[:s] + NEW_PATCH + h[e:]
    with open(p, 'w', encoding='utf-8') as f: f.write(h2)
    print(f"  RE-PATCHED ✓ {rel}")
