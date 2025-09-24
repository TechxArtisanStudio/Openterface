---
draft: false
date: 2024-08-22
description: "Aggiornamento importante Openterface Mini-KVM: certificazione CE completata, produzione in corso, nuova ETA metà gennaio. Hardware V1.9 finalizzato con pin di espansione, sviluppo app Android, imballaggio migliorato e manuale multilingue in corso."
keywords: "Openterface Mini-KVM, certificazione CE, hardware V1.9, aggiornamento produzione, timeline spedizione, sviluppo app Android, pin espansione, KVM-over-IP, controllo qualità, imballaggio prodotto, manuale multilingue, USB KVM, produzione tech, hardware open source, aggiornamento consegna"
---

# Superare gli ostacoli: Aggiornamento progressi e nuova timeline

Ciao a tutti,

Spero che stiate tutti bene. È passato un po' di tempo dal nostro ultimo aggiornamento. Vorrei poter dire che tutto è andato liscio per Openterface, ma abbiamo incontrato alcuni ostacoli che ritarderanno la nostra timeline di consegna. Anche se questo non era quello che ci aspettavamo, stiamo affrontando queste sfide a testa alta e facendo progressi costanti con molte buone notizie da condividere. Questo post è una **lettura di 7 minuti**, quindi tuffiamoci nei dettagli così sapete esattamente dove stanno le cose e cosa viene dopo.

## Regolamentazione, produzione e qualità

Prima di poter avviare la produzione, dovevamo superare i test di qualità necessari secondo le regolamentazioni, in particolare la certificazione CE. Poiché la nostra versione toolkit include non solo il Mini-KVM ma anche diversi accessori, ogni parte doveva sottoporsi ai test CE. Questi test hanno richiesto più tempo del previsto (si scopre che i cavi possono essere piuttosto esigenti), ma la buona notizia è che **abbiamo superato la CE per il nostro Mini-KVM e tutti i suoi componenti!** Di seguito è una panoramica delle certificazioni per tutte le nostre parti: Mini-KVM, cavo HDMI, cavo Type-C arancione, cavo Type-C corto nero e cavo VGA2HDMI. Con la certificazione in mano, la nostra timeline di produzione è ora certa, e i nostri produttori stanno **attualmente producendo tutte le parti** mentre parlo.

![240823-0](https://www.crowdsupply.com/img/fcb5/db59e179-2413-4d57-8462-2285c007fcb5/openterface-240823-0_jpg_gallery-lg.jpg)
*I requisiti UKCA e CE sono gli stessi per i nostri prodotti elettronici, con CE che copre anche la conformità RoHS.*

Due settimane fa, abbiamo visitato uno dei nostri produttori per formare i loro responsabili di linea sul controllo qualità per i cavi arancioni prima che li spedissero a noi. Ora, TUTTI i cavi arancioni sono stati prodotti e sono seduti in un angolo del nostro studio.
![240823-1](https://www.crowdsupply.com/img/28dc/34844b54-0e02-414d-b58b-d40e8abe28dc/openterface-240823-1_jpg_gallery-lg.jpg)
*Kevin e Shawn stavano spiegando i metodi di test per assicurarsi che il cavo arancione funzioni correttamente con il nostro Openterface Mini-KVM.*

Faremo lo stesso compito questa settimana per formare QA in prima linea di produzione anche per le altre parti. Ecco campioni di cavi aggiuntivi.
![240823-2](https://www.crowdsupply.com/img/e703/abb8ffa5-eb85-4eb9-b5f8-d8a3d349e703/openterface-240823-2_jpg_md-xl.jpg)
*Orgogliosamente marchiati con il nostro logo TechxArtisan, questi sono campioni del cavo HDMI, del cavo Type-C corto e del cavo VGA-to-HDMI.*

Ci aspettiamo che le altre parti e Mini-KVM arrivino presto dai nostri produttori, momento in cui ricontrolleremo la qualità di ogni componente e li imballeremo correttamente nel nostro studio prima della spedizione. In altre parole, **il nostro team assicurerà personalmente la qualità** prima che raggiunga le vostre mani.

## Spedizione, potenziali ritardi e nuova ETA

**L'incertezza attuale risiede nel processo di spedizione**. Dopo aver investigato diverse compagnie di spedizione, abbiamo scoperto che la spedizione richiederà tempo extra poiché probabilmente trasferiremo i pacchi attraverso un magazzino prima di raggiungere il magazzino di Crowd Supply. Stiamo ancora discutendo se scegliere il trasporto marittimo o aereo—per favore abbiate pazienza per qualche altro giorno mentre sistemiamo gli accordi.

Lo sdoganamento è un altro ostacolo potenziale che potrebbe causare ritardi inaspettati. Una volta che i nostri prodotti arrivano al magazzino di Crowd Supply negli Stati Uniti, impiegheranno una o due settimane per essere spediti globalmente basandosi su ogni ordine. Per i sostenitori fuori dagli Stati Uniti, i pacchi individuali dovranno ancora passare attraverso la spedizione globale e lo sdoganamento nel paese di destinazione.

Considerando la situazione attuale e aggiungendo un po' di tempo di buffer, rimango cautamente ottimista che completeremo la consegna prima della fine di quest'anno, con **una nuova ETA di metà gennaio**. Mi dispiace davvero per l'inconveniente e apprezzo il vostro supporto e pazienza durante questo cambiamento.

## Hardware V1.9 finalizzato

Come potreste sapere dal nostro precedente [post Reddit](https://www.reddit.com/r/Openterface_miniKVM/comments/1e25pco/openterface_minikvm_v19_with_pins_for_more/), abbiamo deciso di **aggiornare il nostro hardware a V1.9**, includendo un set di pin di espansione hackabili. Questo non faceva parte del piano originale per la campagna di crowdfunding, ma crediamo che migliori significativamente il **potenziale per un uso più ampio** dell'hardware.

![240823-3](https://www.crowdsupply.com/img/77d7/09a9d0e5-3065-4f3e-8b61-bae66b5c77d7/openterface-240823-3_jpg_md-xl.jpg)
*I pin VCC, GND, Target D+, Target D-, Host D+ e Host D-—dove 'D' sta per dati USB.*

Una motivazione chiave era quella di **permettere al commutatore USB di essere commutato a livello software**. Perché è importante? Nella nostra roadmap, **miriamo a supportare una soluzione KVM-over-IP**, come VNC, in futuro. L'idea è di abbinare il controllo KVM locale con il protocollo VNC, permettendo agli utenti di controllare il computer target tramite il computer host. In un tale scenario remoto, la capacità per gli utenti di commutare la porta USB è essenziale, specialmente quando sono richiesti trasferimenti di file tra host e target.

**I pin di espansione aprono anche possibilità per altro**, come l'integrazione con iPadOS, controllo ATX, bridging di rete e bypass audio. Anche se non approfondirò tutti i dettagli qui, vi incoraggio a unirvi alla nostra comunità Openterface per discutere ulteriormente con noi.

Questo aggiornamento hardware potrebbe potenzialmente estendere la nostra soluzione Openterface per operare su IP e includere funzionalità più avanzate mantenendo ancora la sua forza centrale come strumento KVM-over-USB plug-and-play—perfetto per i professionisti IT che navigano ambienti IT incerti, come data center non familiari.

Sono felice di riportare che V1.9 ha superato i nostri test interni di base e sarà finalizzato come la versione ufficiale per tutti i nostri sostenitori. Tuttavia, questo aggiornamento hardware richiederà ulteriori test, e qualsiasi sviluppo basato su questi pin di espansione sarà sperimentale e probabilmente avrà bug. È qui che potete contribuire. Contiamo sulla comunità open-source per aiutarci a migliorare Openterface insieme.

## Più aggiornamenti software

Sul fronte software, stiamo facendo progressi entusiasmanti. Stiamo ora immergendoci nell'**app Openterface Android**! Date un'occhiata a questo [tweet](https://x.com/TechxArtisan/status/1825460088922071398) per una demo iniziale che mostra controllo KVM fluido, movimento del mouse e clic in azione. Più funzionalità sono in arrivo, e come sempre, una volta che avremo lucidato un po' di più il codice, **questa app sarà anche open-sourced** nel nostro repo GitHub [Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android).
![240823-4](https://www.crowdsupply.com/img/7007/b192f260-1e1f-4dab-905b-fb0a6d927007/openterface-240823-4_jpg_md-xl.jpg)
*Usando solo le nostre punte delle dita per controllare KVM un computer Linux da un tablet Android. Bello!*

La nostra versione QT ha appena ricevuto un aggiornamento utile—ora potete [trasferire testo dall'host al target](https://x.com/TechxArtisan/status/1825919721960780131)! Quindi ora questa funzionalità è supportata sulle app host macOS, Windows e Linux.

Inoltre, stiamo anche pianificando di aggiungere una funzionalità divertente—[un movimento automatico del mouse per prevenire che il vostro computer target si addormenti](https://x.com/TechxArtisan/status/1825471186668847241). Dovremmo andare con la pallina da ping-pong che rimbalza intorno allo schermo o l'effetto classico dello screensaver DVD? Votate e commentate il [tweet](https://x.com/TechxArtisan/status/1825470086800691459) 😃

## Design del pacchetto, etichettatura e manuale

Abbiamo [sperimentato con vari mock-up e design di imballaggio](https://www.reddit.com/r/Openterface_miniKVM/comments/1elm4vq/almost_ready_to_finalize_our_package_design/) per trovare l'equilibrio perfetto tra diversi fattori chiave:

- Selezionare materiali abbastanza robusti per proteggere il prodotto e le sue parti durante la spedizione,
- Creare etichettatura informativa che aiuti gli utenti a capire il prodotto a colpo d'occhio,
- Assicurare conformità alle regolamentazioni,
- Rendere l'imballaggio visivamente attraente,
- Ed essere eco-friendly minimizzando l'uso di plastica ovunque possibile.

Inoltre, abbiamo fatto diversi miglioramenti alla vecchia borsa toolkit, inclusi:

- Spazio di stoccaggio più grande,
- Cerniera arancione elegante,
- Materiali esterni e interni aggiornati,
- E una tasca mesh super elastica.

Abbiamo scelto questo materiale perché colpisce l'equilibrio ideale tra essere economico, piacevole al tatto e abbastanza duraturo per proteggere gli articoli all'interno. **Siamo fiduciosi che lo amerete**.

![240823-5](https://www.crowdsupply.com/img/099a/75e16f52-bd0c-4652-af27-08caf448099a/openterface-240823-5_jpg_md-xl.jpg)

Stiamo anche aggiornando le etichette sul contenitore in alluminio per renderle il più informative e visivamente attraenti possibile. Speriamo che questi miglioramenti miglioreranno la vostra esperienza utente e renderanno più facile iniziare con Openterface.

![240823-6](https://www.crowdsupply.com/img/94d8/441a5757-2d6a-4c79-885b-7b5b3a7094d8/openterface-240823-6_jpg_md-xl.jpg)

Stiamo finalizzando il manuale Openterface, che sarà disponibile in inglese, tedesco, francese, giapponese e cinese. Scusate se abbiamo perso la vostra lingua—la nostra scatola non è di dimensioni TARDIS (la scatola della polizia del Doctor Who)! Ma faremo del nostro meglio per aggiungere più traduzioni sul nostro sito web.

![240823-7](https://www.crowdsupply.com/img/e2d9/2e5a2086-20f0-47ec-a27b-288d10d0e2d9/openterface-240823-7_jpg_md-xl.jpg)

## Revisione linguistica della comunità

Ho usato ChatGPT per assistere con le traduzioni, ma a volte può mancare il bersaglio con frasi e scelta delle parole. Se non è troppo disturbo, apprezzerei molto qualsiasi aiuto nel rivedere il contenuto in altre lingue, specialmente per i materiali stampati che stiamo per finalizzare. Ho aggiornato tutto il contenuto testuale per l'imballaggio nella nostra cartella GitHub [product-printed-materials](https://github.com/TechxArtisanStudio/Openterface/tree/main/product-printed-materials), dove potete rivedere e sottomettere qualsiasi miglioramento. Potete anche DMarmi direttamente. Grazie!

## Osservazioni finali e progressi in corso

Ci scusiamo ancora per i ritardi e il cambiamento nell'ETA del nostro prodotto. Grazie per la vostra pazienza e per rimanere con noi—stiamo lavorando sodo per portarvelo il prima possibile! Vi aggiornerò immediatamente una volta che la nostra spedizione sarà organizzata. Più aggiornamenti sono in arrivo, quindi unitevi alla nostra comunità Openterface e rimanete sintonizzati!

Saluti,

Billy Wang  
Product Manager  
Team Openterface | TechxArtisan
