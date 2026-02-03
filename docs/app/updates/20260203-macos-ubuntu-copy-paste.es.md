---
title: Consejo de Copiar/Pegar en Ubuntu (macOS → Ubuntu)
description: Soluciona los atajos de pegado al controlar Ubuntu desde macOS con Openterface. Usa el modo Windows para un pegado fiable estilo Ctrl, o Edición → Pegar como alternativa en modo Mac.
keywords: Openterface, macOS, Ubuntu, copiar pegar, modo teclado, modo Windows, modo Mac, KVM, escritorio remoto
author: Openterface
date: 2026-02-03
tags:
  - macOS
  - Ubuntu
  - keyboard
  - copy-paste
---

# Consejo de Copiar/Pegar en Ubuntu (macOS → Ubuntu)

Al controlar **Ubuntu** desde **macOS** con **Openterface**, el pegado por atajo puede no funcionar de forma fiable en **modo Mac**. Esta guía muestra la solución recomendada y una alternativa sencilla.

![setting](https://assets2.openterface.com/images/setting.webp)

---

## Solución rápida (recomendado para Ubuntu/Linux)

1. Abre **Openterface** en macOS.
2. Ve a **Ajustes**.
3. Busca **Modo de disposición de teclado del dispositivo de destino**.
4. Selecciona **Modo Windows**.

![win-mode](https://assets2.openterface.com/images/win-mode.webp)


✅ Resultado: Los atajos de pegado se comportan como se espera en Ubuntu (comportamiento estilo Ctrl).

![win-ctrl+v](https://assets2.openterface.com/images/win-ctrl+v.webp)

---

## Alternativa (si quieres mantener el modo Mac)

Si prefieres mantener el **modo Mac**, aún puedes pegar de forma fiable usando el menú:

- **Edición → Pegar**

![edit-paste](https://assets2.openterface.com/images/edit-paste.webp)

✅ Resultado: El pegado funciona incluso si el atajo de pegado es inconsistente en modo Mac.

![workaround](https://assets2.openterface.com/images/workaround.webp)

---

## Por qué ocurre esto

La mayoría de las aplicaciones de Ubuntu usan atajos **basados en Ctrl** para pegar. En algunas configuraciones, el mapeo de atajos en **modo Mac** puede no activar el pegado de forma consistente, mientras que **Edición → Pegar** funciona de forma fiable.

---

## Resumen rápido

- **Mejor experiencia en Ubuntu/Linux:** usa el **modo Windows**
- **Si mantienes el modo Mac:** usa **Edición → Pegar**

---

## ¿Necesitas ayuda para identificar el modo correcto?

Si no estás seguro de qué modo usar, aquí tienes una regla sencilla:

- Si tu SO de destino es **Ubuntu/Linux**, empieza con el **modo Windows** (más consistente para atajos comunes).
- Si controlas principalmente **objetivos macOS** y quieres atajos estilo Mac, usa el **modo Mac**.

Si cambias entre diferentes SO de destino con frecuencia, considera marcar esta página. Suele ser una solución de un solo clic.

---

## Preguntas frecuentes

**¿El modo Windows cambia mis atajos de Mac?**  
Cambia cómo Openterface envía los atajos al **dispositivo de destino**, para que Ubuntu reciba el comportamiento **estilo Ctrl** esperado.

**¿Puedo usar pegar por menú en cualquier modo?**  
Sí — **Edición → Pegar** es una opción fiable en ambos modos.

**¿Esto afecta también a Raspberry Pi OS?**  
A menudo menos afectado, pero si ves un comportamiento similar, la misma solución se aplica.
