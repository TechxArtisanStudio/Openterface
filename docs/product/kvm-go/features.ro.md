---
title: "Funcții și specificații"
description: "Prezentare completă a seriei Openterface KVM-Go: design ultra-compact cu conectori video încorporați, suport 4K/60Hz, slot MicroSD și specificații tehnice detaliate. Soluție KVM-over-USB de dimensiunea unui breloc pentru profesioniștii IT."
keywords: "funcții KVM-Go, KVM ultra-compact, HDMI încorporat, KVM 4K, KVM MicroSD, KVM breloc, specificații KVM, control headless, KVM portabil, unelte IT, gestionare servere"
---

# **Funcții și specificații** | Seria Openterface KVM-Go

## Stadiu pre-lansare

Seria KVM-Go este în prezent în dezvoltare pre-lansare. Perfecționăm designurile PCB și carcasă. Alăturați-vă [listei de așteptare]({{ config.extra.kvmgo_purchase_link }}) pentru a rămâne la curent cu progresul și a obține acces anticipat.

> **Notă:** Funcțiile, specificațiile și designul sunt încă supuse modificărilor pe măsură ce dezvoltarea continuă.

## Modele de produse
- **KVM-Go HDMI Male** — Conexiune HDMI directă
- **KVM-Go DisplayPort Male** — DisplayPort de înaltă performanță
- **KVM-Go VGA Male** — Suport pentru sisteme vechi (în dezvoltare)

## Funcții principale

### **Design ultra-compact**
Format de dimensiunea unui breloc care încape în buzunar. Nu mai este nevoie să cărați dispozitive KVM voluminoase sau să căutați cabluri video.

### **Conectori video încorporați**
Capacitate de conectare directă cu conectori masculi încorporați:

- **HDMI Male** — Compatibilitate cu dispozitive moderne
- **DisplayPort Male** — Suport de înaltă performanță
- **VGA Male** — Suport pentru sisteme vechi (în curând)

### **Acces la nivel BIOS**
Acces direct la BIOS, firmware și gestionarea pornirii dispozitivului țintă fără dependențe de rețea.

### **Independență de rețea**
Control headless stabil folosind captura video încorporată și intrarea de tastatură/mouse emulată (HID). Nu necesită conexiune la rețea.

### **Performanță video îmbunătățită**
Îmbunătățire masivă față de 1080p@30Hz al Mini-KVM:

- **Intrare**: 4096×2160 @ 60 Hz (YUV420), 4096×2160 @ 30 Hz (YUV444)
- **Ieșire**: 4096×2160 @ 60 Hz (MJPEG), 3840×2160 @ 30 Hz (YUV420)
- **Compresie**: Suport YUV420, YUV444 și MJPEG

### **Slot MicroSD**
Transfer de fișiere între dispozitivele gazdă și țintă

### **Suport multi-platformă**
[Aplicații gazdă](/app) compatibile cu macOS, Windows, Linux, Android și aplicația web Chrome pentru integrare universală.

### **Transfer de text**
Transmiteți text fără efort simulând apăsări de taste — perfect pentru nume de utilizator, parole și fragmente de cod. Suportă caractere ASCII incluzând simboluri și punctuație.

!!! warning "Limitări transfer de text"
    - **Fără integrare clipboard**: Doar emulează tastarea, fără transfer de imagini sau documente
    - **Doar ASCII**: Limitat la caractere ASCII (fără suport pentru chineză, japoneză, coreeană, etc.)
    - **Considerații de lungime**: Ideal pentru text scurt; blocuri mari pot cauza probleme de performanță

### **Conveniență plug-and-play**
Nu necesită instalare de software pe dispozitivul țintă. Controlul începe imediat după conectare fără a lăsa urme de software.

### **Integrare audio**
Audio HDMI încorporat pentru experiență multimedia completă. (Nu este suportat pe KVM-Go VGA; confirmare în așteptare pentru KVM-Go DP.)

### **Open-source**
Hardware și software [complet open-source](/compliance) pentru transparență și [inovație comunitară](/discord).

## Specificații tehnice

### **Dimensiuni fizice** *(supuse modificării înainte de livrare)*
- **Dimensiune**: 18 × 18 × 55 mm (0,71 × 0,71 × 2,17 inch)
- **Greutate**: ~25 g (0,9 oz)
- **Material**: Carcasă din aliaj de aluminiu cu capace imprimate 3D

### **Conectivitate și alimentare**
- **Alimentare**: Alimentat USB-C (fără sursă externă necesară)
- **Viteză USB**: USB 3.0 pentru versiuni HDMI/DP; USB 2.0 pentru versiune VGA
- **Compatibilitate gazdă**: Windows, macOS, Linux, Android, Chrome
- **Țintă**: Nu necesită instalare de software

### **Video și audio**
- **Intrare max**: 4096×2160@60Hz (YUV420), 4096×2160@30Hz (YUV444)
- **Ieșire max**: 4096×2160@60Hz (MJPEG), 3840×2160@30Hz (YUV420)
- **Audio**: Audio HDMI încorporat

### **Funcții de intrare**
- Emulare completă de tastatură și mouse (absolută și relativă)
- Suport pentru taste multimedia
- Funcționalitate HID personalizată
- Funcție de trezire a computerului

### **Stocare**
- **Slot MicroSD**: Transferuri de fișiere prin MicroSD între gazdă și țintă

