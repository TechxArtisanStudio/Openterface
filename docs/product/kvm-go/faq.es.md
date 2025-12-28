---
title: Preguntas Frecuentes para Openterface KVM-Go Series
description: Preguntas frecuentes sobre la serie KVM-Go, cubriendo características, compatibilidad e información de prelanzamiento.
keywords: KVM-Go, Openterface, KVM ultra compacto, HDMI integrado, KVM llavero, código abierto, prelanzamiento, captura de vídeo, USB, compatibilidad, MicroSD
---

# Preguntas Frecuentes para Openterface KVM-Go Series

Bienvenido a las preguntas frecuentes de nuestra **serie Openterface KVM-Go** de próxima generación.  
Si no encuentras lo que necesitas, **envíanos un correo electrónico a [info@openterface.com](mailto:info@openterface.com)** o **únete a nuestra comunidad** en [Discord](/discord) o [Reddit](/reddit).

⚠️ **Nota**: KVM-Go está actualmente en desarrollo de prelanzamiento. Las características, especificaciones y diseño están sujetos a cambios mientras finalizamos el producto.

---

## :material-clipboard-list: Navegación Rápida

- [Preguntas Frecuentes para Openterface KVM-Go Series](#preguntas-frecuentes-para-openterface-kvm-go-series)
  - [:material-clipboard-list: Navegación Rápida](#material-clipboard-list-navegación-rápida)
  - [General](#general)
  - [MicroSD y Transferencia de Archivos](#microsd-y-transferencia-de-archivos)
  - [Técnico](#técnico)
  - [Prelanzamiento](#prelanzamiento)

---

## General

**:material-chat-question:{ .faq } ¿Qué es KVM-Go?**

KVM-Go es nuestra solución KVM-over-USB ultra compacta de próxima generación. Es del tamaño de un llavero con conectores de vídeo integrados (HDMI, DisplayPort o VGA) que eliminan la necesidad de cables separados.

**:material-chat-question:{ .faq } ¿Qué tan pequeño es?**

Dimensiones ultra compactas: **18 × 18 × 55 mm** (0,71 × 0,71 × 2,17 pulgadas) — lo suficientemente pequeño para caber en tu llavero. El peso es aproximadamente **25g (0,9 oz)**.

**:material-chat-question:{ .faq } ¿Qué modelos están disponibles?**

- **KVM-Go HDMI Male** — Conexión HDMI directa para dispositivos modernos
- **KVM-Go DisplayPort Male** — Soporte DisplayPort de alto rendimiento  
- **KVM-Go VGA Male** — Compatibilidad con sistemas heredados (próximamente)

**:material-chat-question:{ .faq } ¿Cómo se compara con Mini-KVM?**

Mejoras principales:

- **Tamaño**: 18×18×55mm vs 61×53×13,5mm (mucho más pequeño)
- **Peso**: 25g vs 48g (más ligero)
- **Vídeo**: 4K@60Hz vs 1080p@30Hz (mejor rendimiento)
- **USB**: USB 3.0 vs USB 2.0 (más rápido)
- **Configuración**: Conectores integrados vs cables separados (más fácil)

**:material-chat-question:{ .faq } ¿Qué tan rápido arranca?**

El tiempo de arranque del hardware es inferior a 1 segundo, permitiendo solución de problemas inmediata sin retrasos ni interrupciones en tu flujo de trabajo.

---

## MicroSD y Transferencia de Archivos

**:material-chat-question:{ .faq } ¿Puede transferir archivos?**

Sí — a través de la **ranura MicroSD conmutable** que puede ser compartida entre el anfitrión y dispositivos objetivo, permitiendo transferencias de archivos rápidas sin quitar físicamente la tarjeta.

**:material-chat-question:{ .faq } ¿Cómo cambio la dirección del MicroSD?**

Dos métodos convenientes:
1. **Botón de Hardware** – Botón físico en el dispositivo para control manual
2. **Interruptor de Software** – Botón de alternancia dentro de la aplicación anfitrión para cambio instantáneo

**:material-chat-question:{ .faq } ¿Qué significan los indicadores LED?**

Los **indicadores LED de dos colores** muestran el estado actual de conexión MicroSD:

- **🔵 LED Azul ENCENDIDO** – La tarjeta MicroSD está montada en el **dispositivo objetivo**  
- **🟢 LED Verde ENCENDIDO** – La tarjeta MicroSD está montada en el **ordenador anfitrión**  
- **LED APAGADO** – No hay tarjeta MicroSD insertada o dispositivo apagado  
- **LED PARPADEANDO** – Transferencia de datos en progreso (actividad de lectura/escritura)

**:material-chat-question:{ .faq } ¿Cómo instalo correctamente la tarjeta MicroSD?**

Inserta la tarjeta MicroSD firmemente hasta que sientas un **clic**, indicando que está bien colocada y bloqueada. Esta retroalimentación táctil confirma la conexión correcta.

---

## Técnico

**:material-chat-question:{ .faq } ¿Cuál es el rendimiento de vídeo?**

- **Entrada**: Hasta 4096×2160 @ 60 Hz (YUV420), 4096×2160 @ 30 Hz (YUV444)
- **Salida**: 4096×2160 @ 60 Hz (MJPEG), 3840×2160 @ 30 Hz (YUV420)
- **Por defecto**: 1080p@60Hz para estabilidad y rendimiento óptimos
- **Latencia**: Menos de 140ms para un control fluido

**:material-chat-question:{ .faq } ¿El modo 4K tiene limitaciones?**

Sí — el modo 4K es experimental y genera calor adicional. La superficie del dispositivo puede calentarse bastante durante operaciones prolongadas en 4K. Para estabilidad y rendimiento óptimos, se recomienda el modo 1080p@60Hz por defecto.

**:material-chat-question:{ .faq } ¿Es código abierto?**

Sí — certificado por [OSHWA](https://certification.oshwa.org/cn000015.html). El hardware y software están en [GitHub](https://github.com/TechxArtisanStudio/Openterface_KVM-GO_Hardware).

**:material-chat-question:{ .faq } Acceso a BIOS**

La conexión USB directa permite control completo a nivel de BIOS, a diferencia de herramientas solo remotas (VNC, TeamViewer).

**:material-chat-question:{ .faq } ¿Soporte multiplataforma?**

[Aplicaciones anfitrión](/app) compatibles con macOS, Windows, Linux, Android y aplicación web Chrome para integración universal.

**:material-chat-question:{ .faq } ¿Puedo usarlo con un iPad?**

Sí — el soporte para iPadOS llegará pronto a través de una aplicación nativa disponible en el Apple App Store. Esto es posible gracias a la capacidad Bluetooth integrada de KVM-GO, convirtiéndolo en uno de los pocos KVM que funciona nativamente con iPads.

**:material-chat-question:{ .faq } ¿Hay una aplicación basada en web?**

Sí — visita [Openterface Viewer](https://openterface-viewer.pages.dev/) para una aplicación basada en navegador sin instalación (funciona en Chrome, Edge, Safari). Perfecta para acceso rápido o cuando no puedes instalar software en el ordenador anfitrión. Gracias a nuestra increíble comunidad, particularmente [@kashalls](https://github.com/kashalls) quien inició este proyecto.

**:material-chat-question:{ .faq } ¿Qué conector de vídeo debo elegir?**

- **HDMI**: Mejor para dispositivos modernos, servidores, estaciones de trabajo
- **DisplayPort**: Pantallas de alta resolución, configuraciones profesionales
- **VGA**: Sistemas heredados, servidores más antiguos (próximamente)

---

## Prelanzamiento

**:material-chat-question:{ .faq } ¿Cuándo estará disponible KVM-Go?**

KVM-Go está actualmente en pruebas de producción en pequeños lotes con unidades enviadas a probadores beta para validación en el mundo real.

**Cronograma de Producción**:

- **Noviembre 2025**: Lanzamiento de campaña
- **Diciembre 2025**: Finalizar configuración de producción y abastecimiento de componentes
- **Enero-Marzo 2026**: Producción en masa y control de calidad
- **Abril 2026**: Primeros envíos a patrocinadores

Únete a nuestra [lista de espera]({{ config.extra.kvmgo_purchase_link }}) para mantenerte actualizado sobre el progreso y obtener acceso anticipado.

**:material-chat-question:{ .faq } ¿Cuánto costará?**

Los precios se anunciarán durante la campaña de lanzamiento oficial. Los primeros patrocinadores recibirán descuentos especiales y acceso prioritario.

**:material-chat-question:{ .faq } ¿Puedo convertirme en probador beta?**

¡Sí! Si tienes experiencia en pruebas de hardware y software, eres bienvenido a solicitar nuestro programa de pruebas beta [aquí](https://forms.gle/yaS1F5E5MSo8DWNZ6).

**:material-chat-question:{ .faq } ¿Las especificaciones son finales?**

No, las características, especificaciones y diseño están sujetos a cambios mientras finalizamos el producto durante el desarrollo.

