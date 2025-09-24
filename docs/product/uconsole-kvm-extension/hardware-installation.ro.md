---
title: "Instalare hardware"
description: "Ghid pas cu pas pentru instalarea hardware-ului Openterface KVM Extension for uConsole. Învață cum să instalezi corect placa de extensie în slotul de expansiune al uConsole-ului tău cu ghiduri de siguranță detaliate."
keywords: "instalare extensie KVM, configurare hardware uConsole, instalare placă expansiune, slot expansiune uConsole, ghid hardware KVM, instalare fizică"
---

# **Instalare hardware** | Openterface KVM Extension for uConsole

## Prezentare generală
Extensia KVM înlocuiește modulul 4G/LTE din slotul de expansiune al uConsole-ului, adăugând intrare HDMI directă și control USB HID.

## Ce ai nevoie
- Verifică [Conținutul pachetului](whats-in-the-box.md) înainte de instalare  
- Placa Openterface KVM Extension  
- **Șaibe** furnizate (pentru a asigura montaj stabil și presiune uniformă)  
- Șurubelniță hexagonală (pentru șuruburile de montare)  
- Protecție ESD (brățară sau suprafață împământată) — recomandat  

## Pași de instalare

### **1. Oprire alimentare**
Oprește uConsole-ul și deconectează toată alimentarea și cablurile.

### **2. Eliminare modul existent**
Folosește o șurubelniță hexagonală pentru a elimina cele două șuruburi.  
Ridică placa **drept în sus** pentru a evita îndoirea contactelor cu arc.

### **3. Instalare Extensia KVM**
- Plasează **șaiba** pe postul șurubului.  
- Așează ferm Extensia KVM în slotul de expansiune.  
- Șaiba compensează PCB-ul ușor mai subțire (1,0 mm vs 1,2 mm), menținând presiunea de contact cu arc corespunzătoare.

??? note "Verifică potrivirea înainte de instalarea finală"
    Poți mai întâi să așezi placa **fără șaibă** pentru a testa potrivirea. Dacă placa pare slăbită sau contactele sunt neuniforme, adaugă șaiba și reașează placa. Openterface KVM Extension are 1,0 mm grosime, ușor mai subțire decât modulul LTE original (1,2 mm). Folosirea șaibei furnizate asigură montaj stabil și contact cu arc fiabil.  
    ![extension-slot-loose](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-slot-loose.webp){:style="height:220px"}

### **4. Fixare placă**
Reinserează șuruburile și strânge **ușor** — **nu strânge prea mult**, deoarece aceasta poate deteriora placa sau deteriora filetele.

![extension-screw-washer-installed](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installed.jpg){:style="height:220px"}
![extension-screw-washer-installing](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installing.jpg){:style="height:220px"}
![extension-install-1](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp){:style="height:220px"}

### **5. Verificare instalare**
Placa ar trebui să stea **plat și stabilă**, cu contact cu arc uniform pe toate pad-urile. Nu ar trebui să existe mișcare sau balansare vizibilă.

### **6. Instalare capac slot expansiune**
Reinstalează capacul slotului de expansiune pentru a proteja placa Extensia KVM și pentru a menține aspectul original al uConsole-ului.

??? note "Orientarea textului pe capacul slotului de expansiune"
    Textul de pe capacul slotului de expansiune poate părea "cu susul în jos" când este privit din anumite unghiuri. Acesta este un design intenționat - textul este orientat să fie lizibil când ții uConsole-ul și privești porturile de sus în jos, care este poziția naturală de vizualizare când folosești dispozitivul.
    ![expansion-slot-text-orientation](https://assets.openterface.com/images/product/openterface-kvm-uconsole-expansion-slot-text-orientation.webp){:style="height:220px"}

---

**Următorii pași**

1. Mergi la [Configurare software](/product/uconsole-kvm-extension/software-setup/) pentru a instala App-ul Openterface.  
2. Mergi la [Conectare la dispozitivul țintă](/product/uconsole-kvm-extension/connect-to-target/) pentru a conecta dispozitivul tău țintă.  
3. Revizuiește [Caracteristici și specificații](/product/uconsole-kvm-extension/features/) pentru specificații tehnice detaliate.
