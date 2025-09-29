---
title: "Puerto USB Conmutable"
description: "Aprende sobre el sistema dual de conmutación USB hardware-software en Openterface Mini-KVM. Comprende los cuatro estados operativos, las pautas de seguridad y las futuras capacidades de acceso remoto."
keywords: "conmutación USB, conmutador KVM, conmutador hardware, conmutador software, control de puerto USB, KVM over USB, KVM over IP, acceso remoto, gestión de dispositivos USB, periféricos de ordenador, gestión de alimentación USB"
---

# **Guía de Conmutación del Puerto USB** | Openterface Mini-KVM

El dispositivo mini-KVM tiene un único puerto USB-A 2.0 que puede **conectarse tanto** al anfitrión como al ordenador objetivo, pero **nunca a ambos a la vez**.

El control proviene de dos conmutadores:

- **Conmutador Hardware**: Un interruptor físico de dos posiciones en el dispositivo ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t.svg#only-light){:style="max-height:20px"} ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t_1.svg#only-dark){:style="max-height:20px"} (hacia adentro = anfitrión, hacia afuera = objetivo).
- **Conmutador Software**: Un botón de conmutación en la aplicación anfitrión que redirige instantáneamente el puerto USB al anfitrión o al objetivo.

## Estados Operativos

La conexión del puerto USB-A depende de las posiciones tanto del **Conmutador Hardware** como del **Conmutador Software**. La siguiente tabla resume los cuatro estados posibles:

| **Estado** | **Conmutador Hardware** | **Conmutador Software** | **Puerto Conectado A** | **Estado de Sincronización** |
| ---------- | ----------------------- | ----------------------- | ---------------------- | ---------------------------- |
| 1          | Host                    | Host                    | Host                   | Synced                       |
| 2          | Target                  | Target                  | Target                 | Synced                       |
| 3          | Target                  | Host                    | Host                   | Out of Sync (→ Host)         |
| 4          | Host                    | Target                  | Target                 | Out of Sync (→ Target)       |

- **Synced** significa que la configuración hardware y software coincide.
- **Out of Sync** significa que el software anula temporalmente el conmutador hardware hasta que el conmutador hardware se mueva de nuevo.

Cualquier movimiento manual del conmutador hardware actualizará la pantalla del software y volverá a un estado sincronizado.

Al iniciar, el dispositivo se conecta por defecto al anfitrión. El software detecta la posición del conmutador hardware y se sincroniza en consecuencia.

!!! warning "Recuerda expulsar la memoria USB antes de cambiar el conmutador"
Si el puerto USB está siendo utilizado por una memoria USB, asegúrate de expulsar la memoria USB antes de cambiar el conmutador para transferir el uso del puerto a otro ordenador.

??? note "¿Cómo compartir una memoria/disco USB entre los dispositivos Anfitrión y Objetivo?"
Los archivos se pueden transferir entre el anfitrión y el objetivo siguiendo estos pasos:

    1. Monta una memoria USB en el anfitrión cuando el pequeño conmutador negro está configurado al lado del puerto Type-C del anfitrión.
    2. Copia los archivos en esta unidad montada.
    3. Después de copiar, desmonta la unidad sin desconectarla físicamente.
    4. Voltea el pequeño conmutador negro al otro lado. Esta acción cambia la conexión del puerto USB-A al objetivo.
    5. Monta la memoria USB en el dispositivo objetivo y copia/mueve los archivos de la unidad, completando el proceso de transferencia de archivos del anfitrión al objetivo.

    Este método también se puede usar en la dirección opuesta.

!!! Note "Guía del Usuario" - **Prioridad del Conmutador Software**: Independientemente de la posición del conmutador hardware, hacer clic en el conmutador software cambiará inmediatamente la dirección del circuito.

    - **Sincronización del Conmutador Hardware**: Cualquier cambio manual del Conmutador Hardware alineará su estado con el Conmutador Software, pasando del Estado 3 o 4 no sincronizado al Estado 1 o 2. Sin embargo, esta sincronización no necesariamente altera la conexión del circuito real.

    - **Monitoreo del Conmutador Hardware**: El Conmutador Hardware, a pesar de ser físico, es monitoreado por el software y no controla directamente la dirección del circuito. En su lugar, el software interpreta la posición del conmutador y gestiona la conmutación del circuito real.
