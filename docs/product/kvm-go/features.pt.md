---
title: "Recursos e especificações"
description: "Visão geral completa da série Openterface KVM-Go: design ultra-compacto com conectores de vídeo integrados, suporte 4K/60Hz, slot MicroSD e especificações técnicas detalhadas. Solução KVM-over-USB do tamanho de um chaveiro para profissionais de TI."
keywords: "recursos KVM-Go, KVM ultra-compacto, HDMI integrado, KVM 4K, KVM MicroSD, KVM chaveiro, especificações KVM, controle headless, KVM portátil, ferramentas de TI, gerenciamento de servidores"
---

# **Recursos e especificações** | Série Openterface KVM-Go

## Status pré-lançamento

A série KVM-Go está atualmente em desenvolvimento pré-lançamento. Estamos refinando os designs de PCB e caixa. Junte-se à nossa [lista de espera]({{ config.extra.kvmgo_purchase_link }}) para se manter atualizado sobre o progresso e obter acesso antecipado.

> **Nota:** Recursos, especificações e design ainda estão sujeitos a alterações conforme o desenvolvimento continua.

## Modelos de produtos
- **KVM-Go HDMI Male** — Conexão HDMI direta
- **KVM-Go DisplayPort Male** — DisplayPort de alto desempenho
- **KVM-Go VGA Male** — Suporte a sistemas legados (em desenvolvimento)

## Recursos principais

### **Design ultra-compacto**
Formato do tamanho de um chaveiro que cabe no seu bolso. Chega de carregar dispositivos KVM volumosos ou procurar cabos de vídeo.

### **Conectores de vídeo integrados**
Capacidade de conexão direta com conectores macho integrados:

- **HDMI Male** — Compatibilidade com dispositivos modernos
- **DisplayPort Male** — Suporte de alto desempenho
- **VGA Male** — Suporte a sistemas legados (em breve)

### **Acesso ao nível do BIOS**
Acesso direto ao BIOS, firmware e gerenciamento de inicialização do dispositivo de destino sem dependências de rede.

### **Independência de rede e resposta ultrarrápida**
Controle headless estável usando captura de vídeo integrada e entrada de teclado/mouse emulado (HID). Nenhuma conexão de rede necessária. O tempo de inicialização do hardware é inferior a 1 segundo, garantindo solução de problemas imediata sem atrasos no fluxo de trabalho.

### **Desempenho de vídeo aprimorado**
Atualização massiva em relação aos 1080p@30Hz do Mini-KVM:

- **Entrada**: 4096×2160 @ 60 Hz (YUV420), 4096×2160 @ 30 Hz (YUV444)
- **Saída**: 4096×2160 @ 60 Hz (MJPEG), 3840×2160 @ 30 Hz (YUV420)
- **Padrão**: 1080p@60Hz para estabilidade e desempenho ideais
- **Modo 4K**: Disponível como recurso experimental*
- **Compressão**: Suporte YUV420, YUV444 e MJPEG

*Nota: O modo 4K gera calor adicional; a superfície do dispositivo pode ficar bastante quente durante operação prolongada

### **Slot MicroSD**
Transferência de arquivos entre dispositivos host e de destino

### **Suporte multiplataforma**
[Aplicativos host](/app) compatíveis com macOS, Windows, Linux, Android e aplicativo web Chrome para integração universal.

### **Transferência de texto**
Transmita texto sem esforço simulando pressionamentos de teclas — perfeito para nomes de usuário, senhas e trechos de código. Suporta caracteres ASCII incluindo símbolos e pontuação.

- **Host → Destino**: Enviar texto via pressionamentos de teclas emulados
- **Destino → Host**: Copiar texto da tela do destino para o host via OCR (somente macOS)

!!! warning "Limitações de transferência de texto"
    - **Sem integração de área de transferência**: Apenas emula digitação, sem transferência de imagens ou documentos
    - **Apenas ASCII**: Limitado a caracteres ASCII (sem suporte para chinês, japonês, coreano, etc.)
    - **Considerações de comprimento**: Melhor para textos curtos; blocos grandes podem causar problemas de desempenho
    - **Recurso OCR**: Transferência de texto Destino → Host atualmente disponível apenas no macOS

### **Conveniência plug-and-play**
Nenhuma instalação de software necessária no dispositivo de destino. O controle começa imediatamente após a conexão sem deixar vestígios de software.

### **Integração de áudio**
Passagem de áudio HDMI incorporado para experiência multimídia completa. (Não suportado no KVM-Go VGA; confirmação pendente para KVM-Go DP.)

### **Capacidade Bluetooth**
O suporte Bluetooth integrado habilita a funcionalidade do aplicativo nativo do iPadOS (em breve), tornando o KVM-GO um dos poucos KVMs que funcionam nativamente com iPads.

### **Código aberto**
Hardware e software [totalmente de código aberto](/compliance) para transparência e [inovação da comunidade](/discord).

## Especificações técnicas

### **Dimensões físicas** *(sujeitas a alterações antes da entrega)*
- **Tamanho**: 18 × 18 × 55 mm (0,71 × 0,71 × 2,17 polegadas)
- **Peso**: ~25 g (0,9 oz)
- **Material**: Caixa de liga de alumínio com tampas impressas em 3D

### **Conectividade e energia**
- **Energia**: Alimentado por USB-C (sem necessidade de fonte externa)
- **Velocidade USB**: USB 3.0 para versões HDMI/DP; USB 2.0 para versão VGA
- **Compatibilidade host**: Windows, macOS, Linux, Android, Chrome
- **Destino**: Nenhuma instalação de software necessária

### **Vídeo e áudio**
- **Entrada máx.**: 4096×2160@60Hz (YUV420), 4096×2160@30Hz (YUV444)
- **Saída máx.**: 4096×2160@60Hz (MJPEG), 3840×2160@30Hz (YUV420)
- **Áudio**: Passagem de áudio HDMI incorporado

### **Recursos de entrada**
- Emulação completa de teclado e mouse (absoluta e relativa)
- Suporte a teclas multimídia
- Funcionalidade HID personalizada
- Função de despertar o computador

### **Armazenamento**
- **Slot MicroSD**: Transferências de arquivos via MicroSD entre host e destino

