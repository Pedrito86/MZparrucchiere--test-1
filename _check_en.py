#!/usr/bin/env python3
import os, http.client, threading, time
APP = "/Users/pietro/Desktop/ultima versione sito web zucchini/app"
os.chdir(APP)
from http.server import HTTPServer, SimpleHTTPRequestHandler
server = HTTPServer(('127.0.0.1', 8093), SimpleHTTPRequestHandler)
t = threading.Thread(target=server.serve_forever, daemon=True); t.start(); time.sleep(1)
conn = http.client.HTTPConnection('127.0.0.1', 8093, timeout=8)
URLS = [
    '/salone-villanova-castenaso/index-en.html',
    '/salone-villafontana-medicina/index-en.html',
    '/salone-imola/index-en.html',
    '/barber-shop/index-en.html',
    '/dove-siamo/index-en.html'
]
CHECK_IT = [
    'Lunedì','Martedì','Mercoledì','Giovedì','Venerdì','Sabato','Domenica',
    'Taglio Psico','Solo Taglio Donna','Meches','Trattamento Nashi Argan',
    'Listino Prezzi','Prenota WhatsApp','Chiama subito','Prenota ora',
    'Passa a trovarci','Scrivici su WhatsApp','Listino 2026 ufficiale',
    'le nostre sedi','Dove siamo','Chi Siamo','Servizi e Tariffe',
    'Villanova di Castenaso troverete','vicino Bologna, troverete',
    'Orari Lun 10-18','Mer fino a 21','Recensisci','Raggiungici',
    'Ora aperti','Chiude alle','Riapre alle',
    'Taglio & Piega','Cut Ragazzo','Rifinitura Barba',
    'Tariffe aggiornate 2026','Tutti i servizi del nostro Barber Shop',
    'Scopri listino','I nostri barbieri','Listini 2026 ufficiali',
    'Tre artigiani della cura maschile','Nel Barber Shop di Medicina troverai',
    'Foto precedente','Foto successiva',
    'Servizi e contenuti di',
]
CHECK_EN = ['Monday','Tuesday','Wednesday','Opening Hours','Price List','WhatsApp Booking','Call Us','Book Now','Precision Cut','Blow-dry','Haircuts','Address','Phone','Discover the Salon','Leave a Review','Get Directions','Services & Prices','Contact & Opening Hours','About Us']
for u in URLS:
    conn.request('GET', u); r = conn.getresponse(); body = r.read().decode('utf-8', 'ignore')
    it_left = [w for w in CHECK_IT if w in body]
    en_hits  = [w for w in CHECK_EN if w in body]
    print(f'  HTTP {r.status} {len(body):7d} B {u:58s}')
    print(f'      ✅ EN tokens found: {len(en_hits)}/{len(CHECK_EN)}  — {en_hits[:10]}…')
    print(f'      ⚠️  IT residual:      {it_left[:15]}')
    print()
server.shutdown()
