---
title: "Ghid de Comutare a Cardului MicroSD"
description: "Învață cum să utilizezi sistemul dual de comutare hardware-software MicroSD în Openterface KVM-Go. Înțelege cele patru stări operaționale, indicatorii LED, instrucțiunile de siguranță și capacitățile de transfer de fișiere."
keywords: "comutare MicroSD, comutator KVM, comutator hardware, comutator software, control card MicroSD, KVM prin USB, transfer fișiere, gestionare dispozitive USB, periferice computer, gestionare alimentare MicroSD, indicatori LED"
---

# **Ghid de Comutare a Cardului MicroSD** | Openterface KVM-Go

**Openterface KVM-Go** include un singur slot pentru card MicroSD care poate fi partajat între computerul gazdă și dispozitivul țintă, dar niciodată la ambele simultan.

Acest design îți permite să comuți rapid între dispozitive pentru **transfer de fișiere**, fără a scoate fizic cardul, făcând fluxul tău de lucru mai rapid și mai eficient. Poate servi, de asemenea, doar ca **cititor obișnuit de carduri MicroSD**.

## **Instalarea Cardului MicroSD**

![kvm-go-install-sd](https://assets.openterface.com/images/kvm-go/install-sd.webp){:style="max-height:260px;width:auto"}

!!! note "Instalarea Corectă a Cardului MicroSD"
    Introdu cardul MicroSD ferm până când simți un **clic**, indicând că este așezat în siguranță și blocat la locul său.

## **Metode de Control**

KVM-Go oferă două modalități de a comuta cardul MicroSD între gazdă și țintă:

- **Buton Hardware** – Un buton fizic pe dispozitiv pentru control manual.  
- **Comutator Software** – Un buton de comutare în aplicația gazdă pentru comutare instantanee.


## **Buton de Comutare & Indicatori LED** 

![kvm-go-led-indicator](https://assets.openterface.com/images/kvm-go/led-indicator.webp){:style="max-height:260px;width:auto"}

**Indicatorii LED bicolori** afișează starea curentă a conexiunii MicroSD *(Notă: În Dezvoltare / Supus Modificărilor)*:

- **🔵 LED Albastru APRINS** – Cardul MicroSD este montat pe **dispozitivul țintă**  
- **🟢 LED Verde APRINS** – Cardul MicroSD este montat pe **computerul gazdă**  
- **LED STINS** – Niciun card MicroSD inserat sau dispozitiv oprit  
- **LED INTERMITENT** – Transfer de date în progres (activitate citire/scriere)

!!! note "Funcție de Montare Automată (Experimentală)"
    În mod implicit, cardul MicroSD se montează pe **gazdă** când dispozitivul este pornit pentru prima dată.  
    O funcție experimentală viitoare va permite **montarea automată** pe oricare parte (gazdă sau țintă) care se conectează prima, făcând experiența și mai fluidă.

