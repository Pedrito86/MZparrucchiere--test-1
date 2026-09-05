#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RIGENERA TUTTE LE 5 PAGINE EN (4 saloni + dove-siamo) partendo dal file IT originale
e applicando un dizionario di traduzioni AMPIO e SICURO (SOLO stringhe testuali,
NESSUNA sostituzione di singole lettere - NO più 'a' -> 'to').
"""
import os

APP = "/Users/pietro/Desktop/ultima versione sito web zucchini/app"

# =========== DIZIONARIO TRADUZIONI SICURO ============
# Solo SOTTOSTRINGHE LUNGHE: nessuna lettera singola, nessuna parola chiave JS
TRAD = {
    # --- HTML LANG / META ---
    '<html lang="it">': '<html lang="en">',
    'property="og:locale" content="it_IT">': 'property="og:locale" content="en_US">',

    # --- Villanova DI CASTENASO ---
    'MZ Parrucchieri Villanova di Castenaso | Parrucchiere': 'MZ Parrucchieri Villanova di Castenaso | Hairdresser',
    '<meta name="description" content="MZ Parrucchieri a Villanova di Castenaso (BO): taglio, colore, pieghe, trattamenti Nashi Argan, meches, make up e acconciature sposa. Prenota ora per telefono o WhatsApp.">':
        '<meta name="description" content="MZ Parrucchieri salon in Villanova di Castenaso (Bologna): cuts, colour, blow-dries, Nashi Argan treatments, highlights, make up and bridal hairstyling. Book now by phone or WhatsApp.">',
    '<meta name="keywords" content="parrucchiere Villanova di Castenaso, Villanova Castenaso, taglio capelli, colore capelli, Nashi Argan, acconciature sposa, make up, MZ Parrucchieri">':
        '<meta name="keywords" content="hairdresser Villanova di Castenaso, Villanova Castenaso, haircut, hair colour, Nashi Argan, bridal hairstyling, make up, MZ Parrucchieri">',
    '<meta property="og:description" content="MZ Parrucchieri a Villanova di Castenaso (BO): taglio, colore, pieghe, trattamenti Nashi Argan, meches, make up e acconciature sposa. Prenota per telefono o WhatsApp.">':
        '<meta property="og:description" content="MZ Parrucchieri salon in Villanova di Castenaso (Bologna): cuts, colour, blow-dries, Nashi Argan treatments, highlights, make up and bridal hairstyling. Book by phone or WhatsApp.">',
    '<link rel="canonical" href="https://www.mzparrucchieri.it/salone-villanova-castenaso/">':
        '<link rel="canonical" href="https://www.mzparrucchieri.it/salone-villanova-castenaso/index-en.html">',
    '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-villanova-castenaso/">':
        '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-villanova-castenaso/"><link rel="alternate" hreflang="en" href="https://www.mzparrucchieri.it/salone-villanova-castenaso/index-en.html">',
    # --- Villafontana DI MEDICINA ---
    'MZ Parrucchieri Villafontana di Medicina | Parrucchiere': 'MZ Parrucchieri Villafontana di Medicina | Hairdresser',
    '<meta name="description" content="MZ Parrucchieri a Villafontana di Medicina (BO): taglio, colore, pieghe, styling, trattamenti Nashi Argan, meches, make up e acconciature sposa. Prenota per WhatsApp o telefono.">':
        '<meta name="description" content="MZ Parrucchieri salon in Villafontana di Medicina (Bologna): cuts, colour, blow-dries, styling, Nashi Argan treatments, highlights, make up and bridal hairstyling. Book by WhatsApp or phone.">',
    '<meta name="keywords" content="parrucchiere Villafontana di Medicina, parrucchiere Medicina Bologna, taglio capelli, colore capelli, Villafontana di Medicina, Nashi Argan, meches, make up, acconciature sposa">':
        '<meta name="keywords" content="hairdresser Villafontana di Medicina, salon Medicina Bologna, haircut, hair colour, Villafontana di Medicina, Nashi Argan, highlights, make up, bridal hairstyling">',
    '<meta property="og:description" content="MZ Parrucchieri: eccellenza nel taglio, colore, make up e acconciature sposa dal 2004. Quattro saloni a Villanova di Castenaso, Villafontana di Medicina, Imola e Barber Shop Medicina.">':
        '<meta property="og:description" content="MZ Parrucchieri Villafontana di Medicina salon: luxury cuts, colour, Nashi Argan, bridal. Book now.">',
    '<link rel="canonical" href="https://www.mzparrucchieri.it/salone-villafontana-medicina/">':
        '<link rel="canonical" href="https://www.mzparrucchieri.it/salone-villafontana-medicina/index-en.html">',
    '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-villafontana-medicina/">':
        '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-villafontana-medicina/"><link rel="alternate" hreflang="en" href="https://www.mzparrucchieri.it/salone-villafontana-medicina/index-en.html">',
    # --- IMOLA ---
    'MZ Parrucchieri Imola | Parrucchiere': 'MZ Parrucchieri Imola | Hairdresser',
    '<meta name="description" content="MZ Parrucchieri Imola (BO): taglio, colore, trattamenti, styling, Nashi Argan, pieghe, make up e acconciature sposa. Prenota per telefono o WhatsApp.">':
        '<meta name="description" content="MZ Parrucchieri salon in Imola (Bologna): cuts, colour, treatments, styling, Nashi Argan, blow-dries, make up and bridal hairstyling. Book by phone or WhatsApp.">',
    '<meta name="keywords" content="parrucchiere Imola, MZ Parrucchieri Imola, taglio capelli Imola, colore capelli Imola, Nashi Argan Imola, acconciature sposa Imola, make up Imola, Piazza Gramsci Imola">':
        '<meta name="keywords" content="hairdresser Imola, MZ Parrucchieri Imola, haircut Imola, hair colour Imola, Nashi Argan Imola, bridal hairstyling Imola, make up Imola, Piazza Gramsci Imola">',
    '<link rel="canonical" href="https://www.mzparrucchieri.it/salone-imola/">':
        '<link rel="canonical" href="https://www.mzparrucchieri.it/salone-imola/index-en.html">',
    '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-imola/">':
        '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/salone-imola/"><link rel="alternate" hreflang="en" href="https://www.mzparrucchieri.it/salone-imola/index-en.html">',
    # --- BARBER SHOP ---
    'MZ Barber Shop Medicina · Taglio Uomo, Barba e Barber Tradizionale': 'MZ Barber Shop Medicina · Men\'s Haircut, Beard & Traditional Barbering',
    '<meta name="description" content="MZ Barber Shop Medicina (BO). Taglio uomo, ragazzo, bimbo, rifiniture barba, Barba Spa e rasature tradizionali con asciugamani caldi. Prenota per WhatsApp o telefono.">':
        '<meta name="description" content="MZ Barber Shop Medicina (Bologna). Men\'s, teen and kids\' haircuts, beard trims, Beard Spa and traditional hot-towel shaves. Book by WhatsApp or phone.">',
    '<meta name="keywords" content="barber shop Medicina, barbiere Medicina, taglio uomo, barba Medicina, rasatura tradizionale, MZ Barber Shop, Zucchini Maurizio">':
        '<meta name="keywords" content="barber shop Medicina, barber Medicina, men\'s haircut, beard Medicina, traditional shave, MZ Barber Shop, Zucchini Maurizio">',
    '<link rel="canonical" href="https://www.mzparrucchieri.it/barber-shop/">':
        '<link rel="canonical" href="https://www.mzparrucchieri.it/barber-shop/index-en.html">',
    '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/barber-shop/">':
        '<link rel="alternate" hreflang="it" href="https://www.mzparrucchieri.it/barber-shop/"><link rel="alternate" hreflang="en" href="https://www.mzparrucchieri.it/barber-shop/index-en.html">',

    # --- NAVBAR ---
    '<li><a href="../index.html?skipintro=1#home">Home</a></li>': '<li><a href="../index-en.html?skipintro=1#home">Home</a></li>',
    '<li><a href="../index.html?skipintro=1#chi-siamo">Chi Siamo</a></li>': '<li><a href="../index-en.html?skipintro=1#about-us">About Us</a></li>',
    '<li><a href="../index.html?skipintro=1#servizi">Servizi</a></li>': '<li><a href="../index-en.html?skipintro=1#services">Services</a></li>',
    '<li><a href="../make-up/">Make Up</a></li>': '<li><a href="../index-en.html?skipintro=1#make-up">Make Up</a></li>',
    '<li><a href="../index.html?skipintro=1#make-up">Make Up</a></li>': '<li><a href="../index-en.html?skipintro=1#make-up">Make Up</a></li>',
    '<li><a href="../index.html?skipintro=1#galleria">Galleria</a></li>': '<li><a href="../index-en.html?skipintro=1#gallery">Gallery</a></li>',
    '<li><a href="../index.html?skipintro=1#contatti">Contatti</a></li>': '<li><a href="../index-en.html?skipintro=1#contact">Contact</a></li>',
    '<li><a href="../index.html?skipintro=1#prodotti">Prodotti</a></li>': '<li><a href="../index-en.html?skipintro=1#products">Products</a></li>',
    '<li><a href="../prodotti/">Prodotti</a></li>': '<li><a href="../index-en.html?skipintro=1#products">Products</a></li>',
    '<li><a href="../index.html?skipintro=1#sposa">Sposa</a></li>': '<li><a href="../bridal/">Bridal</a></li>',
    '<li><a href="../sposa/">Sposa</a></li>': '<li><a href="../bridal/">Bridal</a></li>',
    '<i class="fab fa-whatsapp"></i>Prenota': '<i class="fab fa-whatsapp"></i>Book Now',
    '<i class="fas fa-phone"></i> Prenota · 051 782249': '<i class="fas fa-phone"></i> Book · 051 782249',
    '<i class="fas fa-phone"></i> Prenota · ': '<i class="fas fa-phone"></i> Book · ',
    'Prenota ora il tuo <span>appuntamento</span>': 'Book your <span>appointment</span> now',

    # --- PAGESET LANG BUTTONS (en file => EN active) ---
    '                <button class="lang-btn active" onclick="pageSetLang(\'it\')">IT</button>\n                <button class="lang-btn" onclick="pageSetLang(\'en\')">EN</button>':
        '                <button class="lang-btn" onclick="pageSetLang(\'it\')">IT</button>\n                <button class="lang-btn active" onclick="pageSetLang(\'en\')">EN</button>',

    # --- HERO SALONE Eyebrow & H1 / LEAD ---
    'Salone di eccellenza · Villanova':       'Excellence Salon · Villanova',
    'L\'eccellenza del parrucchiere a Castenaso': 'Hairdressing excellence in Castenaso',
    'Taglio, colore, pieghe e styling d\'autore. Trattamenti professionali Nashi Argan, make up e acconciature sposa nel cuore di Villanova di Castenaso.':
        'Signature cuts, colour, blow-dries and styling. Professional Nashi Argan treatments, make up and bridal hairstyling in the heart of Villanova di Castenaso.',
    'Villanova di Castenaso · Salone MZ dal 2019': 'Villanova di Castenaso · MZ Salon since 2019',

    'Salone di eccellenza · Villafontana':    'Excellence Salon · Villafontana',
    'L\'eccellenza del parrucchiere a Bologna': 'Hairdressing excellence in Bologna',
    'Taglio, colore, pieghe e styling d\'autore. Trattamenti professionali Nashi Argan, make up e acconciature sposa nel cuore di Villafontana di Medicina.':
        'Signature cuts, colour, blow-dries and styling. Professional Nashi Argan treatments, make up and bridal hairstyling in the heart of Villafontana di Medicina.',
    'Villafontana di Medicina · Dal 2004 nel cuore di Villafontana': 'Villafontana di Medicina · Since 2004 in the heart of Villafontana',

    'Salone di eccellenza · Imola':           'Excellence Salon · Imola',
    'L\'eccellenza del parrucchiere a Imola': 'Hairdressing excellence in Imola',
    'Taglio, colore, pieghe e styling d\'autore. Trattamenti professionali Nashi Argan, make up e acconciature sposa nel cuore di Imola.':
        'Signature cuts, colour, blow-dries and styling. Professional Nashi Argan treatments, make up and bridal hairstyling in the heart of Imola.',
    'Imola · MZ Parrucchieri in Piazza Gramsci': 'Imola · MZ Parrucchieri on Piazza Gramsci',

    'Barber Shop · L\'arte tradizionale del barbiere': 'Barber Shop · The traditional art of barbering',
    'Rifiniture barba, rasature e taglio uomo.': 'Beard trims, shaves and men\'s haircuts.',
    'Barber Shop Medicina · Taglio Uomo, Barba e Rasature Tradizionali': 'Barber Shop Medicina · Men\'s Cuts, Beard & Traditional Shaves',
    'MZ Barber Shop Medicina · L\'arte del barbiere tradizionale': 'MZ Barber Shop Medicina · The traditional barbering craft',
    'Taglio uomo classico e moderno, rifiniture barba, Barba Spa e rasature tradizionali con asciugamani caldi nel centro di Medicina.':
        'Classic and modern men\'s haircuts, beard trims, Beard Spa and traditional hot-towel shaves in the centre of Medicina.',

    # --- HERO INFO ---
    'Indirizzo': 'Address',
    'Telefono': 'Phone',
    'Prenota un appuntamento': 'Book an appointment',

    # --- HERO BUTTONS ---
    'Prenota ora': 'Book Now',
    'Chiama subito': 'Call Now',
    'Scrivici su WhatsApp': 'WhatsApp Us',
    '<i class="fab fa-whatsapp"></i> Prenota WhatsApp': '<i class="fab fa-whatsapp"></i> WhatsApp Booking',
    'Appuntamento': 'Book Appointment',
    'Passa a trovarci': 'Come & Visit Us',

    # --- SCROLL INDICATOR LABELS ---
    'Listino e Servizi': 'Services & Price List',
    'Il Team del salone': 'Salon Team',
    'Portfolio Lavori': 'Portfolio',
    'Panoramica 360° del Salone': '360° Salon Overview',

    # --- SERVIZI E TARIFFE / LISTINO ---
    'Servizi e Tariffe': 'Services & Prices',
    'Listino <span>Prezzi</span>': 'Price <span>List</span>',
    'I prezzi ufficiali della sede Villanova di Castenaso': 'Official prices of the Villanova di Castenaso salon',
    'I prezzi ufficiali della sede Villafontana di Medicina': 'Official prices of the Villafontana di Medicina salon',
    'I prezzi ufficiali della sede Imola': 'Official prices of the Imola salon',
    'Taglio & Piega':      'Cut & Blow-dry',
    'Solo Taglio Donna':   'Ladies\' Cut Only',
    'Piega':               'Blow-dry',
    'Meches / Colpi di sole': 'Highlights / Balayage',
    'Colore':              'Colour',
    'Trattamento Nashi Argan': 'Nashi Argan Treatment',
    'Taglio Uomo':         'Men\'s Cut',
    'Acconciatura Sposa':  'Bridal Hairstyle',
    'Make Up Sposa':       'Bridal Make Up',
    'Taglio Ragazzo 13-17': 'Teens 13-17 Cut',
    'Taglio Bimbo 0-12':   'Kids 0-12 Cut',
    'Taglio Senior 65+':   'Senior 65+ Cut',
    'Taglio Ragazzo':      'Teens Cut',
    'Rifinitura Barba':    'Beard Trim',
    'Barba Spa':           'Beard Spa',
    'Rasatura Tradizionale': 'Traditional Shave',
    'Rasatura + Barba':    'Shave + Beard',
    'Taglio Psico-morfologico': 'Psico-morphological Cut',
    'Taglio Maury':        'Maury Signature Cut',
    'Taglio e Styling Uomo': "Men's Cut & Styling",
    'Taglio e Styling 13-18': '13-18 Cut & Styling',
    'Taglio Ragazzo 0-13 anni': 'Boys 0-13 Cut',
    'Taglio Donna':        'Ladies\' Cut',
    'Piega con Lavaggio':  'Shampoo & Blow-dry',
    'Piega Lunga con Lavaggio': 'Long Hair Shampoo & Blow-dry',
    'Anomalie Cutanee all\'Argilla': 'Clay-based Scalp Treatment',
    'Pulizia Cutanea Intensiva': 'Deep Scalp Cleansing',
    'Nutriente per le Lunghezze': 'Lengths Nourishing Treatment',
    'Colorazione con/senza Ammoniaca': 'Colour with/without Ammonia',
    'Tonalizzazione Lunghezze': 'Lengths Toning',
    'Lisciatura Cheratinica': 'Keratin Smoothing',
    'Sistema Ondulante':     'Perm / Waving System',
    'Schiariture':           'Lightening',
    'Sfumatura al Sole Balayage': 'Sun-kissed Balayage',
    'Onde Rame Colore':      'Copper Waves Colour',
    'Movimento Naturale Styling': 'Natural Movement Styling',
    'Rosso Intenso Colore':  'Intense Red Colour',
    'Biondo Luminoso Balayage': 'Luminous Blonde Balayage',
    'Raccolto Romantico Acconciatura': 'Romantic Updo Hairstyle',

    # LISTINO HEAD BUTTONS
    '<i class="fas fa-phone"></i> Chiamaci': '<i class="fas fa-phone"></i> Call Us',
    '<i class="fab fa-whatsapp"></i> WhatsApp · ': '<i class="fab fa-whatsapp"></i> WhatsApp · ',
    'Listino 2026 ufficiale MZ Parrucchieri · I prezzi possono variare in base a lunghezza e quantità · Per un preventivo preciso chiama la sede':
        'Official 2026 MZ Parrucchieri price list · Prices may vary based on length and quantity · For a precise quote please call the salon',

    # --- TEAM ---
    'Il nostro team': 'Our Team',
    'Team Villanova di Castenaso': 'Villanova di Castenaso Team',
    'A Villanova di Castenaso, vicino Bologna, troverete <strong>Alessandra, Cinzia, Rosa, Veronica e Gabriele</strong>, pronte ad accogliervi! Uno Staff di parrucchieri professionale grazie all\'esperienza acquisita negli anni.':
        'In Villanova di Castenaso, close to Bologna, you will meet <strong>Alessandra, Cinzia, Rosa, Veronica and Gabriele</strong>, ready to welcome you! A team of professional hairstylists with years of experience.',
    'Team Villafontana di Medicina': 'Villafontana di Medicina Team',
    'A Villafontana di Medicina, vicino Bologna, troverete <strong>Arianna, Claudia, Miriam, Samuele e Martina</strong>, pronte ad accogliervi! Uno Staff di parrucchieri professionale grazie all\'esperienza acquisita negli anni.':
        'In Villafontana di Medicina, close to Bologna, you will meet <strong>Arianna, Claudia, Miriam, Samuele and Martina</strong>, ready to welcome you! A team of professional hairstylists with years of experience.',
    'Team Imola': 'Imola Team',
    'A Imola troverete <strong>Carmine, Giorgia, Alex, Luigi e Gaia</strong>, pronte ad accogliervi! Uno Staff di parrucchieri professionale grazie all\'esperienza acquisita negli anni.':
        'In Imola you will meet <strong>Carmine, Giorgia, Alex, Luigi and Gaia</strong>, ready to welcome you! A team of professional hairstylists with years of experience.',
    'Team Barber Shop Medicina': 'Barber Shop Medicina Team',
    'Nel Barber Shop di Medicina troverete <strong>Gabriele, Mirco, Mattia e Luca</strong>, barbieri specializzati con anni di esperienza nel taglio uomo e nella cura della barba.':
        'In the Barber Shop Medicina you will meet <strong>Gabriele, Mirco, Mattia and Luca</strong>, specialised barbers with years of experience in men\'s cutting and beard care.',

    'Titolare · Fondatore': 'Owner · Founder',
    'Hairstylist Senior': 'Senior Hairstylist',
    'Senior Hairstylist': 'Senior Hairstylist',
    'Hairstylist': 'Hairstylist',
    'Receptionist': 'Receptionist',
    'Barbiere Senior': 'Senior Barber',
    'Junior Barber': 'Junior Barber',
    'Barbiere Junior': 'Junior Barber',

    # --- IL NOSTRO LAVORO / PORTFOLIO ---
    'Il nostro <span>Lavoro</span>': 'Our <span>Work</span>',
    'Il <span>nostro</span> lavoro': 'Our <span>Work</span>',
    'Collezione': 'Collection',
    'Esperienza': 'Experience',
    'Taglio di Precisione': 'Precision Cut',
    'Taglio': 'Cut',
    'Movimento Naturale': 'Natural Movement',
    'Styling': 'Styling',
    'Riflessi Dorati': 'Golden Highlights',
    'Colore': 'Colour',
    'Look Moderno': 'Modern Look',
    'Volume & Brillance': 'Volume & Shine',
    'Lunghezze Mosse': 'Wavy Lengths',
    'Acconciatura Sposa': 'Bridal Hairstyle',
    'Sposa': 'Bridal',
    'Backstage': 'Backstage',
    'Raccolto Elegante': 'Elegant Updo',
    'Acconciatura': 'Hairstyle',
    'Frangia & Movimento': 'Fringe & Movement',
    'Colore Intenso': 'Intense Colour',
    'Castagna Caldi': 'Warm Chestnut',
    'Onde Naturali': 'Natural Waves',
    'Biondo Baciato dal Sole': 'Sun-kissed Blonde',
    'L\'Arte del Colore': 'The Art of Colour',

    # --- PANORAMICA + VIRTUAL TOUR ---
    'Panoramica 360°': '360° Overview',
    'Guarda il Virtual Tour': 'Open the Virtual Tour',
    'Interno Salone Villanova MZ Experience': 'Villanova MZ Experience Salon Interior',

    # --- SEDI INFO + CONTATTI ---
    'Informazioni <span>sede</span>': '<span>Salon</span> Information',
    'Orari di oggi': 'Today\'s hours',
    'Ora aperti': 'Open now',
    'Chiuso': 'Closed',
    'Chiude alle': 'Closes at',
    'Riapre alle': 'Reopens at',
    'Orari': 'Opening Hours',
    'Lunedì': 'Monday',
    'Martedì': 'Tuesday',
    'Mercoledì': 'Wednesday',
    'Giovedì': 'Thursday',
    'Venerdì': 'Friday',
    'Sabato': 'Saturday',
    'Domenica': 'Sunday',
    'chiuso': 'closed',
    'Contatti': 'Contact',
    'Raggiungici': 'Get Directions',
    'Recensisci': 'Leave a Review',

    # --- SEDI HERO STRIP SULLA HOME ---
    'Villanova di Castenaso': 'Villanova di Castenaso',
    'Villafontana di Medicina': 'Villafontana di Medicina',
    'Via Cesare Battisti 6': 'Via Cesare Battisti 6',
    'Piazza G. Bersani 17': 'Piazza G. Bersani 17',
    'Piazza A. Gramsci 10': 'Piazza A. Gramsci 10',
    'Via O. Argentesi 22, Medicina': 'Via O. Argentesi 22, Medicina',
    'Orari Lun 10-18 · Mar-Ven 9-19:30 (Mer fino a 21) · Sab 8-18': 'Hours Mon 10-18 · Tue-Fri 9:00-19:30 (Wed until 21:00) · Sat 8:00-18:00',
    'Orari Apertura Lunedì: 10:00 - 18:00 Martedì: 09:00 - 19:30 Mercoledì: 09:00 - 21:00 Giovedì: 09:00 - 19:30 Venerdì: 09:00 - 19:30 Sabato: 08:00 - 18:00':
        'Opening Hours Monday: 10:00 - 18:00 Tuesday: 09:00 - 19:30 Wednesday: 09:00 - 21:00 Thursday: 09:00 - 19:30 Friday: 09:00 - 19:30 Saturday: 08:00 - 18:00',
    'Orari Mar-Ven 8:30-19:30 (Mer fino a 20:30) · Sab 8-18': 'Hours Tue-Fri 8:30-19:30 (Wed until 20:30) · Sat 8:00-18:00',
    'Orari Mar-Sab 9-18:30 (Mer fino a 20:30)': 'Hours Tue-Sat 9:00-18:30 (Wed until 20:30)',
    'Orari Mar-Ven 9:30-19:30 · Sab 9:00-18:00': 'Hours Tue-Fri 9:30-19:30 · Sat 9:00-18:00',
    'Dove Siamo Via Cesare Battisti 6, Villanova di Castenaso (BO)': 'Find Us Via Cesare Battisti 6, Villanova di Castenaso (BO)',
    'Contatti e Orari': 'Contact & Opening Hours',
    'trovarci': 'find us',
    'sede': 'salon',

    # --- CTA FINALE ---
    'Prenota il tuo appuntamento in <span>sede</span>': 'Book your appointment in <span>salon</span>',
    'Chiama o scrivici su WhatsApp: il nostro team di Villanova è pronto ad accoglierti.<br>Come & Visit Us in Via Cesare Battisti 6 o lascia una recensione se ti sei trovato bene con noi!':
        'Call or WhatsApp us: our Villanova team is ready to welcome you.<br>Come & Visit Us at Via Cesare Battisti 6 or leave a review if you enjoyed your experience with us!',
    'Chiama o scrivici su WhatsApp: il nostro team di Villafontana è pronto ad accoglierti.<br>Come & Visit Us in Piazza G. Bersani 17 o lascia una recensione se ti sei trovato bene con noi!':
        'Call or WhatsApp us: our Villafontana team is ready to welcome you.<br>Come & Visit Us at Piazza G. Bersani 17 or leave a review if you enjoyed your experience with us!',
    'Chiama o scrivici su WhatsApp: il nostro team di Imola è pronto ad accoglierti.<br>Come & Visit Us in Piazza A. Gramsci 10 o lascia una recensione se ti sei trovato bene con noi!':
        'Call or WhatsApp us: our Imola team is ready to welcome you.<br>Come & Visit Us at Piazza A. Gramsci 10 or leave a review if you enjoyed your experience with us!',
    'Chiama o scrivici su WhatsApp: il nostro team del Barber Shop è pronto ad accoglierti.<br>Come & Visit Us in Via O. Argentesi 22 o lascia una recensione se ti sei trovato bene con noi!':
        'Call or WhatsApp us: our Barber Shop team is ready to welcome you.<br>Come & Visit Us at Via O. Argentesi 22 or leave a review if you enjoyed your experience with us!',
    'Esperienza lusso, team, prodotti top e location esclusiva.': 'Luxury experience, team, premium products and exclusive location.',

    # --- SERVIZI CARD (sezioni SERVIZI EVOLUTI - per barber) ---
    'Taglio Classico · Ragazzo · Uomo': 'Classic Cut · Boys · Men',
    'Taglio & Barba': 'Cut & Beard',
    'Rasatura Tradizionale': 'Traditional Shave',
    'Servizi e Listino': 'Services & Price List',
    'Taglio, colore, styling, make up e trattamenti.': 'Cuts, colour, styling, make up and treatments.',
    'Taglio, colore, styling, make up e trattamenti.': 'Men\'s services, classic and modern cuts, beard and traditional shaves.',
    'Servizi e listino taglio, colore, styling, make up e trattamenti.': 'Services & price list cuts, colour, styling, make up and treatments.',
    'I servizi del salone': 'Salon Services',
    'Cosa rende questo salone speciale': 'What Makes This Salon Special',
    'Il Salone': 'The Salon',
    'Il Fondatore': 'The Founder',
    'Recensioni vere dei nostri clienti.': 'Genuine reviews from our customers.',
    'Dicono di noi': 'What They Say',
    'Nostro Team': 'Our Team',
    'Listino Servizi': 'Service Price List',
    'Scopri tutti i servizi': 'Discover all services',
    'Torna alla Home': 'Back to Home',
    'Artisti': 'Artists',
    'Lavoro': 'Work',
    'Portfolio': 'Portfolio',
    'appuntamento': 'appointment',
    'Riconoscimenti e Premi': 'Awards & Recognition',

    # --- FOOTER ---
    'Cookie Policy': 'Cookie Policy',
    'Privacy Policy': 'Privacy Policy',
    'Termini di servizio': 'Terms of Service',
    'Tutti i diritti riservati.': 'All rights reserved.',
    'P.IVA': 'VAT No.',
    'REA': 'Business Register',
    'Capitale Sociale': 'Share Capital',
    'Area riservata': 'Private Area',
    'Metodi di pagamento accettati': 'Accepted payment methods',
    'Seguici': 'Follow Us',

    # --- COOKIE BANNER ---
    'Questo sito utilizza solo cookie tecnici per garantirti la migliore esperienza di navigazione, nessun cookie di profilazione. Puoi accettare o rifiutare: la tua scelta sarà ricordata. Leggi la Cookie Policy':
        'This website only uses technical cookies to ensure you the best browsing experience, no profiling cookies. You can accept or refuse: your choice will be remembered. Read the Cookie Policy',
    'cookie tecnici': 'technical cookies',
    'Leggi la Cookie Policy': 'Read the Cookie Policy',
    'Accetta': 'Accept',
    'Rifiuta': 'Refuse',

    # --- RECENSIONI NELLE LANDING SE PRESENTI ---
    '4 .9 SU GOOGLE': '4.9 ON GOOGLE',
    '500 + RECENSIONI VERIFICATE': '500+ VERIFIED REVIEWS',
    'Le Voci dei Nostri Clienti': 'What Our Clients Say',

    # --- JSON-LD knowsAbout (SEO) ---
    '"Taglio capelli"': '"Haircuts"',
    '"Colore capelli"': '"Hair colour"',
    '"Colour capelli"': '"Hair colour"',
    '"Meches"': '"Highlights"',
    '"Pieghe"': '"Blow-dries"',
    '"Trattamenti Nashi Argan"': '"Nashi Argan Treatments"',
    '"Acconciature sposa"': '"Bridal hairstyling"',
    '"Make up professionale"': '"Professional make up"',

    # --- MENU MOBILE ---
    'Menu': 'Menu',

    # --- DOVE SIAMO EN SEZIONE ---
    'Dove Siamo | MZ Parrucchieri - 4 Saloni tra Bologna e Imola': 'Find Us | MZ Parrucchieri - 4 Salons between Bologna and Imola',
    'Trova il salone MZ Parrucchieri più vicino: Villanova di Castenaso, Villafontana di Medicina, Imola e Barber Shop Medicina. Orari, telefoni, WhatsApp e mappe Google.':
        'Find your nearest MZ Parrucchieri salon: Villanova di Castenaso, Villafontana di Medicina, Imola and Barber Shop Medicina. Opening hours, phone numbers, WhatsApp and Google maps.',
    'MZ Parrucchieri, Dove Siamo | MZ Parrucchieri - 4 Saloni tra Bologna e Imola':
        'MZ Parrucchieri, Find Us | MZ Parrucchieri - 4 Salons between Bologna and Imola',
    'Dove trovarci': 'Where to Find Us',
    'Quattro Sedi,': 'Four Locations,',
    'una sola': 'one',
    'eccellenza': 'excellence',
    'Villanova di Castenaso, Villafontana di Medicina, Imola e Barber Shop Medicina: quattro atelier MZ Parrucchieri tra Bologna e Imola, facilmente raggiungibili.':
        'Villanova di Castenaso, Villafontana di Medicina, Imola and Barber Shop Medicina: four MZ Parrucchieri ateliers between Bologna and Imola, all easy to reach.',
    'Le nostre sedi': 'Our Locations',
    'Scopri il salone': 'Discover the Salon',

    # ----- WHATSAPP CTA MESSAGES -----
    '?text=Ciao%2C%20vorrei%20prenotare%20al%20salone%20di%20Villafontana%20di%20Medicina':
        '?text=Hello%2C%20I%20would%20like%20to%20book%20at%20the%20Villafontana%20di%20Medicina%20salon',
    '?text=Ciao%2C%20vorrei%20prenotare%20al%20salone%20di%20Villanova%20di%20Castenaso':
        '?text=Hello%2C%20I%20would%20like%20to%20book%20at%20the%20Villanova%20di%20Castenaso%20salon',
    '?text=Ciao%2C%20vorrei%20prenotare%20al%20salone%20di%20Imola':
        '?text=Hello%2C%20I%20would%20like%20to%20book%20at%20the%20Imola%20salon',
    '?text=Ciao%2C%20vorrei%20prenotare%20al%20Barber%20Shop%20di%20Medicina':
        '?text=Hello%2C%20I%20would%20like%20to%20book%20at%20the%20Barber%20Shop%20Medicina',

    # ==== NUOVE TRADUZIONI RESIDUALI BARBER SHOP ====
    '<span>Scopri listino</span>': '<span>See price list</span>',
    'Tariffe aggiornate 2026': '2026 Updated rates',
    'Tutti i servizi del nostro Barber Shop: professionalità e prodotti Level 3':
        'All our Barber Shop services: expertise and Level 3 products',
    'Interno del MZ Barber Shop Medicina': 'Inside MZ Barber Shop Medicina',
    '<i class="fas fa-phone"></i> Prenota · 388 8604444': '<i class="fas fa-phone"></i> Book · 388 8604444',
    'Men\'s Cut Laterali': "Men's Sides & Back Cut",
    'Cut Ragazzo 14-18': 'Teens 14-18 Cut',
    'Cut Bimbo 0-13 anni': 'Boys 0-13 Cut',
    'Capelli': 'Hair',
    'Rifilatura Barba': 'Beard Trim',
    'Barba': 'Beard',
    'Listini 2026 ufficiali MZ Parrucchieri · I prezzi possono variare in base a lunghezza e quantità · Per un preventivo preciso chiama la sede':
        'Official 2026 MZ Parrucchieri price lists · Prices may vary based on length and quantity · For an accurate quote please call the salon',
    'Listini 2026 ufficiali MZ Parrucchieri · I prezzi possono variare in base a lunghezza e quantità · Per un preventivo preciso chiama la salon':
        'Official 2026 MZ Parrucchieri price lists · Prices may vary based on length and quantity · For an accurate quote please call the salon',
    'Le Pieghe di MZ': 'MZ Blow-dries',
    'Ogni piega include un trattamento scelto in base al tipo di capello e alle esigenze di stile: <em style="color:var(--gold);font-style:italic">Idratazione, Armonia, Colour, Volume, Energia, Filler, Blondy</em>.':
        'Each blow-dry includes a treatment chosen according to hair type and styling needs: <em style="color:var(--gold);font-style:italic">Hydration, Harmony, Colour, Volume, Energy, Filler, Blondy</em>.',
    'Trattamenti Extra': 'Extra Treatments',
    'I trattamenti per le anomalie cutanee vengono scelti tra: <em style="color:var(--gold);font-style:italic">Armonia, Armonia Plus, Energy</em>.':
        'Scalp-condition treatments are chosen from: <em style="color:var(--gold);font-style:italic">Harmony, Harmony Plus, Energy</em>.',
    'Le Forbici · Per Lei': 'The Scissors · For Her',
    'Le Forbici · Per Lui': 'The Scissors · For Him',
    'La Colorazione': 'Colour',
    'Con infusione di olii essenziali di Argan e lino biologico.':
        'With an infusion of essential oils of Argan and organic linseed.',
    'Forma': 'Shape',
    'Effetti Luce e Ombre': 'Light & Shade Effects',
    'Ottenute tramite prodotti che rispettano il capello.':
        'Achieved with hair-friendly products.',

    # Barbershop IT missing
    'I nostri barbieri': 'Our barbers',
    'Tre artigiani della cura maschile, sempre aggiornati sulle ultime tendenze':
        'Three male-grooming craftsmen, always up-to-date on the latest trends',
    'Il <span>Team</span>': 'The <span>Team</span>',
    'Tre artigiani della cura maschile, sempre aggiornati sulle ultime tendenze':
        'Three male-grooming craftsmen, always up-to-date on the latest trends',
    'Nel Barber Shop di Medicina troverai <strong>Gabriele, Daniele e Mirco</strong>, sempre pronti ad allinearsi alle nuove tendenze riguardanti la cura dell\'aspetto dell\'uomo. Barbe lunghe, barbe corte, curate con la massima attenzione e rasature rilassanti con impacchi di asciugamani caldi e freddi: un vero rituale per uomini, senza trascurare la cura del capello, dal taglio a macchinetta al classico pettine e forbici <em>old school</em>.':
        'In the Barber Shop Medicina you will find <strong>Gabriele, Daniele and Mirco</strong>, always ready to follow the latest trends in men\'s grooming. Long beards, short beards, meticulously groomed and relaxing shaves with hot and cold towel compresses: a true ritual for men, without neglecting hair care, from clipper cuts to the classic comb-and-scissors <em>old school</em> cut.',
    'Fade con riccio e barba — MZ Barber Shop': 'Curly fade with beard — MZ Barber Shop',
    'Hair tattoo con linee freestyle — MZ Barber Shop': 'Freestyle hair tattoo lines — MZ Barber Shop',
    'Taper fade classico — MZ Barber Shop': 'Classic taper fade — MZ Barber Shop',
    'Fade alto con ciuffo — MZ Barber Shop': 'High fade with fringe — MZ Barber Shop',
    'Riccio naturale maschile — MZ Barber Shop': 'Natural men\'s curls — MZ Barber Shop',
    'Cut biondo ghiaccio — MZ Barber Shop': 'Ice blonde cut — MZ Barber Shop',
    'Barbiere al lavoro con lo styling — MZ Barber Shop': 'Barber at work styling — MZ Barber Shop',
    'Cut pulito visto da dietro — MZ Barber Shop': 'Clean cut rear view — MZ Barber Shop',
    'Low fade con frangia — MZ Barber Shop': 'Low fade with fringe — MZ Barber Shop',
    'Rifinitura con rasoio a mano libera — MZ Barber Shop': 'Freehand razor finishing — MZ Barber Shop',
    'Cliente in poltrona dal barbiere — MZ Barber Shop': 'Client in the barber chair — MZ Barber Shop',
    'La reception del barber shop — MZ Barber Shop': 'The barber shop reception — MZ Barber Shop',
    'Collage Interno Barber Shop — foto principale': 'Barber Shop Interior Collage — main photo',
    'Angolo barber shop MZ — foto 1': 'MZ Barber Shop corner — photo 1',
    'Angolo barber shop MZ — foto 2': 'MZ Barber Shop corner — photo 2',
    'Angolo barber shop MZ — foto 3': 'MZ Barber Shop corner — photo 3',
    'Angolo barber shop MZ — foto 4': 'MZ Barber Shop corner — photo 4',
    'Foto precedente': 'Previous photo',
    'Foto successiva': 'Next photo',
    'Chiudi': 'Close',

    # ==== TRADUZIONI RESIDUALI DOVE SIAMO NAVBAR & HERO ====
    '<li><a class="" href="../chi-siamo/">Chi Siamo</a></li>':
        '<li><a class="" href="../index-en.html?skipintro=1#about-us">About Us</a></li>',
    '<li><a class="" href="../index.html?skipintro=1#servizi">Servizi</a></li>':
        '<li><a class="" href="../index-en.html?skipintro=1#services">Services</a></li>',
    '<li><a class="" href="../make-up/">Make Up</a></li>':
        '<li><a class="" href="../index-en.html?skipintro=1#make-up">Make Up</a></li>',
    '<li><a class="" href="../sposa/">Sposa</a></li>':
        '<li><a class="" href="../bridal/">Bridal</a></li>',
    '<li><a class="" href="../prodotti/">Prodotti</a></li>':
        '<li><a class="" href="../index-en.html?skipintro=1#products">Products</a></li>',
    '<li><a class="" href="../index.html?skipintro=1#galleria">Galleria</a></li>':
        '<li><a class="" href="../index-en.html?skipintro=1#gallery">Gallery</a></li>',
    '<li><a class="" href="../index.html?skipintro=1#contatti">Contatti</a></li>':
        '<li><a class="" href="../index-en.html?skipintro=1#contact">Contact</a></li>',

    'Le nostre <span>Sedi</span>': 'Our <span>Locations</span>',
    'Servizi e contenuti di <span>terze parti</span>': 'Services & <span>third-party</span> content',
    'Scopri il salone': 'Discover the Salon',
}

# ========== FUNCTIONS ==========
def translate(html, folder):
    """Applica traduzioni in ORDINE di grandezza decrescente per evitare sovrapposizioni."""
    # ordina per lunghezza stringa decrescente (sostituisce prima frasi lunghe)
    items = sorted(TRAD.items(), key=lambda kv: -len(kv[0]))
    for it, en in items:
        if it in html:
            html = html.replace(it, en)
    return html

def build_en(folder):
    """Da IT -> EN, copia pagina IT in index-en.html, traduce, setta pageSetLang."""
    it_file = os.path.join(APP, folder, "index.html")
    en_file = os.path.join(APP, folder, "index-en.html")
    with open(it_file, 'r', encoding='utf-8') as f:
        html = f.read()
    html = translate(html, folder)

    # Assicuriamoci che pageSetLang() sia in coda (se non c'è, lo aggiungiamo)
    script_salone = """
<script>
function pageSetLang(l) {
    try { localStorage.setItem('mz_lang', l); } catch(e) {}
    if (l === 'it') window.location.href = 'index.html';
    else if (l === 'en') window.location.href = 'index-en.html';
    else window.location.href = 'index.html';
}
</script>
"""
    if 'function pageSetLang(l)' not in html:
        html = html.replace("</body>", script_salone + "\n</body>")
    # Se c'è più di una funzione de-duplichiamo
    while html.count('function pageSetLang(l)') > 1:
        html = html.replace(script_salone, '', 1)

    with open(en_file, 'w', encoding='utf-8') as f:
        f.write(html)

def build_dovesiamo_en():
    it_file = os.path.join(APP, "dove-siamo", "index.html")
    en_file = os.path.join(APP, "dove-siamo", "index-en.html")
    with open(it_file, 'r', encoding='utf-8') as f:
        html = f.read()
    html = translate(html, "dove-siamo")

    # Correzioni specifiche dove-siamo EN navbar
    html = html.replace(
        '<li><a href="../dove-siamo/" class="active">Dove siamo</a></li>',
        '<li><a href="../dove-siamo/index-en.html" class="active">Find Us</a></li>'
    )
    html = html.replace(
        '<li><a href="../sposa/">Sposa</a></li>',
        '<li><a href="../bridal/">Bridal</a></li>'
    )
    html = html.replace(
        '<a class="nav-cta" style="text-decoration:none" href="../index.html?skipintro=1#contatti"><i class="far fa-calendar-check"></i>Prenota</a>',
        '<a class="nav-cta" style="text-decoration:none" href="../index-en.html?skipintro=1#contact"><i class="far fa-calendar-check"></i>Book Now</a>'
    )
    # canonical + hreflang
    html = html.replace(
        '<link rel="canonical" href="https://www.mzparrucchieri.it/dove-siamo/">',
        '<link rel="canonical" href="https://www.mzparrucchieri.it/dove-siamo/index-en.html">'
    )
    # pageSetLang in EN -> toggle index.html / index-en.html LOCAL
    MAP_OLD = '''    var MAP = {
                "en": "./index-en.html",
                "it": "./index.html"
};'''
    MAP_NEW = MAP_OLD  # già OK dal translate (dove-siamo IT è già convertito con questa mappa)
    html = html.replace(
        '<meta property="og:locale" content="it_IT">',
        '<meta property="og:locale" content="en_US">'
    )
    # Forza pulsante EN come active (dove-siamo EN)
    html = html.replace(
        '                <button class="lang-btn active" onclick="pageSetLang(\'it\')">IT</button>\n                <button class="lang-btn " onclick="pageSetLang(\'en\')">EN</button>',
        '                <button class="lang-btn" onclick="pageSetLang(\'it\')">IT</button>\n                <button class="lang-btn active" onclick="pageSetLang(\'en\')">EN</button>'
    )
    # Sostituisci cur_lang = 'it' con cur_lang = 'en' nel blocco IIFE (per dove-siamo EN)
    # - il blocco pageSetLang nella pagina dove-siamo usa MAP locale e un IIFE che controlla la lingua salvata
    html = html.replace(
        "var cur_lang = 'it';\n        if (saved !== cur_lang && MAP[saved]) {\n            // Utente ha lingua diversa salvata: vai alla versione corretta o home equivalente\n            window.location.replace(MAP[saved]);",
        "var cur_lang = 'en';\n        if (saved !== cur_lang && MAP[saved]) {\n            // Utente ha lingua diversa salvata: vai alla versione corretta o home equivalente\n            window.location.replace(MAP[saved]);"
    )
    # Rimuovi ogni duplicato di pageSetLang
    while html.count('function pageSetLang(l)') > 1:
        start = html.find('function pageSetLang(l)')
        end = html.find('</script>', start)
        block = html[start : end + len('</script>')]
        html = html.replace('\n' + block, '', 1)
    with open(en_file, 'w', encoding='utf-8') as f:
        f.write(html)

# ========= ESECUZIONE ==========
for folder in [
    "salone-villanova-castenaso",
    "salone-villafontana-medicina",
    "salone-imola",
    "barber-shop",
]:
    build_en(folder)
    print(f"✅ RE-GENERATED  {folder}/index-en.html")

build_dovesiamo_en()
print("✅ RE-GENERATED  dove-siamo/index-en.html")
