---
title: "Cum să conectați"
description: "Ghid pas cu pas pentru configurarea Openterface KVM-Go. Învățați cum să conectați computerul gazdă și dispozitivul țintă folosind conectori video încorporați pentru o experiență de conectare directă ultra-simplă."
keywords: "configurare KVM-Go, configurare KVM ultra-compact, conexiune HDMI încorporată, ghid instalare KVM, configurare KVM breloc, conexiune USB KVM, configurare computer headless, configurare KVM portabil"
---

# **Cum să conectați** | Ghid de configurare | Openterface KVM-Go

## **Prezentare generală a conexiunilor**

![Prezentare generală conexiuni KVM-Go](https://assets.openterface.com/images/kvm-go/step-0-overview.webp){:style="max-height:360px"}

Imaginile de mai sus arată toate conexiunile dintre [**KVM-Go**](/product/kvm-go), computerul gazdă și dispozitivul țintă.

- **Computer gazdă**: Necesită instalarea [aplicației Openterface](/app).  
- **Dispozitiv țintă**: Nu necesită software și pre-configurare.
- **Video**: Conectorul încorporat se conectează direct la dispozitivul țintă, astfel nu trebuie să cărați sau să gestionați cabluri video suplimentare.

## **Ce aveți nevoie pentru conexiuni**

![KVM-Go toate piesele](https://assets.openterface.com/images/kvm-go/step-0-all-parts.webp){:style="max-height:360px"}

Pentru a configura **KVM-Go**, veți avea nevoie de următoarele componente:

- **KVM-Go (HDMI / DP / VGA)** — se conectează la **dispozitivul țintă** (pentru captura video)  
- **Cablu USB-C scurt negru** — se conectează la **dispozitivul țintă** (pentru emularea tastaturii și mouse-ului)
- **Cablu USB-C lung portocaliu** — se conectează la **computerul gazdă** (care rulează [aplicația Openterface](/app))

!!! note "Notă privind lungimea cablurilor"
    Lungimile exacte ale cablurilor incluse în **pachetul oficial KVM-Go** **nu sunt încă finalizate** și pot diferi ușor de cele prezentate aici.  
    Cablurile demonstrate în acest ghid provin din *kitul clasic Mini-KVM* și sunt doar în scop ilustrativ.

!!! warning "Folosirea propriilor cabluri"
    Dacă alegeți să folosiți propriile cabluri, asigurați-vă că sunt **cabluri USB de înaltă calitate, capabile de transfer de date**. Cablurile de calitate slabă sau doar pentru încărcare pot duce la:
    
    - Probleme de ecran negru
    - Intrări de tastatură sau mouse fără răspuns
    - Deconectări intermitente
    - Ieșire video instabilă sau tremurătoare

## **Configurare pas cu pas**

### **Pasul 1 — Conectați cablurile USB la KVM-Go**
![Conectarea cablurilor USB](https://assets.openterface.com/images/kvm-go/step-1-plugged.webp){:style="max-height:360px"}

- **Cablu USB-C negru** → Conectați la portul etichetat ![Pictogramă țintă](https://assets.openterface.com/images/shell-icons/target-computer.svg#only-light){:style="max-height:20px"} ![Pictogramă țintă](https://assets.openterface.com/images/shell-icons/target-computer_1.svg#only-dark){:style="max-height:20px"} **Target** pe carcasa KVM-Go.  
- **Cablu USB-C portocaliu** → Conectați la portul etichetat ![Pictogramă gazdă](https://assets.openterface.com/images/shell-icons/host-computer.svg#only-light){:style="max-height:20px"} ![Pictogramă gazdă](https://assets.openterface.com/images/shell-icons/host-computer_1.svg#only-dark){:style="max-height:20px"} **Host**.

!!! warning
    Ambele porturi USB-C sunt fizic identice.  
    Verificați întotdeauna **etichetele** de pe suprafața carcasei pentru a evita confundarea lor.

### **Pasul 2 — Conectați video la țintă**
![Conectarea conectorului HDMI](https://assets.openterface.com/images/kvm-go/step-3-hdmi-plugged.webp){:style="max-height:360px"}

Conectați **conectorul video mascul încorporat** direct la portul de ieșire video al dispozitivului țintă.

### **Pasul 3 — Conectați portul USB țintă**
Conectați **cablul USB negru** la dispozitivul țintă pentru control HID.

- **Opțiunea A:** Direct într-un port USB-A  
  ![Țintă USB-A](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-b.webp){:style="max-height:360px"}

- **Opțiunea B:** Folosind un adaptor USB-C  
  ![Țintă USB-C](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-a.webp){:style="max-height:360px"}

!!! note "Verificarea conexiunii USB-C"
    Unele porturi USB-C pot să nu ofere o conexiune sigură. Dacă experimentați probleme intermitente de control al tastaturii/mouse-ului, mișcați ușor conexiunea adaptorului pentru a vă asigura că este așezat corect și face contact.


### **Pasul 4 — Conectați portul USB gazdă**
Conectați **cablul USB portocaliu** la computerul gazdă.

- Direct la un port USB-C **SAU** printr-un adaptor USB-C către USB-A.  
  ![Conectarea USB gazdă](https://assets.openterface.com/images/kvm-go/step-5-plug-in-host-computer-1.webp){:style="max-height:360px"}

