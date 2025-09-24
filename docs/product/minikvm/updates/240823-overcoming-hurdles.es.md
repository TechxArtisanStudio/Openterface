---
draft: false
date: 2024-08-22
description: "Actualización importante Openterface Mini-KVM: certificación CE completada, producción en curso, nueva ETA mediados de enero. Hardware V1.9 finalizado con pines de expansión, desarrollo de app Android, empaquetado mejorado y manual multilingüe en progreso."
keywords: "Openterface Mini-KVM, certificación CE, hardware V1.9, actualización producción, cronograma envío, desarrollo app Android, pines expansión, KVM-over-IP, control calidad, empaquetado producto, manual multilingüe, USB KVM, fabricación tech, hardware open source, actualización entrega"
---

# Superando obstáculos: Actualización de progreso y nueva cronología

Hola a todos,

Espero que todos estén bien. Ha pasado un tiempo desde nuestra última actualización. Me gustaría poder decir que todo ha ido sobre ruedas para Openterface, pero hemos encontrado algunos obstáculos que retrasarán nuestro cronograma de entrega. Aunque esto no era lo que esperábamos, estamos abordando estos desafíos de frente y haciendo progreso constante con muchas buenas noticias que compartir. Esta publicación es una **lectura de 7 minutos**, así que profundicemos en los detalles para que sepan exactamente dónde están las cosas y qué viene después.

## Regulación, producción y calidad

Antes de poder iniciar la producción, tuvimos que pasar las pruebas de calidad necesarias según las regulaciones, particularmente la certificación CE. Como nuestra versión toolkit incluye no solo el Mini-KVM sino también varios accesorios, cada parte necesitaba someterse a pruebas CE. Estas pruebas tomaron más tiempo del esperado (resulta que los cables pueden ser bastante exigentes), pero la gran noticia es que **¡hemos pasado CE para nuestro Mini-KVM y todos sus componentes!** A continuación hay una visión general de las certificaciones para todas nuestras partes: Mini-KVM, cable HDMI, cable Type-C naranja, cable Type-C corto negro y cable VGA2HDMI. Con la certificación en mano, nuestro cronograma de producción ahora es cierto, y nuestros fabricantes están **actualmente produciendo todas las partes** mientras hablo.

![240823-0](https://www.crowdsupply.com/img/fcb5/db59e179-2413-4d57-8462-2285c007fcb5/openterface-240823-0_jpg_gallery-lg.jpg)
*Los requisitos UKCA y CE son los mismos para nuestros productos electrónicos, con CE cubriendo también el cumplimiento RoHS.*

Hace dos semanas, visitamos uno de nuestros fabricantes para capacitar a sus gerentes de línea en control de calidad para los cables naranjas antes de que nos los enviaran. Ahora, TODOS los cables naranjas han sido producidos y están sentados en una esquina de nuestro estudio.
![240823-1](https://www.crowdsupply.com/img/28dc/34844b54-0e02-414d-b58b-d40e8abe28dc/openterface-240823-1_jpg_gallery-lg.jpg)
*Kevin y Shawn estaban explicando los métodos de prueba para asegurar que el cable naranja funcione correctamente con nuestro Openterface Mini-KVM.*

Haremos la misma tarea esta semana para capacitar QA en primera línea de producción para las otras partes también. Aquí hay muestras de cables adicionales.
![240823-2](https://www.crowdsupply.com/img/e703/abb8ffa5-eb85-4eb9-b5f8-d8a3d349e703/openterface-240823-2_jpg_md-xl.jpg)
*Orgullosamente marcados con nuestro logo TechxArtisan, estos son muestras del cable HDMI, el cable Type-C corto y el cable VGA-to-HDMI.*

Esperamos que las otras partes y Mini-KVMs lleguen pronto de nuestros fabricantes, momento en el cual verificaremos la calidad de cada componente y los empaquetaremos correctamente en nuestro estudio antes del envío. En otras palabras, **nuestro equipo asegurará personalmente la calidad** antes de que llegue a sus manos.

## Envío, retrasos potenciales y nueva ETA

**La incertidumbre actual reside en el proceso de envío**. Después de investigar varias compañías de envío, descubrimos que el envío tomará tiempo adicional ya que probablemente transferiremos paquetes a través de un almacén antes de llegar al almacén de Crowd Supply. Todavía estamos debatiendo si elegir transporte marítimo o aéreo—por favor tengan paciencia con nosotros por unos días más mientras resolvemos los arreglos.

El despacho de aduanas es otro obstáculo potencial que podría causar retrasos inesperados. Una vez que nuestros productos lleguen al almacén de Crowd Supply en los Estados Unidos, tomarán una o dos semanas para enviarse globalmente basándose en cada pedido. Para patrocinadores fuera de los Estados Unidos, los paquetes individuales aún necesitarán pasar por envío global y despacho de aduanas en el país de destino.

Considerando la situación actual y agregando algo de tiempo de buffer, sigo cautelosamente optimista de que completaremos la entrega antes del final de este año, con **una nueva ETA de mediados de enero**. Realmente me disculpo por la inconveniencia y aprecio su apoyo y paciencia durante este cambio.

## Hardware V1.9 finalizado

Como pueden saber de nuestro anterior [post de Reddit](https://www.reddit.com/r/Openterface_miniKVM/comments/1e25pco/openterface_minikvm_v19_with_pins_for_more/), decidimos **actualizar nuestro hardware a V1.9**, incluyendo un conjunto de pines de expansión hackeables. Esto no era parte del plan original para la campaña de crowdfunding, pero creemos que mejora significativamente el **potencial para uso más amplio** del hardware.

![240823-3](https://www.crowdsupply.com/img/77d7/09a9d0e5-3065-4f3e-8b61-bae66b5c77d7/openterface-240823-3_jpg_md-xl.jpg)
*Los pines VCC, GND, Target D+, Target D-, Host D+ y Host D-—donde 'D' significa datos USB.*

Una motivación clave era **permitir que el interruptor USB sea alternado a nivel de software**. ¿Por qué es esto importante? En nuestra hoja de ruta, **apuntamos a soportar una solución KVM-over-IP**, como VNC, en el futuro. La idea es hacer coincidir el control KVM local con el protocolo VNC, permitiendo a los usuarios controlar remotamente el ordenador objetivo a través del ordenador anfitrión. En tal escenario remoto, la capacidad para que los usuarios cambien el puerto USB es esencial, especialmente cuando se requieren transferencias de archivos entre el anfitrión y el objetivo.

**Los pines de expansión también abren posibilidades para más**, como integración con iPadOS, control ATX, bridging de red y bypass de audio. Aunque no profundizaré en todos los detalles aquí, los animo a unirse a nuestra comunidad Openterface para discutir más con nosotros.

Esta actualización de hardware podría potencialmente extender nuestra solución Openterface para operar sobre IP e incluir características más avanzadas mientras mantiene aún su fortaleza central como herramienta KVM-over-USB plug-and-play—perfecta para profesionales IT navegando entornos IT inciertos, como centros de datos no familiares.

Me complace reportar que V1.9 ha pasado nuestras pruebas internas básicas y será finalizado como la versión oficial para todos nuestros patrocinadores. Sin embargo, esta actualización de hardware requerirá pruebas adicionales, y cualquier desarrollo basado en estos pines de expansión será experimental y probablemente tendrá errores. Aquí es donde pueden contribuir. Contamos con la comunidad open-source para ayudarnos a mejorar Openterface juntos.

## Más actualizaciones de software

En el frente de software, estamos haciendo avances emocionantes. ¡Ahora estamos sumergiéndonos en la **app Openterface Android**! Echen un vistazo a este [tweet](https://x.com/TechxArtisan/status/1825460088922071398) para una demo temprana mostrando control KVM fluido, movimiento del ratón y clics en acción. Más características están en camino, y como siempre, una vez que hayamos pulido el código un poco más, **esta app también será open-sourced** en nuestro repo GitHub [Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android).
![240823-4](https://www.crowdsupply.com/img/7007/b192f260-1e1f-4dab-905b-fb0a6d927007/openterface-240823-4_jpg_md-xl.jpg)
*¡Usando solo nuestras yemas de los dedos para controlar KVM un ordenador Linux desde una tablet Android. Genial!*

Nuestra versión QT acaba de recibir una actualización útil—¡ahora pueden [transferir texto del anfitrión al objetivo](https://x.com/TechxArtisan/status/1825919721960780131)! Así que ahora esta característica es soportada en las apps anfitrión de macOS, Windows y Linux.

Además, también estamos planeando agregar una característica divertida—[un movimiento automático del ratón para prevenir que su ordenador objetivo se duerma](https://x.com/TechxArtisan/status/1825471186668847241). ¿Deberíamos ir con la pelota de ping-pong rebotando alrededor de la pantalla o el efecto clásico del salvapantallas DVD? Voten y comenten el [tweet](https://x.com/TechxArtisan/status/1825470086800691459) 😃

## Diseño de paquete, etiquetado y manual

Hemos estado [experimentando con varios mock-ups y diseños de empaquetado](https://www.reddit.com/r/Openterface_miniKVM/comments/1elm4vq/almost_ready_to_finalize_our_package_design/) para encontrar el equilibrio perfecto entre varios factores clave:

- Seleccionar materiales lo suficientemente robustos para proteger el producto y sus partes durante el envío,
- Crear etiquetado informativo que ayude a los usuarios a entender el producto de un vistazo,
- Asegurar cumplimiento con regulaciones,
- Hacer el empaquetado visualmente atractivo,
- Y ser eco-friendly minimizando el uso de plástico donde sea posible.

Además, hemos hecho varias mejoras a la bolsa toolkit antigua, incluyendo:

- Espacio de almacenamiento más grande,
- Cremallera naranja elegante,
- Materiales exteriores e interiores actualizados,
- Y un bolsillo de malla súper elástico.

Elegimos este material porque logra el equilibrio ideal entre ser económico, agradable al tacto y lo suficientemente duradero para proteger los artículos dentro. **Estamos seguros de que lo amarán**.

![240823-5](https://www.crowdsupply.com/img/099a/75e16f52-bd0c-4652-af27-08caf448099a/openterface-240823-5_jpg_md-xl.jpg)

También estamos actualizando las etiquetas en la carcasa de aluminio para hacerlas lo más informativas y visualmente atractivas posible. Esperamos que estas mejoras mejoren su experiencia de usuario y hagan más fácil comenzar con Openterface.

![240823-6](https://www.crowdsupply.com/img/94d8/441a5757-2d6a-4c79-885b-7b5b3a7094d8/openterface-240823-6_jpg_md-xl.jpg)

Estamos finalizando el manual Openterface, que estará disponible en inglés, alemán, francés, japonés y chino. Disculpas si perdimos su idioma—¡nuestra caja no es del tamaño TARDIS (la caja de policía del Doctor Who)! Pero haremos nuestro mejor esfuerzo para agregar más traducciones en nuestro sitio web.

![240823-7](https://www.crowdsupply.com/img/e2d9/2e5a2086-20f0-47ec-a27b-288d10d0e2d9/openterface-240823-7_jpg_md-xl.jpg)

## Revisión de idioma de la comunidad

He estado usando ChatGPT para asistir con traducciones, pero a veces puede fallar con frases y elección de palabras. Si no es demasiado problema, apreciaría mucho cualquier ayuda en revisar el contenido en otros idiomas, especialmente para los materiales impresos que estamos a punto de finalizar. He actualizado todo el contenido textual para el empaquetado en nuestra carpeta GitHub [product-printed-materials](https://github.com/TechxArtisanStudio/Openterface/tree/main/product-printed-materials), donde pueden revisar y enviar cualquier mejora. También pueden DMarme directamente. ¡Gracias!

## Observaciones finales y progreso en curso

Nos disculpamos nuevamente por los retrasos y el cambio en la ETA de nuestro producto. Gracias por su paciencia y por quedarse con nosotros—¡estamos trabajando duro para llevárselo lo antes posible! Los actualizaré inmediatamente una vez que nuestro envío esté arreglado. Más actualizaciones están en camino, ¡así que únanse a nuestra comunidad Openterface y manténganse atentos!

Saludos,

Billy Wang  
Gerente de Producto  
Equipo Openterface | TechxArtisan
