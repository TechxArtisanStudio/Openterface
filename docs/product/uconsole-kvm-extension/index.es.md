# Extensión KVM de Openterface para uConsole

![KVM Extension Connected to Target Device 2](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-2.webp){:style="height:300px"}

## Resumen

Transforma tu uConsole en una **consola KVM (Teclado, Video, Ratón) portátil** con esta placa de extensión plug-and-play.

La **Extensión KVM de Openterface** reemplaza el módem 4G/LTE original en la ranura de expansión de tu uConsole y proporciona **entrada HDMI directa y control USB HID**, permitiéndote gestionar dispositivos headless sobre la marcha—sin necesidad de monitores externos, teclados o configuración de red.

![KVM Extension Board Front Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:300px"}
![KVM Extension Board Backm Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:300px"}


## Características

- **Factor de Forma Perfecto**  
    Coincide con el tamaño de 37×77 mm del módulo 4G/LTE para una integración de hardware perfecta.

- **HDMI Directo + USB HID**  
    Permite control responsivo de dispositivos conectados usando la entrada y pantalla integradas del uConsole.

- **Baja Latencia**  
    Adecuado para resolución de problemas a nivel BIOS e interacción en tiempo real.

- **Verdaderamente Portátil**  
    Convierte el uConsole en una herramienta móvil para desarrolladores, ingenieros y técnicos.

- **Amigable con Código Abierto**  
    Construido sobre la plataforma [Openterface KVM](https://github.com/techxArtisanStudio/openterface_qt). Contribuciones de la comunidad bienvenidas.


## Casos de Uso

- **Administración de Sistemas**  
    Accede y resuelve problemas de servidores o dispositivos embebidos sin un interruptor KVM voluminoso.

- **Desarrollo de Hardware**  
    Prueba y depura Raspberry Pi, SBCs o microcontroladores directamente.

- **Despliegue en Campo**  
    Realiza mantenimiento o configuración en centros de datos o ubicaciones remotas.


## Instalación de Hardware

Sigue estos pasos de instalación de hardware para reemplazar el módulo 4G/LTE en tu uConsole con la placa de Extensión KVM de Openterface y asegurar un ajuste seguro.

### Lo que Necesitarás

- Tu placa de extensión KVM de Openterface
- La junta proporcionada (espaciador de plástico) 
- Un destornillador hexagonal (para los tornillos de montaje de la placa)
- Precauciones ESD (pulsera o superficie conectada a tierra) — recomendado

### Instalando la Placa de Extensión

1. Apagar y Desconectar

    Apaga el uConsole y desconecta toda la alimentación y cables.

2. Remover el Módulo Existente

    Usa un destornillador hexagonal para remover los dos tornillos que sostienen el módulo 4G/LTE o la placa de extensión existente.

    Levanta cuidadosamente la placa hacia arriba para evitar doblar los contactores de resorte.

3. Instalar la Placa de Extensión KVM

    - La placa de Extensión KVM de Openterface tiene 1.0 mm de grosor (más delgada que el 4G/LTE original de 1.2 mm). Por esto, recomendamos colocar la junta proporcionada en los postes de tornillo (entre el PCB y los separadores de montaje) para que la junta se asiente bajo los postes de tornillo antes de colocar la placa. Esto compensa el PCB más delgado y ayuda a asegurar la presión adecuada del contactor de resorte.
    - Si prefieres verificar primero, coloca la placa sin la junta y verifica contacto uniforme del resorte; si el contacto es desigual o la placa se asienta sueltamente, añade la junta y recoloca la placa.

<div style="display:flex;gap:1rem;align-items:flex-start;flex-wrap:wrap">
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-gasket-1.webp" alt="Installing KVM Extension gasket" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp" alt="Installing KVM Extension into uConsole" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
</div>

4. Reinsertar Tornillos

    Reinserta los dos tornillos y aprieta con el destornillador hexagonal. Ajustado es suficiente — no aprietes demasiado.

5. Verificar Ajuste

    La placa debe asentarse plana sin movimiento notable. Verifica que los contactores de resorte estén haciendo contacto uniforme a través de las almohadillas.

6. Probar el Hardware

    Reconecta la alimentación, arranca el sistema y prueba dispositivos HDMI, audio y USB HID para confirmar operación adecuada.

## Guía de Configuración de Software

Para usar la Extensión KVM, instala la **App Openterface** en tu uConsole.

Opción 1 - Usar la versión Flatpak de Openterface
- 📖 Sigue nuestra [Guía de Instalación Flatpak](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) para pasos de configuración detallados.

![KVM Extension Connected to Target Device](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1c.webp){:style="height:300px"}

Opción 2 - Instalar versión comunitaria de Rex

Si quieres la compilación comunitaria mantenida por Rex, añade su repositorio e instala el paquete con los comandos de abajo.

1. Añadir la clave GPG del repositorio y el repositorio

```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. Actualizar e instalar

```bash
sudo apt update
sudo apt install openterfaceqt
```

Notas: estos comandos requieren sudo. El repositorio apunta a paquetes arm64 Bookworm; verifica compatibilidad con tu dispositivo antes de instalar.

## Estado de Pre-Lanzamiento

- 📦 Primer lote actualmente en preparación  
- ⏳ Envío estimado comienza en **principios de agosto 2024**  
- 🛒 Cantidad limitada – [Pre-ordena ahora](https://shop.techxartisan.com/products/openterface-kvm-ext-for-uconsole) para reservar tu unidad

> **Aviso de Pre-Orden**  
> Este artículo está actualmente en pre-orden con un tiempo de entrega estimado de **aproximadamente 2 meses**.  
> Si necesitas otros artículos más pronto, por favor haz una **orden separada**. Las órdenes combinadas se enviarán cuando este producto esté listo.

## Comunidad y Soporte

- 🗨️ Únete a la discusión: [Servidor Discord](https://discord.gg/ruAD9kcYbq)  
- 📧 Soporte por email: [info@openterface.com](mailto:info@openterface.com)


## Preguntas Frecuentes

**P: ¿Cómo funciona la Placa de Extensión KVM?**  
Captura la salida HDMI de un dispositivo objetivo y la muestra en el uConsole. Al mismo tiempo, el teclado y trackball del uConsole se usan para controlar el dispositivo objetivo vía emulación USB HID.

**P: ¿Puedo usar esto con el módulo 4G/LTE instalado?**  
No. Esta placa ocupa la misma ranura de expansión. Necesitarás elegir entre conectividad celular o funcionalidad KVM.

**P: ¿El software es de código abierto?**  
¡Sí! Nuestras Apps **Openterface Connect** son completamente de código abierto y están disponibles en nuestro [repositorio GitHub](https://github.com/TechxArtisanStudio/Openterface_QT).
