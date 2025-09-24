---
title: "Recursos e especificações"
description: "Visão geral completa do Openterface KVM Extension for uConsole: recursos poderosos incluindo entrada HDMI direta, controle USB HID, fator de forma perfeito e especificações técnicas detalhadas. Tudo que você precisa saber sobre esta solução KVM portátil."
keywords: "recursos extensão KVM, uConsole KVM, HDMI KVM, controle USB HID, KVM portátil, controle headless, substituição 4G LTE, especificações técnicas, expansão uConsole"
---

# **Recursos e especificações** | Openterface KVM Extension for uConsole

![PCB-front](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:320px"}
![PCB-Back](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:320px"}

## Recursos principais

- **HDMI direto + USB HID**: Aproveite a tela e controles integrados do uConsole com entrada HDMI direta e emulação USB HID.
- **Plug-and-Play**: Controle instantâneo sem instalação de software ou vestígios residuais no dispositivo alvo.
- **Baixa latência**: Otimizado para solução de problemas em nível BIOS e interações em tempo real.
- **Portátil**: Ferramenta móvel tudo-em-um—não precisa de monitores extras, teclados ou configuração de rede.
- **Sem rede**: Controle headless estável via captura HDMI e entrada HID, nenhuma rede necessária.
- **Transferência de texto**: Transfira rapidamente texto simulando pressionamentos de teclas—ideal para nomes de usuário, senhas e trechos de código. Suporta ASCII completo, incluindo símbolos e pontuação. [Verifique nosso app](/app) para detalhes.
- **Código aberto**: Construído sobre [Openterface KVM QT](https://github.com/techxArtisanStudio/openterface_qt) com suporte ativo da comunidade.

## Especificações técnicas

### Dimensões físicas

- **Tamanho:** 37 × 77 mm (corresponde ao módulo 4G/LTE)
- **Espessura:** 1,0 mm (mais fino que o módulo 4G/LTE original de 1,2 mm)
- **Material:** PCB de alta qualidade com contatos de mola

### Emulação completa de teclado e mouse

- **USB HID:** Posicionamento absoluto e relativo do mouse, suporte completo de teclado, teclas multimídia.
- **Conexão:** Link USB para o alvo via porta fêmea Type-C da placa de extensão.

### Vídeo e áudio

- **Entrada:** Até 4K (3840×2160) @ 30Hz via HDMI
- **Saída:** Full HD (1920×1080) @ 30Hz com latência inferior a 140ms
- **Display:** Usa a tela integrada do uConsole
- **Compressão:** Suporte YUV e MJPEG
- **Compatibilidade:** VGA, DVI, Micro HDMI (via adaptadores)
- **Áudio:** Pass-through de áudio embutido HDMI

### Porta USB 2.0 comutável

- **Porta compartilhada:** Mude facilmente o acesso USB entre uConsole e dispositivo alvo (ex. drives flash) usando o app host.
- **Velocidade USB:** Transmissão em velocidade completa de 12Mbps

### Conectividade e energia

- **Energia:** Obtém energia diretamente do slot de expansão do uConsole (nenhuma fonte externa necessária)
- **Compatibilidade alvo:** Windows, macOS, Linux, Android, iOS
- **Software alvo:** Nenhuma instalação necessária
