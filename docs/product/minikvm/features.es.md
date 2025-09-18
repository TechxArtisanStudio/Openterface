---
title: "Funciones y Especificaciones"
description: "Resumen completo de Openterface Mini-KVM: funciones potentes incluyendo acceso a nivel BIOS, soporte de video 4K, compatibilidad multiplataforma, compartir USB y especificaciones técnicas detalladas. Todo lo que necesitas saber sobre esta solución de control de ordenador headless."
keywords: "funciones Mini-KVM, especificaciones KVM, acceso BIOS, control headless, KVM 4K, compartir USB, KVM multiplataforma, transferencia de texto, KVM plug and play, KVM open source, especificaciones técnicas"
---

# **Funciones y Especificaciones** | Openterface Mini-KVM

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

## Funciones Principales

### **Acceso a Nivel BIOS**

Acceso directo al BIOS del dispositivo objetivo, firmware y gestión de inicio sin dependencias de red.

### **Independencia de Red**

Control headless estable usando captura de video HDMI y entrada de teclado/ratón emulada (HID). No se requiere conexión de red.

### **Video de Alto Rendimiento**

- **Entrada**: Hasta 4K (3840×2160) @ 30Hz vía HDMI
- **Salida**: Full HD (1920×1080) @ 30Hz con latencia inferior a 140ms
- **Compresión**: Soporte YUV y MJPEG
- **Compatibilidad**: VGA, DVI, Micro HDMI vía adaptadores

### **Puerto USB Conmutable**

Alternar acceso USB entre dispositivos anfitrión y objetivo para compartir unidades USB sin problemas. Aprende más en la página [Puerto USB Conmutable](../usb-switch).

### **Soporte Multiplataforma**

[Aplicaciones anfitrión](/app) compatibles con macOS, Windows, Linux y Android para integración universal.

### **Transferencia de Texto**

Transmitir texto sin esfuerzo simulando pulsaciones de teclas—perfecto para nombres de usuario, contraseñas y fragmentos de código. Soporta caracteres ASCII incluyendo símbolos y puntuación.

!!! warning "Limitaciones de Transferencia de Texto" - **Sin Integración de Portapapeles**: Solo emula escritura, no transferencia de imágenes o documentos - **Solo ASCII**: Limitado a caracteres ASCII (sin soporte para chino, japonés, coreano) - **Consideraciones de Longitud**: Mejor para texto corto; bloques grandes pueden causar problemas de rendimiento

### **Conveniencia Plug-and-Play**

No se requiere instalación de software en el dispositivo objetivo. El control comienza inmediatamente al conectar sin dejar rastros de software.

### **Integración de Audio**

Passthrough de audio integrado HDMI para experiencia multimedia completa.

### **Pines de Extensión**

Los [pines de extensión](../extension-pins) habilitan desarrollo avanzado y personalización para necesidades específicas.

### **Open-Source**

Hardware y software [completamente open-source](/compliance) para transparencia e [innovación de la comunidad](/discord).

## Especificaciones Técnicas

### **Dimensiones Físicas**

- **Tamaño**: 61 × 53 × 13.5 mm (2.40 × 2.09 × 0.53 pulgadas)
- **Peso**: ~48g
- **Material**: Aleación de aluminio, carcasa PLA

### **Conectividad y Alimentación**

- **Alimentación**: Alimentado por USB-C (no se necesita alimentación externa)
- **Velocidad USB**: Transmisión a velocidad completa 12Mbps
- **Compatibilidad Anfitrión**: Windows, macOS, Linux, Android
- **Objetivo**: No se requiere instalación de software

### **Video y Audio**

- **Entrada Máx**: 3840×2160@30Hz (HDMI)
- **Salida Máx**: 1920×1080@30Hz
- **Latencia**: Inferior a 140ms
- **Audio**: Passthrough de audio integrado HDMI

### **Funciones de Entrada**

- Emulación completa de teclado y ratón (absoluta y relativa)
- Soporte de teclas multimedia
- Funcionalidad HID personalizada
- Función de despertar ordenador

### **Ambiental**

- **Funcionamiento**: 0°C a 40°C
- **Almacenamiento**: -10°C a 50°C
- **Humedad**: 80% RH

## Modelos de Producto

- **Basic**: OP-MINIKVM-BASIC
- **Toolkit**: OP-MINIKVM-TOOLKIT

## Descargas de Documentación

- **[Guía de Inicio Rápido](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/minikvm_quick_start_guide_20240928.pdf)** (PDF)
- **[Hoja de Datos (Inglés)](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/Openterface-Mini-KVM-Basic-and-Toolkit-Datasheet-Eng-20250313.pdf)** (PDF)

![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front.svg#only-light){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back.svg#only-light){:style="max-height:260px"}
![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front_1.svg#only-dark){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back_1.svg#only-dark){:style="max-height:260px"}
