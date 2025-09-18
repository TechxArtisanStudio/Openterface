# Preguntas Frecuentes de las Apps

Bienvenidos a las preguntas frecuentes de nuestras apps. Si no encuentran la respuesta que necesitan, **envíennos un email a [info@openterface.com](mailto:info@openterface.com)** o **únanse a nuestra comunidad** en [Discord](/discord) o [Reddit](/reddit) para conectarse con nuestro equipo de desarrollo y otros usuarios.

⚠️ *Las preguntas frecuentes pueden volverse obsoletas — ¡por favor háganos saber si encuentran algo que necesita actualización!*

### :material-clipboard-list: Lista de Preguntas

- [¿Dónde puedo descargar las aplicaciones host?](#host-app-download)
- [¿Por qué las características difieren entre diferentes apps host?](#host-app-differences)
- [¿Qué app host ofrece actualmente la mejor experiencia?](#best-host-app)
- [¿Hay una app host que soporte ChromeOS?](#host-app-chromeos)
- [¿Hay una app host que soporte los dispositivos móviles de Apple?](#host-app-ios)
- [¿Qué hacer si F11 no funciona en las aplicaciones macOS?](#f11-macos-issue)

#### :material-chat-question:{ .faq } ¿Dónde puedo descargar las aplicaciones host? {: #host-app-download }

Visiten nuestra [página de instalación de aplicación host](/quick-start/#install-host-application) para descargas oficiales que soportan **MacOS, Windows, Linux y Android**.

??? warning "Privacidad y Seguridad: Tengan cuidado al usar apps host de terceros"
    Como nuestro proyecto es de código abierto, pueden encontrar versiones alternativas de aplicaciones host compatibles con nuestro Mini-KVM desarrolladas por otros. Aunque estas pueden ofrecer características adicionales, asegúrense de revisar sus prácticas de seguridad y privacidad. **El equipo de Openterface no puede garantizar o ser responsable de la seguridad de las aplicaciones de terceros**.

#### :material-chat-question:{ .faq } ¿Por qué las características difieren entre diferentes apps host? {: #host-app-differences }

Nuestro equipo de desarrollo mantiene activamente aplicaciones host para macOS, Linux, Windows y Android, pero debido a desafíos específicos de la plataforma y recursos limitados, el progreso de desarrollo varía. Esto significa que algunas características podrían aparecer primero en una plataforma y tomar más tiempo en llegar a otras.

Estamos haciendo nuestro mejor esfuerzo para sincronizar el desarrollo de características en todas las plataformas, pero es un trabajo en progreso.

Sus comentarios juegan un papel importante en dar forma a nuestra hoja de ruta de desarrollo — ya sea a través de nuestra [comunidad](/community/) o nuestro [repositorio de GitHub](/app/). ¡Cada sugerencia nos ayuda a priorizar lo que más les importa!

Si son desarrolladores, sus contribuciones son increíblemente valiosas — ¡y nos encantaría su ayuda para acelerar el proceso!

#### :material-chat-question:{ .faq } ¿Qué app host ofrece actualmente la mejor experiencia? {: #best-host-app }

A partir de marzo de 2025, las apps host basadas en Qt para Windows y Linux ofrecen el conjunto de características más completo en general. La versión macOS se destaca por su experiencia de usuario más fluida y refinada, gracias a una integración de sistema más profunda y mejoras de UI. La app Android es una opción conveniente sobre la marcha, con más características que están alcanzando constantemente.

#### :material-chat-question:{ .faq } ¿Hay una app web que pueda usar en Chrome u otras plataformas? {: #host-app-chromeos }

¡Sí! Uno de nuestros increíbles miembros de la comunidad, [Kashall](https://github.com/kashalls/openterface-viewer/), construyó **una app web de código abierto ligera** que pueden usar directamente en su navegador: [openterface-viewer.pages.dev](https://openterface-viewer.pages.dev). Aún no es parte de nuestra documentación oficial, pero nuestro equipo de desarrollo la probó y la encontró sólida, fácil de usar y súper práctica — especialmente en Chrome o cuando quieren algo rápido y basado en navegador. ¡Pruébenla!

#### :material-chat-question:{ .faq } ¿Hay una app host que soporte los dispositivos móviles de Apple? {: #host-app-ios }

Actualmente estamos explorando la compatibilidad con los sistemas móviles de Apple, como iOS e iPadOS. Debido a los controles estrictos de Apple, estas plataformas podrían no soportar conexiones cableadas con dispositivos de terceros. Sin embargo, la situación podría cambiar, o podría haber soluciones alternativas potenciales. Si tienen alguna perspectiva o sugerencia, los invitamos a unirse a nuestra comunidad para discutirlas con nosotros. Estamos comprometidos a mejorar la conveniencia de nuestro dispositivo soportando tantos sistemas como sea posible. Si están interesados en ayudar con nuestro desarrollo, ¡vengan a pasar tiempo con nosotros en la comunidad o envíennos un email!

#### :material-chat-question:{ .faq } ¿Qué hacer si F11 no funciona en las aplicaciones macOS? {: #f11-macos-issue }

En macOS, presionar F11 muestra el escritorio de macOS en lugar de pasar la tecla F11 a la app y la computadora objetivo. Para arreglar esto, pueden desvincular F11 de la función "Mostrar Escritorio".

???+ info "Arreglando el problema de la tecla F11 en macOS"
    1. Vayan a **Configuración del Sistema**.
    2. Seleccionen **Escritorio y Dock**.
    3. Desplácese hacia abajo y hagan clic en el botón **"Atajos…"**.
    4. Encuentren **"Mostrar Escritorio"** y configúrenlo en el guión **(-)** en la parte inferior de la lista desplegable.
    5. Este cambio permitirá que la tecla F11 pase a su aplicación en la computadora objetivo.
