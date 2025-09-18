# Openterface Android

## Panoramica

Openterface Mini-KVM è una soluzione hardware e software open-source progettata per fornire funzionalità KVM (Keyboard, Video, Mouse) di base per controllare dispositivi tramite un'interfaccia basata su Android. Questo repository contiene il codice sorgente dell'applicazione Android, le configurazioni di build e gli script di supporto per configurare e distribuire il progetto.

Siamo impegnati nell'hardware aperto e nel software open-source, con licenza secondo la [GNU Affero General Public License v3](LICENSE).

## Moduli Funzionali

### 1. Visualizzazione Video

#### Funzionalità Principale

-   Trasmette in streaming l'output video del dispositivo target collegato sullo schermo Android in tempo reale.
-   Supporta regolazioni dell'immagine per una visione ottimale.

![image](https://assets.openterface.com/images/android/videoConnect.webp)

#### Descrizione Interfaccia Utente

-   Lo schermo principale mostra il feed video del dispositivo target, occupando la maggior parte dell'interfaccia.
-   Una barra degli strumenti laterale offre controlli di regolazione (luminosità, contrasto, tonalità).

#### Flusso Operativo

1. Collega l'hardware Mini-KVM al dispositivo target tramite HDMI e USB.
2. Collega il Mini-KVM al tuo dispositivo Android tramite USB-C.
3. Avvia l'app; il feed video apparirà automaticamente.
4. Usa i cursori nella barra degli strumenti per regolare luminosità, contrasto o tonalità secondo necessità.

![image](https://assets.openterface.com/images/android/colorSetting.webp)

#### Funzionalità Speciali

-   Zoom con due dita per migliorare la visione

![image](https://assets.openterface.com/images/android/enlargeAndSideBar.webp)

---

### 2. Controllo del Mouse

#### Funzionalità Principale

-   Fornisce controllo del mouse assoluto e relativo per interagire con l'interfaccia del dispositivo target.
-   Supporta clic sinistro e destro.
-   Seleziona la modalità dal menu laterale destro.

#### Descrizione Interfaccia Utente

-   Il feed video funge anche da touchpad per l'input del mouse.
-   Un pulsante di azione flottante (FAB) consente di alternare tra le modalità mouse e tastiera.

#### Flusso Operativo

1. Assicurati che il dispositivo sia connesso correttamente.
2. Tocca lo schermo per spostare il cursore del mouse in quella posizione (controllo assoluto).
3. Tocca due volte con un dito per clic sinistro, tocca con due dita per clic destro.
4. La modalità trascinamento consiste nel tenere premuto il pulsante sinistro senza rilasciarlo.

#### Funzionalità Speciali

-   Controllo del mouse relativo (in sviluppo, attivabile tramite le impostazioni quando disponibile).

## ![image](https://assets.openterface.com/images/android/mouseThouchMode.webp)

### 3. Input da Tastiera

#### Funzionalità Principale

-   Consente di digitare nel dispositivo cliccando sui tasti della tastiera.

#### Descrizione Interfaccia Utente

-   L'icona della tastiera si trova nell'angolo in basso a destra.
-   La tastiera include tasti di scelta rapida, tasti di sistema, tasti standard e tasti funzione (F1-F12).

#### Flusso Operativo

1. Clicca sull'icona della tastiera nell'angolo in basso a destra per visualizzare la tastiera.
2. Digita il testo o premi i tasti funzione secondo necessità.

#### Funzionalità Speciali o Scorciatoie

-   **Tasti di Scelta Rapida**: Ctrl+C、Ctrl+V、Ctrl+Z、Ctrl+X、Ctrl+A、Ctrl+S、
    Win+Tab、Win+S、Win+E、Win+R、Win+D、Win+L、Alt+F4、Ctrl+Alt+Del、Alt+PrtScr.
-   **Tasti Funzione**: F1-F12、Tasti Simbolo.
-   **Tasti Standard**: 0-9、A-Z、Invio、Spazio、Cancella.

![image](https://assets.openterface.com/images/android/enlargeAndKeyBoard.webp)
![image](https://assets.openterface.com/images/android/keyBoardFunction.webp)
![image](https://assets.openterface.com/images/android/keyBoardSystem.webp)

---

Nel frattempo, sentiti libero di esplorare il nostro **repository open-source su GitHub**: [Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) per il codice più recente, aggiornamenti, esempi e per segnalare problemi.

Puoi anche unirti alla nostra [community su Discord](/discord) per entrare in contatto con il nostro team di sviluppo e altri utenti appassionati per discutere di qualsiasi argomento relativo a KVM.

Per supporto diretto, puoi scriverci a [support@openterface.com](mailto:support@openterface.com).

---

**Hai dei commenti su questa pagina?** [Facci sapere qui.](https://forms.gle/wmxoR2C1VdG36mT69)
