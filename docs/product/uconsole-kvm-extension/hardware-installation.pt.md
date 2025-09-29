---
title: "Instalação de hardware"
description: "Guia passo a passo de instalação de hardware para Openterface KVM Extension for uConsole. Aprenda como instalar corretamente a placa de extensão no slot de expansão do seu uConsole com diretrizes de segurança detalhadas."
keywords: "instalação extensão KVM, configuração hardware uConsole, instalação placa expansão, slot expansão uConsole, guia hardware KVM, instalação física"
---

# **Instalação de hardware** | Openterface KVM Extension for uConsole

## Visão geral
A Extensão KVM substitui o módulo 4G/LTE no slot de expansão do uConsole, adicionando entrada HDMI direta e controle USB HID.

## O que você precisa
- Verifique o seu [Conteúdo da embalagem](whats-in-the-box.md) antes da instalação  
- Placa Openterface KVM Extension  
- **Arruelas** fornecidas (para garantir montagem estável e pressão uniforme)  
- Chave de fenda hexagonal (para parafusos de montagem)  
- Proteção ESD (pulseira ou superfície aterrada) — recomendado  

## Passos de instalação

### **1. Desligar**
Desligue o uConsole e desconecte toda alimentação e cabos.

### **2. Remover módulo existente**
Use uma chave de fenda hexagonal para remover os dois parafusos.  
Levante a placa **direto para cima** para evitar dobrar os contatos de mola.

### **3. Instalar a Extensão KVM**
- Coloque a **arruela** no poste do parafuso.  
- Assente firmemente a Extensão KVM no slot de expansão.  
- A arruela compensa o PCB ligeiramente mais fino (1,0 mm vs 1,2 mm), mantendo pressão de contato de mola apropriada.

??? note "Verificar ajuste antes da instalação final"
    Você pode primeiro assentar a placa **sem a arruela** para testar o ajuste. Se a placa parecer solta ou os contatos forem desiguais, adicione a arruela e reassente a placa. A Openterface KVM Extension tem 1,0 mm de espessura, ligeiramente mais fina que o módulo LTE original (1,2 mm). Usar a arruela fornecida garante montagem estável e contato de mola confiável.  
    ![extension-slot-loose](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-slot-loose.webp){:style="max-height:220px"}

### **4. Fixar a placa**
Reinsira os parafusos e aperte **suavemente** — **não aperte demais**, pois isso pode danificar a placa ou desgastar as roscas.

![extension-screw-washer-installed](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installed.jpg){:style="max-height:220px"}
![extension-screw-washer-installing](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installing.jpg){:style="max-height:220px"}
![extension-install-1](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp){:style="max-height:220px"}

### **5. Verificar instalação**
A placa deve ficar **plana e estável**, com contato de mola uniforme em todos os pads. Não deve haver movimento ou balanço notável.

### **6. Instalar tampa do slot de expansão**
Reinstale a tampa do slot de expansão para proteger a placa Extensão KVM e manter a aparência original do uConsole.

??? note "Orientação do texto na tampa do slot de expansão"
    O texto na tampa do slot de expansão pode aparecer "de cabeça para baixo" quando visto de certos ângulos. Este é um design intencional - o texto está orientado para ser legível quando você segura o uConsole e olha as portas de cima para baixo, que é a posição de visualização natural ao usar o dispositivo.
    ![expansion-slot-text-orientation](https://assets.openterface.com/images/product/openterface-kvm-uconsole-expansion-slot-text-orientation.webp){:style="max-height:220px"}

---

**Próximos passos**

1. Vá para [Configuração de software](/product/uconsole-kvm-extension/software-setup/) para instalar o App Openterface.  
2. Vá para [Conectar ao dispositivo alvo](/product/uconsole-kvm-extension/connect-to-target/) para conectar seu dispositivo alvo.  
3. Revise [Recursos e especificações](/product/uconsole-kvm-extension/features/) para especificações técnicas detalhadas.
