---
title: "Openterface Mini-KVM (Windows) - Guida per il controllo diagnostico hardware"
description: "Guida passo dopo passo per eseguire il controllo diagnostico hardware nell'app Openterface per Windows. Impara come testare le connessioni USB, rilevare problemi e inviare report diagnostici al supporto."
keywords: "Openterface Mini-KVM, Windows, diagnostica hardware, controllo diagnostico auto, risoluzione dei problemi KVM, diagnosi USB KVM, supporto Mini-KVM, test del dispositivo KVM, Windows KVM, segnalazione di difetti KVM, guida alla risoluzione dei problemi Mini-KVM"
---

# Openterface Mini-KVM (Windows) — Guida per il controllo diagnostico hardware

Questa guida spiega come eseguire il controllo **Diagnostica hardware** nell'app Openterface per **Windows** e come inviare il report diagnostico al supporto se viene rilevato un problema.

---

## Prima di iniziare

- Collegare Mini-KVM a **Host** e **Target**.
- Mantenere il dispositivo target inattivo durante i test (soprattutto durante il test di stress).

> **Importante (Windows):** La diagnostica **non avanza automaticamente**.  
> Per passare tra i test, usare **Avanti** (barra inferiore) **oppure** fare clic su un elemento di test nel **pannello sinistro**.  
> Ogni test viene eseguito facendo clic su **Controlla Ora**.

![next_webp](https://assets2.openterface.com/images/next.webp)

---

## Unità funzionante (PASS)

### Passaggio 1 — Aprire Diagnostica hardware (Windows)
Nell'app Openterface per Windows, aprire: **Avanzate → Diagnostica hardware**.  

### Passaggio 2 — Eseguire il controllo
Nella finestra Diagnostica hardware, fare clic su **Controlla Ora** per eseguire il passo diagnostico corrente.  

### Passaggio 3 — Target Plug & Play (seguire le istruzioni)
Quando **Target Plug & Play** chiede di riconnettere il cavo target, seguire le istruzioni sullo schermo.  
Alcune configurazioni possono richiedere di **scollegare/ricollegare più di una volta** (ad es. due volte).  

![Target-plug&play](https://assets2.openterface.com/images/Target-plug%26play.webp)

### Passaggio 4 — Host Plug & Play (seguire le istruzioni)
Seguire le istruzioni sullo schermo per il lato host.  

![Host-plug&play](https://assets2.openterface.com/images/Host-plug%26play.webp)

### Passaggio 5 — Test di stress (non toccare il target)
Durante il **Test di stress**, il mouse target può muoversi automaticamente per il rilevamento.  
**Non operare sul target** mentre il test è in esecuzione.  

> **Nota:** Il mouse potrebbe muoversi velocemente — non toccare il target.

![stress-test](https://assets2.openterface.com/images/stress-test.webp)

### Passaggio 6 — Confermare PASS
Continuare fino al completamento del controllo. Se tutto è normale, i risultati mostreranno **PASS / Tutti i test superati**.  

---

## Problema rilevato (Esempio tastiera/mouse)

Se viene rilevato un problema, uno o più elementi possono mostrare **FAIL**.

### Passaggio 1 — Eseguire la stessa Diagnostica hardware
Aprire **Avanzate → Diagnostica hardware**, quindi fare clic su **Controlla Ora** per avviare.  

### Passaggio 2 — Continuare con i controlli
Continuare con i test rimanenti fino al completamento della diagnostica.  

### Passaggio 3 — L'email di supporto si apre automaticamente
Quando la diagnostica termina con un problema, si aprirà automaticamente una finestra **Email di supporto**.  

---

## Invio dei log al supporto (Windows)

### Passaggio 4 — Applicare ID Ordine + Nome
Inserire il proprio **ID Ordine** e **Nome**, quindi fare clic su **Applica** per inserirli nella bozza dell'email. 

![ID+Name](https://assets2.openterface.com/images/ID+Name.webp)

### Passaggio 5 — Copiare indirizzo email e bozza
- Fare clic su **Copia Email** per copiare l'indirizzo email del supporto.
- Fare clic su **Copia Bozza** per copiare il contenuto dell'email precompilato (inclusi ID Ordine + Nome).  
Incollare entrambi nel client email (Gmail/Outlook/ecc.).  

![copy](https://assets2.openterface.com/images/copy.webp)

### Passaggio 6 — Allegare i file di log corretti
Fare clic su **Apri Cartella File**. Lo strumento indicherà quali file allegare.  
**Allegare solo i file di log richiesti** (la cartella può contenere molti altri log).  

![list](https://assets2.openterface.com/images/list.webp)

![compress](https://assets2.openterface.com/images/compress.webp)

### Passaggio 7 — Allegare anche una foto della configurazione
Nella stessa email, allegare una **foto chiara della configurazione** che mostri:
- il dispositivo Mini-KVM,
- entrambe le connessioni **Host** e **Target**,
- porte e cavi chiaramente visibili.  

### Passaggio 8 — Inviare l'email
Inviare l'email al supporto (testo della bozza + log richiesti + foto della configurazione allegati).  

---

## Cosa includere quando si contatta il supporto

- **ID Ordine**
- **File di log diagnostici richiesti**
- **Foto della configurazione** (Mini-KVM + cablaggio host/target)
