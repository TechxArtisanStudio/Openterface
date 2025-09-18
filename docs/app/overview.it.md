# Software

Per far funzionare i tuoi gadget Openterface™ KVM, dovrai installare una delle app elencate di seguito sul tuo computer host. Puoi scaricare queste app da diverse piattaforme di app o semplicemente cliccare sui link forniti. Se ti senti avventuroso, puoi anche costruirle dal codice sorgente usando i nostri repository GitHub!

![use-case-pc-angled-view](https://assets.openterface.com/images/product/use-case-pc-angled-view.webp){ width=600 }

## Download e Installazione

<div class="grid cards" markdown>

-   ### :fontawesome-brands-windows:{ .lg } **Windows**

    ***

    Scarica o costruisci dal codice sorgente per **Openterface QT Win**:

    [:octicons-download-24: Scarica Installer {{qt_version}}](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.windows.amd64.installer.exe) <br>
    [:octicons-download-24: Scarica EXE Portatile {{qt_version}}](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT-portable.exe) <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) <br>
    [:octicons-play-24: Guarda Demo](https://youtu.be/ERzpGtRvP2o?si=e9k402f0nxsD8o2j)

-   ### :fontawesome-brands-apple:{ .lg } **macOS**

    ***

    Scarica o costruisci dal codice sorgente per **Openterface MacOS**:

    [:octicons-arrow-right-24: Installa dall'App Store](/appstore) <br>
    [:octicons-download-24: Scarica DMG Portatile](macos/dmg-installation.md) <br>
    [:octicons-mark-github-16: Openterface_MacOS](https://github.com/TechxArtisanStudio/Openterface_MacOS) <br>
    [:octicons-play-24: Guarda Demo](https://youtu.be/m7OpUem0zqY?si=tclfl0Jl77tmE6_e)

-   ### :fontawesome-brands-linux:{ .lg } **Linux**

    ***

    Scarica o costruisci dal codice sorgente per **Openterface QT Linux**:

    [:octicons-download-24: Scarica {{qt_stable}} AMD64 DEB](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_stable}}/openterfaceQT.linux.amd64.deb) <br>
    [:octicons-download-24: Scarica {{qt_stable}} AMD64 RPM](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_stable}}/openterfaceQT.linux.amd64.rpm) <br>
    [:octicons-download-24: Scarica {{qt_stable}} AMD64 AppImage](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_stable}}/openterfaceQT.linux.amd64.AppImage) <br>
    [:octicons-download-24: Scarica {{qt_stable}} ARM64 DEB](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_stable}}/openterfaceQT.linux.arm64.deb) <br>
    [:octicons-download-24: Scarica {{qt_stable}} ARM64 RPM](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_stable}}/openterfaceQT.linux.arm64.rpm) <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) <br>
    [:octicons-play-24: Guarda Demo](https://youtu.be/_ScpI6TC0Pk?si=FSg7A2zmST8QbFec)

-   ### :fontawesome-brands-android:{ .lg } **Android**

    ***

    Scarica o costruisci dal codice sorgente per **Android APK**:

    [:octicons-download-24: Scarica {{android_version}}](https://github.com/TechxArtisanStudio/Openterface_Android/releases/download/{{android_version}}/OpenterfaceAndroid-release.apk) <br>
    [:octicons-mark-github-16: Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) <br>
    [:octicons-play-24: Guarda Demo](https://x.com/TechxArtisan/status/1825460088922071398)

</div>

???+ warning "Attenzione: Controlla Privacy e Sicurezza con App di Terze Parti"
Poiché tutte le nostre app sono open source, potresti imbatterti in versioni alternative di applicazioni host per dispositivi Openterface create da altri. Possono essere piuttosto interessanti e offrire funzionalità extra, ma ecco un promemoria amichevole: rivedi attentamente le loro pratiche di sicurezza e privacy—specialmente perché il controllo KVM coinvolge eventi dal tuo schermo, tastiera e mouse. Il Team Openterface non può garantire la sicurezza di queste app di terze parti, quindi procedi con cautela!

## Controlli Base dell'App Host

### 💻 Compatibilità

-   **Software Host**: Installa la nostra app host per macOS, Windows o Linux.
-   **Dispositivi Target**: Nessuna configurazione necessaria—collega semplicemente qualsiasi dispositivo con output video (HDMI, VGA, ecc.) e una porta USB per il controllo tastiera/mouse. Funziona con Windows, macOS, Linux, Android e iOS.

### 🖱 Modalità Mouse

-   **Modalità Assoluta**: Il mouse host mappa direttamente alla posizione dello schermo target.
-   **Modalità Relativa**: Muove il cursore target relativamente alla posizione corrente. Esci con una scorciatoia.

### ⌨️ Tastiera

I tasti premuti dall'host vengono inviati direttamente al target quando l'app è focalizzata.

### ⚙️ Accesso BIOS

Controlla direttamente il BIOS target.  
Tasti comuni: F2 (Dell/Lenovo/ASUS), F10 (HP), Del (ASUS/Gigabyte/MSI), ⌥ (Apple).

### 🔊 Audio

L'audio target viene trasmesso tramite HDMI e riprodotto sul tuo computer host.

### 🎥 Video

Visualizza il tuo schermo target direttamente nell'app.

-   **Modelli Attuali**: Display fino a **1080p 30Hz** nell'app, con supporto per input **4K 30Hz** tramite HDMI.
-   **Altri Input**: Compatibile con VGA, DVI, Micro HDMI e altro quando si usano adattatori appropriati.
-   **Modelli Futuri**: Risoluzioni e frame rate più alti saranno supportati quando verranno rilasciate nuove versioni hardware.

### 🔄 Porte Commutabili

Alcuni dispositivi Openterface includono porte che possono essere **commutate tra host e target**, come porte USB 2.0 o slot per schede micro-SD (su modelli futuri).

-   **Uso Uno alla Volta**: Solo un lato (host o target) può accedere alla porta alla volta.
-   **Metodi di Commutazione**:
    -   **Toggle Hardware** — interruttore fisico sul dispositivo
    -   **Pulsante Software** — controllo tramite l'app host
-   **Importante**:
    -   Espelli in sicurezza i dispositivi di archiviazione (unità USB o schede micro-SD) prima di commutare.
    -   Evita di collegare dispositivi ad alta potenza per prevenire instabilità o danni.
    -   Vedi la [Guida alle Porte Commutabili](/usb-switch) per dettagli e diagrammi logici.
