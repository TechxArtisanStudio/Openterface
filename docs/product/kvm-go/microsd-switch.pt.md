---
title: "Guia de comutação de cartão MicroSD"
description: "Aprenda a usar o sistema de comutação MicroSD dual hardware-software no Openterface KVM-Go. Compreenda os quatro estados operacionais, indicadores LED, diretrizes de segurança e capacidades de transferência de arquivos."
keywords: "comutação MicroSD, switch KVM, switch hardware, switch software, controle cartão MicroSD, KVM over USB, transferência de arquivos, gerenciamento dispositivos USB, periféricos computador, gerenciamento energia MicroSD, indicadores LED"
---

# **Guia de comutação de cartão MicroSD** | Openterface KVM-Go

O **Openterface KVM-Go** inclui um único slot de cartão MicroSD que pode ser compartilhado entre o computador host e o dispositivo de destino, mas nunca ambos ao mesmo tempo.

Este design permite que você alterne rapidamente entre dispositivos para **transferência de arquivos**, sem remover fisicamente o cartão, tornando seu fluxo de trabalho mais rápido e eficiente. Também pode servir simplesmente como seu **leitor de cartão MicroSD regular**.

## **Instalar o cartão MicroSD**

![kvm-go-install-sd](https://assets.openterface.com/images/kvm-go/install-sd.webp){:style="max-height:260px;width:auto"}

!!! note "Instalação correta do cartão MicroSD"
    Insira firmemente o cartão MicroSD até sentir um **clique**, indicando que está seguramente assentado e travado no lugar.

## **Métodos de controle**

KVM-Go fornece duas maneiras de alternar o cartão MicroSD entre host e destino:

- **Botão de hardware** — Um botão físico no dispositivo para controle manual.  
- **Switch de software** — Um botão de alternância dentro do aplicativo host para comutação instantânea.


## **Botão de comutação e indicadores LED** 

![kvm-go-led-indicator](https://assets.openterface.com/images/kvm-go/led-indicator.webp){:style="max-height:260px;width:auto"}

Os **indicadores LED de dupla cor** exibem o estado atual da conexão MicroSD *(Nota: Em desenvolvimento / Sujeito a alterações)*:

- **🔵 LED azul aceso** — O cartão MicroSD está montado no **dispositivo de destino**  
- **🟢 LED verde aceso** — O cartão MicroSD está montado no **computador host**  
- **LED apagado** — Nenhum cartão MicroSD inserido ou dispositivo desligado  
- **LED piscando** — Transferência de dados em andamento (atividade de leitura/escrita)

!!! note "Função de montagem automática (Experimental)"
    Por padrão, o cartão MicroSD monta no **host** quando o dispositivo é ligado pela primeira vez.  
    Um recurso experimental futuro permitirá **montagem automática** em qualquer lado (host ou destino) que se conectar primeiro, tornando a experiência ainda mais fluida.


