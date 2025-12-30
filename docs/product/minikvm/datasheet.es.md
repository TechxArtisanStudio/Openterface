---
title: "Ficha técnica del Mini-KVM de Openterface | Especificaciones técnicas y detalles del producto"
description: "Ficha técnica completa del Mini-KVM de Openterface. Consulte las especificaciones, dimensiones, capacidades de video/audio, requisitos de energía, accesorios y opciones de conectividad para esta solución KVM-over-USB."
keywords: "Ficha técnica Mini-KVM, especificaciones Mini-KVM, especificaciones técnicas KVM sobre USB, dimensiones Mini-KVM, accesorios Mini-KVM, especificaciones HDMI KVM, detalles técnicos USB KVM, especificaciones de control de ordenadores sin cabeza, especificaciones del conmutador KVM, herramientas de gestión de servidores"
---

# Ficha técnica del Mini-KVM de Openterface

## Visión general

El Mini-KVM de Openterface™ es un dispositivo rique en características, de producción, de código abierto y impulsado por la comunidad. Ofrece una solución KVM-over-USB ligera y rápida, lo que le permite controlar directamente un ordenador sin cabeza (denominado como el computador objetivo) desde su propio portátil o ordenador de escritorio (denominado como el computador anfitrión), mediante una conexión simple USB y HDMI. Este enfoque compacto elimina la necesidad de teclados adicionales, ratones, monitores o cualquier configuración de red, simplificando su instalación y mejorando la eficiencia.

## Especificaciones

### General

| Parámetro | Características |
|-----------|----------------|
| Nombre del producto | Openterface Mini-KVM |
| Fabricante | TechxArtisan Limited |

### Variantes del producto

#### Mini-KVM Básico (392-OP-MINIKVM-BASIC)

**Contenido:**

- Openterface Mini-KVM
- Guía de inicio rápido

#### Mini-KVM Toolkit (392-OPMINIKVMTOOLKIT)

**Contenido:**

- Openterface Mini-KVM
- Guía de inicio rápido
- Bolsa de herramientas (165 x 110 x 50mm)
- Tapa de pin de extensión
- Cable HDMI macho a macho (0,3m)
- Cable Type-C macho a USB-A macho (0,3m) con adaptador USB-A hembra a Type-C macho
- Cable Type-C macho a macho (1,5m) con adaptador USB-C hembra a USB-A macho

### Energía

| Parámetro | Características |
|-----------|----------------|
| Tipo de conexión | Alimentado por USB-C. No se requiere fuente de alimentación externa. |

### Video

| Parámetro | Características |
|-----------|----------------|
| Entrada de video máxima | Hasta 3840x2160@30Hz, mediante HDMI<br>(Nota: Con el uso de un adaptador, también puede admitir VGA, Micro HDMI, DVI y otras fuentes de entrada de video) |
| Resoluciones de video admitidas | Hasta 1920x1080@30Hz |
| Métodos de compresión de video | YUV, MJPEG |
| Latencia | Menos de 140 milisegundos |

### Audio

| Parámetro | Características |
|-----------|----------------|
| Modo de captura de audio | Audio incrustado en HDMI |

### Ambiental

| Parámetro | Características |
|-----------|----------------|
| Temperatura de operación | 0°C a 40°C |
| Temperatura de almacenamiento | -10°C a 50°C |
| Humedad | 80% RH |

### Tamaño y peso

| Parámetro | Características |
|-----------|----------------|
| Longitud x Anchura x Altura | 61 x 13,5 x 53 mm |
| Peso | 48 g |

## Accesorios para el Toolkit

| Artículo | Número de modelo | Descripción |
|--------|------------------|-------------|
| Cable HDMI macho a macho | OP-03-CABLE30-HDMI | Longitud: 0,3 m / ~12"<br>Color: Negro<br>Uso: Transmisión de video HDMI en alta definición |
| Cable Type-C a USB-A con adaptador | OP-04-CABLE30-C2A | Longitud: 0,3 m / ~12"<br>Color: Negro<br>Adaptador: USB-A hembra a Type-C macho<br>Uso: Transferencia de datos / control KVM |
| Cable Type-C de nailon con adaptador | OP-05-CABLE150-C2C | Longitud: 1,5 m / 4' 11"<br>Color: Naranja<br>Adaptador: USB-C a USB-A<br>Transferencia de datos: Hasta 10 Gbps<br>Potencia de carga: 240 W |

## Conexiones

### Conectividad / Interfaces

1. **Puerto USB-C (hembra)** ⓵  
   Como puerto de dispositivo USB, conectarse al computador anfitrión para la transferencia de datos mediante el hub USB integrado

2. **Puerto USB-C (hembra)** ②  
   Como puerto de dispositivo USB, conectarse al computador anfitrión para emular la salida HID de teclado y ratón mediante el hub USB integrado

3. **Puerto de entrada HDMI (hembra)** ③  
   Entrada de video HDMI desde el computador objetivo

4. **Puerto USB-A 2.0 (hembra) intercambiable** ④  
   Como puerto USB host, utilizado por el computador anfitrión o el computador objetivo en cualquier momento dado, pero no simultáneamente

5. **Interruptor de conmutación** ⑤  
   Para alternar la conexión del puerto USB-A 2.0 entre el anfitrión y el objetivo

6. **Pines de extensión** ⑥  
   Para más información, consulte los pines de extensión para uso por desarrolladores.

## Aplicaciones

El Mini-KVM de Openterface es el compañero perfecto para una amplia gama de usuarios y escenarios:

- Profesionales de IT que solucionan problemas en servidores
- Técnicos que atienden cajeros automáticos, máquinas de venta y kioscos
- Desarrolladores que gestionan dispositivos de computación en la nube
- Entusiastas tecnológicos que experimentan con computadoras de un solo chip
- Profesionales que requieren operaciones locales seguras en redes aisladas, como los que gestionan activos de criptomonedas
- Cualquier persona que necesite flujos de trabajo integrados con frecuencia entre computadoras personales y laborales.

## Software para el computador anfitrión

Para poner este dispositivo en funcionamiento en macOS, Windows, Linux o Android, instale una de nuestras aplicaciones disponibles desde las plataformas de aplicación correspondientes o compílelo desde la fuente utilizando nuestros repositorios de GitHub.

## Código abierto y cumplimiento

Las aplicaciones de Openterface están licenciadas bajo AGPL-3.0, con desarrollo activo por parte de TechxArtisan. El dispositivo está certificado como OSHWA (UID CN000015), lo que garantiza el acceso abierto a todos los esquemas y código fuente en GitHub: [Openterface_Mini-KVM_Hardware](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware).

## Manténgase actualizado

Visite [openterface.com](https://openterface.com) y únase a nuestra comunidad de Discord para mantenerse informado, obtener soporte y colaborar con otros usuarios.