---
draft: false
date: 2026-05-21
title: "Atualização KVM-GO: controle o seu dispositivo alvo pelo celular com o KeyCmd 0.19"
description: "Use o KeyCmd 0.19 com o KVM-GO via USB ou Bluetooth: teclados KM Basic e Pro, modo Compose, predefinições de gamepad, Shortcut Hub e controles de apresentação—sem necessidade de dongle de vídeo para entrada HID."
keywords: "KVM-GO KeyCmd, KeyCmd 0.19, aplicativo KVM-GO Android, controle de celular KVM-over-USB, Openterface KeyCmd, teclado virtual KVM, KVM-GO Bluetooth USB, modo KM Pro Compose, KVM-GO HDMI DP VGA, aplicativo Openterface KVM, entrada KVM portátil"
author: "Openterface Team | TechxArtisan"
category: "Atualizações de Produto"
tags: ["KVM-GO", "KeyCmd", "Atualizações de Produto", "Android", "USB", "Bluetooth", "Teclado", "Gamepad", "Lançamento"]
featured: false
social:
  image: "https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp"
  title: "KVM-GO + KeyCmd 0.19 — controle o seu dispositivo alvo pelo seu celular"
  description: "O KeyCmd 0.19 emparelha com o KVM-GO via USB ou Bluetooth para teclado, mouse, gamepad, atalhos e Compose—enquanto o Openterface KVM cuida do vídeo quando você precisar."
---

# Atualização KVM-GO: controle o seu dispositivo alvo pelo celular com o KeyCmd 0.19

Olá a todos,

Obrigado por apoiar o **KVM-GO** e pela sua paciência enquanto as unidades passam pela produção e envio. Sabemos que muitos de vocês ainda estão aguardando o hardware, e queremos que sua configuração pareça completa desde o primeiro dia.

Junto com o aplicativo **Openterface KVM** (vídeo e controle KVM total no seu celular ou tablet), temos aprimorado o **KeyCmd**, nosso aplicativo complementar para entrada de teclado, mouse, gamepad e atalhos. O **KeyCmd 0.19** é a versão que recomendamos hoje se você usa o KVM-GO. Emparelhe via **USB** ou **Bluetooth**, instale sobre qualquer versão anterior e suas configurações, perfis e dispositivos emparelhados serão mantidos.

![KVM-GO em um laptop com teclado KeyCmd em um celular](https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp){:style="max-width:720px;width:100%;height:auto"}

Abaixo, detalhamos o que o KeyCmd faz com o KVM-GO, qual modo abrir para cada tarefa e como aproveitá-lo ao máximo em uma máquina alvo real.

![Tela de boas-vindas do KeyCmd](https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape_1.webp){:style="max-height:320px;width:auto"}

## Modos e como usá-los

### Teclado e Mouse (Basic)

Abra este modo quando desejar um **teclado simples em tela cheia** e nada mais atrapalhando.

**Ideal para:** senhas de BIOS, comandos curtos de shell, entrada de teclado numérico ou controle de mouse com um touchpad grande enquanto o KVM-GO mostra a tela.

**Como usar:**

- Abra o **KM Basic** no menu de navegação.
- Use o teclado na tela, o **teclado numérico** (retrato ou paisagem) ou a aba **touchpad**, conforme necessário.
- Em **Configurações**, escolha **teclas modificadoras fixas** (toque para travar Shift/Ctrl) ou modificadores **estilo acorde** se preferir combinações de segurar e tocar.

**Por que ajuda:** mais espaço na tela para as teclas, menos interface, mais rápido quando você precisa apenas de entrada e não de atalhos.

![Teclado de tela cheia KM Basic](https://assets2.openterface.com/images/keymod/KM-Basic-Keyboard_1.webp){:style="max-height:320px;width:auto"}

![Teclado numérico KeyCmd em paisagem](https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape_1.webp){:style="max-height:320px;width:auto"}

### Teclado e Mouse (Pro)

![Teclado dividido KM Pro em paisagem](https://assets2.openterface.com/images/keymod/KM-Pro-Keyboard-landscape-split_1.webp){:style="max-height:320px;width:auto"}

![Teclado e touchpad KeyCmd em retrato](https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait_1.webp){:style="max-height:320px;width:auto"}

Abra este modo para **trabalho de controle diário** em máquinas conectadas ao KVM-GO: teclados divididos, IME, barras do Shortcut Hub e o editor **Compose**.

**Ideal para:** sessões de digitação mais longas, macros e atalhos, envio de blocos de texto ou scripts para o host enquanto você observa o resultado na visualização KVM.

![Modo Compose enviando um script](https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait_1.webp){:style="max-height:320px;width:auto"}

Vale a pena experimentar o **Compose** se você costuma colar comandos ou scripts: escreva no seu celular, revise e envie como toques de tecla para o host. Uma [curta demonstração no YouTube](https://www.youtube.com/watch?v=_rJF-hTF3_E) mostra o fluxo de ponta a ponta.

**Como usar:**

- Abra o **KM Pro** no menu de navegação.
- Use o teclado e o touchpad como no modo Basic, além das categorias do **Shortcut Hub** no topo para ações de um toque configuradas nos perfis.
- Abra o **Compose** para rascunhar textos mais longos no seu celular, revise-os e clique em **enviar** como teclas HID. Envios longos mostram uma barra de progresso. Se o seu texto tiver caracteres não ASCII, o aplicativo avisará antes do envio para que você possa verificar a compatibilidade do host (especialmente útil no macOS).

**Por que ajuda:** um único lugar para digitar, apontar, usar atalhos e fluxos de trabalho tipo "colar" sem carregar um teclado físico até o alvo.

### Gamepad

Abra este modo quando desejar um layout de **controle virtual** na tela, ajustado para jogos ou qualquer aplicativo no alvo que espere um gamepad.

**Ideal para:** emuladores, jogos casuais ou uma superfície de controle compacta com sticks e botões enquanto o KVM-GO gerencia a tela.

**Como usar:**

- Mude para o modo **Gamepad**.
- Toque em **Preset** na barra de ferramentas para **alternar** entre os layouts salvos. **Pressione e segure Preset** para abrir a lista completa, **importar/exportar** ou **adicionar módulos** (sticks, botões, touchpads).
- Comece pela predefinição **emu-6** inclusa e edite a partir daí. Você pode adicionar **vários touchpads** e módulos de stick extras em um único layout.

**Por que ajuda:** você não fica preso a um único layout de fábrica; salve layouts por jogo ou por máquina e compartilhe predefinições com outras pessoas.

![Layout de predefinição de Gamepad](https://assets2.openterface.com/images/keymod/Gamepad-perset-1_1.webp){:style="max-height:320px;width:auto"}

![Predefinição de Gamepad usada no Minecraft](https://assets2.openterface.com/images/keymod/Gamepad-perset-minecraft_1.webp){:style="max-height:320px;width:auto"}

*Predefinição personalizada para Minecraft.*

### Shortcut Hub

Este é o centro de **perfis e atalhos** dentro do KM Pro: categorias, painéis de detalhes e os atalhos que você atribui às barras.

**Ideal para:** operações repetitivas no alvo (abrir terminal, colar uma cadeia de comandos, alternar configurações) enquanto o KVM-GO permanece conectado para vídeo.

**Como usar:**

- No KM Pro, trabalhe no perfil **Default** (ou no seu próprio).
- Use as abas de categorias e a interface de detalhes para gerenciar atalhos.
- Siga o **guia do Shortcut Hub** se você for novo na organização de perfis.

### Apresentação

Uma superfície de controle mais simples no estilo **apresentador**, mantida em **retrato** para que os botões não pulem quando você girar o celular.

**Ideal para:** passar slides ou controles leves de apresentação no alvo.

![Modo Apresentação controlando o Google Slides](https://assets2.openterface.com/images/keymod/KeyCmd-Presentation-Google-Slides.webp){:style="max-height:320px;width:auto"}

---

## Idiomas

A interface do aplicativo está disponível em **11 idiomas**. Adições recentes: coreano, italiano, russo e português brasileiro.

Abra **Settings** → **App language** para trocar.

---

## Obtenha o KeyCmd 0.19 e conecte ao KVM-GO

**Download:** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

Instale sobre o seu aplicativo existente se você já tiver um. Não é necessário apagar os dados.

**Conecte ao KVM-GO (a porta de vídeo pode ficar desconectada):**

Para **todas as três variantes do KVM-GO** (HDMI, VGA e DP), você não precisa conectar o **conector de vídeo do dongle** em nada para a entrada do KeyCmd. A porta HDMI, VGA ou DP pode ficar vazia. Escolha uma das configurações abaixo.

**Opção A — Bluetooth (o alvo alimenta o KVM-GO)**

1. Conecte o **cabo USB preto curto** na porta **Target** do KVM-GO e na máquina que você está controlando. Essa conexão sozinha **alimenta** o KVM-GO.
2. No seu celular, abra o **KeyCmd** e localize o KVM-GO via **Bluetooth**.

**Opção B — USB para o seu celular Android (porta Host)**

1. Conecte o **cabo laranja longo** da porta **Host** do KVM-GO ao seu celular Android.
2. Abra o **KeyCmd** e conecte via **USB** no aplicativo.

![Porta Target do KVM-GO conectada a um laptop via o cabo USB preto curto](https://assets2.openterface.com/images/kvm-go/kvm-go-target-port-laptop-power.webp){:style="max-height:360px;width:auto"}

Para vídeo em tela cheia e entrada, use o **Openterface KVM** para a tela do alvo e o **KeyCmd** para teclado, mouse e atalhos. O KeyCmd sozinho é suficiente quando o alvo já possui sua própria tela e você só precisa de entrada.

**Também funciona com Mini-KVM** via USB se você usar ambos os dispositivos.

> **Ainda em beta.** As predefinições de gamepad e os envios do Compose podem se comportar de forma diferente dependendo do SO do host. Se algo estranho acontecer com o KVM-GO, entre em contato conosco no **Discord** com uma captura de tela, sua variante do KVM-GO (HDMI / DP / VGA) e o que você esperava.

> **Código fonte:** Ainda não é público. Planejamos abrir o código após os marcos de financiamento coletivo em projetos relacionados. Pergunte no Discord se precisar de ajuda para encontrar o APK.

---

## Sobre o KeyMod (opcional, separado do KVM-GO)

Também estamos desenvolvendo o **[KeyMod](https://openterface.com/product/keymod/)**, um dongle HID dedicado USB e Bluetooth para o mesmo aplicativo KeyCmd. Os apoiadores do KVM-GO não precisam do KeyMod para os fluxos de trabalho acima; o KeyCmd sobre o KVM-GO é o caminho que queremos que você siga agora.

Se você tiver curiosidade sobre um dongle independente para configurações não KVM, pode acompanhar a [campanha do KeyMod no Crowd Supply](https://www.crowdsupply.com/techxartisan/openterface-keymod). Isso é independente da entrega do KVM-GO.

---

## Gostaríamos muito do seu feedback

Se você tiver alguns minutos, instale o **KeyCmd 0.19**, conecte-o ao seu KVM-GO (ou Mini-KVM) e conte-nos o que ainda parece estranho. Relatos de casos de uso em campo ("crash-cart") e laboratórios domésticos (homelab) vão direto para nossos próximos lançamentos.

Formas práticas de ajudar o projeto KVM-GO:

- **Compartilhe o que funciona** no Discord ou na sua comunidade (dicas de BIOS, emparelhamento Bluetooth, modos favoritos)
- **Conte para um colega** que gerencia equipamentos headless e poderia usar um KVM de bolso
- **Continue enviando feedback honesto**, especialmente os pontos a melhorar. Isso molda o produto mais do que elogios

Obrigado novamente por apoiar o KVM-GO e por nos ajudar a tornar o KVM-over-USB portátil melhor para todos.

Atenciosamente,

**Equipe Openterface | TechxArtisan**
