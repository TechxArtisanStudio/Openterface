---
title: "Funzionalità e specifiche"
description: "Panoramica completa di Openterface KVM Extension for uConsole: funzionalità potenti inclusi input HDMI diretto, controllo USB HID, fattore di forma perfetto e specifiche tecniche dettagliate. Tutto quello che devi sapere su questa soluzione KVM portatile."
keywords: "funzionalità estensione KVM, uConsole KVM, HDMI KVM, controllo USB HID, KVM portatile, controllo headless, sostituzione 4G LTE, specifiche tecniche, espansione uConsole"
---

# **Funzionalità e specifiche** | Openterface KVM Extension for uConsole

![PCB-front](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:320px"}
![PCB-Back](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:320px"}

## Funzionalità principali

- **HDMI diretto + USB HID**: Sfrutta lo schermo e i controlli integrati del uConsole con input HDMI diretto ed emulazione USB HID.
- **Plug-and-Play**: Controllo istantaneo senza installazione software o tracce residue sul dispositivo target.
- **Bassa latenza**: Ottimizzato per troubleshooting a livello BIOS e interazioni in tempo reale.
- **Portatile**: Strumento mobile tutto-in-uno—nessun bisogno di monitor aggiuntivi, tastiere o configurazione di rete.
- **Senza rete**: Controllo headless stabile tramite cattura HDMI e input HID, nessuna rete richiesta.
- **Trasferimento testo**: Trasferisci rapidamente testo simulando pressioni di tasti—ideale per nomi utente, password e frammenti di codice. Supporta ASCII completo, inclusi simboli e punteggiatura. [Controlla la nostra app](/app) per i dettagli.
- **Open Source**: Costruito su [Openterface KVM QT](https://github.com/techxArtisanStudio/openterface_qt) con supporto attivo della comunità.

## Specifiche tecniche

### Dimensioni fisiche

- **Dimensione:** 37 × 77 mm (corrisponde al modulo 4G/LTE)
- **Spessore:** 1,0 mm (più sottile del modulo 4G/LTE originale a 1,2 mm)
- **Materiale:** PCB di alta qualità con contatti a molla

### Emulazione completa tastiera e mouse

- **USB HID:** Posizionamento assoluto e relativo del mouse, supporto completo tastiera, tasti multimediali.
- **Connessione:** Collegamento USB al target tramite la porta femmina Type-C della scheda di estensione.

### Video e audio

- **Input:** Fino a 4K (3840×2160) @ 30Hz tramite HDMI
- **Output:** Full HD (1920×1080) @ 30Hz con latenza inferiore a 140ms
- **Display:** Utilizza lo schermo integrato del uConsole
- **Compressione:** Supporto YUV e MJPEG
- **Compatibilità:** VGA, DVI, Micro HDMI (tramite adattatori)
- **Audio:** Pass-through audio incorporato HDMI

### Porta USB 2.0 commutabile

- **Porta condivisa:** Commuta facilmente l'accesso USB tra uConsole e dispositivo target (es. chiavi USB) utilizzando l'app host.
- **Velocità USB:** Trasmissione a velocità completa 12Mbps

### Connettività e alimentazione

- **Alimentazione:** Attinge energia direttamente dallo slot di espansione del uConsole (nessuna alimentazione esterna necessaria)
- **Compatibilità target:** Windows, macOS, Linux, Android, iOS
- **Software target:** Nessuna installazione richiesta
