---
draft: false
date: 2026-05-09
title: "KeyMod 0.15: Pipeline preset gamepad, Tastiera e mouse (Basic), Layout multi-touchpad"
description: "KeyMod 0.15 introduce la pipeline preset del gamepad con schema v7, layout multi-touchpad, livello Tastiera e mouse (Basic) con tastiera a schermo intero e branding KeyMod in tutta l'app. Un passo importante verso un'esperienza di input raffinata."
keywords: "KeyMod 0.15, KeyMod rilascio, preset gamepad, multi-touchpad, tastiera mouse basic, branding KeyMod, aggiornamento Openterface KeyMod, emulatore HID, gamepad virtuale, app tastiera Android"
author: "TechxArtisan Studio"
category: "Aggiornamenti del prodotto"
tags: ["KeyMod", "Aggiornamenti del prodotto", "Rilascio", "Gamepad", "Tastiera", "Android"]
featured: false
social:
  image: "https://assets.openterface.com/images/keymod/keymod-015-release.jpg"
  title: "Rilascio KeyMod 0.15 — preset gamepad, livello basic, multi-touchpad"
  description: "KeyMod 0.15 porta la pipeline preset del gamepad v7, un livello dedicato Tastiera e mouse (Basic), layout multi-touchpad e il nuovo branding KeyMod."
---

# KeyMod 0.15: Pipeline preset gamepad, Tastiera e mouse (Basic), Layout multi-touchpad

KeyMod **0.15** (`versionCode` **15**) è una versione fondamentale che introduce tre funzionalità principali: la **pipeline preset del gamepad** con schema layout **v6-v7**, il livello dedicato **Tastiera e mouse (Basic)** e i layout **multi-touchpad**. Questo aggiornamento porta anche il branding **KeyMod** completo nel flusso di benvenuto e negli artefatti di build.

## Gamepad: Pipeline preset v7

Il gamepad utilizza ora un vero **sistema di preset** che consente di salvare, caricare, importare ed esportare layout controller personalizzati.

### Cosa è cambiato

- **Preset store v7** sostituisce i vecchi layout integrati. I preset di fabbrica classici (`preset_classic_*`) e **Two buttons** (`preset_two_buttons`) sono stati rimossi dal disco. Solo **`preset_default`** rimane come layout di fabbrica protetto dalla cancellazione.
- **Schema v7** rende **`stick_left`** opzionale. Un layout può ora non avere alcun modulo pollice sinistro. Il menu **Add module** inserisce **`stick_left`**, **`stick_left_2`**, **`stick_left_3`**, ecc.
- **Supporto multi-touchpad**: i preset possono includere più touchpad (`touchpad_1`, `touchpad_2`). Aggiungere un touchpad assegna il prossimo id disponibile con un'ancora leggermente spostata. I pulsanti del mouse L/M/R integrati sono condivisi tra tutti i touchpad.
- **Dimensione pulsanti mouse del touchpad**: i pulsanti del mouse usano ora un raggio di disegno predefinito più grande. Puoi regolare la dimensione con pressione lunga **Mouse button size** sul touchpad o **This button size** sui singoli moduli mouse.
- **Predefiniti stick ausiliario**: **`stick_left_2+`** predefinito su croce D-pad + mappatura WASD.

### Gestione preset

- **Tocca** il chip Preset nella barra degli strumenti per scorrere i layout disponibili
- **Pressione lunga** per l'elenco completo dei preset con opzioni di importazione, aggiunta modulo ed esportazione
- Il layout **emu-6** incluso è il preset iniziale
- Il creatore di esportazione supporta i18n per condividere preset tra lingue

## Tastiera e mouse (Basic)

Un livello dedicato di tastiera a schermo intero progettato per la digitazione concentrata senza l'intestazione dell'app.

### Cosa ottieni

- **Tastiera a schermo intero** senza l'intestazione principale dell'app per più spazio sullo schermo
- **Numpad verticale e orizzontale**: griglia 5x8 in verticale (PrtSc / ScrLk / Pause / Home / End), griglia 8x5 in orizzontale con + alto, Invio e 00
- **Gateway invio ASCII-only IME**: digita testo lungo in modalità compose, invia come pulsazioni HID pulite
- **Ripetizione pressione lunga**: tieni premuti i tasti carattere/funzione per la ripetizione automatica (~400ms di ritardo, ~50ms di ripetizione)
- **Anteprima tasto**: una bolla fluttuante mostra l'etichetta effettiva sopra il tasto premuto
- **Feedback aptico** e superfici dei tasti **adattate al tema**

### Modificatori Sticky vs Chord

Le impostazioni permettono di scegliere tra **modificatori sticky** (tocca per bloccare) e **momentaneo + chord con pressione lunga** (predefinito) per la tastiera Basic.

## Branding

- Il nome di visualizzazione dell'app è ora **KeyMod**
- La schermata di benvenuto mostra il logotipo **KeyMod**
- Gli artefatti CI e i nomi dei file APK usano il prefisso **KeyMod**
- `applicationId` rimane **`com.openterface.keymod`** per aggiornamenti in-place

## Cosa resta invariato

**Tastiera e mouse Pro** (modalità composita con barre Shortcut Hub, layout divisi e comportamento IME ricco) resta l'esperienza completa di sempre.

## Ottenere l'aggiornamento

**Questa versione (0.15):** [KeyMod-release-0.15.apk](https://assets2.openterface.com/data/KeyMod-release-0.15.apk)

> **Avviso beta:** L'app KeyMod per Android è ancora in fase beta attiva. Il repo non è ancora pubblico — pianifichiamo di renderlo open source dopo una campagna crowdfunding di successo. Se sei un beta tester e hai bisogno dell'APK più recente, contattaci su Discord e ti invieremo la build.

> **Problemi noti:** Questa versione introduce cambiamenti significativi al sistema di preset del gamepad e al livello di tastiera Basic. Il nostro team di sviluppo sta ancora testando internamente, quindi potresti incontrare bug. Se riscontri qualcosa di inaspettato, segnalalo su Discord — il tuo feedback ci aiuta a stabilizzare più velocemente.

Le installazioni esistenti si aggiornano in-place.

## Compatibile con Mini-KVM e KVM-Go

L'app KeyMod non si limita all'hardware KeyMod. Anche gli utenti Openterface esistenti possono provarla:

- **KVM-Go**: connessione via **Bluetooth** o **USB**
- **Mini-KVM**: connessione via **USB**

## Note di aggiornamento

- **Gamepad**: la tua precedente preferenza a due pulsanti attiva automaticamente il preset **Two buttons** al primo avvio. Usa **Preset** (tocca per scorrere, pressione lunga per l'elenco) al posto del vecchio controllo 1 Button / 2 Buttons.
- **Tastiera e mouse (Basic)**: apri Basic per sperimentare la tastiera a schermo intero. La modalità Pro è disponibile dal cassetto di navigazione per l'esperienza completa Shortcut Hub.

Cordiali saluti,

Openterface Team | TechxArtisan
