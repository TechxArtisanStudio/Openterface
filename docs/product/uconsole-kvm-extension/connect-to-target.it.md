---
title: "Connettersi al Dispositivo Target"
description: "Impara come connettere il tuo dispositivo target all'Openterface KVM Extension for uConsole. Guida completa per la configurazione del controllo USB e dell'ingresso video dopo l'installazione hardware e la configurazione software."
keywords: "configurazione connessione KVM, connessione dispositivo target, configurazione controllo USB, configurazione ingresso HDMI, connessione estensione KVM uConsole"
---

# **Connettersi al Dispositivo Target** | Openterface KVM Extension for uConsole

## Panoramica della Connessione

![extension-use-case-1a](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1a.webp){:style="max-height:480px"}

## Prerequisiti

Prima di connettere il tuo dispositivo target, assicurati di aver completato:

1. [Installazione Hardware](/product/uconsole-kvm-extension/hardware-installation/) - Installazione fisica della scheda Extension KVM
2. [Configurazione Software](/product/uconsole-kvm-extension/software-setup/) - Installazione dell'App Openterface

## Passaggi di Connessione

### **Controllo USB**
Collega la porta femmina Type-C alla porta USB del dispositivo target per emulare i segnali di tastiera e mouse.

### **Ingresso Video**
Collega l'uscita video del dispositivo target alla porta HDMI sull'Extension KVM:

- Usa un cavo HDMI standard per dispositivi con uscita HDMI
- Usa un cavo convertitore VGA-to-HDMI per dispositivi con uscita VGA.
    - *Nota*: Assicurati che il convertitore sia alimentato tramite il suo connettore USB per un funzionamento corretto.
- Usa altri adattatori appropriati per diversi tipi di segnali video

## Test della Connessione

1. Accendi l'alimentazione e avvia l'uConsole
2. Esegui l'app Openterface QT
3. Testa le funzionalità HDMI, audio e USB HID per confermare il funzionamento corretto
