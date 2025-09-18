# Openterface Android

## Descripción General

Openterface Mini-KVM es una solución de hardware y software de código abierto diseñada para proporcionar funcionalidad básica de KVM (Teclado, Video, Ratón) para controlar dispositivos a través de una interfaz basada en Android. Este repositorio contiene el código fuente de la aplicación Android, configuraciones de compilación y scripts de soporte para configurar y desplegar el proyecto.

Estamos comprometidos con el hardware abierto y el software de código abierto, bajo la licencia [GNU Affero General Public License v3](LICENSE).

## Módulos de Funciones

### 1. Visualización de Video

#### Funcionalidad Principal

-   Transmite la salida de video del dispositivo objetivo conectado a la pantalla de Android en tiempo real.
-   Soporta ajustes de imagen para una visualización óptima.

![image](https://assets.openterface.com/images/android/videoConnect.webp)

#### Descripción de la Interfaz de Usuario

-   La pantalla principal muestra la transmisión de video del dispositivo objetivo, ocupando la mayor parte de la interfaz.
-   Una barra de herramientas en el lado proporciona controles de ajuste (brillo, contraste, matiz).

#### Flujo de Operación

1. Conecta el hardware Mini-KVM al dispositivo objetivo a través de HDMI y USB.
2. Conecta el Mini-KVM a tu dispositivo Android a través de USB-C.
3. Inicia la aplicación; la transmisión de video aparece automáticamente.
4. Usa los deslizadores de la barra de herramientas para ajustar el brillo, el contraste o el matiz según sea necesario.

![image](https://assets.openterface.com/images/android/colorSetting.webp)

#### Características Especiales

-   El zoom con dos dedos mejora la visualización

![image](https://assets.openterface.com/images/android/enlargeAndSideBar.webp)

---

### 2. Control del Ratón

#### Funcionalidad Principal

-   Proporciona control absoluto y relativo del ratón para interactuar con la interfaz del dispositivo objetivo.
-   Soporta clics izquierdo y derecho.
-   Selecciona el modo desde el menú de la derecha.

#### Descripción de la Interfaz de Usuario

-   La transmisión de video también funciona como un panel táctil para la entrada del ratón.
-   Un botón de acción flotante (FAB) alterna entre los modos de ratón y teclado.

#### Flujo de Operación

1. Asegúrate de que el dispositivo esté conectado correctamente.
2. Toca la pantalla para mover el cursor del ratón a esa posición (control absoluto).
3. Haz doble clic con un dedo para el clic izquierdo, clic con dos dedos para el clic derecho.
4. El modo de arrastre consiste en mantener presionado el botón izquierdo sin soltarlo.

#### Características Especiales

-   Control del ratón relativo (en desarrollo, alternar a través de la configuración cuando esté disponible).

## ![image](https://assets.openterface.com/images/android/mouseThouchMode.webp)

### 3. Entrada de Teclado

#### Funcionalidad Principal

-   Escribe en el dispositivo haciendo clic en las teclas del teclado.

#### Descripción de la Interfaz de Usuario

-   El ícono del teclado está en la esquina inferior derecha.
-   El teclado incluye teclas de acceso rápido, teclas del sistema, teclas estándar y teclas de función (F1-F12).

#### Flujo de Operación

1. Haz clic en el ícono del teclado en la esquina inferior derecha para mostrar el teclado.
2. Escribe texto o presiona las teclas de función según sea necesario.

#### Características Especiales o Atajos

-   **Teclas de Atajo**: Ctrl+C, Ctrl+V, Ctrl+Z, Ctrl+X, Ctrl+A, Ctrl+S,
    Win+Tab, Win+S, Win+E, Win+R, Win+D, Win+L, Alt+F4, Ctrl+Alt+Del, Alt+PrtScr.
-   **Teclas de Función**: F1-F12, Teclas de Símbolo.
-   **Teclas Estándar**: 0-9, A-Z, Enter, Espacio, Suprimir.

![image](https://assets.openterface.com/images/android/enlargeAndKeyBoard.webp)
![image](https://assets.openterface.com/images/android/keyBoardFunction.webp)
![image](https://assets.openterface.com/images/android/keyBoardSystem.webp)

---

Mientras tanto, siéntete libre de explorar nuestro **repositorio de GitHub** de código abierto: [Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) para el código más reciente, actualizaciones, ejemplos y para comunicar problemas.

También puedes unirte a nuestra [comunidad de Discord](/discord) para contactar con nuestro equipo de desarrollo y otros usuarios increíbles para discutir cualquier tema relacionado con KVM.

Para soporte directo, no dudes en enviarnos un correo electrónico a [support@openterface.com](mailto:support@openterface.com).

---

**¿Tienes comentarios sobre esta página?** [Háznoslo saber aquí.](https://forms.gle/wmxoR2C1VdG36mT69)
