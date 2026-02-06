---
title: "Openterface Mini-KVM - Guía de autodiagnóstico (macOS)"
description: "Guía paso a paso para realizar autodiagnósticos en el dispositivo Openterface Mini-KVM con la app macOS. Aprenda cómo probar las conexiones USB, detectar problemas y enviar informes de defectos al soporte."
keywords: "Openterface Mini-KVM, macOS, autodiagnóstico, solución de problemas KVM, diagnósticos USB KVM, soporte Mini-KVM, prueba del dispositivo KVM, prueba de conexión USB, informe de defectos KVM, guía de solución de problemas Mini-KVM, herramienta de diagnóstico KVM, diagnósticos de servidores headless, herramientas de solución de problemas IT"
---

# Openterface Mini-KVM - Guía de autodiagnóstico (macOS)

Esta guía proporciona instrucciones paso a paso para realizar autodiagnósticos en el dispositivo Openterface Mini-KVM.

## Antes de comenzar

- **Actualizar la aplicación:** Asegúrese de tener la última versión de la [aplicación Openterface macOS](/app) instalada antes de ejecutar el diagnóstico. Verifique el menú de la aplicación para obtener actualizaciones.
- **Conectar el dispositivo:** Verifique que Mini-KVM esté correctamente conectado a los dispositivos Host y Target.
- **Mantener el objetivo inactivo:** Durante las pruebas (especialmente la Prueba de estrés), mantenga el dispositivo de destino inactivo y no lo use.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-K6Idzky3fY?si=r7pZgCkBzzZXgrLT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Unidad en buen estado

**Paso 1:** En la aplicación Openterface, abra Ajustes → Ajustes…

**Paso 2:** En la ventana de Ajustes, vaya a Avanzado y Depuración.

**Paso 3:** Haga clic en Abrir Herramienta de Diagnóstico.

**Paso 4:** Cuando se le pida, haga clic en Habilitar para activar el registro de diagnósticos.

**Paso 5:** Haga clic en Comprobar Ahora para iniciar el autodiagnóstico.

**Paso 6:** Haga clic en Iniciar Prueba, luego desconecte y vuelva a conectar el USB-C negro (lado objetivo) cuando se le indique.

![minikvm-support-target](https://assets.openterface.com/images/minikvm/support/target.webp)

**Paso 7:** Haga clic en Iniciar Prueba, luego desconecte y vuelva a conectar el USB-C naranja (lado anfitrión) cuando se le indique.

![minikvm-support-host](https://assets.openterface.com/images/minikvm/support/host.webp)

**Paso 8:** Haga clic en Iniciar Prueba y espere a que finalice la prueba.

**Paso 9:** Haga clic en Reiniciar Ahora y espere a que finalice.

**Paso 10:** Haga clic en Cambiar Ahora y espere a que finalice el cambio de velocidad baud.

**Paso 11:** Haga clic en Iniciar Prueba y espere aproximadamente 30 segundos. No opere el objetivo mientras se ejecuta la prueba.

> **Nota:** El ratón puede moverse rápidamente. No toque el objetivo.

![minikvm-support-stress_test](https://assets.openterface.com/images/minikvm/support/stress_test.gif)

**Paso 12:** Confirme que todos los elementos muestren marcas de verificación verdes y que el progreso esté completo.

**Paso 13:** Haga clic en ❌ (esquina superior derecha) para cerrar la ventana de Diagnóstico.

---

## Problema detectado (Ejemplo de teclado/ratón)

Primero siga los Pasos 1–11 en "Unidad en buen estado". Las notas a continuación explican lo que verá cuando se detecte un problema de teclado/ratón.

## Cómo se manifiesta este problema

En este ejemplo, la Conexión General muestra FALLA primero porque un problema de teclado/ratón (HID) en el lado objetivo afecta la comprobación general. Esto es un indicador temprano, no un problema separado (verá el estado FALLA resaltado junto a "Conexión General" a la izquierda).

- **Conexión General:** FALLA se muestra aquí primero debido al problema del lado objetivo.

![minikvm-support-overall_connection](https://assets.openterface.com/images/minikvm/support/overall_connection.webp)

- **Conexión Plug & Play del Objetivo:** Después de ejecutar este paso, el resultado puede mostrar con más claridad el problema del lado objetivo.

> **Consejo:** Si un paso muestra FALLA, los diagnósticos no se detendrán, pero puede que deje de avanzar automáticamente—por lo tanto, deberá continuar manualmente.

## Prueba final adicional (dependiendo del tipo de problema)

**Paso 12:** Después de la Prueba de Estrés, los diagnósticos pueden mostrar una prueba final adicional dependiendo del problema detectado; en este ejemplo de teclado/ratón, continúa con la Verificación del Puerto Objetivo.

**Paso 13:** Haga clic en "Detectar Dispositivos" para iniciar la Verificación del Puerto Objetivo, luego siga las instrucciones en pantalla.

![minikvm-support-target_port_checking](https://assets.openterface.com/images/minikvm/support/target_port_checking.webp)

## Qué ocurre cuando se detecta un problema

**Paso 14:** Para continuar, haga clic en Siguiente (barra inferior) o seleccione la siguiente prueba desde el panel izquierdo.

![minikvm-support-target_plug_n_play](https://assets.openterface.com/images/minikvm/support/target_plug_n_play.webp)

## Enviar registros al soporte

**Paso 15:** Haga clic en Enviar Informe de Defecto al Soporte para preparar el informe para soporte.

![minikvm-support-send_defect_report_to_support](https://assets.openterface.com/images/minikvm/support/send_defect_report_to_support.webp)

**Paso 16:** En la ventana de Informe de Defecto, ingrese su **Número de Pedido** y **Nombre**, luego haga clic en **Aplicar** para insertarlos en el borrador del correo electrónico.

**Paso 17:** Copie la dirección de correo y el borrador:
- Haga clic en **Copiar Email** para copiar la dirección de correo del soporte.
- Haga clic en **Copiar Borrador** para copiar el contenido del correo prellenado (incluyendo Número de Pedido + Nombre).
- Pegue ambos en su cliente de correo (Gmail/Outlook/etc.).

![minikvm-support-support](https://assets.openterface.com/images/minikvm/support/support.webp)

**Paso 18:** Haga clic en **Abrir Carpeta de Registros**. La herramienta indicará qué archivos adjuntar. **Adjunte solo los archivos de registro solicitados** (la carpeta puede contener muchos otros registros).

**Paso 19:** En el mismo correo, adjunte una **foto clara de la configuración** que muestre:
- el dispositivo Mini-KVM,
- ambas conexiones **Anfitrión** y **Objetivo**,
- puertos y cables claramente visibles.

**Paso 20:** Envíe el correo al soporte (texto del borrador + registros solicitados + foto de configuración adjuntos).

**Paso 21:** Haga clic en ❌ (esquina superior derecha) para cerrar la ventana de Diagnóstico.