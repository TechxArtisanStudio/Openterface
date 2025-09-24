---
title: "Configurazione software"
description: "Guida completa alla configurazione software per Openterface KVM Extension for uConsole. Impara come installare e configurare l'App Openterface sul tuo uConsole per funzionalità KVM senza interruzioni."
keywords: "installazione app Openterface, configurazione software uConsole, configurazione app KVM, configurazione app uConsole, guida installazione software"
---

# **Configurazione software** | Openterface KVM Extension for uConsole

## Panoramica installazione

L'App Openterface consente al tuo uConsole di funzionare come un'interfaccia KVM, permettendoti di controllare i dispositivi target attraverso lo schermo integrato, la tastiera e il trackball.

!!! note "Requisiti"
    - **uConsole**: Richiede l'installazione dell'App Openterface
    - **Target**: Nessuna app necessaria - supporta Windows, macOS, Linux, Android, iOS
    - **Video**: Usa un cavo HDMI standard. Usa un cavo HDMI standard. Con un convertitore HDMI alimentato, supporta anche altri formati come **VGA**, **DP** e altro. *Suggerimento: Assicurati che il convertitore sia correttamente alimentato; altrimenti potresti riscontrare uno schermo nero.*

## Metodi di installazione

### **Opzione 1: Installazione Flatpak**

Segui la nostra [Guida all'installazione Flatpak](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) per i passaggi di configurazione dettagliati.

### **Opzione 2: Repository della comunità (Raccomandato)**

Se preferisci la build della comunità mantenuta da Rex:

1. **Aggiungi Repository**:
```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. **Installa Pacchetto**:
```bash
sudo apt update
sudo apt install openterfaceqt
```

!!! warning "Note Repository"
    Questi comandi richiedono sudo. Il repository è rivolto ai pacchetti arm64 Bookworm; verifica la compatibilità con il tuo dispositivo prima dell'installazione.

## Istruzioni per l'uso

### **Avvio sessione KVM**
1. Avvia l'App Openterface sul tuo uConsole
2. L'app rileverà automaticamente la scheda Extension KVM
3. Collega il tuo dispositivo target tramite HDMI
4. Usa la tastiera e trackball integrati del uConsole per controllare il dispositivo target

### **Funzionalità di controllo**
- **Tastiera**: Emulazione completa della tastiera inclusi i tasti multimediali
- **Mouse**: Posizionamento assoluto e relativo del mouse
- **Audio**: Pass-through audio HDMI agli altoparlanti uConsole

### **Funzionalità avanzate**
- **Trasferimento testo**: Trasferisci rapidamente testo simulando pressioni di tasti—ideale per nomi utente, password e frammenti di codice
- **USB commutabile**: Commuta facilmente l'accesso USB tra uConsole e dispositivo target usando l'app host
