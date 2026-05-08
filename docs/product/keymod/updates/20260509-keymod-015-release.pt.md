---
draft: false
date: 2026-05-09
title: "KeyMod 0.15: Pipeline de Predefinições do Gamepad, Teclado e Rato (Basic), Layouts Multi-Touchpad"
description: "KeyMod 0.15 inclui a pipeline de predefinições do gamepad com esquema v7, layouts multi-touchpad, nível Teclado e Rato (Basic) com teclado em ecrã inteiro, e marca KeyMod em toda a app. Um passo importante para uma experiência de entrada refinada."
keywords: "KeyMod 0.15, KeyMod lançamento, predefinição gamepad, multi-touchpad, teclado rato basic, marca KeyMod, Openterface KeyMod atualização, emulador HID, gamepad virtual, app teclado Android"
author: "TechxArtisan Studio"
category: "Atualizações do Produto"
tags: ["KeyMod", "Atualizações do Produto", "Lançamento", "Gamepad", "Teclado", "Android"]
featured: false
social:
  image: "https://assets.openterface.com/images/keymod/keymod-015-release.jpg"
  title: "KeyMod 0.15 lançamento — predefinições gamepad, nível basic, multi-touchpad"
  description: "KeyMod 0.15 traz a pipeline de predefinições do gamepad v7, um nível dedicado de Teclado e Rato (Basic), layouts multi-touchpad e nova marca KeyMod."
---

# KeyMod 0.15: Pipeline de Predefinições do Gamepad, Teclado e Rato (Basic), Layouts Multi-Touchpad

KeyMod **0.15** (`versionCode` **15**) é uma versão de referência que inclui três funcionalidades principais: a **pipeline de predefinições do gamepad** com esquema de layout **v6-v7**, o nível dedicado **Teclado e Rato (Basic)** e layouts **multi-touchpad**. Esta atualização também traz a marca **KeyMod** completa no fluxo de boas-vindas e nos artefactos de compilação.

## Gamepad: Pipeline de Predefinições v7

O gamepad utiliza agora um **sistema de predefinições** que permite guardar, carregar, importar e exportar layouts de controlador personalizados.

### O que mudou

- **Preset store v7** substitui os layouts integrados anteriores. As predefinições de fábrica clássicas (`preset_classic_*`) e **Two buttons** (`preset_two_buttons`) foram removidas do disco. Apenas **`preset_default`** permanece como layout de fábrica protegido contra eliminação.
- **Esquema v7** torna **`stick_left`** opcional. Um layout pode agora não ter nenhum módulo de polegar esquerdo. O menu **Add module** insere **`stick_left`**, **`stick_left_2`**, **`stick_left_3`**, etc.
- **Suporte multi-touchpad**: as predefinições podem incluir múltiplos touchpads (`touchpad_1`, `touchpad_2`). Adicionar um touchpad aloca o próximo id disponível com uma âncora ligeiramente deslocada. Os botões do rato L/M/R incluídos são partilhados entre todos os touchpads.
- **Tamanho dos botões do rato no touchpad**: os botões do rato usam agora um raio de desenho predefinido maior. Podes ajustar o tamanho com pressão longa **Mouse button size** no touchpad ou **This button size** em módulos de rato individuais.
- **Valores predefinidos do stick auxiliar**: **`stick_left_2+`** por defeito para cruz D-pad + mapeamento WASD.

### Gestão de predefinições

- **Toca** no chip Preset na barra de ferramentas para percorrer os layouts disponíveis
- **Pressão longa** para a lista completa de predefinições com opções de importação, adicionar módulo e exportar
- O layout **emu-6** incluído serve como predefinição inicial
- O criador de exportação suporta i18n para partilhar predefinições entre idiomas

## Teclado e Rato (Basic)

Um nível dedicado de teclado em ecrã inteiro desenhado para digitação focada sem o cabeçalho da app.

### O que obténs

- **Teclado em ecrã inteiro** sem o cabeçalho principal da app para mais espaço de ecrã
- **Numpad retrato e paisagem**: grelha 5x8 em retrato (PrtSc / ScrLk / Pause / Home / End), grelha 8x5 em paisagem com + alto, Enter e 00
- **Porta de envio ASCII-only IME**: escreve texto longo em modo compose, envia como pulsos HID limpos
- **Repetição com pressão longa**: mantém as teclas de caráter/função premidas para repetição automática (~400ms de atraso, ~50ms de repetição)
- **Pré-visualização de tecla**: bolha flutuante mostra o rótulo efetivo acima da tecla quando premida
- **Feedback háptico** e superfícies de teclas com **tema adaptável**

### Modificadores Sticky vs Chord

As definições permitem escolher entre **modificadores sticky** (tocar para fixar) e **momentâneo + chord com pressão longa** (predefinido) para o teclado Basic.

## Marca

- O nome de exibição da app é agora **KeyMod**
- O ecrã de boas-vindas mostra o logotipo **KeyMod**
- Os artefactos CI e nomes de ficheiros APK usam o prefixo **KeyMod**
- `applicationId` permanece **`com.openterface.keymod`** para atualizações in-place

## O que permanece inalterado

**Teclado e Rato Pro** (modo composto com barras Shortcut Hub, layouts divididos e comportamento IME rico) mantém a experiência completa de sempre.

## Obter a atualização

**Esta versão (0.15):** [KeyMod-release-0.15.apk](https://assets2.openterface.com/data/KeyMod-release-0.15.apk)

Também podes obter compilações em [GitHub Releases](https://github.com/TechxArtisanStudio/Openterface_KeyMod_Android/releases) ou [GitHub Actions](https://github.com/TechxArtisanStudio/Openterface_KeyMod_Android/actions). As instalações existentes atualizam in-place.

## Notas de atualização

- **Gamepad**: a tua preferência anterior de dois botões ativa automaticamente a predefinição **Two buttons** no primeiro início. Usa **Preset** (toca para percorrer, pressão longa para a lista) em vez do controlo antigo 1 Button / 2 Buttons.
- **Teclado e Rato (Basic)**: abre Basic para experimentar o teclado em ecrã inteiro. O modo Pro está disponível na gaveta de navegação para a experiência completa Shortcut Hub.

Cumprimentos,

Openterface Team | TechxArtisan
