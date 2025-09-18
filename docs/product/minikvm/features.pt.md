---
title: "Funcionalidades e Especificações"
description: "Visão geral completa do Openterface Mini-KVM: funcionalidades poderosas incluindo acesso a nível BIOS, suporte de vídeo 4K, compatibilidade multiplataforma, compartilhamento USB e especificações técnicas detalhadas. Tudo que você precisa saber sobre esta solução de controle de computador headless."
keywords: "funcionalidades Mini-KVM, especificações KVM, acesso BIOS, controle headless, KVM 4K, compartilhamento USB, KVM multiplataforma, transferência de texto, KVM plug and play, KVM open source, especificações técnicas"
---

# **Funcionalidades e Especificações** | Openterface Mini-KVM

<iframe 
  width="560" 
  height="315" 
  src="https://www.youtube.com/embed/r3HNUflWGOY?si=84Ek6F9ocHmmGTqW" 
  title="YouTube video player" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
  referrerpolicy="strict-origin-when-cross-origin" 
  allowfullscreen>
</iframe>

## Funcionalidades Principais

### **Acesso a Nível BIOS**

Acesso direto ao BIOS do dispositivo alvo, firmware e gerenciamento de inicialização sem dependências de rede.

### **Independência de Rede**

Controle headless estável usando captura de vídeo HDMI e entrada de teclado/mouse emulada (HID). Nenhuma conexão de rede necessária.

### **Vídeo de Alta Performance**

- **Entrada**: Até 4K (3840×2160) @ 30Hz via HDMI
- **Saída**: Full HD (1920×1080) @ 30Hz com latência inferior a 140ms
- **Compressão**: Suporte YUV e MJPEG
- **Compatibilidade**: VGA, DVI, Micro HDMI via adaptadores

### **Porta USB Comutável**

Alternar acesso USB entre dispositivos host e alvo para compartilhamento seamless de unidades USB. Saiba mais na página [Porta USB Comutável](../usb-switch).

### **Suporte Multiplataforma**

[Apps host](/app) compatíveis com macOS, Windows, Linux e Android para integração universal.

### **Transferência de Texto**

Transmitir texto sem esforço simulando pressionamentos de teclas—perfeito para nomes de usuário, senhas e fragmentos de código. Suporta caracteres ASCII incluindo símbolos e pontuação.

!!! warning "Limitações da Transferência de Texto" - **Sem Integração de Área de Transferência**: Apenas emula digitação, sem transferência de imagens ou documentos - **Apenas ASCII**: Limitado a caracteres ASCII (sem suporte para chinês, japonês, coreano) - **Considerações de Comprimento**: Melhor para texto curto; blocos grandes podem causar problemas de performance

### **Conveniência Plug-and-Play**

Nenhuma instalação de software necessária no dispositivo alvo. O controle começa imediatamente na conexão sem deixar rastros de software.

### **Integração de Áudio**

Pass-through de áudio integrado HDMI para experiência multimídia completa.

### **Pinos de Extensão**

[Pinos de extensão](../extension-pins) habilitam desenvolvimento avançado e personalização para necessidades específicas.

### **Open-Source**

Hardware e software [completamente open-source](/compliance) para transparência e [inovação da comunidade](/discord).

## Especificações Técnicas

### **Dimensões Físicas**

- **Tamanho**: 61 × 53 × 13.5 mm (2.40 × 2.09 × 0.53 polegadas)
- **Peso**: ~48g
- **Material**: Liga de alumínio, carcaça PLA

### **Conectividade e Energia**

- **Energia**: Alimentado por USB-C (nenhuma fonte externa necessária)
- **Velocidade USB**: Transmissão de velocidade completa 12Mbps
- **Compatibilidade Host**: Windows, macOS, Linux, Android
- **Alvo**: Nenhuma instalação de software necessária

### **Vídeo e Áudio**

- **Entrada Máx**: 3840×2160@30Hz (HDMI)
- **Saída Máx**: 1920×1080@30Hz
- **Latência**: Inferior a 140ms
- **Áudio**: Pass-through de áudio integrado HDMI

### **Funcionalidades de Entrada**

- Emulação completa de teclado e mouse (absoluta e relativa)
- Suporte de teclas multimídia
- Funcionalidade HID personalizada
- Função de despertar computador

### **Ambiental**

- **Operação**: 0°C a 40°C
- **Armazenamento**: -10°C a 50°C
- **Umidade**: 80% RH

## Modelos de Produto

- **Basic**: OP-MINIKVM-BASIC
- **Toolkit**: OP-MINIKVM-TOOLKIT

## Downloads de Documentação

- **[Guia de Início Rápido](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/minikvm_quick_start_guide_20240928.pdf)** (PDF)
- **[Folha de Dados (Inglês)](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/Openterface-Mini-KVM-Basic-and-Toolkit-Datasheet-Eng-20250313.pdf)** (PDF)

![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front.svg#only-light){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back.svg#only-light){:style="max-height:260px"}
![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front_1.svg#only-dark){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back_1.svg#only-dark){:style="max-height:260px"}
