---
title: "Características y especificaciones"
description: "Resumen completo de Openterface KVM Extension for uConsole: características potentes incluyendo entrada HDMI directa, control USB HID, factor de forma perfecto y especificaciones técnicas detalladas. Todo lo que necesitas saber sobre esta solución KVM portátil."
keywords: "características extensión KVM, uConsole KVM, HDMI KVM, control USB HID, KVM portátil, control headless, reemplazo 4G LTE, especificaciones técnicas, expansión uConsole"
---

# **Características y especificaciones** | Openterface KVM Extension for uConsole

![PCB-front](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:320px"}
![PCB-Back](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:320px"}

## Características principales

- **HDMI directo + USB HID**: Aprovecha la pantalla y controles integrados del uConsole con entrada HDMI directa y emulación USB HID.
- **Plug-and-Play**: Control instantáneo sin instalación de software o rastros residuales en el dispositivo objetivo.
- **Baja latencia**: Optimizado para resolución de problemas a nivel BIOS e interacciones en tiempo real.
- **Portátil**: Herramienta móvil todo-en-uno—no necesitas monitores adicionales, teclados o configuración de red.
- **Sin red**: Control headless estable a través de captura HDMI y entrada HID, no se requiere red.
- **Transferencia de texto**: Transfiere rápidamente texto simulando pulsaciones de teclas—ideal para nombres de usuario, contraseñas y fragmentos de código. Soporta ASCII completo, incluyendo símbolos y puntuación. [Consulta nuestra app](/app) para detalles.
- **Código abierto**: Construido sobre [Openterface KVM QT](https://github.com/techxArtisanStudio/openterface_qt) con soporte activo de la comunidad.

## Especificaciones técnicas

### Dimensiones físicas

- **Tamaño:** 37 × 77 mm (coincide con el módulo 4G/LTE)
- **Grosor:** 1,0 mm (más delgado que el módulo 4G/LTE original de 1,2 mm)
- **Material:** PCB de alta calidad con contactos de resorte

### Emulación completa de teclado y ratón

- **USB HID:** Posicionamiento absoluto y relativo del ratón, soporte completo de teclado, teclas multimedia.
- **Conexión:** Enlace USB al objetivo a través del puerto hembra Type-C de la placa de extensión.

### Video y audio

- **Entrada:** Hasta 4K (3840×2160) @ 30Hz a través de HDMI
- **Salida:** Full HD (1920×1080) @ 30Hz con latencia inferior a 140ms
- **Pantalla:** Utiliza la pantalla integrada del uConsole
- **Compresión:** Soporte YUV y MJPEG
- **Compatibilidad:** VGA, DVI, Micro HDMI (a través de adaptadores)
- **Audio:** Passthrough de audio embebido HDMI

### Puerto USB 2.0 conmutable

- **Puerto compartido:** Cambia fácilmente el acceso USB entre el uConsole y el dispositivo objetivo (ej. unidades flash) usando la app anfitrión.
- **Velocidad USB:** Transmisión a velocidad completa de 12Mbps

### Conectividad y alimentación

- **Alimentación:** Obtiene energía directamente del slot de expansión del uConsole (no se necesita alimentación externa)
- **Compatibilidad objetivo:** Windows, macOS, Linux, Android, iOS
- **Software objetivo:** No se requiere instalación
