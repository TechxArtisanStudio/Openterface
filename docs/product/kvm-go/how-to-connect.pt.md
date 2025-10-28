---
title: "Como conectar"
description: "Guia passo a passo para configurar o Openterface KVM-Go. Aprenda a conectar seu computador host e dispositivo de destino usando conectores de vídeo integrados para uma experiência de conexão direta ultra-simples."
keywords: "configuração KVM-Go, configuração KVM ultra-compacto, conexão HDMI integrada, guia instalação KVM, configuração KVM chaveiro, conexão USB KVM, configuração computador headless, configuração KVM portátil"
---

# **Como conectar** | Guia de configuração | Openterface KVM-Go

## **Visão geral das conexões**

![Visão geral das conexões KVM-Go](https://assets.openterface.com/images/kvm-go/step-0-overview.webp){:style="max-height:360px"}

As imagens acima mostram todas as conexões entre o [**KVM-Go**](/product/kvm-go), o computador host e o dispositivo de destino.

- **Computador host**: Requer a instalação do [aplicativo Openterface](/app).  
- **Dispositivo de destino**: Nenhum software ou pré-configuração necessária.
- **Vídeo**: O conector integrado conecta-se diretamente ao dispositivo de destino, então você não precisa carregar ou gerenciar cabos de vídeo extras.

## **O que você precisa para as conexões**

![KVM-Go todas as peças](https://assets.openterface.com/images/kvm-go/step-0-all-parts.webp){:style="max-height:360px"}

Para configurar seu **KVM-Go**, você precisará dos seguintes componentes:

- **KVM-Go (HDMI / DP / VGA)** — conecta-se ao **dispositivo de destino** (para captura de vídeo)  
- **Cabo USB-C curto preto** — conecta-se ao **dispositivo de destino** (para emulação de teclado e mouse)
- **Cabo USB-C longo laranja** — conecta-se ao **computador host** (executando o [aplicativo Openterface](/app))

!!! note "Aviso sobre comprimento dos cabos"
    Os comprimentos exatos dos cabos incluídos no **pacote oficial KVM-Go** **ainda não foram finalizados** e podem diferir ligeiramente daqueles mostrados aqui.  
    Os cabos demonstrados neste guia são do *kit clássico Mini-KVM* e são apenas para fins ilustrativos.

!!! warning "Uso de seus próprios cabos"
    Se você optar por usar seus próprios cabos, certifique-se de que sejam **cabos USB de alta qualidade capazes de transferir dados**. Cabos de má qualidade ou apenas para carga podem resultar em:
    
    - Problemas de tela preta
    - Entradas de teclado ou mouse sem resposta
    - Quedas de conexão intermitentes
    - Saída de vídeo instável ou tremulante

## **Configuração passo a passo**

### **Passo 1 — Conectar os cabos USB ao KVM-Go**
![Conectando cabos USB](https://assets.openterface.com/images/kvm-go/step-1-plugged.webp){:style="max-height:360px"}

- **Cabo USB-C preto** → Conectar à porta rotulada ![Ícone destino](https://assets.openterface.com/images/shell-icons/target-computer.svg#only-light){:style="max-height:20px"} ![Ícone destino](https://assets.openterface.com/images/shell-icons/target-computer_1.svg#only-dark){:style="max-height:20px"} **Target** na caixa do KVM-Go.  
- **Cabo USB-C laranja** → Conectar à porta rotulada ![Ícone host](https://assets.openterface.com/images/shell-icons/host-computer.svg#only-light){:style="max-height:20px"} ![Ícone host](https://assets.openterface.com/images/shell-icons/host-computer_1.svg#only-dark){:style="max-height:20px"} **Host**.

!!! warning
    Ambas as portas USB-C são fisicamente idênticas.  
    Sempre **verifique os rótulos** na superfície da caixa para evitar confundi-los.

### **Passo 2 — Conectar vídeo ao destino**
![Conectando conector HDMI](https://assets.openterface.com/images/kvm-go/step-3-hdmi-plugged.webp){:style="max-height:360px"}

Conecte o **conector de vídeo macho integrado** diretamente à porta de saída de vídeo do dispositivo de destino.

### **Passo 3 — Conectar a porta USB de destino**
Conecte o **cabo USB preto** ao dispositivo de destino para controle HID.

- **Opção A:** Diretamente em uma porta USB-A  
  ![Destino USB-A](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-b.webp){:style="max-height:360px"}

- **Opção B:** Usando um adaptador USB-C  
  ![Destino USB-C](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-a.webp){:style="max-height:360px"}

!!! note "Verificação de conexão USB-C"
    Algumas portas USB-C podem não fornecer uma conexão segura. Se você experimentar problemas intermitentes de controle de teclado/mouse, balance suavemente a conexão do adaptador para garantir que esteja devidamente encaixado e fazendo contato.


### **Passo 4 — Conectar a porta USB host**
Conecte o **cabo USB laranja** ao computador host.

- Diretamente a uma porta USB-C **OU** através de um adaptador USB-C para USB-A.  
  ![Conectando USB host](https://assets.openterface.com/images/kvm-go/step-5-plug-in-host-computer-1.webp){:style="max-height:360px"}

