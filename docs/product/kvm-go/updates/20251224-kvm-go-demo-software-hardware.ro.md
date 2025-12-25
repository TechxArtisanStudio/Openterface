---
draft: false
date: 2025-12-24
title: "Nouă demonstrație video, progres software și ce se află în interiorul KVM-GO"
description: "Vizualizați noua demonstrație video pentru KVM-GO care arată versiunile HDMI/DP/VGA în acțiune. Aflați despre software unificat pentru Mini-KVM și KVM-GO, actualizări hardware inclusiv procesor video MS2130S 4K@60Hz și MCU CH32V208, plus funcții viitoare precum suportul personalizat EDID. Actualizare campanie: $72k cu peste 220 de susținători."
keywords: "demonstrație video KVM-GO, actualizare software KVM-GO, upgrade hardware KVM-GO, procesor video MS2130S, MCU CH32V208, KVM 4K@60Hz, KVM-GO vs Mini-KVM, aplicație unificată Openterface, performanță tastatură și mouse KVM-GO, suport EDID personalizat, control script KVM-GO, certificare OSHWA, crowdfunding KVM-GO, Crowd Supply KVM-GO, Openterface KVM-GO, TechxArtisan, comparație hardware KVM-over-USB"
author: "TechxArtisan Studio"
category: "Actualizări produs"
tags: ["KVM-GO", "Actualizări produs", "Software", "Hardware", "Demonstrație video", "Crowdfunding", "Dive tehnic"]
featured: true
social:
  image: "https://assets.openterface.com/images/blog/Gemini_Generated_Image_kvm-go.webp"
  title: "Nouă demonstrație video, progres software și ce se află în interiorul KVM-GO"
  description: "Vizualizați KVM-GO în acțiune, aflați despre actualizări software unificate și descoperiți upgrade-urile hardware care alimentează dispozitivul nostru KVM-over-USB de ultimă generație."
---

# Nouă demonstrație video, progres software și ce se află în interiorul KVM-GO

Salut toți! Îmi pare rău pentru perioada liniștită. Am fost concentrat asupra polisajului atât hardware, cât și software pentru [KVM-GO](https://openterface.com/product/kvm-go/), iar timpul a trecut repede. Până la sfârșitul decembrie, am atins **$72k cu peste 220 de susținători**, ceea ce este minunat. Dacă poți să ne ajuti să mergem mai departe, te rog **răspândește cuvântul**!

Mulțumesc foarte mult pentru răbdare și sprijin. Da, Crăciunul a adăugat cu siguranță haosul 🙂🎄 Acum, să ne actualizăm.

![blog-Gemini_Generated_Image_kvm-go](https://assets.openterface.com/images/blog/Gemini_Generated_Image_kvm-go.webp)
*Imagine generată cu Nano Banana, bazată pe fotografii reale ale produselor noastre KVM-GO.*

## Nouă demonstrație video: KVM-GO în acțiune

Am publicat recent o [**nouă demonstrație video**](https://www.youtube.com/watch?v=459rWCQbJRE) care arată KVM-GO în utilizare reală.


În videoclip vei vedea:

* Versiunile KVM-GO **HDMI / DP / VGA** în acțiune
* Ce este inclus **în cutie**
* Cum se controlează diferite dispozitive țintă
* Cum KVM-GO se încadrează în fluxuri de lucru reale, de la acces rapid la setări pentru mai multe dispozitive țintă

Dacă ești curios despre testare mai puțin formală, hands-on și utilizare reală, poți verifica și [rețeaua socială](https://openterface.com/about/community/). Adesea împărtășim clipuri brute de testare și scenarii practice care arată cum se comportă KVM-GO pe frontul tehnologic real.

## Progres software: O aplicație pentru Mini-KVM și KVM-GO

Pe partea soft, am făcut un pas solid înainte.

Actualizările noastre cele mai recente permit ca **aceeași aplicație Openterface să funcționeze fără probleme cu atât Mini-KVM, cât și seria KVM-GO**. Pentru utilizatori, asta înseamnă:

* O experiență coerentă între produse
* Mai puțină fragmentare dacă folosești mai multe dispozitive Openterface

Am dedicat timp și îmbunătățirii **performanței tastaturii și mouse-ului**, cu accent pe:

* Latență mai mică în total
* Gestionare mai stabilă a intrărilor, inclusiv detectarea mai bună a stării de conexiune și calitatea semnalului
* Răspuns mai rapid în interacțiuni rapide sau continue

Deși gaming nu este utilizarea principală a soluțiilor noastre KVM, tot ne preocupăm profund de responsivitatea intrărilor în scenarii reale. Dacă ești interesat de detaliile tehnice, în special pe macOS, am publicat recent o analiză profundă aici:
👉 **[Viteza mouse-ului și performanța gaming pentru Openterface Mini-KVM pe macOS](https://openterface.com/app/updates/20251218-macos-mouse-speed/)**

Multe dintre îmbunătărțirile discutate acolo sunt acum integrate direct în stiva noastră de software unificat pentru atât Mini-KVM, cât și KVM-GO.

## Upgrade-uri hardware esențiale în KVM-GO (comparativ cu Mini-KVM)

Pentru cei interesați de detaliile interne, iată o comparație rapidă a principalelor modificări hardware de la Mini-KVM la KVM-GO.

### Upgrade-uri în pipeline-ul video

| Aspect           | **MS2109 (Mini-KVM)**    | **MS2130S (KVM-GO)** | Îmbunătățire           |
| ---------------- | ------------------------ | -------------------- | --------------------- |
| Intrare HDMI     | 4K @ 30Hz                | 4K @ 60Hz            | Bandwidth de intrare dublu    |
| Ieșire video USB | 1080p @ 30Hz             | 4K @ 60Hz            | 4× throughput de pixeli   |
| Scalare internă  | 4K → 1080p               | 4K nativ             | Nici o scalare forțată |
| Latență de cadru | Mai mare (scaler + buffer) | Mai mică (cale directă)  | Latență redusă       |

### Upgrade-uri în emularea tastaturii și mouse-ului USB

| Aspect             | **CH340 + CH9329 (Mini-KVM)** | **CH32V208 (KVM-GO)** | Îmbunătățire     |
| ------------------ | ----------------------------- | --------------------- | --------------- |
| Număr de chipuri   | 2 chipuri                     | Un singur MCU         | Sistem mai simplu |
| Gestionare USB     | Pontaj USB–Serial             | Dispozitiv USB nativ   | Latență mai mică |
| Generare HID       | Funcție fixă                  | Definită prin firmware | Control complet   |
| Cale de date       | USB → UART → HID              | USB → HID             | Eliminat un salt |
| Compatibilitate BIOS | Amestecată                   | Excelentă             | Mai fiabilă     |

## Funcții avansate în dezvoltare activă

Sunt planificate mai multe funcții avansate și sunt în dezvoltare activă pentru firmware-ul finalizat KVM-GO. O privire rapidă:

* **Suport pentru EDID personalizat** pentru rezolvarea problemelor de compatibilitate a afișajului
* **Control bazat pe script** pentru automatizare și fluxuri de lucru avansate

Vom împărtăși mai multe detalii odată ce aceste funcții vor fi finalizate.

## Angajament Open-Source (așa cum întotdeauna)

Da, **KVM-GO va rămâne complet open-source**.

Odată ce proiectul hardware este finalizat pentru producția în masă, vom aplica pentru **certificare OSHWA (Asociația Hardware Open Source)**.

Toate fișierele de proiect hardware și modelele STL vor fi publicate aici:
👉 [https://github.com/TechxArtisanStudio/Openterface_KVM-GO_Hardware](https://github.com/TechxArtisanStudio/Openter:
[https://www.crowdsupply.com/techxartisan/openterface-kvm-go](https://www.crowdsupply.com/techxartisan/openterface-kvm-go)

Vă mulțumim din nou pentru răbdare, încredere și sprijin. Mai multe actualizări vor veni curând, iar vom încerca să nu mai rămânem tăcute. Speranțe de Crăciun calde din partea tuturor noastră!

**Echipa Openterface | TechxArtisan**