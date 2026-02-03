---
title: "Guía de conmutación de tarjeta MicroSD"
description: "Aprende a utilizar el sistema de conmutación MicroSD dual hardware-software en el Openterface KVM-Go. Comprende los cuatro estados operativos, los indicadores LED, las directrices de seguridad y las capacidades de transferencia de archivos."
keywords: "conmutación MicroSD, conmutador KVM, conmutador hardware, conmutador software, control tarjeta MicroSD, KVM over USB, transferencia de archivos, gestión dispositivos USB, periféricos ordenador, gestión energía MicroSD, indicadores LED"
---

# **Guía de conmutación de tarjeta MicroSD** | Openterface KVM-Go

El **Openterface KVM-Go** incluye una única ranura para tarjeta MicroSD que puede compartirse entre el ordenador anfitrión y el dispositivo objetivo, pero nunca ambos al mismo tiempo.

Este diseño te permite cambiar rápidamente entre dispositivos para **transferencia de archivos**, sin quitar físicamente la tarjeta, haciendo que tu flujo de trabajo sea más rápido y eficiente. También puede servir simplemente como tu **lector de tarjetas MicroSD normal**.

## **Instalar la tarjeta MicroSD**

![kvm-go-install-sd](https://assets.openterface.com/images/kvm-go/install-sd.webp){:style="max-height:260px;width:auto"}

!!! note "Instalación correcta de la tarjeta MicroSD"
    Inserta firmemente la tarjeta MicroSD hasta que sientas un **clic**, indicando que está asentada de forma segura y bloqueada en su lugar.

## **Métodos de control**

KVM-Go proporciona dos formas de conmutar la tarjeta MicroSD entre anfitrión y objetivo:

- **Botón hardware** — Un botón físico en el dispositivo para control manual.  
- **Conmutador software** — Un botón de alternancia dentro de la aplicación anfitrión para conmutación instantánea.


## **Botón de conmutación e indicadores LED** 

![kvm-go-led-indicator](https://assets.openterface.com/images/kvm-go/led-indicator.webp){:style="max-height:260px;width:auto"}

Los **indicadores LED de doble color** muestran el estado actual de conexión MicroSD *(Nota: En desarrollo / Sujeto a cambios)*:

- **🔵 LED azul encendido** — La tarjeta MicroSD está montada en el **dispositivo objetivo**  
- **🟢 LED verde encendido** — La tarjeta MicroSD está montada en el **ordenador anfitrión**  
- **LED apagado** — No hay tarjeta MicroSD insertada o dispositivo apagado  
- **LED parpadeando** — Transferencia de datos en curso (actividad de lectura/escritura)

!!! note "Función de montaje automático (Experimental)"
    Por defecto, la tarjeta MicroSD se monta en el **anfitrión** cuando el dispositivo se enciende por primera vez.  
    Una próxima función experimental permitirá el **montaje automático** en el lado (anfitrión u objetivo) que se conecte primero, haciendo la experiencia aún más fluida.

---

## Relacionado

- [microSD EXPRESS en KVM-GO: prueba de compatibilidad y velocidades de transferencia reales](updates/20260203-kvm-go-microsd-express.es.md) — Prueba de compatibilidad con tarjeta SanDisk microSD EXPRESS y velocidades de transferencia reales

