---
title: "Port USB Comutabil"
description: "Învață despre sistemul dual de comutare USB hardware-software din Openterface Mini-KVM. Înțelege cele patru stări operaționale, ghidurile de siguranță și capacitățile viitoare de acces la distanță."
keywords: "comutare USB, comutator KVM, comutator hardware, comutator software, control port USB, KVM over USB, KVM over IP, acces la distanță, gestionare dispozitive USB, periferice computer, gestionare alimentare USB"
---

# **Ghid de Comutare Port USB** | Openterface Mini-KVM

Dispozitivul mini-KVM are un singur port USB-A 2.0 care se poate **conecta fie** la gazdă fie la computerul țintă, dar **niciodată la ambele simultan**.

Controlul vine de la două comutatoare:

- **Comutator Hardware**: Un comutator fizic cu două poziții pe dispozitiv ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t.svg#only-light){:style="height:20px"} ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t_1.svg#only-dark){:style="height:20px"} (spre interior = gazdă, spre exterior = țintă).
- **Comutator Software**: Un buton de comutare în aplicația gazdă care redirecționează instant portul USB către gazdă sau țintă.

## Stări Operaționale

Conexiunea portului USB-A depinde de pozițiile atât ale **Comutatorului Hardware** cât și ale **Comutatorului Software**. Următorul tabel rezumă cele patru stări posibile:

| **Stare** | **Comutator Hardware** | **Comutator Software** | **Port Conectat La** | **Status Sincronizare** |
| --------- | ---------------------- | ---------------------- | -------------------- | ----------------------- |
| 1         | Host                   | Host                   | Host                 | Synced                  |
| 2         | Target                 | Target                 | Target               | Synced                  |
| 3         | Target                 | Host                   | Host                 | Out of Sync (→ Host)    |
| 4         | Host                   | Target                 | Target               | Out of Sync (→ Target)  |

- **Synced** înseamnă că setările hardware și software se potrivesc.
- **Out of Sync** înseamnă că software-ul suprascrie temporar comutatorul hardware până când comutatorul hardware este mutat din nou.

Orice mișcare manuală a comutatorului hardware va actualiza afișajul software și va reveni la o stare sincronizată.

La pornire, dispozitivul se conectează implicit la gazdă. Software-ul detectează poziția comutatorului hardware și se sincronizează în consecință.

!!! warning "Nu uita să scoți stick-ul USB înainte de a comuta comutatorul"
Dacă portul USB este folosit de un stick USB, asigură-te că scoți stick-ul USB înainte de a comuta comutatorul pentru a transfera folosirea portului către alt computer.

??? note "Cum să împărtășești un stick/disk USB între dispozitivele Host și Target?"
Fișierele pot fi transferate între gazdă și țintă urmând acești pași:

    1. Montează un stick USB pe gazdă când micul comutator negru este setat pe partea portului Type-C al gazdei.
    2. Copiază fișierele pe această unitate montată.
    3. După copiere, demontează unitatea fără să o deconectezi fizic.
    4. Întoarce micul comutator negru pe cealaltă parte. Această acțiune comută conexiunea portului USB-A către țintă.
    5. Montează stick-ul USB pe dispozitivul țintă și copiază/mută fișierele de pe unitate, completând procesul de transfer de fișiere de la gazdă la țintă.

    Această metodă poate fi folosită și în direcția opusă.

!!! Note "Ghid Utilizator" - **Prioritatea Comutatorului Software**: Indiferent de poziția comutatorului hardware, apăsarea comutatorului software va schimba imediat direcția circuitului.

    - **Sincronizarea Comutatorului Hardware**: Orice comutare manuală a Comutatorului Hardware își va alinia starea cu Comutatorul Software, trecând de la Starea 3 sau 4 nesincronizată la Starea 1 sau 2. Cu toate acestea, această sincronizare nu alterează neapărat conexiunea circuitului real.

    - **Monitorizarea Comutatorului Hardware**: Comutatorul Hardware, în ciuda faptului că este fizic, este monitorizat de software și nu controlează direct direcția circuitului. În schimb, software-ul interpretează poziția comutatorului și gestionează comutarea reală a circuitului.
