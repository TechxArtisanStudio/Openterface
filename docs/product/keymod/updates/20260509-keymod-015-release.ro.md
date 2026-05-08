---
draft: false
date: 2026-05-09
title: "KeyMod 0.15: Pipeline preset gamepad, Tastatură și mouse (Basic), Layout-uri multi-touchpad"
description: "KeyMod 0.15 aduce pipeline-ul de presetări gamepad cu schema v7, layout-uri multi-touchpad, nivelul Tastatură și mouse (Basic) cu tastatură pe tot ecranul și branding KeyMod în întreaga aplicație. Un pas important către o experiență de input rafinată."
keywords: "KeyMod 0.15, KeyMod lansare, preset gamepad, multi-touchpad, tastatură mouse basic, branding KeyMod, Openterface KeyMod actualizare, emulator HID, gamepad virtual, aplicație tastatură Android"
author: "TechxArtisan Studio"
category: "Actualizări produs"
tags: ["KeyMod", "Actualizări produs", "Lansare", "Gamepad", "Tastatură", "Android"]
featured: false
social:
  image: "https://assets.openterface.com/images/keymod/keymod-015-release.jpg"
  title: "KeyMod 0.15 lansare — presetări gamepad, nivel basic, multi-touchpad"
  description: "KeyMod 0.15 aduce pipeline-ul de presetări gamepad v7, un nivel dedicat Tastatură și mouse (Basic), layout-uri multi-touchpad și noul branding KeyMod."
---

# KeyMod 0.15: Pipeline preset gamepad, Tastatură și mouse (Basic), Layout-uri multi-touchpad

KeyMod **0.15** (`versionCode` **15**) este o versiune reper care aduce trei funcționalități majore: **pipeline-ul de presetări gamepad** cu schema de layout **v6-v7**, nivelul dedicat **Tastatură și mouse (Basic)** și layout-urile **multi-touchpad**. Această actualizare aduce, de asemenea, branding-ul **KeyMod** complet în fluxul de bun venit și în artefactele de build.

## Gamepad: Pipeline preset v7

Gamepad-ul folosește acum un **sistem de presetări** care îți permite să salvezi, încarci, imporți și exportezi layout-uri de controller personalizate.

### Ce s-a schimbat

- **Preset store v7** înlocuiește layout-urile integrate anterioare. Presetările de fabrică clasice (`preset_classic_*`) și **Two buttons** (`preset_two_buttons`) au fost eliminate de pe disc. Doar **`preset_default`** rămâne ca layout de fabrică protejat la ștergere.
- **Schema v7** face ca **`stick_left`** să fie opțional. Un layout poate acum să nu aibă niciun modul de deget mare stânga. Meniul **Add module** inserează **`stick_left`**, **`stick_left_2`**, **`stick_left_3`**, etc.
- **Suport multi-touchpad**: presetările pot include mai multe touchpad-uri (`touchpad_1`, `touchpad_2`). Adăugarea unui touchpad alocă următorul id disponibil cu o ancoră ușor deplasată. Butoanele mouse-ului L/M/R incluse sunt partajate între toate touchpad-urile.
- **Dimensiunea butoanelor mouse-ului de pe touchpad**: butoanele mouse-ului folosesc acum un rază de desen implicită mai mare. Poți ajusta dimensiunea prin apăsare lungă **Mouse button size** pe touchpad sau **This button size** pe module individuale de mouse.
- **Valori implicite stick auxiliar**: **`stick_left_2+`** implicit pe cruce D-pad + mapare WASD.

### Gestionarea presetărilor

- **Atinge** chipul Preset din bara de instrumente pentru a parcurge layout-urile disponibile
- **Apăsare lungă** pentru lista completă de presetări cu opțiuni de import, adăugare modul și export
- Layout-ul **emu-6** inclus servește ca presetare de start
- Creatorul de export suportă i18n pentru partajarea presetărilor între limbi

## Tastatură și mouse (Basic)

Un nivel dedicat de tastatură pe tot ecranul, conceput pentru tastare concentrată fără antetul aplicației.

### Ce primești

- **Tastatură pe tot ecranul** fără antetul principal al aplicației pentru mai mult spațiu pe ecran
- **Numpad portret și landscape**: grilă 5x8 în portret (PrtSc / ScrLk / Pause / Home / End), grilă 8x5 în landscape cu + înalt, Enter și 00
- **Poartă de trimitere ASCII-only IME**: tastează text lung în modul compose, trimite ca apăsări HID curate
- **Repetare prin apăsare lungă**: ține apăsate tastele caracter/funcție pentru repetare automată (~400ms întârziere, ~50ms repetare)
- **Previzualizare tastă**: bula flotantă afișează eticheta efectivă deasupra tastei apăsate
- **Feedback haptic** și suprafețe de taste cu **temă adaptivă**

### Modificatori Sticky vs Chord

Setările îți permit să alegi între **modificatori sticky** (atingere pentru blocare) și **momentan + chord cu apăsare lungă** (implicit) pentru tastatura Basic.

## Branding

- Numele de afișare al aplicației este acum **KeyMod**
- Ecranul de bun venit afișează logotipul **KeyMod**
- Artefactele CI și numele fișierelor APK folosesc prefixul **KeyMod**
- `applicationId` rămâne **`com.openterface.keymod`** pentru actualizări in-place

## Ce rămâne neschimbat

**Tastatură și mouse Pro** (mod compozit cu benzi Shortcut Hub, layout-uri divizate și comportament IME bogat) rămâne experiența completă de până acum.

## Obținerea actualizării

**Această versiune (0.15):** [KeyMod-release-0.15.apk](https://assets2.openterface.com/data/KeyMod-release-0.15.apk)

> **Notă beta:** Aplicația KeyMod pentru Android este încă în fază beta activă. Repo-ul nu este încă public — plănuim să-l facem open source după o campanie crowdfunding de succes. Dacă ești beta tester și ai nevoie de cel mai recent APK, contactează-ne pe Discord și îți trimitem build-ul.

> **Probleme cunoscute:** Această versiune introduce modificări semnificative în sistemul de presetări gamepad și nivelul de tastatură Basic. Echipa noastră de dev încă testează intern, așa că poți întâlni bug-uri. Dacă întâlnești ceva neașteptat, raportează-l pe Discord — feedback-ul tău ne ajută să stabilizăm mai repede.

Instalările existente se actualizează in-place.

## Note de actualizare

- **Gamepad**: preferința ta anterioară de două butoane activează automat presetarea **Two buttons** la prima lansare. Folosește **Preset** (atinge pentru a parcurge, apăsare lungă pentru listă) în locul vechiului control 1 Button / 2 Buttons.
- **Tastatură și mouse (Basic)**: deschide Basic pentru a experimenta tastatura pe tot ecranul. Modul Pro este disponibil din sertarul de navigare pentru experiența completă Shortcut Hub.

Cu stimă,

Openterface Team | TechxArtisan
