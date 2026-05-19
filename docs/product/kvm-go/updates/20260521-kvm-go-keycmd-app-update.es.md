---
draft: false
date: 2026-05-21
title: "Actualización de KVM-GO: controla tu objetivo desde tu móvil con KeyCmd 0.19"
description: "Usa KeyCmd 0.19 con KVM-GO mediante USB o Bluetooth: teclados KM Basic y Pro, modo Compose, ajustes preestablecidos de gamepad, Shortcut Hub y controles de presentación, sin necesidad de dongle de vídeo para la entrada HID."
keywords: "KVM-GO KeyCmd, KeyCmd 0.19, aplicación KVM-GO Android, control móvil KVM-over-USB, Openterface KeyCmd, teclado virtual KVM, KVM-GO Bluetooth USB, modo KM Pro Compose, KVM-GO HDMI DP VGA, aplicación Openterface KVM, entrada KVM portátil"
author: "Openterface Team | TechxArtisan"
category: "Actualizaciones de Producto"
tags: ["KVM-GO", "KeyCmd", "Actualizaciones de Producto", "Android", "USB", "Bluetooth", "Teclado", "Gamepad", "Lanzamiento"]
featured: false
social:
  image: "https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp"
  title: "KVM-GO + KeyCmd 0.19 — controla tu objetivo desde tu móvil"
  description: "KeyCmd 0.19 se empareja con KVM-GO por USB o Bluetooth para teclado, ratón, gamepad, accesos directos y Compose, mientras que Openterface KVM gestiona el vídeo cuando lo necesitas."
---

# Actualización de KVM-GO: controla tu objetivo desde tu móvil con KeyCmd 0.19

Hola a todos:

Gracias por apoyar **KVM-GO** y por vuestra paciencia mientras las unidades pasan por producción y envío. Sabemos que muchos de vosotros todavía estáis esperando el hardware y queremos que vuestra configuración se sienta completa desde el primer día.

Junto con la aplicación **Openterface KVM** (vídeo y control KVM total en tu teléfono o tableta), hemos estado mejorando **KeyCmd**, nuestra aplicación complementaria para entrada de teclado, ratón, gamepad y accesos directos. **KeyCmd 0.19** es la versión que recomendamos hoy si usas KVM-GO. Emparéjala mediante **USB** o **Bluetooth**, instálala sobre cualquier versión anterior y tus ajustes, perfiles y dispositivos emparejados se mantendrán.

![KVM-GO en un portátil con el teclado KeyCmd en un móvil](https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp){:style="max-width:720px;width:100%;height:auto"}

A continuación explicamos qué hace KeyCmd con KVM-GO, qué modo abrir para cada tarea y cómo sacarle el máximo partido en una máquina objetivo real.

![Pantalla de bienvenida de KeyCmd](https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape_1.webp){:style="max-height:320px;width:auto"}

## Modos y cómo usarlos

### Teclado y ratón (Basic)

Abre esto cuando quieras un **teclado simple a pantalla completa** y nada más que se interponga en el camino.

**Ideal para:** contraseñas de BIOS, comandos cortos de shell, entrada de teclado numérico o control del ratón con un panel táctil grande mientras KVM-GO te muestra la pantalla.

**Cómo usarlo:**

- Abre **KM Basic** desde el menú de navegación.
- Usa el teclado en pantalla, el **teclado numérico** (vertical u horizontal) o la pestaña de **panel táctil** según sea necesario.
- En **Ajustes**, elige **teclas modificadoras persistentes** (toca para bloquear Shift/Ctrl) o modificadores **estilo acorde** si prefieres combos de mantener y tocar.

**Por qué ayuda:** más espacio en pantalla para las teclas, menos interfaz, más rápido cuando solo necesitas entrada y no accesos directos.

![Teclado KM Basic a pantalla completa](https://assets2.openterface.com/images/keymod/KM-Basic-Keyboard_1.webp){:style="max-height:320px;width:auto"}

![Teclado numérico KeyCmd en horizontal](https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape_1.webp){:style="max-height:320px;width:auto"}

### Teclado y ratón (Pro)

![Teclado dividido KM Pro en horizontal](https://assets2.openterface.com/images/keymod/KM-Pro-Keyboard-landscape-split_1.webp){:style="max-height:320px;width:auto"}

![Teclado y panel táctil KeyCmd en vertical](https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait_1.webp){:style="max-height:320px;width:auto"}

Abre esto para el **trabajo de control diario** en máquinas conectadas a KVM-GO: teclados divididos, IME, barras de Shortcut Hub y el editor **Compose**.

**Ideal para:** sesiones de escritura más largas, macros y accesos directos, envío de bloques de texto o scripts al host mientras ves el resultado en la vista KVM.

![Modo Compose enviando un script](https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait_1.webp){:style="max-height:320px;width:auto"}

Vale la pena probar **Compose** si sueles pegar comandos o scripts: escribe en tu móvil, revisa y luego envíalo como pulsaciones de teclas al host. Esta [breve demostración en YouTube](https://www.youtube.com/watch?v=_rJF-hTF3_E) muestra el flujo completo.

**Cómo usarlo:**

- Abre **KM Pro** desde el menú de navegación.
- Usa el teclado y el panel táctil como en Basic, además de las categorías de **Shortcut Hub** en la parte superior para acciones de un solo toque configuradas en los perfiles.
- Abre **Compose** para redactar textos largos en tu móvil, revísalos y luego haz clic en **enviar** como pulsaciones de teclas HID. Los envíos largos muestran una barra de progreso. Si tu texto tiene caracteres no ASCII, la aplicación te avisará antes de enviar para que compruebes la compatibilidad del host (especialmente útil en macOS).

**Por qué ayuda:** un único lugar para escribir, señalar, usar accesos directos y flujos de trabajo tipo "pegar" sin tener que llevar un teclado físico a la máquina objetivo.

### Gamepad

Abre esto cuando quieras un diseño de **mando virtual** en pantalla, ajustado para juegos o cualquier aplicación en el objetivo que espere un gamepad.

**Ideal para:** emuladores, juegos casuales o una superficie de control compacta con sticks y botones mientras KVM-GO gestiona la pantalla.

**Cómo usarlo:**

- Cambia al modo **Gamepad**.
- Toca **Preset** en la barra de herramientas para **alternar** entre los diseños guardados. **Mantén pulsado Preset** para abrir la lista completa, **importar/exportar** o **añadir módulos** (sticks, botones, paneles táctiles).
- Empieza con el ajuste preestablecido **emu-6** incluido y edítalo desde ahí. Puedes añadir **varios paneles táctiles** y módulos de stick adicionales en un mismo diseño.

**Por qué ayuda:** no estás limitado a un único diseño de fábrica; guarda diseños por juego o por máquina y comparte los ajustes con otros.

![Diseño preestablecido de Gamepad](https://assets2.openterface.com/images/keymod/Gamepad-perset-1_1.webp){:style="max-height:320px;width:auto"}

![Ajuste preestablecido de Gamepad usado en Minecraft](https://assets2.openterface.com/images/keymod/Gamepad-perset-minecraft_1.webp){:style="max-height:320px;width:auto"}

*Ajuste preestablecido personalizado para Minecraft.*

### Shortcut Hub

Este es el hogar de los **perfiles y accesos directos** dentro de KM Pro: categorías, paneles de detalles y los accesos directos que asignas a las barras.

**Ideal para:** operaciones repetitivas en el objetivo (abrir terminal, pegar una cadena de comandos, cambiar ajustes) mientras KVM-GO sigue conectado para el vídeo.

**Cómo usarlo:**

- Desde KM Pro, trabaja en el perfil **Default** (o el tuyo propio).
- Usa las pestañas de categorías y la interfaz de detalles para gestionar los accesos directos.
- Realiza el **recorrido guiado por Shortcut Hub** si es la primera vez que ves cómo se organizan los perfiles.

### Presentación

Una superficie de control más simple tipo **presentador**, mantenida en **vertical** para que los botones no salten al girar el móvil.

**Ideal para:** pasar diapositivas o controles de presentación ligeros en el objetivo.

![Modo presentación controlando Google Slides](https://assets2.openterface.com/images/keymod/KeyCmd-Presentation-Google-Slides.webp){:style="max-height:320px;width:auto"}

---

## Idiomas

La interfaz de la aplicación está disponible en **11 idiomas**. Incorporaciones recientes: coreano, italiano, ruso y portugués brasileño.

Abre **Settings** → **App language** para cambiar de idioma.

---

## Obtén KeyCmd 0.19 y conéctate a KVM-GO

**Descarga:** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

Instálala sobre tu aplicación actual si ya tienes una. No es necesario borrar los datos.

**Conexión a KVM-GO (el puerto de vídeo puede quedarse desconectado):**

Para las **tres variantes de KVM-GO** (HDMI, VGA y DP), no es necesario conectar el **conector de vídeo del dongle** a nada para la entrada de KeyCmd. El puerto HDMI, VGA o DP puede quedarse vacío. Elige una de las siguientes configuraciones.

**Opción A — Bluetooth (el objetivo alimenta al KVM-GO)**

1. Conecta el **cable USB negro corto** al puerto **Target** del KVM-GO y a la máquina que vas a controlar. Esa conexión por sí sola **alimenta** al KVM-GO.
2. En tu móvil, abre **KeyCmd** y busca el KVM-GO mediante **Bluetooth**.

**Opción B — USB a tu móvil Android (puerto Host)**

1. Conecta el **cable naranja largo** desde el puerto **Host** del KVM-GO a tu móvil Android.
2. Abre **KeyCmd** y conéctate mediante **USB** en la aplicación.

![Puerto Target del KVM-GO conectado a un portátil mediante el cable USB negro corto](https://assets2.openterface.com/images/kvm-go/kvm-go-target-port-laptop-power.webp){:style="max-height:360px;width:auto"}

Para vídeo a pantalla completa más entrada, usa **Openterface KVM** para la pantalla del objetivo y **KeyCmd** para teclado, ratón y accesos directos. KeyCmd por sí solo es suficiente cuando el objetivo ya tiene su propia pantalla y solo necesitas entrada.

**También funciona con Mini-KVM** mediante USB si usas ambos dispositivos.

> **Todavía en fase beta.** Los ajustes preestablecidos del gamepad y los envíos de Compose pueden comportarse de forma diferente según el SO del host. Si ocurre algo extraño con KVM-GO, ponte en contacto con nosotros en **Discord** con una captura de pantalla, tu variante de KVM-GO (HDMI / DP / VGA) y lo que esperabas que ocurriera.

> **Código fuente:** Aún no es público. Tenemos previsto abrirlo tras alcanzar los hitos de crowdfunding en proyectos relacionados. Pregunta en Discord si necesitas ayuda para encontrar el APK.

---

## Acerca de KeyMod (opcional, independiente de KVM-GO)

También estamos desarrollando **[KeyMod](https://openterface.com/product/keymod/)**, un dongle HID dedicado para USB y Bluetooth para la misma aplicación KeyCmd. Los patrocinadores de KVM-GO no necesitan KeyMod para los flujos de trabajo anteriores; KeyCmd sobre KVM-GO es el camino que queremos que sigas ahora.

Si tienes curiosidad por un dongle independiente para configuraciones sin KVM, puedes seguir la [campaña de KeyMod en Crowd Supply](https://www.crowdsupply.com/techxartisan/openterface-keymod). Eso es independiente del cumplimiento de KVM-GO.

---

## Nos encantaría conocer tu opinión

Si tienes unos minutos, instala **KeyCmd 0.19**, conéctalo a tu KVM-GO (o Mini-KVM) y cuéntanos qué te sigue pareciendo incómodo. Los informes de casos de uso de "crash-cart" y laboratorios domésticos van directos a nuestras próximas versiones.

Formas prácticas de ayudar al proyecto KVM-GO:

- **Comparte lo que funciona** en Discord o en tu comunidad (consejos de BIOS, emparejamiento Bluetooth, modos favoritos).
- **Cuéntaselo a algún colega** que trabaje con equipos sin monitor y que podría usar un KVM de bolsillo.
- **Sigue enviando comentarios honestos**, especialmente sobre los puntos a mejorar. Eso da más forma al producto que los simples ánimos.

Gracias de nuevo por apoyar KVM-GO y por ayudarnos a que el KVM-over-USB portátil sea mejor para todos.

Atentamente,

**Openterface Team | TechxArtisan**
