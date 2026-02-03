---
title: FAQ per Openterface Mini-KVM
description: Domande frequenti sul Mini-KVM, che coprono funzionalità, compatibilità, risoluzione problemi e piani futuri.
keywords: Mini-KVM, Openterface, switch KVM, open-source, risoluzione problemi, cattura video, USB, compatibilità, controllo diagnostico auto, controllo tastiera mouse, diagnostica hardware, supporto
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

Sì — certificato da [OSHWA](https://certification.oshwa.org/cn000015.html). Hardware e software sono su [GitHub](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware).

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

**:material-chat-question:{ .faq } Tastiera e mouse non possono controllare il computer target**

Se vedete il desktop del target ma gli input di tastiera e mouse non rispondono, di solito significa che la comunicazione HID non è stabilita. Provate questi passaggi:

1. **Verificare le connessioni dei cavi** — Assicuratevi che il cavo Type-C target sia collegato al computer target; il cavo host al vostro computer di controllo.
2. **Evitare hub USB non alimentati** — Usate connessione diretta o un hub alimentato.
3. **Ripristinare il chip HID** — Se il dispositivo sembra "bloccato", usate **Menu Avanzate → Ripristino chip HID di fabbrica** (OpenterfaceQt) o **Strumento di ripristino seriale** (macOS).
4. **Provare un'altra porta USB o riavviare** — L'OS host può disabilitare una porta dopo errori USB.
5. **Ridurre la velocità in baud** — In ambienti rumorosi, passate a 9600 bps per una comunicazione più affidabile.

Per i dettagli, vedete [Risoluzione problemi controllo tastiera e mouse](/product/minikvm/support/keyboard-mouse-control/).

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

**:material-chat-question:{ .faq } Come eseguo i controlli diagnostici per verificare se il mio Mini-KVM funziona?**

Eseguite il controllo diagnostico auto integrato per verificare le connessioni USB e rilevare problemi hardware:

- **macOS:** [Guida al controllo diagnostico auto (macOS)](/product/minikvm/support/diagnostic-self-check/) — Impostazioni → Avanzate e Debug → Apri Strumento diagnostico
- **Windows:** [Guida al controllo diagnostico auto (Windows)](/product/minikvm/support/diagnostic-self-check-windows/) — Avanzate → Hardware Diagnostics

I controlli testano Target/Host Plug & Play, test a stress, ecc. Se tutti i test passano, il dispositivo funziona correttamente.

**:material-chat-question:{ .faq } Come segnalo un problema hardware al supporto?**

Se il controllo diagnostico auto mostra **FAIL** su uno o più test:

1. Completate i passaggi diagnostici rimanenti (lo strumento vi guiderà).
2. Quando viene rilevato un problema, si apre una finestra **Email di supporto** o **Segnalazione di difetto**.
3. Inserite **ID Ordine** e **Nome**, poi copiate indirizzo email e bozza.
4. Allega i **file di log richiesti** (lo strumento indica quali) e una **foto della configurazione** (Mini-KVM + connessioni host/target chiaramente visibili).
5. Inviate l'email al supporto.

Istruzioni passo-passo: [Guida al controllo diagnostico auto (macOS)](/product/minikvm/support/diagnostic-self-check/) o [Guida al controllo diagnostico auto (Windows)](/product/minikvm/support/diagnostic-self-check-windows/).

**:material-chat-question:{ .faq } Problemi hub USB**

Usate un **hub alimentato** per evitare cali di tensione. Gli hub non alimentati possono causare alimentazione insufficiente e comportamento erratico dell'HID (tastiera/mouse). Vedi [Risoluzione problemi controllo tastiera e mouse](/product/minikvm/support/keyboard-mouse-control/).

**:material-chat-question:{ .faq } L'app non mostra video o controllo non risponde**

1. Scollegate tutti i cavi, aspettate qualche secondo, riconnettete.
2. Controllate [Risoluzione problemi controllo tastiera e mouse](/product/minikvm/support/keyboard-mouse-control/) per problemi HID (cavi, hub, ripristino HID).
3. Eseguite il [controllo diagnostico auto](/product/minikvm/support/diagnostic-self-check/) (macOS) o [Hardware Diagnostics](/product/minikvm/support/diagnostic-self-check-windows/) (Windows) per verificare il dispositivo.
4. Se non risolto, controllate il firmware o aggiornate l'app host.

**:material-chat-question:{ .faq } Risoluzioni strane come 43184x24228@44Hz**

Il firmware di cattura probabilmente è tornato alle impostazioni di fabbrica.  
Re-flash del firmware via [release GitHub](https://github.com/TechxArtisanStudio/Openterface_QT/releases).

**:material-chat-question:{ .faq } Re-flashato ma ancora rotto?**

-   Verificate la corretta enumerazione USB (`USB Tree Viewer` o `lsusb -v`)
-   Confermate la più recente app host
-   Eseguite il [controllo diagnostico auto](/product/minikvm/support/diagnostic-self-check/) per acquisire i log
-   Se ancora fallisce, contattate il supporto con ID Ordine, log diagnostici e foto della configurazione — vedi [Come segnalo un problema hardware al supporto?](#come-segnalo-un-problema-hardware-al-supporto)
