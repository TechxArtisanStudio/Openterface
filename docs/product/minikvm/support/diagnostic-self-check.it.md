---
title: "Openterface Mini-KVM - Guida per il controllo diagnostico auto (macOS)"
description: "Guida passo dopo passo per eseguire controlli diagnostici auto sull'apparecchio Openterface Mini-KVM con l'app macOS. Impara come testare le connessioni USB, rilevare problemi e inviare segnalazioni di difetti al supporto."
keywords: "Openterface Mini-KVM, macOS, controllo diagnostico auto, risoluzione dei problemi KVM, diagnosi USB KVM, supporto Mini-KVM, test del dispositivo KVM, test della connessione USB, segnalazione di difetti KVM, guida alla risoluzione dei problemi Mini-KVM, strumento diagnostico KVM, diagnosi per server headless, strumenti IT per la risoluzione dei problemi"
---

# Openterface Mini-KVM - Guida per il controllo diagnostico auto (macOS)

Questa guida fornisce istruzioni passo dopo passo per eseguire controlli diagnostici auto sull'apparecchio Openterface Mini-KVM.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-K6Idzky3fY?si=r7pZgCkBzzZXgrLT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Unità Buona

**Passaggio 1:** Nell'app Openterface, apri Impostazioni → Impostazioni...

**Passaggio 2:** Nella finestra delle impostazioni, vai a Avanzate e Debug.

**Passaggio 3:** Fare clic su Apri Strumento diagnostico.

**Passaggio 4:** Quando richiesto, fare clic su Abilita per attivare il registro diagnostico.

**Passaggio 5:** Fare clic su Controlla Ora per avviare il controllo auto.

**Passaggio 6:** Fare clic su Avvia Test, quindi stacca e ricollega il cavo USB-C nero (lato target) quando richiesto.

![minikvm-support-target](https://assets.openterface.com/images/minikvm/support/target.webp)

**Passaggio 7:** Fare clic su Avvia Test, quindi stacca e ricollega il cavo USB-C arancione (lato host) quando richiesto.

![minikvm-support-host](https://assets.openterface.com/images/minikvm/support/host.webp)

**Passaggio 8:** Fare clic su Avvia Test e attendi che il test venga completato.

**Passaggio 9:** Fare clic su Ripristina Ora e attendi che venga completato.

**Passaggio 10:** Fare clic su Cambia Ora e attendi che il cambio della velocità di baud termini.

**Passaggio 11:** Fare clic su Avvia Test, quindi attendi circa 30 secondi. Non operare sul target durante l'esecuzione del test.

> **Nota:** Il mouse potrebbe muoversi velocemente. Non toccare il target.

![minikvm-support-stress_test](https://assets.openterface.com/images/minikvm/support/stress_test.gif)

**Passaggio 12:** Conferma che tutti gli elementi mostrino un segno verde e che il progresso sia completo.

**Passaggio 13:** Fare clic sul ❌ (in alto a destra) per chiudere la finestra diagnostica.

---

## Problema Rilevato (Esempio Tastiera/Mouse)

Segui prima i Passaggi 1–11 in "Unità Buona". Le note di seguito spiegano ciò che vedrai quando viene rilevato un problema con la tastiera/mouse.

## Come si manifesta questo problema

In questo esempio, Connessione Generale mostra FAIL inizialmente perché un problema della tastiera/mouse (HID) sul lato target influisce sulla verifica generale. Questo è un indicatore precoce, non un problema separato (vedrai lo stato FAIL evidenziato accanto a "Connessione Generale" a sinistra).

- **Connessione Generale:** FAIL è mostrato qui inizialmente a causa del problema sul lato target.

![minikvm-support-overall_connection](https://assets.openterface.com/images/minikvm/support/overall_connection.webp)

- **Plug & Play Target:** Dopo aver eseguito questo passaggio, il risultato può mostrare più chiaramente il problema sul lato target.

> **Consiglio:** Se un passaggio mostra FAIL, le diagnosi non si fermeranno, ma potrebbe smettere di avanzare automaticamente—quindi dovrai continuare manualmente.

## Test finale extra (dipende dal tipo di problema)

**Passaggio 12:** Dopo il test a stress, le diagnosi potrebbero mostrare un test finale extra in base al problema rilevato; nell'esempio tastiera/mouse, continua con il Controllo della porta target.

**Passaggio 13:** Fare clic su "Rileva dispositivi" per iniziare il Controllo della porta target, quindi segui le istruzioni visualizzate.

![minikvm-support-target_port_checking](https://assets.openterface.com/images/minikvm/support/target_port_checking.webp)

## Cosa accade quando viene rilevato un problema

**Passaggio 14:** Per continuare, fare clic su Avanti (barra inferiore) o selezionare il test successivo dal pannello sinistro.

![minikvm-support-target_plug_n_play](https://assets.openterface.com/images/minikvm/support/target_plug_n_play.webp)

## Invio dei log al supporto

**Passaggio 15:** Fare clic su Invia Segnalazione di Difetto al Supporto per preparare il report per il supporto.

![minikvm-support-send_defect_report_to_support](https://assets.openterface.com/images/minikvm/support/send_defect_report_to_support.webp)

**Passaggio 16:** Nella finestra della Segnalazione di Difetto, inserisci il tuo **ID Ordine** e **Nome**, quindi fare clic su **Applica** per inserirli nella bozza dell'email.

**Passaggio 17:** Copia l'indirizzo email e la bozza:
- Fare clic su **Copia Email** per copiare l'indirizzo email del supporto.
- Fare clic su **Copia Bozza** per copiare il contenuto dell'email precompilato (inclusi ID Ordine + Nome).
- Incolla entrambi nel tuo client email (Gmail/Outlook/ecc.).

![minikvm-support-support](https://assets.openterface.com/images/minikvm/support/support.webp)

**Passaggio 18:** Fare clic su **Apri Cartella dei Log**. Lo strumento indicherà quali file allegare. **Allega solo i file di log richiesti** (la cartella può contenere molti altri log).

**Passaggio 19:** Nella stessa email, allega una **foto chiara della configurazione** che mostri:
- il dispositivo Mini-KVM,
- entrambe le connessioni **Host** e **Target**,
- porte e cavi chiaramente visibili.

**Passaggio 20:** Invia l'email al supporto (testo della bozza + log richiesti + foto della configurazione allegati).

**Passaggio 21:** Fare clic sul ❌ (in alto a destra) per chiudere la finestra diagnostica.