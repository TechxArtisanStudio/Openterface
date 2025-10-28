---
title: "Come connettersi"
description: "Guida passo passo per configurare l'Openterface KVM-Go. Scopri come collegare il tuo computer host e il dispositivo di destinazione utilizzando connettori video integrati per un'esperienza di connessione diretta ultra-semplice."
keywords: "configurazione KVM-Go, configurazione KVM ultra-compatto, connessione HDMI integrata, guida installazione KVM, configurazione KVM portachiavi, connessione USB KVM, configurazione computer headless, configurazione KVM portatile"
---

# **Come connettersi** | Guida alla configurazione | Openterface KVM-Go

## **Panoramica delle connessioni**

![Panoramica connessioni KVM-Go](https://assets.openterface.com/images/kvm-go/step-0-overview.webp){:style="max-height:360px"}

Le immagini sopra mostrano tutte le connessioni tra il [**KVM-Go**](/product/kvm-go), il computer host e il dispositivo di destinazione.

- **Computer host**: Richiede l'installazione dell'[app Openterface](/app).  
- **Dispositivo di destinazione**: Non sono necessari software e pre-configurazioni.
- **Video**: Il connettore integrato si collega direttamente al dispositivo di destinazione, quindi non è necessario portare o gestire cavi video aggiuntivi.

## **Cosa serve per le connessioni**

![KVM-Go tutte le parti](https://assets.openterface.com/images/kvm-go/step-0-all-parts.webp){:style="max-height:360px"}

Per configurare il tuo **KVM-Go**, avrai bisogno dei seguenti componenti:

- **KVM-Go (HDMI / DP / VGA)** — si collega al **dispositivo di destinazione** (per la cattura video)  
- **Cavo USB-C corto nero** — si collega al **dispositivo di destinazione** (per l'emulazione di tastiera e mouse)
- **Cavo USB-C lungo arancione** — si collega al **computer host** (che esegue l'[app Openterface](/app))

!!! note "Disclaimer sulla lunghezza dei cavi"
    Le lunghezze esatte dei cavi inclusi nel **pacchetto ufficiale KVM-Go** **non sono ancora finalizzate** e potrebbero differire leggermente da quelle mostrate qui.  
    I cavi dimostrati in questa guida provengono dal *classico Mini-KVM Toolkit* e sono solo a scopo illustrativo.

!!! warning "Utilizzo di cavi propri"
    Se scegli di utilizzare i tuoi cavi, assicurati che siano **cavi USB di alta qualità, capaci di trasferire dati**. Cavi di scarsa qualità o solo per la ricarica possono causare:
    
    - Problemi di schermo nero
    - Input di tastiera o mouse non reattivi
    - Cadute di connessione intermittenti
    - Output video tremolante o instabile

## **Configurazione passo passo**

### **Passo 1 — Collegare i cavi USB al KVM-Go**
![Collegamento cavi USB](https://assets.openterface.com/images/kvm-go/step-1-plugged.webp){:style="max-height:360px"}

- **Cavo USB-C nero** → Collegare alla porta etichettata ![Icona Target](https://assets.openterface.com/images/shell-icons/target-computer.svg#only-light){:style="max-height:20px"} ![Icona Target](https://assets.openterface.com/images/shell-icons/target-computer_1.svg#only-dark){:style="max-height:20px"} **Target** sulla custodia KVM-Go.  
- **Cavo USB-C arancione** → Collegare alla porta etichettata ![Icona Host](https://assets.openterface.com/images/shell-icons/host-computer.svg#only-light){:style="max-height:20px"} ![Icona Host](https://assets.openterface.com/images/shell-icons/host-computer_1.svg#only-dark){:style="max-height:20px"} **Host**.

!!! warning
    Entrambe le porte USB-C sono fisicamente identiche.  
    Controllare sempre **le etichette** sulla superficie della custodia per evitare di confonderle.

### **Passo 2 — Collegare il video alla destinazione**
![Collegamento connettore HDMI](https://assets.openterface.com/images/kvm-go/step-3-hdmi-plugged.webp){:style="max-height:360px"}

Collegare il **connettore video maschio integrato** direttamente alla porta di uscita video del dispositivo di destinazione.

### **Passo 3 — Collegare la porta USB di destinazione**
Collegare il **cavo USB nero** al dispositivo di destinazione per il controllo HID.

- **Opzione A:** Direttamente in una porta USB-A  
  ![Target USB-A](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-b.webp){:style="max-height:360px"}

- **Opzione B:** Utilizzando un adattatore USB-C  
  ![Target USB-C](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-a.webp){:style="max-height:360px"}

!!! note "Verifica connessione USB-C"
    Alcune porte USB-C potrebbero non fornire una connessione sicura. Se si verificano problemi di controllo intermittente della tastiera/mouse, muovere delicatamente la connessione dell'adattatore per assicurarsi che sia inserita correttamente e faccia contatto.


### **Passo 4 — Collegare la porta USB host**
Collegare il **cavo USB arancione** al computer host.

- Direttamente a una porta USB-C **OPPURE** tramite un adattatore da USB-C a USB-A.  
  ![Collegamento USB host](https://assets.openterface.com/images/kvm-go/step-5-plug-in-host-computer-1.webp){:style="max-height:360px"}

