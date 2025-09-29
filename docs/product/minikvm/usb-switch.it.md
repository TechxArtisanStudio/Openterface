---
title: "Porta USB Commutabile"
description: "Scopri il sistema di commutazione USB dual hardware-software in Openterface Mini-KVM. Comprendi i quattro stati operativi, le linee guida di sicurezza e le future capacità di accesso remoto."
keywords: "commutazione USB, commutatore KVM, commutatore hardware, commutatore software, controllo porta USB, KVM over USB, KVM over IP, accesso remoto, gestione dispositivi USB, periferiche computer, gestione alimentazione USB"
---

# **Guida alla Commutazione della Porta USB** | Openterface Mini-KVM

Il dispositivo mini-KVM ha una singola porta USB-A 2.0 che può **connettersi sia** all'host che al computer target, ma **mai a entrambi contemporaneamente**.

Il controllo proviene da due commutatori:

- **Commutatore Hardware**: Un interruttore fisico a due posizioni sul dispositivo ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t.svg#only-light){:style="max-height:20px"} ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t_1.svg#only-dark){:style="max-height:20px"} (verso l'interno = host, verso l'esterno = target).
- **Commutatore Software**: Un pulsante di commutazione nell'app host che reindirizza istantaneamente la porta USB all'host o al target.

## Stati Operativi

La connessione della porta USB-A dipende dalle posizioni sia del **Commutatore Hardware** che del **Commutatore Software**. La tabella seguente riassume i quattro stati possibili:

| **Stato** | **Commutatore Hardware** | **Commutatore Software** | **Porta Connessa A** | **Stato di Sincronizzazione** |
| --------- | ------------------------ | ------------------------ | -------------------- | ----------------------------- |
| 1         | Host                     | Host                     | Host                 | Synced                        |
| 2         | Target                   | Target                   | Target               | Synced                        |
| 3         | Target                   | Host                     | Host                 | Out of Sync (→ Host)          |
| 4         | Host                     | Target                   | Target               | Out of Sync (→ Target)        |

- **Synced** significa che le impostazioni hardware e software corrispondono.
- **Out of Sync** significa che il software sovrascrive temporaneamente il commutatore hardware fino a quando il commutatore hardware non viene spostato di nuovo.

Qualsiasi movimento manuale del commutatore hardware aggiornerà la visualizzazione software e tornerà a uno stato sincronizzato.

All'avvio, il dispositivo si connette per impostazione predefinita all'host. Il software rileva la posizione del commutatore hardware e si sincronizza di conseguenza.

!!! warning "Ricorda di espellere la chiavetta USB prima di commutare l'interruttore"
Se la porta USB è utilizzata da una chiavetta USB, assicurati di espellere la chiavetta USB prima di commutare l'interruttore per trasferire l'uso della porta a un altro computer.

??? note "Come condividere una chiavetta/disco USB tra i dispositivi Host e Target?"
I file possono essere trasferiti tra host e target seguendo questi passaggi:

    1. Monta una chiavetta USB sull'host quando il piccolo interruttore nero è impostato sul lato della porta Type-C dell'host.
    2. Copia i file su questo drive montato.
    3. Dopo la copia, smonta il drive senza scollegarlo fisicamente.
    4. Capovolgi il piccolo interruttore nero dall'altra parte. Questa azione commuta la connessione della porta USB-A al target.
    5. Monta la chiavetta USB sul dispositivo target e copia/sposta i file dal drive, completando il processo di trasferimento dei file dall'host al target.

    Questo metodo può essere utilizzato anche nella direzione opposta.

!!! Note "Guida Utente" - **Priorità del Commutatore Software**: Indipendentemente dalla posizione del commutatore hardware, cliccare sul commutatore software cambierà immediatamente la direzione del circuito.

    - **Sincronizzazione del Commutatore Hardware**: Qualsiasi commutazione manuale del Commutatore Hardware allineerà il suo stato con il Commutatore Software, passando dallo Stato 3 o 4 non sincronizzato allo Stato 1 o 2. Tuttavia, questa sincronizzazione non altera necessariamente la connessione del circuito effettiva.

    - **Monitoraggio del Commutatore Hardware**: Il Commutatore Hardware, nonostante sia fisico, è monitorato dal software e non controlla direttamente la direzione del circuito. Invece, il software interpreta la posizione del commutatore e gestisce la commutazione del circuito effettiva.
