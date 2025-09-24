---
title: "Funcționalități și specificații"
description: "Prezentare completă a Openterface KVM Extension for uConsole: funcționalități puternice incluzând intrare HDMI directă, control USB HID, factor de formă perfect și specificații tehnice detaliate. Tot ce trebuie să știi despre această soluție KVM portabilă."
keywords: "funcționalități extensie KVM, uConsole KVM, HDMI KVM, control USB HID, KVM portabil, control headless, înlocuire 4G LTE, specificații tehnice, expansiune uConsole"
---

# **Funcționalități și specificații** | Openterface KVM Extension for uConsole

![PCB-front](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:320px"}
![PCB-Back](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:320px"}

## Funcționalități principale

- **HDMI direct + USB HID**: Folosește ecranul și controalele integrate ale uConsole cu intrare HDMI directă și emulare USB HID.
- **Plug-and-Play**: Control instantaneu fără instalare software sau urme reziduale pe dispozitivul țintă.
- **Latență mică**: Optimizat pentru depanare la nivel BIOS și interacțiuni în timp real.
- **Portabil**: Instrument mobil all-in-one—nu ai nevoie de monitoare suplimentare, tastaturi sau configurare de rețea.
- **Fără rețea**: Control headless stabil prin captură HDMI și intrare HID, nicio rețea necesară.
- **Transfer de text**: Transferă rapid text prin simularea apăsărilor de taste—ideal pentru nume de utilizator, parole și fragmente de cod. Suportă ASCII complet, incluzând simboluri și punctuație. [Verifică aplicația noastră](/app) pentru detalii.
- **Open Source**: Construit pe [Openterface KVM QT](https://github.com/techxArtisanStudio/openterface_qt) cu suport activ al comunității.

## Specificații tehnice

### Dimensiuni fizice

- **Mărime:** 37 × 77 mm (se potrivește cu modulul 4G/LTE)
- **Grosime:** 1,0 mm (mai subțire decât modulul 4G/LTE original de 1,2 mm)
- **Material:** PCB de înaltă calitate cu contacte cu arc

### Emulare completă tastatură și mouse

- **USB HID:** Poziționare absolută și relativă a mouse-ului, suport complet tastatură, taste multimedia.
- **Conexiune:** Legătură USB către țintă prin portul femelă Type-C al plăcii de extensie.

### Video și audio

- **Intrare:** Până la 4K (3840×2160) @ 30Hz prin HDMI
- **Ieșire:** Full HD (1920×1080) @ 30Hz cu latență sub 140ms
- **Display:** Folosește ecranul integrat al uConsole
- **Compresie:** Suport YUV și MJPEG
- **Compatibilitate:** VGA, DVI, Micro HDMI (prin adaptoare)
- **Audio:** Passthrough audio încorporat HDMI

### Port USB 2.0 comutabil

- **Port partajat:** Comută ușor accesul USB între uConsole și dispozitivul țintă (ex. unități flash) folosind aplicația gazdă.
- **Viteza USB:** Transmisie la viteză completă de 12Mbps

### Conectivitate și alimentare

- **Alimentare:** Obține energie direct din slotul de expansiune al uConsole (nicio sursă externă necesară)
- **Compatibilitate țintă:** Windows, macOS, Linux, Android, iOS
- **Software țintă:** Nicio instalare necesară
