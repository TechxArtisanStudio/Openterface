---
draft: false
date: 2026-05-21
title: "KeyCmd 0.19: Cambio de marca de la app, modo Compose KM Pro, soporte multiidioma y guías interactivas por modo"
description: "KeyCmd 0.19 trae un cambio de marca importante de KeyMod a KeyCmd, el nuevo modo Compose KM Pro con envío HID Unicode, interfaz multiidioma (coreano, italiano, ruso, pt-BR), guías interactivas por modo y decenas de mejoras UX."
keywords: "KeyCmd 0.19, lanzamiento KeyCmd, cambio de marca app, modo Compose, envío HID Unicode, multiidioma, guías interactivas, actualización Openterface KeyCmd, emulador HID, teclado virtual, aplicación teclado Android"
author: "TechxArtisan Studio"
category: "Product Updates"
tags: ["KeyCmd", "Product Updates", "Release", "Compose", "i18n", "Android"]
featured: false
social:
  image: "https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp"
  title: "Lanzamiento de KeyCmd 0.19 — Modo Compose, cambio de marca, multiidioma, guías interactivas"
  description: "KeyCmd 0.19 trae el nuevo modo Compose, cambio de marca a KeyCmd, 4 nuevos idiomas, guías interactivas y mejoras significativas de UX."
---

# KeyCmd 0.19: Cambio de marca de la app, modo Compose KM Pro, soporte multiidioma y guías interactivas por modo

KeyCmd **0.19** (`versionCode` **19**) es una actualización importante que trae el **cambio de marca** de KeyMod a KeyCmd, el nuevo **modo Compose de KM Pro** con envío HID compatible con Unicode, una **interfaz multiidioma ampliada** (incluyendo coreano, italiano, ruso y portugués brasileño), **guías interactivas por modo**, y decenas de mejoras de UX en los modos teclado, gamepad y presentación.

## Cambio de marca de la app: KeyMod → KeyCmd

El nombre visible de la aplicación ahora es **KeyCmd** en todos los puntos de entrada. Este cambio de marca aclara la distinción entre el **hardware KeyMod** y su **aplicación complementaria KeyCmd**.

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp" alt="Pantalla de bienvenida KeyCmd" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">

### Qué cambió

- **Nombre visible de la app**: El icono del lanzador y la interfaz del sistema ahora muestran «KeyCmd»
- **Flujo de bienvenida**: Marca y texto actualizados de KeyMod a KeyCmd
- **Artefactos CI y nombres de archivos APK**: Usan el prefijo **KeyCmd**
- `applicationId` sigue siendo **`com.openterface.keymod`** para actualizaciones in situ sin interrupciones

Usuarios existentes: tu configuración, perfiles y dispositivos vinculados se conservan. La actualización es transparente.

## Teclado y ratón: experiencia a pantalla completa

KeyCmd ofrece una experiencia a pantalla completa de teclado, panel táctil y teclado numérico — optimizada para orientaciones vertical y horizontal.

<div class="slideshow-container" id="slideshow-keycmd-019-kbm-es" data-auto-slide="true" data-auto-slide-interval="3000">
  <div class="slideshow-wrapper">
    <div class="slide active">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Full-Keyboard-landscape.webp" alt="Teclado horizontal a pantalla completa" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape.webp" alt="Teclado numérico horizontal" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-portrait.webp" alt="Teclado numérico vertical" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait.webp" alt="Teclado y panel táctil vertical" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-km-basic-Touchpad.webp" alt="Panel táctil horizontal" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Remote-Coding-portrait.webp" alt="Codificación remota con KeyCmd" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Settings-screen.webp" alt="Pantalla de configuración KeyCmd" style="max-height:320px;" loading="lazy">
    </div>
  </div>

  <div class="slideshow-navigation">
    <button class="nav-arrow left" onclick="changeSlide('slideshow-keycmd-019-kbm-es', -1)">❮</button>
    <div class="slideshow-dots">
      <span class="dot active" onclick="currentSlide('slideshow-keycmd-019-kbm-es', 1)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-es', 2)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-es', 3)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-es', 4)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-es', 5)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-es', 6)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-es', 7)"></span>
    </div>
    <button class="nav-arrow right" onclick="changeSlide('slideshow-keycmd-019-kbm-es', 1)">❯</button>
  </div>
</div>

## KM Pro: modo Compose & Send

La mayor novedad en la versión 0.19 es el **modo Compose** en KM Pro — un editor de texto dedicado que te permite escribir pasajes largos y enviarlos como pulsaciones de teclado HID al equipo objetivo.

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait.webp" alt="Ejecución de script en modo Compose" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">


### Editor Compose

- **Barra de accesos directos superior + fila de acción de composición** con controles **Limpiar** y **Deshacer/Limpiar**
- **Retención de borrador**: tu texto se conserva al cambiar de submodo e incluso después de un envío exitoso
- **Integración IME**: escribe con el teclado de tu teléfono, envía como pulsaciones HID limpias
- **Progreso de envío determinado**: una barra de progreso visible para búferes HID largos para que sepas exactamente cuánto ha avanzado el envío

### Envío HID compatible con Unicode

- **Revisión de riesgos en doble modo**: antes de enviar texto no ASCII, un diálogo advierte sobre la compatibilidad Unicode y proporciona acciones de inspección y vista previa
- **Flujo hexadecimal Unicode en macOS**: en equipos macOS, la aplicación usa el método de entrada Option+código hexadecimal para caracteres extendidos
- **Diálogos de envío más seguros**: la pantalla de revisión adapta su contenido según si el búfer es ASCII puro o contiene caracteres Unicode
- **Herramientas de inspección de caracteres**: el diálogo de riesgo de envío proporciona acciones **Verificar** y **Vista previa**, y los equipos macOS incluyen una entrada dedicada de **auditoría de ruta hexadecimal Unicode**

### Alcance de KM Basic

En la versión 0.19, **Compose & Send sigue siendo una función de Teclado y Ratón Pro**. KM Basic se centra en flujos de trabajo de teclado a pantalla completa, panel táctil y teclado numérico.

## Soporte multiidioma

KeyCmd ahora soporta **11 idiomas de interfaz**. Esta versión añade cuatro nuevas localizaciones:

- **Coreano (ko)**: traducción completa de la interfaz
- **Italiano (it)**: traducción completa de la interfaz
- **Ruso (ru)**: traducción completa de la interfaz
- **Portugués brasileño (pt-BR)**: traducción completa de la interfaz

Junto con el inglés, chino simplificado, chino tradicional, japonés, francés, alemán y español existentes, KeyCmd ahora cubre la gran mayoría de nuestra base de usuarios global.

### Qué cambió

- **Selector de idioma** en Configuración con nombres canónicos de idiomas
- **Encabezados Bluetooth** y **vista previa de pulsación** localizados
- **Correcciones lint de versión** para pestañas de advertencia de composición en todos los idiomas

## Guías interactivas por modo

Cada modo ahora tiene una **guía interactiva integrada** que te acompaña paso a paso por sus funciones.

### Guías disponibles

- **Guía Shortcut Hub**: abre el perfil por defecto y cubre la interfaz de detalle, pestañas de categorías y gestión de accesos directos
- **Guía Gamepad**: explica la disposición del gamepad, gestión de módulos y sistema de ajustes preestablecidos
- **Guía KM Pro**: cubre el modo Compose, panel de accesos directos y funciones específicas de Pro
- **Guía KM Basic**: explica el teclado a pantalla completa, deslizamiento con mantenimiento de modificadores y teclado numérico

### Funciones de las guías

- **Guías por modo**: cada modo tiene su propia guía personalizada
- **Hoja de repetición**: revisita cualquier guía en cualquier momento mediante el botón **Guía de modo** (icono a la izquierda de la sección de conexión)
- **Soporte i18n**: el contenido de las guías está localizado en todos los idiomas de la aplicación
- **Optimizado para horizontal**: las hojas inferiores se adaptan correctamente en orientación horizontal

## Mejoras de UX

### Teclado

- **Vista previa de pulsación**: ve exactamente qué se enviará antes de pulsar. Actívalo en Configuración. Activado por defecto.
- **Corrección HID de pulsación rápida**: mejora del tiempo de liberación de pulsaciones y eventos de liberación consolidados para una escritura más rápida
- **Manejo táctil de caracteres alternativos**: mantener pulsada la tecla `a` ahora muestra alternativas ¥ (arriba), £ (izquierda), € (derecha) con retroalimentación visual mejorada
- **Deslizamiento con mantenimiento de modificadores**: en las guías KM Basic/Pro, un nuevo paso enseña el gesto de deslizamiento con mantenimiento para acceso rápido a modificadores

### Gamepad

- **Barra de sesión de edición eliminada**: interfaz de gamepad más limpia sin la antigua barra de herramientas de sesión de edición
- **Interfaz y guía del gamepad**: nuevo pulido visual y guía interactiva integrada
- **Icono de guía de modo**: colocado a la izquierda de la sección de conexión para fácil acceso

### Presentación

- **Bloqueo vertical**: el modo Presentación está limitado a orientaciones vertical y vertical invertida para un control de presentador estable

### Interfaz y tema

- **Muestras de acento**: reemplazado el selector de familia de colores de tema por muestras visuales de acento para una selección de color más fácil
- **Alineación de acentos UI**: todos los acentos UI siguen ahora la familia de colores de tema (no el color primario heredado)
- **Clúster derecho del encabezado**: dimensiones mejoradas para iconos de conexión tanto en la app principal como en la interfaz KM Basic
- **Estilo del botón de envío Compose**: apariencia del botón de envío no ASCII alineada en modo claro

### Configuración

- **Reorganización de configuración**: nombres canónicos de idiomas; scripts de instalación de emulador renombrados para mayor claridad
- **Scripts de ayuda al desarrollo**: renombrados para una identificación más clara de dispositivos y acciones
- **Documentación FAQ**: actualizado `docs/FAQ.md` con el comportamiento actual de la aplicación

## Casos de uso reales

### Codificación remota

KeyCmd no es solo para gestión de servidores. Los desarrolladores lo usan para **sesiones de codificación remota** — controlando una máquina de desarrollo headless desde un teléfono o tableta, con teclado, panel táctil y teclado numérico completos.

## Qué no ha cambiado

**Teclado y Ratón Pro** (modo compuesto con barras Shortcut Hub, disposiciones divididas y rico comportamiento IME) sigue siendo la experiencia completa de antes. Todos los perfiles, ajustes preestablecidos y dispositivos vinculados existentes se conservan.

## Obtener la actualización

**Esta versión (0.19):** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

> **Aviso Beta:** La aplicación Android KeyCmd sigue en fase beta activa. El repositorio fuente aún no es público — planeamos hacerlo de código abierto después de una campaña de crowdfunding exitosa. Si eres un probador beta y necesitas el último APK, contáctanos en Discord y te enviaremos la versión.

Las instalaciones existentes se actualizan in situ.

## Compatible con Mini-KVM y KVM-Go

La aplicación KeyCmd no se limita al hardware KeyMod. Los usuarios existentes de Openterface también pueden probarla:

- **KVM-Go**: conexión por **Bluetooth** o **USB**
- **Mini-KVM**: conexión por **USB**

## Notas de actualización

- **Cambio de marca**: el nombre de la app cambia de KeyMod a KeyCmd. Tus datos se conservan.
- **Modo Compose**: nuevo para Teclado y Ratón Pro.
- **Guías interactivas**: pulsa el icono de guía (a la izquierda de la sección de conexión) en cualquier modo para iniciar la guía interactiva.
- **Idiomas**: ve a Configuración para cambiar el idioma de la aplicación. KeyCmd ahora soporta 11 idiomas de interfaz.

Saludos cordiales,

Openterface Team | TechxArtisan
