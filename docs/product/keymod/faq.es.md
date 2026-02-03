---
title: Preguntas frecuentes sobre Openterface KeyMod
description: Preguntas frecuentes sobre KeyMod: funciones, compatibilidad, plataformas e información de pre-lanzamiento.
keywords: KeyMod, Openterface, emulador HID, teclado Bluetooth, teclado teléfono, código abierto, pre-lanzamiento, Android, iPadOS
---

# Preguntas frecuentes sobre Openterface KeyMod

Bienvenido a las preguntas frecuentes de **Openterface KeyMod**.  
Si no encuentras lo que necesitas, **envíanos un correo a [info@openterface.com](mailto:info@openterface.com)** o **únete a nuestra comunidad** en [Discord](/discord) o [Reddit](/reddit).

⚠️ **Nota**: KeyMod está actualmente en desarrollo de pre-lanzamiento. Las funciones, especificaciones y diseño están sujetos a cambios a medida que finalizamos el producto.

---

## :material-clipboard-list: Navegación rápida

- [Preguntas frecuentes sobre Openterface KeyMod](#preguntas-frecuentes-sobre-openterface-keymod)
  - [:material-clipboard-list: Navegación rápida](#material-clipboard-list-navegación-rápida)
  - [General](#general)
  - [Conectividad](#conectividad)
  - [Funciones](#funciones)
  - [Pre-lanzamiento](#pre-lanzamiento)

---

## General

**:material-chat-question:{ .faq } ¿Qué es KeyMod?**

KeyMod es un emulador HID (teclado y ratón) compacto USB + Bluetooth que convierte tu teléfono en un teclado y trackpad portátil. Úsalo para controlar dispositivos que necesitan entrada de teclado/ratón—quioscos, smart TVs, decodificadores, pantallas exteriores—sin llevar un teclado completo.

**:material-chat-question:{ .faq } ¿Qué plataformas soporta la aplicación KeyMod?**

La aplicación controladora KeyMod se centra en **Android** e **iPadOS**. También estamos ampliando el control de escritorio con software para **Windows y macOS** en nuestro ecosistema Openterface más amplio.

**:material-chat-question:{ .faq } ¿El dispositivo de destino necesita algún software?**

No. KeyMod emula un teclado y ratón USB estándar. El dispositivo de destino lo reconoce como hardware HID plug-and-play—no se requieren controladores ni instalación de software.

**:material-chat-question:{ .faq } ¿KeyMod es de código abierto?**

Sí. KeyMod es hardware y software abiertos. Publicaremos esquemas, archivos PCB, firmware, software y BOM a medida que el proyecto evolucione.

---

## Conectividad

**:material-chat-question:{ .faq } ¿USB o Bluetooth—cuál debo usar?**

- **USB**: Más fiable, menor latencia. Úsalo cuando quieras la conexión más estable.
- **Bluetooth**: Sin cables. Úsalo cuando quieras una configuración más ligera y el escenario permita inalámbrico.

**:material-chat-question:{ .faq } ¿Qué variantes de hardware están planificadas?**

1. **Conector 2 en 1** — Conector USB A + USB C combinado para amplia compatibilidad
2. **Versión USB C** — Conector USB C dedicado para dispositivos modernos

---

## Funciones

**:material-chat-question:{ .faq } ¿Qué diseños de gamepad son compatibles?**

KeyMod puede actuar como un controlador de juegos virtual con **diseño Xbox**, **diseño PlayStation** y **diseño NES**.

**:material-chat-question:{ .faq } ¿Puedo crear perfiles y macros personalizados?**

Sí. La aplicación móvil de código abierto soporta perfiles de entrada personalizados, macros, atajos de teclado y accesos directos de flujo de trabajo. También puedes usar modos de teclado numérico y gamepad.

**:material-chat-question:{ .faq } ¿Qué son los botones de hardware programables?**

KeyMod incluye botones de hardware programables para acciones en el dispositivo como disparadores rápidos y flujos de trabajo simples tipo macro. Esta capacidad es aún experimental y se refinará mediante comentarios de la comunidad.

---

## Pre-lanzamiento

**:material-chat-question:{ .faq } ¿Cuándo se lanzará KeyMod?**

KeyMod está en desarrollo de pre-lanzamiento. Suscríbete en la [página del producto](/product/keymod/) para notificaciones de lanzamiento y actualizaciones.

**:material-chat-question:{ .faq } ¿Cómo se relaciona KeyMod con Mini-KVM y KVM-Go?**

KeyMod utiliza el núcleo HID probado de Openterface Mini-KVM. Comparte el mismo enfoque de emulación de teclado y ratón basado en hardware, pero está diseñado para un caso de uso diferente: convertir tu teléfono en un teclado/trackpad portátil para control local de dispositivos, en lugar de captura de video KVM-over-USB.
