---
title: FAQ per Openterface Mini-KVM
description: Domande frequenti sul Mini-KVM, che coprono funzionalità, compatibilità, risoluzione problemi e piani futuri.
keywords: Mini-KVM, Openterface, switch KVM, open-source, risoluzione problemi, cattura video, USB, compatibilità
---

# FAQ per Openterface Mini-KVM

Benvenuti alle FAQ per il nostro prodotto di punta **Openterface Mini-KVM**.  
Se non trovate quello che vi serve, **inviateci una email a [info@openterface.com](mailto:info@openterface.com)** o **unitevi alla nostra comunità** su [Discord](/discord) o [Reddit](/reddit).

⚠️ _Le FAQ potrebbero essere obsolete — fateci sapere se vedete qualcosa che necessita di aggiornamento._

---

## :material-clipboard-list: Navigazione rapida

-   [Porta USB e trasferimento file](#porta-usb-e-trasferimento-file)
-   [Tecnico](#tecnico)
-   [Controllo](#controllo)
-   [Video](#video)
-   [Risoluzione problemi](#risoluzione-problemi)
-   [Altro](#altro)

---

## Porta USB e trasferimento file

**:material-chat-question:{ .faq } Può trasferire file?**

Sì — tramite la porta USB-A commutabile condivisa tra host e target.

**:material-chat-question:{ .faq } Posso commutare la porta USB via software?**

Sì, sulla versione hardware **v1.9+**.

**:material-chat-question:{ .faq } Perché USB 2.0 invece di 3.0?**

USB 2.0 è sufficiente per video 1080p@30Hz + HID + trasferimento file a velocità standard mantenendo compattezza, maggiore freschezza e convenienza.  
USB 3.0 potrebbe apparire nei futuri modelli pro.

---

## Tecnico

**:material-chat-question:{ .faq } Open-source?**

Sì — certificato da [OSHWA](https://certification.oshwa.org/cn000015.html). Hardware e software sono su [GitHub](/contributing/).

**:material-chat-question:{ .faq } Accesso BIOS**

La connessione USB diretta consente controllo completo a livello BIOS, a differenza degli strumenti solo remoti (VNC, TeamViewer).  
Le macchine più vecchie potrebbero avere problemi BIOS nel riconoscere il nostro hub USB — segnalate i casi.

**:material-chat-question:{ .faq } Trasmissione video/dati**

Il video viene catturato via HDMI e inviato via USB 2.0.  
La porta USB commutabile vi consente di condividere unità o altri dispositivi.

**:material-chat-question:{ .faq } Gestione alimentazione**

Il Mini-KVM può attingere alimentazione da **entrambi i lati** (host o target). Il lato con il **cavo più corto** di solito diventa la fonte di alimentazione principale.  
Per target a basso consumo (es. Raspberry Pi), usate un alimentatore dedicato invece di alimentazione inversa via Mini-KVM.

**:material-chat-question:{ .faq } Limiti lunghezza cavi**

-   Mantenete il **cavo USB-C host arancione ≤1.5m**.
-   Per cavi più lunghi, iniettate alimentazione tramite:
    -   Cavo USB-A maschio-maschio
    -   [Pin di estensione](/product/minikvm/extension-pins/)
    -   Splitter USB-C Y
-   Stessa regola si applica al **cavo target nero**.

---

## Controllo

**:material-chat-question:{ .faq } Versione wireless o Ethernet?**

Non integrata. Usate un computer headless (es. Raspberry Pi) + desktop remoto per controllo remoto.

**:material-chat-question:{ .faq } Compatibilità PS/2?**

No — il supporto PS/2 potrebbe essere esplorato nelle versioni future.

**:material-chat-question:{ .faq } Più Mini-KVM su un computer?**

Sì, funzionalità sperimentale nell'app QT (Windows/Linux).

**:material-chat-question:{ .faq } Controllo accensione/spegnimento?**

Non direttamente, ma i [pin di estensione](/product/minikvm/extension-pins/) consentono futuri moduli di controllo ATX.

---

## Video

**:material-chat-question:{ .faq } Latenza e risoluzione**

-   Cattura a **1080p@30Hz**
-   Latenza sotto **140ms** → controllo fluido

**:material-chat-question:{ .faq } Risoluzione input vs cattura**

-   Accetta input fino a **4K@30Hz**
-   Cattura a **1080p**, input più alti vengono sottocampionati (potrebbero apparire leggermente sfocati).
-   Migliore pratica: **Impostate il target a 1080p**.

**:material-chat-question:{ .faq } Idoneità gaming**

Non per gaming AAA. Funziona bene per giochi più leggeri come Minecraft o emulatori.

**:material-chat-question:{ .faq } Controllo remoto su internet**

Non integrato, ma accoppiate Mini-KVM con software desktop remoto sull'host.

**:material-chat-question:{ .faq } Altri formati video**

Usate adattatori per VGA, DVI, DisplayPort, ecc.

---

## Risoluzione problemi

**:material-chat-question:{ .faq } Problemi hub USB**

Usate un **hub alimentato** per evitare cali di tensione che causano instabilità.

**:material-chat-question:{ .faq } L'app non mostra video o controllo non risponde**

Scollegate tutti i cavi, aspettate, riconnettete.  
Se non risolto, controllate il firmware o aggiornate l'app host.

**:material-chat-question:{ .faq } Risoluzioni strane come 43184x24228@44Hz**

Il firmware di cattura probabilmente è tornato alle impostazioni di fabbrica.  
Re-flash del firmware via [release GitHub](https://github.com/TechxArtisanStudio/Openterface_QT/releases).

**:material-chat-question:{ .faq } Re-flashato ma ancora rotto?**

-   Verificate la corretta enumerazione USB (`USB Tree Viewer` o `lsusb -v`)
-   Confermate la più recente app host
-   Se ancora fallisce, contattate il supporto per diagnostica/sostituzione.
