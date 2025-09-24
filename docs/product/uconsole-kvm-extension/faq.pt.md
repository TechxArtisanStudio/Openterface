---
title: Perguntas Frequentes para Openterface KVM Extension for uConsole
description: Perguntas frequentes sobre a Extensão KVM para uConsole, cobrindo funcionalidades, compatibilidade, resolução de problemas e instalação.
keywords: extensão KVM, uConsole KVM, resolução problemas, captura vídeo, USB HID, compatibilidade, instalação
---

# Perguntas Frequentes para Openterface KVM Extension for uConsole

Bem-vindos às Perguntas Frequentes para a nossa **Openterface KVM Extension for uConsole**.  
Se não encontrarem o que precisam, **enviem-nos um email para [support@openterface.com](mailto:support@openterface.com)** ou **juntem-se à nossa comunidade** no [Discord](/discord).

⚠️ _As Perguntas Frequentes podem estar desatualizadas — façam-nos saber se virem algo que precisa de atualização._

---

## :material-clipboard-list: Navegação Rápida

- [Perguntas Frequentes para Openterface KVM Extension for uConsole](#perguntas-frequentes-para-openterface-kvm-extension-for-uconsole)
  - [:material-clipboard-list: Navegação Rápida](#material-clipboard-list-navegação-rápida)
  - [Instalação e Hardware](#instalação-e-hardware)
  - [Compatibilidade](#compatibilidade)
  - [Controlo e Funcionalidades](#controlo-e-funcionalidades)
  - [Vídeo e Áudio](#vídeo-e-áudio)
  - [Resolução de Problemas](#resolução-de-problemas)
  - [Mais](#mais)

---

## Instalação e Hardware

**:material-chat-question:{ .faq } Como funciona a placa Extensão KVM?**

Captura a saída HDMI de um dispositivo alvo e exibe-a no uConsole. Ao mesmo tempo, o teclado e trackball do uConsole são utilizados para controlar o dispositivo alvo através de emulação USB HID.

**:material-chat-question:{ .faq } Posso usar isto com o módulo 4G/LTE instalado?**

Não. Esta placa ocupa o mesmo slot de expansão. Terão de escolher entre conectividade celular ou funcionalidade KVM.

**:material-chat-question:{ .faq } Por que preciso das arruelas?**

A placa Extensão KVM tem 1,0 mm de espessura (mais fina que a original 4G/LTE de 1,2 mm). As arruelas compensam esta diferença e asseguram pressão apropriada do contactor de mola para conexões confiáveis.

**:material-chat-question:{ .faq } Que ferramentas preciso para a instalação?**

Precisarão de uma chave de fendas hexagonal para remover e instalar os parafusos de montagem. Precauções ESD (pulseira de pulso ou superfície aterrada) são recomendadas mas não obrigatórias.

**:material-chat-question:{ .faq } A instalação é reversível?**

Sim, podem remover a placa Extensão KVM e reinstalar o módulo 4G/LTE original a qualquer momento. Guardem o módulo original e os parafusos num local seguro.

---

## Compatibilidade

**:material-chat-question:{ .faq } Que modelos uConsole são compatíveis?**

Compatível com dispositivos uConsole que têm o slot de expansão 4G/LTE padrão. Verifiquem as especificações do vosso dispositivo para confirmar compatibilidade.

**:material-chat-question:{ .faq } Que dispositivos alvo posso controlar?**

Qualquer dispositivo com saída HDMI, incluindo:

- Computadores desktop e servidores
- Computadores de placa única (Raspberry Pi, etc.)
- Sistemas embebidos
- PCs industriais
- Consolas de jogos
- Leitores multimédia

**:material-chat-question:{ .faq } O dispositivo alvo precisa de software especial?**

Nenhuma instalação de software é necessária no dispositivo alvo. A Extensão KVM funciona com qualquer dispositivo que tenha saída HDMI.

**:material-chat-question:{ .faq } Posso controlar múltiplos dispositivos alvo?**

Podem controlar um dispositivo alvo de cada vez. Para alternar entre dispositivos, desliguem o cabo HDMI e conectem-no a um dispositivo alvo diferente.

---

## Controlo e Funcionalidades

**:material-chat-question:{ .faq } Que métodos de entrada são suportados?**

- Emulação completa do teclado incluindo teclas multimédia
- Posicionamento absoluto e relativo do rato
- Função de despertar do computador
- Pass-through de áudio via HDMI

**:material-chat-question:{ .faq } Posso transferir ficheiros entre uConsole e dispositivo alvo?**

A Extensão KVM fornece apenas controlo de vídeo e entrada. Para transferência de ficheiros, precisarão usar outros métodos como partilha de rede, unidades USB ou armazenamento na nuvem.

**:material-chat-question:{ .faq } Suporta acesso a nível BIOS?**

Sim, a emulação USB HID direta permite controlo completo a nível BIOS, ao contrário das ferramentas de acesso remoto baseadas em rede.

**:material-chat-question:{ .faq } Posso usá-lo para jogos?**

Embora tecnicamente possível, a latência e método de controlo podem não ser ideais para jogos rápidos. É mais adequado para tarefas de administração de sistema e desenvolvimento.

---

## Vídeo e Áudio

**:material-chat-question:{ .faq } Que resoluções de vídeo são suportadas?**

A extensão aceita entrada de vídeo HDMI padrão. A resolução de exibição real depende das capacidades do ecrã do vosso uConsole.

**:material-chat-question:{ .faq } O áudio é suportado?**

Sim, o áudio embebido HDMI é passado para os altifalantes do uConsole.

**:material-chat-question:{ .faq } E a latência de vídeo?**

A extensão fornece vídeo de baixa latência adequado para interação em tempo real e resolução de problemas a nível BIOS.

**:material-chat-question:{ .faq } Posso usar adaptadores para diferentes saídas de vídeo?**

Sim, podem usar adaptadores HDMI para dispositivos com saídas VGA, DVI ou DisplayPort.

---

## Resolução de Problemas

**:material-chat-question:{ .faq } Nenhum sinal de vídeo aparece**

- Verifiquem a conexão do cabo HDMI em ambas as extremidades
- Confirmem que o dispositivo alvo está ligado e configurado para sair via HDMI
- Tentem um cabo HDMI diferente
- Reiniciem a App Openterface

**:material-chat-question:{ .faq } A entrada de controlo não funciona**

- Assegurem-se de que a placa Extensão KVM está corretamente instalada
- Verifiquem que os contactores de mola fazem bom contacto
- Reiniciem a App Openterface
- Confirmem que o dispositivo alvo reconhece entrada USB

**:material-chat-question:{ .faq } A placa não encaixa corretamente**

- Assegurem-se de que as arruelas estão corretamente posicionadas
- Verifiquem que os parafusos não estão demasiado apertados
- Confirmem que a placa se assenta plana sem movimento
- Assegurem-se de que estão usando os parafusos de montagem corretos

**:material-chat-question:{ .faq } A App não deteta a extensão**

- Verifiquem que a placa está corretamente instalada
- Reiniciem o uConsole
- Reinstalem a App Openterface
- Confirmem que estão usando a versão de software correta

---

## Mais

**:material-chat-question:{ .faq } O software é open source?**

Sim! As nossas Apps **Openterface Connect** são completamente open source e estão disponíveis no nosso [repositório GitHub](https://github.com/TechxArtisanStudio/Openterface_QT).

**:material-chat-question:{ .faq } Onde posso obter suporte?**

- **Email**: [support@openterface.com](mailto:support@openterface.com)
- **Discord**: [Juntem-se à nossa comunidade](https://discord.gg/ruAD9kcYbq)
- **GitHub**: [Reportar problemas](https://github.com/TechxArtisanStudio/Openterface_QT/issues)
