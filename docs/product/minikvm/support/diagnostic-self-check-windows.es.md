---
title: "Openterface Mini-KVM (Windows) - Guía de autodiagnóstico de hardware"
description: "Guía paso a paso para realizar el autodiagnóstico de hardware en la aplicación Openterface para Windows. Aprenda cómo probar las conexiones USB, detectar problemas y enviar informes de diagnóstico al soporte."
keywords: "Openterface Mini-KVM, Windows, autodiagnóstico de hardware, solución de problemas KVM, diagnósticos USB KVM, soporte Mini-KVM, prueba del dispositivo KVM, Windows KVM, informe de defectos KVM, guía de solución de problemas Mini-KVM"
---

# Openterface Mini-KVM (Windows) — Guía de autodiagnóstico de hardware

Esta guía explica cómo ejecutar el autodiagnóstico de **Hardware** en la versión **Windows** de la aplicación Openterface, y cómo enviar el informe de diagnóstico al soporte si se detecta un problema.

<iframe width="560" height="315" src="https://www.youtube.com/embed/uSq3BDc_SBU?si=rREugsUxX1FzDGqm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Antes de comenzar

- **Actualizar la aplicación:** Asegúrese de tener la última versión de la [aplicación Openterface para Windows](/app) instalada antes de ejecutar el diagnóstico. Verifique el menú de la aplicación para obtener actualizaciones.
- Conecte Mini-KVM a **Host** y **Objetivo**.
- Mantenga el dispositivo objetivo inactivo durante las pruebas (especialmente durante la Prueba de Estrés).

> **Importante (Windows):** Los diagnósticos **no avanzan automáticamente**.  
> Para moverse entre pruebas, use **Siguiente** (barra inferior) **o** haga clic en un elemento de prueba en el **panel izquierdo**.  
> Cada prueba se ejecuta haciendo clic en **Comprobar Ahora**.

![next_webp](https://assets2.openterface.com/images/next.webp)

---

## Unidad en buen estado (PASS)

### Paso 1 — Abrir Hardware Diagnostics (Windows)
En la aplicación Openterface para Windows, abra: **Avanzado → Hardware Diagnostics**.  

### Paso 2 — Ejecutar el autodiagnóstico
En la ventana de Hardware Diagnostics, haga clic en **Comprobar Ahora** para ejecutar el paso de diagnóstico actual.  

### Paso 3 — Target Plug & Play (seguir las instrucciones)
Cuando **Target Plug & Play** le pida reconectar el cable objetivo, siga las instrucciones en pantalla.  
Algunas configuraciones pueden pedirle **desconectar/reconectar más de una vez** (por ejemplo, dos veces).  

![Target-plug&play](https://assets2.openterface.com/images/Target-plug%26play.webp)

### Paso 4 — Host Plug & Play (seguir las instrucciones)
Siga las instrucciones en pantalla para el lado anfitrión.  

![Host-plug&play](https://assets2.openterface.com/images/Host-plug%26play.webp)

### Paso 5 — Prueba de Estrés (no tocar el objetivo)
Durante la **Prueba de Estrés**, el ratón del objetivo puede moverse automáticamente para la detección.  
**No opere el objetivo** mientras se ejecuta la prueba.  

> **Nota:** El ratón puede moverse rápidamente — no toque el objetivo.

![stress-test](https://assets2.openterface.com/images/stress-test.webp)

### Paso 6 — Confirmar PASS
Continúe hasta que se complete el autodiagnóstico. Si todo es normal, los resultados mostrarán **PASS / Todas las pruebas pasadas**.  

---

## Problema detectado (Ejemplo de teclado/ratón)

Si se detecta un problema, uno o más elementos pueden mostrar **FALLA**.

### Paso 1 — Ejecutar el mismo Hardware Diagnostics
Abra **Avanzado → Hardware Diagnostics**, luego haga clic en **Comprobar Ahora** para iniciar.  

### Paso 2 — Continuar con las comprobaciones
Continúe con las pruebas restantes hasta que finalicen los diagnósticos.  

### Paso 3 — El correo de soporte se abre automáticamente
Cuando los diagnósticos finalicen con un problema, se abrirá automáticamente una ventana de **Correo de Soporte**.  

---

## Enviar registros al soporte (Windows)

### Paso 4 — Aplicar Número de Pedido + Nombre
Ingrese su **Número de Pedido** y **Nombre**, luego haga clic en **Aplicar** para insertarlos en el borrador del correo. 

![ID+Name](https://assets2.openterface.com/images/ID+Name.webp)

### Paso 5 — Copiar dirección de correo y borrador
- Haga clic en **Copiar Email** para copiar la dirección de correo del soporte.
- Haga clic en **Copiar Borrador** para copiar el contenido del correo prellenado (incluyendo Número de Pedido + Nombre).  
Pegue ambos en su cliente de correo (Gmail/Outlook/etc.).  

![copy](https://assets2.openterface.com/images/copy.webp)

### Paso 6 — Adjuntar los archivos de registro correctos
Haga clic en **Abrir Carpeta de Archivos**. La herramienta indicará qué archivos adjuntar.  
**Adjunte solo los archivos de registro solicitados** (la carpeta puede contener muchos otros registros).  

![list](https://assets2.openterface.com/images/list.webp)

![compress](https://assets2.openterface.com/images/compress.webp)

### Paso 7 — También adjuntar una foto de la configuración
En el mismo correo, adjunte una **foto clara de la configuración** que muestre:
- el dispositivo Mini-KVM,
- ambas conexiones **Anfitrión** y **Objetivo**,
- puertos y cables claramente visibles.  

### Paso 8 — Enviar el correo
Envíe el correo al soporte (texto del borrador + registros solicitados + foto de configuración adjuntos).  

---

## Qué incluir al contactar al soporte

- **Número de Pedido**
- **Archivos de registro de diagnóstico solicitados**
- **Foto de la configuración** (Mini-KVM + cableado host/objetivo)
