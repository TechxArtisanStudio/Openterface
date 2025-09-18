# FAQ per le App

Benvenuti alle FAQ per le nostre app. Se non trovate la risposta di cui avete bisogno, **inviateci un'email a [info@openterface.com](mailto:info@openterface.com)** o **unitevi alla nostra comunità** su [Discord](/discord) o [Reddit](/reddit) per connettervi con il nostro team di sviluppo e altri utenti.

⚠️ *Le FAQ potrebbero diventare obsolete — fateci sapere se notate qualcosa che ha bisogno di essere aggiornato!*

### :material-clipboard-list: Elenco delle Domande

- [Dove posso scaricare le applicazioni host?](#host-app-download)
- [Perché le funzionalità differiscono tra diverse app host?](#host-app-differences)
- [Quale app host offre attualmente la migliore esperienza?](#best-host-app)
- [C'è un'app host che supporta ChromeOS?](#host-app-chromeos)
- [C'è un'app host che supporta i dispositivi mobili di Apple?](#host-app-ios)
- [Cosa fare se F11 non funziona nelle applicazioni macOS?](#f11-macos-issue)

#### :material-chat-question:{ .faq } Dove posso scaricare le applicazioni host? {: #host-app-download }

Visitate la nostra [pagina di installazione applicazione host](/quick-start/#install-host-application) per i download ufficiali che supportano **MacOS, Windows, Linux e Android**.

??? warning "Privacy e Sicurezza: Fate attenzione quando usate app host di terze parti"
    Poiché il nostro progetto è open source, potreste trovare versioni alternative di applicazioni host compatibili con il nostro Mini-KVM sviluppate da altri. Mentre queste possono offrire funzionalità aggiuntive, assicuratevi di rivedere le loro pratiche di sicurezza e privacy. **Il team Openterface non può garantire o essere responsabile per la sicurezza delle applicazioni di terze parti**.

#### :material-chat-question:{ .faq } Perché le funzionalità differiscono tra diverse app host? {: #host-app-differences }

Il nostro team di sviluppo mantiene attivamente applicazioni host per macOS, Linux, Windows e Android, ma a causa delle sfide specifiche della piattaforma e risorse limitate, i progressi di sviluppo variano. Questo significa che alcune funzionalità potrebbero apparire prima su una piattaforma e impiegare più tempo ad arrivare su altre.

Stiamo facendo del nostro meglio per sincronizzare lo sviluppo delle funzionalità su tutte le piattaforme, ma è un lavoro in corso.

Il vostro feedback gioca un ruolo importante nel plasmare la nostra roadmap di sviluppo — sia attraverso la nostra [comunità](/community/) che il nostro [repository GitHub](/app/). Ogni suggerimento ci aiuta a prioritizzare ciò che conta di più per voi!

Se siete sviluppatori, i vostri contributi sono incredibilmente preziosi — e ci piacerebbe il vostro aiuto per accelerare il processo!

#### :material-chat-question:{ .faq } Quale app host offre attualmente la migliore esperienza? {: #best-host-app }

A marzo 2025, le app host basate su Qt per Windows e Linux offrono l'insieme di funzionalità più completo nel complesso. La versione macOS si distingue per la sua esperienza utente più fluida e raffinata, grazie a un'integrazione di sistema più profonda e miglioramenti dell'interfaccia utente. L'app Android è un'opzione conveniente in movimento, con più funzionalità che stanno recuperando costantemente.

#### :material-chat-question:{ .faq } C'è un'app web che posso usare su Chrome o altre piattaforme? {: #host-app-chromeos }

Sì! Uno dei nostri fantastici membri della comunità, [Kashall](https://github.com/kashalls/openterface-viewer/), ha costruito **un'app web open source leggera** che potete usare direttamente nel vostro browser: [openterface-viewer.pages.dev](https://openterface-viewer.pages.dev). Non è ancora parte della nostra documentazione ufficiale, ma il nostro team di sviluppo l'ha provata e l'ha trovata solida, facile da usare e super pratica — specialmente su Chrome o quando volete qualcosa di veloce e basato su browser. Provatela!

#### :material-chat-question:{ .faq } C'è un'app host che supporta i dispositivi mobili di Apple? {: #host-app-ios }

Stiamo attualmente esplorando la compatibilità con i sistemi mobili di Apple, come iOS e iPadOS. A causa dei controlli rigorosi di Apple, queste piattaforme potrebbero non supportare connessioni cablate con dispositivi di terze parti. Tuttavia, la situazione potrebbe cambiare, o potrebbero esserci potenziali soluzioni alternative. Se avete intuizioni o suggerimenti, vi invitiamo a unirvi alla nostra comunità per discuterne con noi. Siamo impegnati a migliorare la convenienza del nostro dispositivo supportando il maggior numero di sistemi possibile. Se siete desiderosi di aiutare con il nostro sviluppo, venite a passare del tempo con noi nella comunità o inviateci un'email!

#### :material-chat-question:{ .faq } Cosa fare se F11 non funziona nelle applicazioni macOS? {: #f11-macos-issue }

Su macOS, premere F11 mostra il desktop macOS invece di passare il tasto F11 all'app e al computer target. Per risolvere questo, potete scollegare F11 dalla funzione "Mostra Desktop".

???+ info "Risoluzione del problema del tasto F11 su macOS"
    1. Andate a **Impostazioni di Sistema**.
    2. Selezionate **Desktop e Dock**.
    3. Scorrete verso il basso e cliccate sul pulsante **"Scorciatoie…"**.
    4. Trovate **"Mostra Desktop"** e impostatelo sul trattino **(-)** in fondo alla lista a discesa.
    5. Questa modifica permetterà al tasto F11 di passare alla vostra applicazione sul computer target.
