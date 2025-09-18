---
title: "Cómo conectarse"
description: "Guía paso a paso para configurar Openterface Mini-KVM. Aprende cómo conectar tu ordenador anfitrión y dispositivo objetivo con instrucciones detalladas para conexiones USB-C, HDMI y periféricos. Incluye descripciones de interfaz y consejos importantes de configuración."
keywords: "Configuración Mini-KVM, guía de conexión KVM, configuración KVM USB-C, conexión KVM HDMI, guía de instalación KVM, configuración de periféricos de ordenador, conexión de dispositivo USB, guía de interfaz KVM, configuración de ordenador headless, configuración KVM"
---

# **Cómo conectarse** | Guía de configuración | Openterface Mini-KVM

## Configuración rápida

![to-host](https://assets.openterface.com/images/product/to-host.svg#only-light){:style="height:200px"} ![to-host](https://assets.openterface.com/images/product/to-host_1.svg#only-dark){:style="height:200px"}
![to-target](https://assets.openterface.com/images/product/to-target.svg#only-light){:style="height:200px"} ![to-target](https://assets.openterface.com/images/product/to-target_1.svg#only-dark){:style="height:200px"}

**Configuración en 4 pasos simples:**

1. **Conexión anfitrión** (lado naranja): Conectar ordenador anfitrión usando cable Type-C de 1,5m
2. **Conexión objetivo** (lado negro): Conectar dispositivo objetivo usando cable Type-C de 0,3m
3. **Conexión de vídeo** (lado negro): Conectar salida de vídeo del objetivo al puerto HDMI
4. **Dispositivo USB** (opcional): Conectar al puerto USB-A después de completar los pasos 1-3

!!! note "Requisitos" - **Anfitrión**: Requiere [Openterface App](/app) instalada - **Objetivo**: No se necesita app - soporta Windows, macOS, Linux, Android, iOS - **Vídeo**: Usar cable HDMI proporcionado o convertidor VGA-to-HDMI

## Guía de puertos

![host-side](https://assets.openterface.com/images/product/host-htc.svg#only-light){:style="width:300px"} ![target-side](https://assets.openterface.com/images/product/target-htc.svg#only-light){:style="width:300px"}
![host-side](https://assets.openterface.com/images/product/host-htc_1.svg#only-dark){:style="width:300px"} ![target-side](https://assets.openterface.com/images/product/target-htc_1.svg#only-dark){:style="width:300px"}

- ① **USB-C anfitrión**: Transferencia de datos al ordenador anfitrión
- ② **USB-C objetivo**: Salida de control de teclado/ratón
- ③ **Entrada HDMI**: Entrada de vídeo desde dispositivo objetivo
- ④ **Puerto USB-A**: Conmutable entre anfitrión/objetivo

!!! warning "Notas importantes" - **Alimentación**: Los dispositivos USB no deben exceder 1,5W de consumo - **Bloqueo USB-A**: Requiere fuerza extra para insertar/retirar (evitar dispositivos pequeños) - **Hub USB**: Usar solo hubs alimentados externamente; evitar árboles USB profundos - **Conmutación**: Ver [Guía de conmutación de puerto USB](../usb-switch) para detalles

⑤ ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t.svg#only-light){:style="height:20px"} ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t_1.svg#only-dark){:style="height:20px"} **Interruptor de conmutación**: Conmutar puerto USB-A entre anfitrión/objetivo

⑥ ![Extension Pins](https://assets.openterface.com/images/shell-icons/pins.svg#only-light){:style="height:15px"} ![Extension Pins](https://assets.openterface.com/images/shell-icons/pins_1.svg#only-dark){:style="height:15px"} **Pines de extensión**: Acceso de desarrollador (ver [Pines de extensión](../extension-pins))
