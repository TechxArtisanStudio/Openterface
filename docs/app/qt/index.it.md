# Openterface QT per Windows & Linux

Questo documento fornisce una panoramica del software KVM (Keyboard, Video, Mouse) multipiattaforma sviluppato con Qt, compatibile con i sistemi operativi Linux e Windows. Il software consente il controllo di un dispositivo target da un sistema host, offrendo una varietà di funzionalità accessibili tramite la barra dei menu e funzionalità aggiuntive.

## Funzionalità della Barra dei Menu Principale

### Preferenze

Il menu Preferenze consente agli utenti di personalizzare le impostazioni tramite una finestra di dialogo con quattro schede:<br>
![Preferences Gernal](https://assets.openterface.com/images/qt/preferenceGernal.webp)

-   General: consente di configurare i filtri dei log di debug e di decidere se inibire il salvaschermo durante l'esecuzione dell'applicazione. Le categorie di log includono:

    -   Core
    -   Serial
    -   UserInterface
    -   Host

    Gli utenti possono scegliere se salvare i log in un file .txt e se inibire o meno il salvaschermo.<br>

![Preferences Video](https://assets.openterface.com/images/qt/preferenceVideo.webp)

-   Video: consente di:

    -   Selezionare quale videocamera utilizzare.
    -   Impostare la risoluzione.
    -   Scegliere il formato dello stream video.

-   Audio: questa sezione è attualmente in fase di sviluppo.<br>

![Preferences TargetControl](https://assets.openterface.com/images/qt/preferenceTargetControl.webp)

-   Controllo del Dispositivo Target: consente di configurare le modalità di controllo per il dispositivo target:

    -   Modalità di controllo disponibili:

        -   Tastiera + Mouse + dispositivo USB HID
        -   Solo tastiera USB
        -   Tastiera + Mouse
        -   Solo dispositivo USB HID

    -   Impostare il Vendor ID (VID) e il Product ID (PID) letti dal dispositivo target.
    -   Definire il descrittore USB del target.

### Modifica

-   Incolla: sia l'opzione Incolla nel menu Modifica che il pulsante in alto a sinistra permettono di incollare il testo dagli appunti dell’host al dispositivo target.

### Controllo

Questo menu permette di:<br>

-   Impostare le modalità di movimento del mouse: Assoluto o Relativo. Control >> MouseMode >> Assoluto o Relativo.
-   Attivare/disattivare la visibilità del cursore del mouse dell’host. Control >> Mouse Visibility >> Nascondi Automaticamente o Mostra Sempre.
-   Commutare una porta USB tra utilizzo da parte del target o dell’host. Control >> Switchable USB >> Verso Target o Verso Host.
-   Regolare il baud rate per la trasmissione del chip. Control >> Baudrate >> 9600, 115200.

### Avanzate

Il menu Avanzate include le seguenti opzioni:<br>
![Advance menu](https://assets.openterface.com/images/qt/menuAdvance.webp)

-   Verifica Ambiente: controlla se i driver richiesti sono installati.
-   Reimposta Porta Seriale: riavvia la porta seriale.
-   Reimposta Tastiera e Mouse: ripristina le impostazioni di tastiera e mouse.
-   Ripristino di Fabbrica del Chip HID: ripristina il chip HID alle impostazioni di fabbrica.<br>
    ![Advance SerialConsole](https://assets.openterface.com/images/qt/advanceSerialConsole.webp)
-   Console Seriale: apre una nuova finestra per monitorare tutti i messaggi inviati alla porta seriale, con filtri per i messaggi inviati/ricevuti.<br>
    ![Advance ScriptTool](https://assets.openterface.com/images/qt/advanceScriptTool.webp)
-   Strumento Script: consente l'esecuzione di script AutoHotkey (AHK). Questa funzione imita AutoHotkey ma supporta solo un sottoinsieme di funzioni per mouse/tastiera e la cattura schermate. Gli script agiscono sul dispositivo target.
-   Server TCP: riceve comandi AutoHotkey via TCP da eseguire sul target.
-   Aggiornamento Firmware: scarica il firmware più recente da un server remoto, consentendo agli utenti di scegliere se flasharlo sul dispositivo.

### Lingue

La lingua dell’interfaccia può essere impostata su:

-   Danese
-   Inglese
-   Tedesco
-   Francese
-   Giapponese
-   Svedese

### Aiuto

Il menu Aiuto fornisce:<br>
![Help menu](https://assets.openterface.com/images/qt/menuHelp.webp)

-   Link al sito ufficiale e ai moduli per feedback su problemi software/hardware.
-   Informazioni sull’acquisto dell’hardware.
-   Una descrizione dell’ambiente software.
-   Informazioni: dettagli sull’organizzazione.
-   Aggiornamento: verifica aggiornamenti software.

## Funzionalità della Barra dei Menu (da sinistra a destra)

La barra dei menu, da sinistra a destra, include le seguenti funzionalità:<br>

![MenuBar](https://assets.openterface.com/images/qt/menubar.webp)

-   Selezione del Layout Tastiera: scegli il layout della tastiera.
-   Controlli Zoom: ingrandisci, riduci o ripristina lo zoom dello stream video.
-   Tastiera Virtuale: include tasti funzione e combinazioni rapide predefinite.
-   Screenshot: cattura l'intero schermo del target e lo salva in una cartella predefinita.
-   Modalità Schermo Intero: attiva/disattiva la visualizzazione a schermo intero.
-   Incolla: incolla testo dagli appunti dell’host al dispositivo target.
-   Danza del Mouse: esegue movimenti predefiniti del mouse.
-   Indicatore Dispositivo USB: mostra se un dispositivo USB è assegnato al target o all’host.

Nel frattempo, sentiti libero di esplorare il nostro repository open-source su **GitHub**: [Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) per il codice più aggiornato, gli aggiornamenti, gli esempi e per segnalare problemi.

Puoi anche unirti alla nostra [community su Discord](/discord) per entrare in contatto con il nostro team di sviluppo e con altri utenti per discutere di qualsiasi argomento relativo a KVM.

Per assistenza diretta, contattaci via email: [support@openterface.com](mailto:support@openterface.com).

---

Hai dei commenti su questa pagina? [Facci sapere qui.](https://forms.gle/wmxoR2C1VdG36mT69)
