---
title: "Installazione hardware"
description: "Guida passo-passo per l'installazione hardware di Openterface KVM Extension for uConsole. Impara come installare correttamente la scheda di estensione nello slot di espansione del tuo uConsole con linee guida di sicurezza dettagliate."
keywords: "installazione estensione KVM, configurazione hardware uConsole, installazione scheda di espansione, slot di espansione uConsole, guida hardware KVM, installazione fisica"
---

# **Installazione hardware** | Openterface KVM Extension for uConsole

## Panoramica
L'Estensione KVM sostituisce il modulo 4G/LTE nello slot di espansione del uConsole, aggiungendo input HDMI diretto e controllo USB HID.

## Cosa ti serve
- Controlla il tuo [Contenuto della confezione](whats-in-the-box.md) prima dell'installazione  
- Scheda Openterface KVM Extension  
- **Rondelle** fornite (per garantire montaggio stabile e pressione uniforme)  
- Cacciavite esagonale (per le viti di montaggio)  
- Protezione ESD (braccialetto o superficie collegata a terra) — raccomandato  

## Passaggi di installazione

### **1. Spegnimento**
Spegni il uConsole e scollega tutta l'alimentazione e i cavi.

### **2. Rimozione modulo esistente**
Usa un cacciavite esagonale per rimuovere le due viti.  
Solleva la scheda **dritto verso l'alto** per evitare di piegare i contatti a molla.

### **3. Installazione dell'Estensione KVM**
- Posiziona la **rondella** sul perno della vite.  
- Inserisci saldamente l'Estensione KVM nello slot di espansione.  
- La rondella compensa il PCB leggermente più sottile (1,0 mm vs 1,2 mm), mantenendo una pressione di contatto a molla appropriata.

??? note "Controlla la vestibilità prima dell'installazione finale"
    Puoi prima inserire la scheda **senza la rondella** per testare la vestibilità. Se la scheda sembra allentata o i contatti sono irregolari, aggiungi la rondella e reinserisci la scheda. L'Openterface KVM Extension è spessa 1,0 mm, leggermente più sottile del modulo LTE originale (1,2 mm). L'uso della rondella fornita garantisce un montaggio stabile e un contatto a molla affidabile.  
    ![extension-slot-loose](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-slot-loose.webp){:style="max-height:220px"}

### **4. Fissaggio della scheda**
Reinserisci le viti e stringi **delicatamente** — **non stringere troppo**, poiché questo potrebbe danneggiare la scheda o rovinare le filettature.

![extension-screw-washer-installed](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installed.jpg){:style="max-height:220px"}
![extension-screw-washer-installing](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installing.jpg){:style="max-height:220px"}
![extension-install-1](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp){:style="max-height:220px"}

### **5. Verifica installazione**
La scheda dovrebbe essere **piatta e stabile**, con contatto a molla uniforme su tutti i pad. Non dovrebbe esserci oscillazione o movimento notevole.

### **6. Installazione copertura slot di espansione**
Reinstalla la copertura dello slot di espansione per proteggere la scheda Estensione KVM e mantenere l'aspetto originale del uConsole.

??? note "Orientamento del testo sulla copertura dello slot di espansione"
    Il testo sulla copertura dello slot di espansione può apparire "sottosopra" quando visto da certe angolazioni. Questo è un design intenzionale - il testo è orientato per essere leggibile quando tieni il uConsole e guardi le porte dall'alto verso il basso, che è la posizione di visualizzazione naturale quando usi il dispositivo.
    ![expansion-slot-text-orientation](https://assets.openterface.com/images/product/openterface-kvm-uconsole-expansion-slot-text-orientation.webp){:style="max-height:220px"}

---

**Prossimi passi**

1. Vai a [Configurazione software](/product/uconsole-kvm-extension/software-setup/) per installare l'App Openterface.  
2. Vai a [Connetti al dispositivo target](/product/uconsole-kvm-extension/connect-to-target/) per connettere il tuo dispositivo target.  
3. Rivedi [Funzionalità e specifiche](/product/uconsole-kvm-extension/features/) per specifiche tecniche dettagliate.
