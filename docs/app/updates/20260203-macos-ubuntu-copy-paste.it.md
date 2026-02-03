---
title: Suggerimento Copia/Incolla Ubuntu (macOS → Ubuntu)
description: Correggi i collegamenti per incollare quando controlli Ubuntu da macOS con Openterface. Usa la modalità Windows per un incolla affidabile in stile Ctrl, o Modifica → Incolla come soluzione alternativa in modalità Mac.
keywords: Openterface, macOS, Ubuntu, copia incolla, modalità tastiera, modalità Windows, modalità Mac, KVM, desktop remoto
author: Openterface
date: 2026-02-03
tags:
  - macOS
  - Ubuntu
  - keyboard
  - copy-paste
---

# Suggerimento Copia/Incolla Ubuntu (macOS → Ubuntu)

Quando controlli **Ubuntu** da **macOS** con **Openterface**, l'incolla tramite scorciatoia potrebbe non funzionare in modo affidabile in **modalità Mac**. Questa guida mostra la correzione consigliata e una semplice soluzione alternativa.

![setting](https://assets2.openterface.com/images/setting.webp)

---

## Correzione rapida (consigliata per Ubuntu/Linux)

1. Apri **Openterface** su macOS.
2. Vai in **Impostazioni**.
3. Trova **Modalità layout tastiera dispositivo di destinazione**.
4. Seleziona **Modalità Windows**.

![win-mode](https://assets2.openterface.com/images/win-mode.webp)


✅ Risultato: Le scorciatoie per incollare si comportano come previsto su Ubuntu (comportamento in stile Ctrl).

![win-ctrl+v](https://assets2.openterface.com/images/win-ctrl+v.webp)

---

## Soluzione alternativa (se vuoi restare in modalità Mac)

Se preferisci mantenere la **modalità Mac**, puoi comunque incollare in modo affidabile usando il menu:

- **Modifica → Incolla**

![edit-paste](https://assets2.openterface.com/images/edit-paste.webp)

✅ Risultato: L'incolla funziona anche se la scorciatoia per incollare è incoerente in modalità Mac.

![workaround](https://assets2.openterface.com/images/workaround.webp)

---

## Perché succede

La maggior parte delle app Ubuntu utilizza scorciatoie **basate su Ctrl** per incollare. In alcune configurazioni, il mapping delle scorciatoie in **modalità Mac** potrebbe non attivare l'incolla in modo coerente, mentre **Modifica → Incolla** funziona in modo affidabile.

---

## Riepilogo rapido

- **Migliore esperienza su Ubuntu/Linux:** usa la **modalità Windows**
- **Se resti in modalità Mac:** usa **Modifica → Incolla**

---

## Hai bisogno di aiuto per identificare la modalità giusta?

Se non sei sicuro di quale modalità usare, ecco una regola pratica:

- Se il tuo OS di destinazione è **Ubuntu/Linux**, inizia con la **modalità Windows** (più coerente per le scorciatoie comuni).
- Se controlli principalmente **dispositivi macOS** e vuoi scorciatoie in stile Mac, usa la **modalità Mac**.

Se passi spesso tra diversi OS di destinazione, considera di aggiungere questa pagina ai segnalibri. Di solito è una correzione con un solo clic.

---

## Domande frequenti

**La modalità Windows cambia le mie scorciatoie Mac?**  
Cambia il modo in cui Openterface invia le scorciatoie al **dispositivo di destinazione**, così Ubuntu riceve il comportamento **in stile Ctrl** previsto.

**Posso usare incolla dal menu in qualsiasi modalità?**  
Sì — **Modifica → Incolla** è un'opzione affidabile in entrambe le modalità.

**Questo influisce anche su Raspberry Pi OS?**  
Spesso meno influenzato, ma se vedi un comportamento simile, la stessa correzione si applica.
