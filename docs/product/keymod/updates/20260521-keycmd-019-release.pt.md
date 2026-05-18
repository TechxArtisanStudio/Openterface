---
draft: false
date: 2026-05-21
title: "KeyCmd 0.19: Rebranding do app, modo Compose KM Pro, suporte multilíngue e guias interativos por modo"
description: "KeyCmd 0.19 traz uma mudança significativa de marca de KeyMod para KeyCmd, o novo modo Compose KM Pro com envio HID compatível com Unicode, interface multilíngue (coreano, italiano, russo, pt-BR), guias interativos por modo e dezenas de melhorias de UX."
keywords: "KeyCmd 0.19, lançamento KeyCmd, rebranding app, modo Compose, envio HID Unicode, multilíngue, guias interativos, atualização Openterface KeyCmd, emulador HID, teclado virtual, aplicativo teclado Android"
author: "TechxArtisan Studio"
category: "Product Updates"
tags: ["KeyCmd", "Product Updates", "Release", "Compose", "i18n", "Android"]
featured: false
social:
  image: "https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp"
  title: "Lançamento do KeyCmd 0.19 — Modo Compose, rebranding, multilíngue, guias interativos"
  description: "KeyCmd 0.19 traz o novo modo Compose, rebranding do app para KeyCmd, 4 novos idiomas, guias interativos e melhorias significativas de UX."
---

# KeyCmd 0.19: Rebranding do app, modo Compose KM Pro, suporte multilíngue e guias interativos por modo

KeyCmd **0.19** (`versionCode` **19**) é uma atualização importante que traz o **rebranding** de KeyMod para KeyCmd, o novíssimo **modo Compose do KM Pro** com envio HID compatível com Unicode, uma **interface multilíngue expandida** (incluindo coreano, italiano, russo e português brasileiro), **guias interativos por modo** e dezenas de melhorias de UX nos modos teclado, gamepad e apresentação.

## Rebranding do app: KeyMod → KeyCmd

O nome de exibição do aplicativo agora é **KeyCmd** em todos os pontos de entrada. Este rebranding esclarece a distinção entre o **hardware KeyMod** e seu **aplicativo complementar KeyCmd**.

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp" alt="Tela de boas-vindas KeyCmd" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">

### O que mudou

- **Nome de exibição do app**: O ícone do launcher e a UI do sistema agora mostram "KeyCmd"
- **Fluxo de boas-vindas**: Marca e textos atualizados de KeyMod para KeyCmd
- **Artefatos CI e nomes de arquivos APK**: Usam o prefixo **KeyCmd**
- `applicationId` permanece **`com.openterface.keymod`** para atualizações locais sem interrupções

Usuários existentes: suas configurações, perfis e dispositivos pareados são mantidos. A atualização é transparente.

## Teclado e mouse: experiência em tela cheia

O KeyCmd oferece uma experiência de teclado, touchpad e teclado numérico em tela cheia — otimizada para orientações retrato e paisagem.

<div class="slideshow-container" id="slideshow-keycmd-019-kbm-pt" data-auto-slide="true" data-auto-slide-interval="3000">
  <div class="slideshow-wrapper">
    <div class="slide active">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Full-Keyboard-landscape.webp" alt="Teclado em tela cheia paisagem" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape.webp" alt="Teclado numérico paisagem" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-portrait.webp" alt="Teclado numérico retrato" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait.webp" alt="Teclado e touchpad retrato" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-km-basic-Touchpad.webp" alt="Touchpad paisagem" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Remote-Coding-portrait.webp" alt="Codificação remota com KeyCmd" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Settings-screen.webp" alt="Tela de configurações KeyCmd" style="max-height:320px;" loading="lazy">
    </div>
  </div>

  <div class="slideshow-navigation">
    <button class="nav-arrow left" onclick="changeSlide('slideshow-keycmd-019-kbm-pt', -1)">❮</button>
    <div class="slideshow-dots">
      <span class="dot active" onclick="currentSlide('slideshow-keycmd-019-kbm-pt', 1)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-pt', 2)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-pt', 3)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-pt', 4)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-pt', 5)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-pt', 6)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-pt', 7)"></span>
    </div>
    <button class="nav-arrow right" onclick="changeSlide('slideshow-keycmd-019-kbm-pt', 1)">❯</button>
  </div>
</div>

## KM Pro: modo Compose & Send

A maior novidade na versão 0.19 é o **modo Compose** no KM Pro — um editor de texto dedicado que permite digitar trechos longos e enviá-los como pressionamentos de teclas HID para a máquina de destino.

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait.webp" alt="Execução de script no modo Compose" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">


### Editor Compose

- **Barra de atalhos superior + linha de ação de composição** com controles **Limpar** e **Desfazer/Limpar**
- **Retenção de rascunho**: seu texto é mantido ao alternar submodos e mesmo após um envio bem-sucedido
- **Integração IME**: digite com o teclado do smartphone, envie como pressionamentos de teclas HID limpos
- **Progresso de envio determinístico**: uma barra de progresso visível para buffers HID longos para que você saiba exatamente quanto do envio já foi concluído

### Envio HID compatível com Unicode

- **Revisão de riscos em modo duplo**: antes de enviar texto não ASCII, um diálogo alerta sobre compatibilidade Unicode e fornece ações de inspeção e pré-visualização
- **Fluxo hexadecimal Unicode no macOS**: em hosts macOS, o app usa o método de entrada Option+código hexadecimal para caracteres estendidos
- **Diálogos de envio mais seguros**: a tela de revisão adapta seu conteúdo dependendo se o buffer é ASCII puro ou contém caracteres Unicode
- **Ferramentas de inspeção de caracteres**: o diálogo de risco de envio fornece ações **Verificar** e **Pré-visualizar**, e hosts macOS incluem uma entrada dedicada de **auditoria de caminho hexadecimal Unicode**

### Escopo do KM Basic

Na versão 0.19, **Compose & Send continua sendo um recurso do Teclado e Mouse Pro**. O KM Basic foca nos fluxos de trabalho de teclado em tela cheia, touchpad e teclado numérico.

## Suporte multilíngue

O KeyCmd agora suporta **11 idiomas de interface do app**. Este lançamento adiciona quatro novas localizações:

- **Coreano (ko)**: tradução completa da interface
- **Italiano (it)**: tradução completa da interface
- **Russo (ru)**: tradução completa da interface
- **Português brasileiro (pt-BR)**: tradução completa da interface

Junto com o inglês, chinês simplificado, chinês tradicional, japonês, francês, alemão e espanhol existentes, o KeyCmd agora cobre a grande maioria de nossa base de usuários global.

### O que mudou

- **Seletor de idioma** nas Configurações com nomes canônicos de idiomas
- **Cabeçalhos Bluetooth** e **pré-visualização de toque de tecla** localizados
- **Correções lint de lançamento** para abas de aviso de composição em todos os idiomas

## Guias interativos por modo

Cada modo agora possui um **guia interativo embutido** que conduz você passo a passo por seus recursos.

### Guias disponíveis

- **Guia do Shortcut Hub**: abre o perfil padrão e cobre a interface de detalhes, abas de categorias e gerenciamento de atalhos
- **Guia do Gamepad**: explica o layout do gamepad, gerenciamento de módulos e sistema de predefinições
- **Guia do KM Pro**: cobre o modo Compose, painel de atalhos e recursos específicos do Pro
- **Guia do KM Basic**: explica o teclado em tela cheia, gesto de deslizar com modificador pressionado e teclado numérico

### Recursos dos guias

- **Guias por modo**: cada modo tem seu próprio guia personalizado
- **Folha de repetição**: revisite qualquer guia a qualquer momento através do botão **Guia do modo** (ícone à esquerda da seção de conexão)
- **Suporte i18n**: o conteúdo dos guias está localizado em todos os idiomas do app
- **Otimizado para paisagem**: os layouts de folha inferior se adaptam corretamente na orientação paisagem

## Melhorias de UX

### Teclado

- **Pré-visualização de toque de tecla**: veja exatamente o que será enviado antes de tocar. Ativável nas Configurações. Ativado por padrão.
- **Correção HID de toque rápido**: melhoria no tempo de liberação de toques e eventos de liberação consolidados para digitação mais rápida
- **Tratamento de toque de caracteres alternativos**: pressionar longamente a tecla `a` agora mostra as alternativas ¥ (acima), £ (esquerda), € (direita) com feedback visual aprimorado
- **Gesto de deslizar com modificador pressionado**: nos guias KM Basic/Pro, um novo passo ensina o gesto de deslizar com modificador pressionado para acesso rápido a modificadores

### Gamepad

- **Barra de sessão de edição removida**: interface de gamepad mais limpa sem a antiga barra de ferramentas de sessão de edição
- **Interface e guia do gamepad**: novo polimento visual e guia interativo integrado
- **Ícone de guia do modo**: posicionado à esquerda da seção de conexão para fácil acesso

### Apresentação

- **Bloqueio de par retrato**: o modo Apresentação é limitado às orientações retrato e retrato invertido para controle estável do apresentador

### Interface e tema

- **Amostras de destaque**: substituído o seletor de família de cores do tema por amostras visuais de destaque para seleção de cores mais fácil
- **Alinhamento de destaques da UI**: todos os destaques da UI agora seguem a família de cores do tema (não a cor primária herdada)
- **Cluster direito do cabeçalho**: dimensões aprimoradas para ícones de conexão tanto no app principal quanto na interface KM Basic
- **Estilo do botão de envio Compose**: aparência do botão de envio não ASCII alinhada no modo claro

### Configurações

- **Reorganização das configurações**: nomes canônicos de idiomas; scripts de instalação do emulador renomeados para maior clareza
- **Scripts auxiliares de desenvolvimento**: renomeados para identificação mais clara de dispositivos e nomeação de ações
- **Documentação FAQ**: `docs/FAQ.md` atualizado com o comportamento atual do app

## Casos de uso reais

### Codificação remota

O KeyCmd não é apenas para gerenciamento de servidores. Desenvolvedores o usam para **sessões de codificação remota** — controlando uma máquina de desenvolvimento headless a partir de um smartphone ou tablet, com suporte completo a teclado, touchpad e teclado numérico.

## O que não mudou

**Teclado e Mouse Pro** (modo composto com barras do Shortcut Hub, layouts divididos e comportamento IME rico) continua sendo a experiência completa de antes. Todos os perfis, predefinições e dispositivos pareados existentes são mantidos.

## Obter a atualização

**Esta versão (0.19):** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

> **Nota Beta:** O aplicativo Android KeyCmd ainda está em fase Beta ativa. O repositório de código-fonte ainda não é público — planejamos torná-lo open source após uma campanha de crowdfunding bem-sucedida. Se você é um testador Beta e precisa do APK mais recente, entre em contato conosco no Discord e enviaremos o build.

Instalações existentes podem ser atualizadas no local.

## Compatível com Mini-KVM e KVM-Go

O aplicativo KeyCmd não se limita ao hardware KeyMod. Usuários existentes do Openterface também podem experimentar:

- **KVM-Go**: conexão via **Bluetooth** ou **USB**
- **Mini-KVM**: conexão via **USB**

## Notas de atualização

- **Rebranding**: o nome do app muda de KeyMod para KeyCmd. Seus dados são mantidos.
- **Modo Compose**: novo para Teclado e Mouse Pro.
- **Guias interativos**: toque no ícone do guia (à esquerda da seção de conexão) em qualquer modo para iniciar o guia interativo.
- **Idiomas**: vá para Configurações para alterar o idioma do app. O KeyCmd agora suporta 11 idiomas de interface do app.

Atenciosamente,

Openterface Team | TechxArtisan
