---
title: "Funzionalità e specifiche"
description: "Panoramica completa della serie Openterface KVM-Go: design ultra-compatto con connettori video integrati, supporto 4K/60Hz, slot MicroSD e specifiche tecniche dettagliate. Soluzione KVM-over-USB delle dimensioni di un portachiavi per professionisti IT."
keywords: "funzionalità KVM-Go, KVM ultra-compatto, HDMI integrato, KVM 4K, KVM MicroSD, KVM portachiavi, specifiche KVM, controllo headless, KVM portatile, strumenti IT, gestione server"
---

# **Funzionalità e specifiche** | Serie Openterface KVM-Go

## Stato pre-lancio

La serie KVM-Go è attualmente in sviluppo pre-lancio. Stiamo perfezionando i design di PCB e case. Unisciti alla nostra [lista d'attesa]({{ config.extra.kvmgo_purchase_link }}) per rimanere aggiornato sui progressi e ottenere l'accesso anticipato.

> **Nota:** Funzionalità, specifiche e design sono ancora soggetti a modifiche mentre lo sviluppo continua.

## Modelli di prodotto
- **KVM-Go HDMI Male** — Connessione HDMI diretta
- **KVM-Go DisplayPort Male** — DisplayPort ad alte prestazioni
- **KVM-Go VGA Male** — Supporto per sistemi legacy (in sviluppo)

## Funzionalità principali

### **Design ultra-compatto**
Fattore di forma delle dimensioni di un portachiavi che entra in tasca. Non è più necessario portare ingombranti dispositivi KVM o cercare cavi video.

### **Connettori video integrati**
Capacità di connessione diretta con connettori maschio integrati:

- **HDMI Male** — Compatibilità con dispositivi moderni
- **DisplayPort Male** — Supporto ad alte prestazioni
- **VGA Male** — Supporto per sistemi legacy (in arrivo)

### **Accesso a livello BIOS**
Accesso diretto a BIOS, firmware e gestione dell'avvio del dispositivo di destinazione senza dipendenze di rete.

### **Indipendenza dalla rete**
Controllo headless stabile utilizzando la cattura video integrata e l'input tastiera/mouse emulato (HID). Nessuna connessione di rete richiesta.

### **Prestazioni video migliorate**
Enorme miglioramento rispetto al 1080p@30Hz di Mini-KVM:

- **Input**: 4096×2160 @ 60 Hz (YUV420), 4096×2160 @ 30 Hz (YUV444)
- **Output**: 4096×2160 @ 60 Hz (MJPEG), 3840×2160 @ 30 Hz (YUV420)
- **Compressione**: Supporto YUV420, YUV444 e MJPEG

### **Slot MicroSD**
Trasferimento file tra dispositivi host e destinazione

### **Supporto multipiattaforma**
[App host](/app) compatibili con macOS, Windows, Linux, Android e app web Chrome per integrazione universale.

### **Trasferimento testo**
Trasmetti facilmente il testo simulando i tasti — perfetto per nomi utente, password e frammenti di codice. Supporta caratteri ASCII inclusi simboli e punteggiatura.

!!! warning "Limitazioni del trasferimento testo"
    - **Nessuna integrazione degli appunti**: Emula solo la digitazione, nessun trasferimento di immagini o documenti
    - **Solo ASCII**: Limitato ai caratteri ASCII (nessun supporto per cinese, giapponese, coreano, ecc.)
    - **Considerazioni sulla lunghezza**: Ideale per testi brevi; blocchi grandi possono causare problemi di prestazioni

### **Convenienza plug-and-play**
Nessuna installazione software richiesta sul dispositivo di destinazione. Il controllo inizia immediatamente dopo la connessione senza lasciare tracce software.

### **Integrazione audio**
Passthrough audio HDMI integrato per un'esperienza multimediale completa. (Non supportato su KVM-Go VGA; conferma in sospeso per KVM-Go DP.)

### **Open-source**
Hardware e software [completamente open-source](/compliance) per trasparenza e [innovazione della comunità](/discord).

## Specifiche tecniche

### **Dimensioni fisiche** *(soggette a modifiche prima della consegna)*
- **Dimensione**: 18 × 18 × 55 mm (0,71 × 0,71 × 2,17 pollici)
- **Peso**: ~25 g (0,9 oz)
- **Materiale**: Involucro in lega di alluminio con cappucci stampati in 3D

### **Connettività e alimentazione**
- **Alimentazione**: Alimentato USB-C (nessuna alimentazione esterna necessaria)
- **Velocità USB**: USB 3.0 per versioni HDMI/DP; USB 2.0 per versione VGA
- **Compatibilità host**: Windows, macOS, Linux, Android, Chrome
- **Destinazione**: Nessuna installazione software richiesta

### **Video e audio**
- **Input max**: 4096×2160@60Hz (YUV420), 4096×2160@30Hz (YUV444)
- **Output max**: 4096×2160@60Hz (MJPEG), 3840×2160@30Hz (YUV420)
- **Audio**: Passthrough audio HDMI integrato

### **Funzionalità di input**
- Emulazione completa di tastiera e mouse (assoluta e relativa)
- Supporto tasti multimediali
- Funzionalità HID personalizzata
- Funzione di riattivazione del computer

### **Archiviazione**
- **Slot MicroSD**: Trasferimenti di file tramite MicroSD tra host e destinazione

