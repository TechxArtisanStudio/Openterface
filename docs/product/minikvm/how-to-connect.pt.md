---
title: "Como conectar"
description: "Guia passo a passo para configurar Openterface Mini-KVM. Aprenda como conectar seu computador host e dispositivo alvo com instruções detalhadas para conexões USB-C, HDMI e periféricos. Inclui descrições de interface e dicas importantes de configuração."
keywords: "Configuração Mini-KVM, guia de conexão KVM, configuração KVM USB-C, conexão KVM HDMI, guia de instalação KVM, configuração de periféricos de computador, conexão de dispositivo USB, guia de interface KVM, configuração de computador headless, configuração KVM"
---

# **Como conectar** | Guia de configuração | Openterface Mini-KVM

## Configuração rápida

![to-host](https://assets.openterface.com/images/product/to-host.svg#only-light){:style="max-height:200px"} ![to-host](https://assets.openterface.com/images/product/to-host_1.svg#only-dark){:style="max-height:200px"}
![to-target](https://assets.openterface.com/images/product/to-target.svg#only-light){:style="max-height:200px"} ![to-target](https://assets.openterface.com/images/product/to-target_1.svg#only-dark){:style="max-height:200px"}

**Configuração em 4 passos simples:**

1. **Conexão host** (lado laranja): Conectar computador host usando cabo Type-C de 1,5m
2. **Conexão alvo** (lado preto): Conectar dispositivo alvo usando cabo Type-C de 0,3m
3. **Conexão de vídeo** (lado preto): Conectar saída de vídeo do alvo à porta HDMI
4. **Dispositivo USB** (opcional): Conectar à porta USB-A após completar os passos 1-3

!!! note "Requisitos" - **Host**: Requer [Openterface App](/app) instalada - **Alvo**: Nenhum app necessário - suporta Windows, macOS, Linux, Android, iOS - **Vídeo**: Usar cabo HDMI fornecido ou conversor VGA-to-HDMI

## Guia de portas

![host-side](https://assets.openterface.com/images/product/host-htc.svg#only-light){:style="max-width:300px"} ![target-side](https://assets.openterface.com/images/product/target-htc.svg#only-light){:style="max-width:300px"}
![host-side](https://assets.openterface.com/images/product/host-htc_1.svg#only-dark){:style="max-width:300px"} ![target-side](https://assets.openterface.com/images/product/target-htc_1.svg#only-dark){:style="max-width:300px"}

- ① **USB-C host**: Transferência de dados para o computador host
- ② **USB-C alvo**: Saída de controle de teclado/mouse
- ③ **Entrada HDMI**: Entrada de vídeo do dispositivo alvo
- ④ **Porta USB-A**: Comutável entre host/alvo

!!! warning "Notas importantes" - **Energia**: Dispositivos USB não devem exceder 1,5W de consumo - **Bloqueio USB-A**: Requer força extra para inserir/remover (evitar dispositivos pequenos) - **Hub USB**: Usar apenas hubs alimentados externamente; evitar árvores USB profundas - **Comutação**: Ver [Guia de comutação de porta USB](../usb-switch) para detalhes

⑤ ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t.svg#only-light){:style="max-height:20px"} ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t_1.svg#only-dark){:style="max-height:20px"} **Interruptor**: Comutar porta USB-A entre host/alvo

⑥ ![Extension Pins](https://assets.openterface.com/images/shell-icons/pins.svg#only-light){:style="max-height:15px"} ![Extension Pins](https://assets.openterface.com/images/shell-icons/pins_1.svg#only-dark){:style="max-height:15px"} **Pinos de extensão**: Acesso de desenvolvedor (ver [Pinos de extensão](../extension-pins))
