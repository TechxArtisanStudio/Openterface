---
title: FAQ per Openterface KeyMod Series
description: Domande frequenti su KeyMod Series: funzionalità, compatibilità, piattaforme e informazioni sul pre-lancio.
keywords: KeyMod, Openterface, emulatore HID, tastiera Bluetooth, tastiera telefono, open source, pre-lancio, Android, iPadOS
---

# FAQ per Openterface KeyMod

Benvenuto nella FAQ di **Openterface KeyMod**.  
Se non trovi ciò che ti serve, **inviaci una email a [info@openterface.com](mailto:info@openterface.com)** o **unisciti alla nostra community** su [Discord](/discord) o [Reddit](/reddit).

⚠️ **Nota**: KeyMod è attualmente in sviluppo pre-lancio. Funzionalità, specifiche e design sono soggetti a modifiche durante la finalizzazione del prodotto.

---

## :material-clipboard-list: Navigazione rapida

- [FAQ per Openterface KeyMod](#faq-per-openterface-keymod)
  - [:material-clipboard-list: Navigazione rapida](#material-clipboard-list-navigazione-rapida)
  - [Generale](#generale)
  - [Connettività](#connettività)
  - [Funzionalità](#funzionalità)
  - [Pre-lancio](#pre-lancio)

---

## Generale

**:material-chat-question:{ .faq } Cos'è KeyMod?**

KeyMod è un emulatore HID (tastiera e mouse) compatto USB + Bluetooth che trasforma il tuo telefono in una tastiera e trackpad portatili. Usalo per controllare dispositivi che necessitano di input tastiera/mouse—chioschi, smart TV, decoder, display esterni—senza portare una tastiera completa.

**:material-chat-question:{ .faq } Quali piattaforme supporta l'app KeyMod?**

L'app controller KeyMod si concentra su **Android** e **iPadOS**. Stiamo anche espandendo il controllo desktop con software **Windows e macOS** nel nostro più ampio ecosistema Openterface.

**:material-chat-question:{ .faq } Il dispositivo di destinazione ha bisogno di software?**

No. KeyMod emula una tastiera e mouse USB standard. Il dispositivo di destinazione lo riconosce come hardware HID plug-and-play—nessun driver o installazione software richiesta.

**:material-chat-question:{ .faq } KeyMod è open source?**

Sì. KeyMod è hardware e software aperti. Pubblicheremo schemi, file PCB, firmware, software e BOM man mano che il progetto evolve.

---

## Connettività

**:material-chat-question:{ .faq } USB o Bluetooth—quale devo usare?**

- **USB**: Più affidabile, latenza inferiore. Usalo quando vuoi la connessione più stabile.
- **Bluetooth**: Senza cavi. Usalo quando vuoi una configurazione più leggera e lo scenario lo consente.

**:material-chat-question:{ .faq } Quali varianti hardware sono previste?**

1. **Connettore 2-in-1** — Spina USB A + USB C combinata per ampia compatibilità
2. **Versione USB C** — Spina USB C dedicata per dispositivi moderni

---

## Funzionalità

**:material-chat-question:{ .faq } Quali layout gamepad sono supportati?**

KeyMod può fungere da controller di gioco virtuale con **layout Xbox**, **layout PlayStation** e **layout NES**.

**:material-chat-question:{ .faq } Posso creare profili e macro personalizzati?**

Sì. L'app mobile open source supporta profili di input personalizzati, macro, scorciatoie e collegamenti per il flusso di lavoro. Puoi anche usare modalità tastierino numerico e gamepad.

**:material-chat-question:{ .faq } Cosa sono i pulsanti hardware programmabili?**

KeyMod include pulsanti hardware programmabili per azioni sul dispositivo come trigger rapidi e flussi di lavoro semplici in stile macro. Questa capacità è ancora sperimentale e sarà perfezionata grazie al feedback della community.

---

## Pre-lancio

**:material-chat-question:{ .faq } Quando verrà lanciato KeyMod?**

KeyMod è in sviluppo pre-lancio. Iscriviti alla [pagina del prodotto](/product/keymod/) per notifiche di lancio e aggiornamenti.

**:material-chat-question:{ .faq } Come si collega KeyMod a Mini-KVM e KVM-Go?**

KeyMod utilizza il collaudato nucleo HID di Openterface Mini-KVM. Condivide lo stesso approccio di emulazione tastiera e mouse basato su hardware, ma è progettato per un caso d'uso diverso: trasformare il tuo telefono in una tastiera/trackpad portatile per il controllo locale dei dispositivi, piuttosto che la cattura video KVM-over-USB.
