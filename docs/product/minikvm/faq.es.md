---
title: Preguntas frecuentes sobre Openterface Mini-KVM
description: Preguntas frecuentes sobre el Mini-KVM, que cubren características, compatibilidad, resolución de problemas y planes futuros.
keywords: Mini-KVM, Openterface, conmutador KVM, código abierto, resolución de problemas, captura de video, USB, compatibilidad, autodiagnóstico, control teclado ratón, diagnóstico hardware, soporte
---

# Preguntas frecuentes sobre Openterface Mini-KVM

Bienvenido a las preguntas frecuentes de nuestro producto estrella **Openterface Mini-KVM**.  
Si no encuentra lo que necesita, **envíenos un correo electrónico a [info@openterface.com](mailto:info@openterface.com)** o **únete a nuestra comunidad** en [Discord](/discord) o [Reddit](/reddit).

⚠️ _Las preguntas frecuentes pueden estar desactualizadas — háganos saber si ve algo que necesita actualización._

---

## :material-clipboard-list: Navegación rápida

-   [Puerto USB y transferencia de archivos](#puerto-usb-y-transferencia-de-archivos)
-   [Técnico](#técnico)
-   [Control](#control)
-   [Video](#video)
-   [Resolución de problemas](#resolución-de-problemas)
-   [Más](#más)

---

## Puerto USB y transferencia de archivos

**:material-chat-question:{ .faq } ¿Puede transferir archivos?**

Sí — a través del puerto USB-A conmutable compartido entre el anfitrión y el objetivo.

**:material-chat-question:{ .faq } ¿Puedo conmutar el puerto USB en software?**

Sí, en la versión de hardware **v1.9+**.

**:material-chat-question:{ .faq } ¿Por qué USB 2.0 en lugar de 3.0?**

USB 2.0 es suficiente para video 1080p@30Hz + HID + transferencia de archivos a velocidad estándar mientras se mantiene compacto, más fresco y más asequible.  
USB 3.0 podría aparecer en futuros modelos profesionales.

---

## Técnico

**:material-chat-question:{ .faq } ¿Código abierto?**

Sí — certificado por [OSHWA](https://certification.oshwa.org/cn000015.html). El hardware y software están en [GitHub](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware).

**:material-chat-question:{ .faq } Acceso BIOS**

La conexión USB directa permite control completo a nivel BIOS, a diferencia de las herramientas solo remotas (VNC, TeamViewer).  
Las máquinas más antiguas pueden tener problemas BIOS reconociendo nuestro hub USB — comunique los casos.

**:material-chat-question:{ .faq } Transmisión de video/datos**

El video se captura vía HDMI y se envía vía USB 2.0.  
El puerto USB conmutable le permite compartir unidades u otros dispositivos.

**:material-chat-question:{ .faq } Manejo de energía**

El Mini-KVM puede obtener energía de **cualquier lado** (anfitrión u objetivo). El lado con el **cable más corto** usualmente se convierte en la fuente de energía principal.  
Para objetivos de baja potencia (ej. Raspberry Pi), use una fuente de alimentación dedicada en lugar de retroalimentación vía Mini-KVM.

**:material-chat-question:{ .faq } Límites de longitud de cable**

-   Mantenga el **cable USB-C anfitrión naranja ≤1.5m**.
-   Para cables más largos, inyecte energía vía:
    -   Cable USB-A macho a macho
    -   [Pines de extensión](/product/minikvm/extension-pins/)
    -   Divisor USB-C Y
-   La misma regla se aplica al **cable objetivo negro**.

---

## Control

**:material-chat-question:{ .faq } El teclado y el ratón no pueden controlar el ordenador objetivo**

Si puede ver el escritorio del objetivo pero las entradas de teclado y ratón no responden, suele significar que la comunicación HID no se ha establecido. Pruebe estos pasos:

1. **Comprobar conexiones de cables** — Asegúrese de que el cable Type-C del objetivo esté conectado al ordenador objetivo; el cable del anfitrión a su ordenador de control.
2. **Evitar hubs USB sin alimentación** — Use conexión directa o un hub alimentado.
3. **Restablecer el chip HID** — Si el dispositivo parece "congelado", use **Menú Avanzado → Restablecer chip HID de fábrica** (OpenterfaceQt) o **Herramienta de restablecimiento serial** (macOS).
4. **Probar otro puerto USB o reiniciar** — El sistema operativo del anfitrión puede desactivar un puerto tras errores USB.
5. **Reducir la velocidad en baudios** — En entornos ruidosos, cambie a 9600 bps para una comunicación más fiable.

Para más detalles, consulte [Solución de problemas de control de teclado y ratón](/product/minikvm/support/keyboard-mouse-control/).

**:material-chat-question:{ .faq } ¿Versión inalámbrica o Ethernet?**

No integrado. Use un ordenador headless (ej. Raspberry Pi) + escritorio remoto para control remoto.

**:material-chat-question:{ .faq } ¿Compatibilidad PS/2?**

No — el soporte PS/2 podría explorarse en versiones futuras.

**:material-chat-question:{ .faq } ¿Múltiples Mini-KVMs en un ordenador?**

Sí, característica experimental en la aplicación QT (Windows/Linux).

**:material-chat-question:{ .faq } ¿Control de encendido/apagado?**

No directamente, pero los [pines de extensión](/product/minikvm/extension-pins/) permiten futuros módulos de control ATX.

---

## Video

**:material-chat-question:{ .faq } Latencia y resolución**

-   Captura a **1080p@30Hz**
-   Latencia bajo **140ms** → control fluido

**:material-chat-question:{ .faq } Resolución de entrada vs captura**

-   Acepta entrada hasta **4K@30Hz**
-   Captura a **1080p**, entradas más altas se submuestrean (pueden verse ligeramente borrosas).
-   Mejor práctica: **Configure el objetivo a 1080p**.

**:material-chat-question:{ .faq } Idoneidad para juegos**

No para juegos AAA. Funciona bien para juegos más ligeros como Minecraft o emuladores.

**:material-chat-question:{ .faq } Control remoto sobre internet**

No integrado, pero empareje Mini-KVM con software de escritorio remoto en el anfitrión.

**:material-chat-question:{ .faq } Otros formatos de video**

Use adaptadores para VGA, DVI, DisplayPort, etc.

---

## Resolución de problemas

**:material-chat-question:{ .faq } ¿Cómo ejecuto diagnósticos para comprobar si mi Mini-KVM funciona?**

Ejecute el autodiagnóstico integrado para verificar las conexiones USB y detectar problemas de hardware:

- **macOS:** [Guía de autodiagnóstico (macOS)](/product/minikvm/support/diagnostic-self-check/) — Ajustes → Avanzado y Depuración → Abrir Herramienta de Diagnóstico
- **Windows:** [Guía de autodiagnóstico (Windows)](/product/minikvm/support/diagnostic-self-check-windows/) — Avanzado → Hardware Diagnostics

Los diagnósticos prueban Target/Host Plug & Play, Prueba de Estrés, etc. Si todas las pruebas pasan, su dispositivo funciona correctamente.

**:material-chat-question:{ .faq } ¿Cómo reporto un problema de hardware al soporte?**

Si el autodiagnóstico muestra **FALLA** en una o más pruebas:

1. Complete los pasos de diagnóstico restantes (la herramienta le guiará).
2. Cuando se detecte un problema, se abrirá una ventana de **Correo de Soporte** o **Informe de Defecto**.
3. Ingrese su **Número de Pedido** y **Nombre**, luego copie la dirección de correo y el borrador.
4. Adjunte los **archivos de registro solicitados** (la herramienta indica cuáles) y una **foto de la configuración** (Mini-KVM + conexiones anfitrión/objetivo claramente visibles).
5. Envíe el correo al soporte.

Instrucciones paso a paso: [Guía de autodiagnóstico (macOS)](/product/minikvm/support/diagnostic-self-check/) o [Guía de autodiagnóstico (Windows)](/product/minikvm/support/diagnostic-self-check-windows/).

**:material-chat-question:{ .faq } Problemas de hub USB**

Use un **hub alimentado** para evitar caídas de voltaje. Los hubs sin alimentación pueden provocar suministro insuficiente y comportamiento errático del HID (teclado/ratón). Consulte [Solución de problemas de control de teclado y ratón](/product/minikvm/support/keyboard-mouse-control/).

**:material-chat-question:{ .faq } La aplicación no muestra video o el control no responde**

1. Desconecte todos los cables, espere unos segundos, reconecte.
2. Consulte [Solución de problemas de control de teclado y ratón](/product/minikvm/support/keyboard-mouse-control/) para problemas HID (cables, hubs, restablecimiento HID).
3. Ejecute el [autodiagnóstico](/product/minikvm/support/diagnostic-self-check/) (macOS) o [Hardware Diagnostics](/product/minikvm/support/diagnostic-self-check-windows/) (Windows) para verificar el dispositivo.
4. Si no se resuelve, verifique el firmware o actualice la aplicación anfitrión.

**:material-chat-question:{ .faq } Resoluciones extrañas como 43184x24228@44Hz**

El firmware de captura probablemente revirtió a fábrica.  
Re-flashee el firmware vía [lanzamientos GitHub](https://github.com/TechxArtisanStudio/Openterface_QT/releases).

**:material-chat-question:{ .faq } ¿Re-flasheado pero aún roto?**

-   Verifique la enumeración USB correcta (`USB Tree Viewer` o `lsusb -v`)
-   Confirme la aplicación anfitrión más reciente
-   Ejecute el [autodiagnóstico](/product/minikvm/support/diagnostic-self-check/) para capturar registros
-   Si aún falla, contacte soporte con su Número de Pedido, registros de diagnóstico y foto de configuración — consulte [¿Cómo reporto un problema de hardware al soporte?](#cómo-reporto-un-problema-de-hardware-al-soporte)
