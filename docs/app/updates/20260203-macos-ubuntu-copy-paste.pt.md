---
title: Dica de Copiar/Colar Ubuntu (macOS → Ubuntu)
description: Corrija os atalhos de colar ao controlar Ubuntu a partir do macOS com Openterface. Use o modo Windows para colar de forma confiável no estilo Ctrl, ou Editar → Colar como alternativa no modo Mac.
keywords: Openterface, macOS, Ubuntu, copiar colar, modo teclado, modo Windows, modo Mac, KVM, desktop remoto
author: Openterface
date: 2026-02-03
tags:
  - macOS
  - Ubuntu
  - keyboard
  - copy-paste
---

# Dica de Copiar/Colar Ubuntu (macOS → Ubuntu)

Ao controlar **Ubuntu** a partir do **macOS** com **Openterface**, o colar por atalho pode não funcionar de forma confiável no **modo Mac**. Este guia mostra a correção recomendada e uma alternativa simples.

![setting](https://assets2.openterface.com/images/setting.webp)

---

## Correção rápida (recomendado para Ubuntu/Linux)

1. Abra o **Openterface** no macOS.
2. Vá para **Configurações**.
3. Encontre **Modo de layout de teclado do dispositivo de destino**.
4. Selecione **Modo Windows**.

![win-mode](https://assets2.openterface.com/images/win-mode.webp)


✅ Resultado: Os atalhos de colar funcionam como esperado no Ubuntu (comportamento estilo Ctrl).

![win-ctrl+v](https://assets2.openterface.com/images/win-ctrl+v.webp)

---

## Alternativa (se quiser permanecer no modo Mac)

Se preferir manter o **modo Mac**, ainda pode colar de forma confiável usando o menu:

- **Editar → Colar**

![edit-paste](https://assets2.openterface.com/images/edit-paste.webp)

✅ Resultado: O colar funciona mesmo quando o atalho de colar é inconsistente no modo Mac.

![workaround](https://assets2.openterface.com/images/workaround.webp)

---

## Por que isso acontece

A maioria dos aplicativos Ubuntu usa atalhos **baseados em Ctrl** para colar. Em algumas configurações, o mapeamento de atalhos no **modo Mac** pode não acionar o colar de forma consistente, enquanto **Editar → Colar** funciona de forma confiável.

---

## Resumo rápido

- **Melhor experiência no Ubuntu/Linux:** use o **modo Windows**
- **Se permanecer no modo Mac:** use **Editar → Colar**

---

## Precisa de ajuda para identificar o modo certo?

Se não tiver certeza de qual modo usar, aqui está uma regra prática:

- Se o seu SO de destino for **Ubuntu/Linux**, comece com o **modo Windows** (mais consistente para atalhos comuns).
- Se você controla principalmente **destinos macOS** e quer atalhos estilo Mac, use o **modo Mac**.

Se você alterna frequentemente entre diferentes SOs de destino, considere adicionar esta página aos favoritos. Geralmente é uma correção com um clique.

---

## Perguntas frequentes

**O modo Windows altera meus atalhos do Mac?**  
Ele altera como o Openterface envia os atalhos para o **dispositivo de destino**, para que o Ubuntu receba o comportamento **estilo Ctrl** esperado.

**Posso usar colar pelo menu em qualquer modo?**  
Sim — **Editar → Colar** é uma opção confiável em ambos os modos.

**Isso afeta o Raspberry Pi OS também?**  
Frequentemente menos afetado, mas se você vir um comportamento similar, a mesma correção se aplica.
