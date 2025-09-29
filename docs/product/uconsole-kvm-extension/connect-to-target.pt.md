---
title: "Conectar ao Dispositivo Alvo"
description: "Aprenda como conectar seu dispositivo alvo à Openterface KVM Extension for uConsole. Guia completo para configuração de controle USB e entrada de vídeo após instalação de hardware e configuração de software."
keywords: "configuração conexão KVM, conexão dispositivo alvo, configuração controle USB, configuração entrada HDMI, conexão extensão KVM uConsole"
---

# **Conectar ao Dispositivo Alvo** | Openterface KVM Extension for uConsole

## Visão Geral da Conexão

![extension-use-case-1a](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1a.webp){:style="max-height:480px"}

## Pré-requisitos

Antes de conectar seu dispositivo alvo, certifique-se de ter completado:

1. [Instalação de Hardware](/product/uconsole-kvm-extension/hardware-installation/) - Instalação física da placa Extension KVM
2. [Configuração de Software](/product/uconsole-kvm-extension/software-setup/) - Instalação do App Openterface

## Passos de Conexão

### **Controle USB**
Conecte a porta fêmea Type-C à porta USB do dispositivo alvo para emular sinais de teclado e mouse.

### **Entrada de Vídeo**
Conecte a saída de vídeo do dispositivo alvo à porta HDMI na Extension KVM:

- Use cabo HDMI padrão para dispositivos com saída HDMI
- Use cabo conversor VGA-to-HDMI para dispositivos com saída VGA.
    - *Nota*: Certifique-se de que o conversor esteja alimentado através de seu conector USB para funcionamento adequado.
- Use outros adaptadores apropriados para diferentes tipos de sinais de vídeo

## Testar a Conexão

1. Ligue a alimentação e inicialize o uConsole
2. Execute o app Openterface QT
3. Teste as funcionalidades HDMI, áudio e USB HID para confirmar o funcionamento adequado
