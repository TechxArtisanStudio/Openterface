---
title: "Risoluzione problemi controllo tastiera e mouse - Openterface Mini-KVM"
description: "Guida alla risoluzione dei problemi per i problemi di controllo tastiera e mouse di Openterface Mini-KVM. Scopri come risolvere problemi di comunicazione HID, connessioni cavo errate, problemi hub USB e stati zombie del chip HID."
keywords: "Openterface Mini-KVM, risoluzione problemi tastiera mouse, problemi HID KVM, tastiera mouse non funziona, supporto Mini-KVM, risoluzione problemi USB KVM, reset chip HID, problemi controllo KVM, tastiera mouse non risponde, risoluzione problemi Openterface, problemi dispositivo KVM, problemi hub USB, velocità baud KVM, errori comunicazione seriale"
---

# **Risoluzione dei problemi di tastiera e mouse che non riescono a controllare il computer di destinazione**

Occasionalmente, gli utenti possono riscontrare situazioni in cui le funzioni di tastiera e mouse del dispositivo Openterface non funzionano come previsto. Questo documento descrive le cause più comuni e come risolverle o prevenirle.

**Feedback del software:** Quando Openterface non riesce a stabilire la comunicazione HID a causa di una connessione di destinazione mancante o errata, l'interfaccia utente evidenzia lo stato in modo da poter agire rapidamente.

- Su **macOS**, l'icona della tastiera e del mouse nell'angolo in alto a destra dell'utility Openterface diventa **arancione**.  

    <img src="https://assets.openterface.com/images/software/inactive_keyboardmoue_macos.webp" alt="Inactive keyboard and mouse (macOS)" width="200" />

- Su **Windows/Linux**, l'icona corrispondente nella parte inferiore della finestra diventa **rossa**.  

    <img src="https://assets.openterface.com/images/software/inactive_keyboardmoue_windows.webp" alt="Inactive keyboard and mouse (Windows)" width="200" />

Il video viene ancora visualizzato in Openterface ma la tastiera e il mouse non rispondono — puoi vedere il desktop di destinazione ma non controllarlo. Di solito significa che la comunicazione HID non è stata stabilita (ad esempio, cavo di destinazione errato, hub senza alimentazione o chip HID difettoso); controlla l'elenco di controllo e le sezioni di seguito. Il software blocca anche ulteriori connessioni di tastiera/mouse fino a quando il cablaggio/il problema non viene risolto.

---

## **1. Connessione del cavo errata**

**Problema:**  
Sorprendentemente comune: gli utenti dimenticano di collegare la porta Openterface Target Type-C al computer di destinazione.

**Soluzione:**  
✅ Verificare sempre:
- Il **cavo Target Type-C** è collegato saldamente dalla **porta Target** di Openterface al **computer di destinazione** che desideri controllare.
- Il **cavo USB-A/USB-C host** è collegato al tuo **computer host/controller** (dove viene eseguito OpenterfaceQt o il software di controllo).

> **Suggerimento:** Etichettare i cavi per evitare confusione in configurazioni complesse.
- Collegare il cavo nero al lato nero del connettore di destinazione.
- Collegare il cavo arancione al lato coperto di arancione del connettore di destinazione.


## **2. Utilizzo di hub USB senza alimentazione**

**Problema:**  
Il collegamento di Openterface tramite un hub USB senza alimentazione può causare un **insufficiente apporto di energia** (calo della tensione VBUS). Ciò potrebbe causare il malfunzionamento del dispositivo o l'impossibilità di inizializzare le funzioni HID (tastiera/mouse).

**Soluzione:**  
✅ **Evitare hub USB senza alimentazione** tra Openterface e il computer di destinazione.  
✅ Se è necessario un hub, utilizzare un **hub USB di alta qualità alimentato esternamente** in grado di fornire un'alimentazione stabile a 5 V.

> **Nota:** L'alimentazione USB è fondamentale per il funzionamento affidabile del chip HID. I cali di tensione possono attivare guasti interni.

---

## **3. Il chip HID entra nello "stato zombie"**

**Problema:**  
In determinate condizioni — ad esempio rapidi burst di comandi combinati con alimentazione marginale — il chip HID interno (ad esempio CH9329) può entrare in uno **"stato zombie".** In questo stato:
- Il chip HID si blocca e interrompe l'invio di dati di risposta seriale al computer host.
- Mantiene uno stato di errore interno che impedisce la reinizializzazione normale da parte del software host.
- Il dispositivo potrebbe apparire collegato (video presente) mentre gli input rimangono non responsivi.
- Il software host (ad esempio OpenterfaceQt) non può reinizializzare correttamente il dispositivo.
- Il ricablaggio di tutti i cavi o il ciclo di alimentazione della connessione USB in genere non cancellano questo errore interno; è necessario un ripristino dei valori di fabbrica del chip HID.

**Soluzione:**  
Eseguire un **ripristino dei valori di fabbrica del chip HID**:

- Su **macOS**: Utilizza il **Serial Reset Tool** disponibile nel **Menu Avanzate** dell'utility macOS.  

    <img src="https://assets.openterface.com/images/software/MacOS_FactoryResetHID.webp" alt="Serial Reset Tool (macOS)" width="150" />

- In **OpenterfaceQt** (app desktop): Vai a **Menu Avanzate → Ripristino valori di fabbrica chip HID**.

    <img src="https://assets.openterface.com/images/software/OpenterfaceQT_FactoryResetHID.webp" alt="Factory Reset HID Chip (OpenterfaceQt)" width="150" />

> Questo cancella lo stato interno del chip e ripristina il funzionamento normale.

---

## **4. Sensibilità della velocità in baud in ambienti rumorosi**

**Problema:**  
Openterface utilizza per impostazione predefinita una velocità in baud di **115200 bps** per una trasmissione dati mouse più veloce. Tuttavia, in ambienti elettricamente rumorosi (ad esempio, alimentatori a commutazione o cavi lunghi/non schermati), questo elevato baud rate può causare **errori di comunicazione seriale**, causando la perdita o la corruzione dei comandi HID.

**Soluzione:**  
Passa a una velocità in baud di **9600 bps**:
- Ciò migliora significativamente l'**affidabilità della comunicazione** in configurazioni rumorose.
- L'impatto sulla latenza è **trascurabile** con un utilizzo tipico (ad esempio, acquisizione video a 30 fps e controllo).

> **Raccomandazione:** Se riscontri anomalie di input intermittenti senza problemi di alimentazione o connessione, prova a ridurre la velocità in baud nella configurazione di Openterface.

---

## **Elenco di controllo riepilogativo**

Se la tastiera/il mouse non funziona:

1. ✅ Conferma che il **cavo Target Type-C** corretto sia collegato al **computer di destinazione**.
2. ✅ Evitare hub USB senza alimentazione — utilizzare una connessione diretta o un **hub alimentato**.
3. ✅ Se il dispositivo sembra "bloccato", **ripristina il chip HID** tramite software.
4. ✅ In ambienti instabili, **riduci la velocità in baud a 9600** per una comunicazione più robusta.
5. ✅ Se i tentativi precedenti non aiutano, prova una porta USB diversa sull'host o riavvia il computer host — il sistema operativo potrebbe disabilitare una porta o l'hub dopo aver ricevuto troppi pacchetti di errore USB. Il passaggio a porte diverse o il riavvio dell'host ripristina solitamente la connessione.

---

Affrontando questi quattro settori, la maggior parte dei problemi HID intermittenti può essere prevenuta o risolta rapidamente. Per i problemi persistenti, contattare il supporto (support@openterface.com) con i dettagli della configurazione e i registri.
