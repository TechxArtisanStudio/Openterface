---
title: "Funciones y especificaciones"
description: "Descripción completa de la serie Openterface KVM-Go: diseño ultracompacto con conectores de vídeo integrados, soporte 4K/60Hz, ranura MicroSD y especificaciones técnicas detalladas. Solución KVM-over-USB del tamaño de un llavero para profesionales de TI."
keywords: "funciones KVM-Go, KVM ultracompacto, HDMI integrado, KVM 4K, KVM MicroSD, KVM llavero, especificaciones KVM, control headless, KVM portátil, herramientas TI, gestión de servidores"
---

# **Funciones y especificaciones** | Serie Openterface KVM-Go

## Estado de prelanzamiento

La serie KVM-Go se encuentra actualmente en desarrollo previo al lanzamiento. Estamos perfeccionando los diseños de PCB y carcasa. Únete a nuestra [lista de espera]({{ config.extra.kvmgo_purchase_link }}) para mantenerte informado sobre el progreso y obtener acceso anticipado.

> **Nota:** Las funciones, especificaciones y diseño aún están sujetos a cambios a medida que continúa el desarrollo.

## Modelos de producto
- **KVM-Go HDMI Male** — Conexión HDMI directa
- **KVM-Go DisplayPort Male** — DisplayPort de alto rendimiento
- **KVM-Go VGA Male** — Soporte para sistemas heredados (en desarrollo)

## Funciones principales

### **Diseño ultracompacto**
Factor de forma del tamaño de un llavero que cabe en tu bolsillo. Ya no es necesario llevar dispositivos KVM voluminosos ni buscar cables de vídeo.

### **Conectores de vídeo integrados**
Capacidad de conexión directa con conectores macho integrados:

- **HDMI Male** — Compatibilidad con dispositivos modernos
- **DisplayPort Male** — Soporte de alto rendimiento
- **VGA Male** — Soporte para sistemas heredados (próximamente)

### **Acceso a nivel BIOS**
Acceso directo a BIOS, firmware y gestión de inicio del dispositivo objetivo sin dependencias de red.

### **Independencia de red**
Control headless estable utilizando captura de vídeo integrada y entrada de teclado/ratón emulado (HID). No se requiere conexión de red.

### **Rendimiento de vídeo mejorado**
Mejora masiva respecto al 1080p@30Hz del Mini-KVM:

- **Entrada**: 4096×2160 @ 60 Hz (YUV420), 4096×2160 @ 30 Hz (YUV444)
- **Salida**: 4096×2160 @ 60 Hz (MJPEG), 3840×2160 @ 30 Hz (YUV420)
- **Compresión**: Soporte YUV420, YUV444 y MJPEG

### **Ranura MicroSD**
Transferencia de archivos entre dispositivos anfitrión y objetivo

### **Soporte multiplataforma**
[Aplicaciones anfitrión](/app) compatibles con macOS, Windows, Linux, Android y aplicación web Chrome para integración universal.

### **Transferencia de texto**
Transmite texto sin esfuerzo simulando pulsaciones de teclas — perfecto para nombres de usuario, contraseñas y fragmentos de código. Admite caracteres ASCII, incluidos símbolos y puntuación.

!!! warning "Limitaciones de transferencia de texto"
    - **Sin integración del portapapeles**: Solo emula la escritura, sin transferencia de imágenes o documentos
    - **Solo ASCII**: Limitado a caracteres ASCII (sin soporte para chino, japonés, coreano, etc.)
    - **Consideraciones de longitud**: Ideal para texto corto; bloques grandes pueden causar problemas de rendimiento

### **Comodidad plug-and-play**
No se requiere instalación de software en el dispositivo objetivo. El control comienza inmediatamente después de la conexión sin dejar rastros de software.

### **Integración de audio**
Audio integrado HDMI para una experiencia multimedia completa. (No compatible con KVM-Go VGA; confirmación pendiente para KVM-Go DP.)

### **Código abierto**
Hardware y software [totalmente de código abierto](/compliance) para transparencia e [innovación de la comunidad](/discord).

## Especificaciones técnicas

### **Dimensiones físicas** *(sujetas a cambios antes de la entrega)*
- **Tamaño**: 18 × 18 × 55 mm (0,71 × 0,71 × 2,17 pulgadas)
- **Peso**: ~25 g (0,9 oz)
- **Material**: Carcasa de aleación de aluminio con tapas impresas en 3D

### **Conectividad y alimentación**
- **Alimentación**: Alimentado por USB-C (no se necesita fuente externa)
- **Velocidad USB**: USB 3.0 para versiones HDMI/DP; USB 2.0 para versión VGA
- **Compatibilidad anfitrión**: Windows, macOS, Linux, Android, Chrome
- **Objetivo**: No se requiere instalación de software

### **Vídeo y audio**
- **Entrada máx.**: 4096×2160@60Hz (YUV420), 4096×2160@30Hz (YUV444)
- **Salida máx.**: 4096×2160@60Hz (MJPEG), 3840×2160@30Hz (YUV420)
- **Audio**: Audio integrado HDMI

### **Funciones de entrada**
- Emulación completa de teclado y ratón (absoluta y relativa)
- Soporte de teclas multimedia
- Funcionalidad HID personalizada
- Función de activación del ordenador

### **Almacenamiento**
- **Ranura MicroSD**: Transferencias de archivos mediante MicroSD entre anfitrión y objetivo

