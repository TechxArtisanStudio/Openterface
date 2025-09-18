# Openterface QT para Win y Linux

Este documento proporciona una visión general de un software KVM (Teclado, Video, Ratón) multiplataforma desarrollado utilizando Qt, compatible con los sistemas operativos Linux y Windows. El software facilita el control de un dispositivo objetivo desde un sistema anfitrión, ofreciendo una variedad de características accesibles a través de su barra de menú y funcionalidades adicionales.

## Características de la Barra de Menú Principal

### Preferencias

El menú de Preferencias permite a los usuarios personalizar la configuración a través de un diálogo con cuatro páginas:<br>
![Preferences Gernal](https://assets.openterface.com/images/qt/preferenceGernal.webp)

-   **General** Esta página configura el filtro de registros de depuración y si se inhabilita o no el protector de pantalla cuando la aplicación está en ejecución. Las categorías de registro incluyen:

    -   Núcleo
    -   Serial
    -   Interfaz de Usuario
    -   Anfitrión

    Los usuarios pueden elegir guardar los registros en un archivo .txt y habilitar o no el protector de pantalla.<br>

![Preferences Video](https://assets.openterface.com/images/qt/preferenceVideo.webp)

-   **Video** Esta página permite a los usuarios:

    -   Seleccionar qué datos de la cámara capturar.
    -   Establecer la resolución.
    -   Elegir el formato de transmisión de video.

-   **Audio** Esta página está actualmente en desarrollo.<br>

![Preferences TargetControl](https://assets.openterface.com/images/qt/preferenceTargetControl.webp)

-   **Control del Objetivo** Esta página proporciona opciones para configurar los modos de control para el dispositivo objetivo:

    -   **Modos de control:**

        -   **Teclado + Ratón + Dispositivo USB HID**
        -   **Teclado USB**
        -   **Teclado + Ratón**
        -   **Dispositivo USB HID**

    -   **Establecer el ID de Vendedor (VID) y el ID de Producto (PID) leídos del objetivo.**
    -   **Definir el descriptor USB para el objetivo.**

### Editar

-   **Pegar:** Tanto la opción Pegar en el menú Editar como el botón de pegar en la esquina superior izquierda permiten a los usuarios pegar texto del portapapeles del anfitrión al dispositivo objetivo.

### Control

Este menú proporciona opciones para:<br>

-   Establecer modos de movimiento del ratón: Absoluto o Relativo. **Control >> MouseMode >> Absoluto o Relativo.**
-   Alternar la visibilidad del cursor del ratón del anfitrión. **Control >> Visibilidad del Ratón >> Ocultar Automáticamente o Mostrar Siempre.**
-   Cambiar un puerto USB en el hardware entre el uso del objetivo y el anfitrión. **Control >> USB Conmutable >> A Objetivo o A Anfitrión.**
-   Ajustar la velocidad en baudios para la transmisión del chip. **Control >> Baudrate >> 9600, 115200.**

### Avanzado

El menú Avanzado incluye las siguientes opciones:<br>
![Advance menu](https://assets.openterface.com/images/qt/menuAdvance.webp)

-   **Verificación del Entorno:** Verifica si los controladores necesarios para el software están instalados.
-   **Reiniciar Puerto Serial:** Reinicia el puerto serial.
-   **Restablecer Teclado y Ratón:** Restablece la configuración del teclado y el ratón.
-   **Restablecer Chip HID de Fábrica:** Restaura el chip HID a su configuración de fábrica.<br>
    ![Advance SerialConsole](https://assets.openterface.com/images/qt/advanceSerialConsole.webp)
-   **Consola Serial:** Abre una nueva ventana para supervisar todos los mensajes enviados al puerto serial, con filtros para mensajes enviados/recibidos.<br>
    ![Advance ScriptTool](https://assets.openterface.com/images/qt/advanceScriptTool.webp)
-   **Herramienta de Script:** Ejecuta scripts de AutoHotkey (AHK). Esta función imita AutoHotkey pero solo admite un subconjunto de funciones de ratón/teclado y capacidades de captura de pantalla. Los scripts afectan al dispositivo objetivo.
-   **Servidor TCP:** Recibe comandos de AutoHotkey a través de TCP para ejecutarlos en el dispositivo objetivo.
-   **Actualización de Firmware:** Descarga el último firmware de un servidor remoto, permitiendo a los usuarios elegir si desean instalarlo en el dispositivo.

### Idiomas

El idioma de la interfaz se puede establecer en:

-   Danés
-   Inglés
-   Alemán
-   Francés
-   Japonés
-   Sueco

### Ayuda

El menú de Ayuda proporciona: <br>
![Help menu](https://assets.openterface.com/images/qt/menuHelp.webp)

-   Enlaces al sitio web oficial y formularios de retroalimentación para problemas de software/hardware.
-   Información sobre la compra de hardware.
-   Una descripción del entorno del software.
-   Acerca de: Detalles sobre la organización.
-   Actualización: Verifica si hay actualizaciones de software.

## Funciones de la Barra de Menú (De Izquierda a Derecha)

La barra de menú, de izquierda a derecha, incluye las siguientes funcionalidades:<br>

![MenuBar](https://assets.openterface.com/images/qt/menubar.webp)

-   Selección de Diseño de Teclado: Elige el diseño del teclado.
-   Controles de Zoom: Acercar, alejar o restablecer la visualización de la transmisión de video capturada.
-   Teclado Virtual: Incluye teclas de función y combinaciones de atajos preestablecidas.
-   Captura de Pantalla: Captura toda la pantalla del objetivo y la guarda en una carpeta predeterminada.
-   Modo de Pantalla Completa: Alterna la visualización en pantalla completa.
-   Pegar: Pega texto del portapapeles del anfitrión al objetivo.
-   Danza del Ratón: Activa el ratón para realizar movimientos preestablecidos.
-   Indicador de Dispositivo USB: Muestra si un dispositivo USB está asignado al objetivo o al anfitrión.

Mientras tanto, siéntete libre de explorar nuestro **repositorio de GitHub** de código abierto: [Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) para el código más reciente, actualizaciones, ejemplos y para comunicar problemas.

También puedes unirte a nuestra [comunidad de Discord](/discord) para contactar con nuestro equipo de desarrollo y otros usuarios increíbles para discutir cualquier tema relacionado con KVM.

Para soporte directo, no dudes en enviarnos un correo electrónico a [support@openterface.com](mailto:support@openterface.com).

---

**¿Tienes comentarios sobre esta página?** [Háznoslo saber aquí.](https://forms.gle/wmxoR2C1VdG36mT69)
