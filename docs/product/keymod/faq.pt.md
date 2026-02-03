---
title: Perguntas frequentes sobre Openterface KeyMod Series
description: Perguntas frequentes sobre KeyMod Series: recursos, compatibilidade, plataformas e informações de pré-lançamento.
keywords: KeyMod, Openterface, emulador HID, teclado Bluetooth, teclado telefone, open source, pré-lançamento, Android, iPadOS
---

# Perguntas frequentes sobre Openterface KeyMod

Bem-vindo às perguntas frequentes do **Openterface KeyMod**.  
Se não encontrar o que precisa, **envie-nos um e-mail em [info@openterface.com](mailto:info@openterface.com)** ou **junte-se à nossa comunidade** no [Discord](/discord) ou [Reddit](/reddit).

⚠️ **Nota**: KeyMod está atualmente em desenvolvimento de pré-lançamento. Recursos, especificações e design estão sujeitos a alterações conforme finalizamos o produto.

---

## :material-clipboard-list: Navegação rápida

- [Perguntas frequentes sobre Openterface KeyMod](#perguntas-frequentes-sobre-openterface-keymod)
  - [:material-clipboard-list: Navegação rápida](#material-clipboard-list-navegação-rápida)
  - [Geral](#geral)
  - [Conectividade](#conectividade)
  - [Recursos](#recursos)
  - [Pré-lançamento](#pré-lançamento)

---

## Geral

**:material-chat-question:{ .faq } O que é KeyMod?**

KeyMod é um emulador HID (teclado e mouse) compacto USB + Bluetooth que transforma seu telefone em um teclado e trackpad portáteis. Use-o para controlar dispositivos que precisam de entrada de teclado/mouse—quiosques, smart TVs, set-top boxes, displays externos—sem carregar um teclado completo.

**:material-chat-question:{ .faq } Quais plataformas o aplicativo KeyMod suporta?**

O aplicativo controlador KeyMod foca em **Android** e **iPadOS**. Também estamos expandindo o controle de desktop com software **Windows e macOS** em nosso ecossistema Openterface mais amplo.

**:material-chat-question:{ .faq } O dispositivo de destino precisa de algum software?**

Não. KeyMod emula um teclado e mouse USB padrão. O dispositivo de destino o reconhece como hardware HID plug-and-play—nenhum driver ou instalação de software necessária.

**:material-chat-question:{ .faq } KeyMod é open source?**

Sim. KeyMod é hardware e software abertos. Publicaremos esquemas, arquivos PCB, firmware, software e BOM conforme o projeto evolui.

---

## Conectividade

**:material-chat-question:{ .faq } USB ou Bluetooth—qual devo usar?**

- **USB**: Mais confiável, menor latência. Use quando quiser a conexão mais estável.
- **Bluetooth**: Sem fios. Use quando quiser uma configuração mais leve e o cenário permitir wireless.

**:material-chat-question:{ .faq } Quais variantes de hardware estão planejadas?**

1. **Conector 2-em-1** — Plug USB A + USB C combinado para ampla compatibilidade
2. **Versão USB C** — Plug USB C dedicado para dispositivos modernos

---

## Recursos

**:material-chat-question:{ .faq } Quais layouts de gamepad são suportados?**

KeyMod pode atuar como um controlador de jogo virtual com **layout Xbox**, **layout PlayStation** e **layout NES**.

**:material-chat-question:{ .faq } Posso criar perfis e macros personalizados?**

Sim. O aplicativo móvel open source suporta perfis de entrada personalizados, macros, atalhos de teclado e atalhos de fluxo de trabalho. Você também pode usar modos de teclado numérico e gamepad.

**:material-chat-question:{ .faq } O que são os botões de hardware programáveis?**

KeyMod inclui botões de hardware programáveis para ações no dispositivo como gatilhos rápidos e fluxos de trabalho simples estilo macro. Esta capacidade ainda é experimental e será refinada através do feedback da comunidade.

---

## Pré-lançamento

**:material-chat-question:{ .faq } Quando o KeyMod será lançado?**

KeyMod está em desenvolvimento de pré-lançamento. Inscreva-se na [página do produto](/product/keymod/) para notificações de lançamento e atualizações.

**:material-chat-question:{ .faq } Como o KeyMod se relaciona com Mini-KVM e KVM-Go?**

KeyMod usa o núcleo HID comprovado do Openterface Mini-KVM. Compartilha a mesma abordagem de emulação de teclado e mouse baseada em hardware, mas é projetado para um caso de uso diferente: transformar seu telefone em um teclado/trackpad portátil para controle local de dispositivos, em vez de captura de vídeo KVM-over-USB.
