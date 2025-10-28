---
title: "Cómo conectar"
description: "Guía paso a paso para configurar el Openterface KVM-Go. Aprende a conectar tu ordenador anfitrión y dispositivo objetivo usando conectores de vídeo integrados para una experiencia de conexión directa ultra-simple."
keywords: "configuración KVM-Go, configuración KVM ultracompacto, conexión HDMI integrada, guía instalación KVM, configuración KVM llavero, conexión USB KVM, configuración ordenador headless, configuración KVM portátil"
---

# **Cómo conectar** | Guía de configuración | Openterface KVM-Go

## **Descripción general de las conexiones**

![Descripción general de conexiones KVM-Go](https://assets.openterface.com/images/kvm-go/step-0-overview.webp){:style="max-height:360px"}

Las imágenes anteriores muestran todas las conexiones entre el [**KVM-Go**](/product/kvm-go), el ordenador anfitrión y el dispositivo objetivo.

- **Ordenador anfitrión**: Requiere la instalación de la [aplicación Openterface](/app).  
- **Dispositivo objetivo**: No se necesita software ni preconfiguración.
- **Vídeo**: El conector integrado se conecta directamente al dispositivo objetivo, por lo que no necesitas llevar ni gestionar cables de vídeo adicionales.

## **Lo que necesitas para las conexiones**

![KVM-Go todas las piezas](https://assets.openterface.com/images/kvm-go/step-0-all-parts.webp){:style="max-height:360px"}

Para configurar tu **KVM-Go**, necesitarás los siguientes componentes:

- **KVM-Go (HDMI / DP / VGA)** — se conecta al **dispositivo objetivo** (para captura de vídeo)  
- **Cable USB-C corto negro** — se conecta al **dispositivo objetivo** (para emulación de teclado y ratón)
- **Cable USB-C largo naranja** — se conecta al **ordenador anfitrión** (ejecutando la [aplicación Openterface](/app))

!!! note "Aviso sobre la longitud de los cables"
    Las longitudes exactas de los cables incluidos en el **paquete oficial KVM-Go** **aún no están finalizadas** y pueden diferir ligeramente de las mostradas aquí.  
    Los cables demostrados en esta guía son del *kit clásico Mini-KVM* y son solo para fines ilustrativos.

!!! warning "Uso de tus propios cables"
    Si eliges usar tus propios cables, asegúrate de que sean **cables USB de alta calidad capaces de transferir datos**. Los cables de mala calidad o solo de carga pueden resultar en:
    
    - Problemas de pantalla negra
    - Entradas de teclado o ratón sin respuesta
    - Caídas de conexión intermitentes
    - Salida de pantalla parpadeante o inestable

## **Configuración paso a paso**

### **Paso 1 — Conectar los cables USB al KVM-Go**
![Conectando cables USB](https://assets.openterface.com/images/kvm-go/step-1-plugged.webp){:style="max-height:360px"}

- **Cable USB-C negro** → Conectar al puerto etiquetado ![Icono objetivo](https://assets.openterface.com/images/shell-icons/target-computer.svg#only-light){:style="max-height:20px"} ![Icono objetivo](https://assets.openterface.com/images/shell-icons/target-computer_1.svg#only-dark){:style="max-height:20px"} **Target** en la carcasa del KVM-Go.  
- **Cable USB-C naranja** → Conectar al puerto etiquetado ![Icono anfitrión](https://assets.openterface.com/images/shell-icons/host-computer.svg#only-light){:style="max-height:20px"} ![Icono anfitrión](https://assets.openterface.com/images/shell-icons/host-computer_1.svg#only-dark){:style="max-height:20px"} **Host**.

!!! warning
    Ambos puertos USB-C son físicamente idénticos.  
    Siempre **verifica las etiquetas** en la superficie de la carcasa para evitar confundirlos.

### **Paso 2 — Conectar vídeo al objetivo**
![Conectando conector HDMI](https://assets.openterface.com/images/kvm-go/step-3-hdmi-plugged.webp){:style="max-height:360px"}

Conecta el **conector de vídeo macho integrado** directamente al puerto de salida de vídeo del dispositivo objetivo.

### **Paso 3 — Conectar el puerto USB objetivo**
Conecta el **cable USB negro** al dispositivo objetivo para control HID.

- **Opción A:** Directamente a un puerto USB-A  
  ![Objetivo USB-A](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-b.webp){:style="max-height:360px"}

- **Opción B:** Usando un adaptador USB-C  
  ![Objetivo USB-C](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-a.webp){:style="max-height:360px"}

!!! note "Verificación de conexión USB-C"
    Algunos puertos USB-C pueden no proporcionar una conexión segura. Si experimentas problemas intermitentes de control de teclado/ratón, mueve suavemente la conexión del adaptador para asegurarte de que esté correctamente insertado y haciendo contacto.


### **Paso 4 — Conectar el puerto USB anfitrión**
Conecta el **cable USB naranja** al ordenador anfitrión.

- Directamente a un puerto USB-C **O** mediante un adaptador USB-C a USB-A.  
  ![Conectando USB anfitrión](https://assets.openterface.com/images/kvm-go/step-5-plug-in-host-computer-1.webp){:style="max-height:360px"}

