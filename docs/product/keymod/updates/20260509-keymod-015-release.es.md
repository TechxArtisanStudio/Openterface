---
draft: false
date: 2026-05-09
title: "KeyMod 0.15: Pipeline de Preajustes de Gamepad, Teclado y Ratón (Basic), Diseños Multi-Touchpad"
description: "KeyMod 0.15 incluye la pipeline de preajustes de gamepad con esquema v7, diseños multi-touchpad, el nivel Teclado y Ratón (Basic) con teclado de pantalla completa, y marca KeyMod en toda la app. Un gran paso hacia una experiencia de entrada pulida."
keywords: "KeyMod 0.15, KeyMod lanzamiento, preajuste gamepad, multi-touchpad, teclado ratón basic, marca KeyMod, Openterface KeyMod actualización, emulador HID, gamepad virtual, app teclado Android"
author: "TechxArtisan Studio"
category: "Actualizaciones del Producto"
tags: ["KeyMod", "Actualizaciones del Producto", "Lanzamiento", "Gamepad", "Teclado", "Android"]
featured: false
social:
  image: "https://assets.openterface.com/images/keymod/keymod-015-release.jpg"
  title: "KeyMod 0.15 lanzamiento — preajustes gamepad, nivel basic, multi-touchpad"
  description: "KeyMod 0.15 trae la pipeline de preajustes de gamepad v7, un nivel dedicado de Teclado y Ratón (Basic), diseños multi-touchpad y nueva marca KeyMod."
---

# KeyMod 0.15: Pipeline de Preajustes de Gamepad, Teclado y Ratón (Basic), Diseños Multi-Touchpad

KeyMod **0.15** (`versionCode` **15**) es un lanzamiento de referencia que incluye tres características principales: la **pipeline de preajustes de gamepad** con esquema de diseño **v6-v7**, el nivel dedicado **Teclado y Ratón (Basic)** y diseños **multi-touchpad**. Esta actualización también trae marca **KeyMod** completa en el flujo de bienvenida y los artefactos de compilación.

## Gamepad: Pipeline de Preajustes v7

El gamepad ahora utiliza un **sistema de preajustes** que te permite guardar, cargar, importar y exportar diseños de controlador personalizados.

### Qué cambió

- **Preset store v7** reemplaza los diseños integrados anteriores. Los preajustes de fábrica clásicos (`preset_classic_*`) y **Two buttons** (`preset_two_buttons`) han sido eliminados del disco. Solo **`preset_default`** permanece como diseño de fábrica protegido contra eliminación.
- **Esquema v7** hace que **`stick_left`** sea opcional. Un diseño puede no tener ningún módulo de pulgar izquierdo. El menú **Add module** inserta **`stick_left`**, **`stick_left_2`**, **`stick_left_3`**, etc.
- **Soporte multi-touchpad**: los preajustes pueden incluir múltiples touchpads (`touchpad_1`, `touchpad_2`). Agregar un touchpad asigna el siguiente id disponible con un ancla ligeramente desplazada. Los botones de ratón L/M/R incluidos se comparten entre todos los touchpads.
- **Tamaño de botones del ratón en touchpad**: los botones del ratón ahora usan un radio de dibujo predeterminado mayor. Puedes ajustar el tamaño con pulsación larga **Mouse button size** en el touchpad, o **This button size** en módulos de ratón individuales.
- **Valores predeterminados del stick auxiliar**: **`stick_left_2+`** por defecto a D-pad cruz + mapeo WASD.

### Gestión de preajustes

- **Toca** el chip Preset en la barra de herramientas para ciclar entre diseños disponibles
- **Pulsación larga** para la lista completa de preajustes con opciones de importación, agregar módulo y exportar
- El diseño **emu-6** incluido viene como preajuste inicial
- El creador de exportación soporta i18n para compartir preajustes entre idiomas

## Teclado y Ratón (Basic)

Un nivel dedicado de teclado de pantalla completa diseñado para escritura enfocada sin el encabezado de la app.

### Lo que obtienes

- **Teclado de pantalla completa** sin el encabezado principal de la app para más espacio en pantalla
- **Numpad en vertical y horizontal**: cuadrícula 5x8 en vertical (PrtSc / ScrLk / Pause / Home / End), cuadrícula 8x5 en horizontal con + alto, Enter y 00
- **Puerta de envío ASCII-only IME**: escribe texto largo en modo compose, envíalo como pulsaciones HID limpias
- **Repetición con pulsación larga**: mantén presionadas teclas de caracteres/función para auto-repetición (~400ms de retardo, ~50ms de repetición)
- **Vista previa de tecla**: burbuja flotante muestra la etiqueta efectiva sobre la tecla al presionar
- **Retroalimentación háptica** y superficies de teclas con **tema adaptable**

### Modificadores Sticky vs Chord

Los ajustes te permiten elegir entre **modificadores sticky** (tocar para fijar) y **momentáneo + chord con pulsación larga** (predeterminado) para el teclado Basic.

## Marca

- El nombre de visualización de la app ahora es **KeyMod**
- La pantalla de bienvenida muestra el logotipo **KeyMod**
- Los artefactos CI y nombres de archivos APK usan el prefijo **KeyMod**
- `applicationId` permanece como **`com.openterface.keymod`** para actualizaciones in-place

## Qué permanece sin cambios

**Teclado y Ratón Pro** (modo compuesto con tiras de Shortcut Hub, diseños divididos y comportamiento IME enriquecido) sigue siendo la experiencia completa de siempre.

## Obtener la actualización

**Esta versión (0.15):** [KeyMod-release-0.15.apk](https://assets2.openterface.com/data/KeyMod-release-0.15.apk)

También puedes obtener compilaciones desde [GitHub Releases](https://github.com/TechxArtisanStudio/Openterface_KeyMod_Android/releases) o [GitHub Actions](https://github.com/TechxArtisanStudio/Openterface_KeyMod_Android/actions). Las instalaciones existentes se actualizan in-place.

## Notas de actualización

- **Gamepad**: tu preferencia anterior de dos botones activa automáticamente el preajuste **Two buttons** en el primer inicio. Usa **Preset** (toca para ciclar, pulsación larga para la lista) en lugar del antiguo control 1 Button / 2 Buttons.
- **Teclado y Ratón (Basic)**: abre Basic para experimentar el teclado de pantalla completa. El modo Pro está disponible desde el cajón de navegación para la experiencia completa de Shortcut Hub.

Saludos cordiales,

Openterface Team | TechxArtisan
