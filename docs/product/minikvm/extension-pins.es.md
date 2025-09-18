---
title: "Pines de extensión"
description: "Explora el potencial de los pines de extensión del Openterface Mini-KVM para el desarrollo de hardware a medida y proyectos de código abierto."
keywords: "Mini-KVM pines de extensión, desarrollo a medida, modificación de hardware, KVM de código abierto"
---

# **Pines de extensión** | Modo desarrollador | Openterface Mini-KVM

![mini-kvm-pins-port](https://assets.openterface.com/images/product/mini-kvm-pins-port.webp){:style="height:360px"}
![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="height:300px"}

Openterface Mini-KVM incorpora pines de extensión para desarrollo avanzado y experimentación con [Open Software](/app). Estos pines no están expuestos en la configuración estándar de la carcasa.

## Cómo acceder a los pines

1. Desmonta el dispositivo.
2. Sustituye la tapa original de la carcasa por una «Extension Pin Cap» especializada.
3. Descarga el [modelo 3D](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models) de la Extension Pin Cap.
4. Consulta nuestro [repositorio de hardware en GitHub](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware).

![change-cap](https://assets.openterface.com/images/product/change-cap.svg#only-light){:style="height:300px"}
![change-cap](https://assets.openterface.com/images/product/change-cap_1.svg#only-dark){:style="height:300px"}

!!! warning "Garantía anulada"
    Retirar la carcasa original puede anular la garantía del producto. Cualquier modificación o desmontaje se realiza bajo la responsabilidad del usuario.

!!! note "Funciones experimentales"
    Las funciones desarrolladas usando estos pines son experimentales y no han sido completamente probadas. Openterface no se hace responsable de ningún daño, lesión o mal funcionamiento resultante de modificaciones, exposición de los pines de extensión u otras alteraciones del dispositivo.

## Configuración de pines

![target-side](https://assets.openterface.com/images/product/extension-pins-1.svg#only-light){:style="height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2.svg#only-light){:style="height:200px"}
![target-side](https://assets.openterface.com/images/product/extension-pins-1_1.svg#only-dark){:style="height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2_1.svg#only-dark){:style="height:200px"}

Los pines de extensión proporcionan las siguientes conexiones:

1. Alimentación USB de 5 V para componentes externos
2. Datos positivos al hub USB del anfitrión
3. Datos negativos al hub USB del anfitrión
4. Datos positivos al hub USB del objetivo
5. Datos negativos al hub USB del objetivo
6. Tierra (GND)

!!! danger "Conexiones incorrectas causan daños"
    Confundir VCC y GND puede causar daños graves al dispositivo y a los componentes conectados. Verifica siempre las conexiones de los pines antes de encender el dispositivo.

## Tapa de pines de extensión

![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="height:360px"}

Esta tapa de pines de extensión impresa en 3D sustituye la tapa original del Openterface Mini-KVM y permite a los usuarios avanzados exponer y acceder a los pines de extensión para desarrollo personalizado. Puedes descargar los archivos del modelo 3D desde nuestro repositorio de GitHub e imprimir la tapa por tu cuenta.

- **Uso**: proporciona acceso a los pines de extensión para desarrollo de hardware avanzado.
- **Descarga**: [Archivos del modelo 3D](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models)

## Participa en el desarrollo

A medida que seguimos desarrollando y experimentando, iremos actualizando esta sección con más información sobre lo que pueden hacer estos pines y cómo pueden utilizarse de forma creativa. Tu creatividad y experiencia pueden ayudar a ampliar los límites de lo posible con el Openterface Mini-KVM. Participa:

1. **Comparte tus ideas**: ¿tienes un concepto interesante para usar estos pines? ¡Queremos escucharlo!
2. **Contribuye con proyectos DIY**: si has creado algo interesante, plantéate compartirlo en nuestra comunidad [Discord Openterface](/discord).
3. **Únete a la discusión**: conéctate con otros desarrolladores y entusiastas para intercambiar ideas y colaborar.

¡Construyamos e innovemos juntos!
