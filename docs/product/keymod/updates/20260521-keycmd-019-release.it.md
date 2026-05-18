---
draft: false
date: 2026-05-21
title: "KeyCmd 0.19: Rebranding dell'app, modalità Compose KM Pro, supporto multilingue e guide interattive per modalità"
description: "KeyCmd 0.19 porta un importante rebranding da KeyMod a KeyCmd, la nuova modalità Compose KM Pro con invio HID Unicode, UI multilingue (coreano, italiano, russo, pt-BR), guide interattive per modalità e decine di miglioramenti UX."
keywords: "KeyCmd 0.19, rilascio KeyCmd, rebranding app, modalità Compose, invio HID Unicode, multilingue, guide interattive, aggiornamento Openterface KeyCmd, emulatore HID, tastiera virtuale, app tastiera Android"
author: "TechxArtisan Studio"
category: "Product Updates"
tags: ["KeyCmd", "Product Updates", "Release", "Compose", "i18n", "Android"]
featured: false
social:
  image: "https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp"
  title: "Rilascio di KeyCmd 0.19 — Modalità Compose, rebranding, multilingue, guide interattive"
  description: "KeyCmd 0.19 porta la nuova modalità Compose, rebranding dell'app in KeyCmd, 4 nuove lingue, guide interattive e miglioramenti UX significativi."
---

# KeyCmd 0.19: Rebranding dell'app, modalità Compose KM Pro, supporto multilingue e guide interattive per modalità

KeyCmd **0.19** (`versionCode` **19**) è un aggiornamento importante che porta il **rebranding** da KeyMod a KeyCmd, la nuovissima **modalità Compose di KM Pro** con invio HID compatibile Unicode, un'**interfaccia multilingue estesa** (inclusi coreano, italiano, russo e portoghese brasiliano), **guide interattive per modalità**, e decine di miglioramenti UX nelle modalità tastiera, gamepad e presentazione.

## Rebranding dell'app: KeyMod → KeyCmd

Il nome visualizzato dell'app è ora **KeyCmd** in tutti i punti di accesso. Questo rebranding chiarisce la distinzione tra l'**hardware KeyMod** e la sua **app companion KeyCmd**.

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp" alt="Schermata di benvenuto KeyCmd" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">

### Cosa è cambiato

- **Nome visualizzato dell'app**: L'icona del launcher e l'UI di sistema ora mostrano "KeyCmd"
- **Flusso di benvenuto**: Wordmark e testi aggiornati da KeyMod a KeyCmd
- **Artefatti CI e nomi file APK**: Usano il prefisso **KeyCmd**
- `applicationId` rimane **`com.openterface.keymod`** per aggiornamenti in loco senza interruzioni

Utenti esistenti: le tue impostazioni, profili e dispositivi abbinati sono conservati. L'aggiornamento è trasparente.

## Tastiera e mouse: esperienza a schermo intero

KeyCmd offre un'esperienza a schermo intero di tastiera, touchpad e tastierino numerico — ottimizzata per orientamenti verticale e orizzontale.

<div class="slideshow-container" id="slideshow-keycmd-019-kbm-it" data-auto-slide="true" data-auto-slide-interval="3000">
  <div class="slideshow-wrapper">
    <div class="slide active">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Full-Keyboard-landscape.webp" alt="Tastiera orizzontale a schermo intero" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape.webp" alt="Tastierino numerico orizzontale" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-portrait.webp" alt="Tastierino numerico verticale" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait.webp" alt="Tastiera e touchpad verticali" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-km-basic-Touchpad.webp" alt="Touchpad orizzontale" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Remote-Coding-portrait.webp" alt="Coding remoto con KeyCmd" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Settings-screen.webp" alt="Schermata impostazioni KeyCmd" style="max-height:320px;" loading="lazy">
    </div>
  </div>

  <div class="slideshow-navigation">
    <button class="nav-arrow left" onclick="changeSlide('slideshow-keycmd-019-kbm-it', -1)">❮</button>
    <div class="slideshow-dots">
      <span class="dot active" onclick="currentSlide('slideshow-keycmd-019-kbm-it', 1)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-it', 2)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-it', 3)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-it', 4)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-it', 5)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-it', 6)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-it', 7)"></span>
    </div>
    <button class="nav-arrow right" onclick="changeSlide('slideshow-keycmd-019-kbm-it', 1)">❯</button>
  </div>
</div>

## KM Pro: modalità Compose & Send

La novità più grande nella versione 0.19 è la **modalità Compose** in KM Pro — un editor di testo dedicato che ti permette di digitare lunghi passaggi e inviarli come sequenze di tasti HID alla macchina target.

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait.webp" alt="Esecuzione script in modalità Compose" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">


### Editor Compose

- **Barra dei collegamenti superiore + riga azione di composizione** con controlli **Cancella** e **Annulla/Cancella**
- **Conservazione della bozza**: il tuo testo viene conservato quando cambi sottomodalità e anche dopo un invio riuscito
- **Integrazione IME**: digita con la tastiera del telefono, invia come sequenze di tasti HID pulite
- **Avanzamento invio determinato**: una barra di avanzamento visibile per i buffer HID lunghi in modo da sapere esattamente a che punto è l'invio

### Invio HID compatibile Unicode

- **Revisione dei rischi in doppia modalità**: prima di inviare testo non ASCII, una finestra di dialogo avvisa sulla compatibilità Unicode e fornisce azioni di ispezione e anteprima
- **Flusso esadecimale Unicode macOS**: sugli host macOS, l'app usa il metodo di inserimento Option+codice esadecimale per i caratteri estesi
- **Finestre di invio più sicure**: la schermata di revisione adatta il suo contenuto in base a se il buffer è ASCII puro o contiene caratteri Unicode
- **Strumenti di ispezione caratteri**: la finestra di dialogo del rischio di invio fornisce azioni **Verifica** e **Anteprima**, e gli host macOS includono una voce dedicata di **audit percorso esadecimale Unicode**

### Ambito di KM Basic

Nella versione 0.19, **Compose & Send rimane una funzione di Tastiera e Mouse Pro**. KM Basic si concentra sui flussi di lavoro di tastiera a schermo intero, touchpad e tastierino numerico.

## Supporto multilingue

KeyCmd ora supporta **11 lingue dell'interfaccia**. Questo rilascio aggiunge quattro nuove localizzazioni:

- **Coreano (ko)**: traduzione completa dell'interfaccia
- **Italiano (it)**: traduzione completa dell'interfaccia
- **Russo (ru)**: traduzione completa dell'interfaccia
- **Portoghese brasiliano (pt-BR)**: traduzione completa dell'interfaccia

Insieme all'inglese, cinese semplificato, cinese tradizionale, giapponese, francese, tedesco e spagnolo esistenti, KeyCmd ora copre la stragrande maggioranza della nostra base utenti globale.

### Cosa è cambiato

- **Selettore lingua** nelle Impostazioni con nomi canonici delle lingue
- **Intestazioni Bluetooth** e **anteprima tocco tasti** localizzate
- **Correzioni lint di rilascio** per le schede di avviso di composizione in tutte le lingue

## Guide interattive per modalità

Ogni modalità ora ha una **guida interattiva integrata** che ti accompagna passo passo attraverso le sue funzioni.

### Guide disponibili

- **Guida Shortcut Hub**: apre il profilo predefinito e copre l'interfaccia di dettaglio, le schede delle categorie e la gestione dei collegamenti
- **Guida Gamepad**: spiega il layout del gamepad, la gestione dei moduli e il sistema di preset
- **Guida KM Pro**: copre la modalità Compose, il pannello dei collegamenti e le funzioni specifiche di Pro
- **Guida KM Basic**: spiega la tastiera a schermo intero, lo scorrimento con mantenimento dei modificatori e il tastierino numerico

### Funzioni delle guide

- **Guide per modalità**: ogni modalità ha la propria guida personalizzata
- **Foglio di ripetizione**: rivisita qualsiasi guida in qualsiasi momento tramite il pulsante **Guida modalità** (icona a sinistra della sezione di connessione)
- **Supporto i18n**: il contenuto delle guide è localizzato in tutte le lingue dell'app
- **Ottimizzato per orizzontale**: i layout bottom-sheet si adattano correttamente in orientamento orizzontale

## Miglioramenti UX

### Tastiera

- **Anteprima tocco tasti**: vedi esattamente cosa verrà inviato prima di premere. Abilitabile tramite Impostazioni. Abilitato di default.
- **Correzione HID tocco rapido**: miglioramento del timing di rilascio dei tocchi e eventi di rilascio consolidati per una digitazione più veloce
- **Gestione tocco caratteri alternativi**: premendo a lungo il tasto `a` ora appaiono le alternative ¥ (su), £ (sinistra), € (destra) con feedback visivo migliorato
- **Scorrimento con mantenimento modificatori**: nelle guide KM Basic/Pro, un nuovo passo insegna il gesto di scorrimento con mantenimento per accesso rapido ai modificatori

### Gamepad

- **Barra sessione di editing rimossa**: interfaccia gamepad più pulita senza la vecchia barra degli strumenti della sessione di editing
- **Interfaccia e guida del gamepad**: nuovo polish visivo e guida interattiva integrata
- **Icona guida modalità**: posizionata a sinistra della sezione di connessione per facile accesso

### Presentazione

- **Blocco verticale**: la modalità Presentazione è limitata agli orientamenti verticale e verticale invertito per un controllo del presentatore stabile

### Interfaccia e tema

- **Campioni di accento**: sostituito lo spinner della famiglia di colori del tema con campioni visivi di accento per una selezione del colore più facile
- **Allineamento accenti UI**: tutti gli accenti UI seguono ora la famiglia di colori del tema (non il colore primario legacy)
- **Cluster destro dell'intestazione**: dimensioni migliorate per le icone di connessione sia nell'app principale che nell'interfaccia KM Basic
- **Stile pulsante di invio Compose**: aspetto del pulsante di invio non ASCII allineato in modalità chiara

### Impostazioni

- **Riorganizzazione delle impostazioni**: nomi canonici delle lingue; script di installazione dell'emulatore rinominati per maggiore chiarezza
- **Script di aiuto allo sviluppo**: rinominati per una più chiara identificazione dei dispositivi e denominazione delle azioni
- **Documentazione FAQ**: `docs/FAQ.md` aggiornato con il comportamento attuale dell'app

## Casi d'uso reali

### Coding remoto

KeyCmd non è solo per la gestione dei server. Gli sviluppatori lo usano per **sessioni di coding remoto** — controllo di una macchina di sviluppo headless da telefono o tablet, con supporto completo per tastiera, touchpad e tastierino numerico.

## Cosa non è cambiato

**Tastiera e Mouse Pro** (modalità composita con barre Shortcut Hub, layout divisi e comportamento IME ricco) rimane l'esperienza completa di prima. Tutti i profili, preset e dispositivi abbinati esistenti sono conservati.

## Ottenere l'aggiornamento

**Questa versione (0.19):** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

> **Nota Beta:** L'app Android KeyCmd è ancora in fase beta attiva. Il repository sorgente non è ancora pubblico — pianifichiamo di renderlo open source dopo una campagna di crowdfunding di successo. Se sei un beta tester e hai bisogno dell'ultima APK, contattaci su Discord e ti invieremo il build.

Le installazioni esistenti si aggiornano in loco.

## Compatibile con Mini-KVM e KVM-Go

L'app KeyCmd non è limitata all'hardware KeyMod. Anche gli utenti Openterface esistenti possono provarla:

- **KVM-Go**: connessione via **Bluetooth** o **USB**
- **Mini-KVM**: connessione via **USB**

## Note di aggiornamento

- **Rebranding**: il nome dell'app cambia da KeyMod a KeyCmd. I tuoi dati sono conservati.
- **Modalità Compose**: nuova per Tastiera e Mouse Pro.
- **Guide interattive**: tocca l'icona della guida (a sinistra della sezione di connessione) in qualsiasi modalità per avviare la guida interattiva.
- **Lingue**: vai alle Impostazioni per cambiare la lingua dell'app. KeyCmd ora supporta 11 lingue dell'interfaccia.

Cordiali saluti,

Openterface Team | TechxArtisan
