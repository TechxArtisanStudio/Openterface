---
title: "Guida alla commutazione della scheda MicroSD"
description: "Scopri come utilizzare il sistema di commutazione MicroSD dual hardware-software nell'Openterface KVM-Go. Comprendi i quattro stati operativi, gli indicatori LED, le linee guida di sicurezza e le capacità di trasferimento file."
keywords: "commutazione MicroSD, switch KVM, switch hardware, switch software, controllo scheda MicroSD, KVM over USB, trasferimento file, gestione dispositivi USB, periferiche computer, gestione alimentazione MicroSD, indicatori LED"
---

# **Guida alla commutazione della scheda MicroSD** | Openterface KVM-Go

L'**Openterface KVM-Go** include un singolo slot per scheda MicroSD che può essere condiviso tra il computer host e il dispositivo di destinazione, ma mai entrambi contemporaneamente.

Questo design ti consente di passare rapidamente tra i dispositivi per il **trasferimento di file**, senza rimuovere fisicamente la scheda, rendendo il tuo flusso di lavoro più veloce ed efficiente. Può anche funzionare semplicemente come il tuo **lettore di schede MicroSD normale**.

## **Installare la scheda MicroSD**

![kvm-go-install-sd](https://assets.openterface.com/images/kvm-go/install-sd.webp){:style="max-height:260px;width:auto"}

!!! note "Installazione corretta della scheda MicroSD"
    Inserisci saldamente la scheda MicroSD finché non senti un **clic**, indicando che è inserita in modo sicuro e bloccata in posizione.

## **Metodi di controllo**

KVM-Go offre due modi per commutare la scheda MicroSD tra host e destinazione:

- **Pulsante hardware** — Un pulsante fisico sul dispositivo per il controllo manuale.  
- **Interruttore software** — Un pulsante toggle all'interno dell'app host per la commutazione istantanea.


## **Pulsante di commutazione e indicatori LED** 

![kvm-go-led-indicator](https://assets.openterface.com/images/kvm-go/led-indicator.webp){:style="max-height:260px;width:auto"}

Gli **indicatori LED bicolore** visualizzano lo stato di connessione MicroSD corrente *(Nota: In sviluppo / Soggetto a modifiche)*:

- **🔵 LED blu acceso** — La scheda MicroSD è montata sul **dispositivo di destinazione**  
- **🟢 LED verde acceso** — La scheda MicroSD è montata sul **computer host**  
- **LED spento** — Nessuna scheda MicroSD inserita o dispositivo spento  
- **LED lampeggiante** — Trasferimento dati in corso (attività di lettura/scrittura)

!!! note "Funzione di montaggio automatico (Sperimentale)"
    Per impostazione predefinita, la scheda MicroSD si monta sull'**host** quando il dispositivo viene acceso per la prima volta.  
    Una prossima funzionalità sperimentale consentirà il **montaggio automatico** su quale lato (host o destinazione) si connette per primo, rendendo l'esperienza ancora più fluida.

---

## Correlati

- [microSD EXPRESS su KVM-GO: test di compatibilità e velocità di trasferimento reali](updates/20260203-kvm-go-microsd-express.it.md) — Test di compatibilità con scheda SanDisk microSD EXPRESS e velocità di trasferimento reali

