# Software

Para poner en marcha tus gadgets Openterface™ KVM, necesitarás instalar una de las aplicaciones listadas abajo en tu ordenador anfitrión. Puedes obtener estas aplicaciones desde diferentes plataformas de aplicaciones o simplemente hacer clic en los enlaces proporcionados. ¡Si te sientes aventurero, también puedes construirlas desde el código fuente usando nuestros repositorios de GitHub!

![use-case-pc-angled-view](https://assets.openterface.com/images/product/use-case-pc-angled-view.webp){ width=600 }

## Descarga e Instalación

<div class="grid cards" markdown>

-   ### :fontawesome-brands-windows:{ .lg } **Windows**

    ***

    Descarga o construye desde el código fuente para **Openterface QT Win**:

    [:octicons-download-24: Descargar {{qt_version}} Instalador](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_windows_amd64_installer.exe) <br>
    [:octicons-download-24: Descargar {{qt_version}} EXE Portable](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_windows_amd64_portable.exe) <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) <br>
    [:octicons-play-24: Ver Demo](https://youtu.be/ERzpGtRvP2o?si=e9k402f0nxsD8o2j)

-   ### :fontawesome-brands-apple:{ .lg } **macOS**

    ***

    Descarga o construye desde el código fuente para **Openterface MacOS**:

    [:octicons-arrow-right-24: Instalar desde App Store](/appstore) <br>
    [:octicons-download-24: Descargar DMG Portable](macos/dmg-installation.md) <br>
    [:octicons-mark-github-16: Openterface_MacOS](https://github.com/TechxArtisanStudio/Openterface_MacOS) <br>
    [:octicons-play-24: Ver Demo](https://youtu.be/m7OpUem0zqY?si=tclfl0Jl77tmE6_e)

-   ### :fontawesome-brands-linux:{ .lg } **Linux**

    ***

    Descarga o construye desde el código fuente para **Openterface QT Linux**:

    [:octicons-download-24: Descargar {{qt_version}} AMD64 DEB](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_amd64.deb) <br>
    [:octicons-download-24: Descargar {{qt_version}} AMD64 RPM](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_amd64.rpm) <br>
    [:octicons-download-24: Descargar {{qt_version}} AMD64 AppImage](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_amd64.AppImage) <br>
    [:octicons-download-24: Descargar {{qt_version}} ARM64 DEB](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_aarch64.deb) <br>
    [:octicons-download-24: Descargar {{qt_version}} ARM64 AppImage](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_aarch64.AppImage) <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) <br>
    [:octicons-play-24: Ver Demo](https://youtu.be/_ScpI6TC0Pk?si=FSg7A2zmST8QbFec)

-   ### :fontawesome-brands-android:{ .lg } **Android**

    ***

    Descarga o construye desde el código fuente para **Android APK**:

    [:octicons-download-24: Descargar {{android_version}}](https://github.com/TechxArtisanStudio/Openterface_Android/releases/download/{{android_version}}/OpenterfaceAndroid-release.apk) <br>
    [:octicons-mark-github-16: Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) <br>
    [:octicons-play-24: Ver Demo](https://x.com/TechxArtisan/status/1825460088922071398)

</div>

???+ warning "Atención: Revisa la Privacidad y Seguridad con Aplicaciones de Terceros"
Dado que todas nuestras aplicaciones son de código abierto, podrías encontrarte con versiones alternativas de aplicaciones anfitrión para dispositivos Openterface creadas por otros. Pueden ser bastante geniales y ofrecer características adicionales, pero aquí hay un recordatorio amigable: revisa cuidadosamente sus prácticas de seguridad y privacidad—especialmente porque el control KVM involucra eventos de tu pantalla, teclado y ratón. El equipo de Openterface no puede avalar la seguridad de estas aplicaciones de terceros, ¡así que procede con precaución!

## Controles Básicos de la Aplicación Anfitrión

### 💻 Compatibilidad

-   **Software Anfitrión**: Instala nuestra aplicación anfitrión para macOS, Windows o Linux.
-   **Dispositivos Objetivo**: No se necesita configuración—simplemente conecta cualquier dispositivo con salida de video (HDMI, VGA, etc.) y un puerto USB para control de teclado/ratón. Funciona con Windows, macOS, Linux, Android e iOS.

### 🖱 Modos de Ratón

-   **Modo Absoluto**: El ratón anfitrión se mapea directamente a la posición de la pantalla objetivo.
-   **Modo Relativo**: Mueve el cursor objetivo relativo a la posición actual. Sal con un atajo.

### ⌨️ Teclado

Las pulsaciones de teclas del anfitrión se envían directamente al objetivo cuando la aplicación tiene el foco.

### ⚙️ Acceso BIOS

Controla el BIOS objetivo directamente.
Teclas comunes: F2 (Dell/Lenovo/ASUS), F10 (HP), Del (ASUS/Gigabyte/MSI), ⌥ (Apple).

### 🔊 Audio

El audio objetivo se transmite a través de HDMI y se reproduce en tu ordenador anfitrión.

### 🎥 Video

Ve tu pantalla objetivo directamente dentro de la aplicación.

-   **Modelos Actuales**: Hasta **1080p 30Hz** de visualización en la aplicación, con soporte para entrada **4K 30Hz** vía HDMI.
-   **Otras Entradas**: Compatible con VGA, DVI, Micro HDMI y más cuando se usan adaptadores apropiados.
-   **Modelos Futuros**: Se soportarán resoluciones y velocidades de fotogramas más altas a medida que se lancen nuevas versiones de hardware.

### 🔄 Puertos Conmutables

Algunos dispositivos Openterface incluyen puertos que pueden ser **conmutados entre el anfitrión y el objetivo**, como puertos USB 2.0 o ranuras de tarjetas micro-SD (en modelos próximos).

-   **Uso Uno a la Vez**: Solo un lado (anfitrión u objetivo) puede acceder al puerto a la vez.
-   **Métodos de Conmutación**:
    -   **Conmutador de hardware** — interruptor físico en el dispositivo
    -   **Botón de software** — control vía la aplicación anfitrión
-   **Importante**:
    -   Expulsa de forma segura los dispositivos de almacenamiento (unidades USB o tarjetas micro-SD) antes de conmutar.
    -   Evita conectar dispositivos de alta potencia para prevenir inestabilidad o daño.
    -   Ve la [Guía de Puertos Conmutables](/usb-switch) para detalles y diagramas lógicos.
