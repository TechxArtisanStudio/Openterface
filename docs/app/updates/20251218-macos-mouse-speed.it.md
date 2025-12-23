---
title: Velocità del mouse e prestazioni di gioco di Openterface Mini-KVM su macOS
description: Test completi delle prestazioni del mouse orientati al gaming per Openterface Mini-KVM su macOS. Confronto tra le modalità mouse Absolute, Relative Event e Relative HID, con baud rate di 9600 vs 115200, per una configurazione di gioco ottimale.
keywords: Openterface Mini-KVM, velocità del mouse, prestazioni di gioco, macOS KVM, frequenza di polling del mouse, mouse da gaming, modalità mouse HID, modalità mouse assoluta, modalità mouse relativa, baud rate 115200, baud rate 9600, KVM gaming, mouse a bassa latenza, test mouse da gaming, prestazioni mouse macOS, throughput seriale, latenza del mouse, configurazione di gioco, gaming competitivo, reattività del mouse
author: Openterface
date: 2025-12-18
tags:
  - gaming
  - mouse-performance
  - macOS
  - Mini-KVM
  - technical-review
  - hardware-testing

---

# Velocità del mouse e prestazioni di gioco di Openterface Mini-KVM su macOS

### Analisi del comportamento del mouse orientata al gaming

Questo articolo riassume i test di prestazioni del mouse in condizioni reali per **Openterface Mini-KVM su macOS**, con particolare attenzione al **comportamento del mouse nei giochi**, ai limiti del baud rate seriale e alle configurazioni consigliate.

<blockquote class="twitter-tweet" data-media-max-width="560"><p lang="en" dir="ltr">Gaming isn't the main goal of Openterface KVMs, but we pushed them to explore the limits of KVM-over-USB. On macOS, 115200 baud + Relative HID gives the best mouse latency. Built for setup and debugging, tuned to stretch performance further. <a href="https://t.co/ianurD9ArL">pic.twitter.com/ianurD9ArL</a></p>&mdash; TechxArtisan (@TechxArtisan) <a href="https://twitter.com/TechxArtisan/status/2003418343806742992?ref_src=twsrc%5Etfw">December 23, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

## 1. Software e ambiente di test

### Software

* **Applicazione host:**
  **Openterface per macOS v1.21** *(in fase di sviluppo)*

* **Strumento di misurazione lato target:**
  Una **applicazione interna personalizzata**, sviluppata per misurare con precisione gli input del mouse ad alta frequenza e i tassi di elaborazione degli eventi sul sistema target.

> ⚠️ Poiché la versione v1.21 è ancora in sviluppo attivo, alcuni comportamenti e caratteristiche delle prestazioni potrebbero migliorare nelle versioni future.

---

### Condizioni di test: limitazione della velocità del mouse

**Non è stata applicata alcuna limitazione della velocità del mouse né alcun limite artificiale di frequenza** durante i test.

L’input del mouse è stato acquisito e inoltrato alla **velocità nativa del dispositivo**, ed è stato limitato solo da:

* Frequenza di polling hardware del mouse
* Modalità mouse selezionata (Absolute / Relative Event / Relative HID)
* Baud rate seriale
* Gestione dell’input del mouse da parte del sistema operativo target

---

## 2. Nozioni di base sul throughput dei dati del mouse

Ogni evento di movimento del mouse trasmesso tramite Mini-KVM è composto da:

```
11 byte = 88 bit
```

### Throughput seriale teorico

| Baud Rate | Eventi max / secondo |
| --------- | -------------------- |
| 9600      | ~109 eventi/s        |
| 115200    | ~1309 eventi/s       |

⚠️ Questi valori rappresentano **limiti teorici superiori**.
Le prestazioni reali sono influenzate da:

* Frequenza di polling del mouse sull’host
* Modalità mouse (Assoluta vs Relativa)
* Pianificazione degli eventi di input in macOS
* Buffering seriale e gestione del firmware
* **Frequenza di polling del mouse sul sistema target**, che può influenzare significativamente la reattività percepita (ad esempio, valori predefiniti bassi su alcune distribuzioni Linux)

---

## 3. Risultati dei test

---

### A. Modalità mouse assoluta (9600 e 115200 baud)

| Tipo di mouse | Baud Rate | Frequenza host (Hz) | Frequenza target (Hz) | Note                                                                  |
| ------------- | --------- | ------------------- | --------------------- | --------------------------------------------------------------------- |
| Bluetooth     | 9600      | ~125                | ~75                   | Banda seriale saturata; input in coda, movimento ritardato            |
| Cablato       | 9600      | ~150                | ~75                   | Banda seriale saturata; input in coda, movimento ritardato            |
| Gaming        | 9600      | ~1000               | ~75                   | Input ad alta frequenza fortemente accodati; reattività molto ridotta |
| Bluetooth     | 115200    | ~125                | ~125                  | Mappatura stabile 1:1 host–target                                     |
| Cablato       | 115200    | ~175                | ~175                  | Throughput migliorato; latenza percepibile nei movimenti rapidi       |
| Gaming        | 115200    | ~1000               | ~350                  | Raggiunto il limite del throughput seriale; input in eccesso accodati |

**Conclusione (modalità assoluta):**

La modalità mouse assoluta scala con il baud rate, ma rimane limitata dal **throughput seriale e dal buffering degli input**.
A **9600 baud**, tutti i tipi di mouse sono colli di bottiglia e i movimenti risultano ritardati.
A **115200 baud**, i mouse standard mostrano un comportamento stabile, ma **i mouse da gaming con polling elevato superano comunque la banda disponibile**, introducendo latenza.

**La modalità assoluta è adatta al controllo desktop, non al gaming sensibile alla latenza.**

---

### B. Modalità Relative Mouse Event

La modalità Relative Mouse Event acquisisce **gli eventi di movimento del mouse direttamente dalla finestra del sistema operativo**, calcola il **delta di movimento tra posizioni consecutive del cursore** e invia al sistema target solo i dati di movimento relativo.

Questa modalità:

* **Non richiede permessi di sistema aggiuntivi**
* È indipendente dalle **coordinate assolute dello schermo**
* Beneficia di una **finestra di cattura più ampia**, consentendo delta di movimento più precisi
* Evita il buffering delle posizioni assolute, ottenendo **minore latenza e migliore reattività**

#### Prestazioni della modalità Relative Mouse Event

| Tipo di mouse | Baud Rate | Frequenza host (Hz) | Frequenza target (Hz) | Note                                                            |
| ------------- | --------- | ------------------- | --------------------- | --------------------------------------------------------------- |
| Bluetooth     | 9600      | ~100                | ~90                   | Vicino al limite seriale; stabile per uso occasionale           |
| Cablato       | 9600      | ~125                | ~90                   | Banda seriale saturata; latenza minima                          |
| Gaming        | 9600      | ~1000               | ~100                  | Polling elevato oltre la banda; input compressi                 |
| Bluetooth     | 115200    | ~125                | ~125                  | Mappatura 1:1 host–target                                       |
| Cablato       | 115200    | ~180                | ~150                  | Throughput migliorato; tracciamento fluido                      |
| Gaming        | 115200    | ~1000               | ~450                  | Migliori prestazioni osservate; limitate dal throughput seriale |

🔴 **9600 baud è insufficiente per mouse da gaming ad alto polling**
🟢 **115200 baud consente input reattivi di livello gaming in modalità Relative Event**

---

### C. Modalità Relative Mouse HID

La modalità Relative Mouse HID **converte direttamente l’input HID del mouse di macOS in eventi HID sul sistema target**, bypassando l’elaborazione del cursore a livello di finestra e la mappatura delle coordinate assolute.

Questa modalità:

* Opera su **eventi del mouse grezzi a livello HID**
* **Non dipende dalla dimensione della finestra dell’applicazione**
* Preserva le **caratteristiche native di polling del mouse**
* Riduce al minimo buffering e traduzioni intermedie
* Fornisce la **latenza più bassa** tra tutte le modalità del mouse

Di conseguenza, la modalità Relative Mouse HID offre un comportamento **più vicino a una connessione USB diretta del mouse**, specialmente a baud rate elevati.

#### Prestazioni della modalità Relative Mouse HID

| Tipo di mouse | Baud Rate | Frequenza host (Hz) | Frequenza target (Hz) | Note                                               |
| ------------- | --------- | ------------------- | --------------------- | -------------------------------------------------- |
| Bluetooth     | 9600      | ~100                | ~90                   | Vicino al limite seriale; accettabile per uso base |
| Cablato       | 9600      | ~250                | ~180                  | Banda seriale parzialmente saturata                |
| Gaming        | 9600      | >1000               | ~90                   | Polling elevato oltre la banda disponibile         |
| Bluetooth     | 115200    | ~160                | ~155                  | Quasi mappatura 1:1 host–target                    |
| Cablato       | 115200    | ~250                | ~150                  | Stabile e reattivo                                 |
| Gaming        | 115200    | >1000               | ~500                  | Migliori prestazioni complessive; limite seriale   |

**Punti chiave (modalità Relative HID):**

* Offre la **latenza più bassa** tra tutte le modalità del mouse
* A **9600 baud**, i mouse ad alto polling restano limitati dalla banda
* A **115200 baud**, i mouse da gaming raggiungono **centinaia di eventi al secondo sul target**
* **Fortemente consigliata per il gaming e i movimenti rapidi della visuale**

---

### D. Mouse diretto su Windows (riferimento)

| Tipo di mouse   | Frequenza target (Hz) |
| --------------- | --------------------- |
| Mouse Bluetooth | 80–85                 |
| Mouse cablato   | 120–125               |
| Mouse da gaming | >1000                 |

Questo riferimento mostra che **Mini-KVM (115200 baud, modalità Relative HID)** può avvicinarsi alle prestazioni native di un mouse cablato, pur non potendo eliminare completamente l’overhead intrinseco del KVM e del trasporto seriale.

---

## 4. Configurazione consigliata per il gaming

### ✅ Consigliato

* **Modalità mouse:** Relative Mouse HID
* **Baud rate:** 115200
* **Tipo di mouse:** Cablato o mouse da gaming
* **Frequenza di polling:** ≤1000 Hz consigliata

### ❌ Da evitare

* Modalità mouse assoluta per il gaming
* 9600 baud con mouse ad alto polling
* Frequenze di polling eccessivamente elevate senza sufficiente banda seriale

---

## 5. Aspettative importanti

Openterface Mini-KVM è progettato principalmente per:

✔ Interazione BIOS / UEFI
✔ Configurazione e debug di sistema
✔ Accesso e gestione remota

Sebbene **il gaming sia possibile**, Mini-KVM **non sostituisce un mouse da gaming USB diretto**, soprattutto per titoli altamente competitivi o sensibili alla latenza.

---

## 6. Riepilogo finale

* **Il gaming con Openterface Mini-KVM è possibile** se configurato correttamente

* La reattività nei giochi è dominata da **modalità del mouse, frequenza di polling e baud rate**, non dalle prestazioni della CPU host

* La **modalità mouse assoluta** privilegia l’accuratezza posizionale ed è inadatta al gaming

* **9600 baud** impone un limite rigido alla banda di input

* **La modalità Relative Mouse HID a 115200 baud** offre il miglior equilibrio tra:

  * Frequenza di input
  * Latenza
  * Stabilità

* Sebbene Mini-KVM non possa eguagliare completamente una connessione USB nativa, può offrire un’**esperienza giocabile e reattiva** per il gaming casual e alcuni scenari competitivi

---

### Verdetto finale

✅ **Tecnicamente solido**
✅ **Posizionamento chiaro per i gamer**
✅ **Onesto riguardo alle limitazioni**
