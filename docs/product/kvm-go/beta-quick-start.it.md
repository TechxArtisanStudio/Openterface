# Guida rapida KVM-GO Beta

> Redatta con ❤️ da [Iker](https://github.com/IkerGarcia) della community di Openterface — grazie per aiutarci a migliorare la documentazione!

Benvenuto/a nella [beta di KVM-GO](/product/kvm-go/updates/251007-kvm-go-beta-test-kits-sent-1/)! Qui trovi una versione sintetica del questionario di feedback beta. Segui ogni sezione, annota le tue osservazioni e, al termine, invia tutto tramite il [questionario di feedback beta su Google Form](https://openterface.com/product/kvm-go/beta-questions).

Congratulazioni per essere stato/a selezionato/a come beta tester! Siamo entusiasti di ricevere il tuo riscontro: siamo certi che riuscirai a testare il dispositivo a fondo in diversi scenari.

Il test è flessibile, ma ci farebbe piacere che concentrassi l’attenzione su alcuni scenari specifici.

Il tuo feedback è estremamente prezioso. Sei libero/a di esplorare altri aspetti del dispositivo, ma questi sono gli ambiti principali su cui vorremmo focalizzarci:

1. **Test di inattività prolungata**

    1. Avvia il software e connettilo a un target
    2. Lascia il software in esecuzione senza interazione per un periodo esteso (diverse ore)
    3. Ritorna e prova a utilizzare i controlli di mouse e tastiera
    - Dopo il periodo di inattività, mouse e tastiera hanno funzionato normalmente al tuo ritorno?

2. **Test di hot-plug**

    - Prova a scollegare e ricollegare il dispositivo mentre il software è in esecuzione.

3. **Accesso al BIOS e a basso livello**

4. **Copia e incolla (testi brevi e lunghi)**

5. **Impostazioni di simulazione del dispositivo (Windows/Linux)**

    - 5.1. Configurazione EDID del display
    - 5.2. Identificazione del dispositivo USB (VID/PID)
    - 5.3. Funzionalità della scheda SD
        - Caso d’uso 1 - Installazione del sistema: consigliamo di provare Ventoy, uno strumento che permette di inserire più file ISO su una sola scheda SD e scegliere quale avviare. Hai provato a scrivere un’immagine di sistema su HOST e poi a passare a TARGET per l’installazione (senza rimuovere la scheda)?
        - Caso d’uso 2 - Trasferimento file: hai utilizzato la scheda SD per trasferire file tra HOST e TARGET?

Questi esempi corrispondono ad alcune domande contenute nel modulo di feedback beta e sono accompagnati da richieste di informazioni generali sulla coerenza di audio/video/tastiera/mouse o sulla gestione del calore.

Grazie per il tuo aiuto!

!!! reminder "Non dimenticare"
    Invia le osservazioni complete tramite Google Form in modo che il team possa esaminarle rapidamente.

