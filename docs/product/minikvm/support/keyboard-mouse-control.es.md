---
title: "Solución de problemas de control de teclado y ratón - Openterface Mini-KVM"
description: "Guía de solución de problemas para problemas de control de teclado y ratón de Openterface Mini-KVM. Aprenda a solucionar problemas de comunicación HID, conexiones de cable incorrectas, problemas de hub USB y estados zombie del chip HID."
keywords: "Openterface Mini-KVM, solución problemas teclado ratón, problemas HID KVM, teclado ratón no funciona, soporte Mini-KVM, solución problemas USB KVM, reset chip HID, problemas control KVM, teclado ratón no responde, solución problemas Openterface, problemas dispositivo KVM, problemas hub USB, velocidad baudios KVM, errores comunicación serie"
---

# **Solución de problemas de teclado y ratón que no pueden controlar la computadora de destino**

Ocasionalmente, los usuarios pueden experimentar situaciones donde las funciones de teclado y ratón del dispositivo Openterface no funcionan como se esperaba. Este documento describe las causas más comunes y cómo resolverlas o prevenirlas.

**Retroalimentación del software:** Cuando Openterface no puede establecer comunicación HID debido a una conexión de destino faltante o incorrecta, la interfaz destaca el estado para que pueda actuar rápidamente.

- En **macOS**, el icono de teclado y ratón en la esquina superior derecha de la utilidad Openterface se vuelve **naranja**.  

    <img src="https://assets.openterface.com/images/software/inactive_keyboardmoue_macos.webp" alt="Inactive keyboard and mouse (macOS)" width="200" />

- En **Windows/Linux**, el icono correspondiente en la parte inferior de la ventana se vuelve **rojo**.  

    <img src="https://assets.openterface.com/images/software/inactive_keyboardmoue_windows.webp" alt="Inactive keyboard and mouse (Windows)" width="200" />

El vídeo sigue apareciendo en Openterface pero el teclado y el ratón no responden — puedes ver el escritorio de destino pero no controlarlo. Esto usualmente significa que la comunicación HID no se ha establecido (por ejemplo, cable de destino incorrecto, concentrador sin alimentación o chip HID defectuoso); consulta la lista de verificación y las secciones a continuación. El software también bloquea las conexiones adicionales de teclado/ratón hasta que se resuelva el cableado/problema.

---

## **1. Conexión de cable incorrecta**

**Problema:**  
Sorprendentemente común: los usuarios olvidan conectar el puerto Openterface Target Type-C a la computadora de destino.

**Solución:**  
✅ Siempre verifica:
- El **cable Type-C de destino** está conectado de forma segura desde el **puerto de destino** de Openterface a la **computadora de destino** que deseas controlar.
- El **cable USB-A/USB-C del anfitrión** está conectado a tu **computadora anfitrión/controladora** (donde se ejecuta OpenterfaceQt o el software de control).

> **Consejo:** Etiqueta los cables para evitar confusión en configuraciones complejas.
- Conecta el cable negro al lado negro del conector de destino.
- Conecta el cable naranja al lado cubierto de naranja del conector de destino.


## **2. Uso de concentradores USB sin alimentación**

**Problema:**  
Conectar Openterface a través de un concentrador USB sin alimentación puede causar **suministro de energía insuficiente** (caída de tensión VBUS). Esto puede causar que el dispositivo funcione de manera errática o no inicialice las funciones HID (teclado/ratón).

**Solución:**  
✅ **Evita los concentradores USB sin alimentación** entre Openterface y la computadora de destino.  
✅ Si es necesario un concentrador, utiliza un **concentrador USB de alta calidad alimentado externamente** que pueda entregar alimentación 5V estable.

> **Nota:** El suministro de energía USB es fundamental para el funcionamiento confiable del chip HID. Las caídas de tensión pueden desencadenar fallos internos.

---

## **3. El chip HID entra en "estado zombie"**

**Problema:**  
En ciertas condiciones — como ráfagas de comandos rápidos combinadas con alimentación marginal — el chip HID interno (por ejemplo, CH9329) puede entrar en un **"estado zombie".** En este estado:
- El chip HID se bloquea y detiene el envío de datos de respuesta en serie a la computadora anfitriona.
- Mantiene un estado de error interno que evita la reinicialización normal por parte del software anfitrión.
- El dispositivo puede parecer conectado (video presente) mientras las entradas permanecen sin respuesta.
- El software anfitrión (por ejemplo, OpenterfaceQt) no puede reinicializar correctamente el dispositivo.
- Volver a conectar todos los cables o el ciclo de energía de la conexión USB típicamente no borra este error interno; se requiere un reinicio de fábrica del chip HID.

**Solución:**  
Realiza un **reinicio de fábrica del chip HID**:

- En **macOS**: Utiliza la **Herramienta de reinicio en serie** disponible en el **Menú Avanzado** de la utilidad macOS.  

    <img src="https://assets.openterface.com/images/software/MacOS_FactoryResetHID.webp" alt="Serial Reset Tool (macOS)" width="150" />

- En **OpenterfaceQt** (aplicación de escritorio): Ve a **Menú Avanzado → Reinicio de fábrica del chip HID**.

    <img src="https://assets.openterface.com/images/software/OpenterfaceQT_FactoryResetHID.webp" alt="Factory Reset HID Chip (OpenterfaceQt)" width="150" />

> Esto borra el estado interno del chip y restaura el funcionamiento normal.

---

## **4. Sensibilidad de la velocidad en baudios en entornos ruidosos**

**Problema:**  
Openterface utiliza de forma predeterminada una velocidad en baudios de **115200 bps** para una transmisión de datos de ratón más rápida. Sin embargo, en entornos eléctricamente ruidosos (por ejemplo, fuentes de alimentación conmutada o cables largos/sin blindaje), esta velocidad en baudios alta puede provocar **errores de comunicación en serie**, causando la pérdida o corrupción de comandos HID.

**Solución:**  
Cambia a una velocidad en baudios de **9600 bps**:
- Esto mejora significativamente la **confiabilidad de la comunicación** en configuraciones ruidosas.
- El impacto en la latencia es **insignificante** bajo un uso típico (por ejemplo, captura de vídeo a 30 fps y control).

> **Recomendación:** Si experimentas fallos de entrada intermitentes sin problemas de alimentación o conexión, intenta reducir la velocidad en baudios en la configuración de Openterface.

---

## **Lista de verificación de resumen**

Si el teclado/ratón no funciona:

1. ✅ Confirma que el **cable Type-C de destino** correcto esté conectado a la **computadora de destino**.
2. ✅ Evita los concentradores USB sin alimentación — utiliza una conexión directa o un **concentrador con alimentación**.
3. ✅ Si el dispositivo parece "congelado", **reinicia el chip HID** a través del software.
4. ✅ En entornos inestables, **reduce la velocidad en baudios a 9600** para una comunicación más robusta.
5. ✅ Si los intentos anteriores no ayudan, intenta un puerto USB diferente en el anfitrión o reinicia la computadora anfitriona — el sistema operativo puede deshabilitar un puerto o el concentrador después de recibir demasiados paquetes de error USB. Cambiar de puertos o reiniciar el anfitrión generalmente restaura la conexión.

---

Al abordar estas cuatro áreas, la mayoría de los problemas intermitentes de HID se pueden prevenir o resolver rápidamente. Para problemas persistentes, comuníquese con el soporte (support@openterface.com) con los detalles de su configuración y registros.
