---
draft: false
date: 2026-05-21
title: "Aggiornamento KVM-GO: controlla il tuo target dallo smartphone con KeyCmd 0.19"
description: "Usa KeyCmd 0.19 con KVM-GO tramite USB o Bluetooth: tastiere KM Basic e Pro, modalità Compose, preset gamepad, Shortcut Hub e controlli per presentazioni—nessun dongle video richiesto per l'input HID."
keywords: "KVM-GO KeyCmd, KeyCmd 0.19, app Android KVM-GO, controllo smartphone KVM-over-USB, Openterface KeyCmd, tastiera virtuale KVM, KVM-GO Bluetooth USB, modalità KM Pro Compose, KVM-GO HDMI DP VGA, app Openterface KVM, input KVM portatile"
author: "Openterface Team | TechxArtisan"
category: "Aggiornamenti Prodotto"
tags: ["KVM-GO", "KeyCmd", "Aggiornamenti Prodotto", "Android", "USB", "Bluetooth", "Tastiera", "Gamepad", "Release"]
featured: false
social:
  image: "https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp"
  title: "KVM-GO + KeyCmd 0.19 — controlla il tuo target dallo smartphone"
  description: "KeyCmd 0.19 si associa a KVM-GO via USB o Bluetooth per tastiera, mouse, gamepad, scorciatoie e Compose—mentre Openterface KVM gestisce il video quando ne hai bisogno."
---

# Aggiornamento KVM-GO: controlla il tuo target dallo smartphone con KeyCmd 0.19

Ciao a tutti,

Grazie per aver sostenuto **KVM-GO** e per la vostra pazienza mentre le unità procedono attraverso la produzione e la spedizione. Sappiamo che molti di voi stanno ancora aspettando l'hardware e vogliamo che la vostra configurazione sia completa fin dal primo giorno.

Insieme all'app **Openterface KVM** (video e controllo KVM completo su smartphone o tablet), abbiamo migliorato **KeyCmd**, la nostra app complementare per l'input di tastiera, mouse, gamepad e scorciatoie. **KeyCmd 0.19** è la versione che consigliamo oggi se usate KVM-GO. Associatela via **USB** o **Bluetooth**, installatela sopra qualsiasi versione precedente e le vostre impostazioni, i profili e i dispositivi associati verranno mantenuti.

![KVM-GO su un laptop con la tastiera KeyCmd su uno smartphone](https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp){:style="max-width:720px;width:100%;height:auto"}

Di seguito vi spieghiamo cosa fa KeyCmd con KVM-GO, quale modalità aprire per ogni attività e come sfruttarla al meglio su una macchina target reale.

![Schermata di benvenuto di KeyCmd](https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape_1.webp){:style="max-height:320px;width:auto"}

## Modalità e come usarle

### Tastiera e Mouse (Basic)

Aprite questa modalità quando desiderate una **tastiera semplice a schermo intero** e nient'altro che possa intralciare il lavoro.

**Ideale per:** password del BIOS, brevi comandi shell, inserimento da tastierino numerico o controllo del mouse con un ampio touchpad mentre KVM-GO mostra lo schermo.

**Come usarla:**

- Aprite **KM Basic** dal menu di navigazione.
- Usate la tastiera su schermo, il **tastierino numerico** (verticale o orizzontale) o la scheda **touchpad** secondo necessità.
- Nelle **Impostazioni**, scegliete i **tasti modificatori permanenti** (tocca per bloccare Shift/Ctrl) o i modificatori **stile accordo** se preferite le combinazioni tieni premuto e tocca.

**Perché è utile:** più spazio sullo schermo per i tasti, meno interfaccia, più veloce quando serve solo l'input e non le scorciatoie.

![Tastiera a schermo intero KM Basic](https://assets2.openterface.com/images/keymod/KM-Basic-Keyboard_1.webp){:style="max-height:320px;width:auto"}

![Tastierino numerico KeyCmd in orizzontale](https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape_1.webp){:style="max-height:320px;width:auto"}

### Tastiera e Mouse (Pro)

![Tastiera divisa KM Pro in orizzontale](https://assets2.openterface.com/images/keymod/KM-Pro-Keyboard-landscape-split_1.webp){:style="max-height:320px;width:auto"}

![Tastiera e touchpad KeyCmd in verticale](https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait_1.webp){:style="max-height:320px;width:auto"}

Aprite questa modalità per il **lavoro di controllo quotidiano** su macchine dietro KVM-GO: tastiere divise, IME, barre Shortcut Hub e l'editor **Compose**.

**Ideale per:** sessioni di digitazione più lunghe, macro e scorciatoie, invio di blocchi di testo o script all'host mentre osservate il risultato sulla vista KVM.

![Modalità Compose che invia uno script](https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait_1.webp){:style="max-height:320px;width:auto"}

Vale la pena provare **Compose** se incollate spesso comandi o script: scrivete sul telefono, revisionate e poi inviate come battute di tasti all'host. Questa [breve demo su YouTube](https://www.youtube.com/watch?v=_rJF-hTF3_E) mostra il flusso completo.

**Come usarla:**

- Aprite **KM Pro** dal menu di navigazione.
- Usate tastiera e touchpad come nella Basic, oltre alle categorie **Shortcut Hub** in alto per azioni con un solo tocco configurate nei profili.
- Aprite **Compose** per redigere testi lunghi sul telefono, revisionarli e poi cliccare su **invia** come battute di tasti HID. Gli invii lunghi mostrano una barra di avanzamento. Se il testo contiene caratteri non ASCII, l'app vi avviserà prima dell'invio in modo da poter verificare la compatibilità con l'host (particolarmente utile su macOS).

**Perché è utile:** un unico posto per digitare, puntare, usare scorciatoie e flussi di lavoro tipo "incolla" senza dover portare una tastiera fisica sulla macchina target.

### Gamepad

Aprite questa modalità quando desiderate un layout di **controller virtuale** sullo schermo, ottimizzato per i giochi o per qualsiasi app sul target che richieda un gamepad.

**Ideale per:** emulatori, giochi casual o una superficie di controllo compatta con stick e pulsanti mentre KVM-GO gestisce il display.

**Come usarla:**

- Passate alla modalità **Gamepad**.
- Toccate **Preset** nella barra degli strumenti per **scorrere** i layout salvati. **Premete a lungo Preset** per aprire l'elenco completo, **importare/esportare** o **aggiungere moduli** (stick, pulsanti, touchpad).
- Iniziate dal preset **emu-6** incluso e modificatelo da lì. Potete aggiungere **più touchpad** e moduli stick extra in un unico layout.

**Perché è utile:** non siete vincolati a un unico layout predefinito; salvate i layout per gioco o per macchina e condividete i preset con altri.

![Layout preset Gamepad](https://assets2.openterface.com/images/keymod/Gamepad-perset-1_1.webp){:style="max-height:320px;width:auto"}

![Preset Gamepad usato in Minecraft](https://assets2.openterface.com/images/keymod/Gamepad-perset-minecraft_1.webp){:style="max-height:320px;width:auto"}

*Preset personalizzato per Minecraft.*

### Shortcut Hub

Questo è il centro di **profili e scorciatoie** all'interno di KM Pro: categorie, pannelli dei dettagli e le scorciatoie che assegnate alle barre.

**Ideale per:** operazioni ripetitive sul target (aprire il terminale, incollare una catena di comandi, attivare impostazioni) mentre KVM-GO rimane connesso per il video.

**Come usarla:**

- Da KM Pro, lavorate nel profilo **Default** (o nel vostro).
- Usate le schede delle categorie e l'interfaccia dei dettagli per gestire le scorciatoie.
- Seguite il **tour guidato di Shortcut Hub** se non conoscete ancora l'organizzazione dei profili.

### Presentazione

Una superficie di controllo più semplice in stile **telecomando per presentazioni**, mantenuta in **verticale** così i pulsanti non si spostano quando ruotate il telefono.

**Ideale per:** scorrere le diapositive o controlli leggeri per presentazioni sul target.

![Modalità Presentazione che controlla Google Slides](https://assets2.openterface.com/images/keymod/KeyCmd-Presentation-Google-Slides.webp){:style="max-height:320px;width:auto"}

---

## Lingue

L'interfaccia dell'app è disponibile in **11 lingue**. Aggiunte recenti: coreano, italiano, russo e portoghese brasiliano.

Aprite **Settings** → **App language** per cambiare lingua.

---

## Scarica KeyCmd 0.19 e connettiti a KVM-GO

**Download:** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

Installate sopra l'app esistente se ne avete già una. Non è necessario cancellare i dati.

**Connetti a KVM-GO (la porta video può rimanere scollegata):**

Per **tutte e tre le varianti di KVM-GO** (HDMI, VGA e DP), non è necessario collegare il **connettore video sul dongle** a nulla per l'input di KeyCmd. La porta HDMI, VGA o DP può rimanere vuota. Scegliete una delle due configurazioni seguenti.

**Opzione A — Bluetooth (il target alimenta il KVM-GO)**

1. Collegate il **cavo USB nero corto** alla porta **Target** del KVM-GO e alla macchina che state controllando. Questa connessione da sola **alimenta** il KVM-GO.
2. Sul telefono, aprite **KeyCmd** e cercate il KVM-GO tramite **Bluetooth**.

**Opzione B — USB al vostro telefono Android (porta Host)**

1. Collegate il **cavo arancione lungo** dalla porta **Host** del KVM-GO al vostro telefono Android.
2. Aprite **KeyCmd** e connettetevi via **USB** nell'app.

![Porta Target di KVM-GO collegata a un laptop tramite il cavo USB nero corto](https://assets2.openterface.com/images/kvm-go/kvm-go-target-port-laptop-power.webp){:style="max-height:360px;width:auto"}

Per video a schermo intero più input, usate **Openterface KVM** per il display del target e **KeyCmd** per tastiera, mouse e scorciatoie. KeyCmd da solo è sufficiente quando il target ha già il proprio schermo e serve solo l'input.

**Funziona anche con Mini-KVM** via USB se usate entrambi i dispositivi.

> **Ancora in beta.** I preset del gamepad e gli invii di Compose possono comportarsi diversamente a seconda del sistema operativo dell'host. Se accade qualcosa di insolito con KVM-GO, contattateci su **Discord** con uno screenshot, la vostra variante di KVM-GO (HDMI / DP / VGA) e cosa vi aspettavate.

> **Codice sorgente:** Non ancora pubblico. Prevediamo di renderlo open-source dopo il raggiungimento dei traguardi di crowdfunding sui progetti correlati. Chiedete su Discord se avete bisogno di aiuto per trovare l'APK.

---

## Informazioni su KeyMod (opzionale, separato da KVM-GO)

Stiamo anche sviluppando **[KeyMod](https://openterface.com/product/keymod/)**, un dongle HID USB e Bluetooth dedicato per la stessa app KeyCmd. I sostenitori di KVM-GO non hanno bisogno di KeyMod per i flussi di lavoro sopra descritti; KeyCmd su KVM-GO è la strada che vi consigliamo di seguire ora.

Se siete curiosi di conoscere un dongle standalone per configurazioni non KVM, potete seguire la [campagna KeyMod su Crowd Supply](https://www.crowdsupply.com/techxartisan/openterface-keymod). Si tratta di un progetto separato rispetto alla spedizione di KVM-GO.

---

## Saremmo lieti di ricevere il vostro feedback

Se avete qualche minuto, installate **KeyCmd 0.19**, connettetelo al vostro KVM-GO (o Mini-KVM) e diteci cosa vi sembra ancora scomodo. Le segnalazioni provenienti da casi d'uso come "crash-cart" e laboratori domestici finiscono direttamente nelle nostre prossime release.

Modi pratici per aiutare il progetto KVM-GO:

- **Condividete cosa funziona** su Discord o nella vostra community (consigli sul BIOS, associazione Bluetooth, modalità preferite)
- **Ditelo a un collega** che gestisce apparecchiature headless e potrebbe aver bisogno di un KVM tascabile
- **Continuate a inviare feedback onesti**, specialmente sui punti critici. Questo modella il prodotto più di qualsiasi complimento

Grazie ancora per aver sostenuto KVM-GO e per aiutarci a rendere il KVM-over-USB portatile migliore per tutti.

Cordiali saluti,

**Openterface Team | TechxArtisan**
