---
title: "Configuración de software"
description: "Guía completa de configuración de software para Openterface KVM Extension for uConsole. Aprende cómo instalar y configurar la App Openterface en tu uConsole para funcionalidad KVM sin problemas."
keywords: "instalación app Openterface, configuración software uConsole, configuración app KVM, configuración app uConsole, guía instalación software"
---

# **Configuración de software** | Openterface KVM Extension for uConsole

## Resumen de instalación

La App Openterface permite que tu uConsole funcione como una interfaz KVM, permitiéndote controlar dispositivos objetivo a través de la pantalla integrada, teclado y trackball.

!!! note "Requisitos"
    - **uConsole**: Requiere instalación de la App Openterface
    - **Objetivo**: No se necesita app - soporta Windows, macOS, Linux, Android, iOS
    - **Video**: Usa un cable HDMI estándar. Usa un cable HDMI estándar. Con un convertidor HDMI alimentado, también soporta otros formatos como **VGA**, **DP** y más. *Consejo: Asegúrate de que el convertidor esté correctamente alimentado; de lo contrario, puedes experimentar una pantalla negra.*

## Métodos de instalación

### **Opción 1: Instalación Flatpak**

Sigue nuestra [Guía de instalación Flatpak](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) para pasos de configuración detallados.

### **Opción 2: Repositorio de la comunidad (Recomendado)**

Si prefieres la build de la comunidad mantenida por Rex:

1. **Añadir repositorio**:
```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. **Instalar paquete**:
```bash
sudo apt update
sudo apt install openterfaceqt
```

!!! warning "Notas del repositorio"
    Estos comandos requieren sudo. El repositorio está dirigido a paquetes arm64 Bookworm; verifica la compatibilidad con tu dispositivo antes de instalar.

## Instrucciones de uso

### **Iniciar sesión KVM**
1. Lanza la App Openterface en tu uConsole
2. La app detectará automáticamente la placa Extension KVM
3. Conecta tu dispositivo objetivo vía HDMI
4. Usa el teclado y trackball integrados del uConsole para controlar el dispositivo objetivo

### **Características de control**
- **Teclado**: Emulación completa del teclado incluyendo teclas multimedia
- **Ratón**: Posicionamiento absoluto y relativo del ratón
- **Audio**: Passthrough de audio HDMI a los altavoces del uConsole

### **Características avanzadas**
- **Transferencia de texto**: Transfiere rápidamente texto simulando pulsaciones de teclas—ideal para nombres de usuario, contraseñas y fragmentos de código
- **USB conmutable**: Cambia fácilmente el acceso USB entre el uConsole y el dispositivo objetivo usando la app anfitrión
