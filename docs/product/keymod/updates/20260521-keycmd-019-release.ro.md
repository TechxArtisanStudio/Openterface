---
draft: false
date: 2026-05-21
title: "KeyCmd 0.19: Rebranding aplicație, mod Compose KM Pro, suport multilingv și ghiduri interactive pe moduri"
description: "KeyCmd 0.19 aduce un rebranding major de la KeyMod la KeyCmd, noul mod Compose KM Pro cu trimitere HID compatibilă Unicode, interfață multilingvă (coreeană, italiană, rusă, portugheză), ghiduri interactive pe moduri și zeci de îmbunătățiri UX."
keywords: "KeyCmd 0.19, lansare KeyCmd, rebranding aplicație, mod Compose, trimitere HID Unicode, multilingv, ghiduri interactive, actualizare Openterface KeyCmd, emulator HID, tastatură virtuală, aplicație tastatură Android"
author: "TechxArtisan Studio"
category: "Product Updates"
tags: ["KeyCmd", "Product Updates", "Release", "Compose", "i18n", "Android"]
featured: false
social:
  image: "https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp"
  title: "Lansarea KeyCmd 0.19 — Mod Compose, rebranding, multilingv, ghiduri interactive"
  description: "KeyCmd 0.19 aduce noul mod Compose, rebranding în KeyCmd, 4 limbi noi, ghiduri interactive și îmbunătățiri UX semnificative."
---

# KeyCmd 0.19: Rebranding aplicație, mod Compose KM Pro, suport multilingv și ghiduri interactive pe moduri

KeyCmd **0.19** (`versionCode` **19**) este o actualizare majoră care aduce **rebranding-ul** de la KeyMod la KeyCmd, noul **mod Compose din KM Pro** cu trimitere HID compatibilă Unicode, o **interfață multilingvă extinsă** (incluzând coreeană, italiană, rusă și portugheză braziliană), **ghiduri interactive pe moduri** și zeci de îmbunătățiri UX în modurile tastatură, gamepad și prezentare.

## Rebranding aplicație: KeyMod → KeyCmd

Numele afișat al aplicației este acum **KeyCmd** în toate punctele de intrare. Acest rebranding clarifică distincția între **hardware-ul KeyMod** și **aplicația companion KeyCmd**.

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp" alt="Ecran de bun venire KeyCmd" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">

### Ce s-a schimbat

- **Numele afișat al aplicației**: Iconița din launcher și interfața de sistem afișează acum „KeyCmd"
- **Fluxul de bun venire**: Wordmark și text actualizate de la KeyMod la KeyCmd
- **Artefacte CI și nume fișiere APK**: Folosesc prefixul **KeyCmd**
- `applicationId` rămâne **`com.openterface.keymod`** pentru upgrade-uri locale fără întreruperi

Utilizatori existenți: setările, profilele și dispozitivele asociate sunt păstrate. Upgrade-ul este transparent.

## Tastatură și mouse: experiență full screen

KeyCmd oferă o experiență full screen de tastatură, touchpad și numeric pad — optimizată pentru orientările portret și peisaj.

<div class="slideshow-container" id="slideshow-keycmd-019-kbm-ro" data-auto-slide="true" data-auto-slide-interval="3000">
  <div class="slideshow-wrapper">
    <div class="slide active">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Full-Keyboard-landscape.webp" alt="Tastatură peisaj full screen" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape.webp" alt="Numeric pad peisaj" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-portrait.webp" alt="Numeric pad portret" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait.webp" alt="Tastatură și touchpad portret" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-km-basic-Touchpad.webp" alt="Touchpad peisaj" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Remote-Coding-portrait.webp" alt="Programare la distanță cu KeyCmd" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Settings-screen.webp" alt="Ecran setări KeyCmd" style="max-height:320px;" loading="lazy">
    </div>
  </div>

  <div class="slideshow-navigation">
    <button class="nav-arrow left" onclick="changeSlide('slideshow-keycmd-019-kbm-ro', -1)">❮</button>
    <div class="slideshow-dots">
      <span class="dot active" onclick="currentSlide('slideshow-keycmd-019-kbm-ro', 1)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ro', 2)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ro', 3)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ro', 4)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ro', 5)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ro', 6)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ro', 7)"></span>
    </div>
    <button class="nav-arrow right" onclick="changeSlide('slideshow-keycmd-019-kbm-ro', 1)">❯</button>
  </div>
</div>

## KM Pro: mod Compose & Send

Cea mai mare noutate din versiunea 0.19 este **modul Compose** din KM Pro — un editor de text dedicat care îți permite să introduci pasaje lungi și să le trimiți ca apăsări de taste HID către mașina țintă.

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait.webp" alt="Executare script în modul Compose" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">

<p><strong>Compose &amp; Send demo (YouTube Short)</strong></p>

<iframe width="560" height="315" loading="lazy" src="https://www.youtube.com/embed/_rJF-hTF3_E" title="KeyCmd Compose &amp; Send demo (YouTube Short)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


### Editor Compose

- **Bara de sus pentru scurtături + rândul de acțiuni de compunere** cu controale **Șterge** și **Anulare/Șterge**
- **Păstrarea ciornelor**: textul tău este păstrat la comutarea submodurilor și chiar după o trimitere reușită
- **Integrare IME**: tastează cu tastatura telefonului, trimite ca apăsări HID curate
- **Progres de trimitere determinist**: o bară de progres vizibilă pentru bufferele HID lungi, astfel încât să știi exact cât a fost trimis

### Trimitere HID compatibilă Unicode

- **Revizuire risc dual-mod**: înainte de a trimite text non-ASCII, un dialog avertizează despre compatibilitatea Unicode și oferă acțiuni de inspectare și previzualizare
- **Flux hexadecimal Unicode macOS**: pe host-urile macOS, aplicația folosește metoda de introducere Option+cod hexazecimal pentru caracterele extinse
- **Dialoguri de trimitere mai sigure**: ecranul de revizuire își adaptează conținutul în funcție de buffer-ul ASCII pur sau care conține caractere Unicode
- **Instrumente de inspectare caractere**: dialogul de risc de trimitere oferă acțiuni **Verifică** și **Previzualizare**, iar host-urile macOS includ o intrare dedicată de **audit cale hexazecimal Unicode**

### Domeniul KM Basic

În versiunea 0.19, **Compose & Send rămâne o funcție a Tastaturii și Mouse-ului Pro**. KM Basic se concentrează pe fluxurile de lucru ale tastaturii full screen, touchpad și numeric pad.

## Suport multilingv

KeyCmd suportă acum **11 limbi ale interfeței aplicației**. Această lansare adaugă patru noi localizări:

- **Coreeană (ko)**: traducere completă a interfeței
- **Italiană (it)**: traducere completă a interfeței
- **Rusă (ru)**: traducere completă a interfeței
- **Portugheză braziliană (pt-BR)**: traducere completă a interfeței

Împreună cu engleza, chineza simplificată, chineza tradițională, japoneza, franceza, germana și spaniola existente, KeyCmd acoperă acum majoritatea covârșitoare a bazei noastre globale de utilizatori.

### Ce s-a schimbat

- **Selector de limbă** în Setări cu nume canonice ale limbilor aplicației
- **Antete Bluetooth** și **previzualizare atingere tastă** localizate
- **Corecturi lint de lansare** pentru filele de avertisment de compunere din toate limbile

## Ghiduri interactive pe moduri

Fiecare mod are acum un **ghid interactiv integrat** care te conduce pas cu pas prin funcționalitățile sale.

### Ghiduri disponibile

- **Ghid Shortcut Hub**: deschide profilul implicit și acoperă interfața de detalii, filele de categorii și gestionarea scurtăturilor
- **Ghid Gamepad**: explică aspectul gamepad-ului, gestionarea modulelor și sistemul de presetări
- **Ghid KM Pro**: acoperă modul Compose, panoul de scurtături și funcțiile specifice Pro
- **Ghid KM Basic**: explică tastatura full screen, gestul de glisare cu modificator ținut și numeric pad

### Funcții ghiduri

- **Ghiduri pe mod**: fiecare mod are propriul ghid personalizat
- **Foaie de reluare**: revizitează orice ghid oricând prin butonul **Ghid mod** (iconița din stânga secțiunii de conexiune)
- **Suport i18n**: conținutul ghidurilor este localizat în toate limbile aplicației
- **Optimizat peisaj**: layout-urile bottom sheet se adaptează corect în orientarea peisaj

## Îmbunătățiri UX

### Tastatură

- **Previzualizare atingere tastă**: vezi exact ce va fi trimis înainte de a atinge. Activabil din Setări. Activat implicit.
- **Corectare HID atingere rapidă**: îmbunătățirea timpului de eliberare a atingerilor și evenimente de eliberare consolidate pentru tastare mai rapidă
- **Gestionare atingere caractere alternative**: apăsarea lungă a tastei `a` afișează acum alternativele ¥ (sus), £ (stânga), € (dreapta) cu feedback vizual îmbunătățit
- **Gest glisare cu modificator ținut**: în ghidurile KM Basic/Pro, un nou pas învață gestul de glisare cu modificator ținut pentru acces rapid la modificatori

### Gamepad

- **Bara de sesiune de editare eliminată**: interfață gamepad mai curată fără vechea bară de instrumente a sesiunii de editare
- **Interfață și ghid gamepad**: nou polish vizual și ghid interactiv integrat
- **Iconiță ghid mod**: plasată în stânga secțiunii de conexiune pentru acces ușor

### Prezentare

- **Blocare pereche portret**: modul Prezentare este limitat la orientările portret și portret inversat pentru control stabil al prezentatorului

### Interfață și temă

- **Specimen de accent**: înlocuit selectorul de familie de culori al temei cu specimen vizuale de accent pentru selecție mai ușoară a culorilor
- **Aliniere accente UI**: toate accentele UI urmăresc acum familia de culori a temei (nu culoarea primară moștenită)
- **Cluster dreapta antet**: dimensiuni îmbunătățite pentru iconițele de conexiune atât în aplicația principală, cât și în interfața KM Basic
- **Stil buton trimitere Compose**: aspectul butonului de trimitere non-ASCII aliniat în modul luminos

### Setări

- **Reorganizare setări**: nume canonice ale limbilor; scripturi de instalare emulator redenumite pentru claritate
- **Scripturi ajutor dezvoltator**: redenumite pentru identificare mai clară a dispozitivelor și numirea acțiunilor
- **Documentație FAQ**: `docs/FAQ.md` actualizat cu comportamentul actual al aplicației

## Cazuri de utilizare reale

### Programare la distanță

KeyCmd nu este doar pentru gestionarea serverelor. Dezvoltatorii îl folosesc pentru **sesiuni de programare la distanță** — controlul unei mașini de development headless de pe telefon sau tabletă, cu suport complet de tastatură, touchpad și numeric pad.

## Ce nu s-a schimbat

**Tastatură și Mouse Pro** (mod compozit cu bare Shortcut Hub, layout-uri împărțite și comportament IME bogat) rămâne experiența completă de dinainte. Toate profilele, presetările și dispozitivele asociate existente sunt păstrate.

## Obținerea actualizării

**Această versiune (0.19):** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

> **Notă Beta:** Aplicația Android KeyCmd este încă în fază Beta activă. Repository-ul sursă nu este încă public — planificăm să-l facem open source după o campanie de crowdfunding de succes. Dacă ești un tester Beta și ai nevoie de cel mai recent APK, contactează-ne pe Discord și îți vom trimite build-ul.

Instalările existente pot fi actualizate local.

## Compatibil cu Mini-KVM și KVM-Go

Aplicația KeyCmd nu se limitează la hardware-ul KeyMod. Utilizatorii existenți Openterface pot de asemenea să o încerce:

- **KVM-Go**: conexiune prin **Bluetooth** sau **USB**
- **Mini-KVM**: conexiune prin **USB**

## Note de upgrade

- **Rebranding**: numele aplicației se schimbă de la KeyMod la KeyCmd. Datele tale sunt păstrate.
- **Mod Compose**: nou pentru Tastatură și Mouse Pro.
- **Ghiduri interactive**: atinge iconița ghidului (în stânga secțiunii de conexiune) în orice mod pentru a porni ghidul interactiv.
- **Limbi**: mergi la Setări pentru a schimba limba aplicației. KeyCmd suportă acum 11 limbi ale interfeței aplicației.

Cu stimă,

Openterface Team | TechxArtisan
