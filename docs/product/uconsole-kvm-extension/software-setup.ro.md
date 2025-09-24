---
title: "Configurare software"
description: "Ghid complet de configurare software pentru Openterface KVM Extension for uConsole. Învață cum să instalezi și să configurezi App-ul Openterface pe uConsole-ul tău pentru funcționalitate KVM fără probleme."
keywords: "instalare app Openterface, configurare software uConsole, configurare app KVM, configurare app uConsole, ghid instalare software"
---

# **Configurare software** | Openterface KVM Extension for uConsole

## Prezentare generală instalare

App-ul Openterface permite uConsole-ului tău să funcționeze ca o interfață KVM, permițându-ți să controlezi dispozitivele țintă prin ecranul integrat, tastatura și trackball.

!!! note "Cerințe"
    - **uConsole**: Necesită instalarea App-ului Openterface
    - **Țintă**: Nu este necesar app - suportă Windows, macOS, Linux, Android, iOS
    - **Video**: Folosește un cablu HDMI standard. Folosește un cablu HDMI standard. Cu un convertor HDMI alimentat, suportă și alte formate precum **VGA**, **DP** și mai multe. *Sfat: Asigură-te că convertorul este alimentat corespunzător; altfel, poți experimenta un ecran negru.*

## Metode de instalare

### **Opțiunea 1: Instalare Flatpak**

Urmărește [Ghidul nostru de instalare Flatpak](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) pentru pași de configurare detaliați.

### **Opțiunea 2: Depozitarul comunității (Recomandat)**

Dacă preferi build-ul comunității întreținut de Rex:

1. **Adaugă depozitarul**:
```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. **Instalează pachetul**:
```bash
sudo apt update
sudo apt install openterfaceqt
```

!!! warning "Note depozitar"
    Aceste comenzi necesită sudo. Depozitarul țintește pachete arm64 Bookworm; verifică compatibilitatea cu dispozitivul tău înainte de instalare.

## Instrucțiuni de utilizare

### **Pornirea sesiunii KVM**
1. Lansează App-ul Openterface pe uConsole-ul tău
2. App-ul va detecta automat placa Extension KVM
3. Conectează dispozitivul tău țintă prin HDMI
4. Folosește tastatura și trackball-ul integrat ale uConsole-ului pentru a controla dispozitivul țintă

### **Funcționalități de control**
- **Tastatură**: Emulare completă a tastaturii incluzând taste multimedia
- **Mouse**: Poziționare absolută și relativă a mouse-ului
- **Audio**: Passthrough audio HDMI către difuzoarele uConsole

### **Funcționalități avansate**
- **Transfer de text**: Transferă rapid text prin simularea apăsărilor de taste—ideal pentru nume de utilizator, parole și fragmente de cod
- **USB comutabil**: Comută ușor accesul USB între uConsole și dispozitivul țintă folosind app-ul gazdă
