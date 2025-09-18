---
title: "Funcționalități și Specificații"
description: "Prezentare completă Openterface Mini-KVM: funcționalități puternice incluzând acces la nivel BIOS, suport video 4K, compatibilitate multiplatformă, partajare USB și specificații tehnice detaliate. Tot ce trebuie să știi despre această soluție de control computer headless."
keywords: "funcționalități Mini-KVM, specificații KVM, acces BIOS, control headless, KVM 4K, partajare USB, KVM multiplatformă, transfer text, KVM plug and play, KVM open source, specificații tehnice"
---

# **Funcționalități și Specificații** | Openterface Mini-KVM

<iframe 
  width="560" 
  height="315" 
  src="https://www.youtube.com/embed/r3HNUflWGOY?si=84Ek6F9ocHmmGTqW" 
  title="YouTube video player" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
  referrerpolicy="strict-origin-when-cross-origin" 
  allowfullscreen>
</iframe>

## Funcționalități Principale

### **Acces la Nivel BIOS**

Acces direct la BIOS-ul dispozitivului țintă, firmware și managementul pornirii fără dependențe de rețea.

### **Independență de Rețea**

Control headless stabil folosind capturare video HDMI și intrare tastatură/mouse emulată (HID). Nu este necesară conexiunea la rețea.

### **Video de Înaltă Performanță**

- **Intrare**: Până la 4K (3840×2160) @ 30Hz via HDMI
- **Ieșire**: Full HD (1920×1080) @ 30Hz cu latență sub 140ms
- **Compresie**: Suport YUV și MJPEG
- **Compatibilitate**: VGA, DVI, Micro HDMI via adaptoare

### **Port USB Comutabil**

Comutarea accesului USB între dispozitivele gazdă și țintă pentru partajarea seamless a unităților USB. Află mai multe pe pagina [Port USB Comutabil](../usb-switch).

### **Suport Multiplatformă**

[Aplicații gazdă](/app) compatibile cu macOS, Windows, Linux și Android pentru integrare universală.

### **Transfer Text**

Transmiterea textului fără efort prin simularea apăsărilor de taste—perfect pentru nume de utilizator, parole și fragmente de cod. Suportă caractere ASCII incluzând simboluri și punctuație.

!!! warning "Limitări Transfer Text" - **Fără Integrare Clipboard**: Emulează doar tastarea, fără transfer de imagini sau documente - **Doar ASCII**: Limitat la caractere ASCII (fără suport chineză, japoneză, coreeană) - **Considerații Lungime**: Cel mai bun pentru text scurt; blocurile mari pot cauza probleme de performanță

### **Conveniență Plug-and-Play**

Nu este necesară instalarea software-ului pe dispozitivul țintă. Controlul începe imediat la conectare fără să lase urme de software.

### **Integrare Audio**

Passthrough audio integrat HDMI pentru experiență multimedia completă.

### **Pinuri de Extensie**

[Pinurile de extensie](../extension-pins) permit dezvoltare avansată și personalizare pentru nevoi specifice.

### **Open-Source**

Hardware și software [complet open-source](/compliance) pentru transparență și [inovare comunitate](/discord).

## Specificații Tehnice

### **Dimensiuni Fizice**

- **Mărime**: 61 × 53 × 13.5 mm (2.40 × 2.09 × 0.53 inci)
- **Greutate**: ~48g
- **Material**: Aliaj aluminiu, carcasă PLA

### **Conectivitate și Alimentare**

- **Alimentare**: Alimentat prin USB-C (nu este necesară alimentare externă)
- **Viteza USB**: Transmisie viteză completă 12Mbps
- **Compatibilitate Gazdă**: Windows, macOS, Linux, Android
- **Țintă**: Nu este necesară instalarea software-ului

### **Video și Audio**

- **Intrare Max**: 3840×2160@30Hz (HDMI)
- **Ieșire Max**: 1920×1080@30Hz
- **Latență**: Sub 140ms
- **Audio**: Passthrough audio integrat HDMI

### **Funcționalități Intrare**

- Emulare completă tastatură și mouse (absolută și relativă)
- Suport taste multimedia
- Funcționalitate HID personalizată
- Funcție trezire computer

### **Ambiental**

- **Funcționare**: 0°C la 40°C
- **Depozitare**: -10°C la 50°C
- **Umiditate**: 80% RH

## Modele Produs

- **Basic**: OP-MINIKVM-BASIC
- **Toolkit**: OP-MINIKVM-TOOLKIT

## Descărcări Documentație

- **[Ghid Start Rapid](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/minikvm_quick_start_guide_20240928.pdf)** (PDF)
- **[Fișă Tehnică (Engleză)](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/Openterface-Mini-KVM-Basic-and-Toolkit-Datasheet-Eng-20250313.pdf)** (PDF)

![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front.svg#only-light){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back.svg#only-light){:style="max-height:260px"}
![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front_1.svg#only-dark){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back_1.svg#only-dark){:style="max-height:260px"}
