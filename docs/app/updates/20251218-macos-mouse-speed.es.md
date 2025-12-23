---
title: Velocidad del ratón y rendimiento en juegos de Openterface Mini-KVM en macOS
description: Pruebas completas del rendimiento del ratón orientadas al gaming para Openterface Mini-KVM en macOS. Comparación de los modos Absolute, Relative Event y Relative HID, con velocidades en baudios de 9600 frente a 115200, para una configuración óptima para juegos.
keywords: Openterface Mini-KVM, velocidad del ratón, rendimiento en juegos, macOS KVM, tasa de sondeo del ratón, ratón gaming, modo de ratón HID, modo de ratón absoluto, modo de ratón relativo, velocidad en baudios 115200, velocidad en baudios 9600, KVM gaming, ratón de baja latencia, pruebas de ratón gaming, rendimiento del ratón en macOS, rendimiento serial, latencia del ratón, configuración de juegos, gaming competitivo, respuesta del ratón
author: Openterface
date: 2025-12-18
tags:
  - gaming
  - mouse-performance
  - macOS
  - Mini-KVM
  - technical-review
  - hardware-testing

---

# Velocidad del ratón y rendimiento en juegos de Openterface Mini-KVM en macOS

### Análisis del comportamiento del ratón orientado al gaming

Este artículo resume las pruebas de rendimiento del ratón en condiciones reales para **Openterface Mini-KVM en macOS**, con un enfoque en el **comportamiento del ratón en juegos**, las limitaciones del baud rate serial y las configuraciones recomendadas.

<blockquote class="twitter-tweet" data-media-max-width="560"><p lang="en" dir="ltr">Gaming isn't the main goal of Openterface KVMs, but we pushed them to explore the limits of KVM-over-USB. On macOS, 115200 baud + Relative HID gives the best mouse latency. Built for setup and debugging, tuned to stretch performance further. <a href="https://t.co/ianurD9ArL">pic.twitter.com/ianurD9ArL</a></p>&mdash; TechxArtisan (@TechxArtisan) <a href="https://twitter.com/TechxArtisan/status/2003418343806742992?ref_src=twsrc%5Etfw">December 23, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---

## 1. Software y entorno de pruebas

### Software

* **Aplicación en el host:**
  **Openterface para macOS v1.21** *(en desarrollo)*

* **Herramienta de medición en el sistema objetivo:**
  Una **aplicación interna personalizada**, desarrollada para medir con precisión las entradas de ratón de alta frecuencia y las tasas de procesamiento de eventos en el sistema objetivo.

> ⚠️ Dado que la versión v1.21 aún está en desarrollo activo, algunos comportamientos y características de rendimiento pueden mejorar en versiones futuras.

---

### Condiciones de prueba: limitación de la velocidad del ratón

**No se aplicó ninguna limitación de velocidad del ratón ni restricción artificial de la tasa** durante las pruebas.

La entrada del ratón se capturó y se reenviò a la **velocidad nativa del dispositivo**, limitada únicamente por:

* Tasa de sondeo del hardware del ratón
* Modo de ratón seleccionado (Absolute / Relative Event / Relative HID)
* Baud rate serial
* Gestión de la entrada del ratón por parte del sistema operativo objetivo

---

## 2. Fundamentos del rendimiento de datos del ratón

Cada evento de movimiento del ratón transmitido a través de Mini-KVM consta de:

```
11 bytes = 88 bits
```

### Rendimiento serial teórico

| Velocidad en baudios | Eventos máx. / segundo |
| -------------------- | ---------------------- |
| 9600                 | ~109 eventos/s         |
| 115200               | ~1309 eventos/s        |

⚠️ Estos valores representan **límites teóricos superiores**.
El rendimiento real está influenciado por:

* Tasa de sondeo del ratón en el host
* Modo del ratón (Absoluto vs Relativo)
* Programación de eventos de entrada en macOS
* Buffering serial y gestión del firmware
* **Tasa de sondeo del ratón en el sistema objetivo**, que puede afectar significativamente la sensación de respuesta (por ejemplo, tasas predeterminadas bajas en algunas distribuciones de Linux)

---

## 3. Resultados de las pruebas

---

### A. Modo de ratón absoluto (9600 y 115200 baudios)

| Tipo de ratón | Baud rate | Frecuencia host (Hz) | Frecuencia objetivo (Hz) | Notas                                                                   |
| ------------- | --------- | -------------------- | ------------------------ | ----------------------------------------------------------------------- |
| Bluetooth     | 9600      | ~125                 | ~75                      | Banda serial saturada; entradas en cola, movimiento retrasado           |
| Con cable     | 9600      | ~150                 | ~75                      | Banda serial saturada; entradas en cola, movimiento retrasado           |
| Gaming        | 9600      | ~1000                | ~75                      | Entradas de alta frecuencia fuertemente en cola; respuesta muy reducida |
| Bluetooth     | 115200    | ~125                 | ~125                     | Mapeo estable 1:1 host–objetivo                                         |
| Con cable     | 115200    | ~175                 | ~175                     | Rendimiento mejorado; latencia perceptible en movimientos rápidos       |
| Gaming        | 115200    | ~1000                | ~350                     | Límite del rendimiento serial alcanzado; entradas excedentes en cola    |

**Conclusión (modo absoluto):**

El modo de ratón absoluto escala con el baud rate, pero sigue estando limitado por el **rendimiento serial y el buffering de las entradas**.
A **9600 baudios**, todos los tipos de ratón están limitados y el movimiento se retrasa.
A **115200 baudios**, los ratones estándar logran un comportamiento estable, pero **los ratones gaming con altas tasas de sondeo aún superan el ancho de banda disponible**, introduciendo latencia.

**El modo absoluto es adecuado para el control de escritorio, no para juegos sensibles a la latencia.**

---

### B. Modo Relative Mouse Event

El modo Relative Mouse Event captura **los eventos de movimiento del ratón directamente desde la ventana del sistema operativo**, calcula el **delta de movimiento entre posiciones consecutivas del cursor** y envía solo los datos de movimiento relativo al sistema objetivo.

Este modo:

* **No requiere permisos adicionales del sistema**
* Es independiente de las **coordenadas absolutas de la pantalla**
* Se beneficia de una **ventana de captura más grande**, permitiendo deltas de movimiento más finos
* Evita el buffering de posiciones absolutas, lo que resulta en **menor latencia y mejor capacidad de respuesta**

#### Rendimiento del modo Relative Mouse Event

| Tipo de ratón | Baud rate | Frecuencia host (Hz) | Frecuencia objetivo (Hz) | Notas                                                           |
| ------------- | --------- | -------------------- | ------------------------ | --------------------------------------------------------------- |
| Bluetooth     | 9600      | ~100                 | ~90                      | Cerca del límite serial; estable para uso casual                |
| Con cable     | 9600      | ~125                 | ~90                      | Banda serial saturada; latencia menor                           |
| Gaming        | 9600      | ~1000                | ~100                     | El alto sondeo excede la banda; entradas comprimidas            |
| Bluetooth     | 115200    | ~125                 | ~125                     | Mapeo 1:1 host–objetivo                                         |
| Con cable     | 115200    | ~180                 | ~150                     | Rendimiento mejorado; seguimiento suave                         |
| Gaming        | 115200    | ~1000                | ~450                     | Mejor rendimiento observado; limitado por el rendimiento serial |

🔴 **9600 baudios es insuficiente para ratones gaming de alto sondeo**
🟢 **115200 baudios permite una entrada reactiva de nivel gaming en el modo Relative Event**

---

### C. Modo Relative Mouse HID

El modo Relative Mouse HID **convierte directamente la entrada HID del ratón en macOS en eventos HID en el sistema objetivo**, evitando el procesamiento del cursor a nivel de ventana y el mapeo de coordenadas absolutas.

Este modo:

* Opera con **eventos de ratón en bruto a nivel HID**
* **No depende del tamaño de la ventana de la aplicación**
* Preserva las **características nativas de sondeo del ratón**
* Minimiza el buffering intermedio y la traducción
* Ofrece la **latencia más baja** entre todos los modos de ratón

Como resultado, el modo Relative Mouse HID proporciona un comportamiento **más cercano a una conexión USB directa del ratón**, especialmente a velocidades en baudios más altas.

#### Rendimiento del modo Relative Mouse HID

| Tipo de ratón | Baud rate | Frecuencia host (Hz) | Frecuencia objetivo (Hz) | Notas                                                         |
| ------------- | --------- | -------------------- | ------------------------ | ------------------------------------------------------------- |
| Bluetooth     | 9600      | ~100                 | ~90                      | Cerca del límite serial; aceptable para uso básico            |
| Con cable     | 9600      | ~250                 | ~180                     | Banda serial parcialmente saturada                            |
| Gaming        | 9600      | >1000                | ~90                      | El alto sondeo excede el ancho de banda disponible            |
| Bluetooth     | 115200    | ~160                 | ~155                     | Casi mapeo 1:1 host–objetivo                                  |
| Con cable     | 115200    | ~250                 | ~150                     | Estable y reactivo                                            |
| Gaming        | 115200    | >1000                | ~500                     | Mejor rendimiento general; limitado por el rendimiento serial |

**Puntos clave (modo Relative HID):**

* Proporciona la **latencia más baja** entre todos los modos de ratón
* A **9600 baudios**, los ratones de alto sondeo siguen estando limitados por el ancho de banda
* A **115200 baudios**, los ratones gaming alcanzan **cientos de eventos por segundo en el sistema objetivo**
* **Muy recomendado para gaming y movimientos rápidos de cámara**

---

### D. Ratón directo en Windows (referencia)

| Tipo de ratón   | Frecuencia objetivo (Hz) |
| --------------- | ------------------------ |
| Ratón Bluetooth | 80–85                    |
| Ratón con cable | 120–125                  |
| Ratón gaming    | >1000                    |

Esta referencia muestra que **Mini-KVM (115200 baudios, modo Relative HID)** puede acercarse al rendimiento nativo de un ratón con cable, aunque no puede eliminar completamente la sobrecarga inherente del KVM y del transporte serial.

---

## 4. Configuración recomendada para gaming

### ✅ Recomendado

* **Modo de ratón:** Relative Mouse HID
* **Baud rate:** 115200
* **Tipo de ratón:** Con cable o ratón gaming
* **Tasa de sondeo:** ≤1000 Hz recomendada

### ❌ Evitar

* Modo de ratón absoluto para gaming
* 9600 baudios con ratones de alto sondeo
* Tasas de sondeo excesivamente altas sin suficiente ancho de banda serial

---

## 5. Expectativas importantes

Openterface Mini-KVM está diseñado principalmente para:

✔ Interacción con BIOS / UEFI
✔ Configuración y depuración del sistema
✔ Acceso y gestión remota

Aunque **es posible jugar**, Mini-KVM **no sustituye a un ratón gaming USB directo**, especialmente en títulos altamente competitivos o sensibles a la latencia.

---

## 6. Resumen final

* **Jugar con Openterface Mini-KVM es posible** cuando se configura correctamente

* La capacidad de respuesta en juegos está dominada por el **modo del ratón, la tasa de sondeo y el baud rate**, no por el rendimiento de la CPU del host

* El **modo de ratón absoluto** prioriza la precisión posicional y no es adecuado para gaming

* **9600 baudios** crea un límite rígido de ancho de banda para la entrada

* **El modo Relative Mouse HID a 115200 baudios** ofrece el mejor equilibrio entre:

  * Frecuencia de entrada
  * Latencia
  * Estabilidad

* Aunque Mini-KVM no puede igualar completamente una conexión USB nativa, puede ofrecer una **experiencia jugable y con buena respuesta** para gaming casual y algunos escenarios competitivos

---

### Veredicto general

✅ **Técnicamente sólido**
✅ **Posicionamiento claro para gamers**
✅ **Honesto sobre las limitaciones**