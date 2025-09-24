---
title: "Instalación de hardware"
description: "Guía paso a paso de instalación de hardware para Openterface KVM Extension for uConsole. Aprende cómo instalar correctamente la placa de extensión en la ranura de expansión de tu uConsole con directrices de seguridad detalladas."
keywords: "instalación extensión KVM, configuración hardware uConsole, instalación placa expansión, ranura expansión uConsole, guía hardware KVM, instalación física"
---

# **Instalación de hardware** | Openterface KVM Extension for uConsole

## Resumen
La Extensión KVM reemplaza el módulo 4G/LTE en la ranura de expansión del uConsole, añadiendo entrada HDMI directa y control USB HID.

## Lo que necesitas
- Revisa tu [Contenido del paquete](whats-in-the-box.md) antes de la instalación  
- Placa Openterface KVM Extension  
- **Arandelas** proporcionadas (para asegurar montaje estable y presión uniforme)  
- Destornillador hexagonal (para tornillos de montaje)  
- Protección ESD (pulsera o superficie conectada a tierra) — recomendado  

## Pasos de instalación

### **1. Apagar**
Apaga el uConsole y desconecta toda la alimentación y cables.

### **2. Retirar módulo existente**
Usa un destornillador hexagonal para retirar los dos tornillos.  
Levanta la placa **directamente hacia arriba** para evitar doblar los contactos de resorte.

### **3. Instalar la Extensión KVM**
- Coloca la **arandela** en el poste del tornillo.  
- Asienta firmemente la Extensión KVM en la ranura de expansión.  
- La arandela compensa el PCB ligeramente más delgado (1,0 mm vs 1,2 mm), manteniendo la presión de contacto de resorte apropiada.

??? note "Verificar ajuste antes de la instalación final"
    Puedes primero asentar la placa **sin la arandela** para probar el ajuste. Si la placa se siente suelta o los contactos son desiguales, añade la arandela y vuelve a asentar la placa. La Openterface KVM Extension tiene 1,0 mm de grosor, ligeramente más delgada que el módulo LTE original (1,2 mm). Usar la arandela proporcionada asegura un montaje estable y contacto de resorte confiable.  
    ![extension-slot-loose](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-slot-loose.webp){:style="height:220px"}

### **4. Asegurar la placa**
Vuelve a insertar los tornillos y aprieta **suavemente** — **no aprietes demasiado**, ya que esto puede dañar la placa o desgastar las roscas.

![extension-screw-washer-installed](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installed.jpg){:style="height:220px"}
![extension-screw-washer-installing](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installing.jpg){:style="height:220px"}
![extension-install-1](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp){:style="height:220px"}

### **5. Verificar instalación**
La placa debe estar **plana y estable**, con contacto de resorte uniforme en todas las almohadillas. No debe haber movimiento o balanceo notable.

### **6. Instalar tapa de ranura de expansión**
Reinstala la tapa de la ranura de expansión para proteger la placa Extensión KVM y mantener la apariencia original del uConsole.

??? note "Orientación del texto en la tapa de ranura de expansión"
    El texto en la tapa de la ranura de expansión puede aparecer "al revés" cuando se ve desde ciertos ángulos. Este es un diseño intencional - el texto está orientado para ser legible cuando sostienes el uConsole y miras los puertos de arriba hacia abajo, que es la posición de visualización natural cuando usas el dispositivo.
    ![expansion-slot-text-orientation](https://assets.openterface.com/images/product/openterface-kvm-uconsole-expansion-slot-text-orientation.webp){:style="height:220px"}

---

**Próximos pasos**

1. Ve a [Configuración de software](/product/uconsole-kvm-extension/software-setup/) para instalar la App Openterface.  
2. Ve a [Conectar al dispositivo objetivo](/product/uconsole-kvm-extension/connect-to-target/) para conectar tu dispositivo objetivo.  
3. Revisa [Características y especificaciones](/product/uconsole-kvm-extension/features/) para especificaciones técnicas detalladas.
