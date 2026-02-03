---
title: Perguntas frequentes sobre Openterface Mini-KVM
description: Perguntas frequentes sobre o Mini-KVM, cobrindo recursos, compatibilidade, solução de problemas e planos futuros.
keywords: Mini-KVM, Openterface, switch KVM, código aberto, solução de problemas, captura de vídeo, USB, compatibilidade, autoverificação diagnóstica, controle teclado mouse, diagnóstico hardware, suporte
---

# Perguntas frequentes sobre Openterface Mini-KVM

Bem-vindo às perguntas frequentes do nosso produto principal **Openterface Mini-KVM**.  
Se não encontrar o que precisa, **envie-nos um email para [info@openterface.com](mailto:info@openterface.com)** ou **junte-se à nossa comunidade** no [Discord](/discord) ou [Reddit](/reddit).

⚠️ _As perguntas frequentes podem estar desatualizadas — informe-nos se vir algo que precisa de atualização._

---

## :material-clipboard-list: Navegação rápida

-   [Porta USB e transferência de arquivos](#porta-usb-e-transferência-de-arquivos)
-   [Técnico](#técnico)
-   [Controle](#controle)
-   [Vídeo](#vídeo)
-   [Solução de problemas](#solução-de-problemas)
-   [Mais](#mais)

---

## Porta USB e transferência de arquivos

**:material-chat-question:{ .faq } Pode transferir arquivos?**

Sim — através da porta USB-A comutável compartilhada entre host e alvo.

**:material-chat-question:{ .faq } Posso alternar a porta USB no software?**

Sim, na versão de hardware **v1.9+**.

**:material-chat-question:{ .faq } Por que USB 2.0 em vez de 3.0?**

USB 2.0 é suficiente para vídeo 1080p@30Hz + HID + transferência de arquivos em velocidade padrão mantendo-se compacto, mais frio e mais acessível.  
USB 3.0 pode aparecer em futuros modelos profissionais.

---

## Técnico

**:material-chat-question:{ .faq } Código aberto?**

Sim — certificado pela [OSHWA](https://certification.oshwa.org/cn000015.html). Hardware e software estão no [GitHub](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware).

**:material-chat-question:{ .faq } Acesso BIOS**

A conexão USB direta permite controle completo em nível BIOS, diferente de ferramentas apenas remotas (VNC, TeamViewer).  
Máquinas mais antigas podem ter problemas BIOS reconhecendo nosso hub USB — reporte os casos.

**:material-chat-question:{ .faq } Transmissão de vídeo/dados**

O vídeo é capturado via HDMI e enviado via USB 2.0.  
A porta USB comutável permite compartilhar unidades ou outros dispositivos.

**:material-chat-question:{ .faq } Gerenciamento de energia**

O Mini-KVM pode obter energia de **qualquer lado** (host ou alvo). O lado com o **cabo mais curto** geralmente se torna a fonte de energia principal.  
Para alvos de baixa potência (ex. Raspberry Pi), use uma fonte de alimentação dedicada em vez de retroalimentação via Mini-KVM.

**:material-chat-question:{ .faq } Limites de comprimento de cabo**

-   Mantenha o **cabo USB-C host laranja ≤1.5m**.
-   Para cabos mais longos, injete energia via:
    -   Cabo USB-A macho-macho
    -   [Pinos de extensão](/product/minikvm/extension-pins/)
    -   Divisor USB-C Y
-   A mesma regra se aplica ao **cabo alvo preto**.

---

## Controle

**:material-chat-question:{ .faq } Teclado e mouse não conseguem controlar o computador alvo**

Se você consegue ver a área de trabalho do alvo mas as entradas de teclado e mouse não respondem, isso geralmente significa que a comunicação HID não foi estabelecida. Tente estes passos:

1. **Verificar conexões dos cabos** — Certifique-se de que o cabo Type-C do alvo está conectado ao computador alvo; o cabo do host ao seu computador de controle.
2. **Evitar hubs USB não alimentados** — Use conexão direta ou um hub alimentado.
3. **Redefinir o chip HID** — Se o dispositivo parecer "congelado", use **Menu Avançado → Redefinição de fábrica do chip HID** (OpenterfaceQt) ou **Ferramenta de redefinição serial** (macOS).
4. **Tentar outra porta USB ou reiniciar** — O SO do host pode desabilitar uma porta após erros USB.
5. **Reduzir taxa de transmissão** — Em ambientes ruidosos, mude para 9600 bps para comunicação mais confiável.

Para detalhes, veja [Solução de problemas de controle de teclado e mouse](/product/minikvm/support/keyboard-mouse-control/).

**:material-chat-question:{ .faq } Versão sem fio ou Ethernet?**

Não integrado. Use um computador headless (ex. Raspberry Pi) + desktop remoto para controle remoto.

**:material-chat-question:{ .faq } Compatibilidade PS/2?**

Não — suporte PS/2 pode ser explorado em versões futuras.

**:material-chat-question:{ .faq } Múltiplos Mini-KVMs em um computador?**

Sim, recurso experimental no aplicativo QT (Windows/Linux).

**:material-chat-question:{ .faq } Controle liga/desliga?**

Não diretamente, mas os [pinos de extensão](/product/minikvm/extension-pins/) permitem futuros módulos de controle ATX.

---

## Vídeo

**:material-chat-question:{ .faq } Latência e resolução**

-   Captura em **1080p@30Hz**
-   Latência abaixo de **140ms** → controle suave

**:material-chat-question:{ .faq } Resolução de entrada vs captura**

-   Aceita entrada até **4K@30Hz**
-   Captura em **1080p**, entradas mais altas são subamostradas (podem parecer ligeiramente desfocadas).
-   Melhor prática: **Configure o alvo para 1080p**.

**:material-chat-question:{ .faq } Adequação para jogos**

Não para jogos AAA. Funciona bem para jogos mais leves como Minecraft ou emuladores.

**:material-chat-question:{ .faq } Controle remoto pela internet**

Não integrado, mas emparelhe Mini-KVM com software de desktop remoto no host.

**:material-chat-question:{ .faq } Outros formatos de vídeo**

Use adaptadores para VGA, DVI, DisplayPort, etc.

---

## Solução de problemas

**:material-chat-question:{ .faq } Como executo diagnósticos para verificar se meu Mini-KVM está funcionando?**

Execute a autoverificação diagnóstica integrada para verificar conexões USB e detectar problemas de hardware:

- **macOS:** [Guia de Autoverificação Diagnóstica (macOS)](/product/minikvm/support/diagnostic-self-check/) — Configurações → Avançado & Debug → Abrir Ferramenta de Diagnóstico
- **Windows:** [Guia de Autoverificação Diagnóstica (Windows)](/product/minikvm/support/diagnostic-self-check-windows/) — Avançado → Hardware Diagnostics

Os diagnósticos testam Target/Host Plug & Play, Teste de Estresse, etc. Se todos os testes passarem, seu dispositivo está funcionando corretamente.

**:material-chat-question:{ .faq } Como reporto um problema de hardware ao suporte?**

Se a autoverificação diagnóstica mostrar **FALHA** em um ou mais testes:

1. Complete as etapas de diagnóstico restantes (a ferramenta irá guiá-lo).
2. Quando um problema for detectado, uma janela de **E-mail de Suporte** ou **Relatório de Defeito** será aberta.
3. Insira seu **ID do Pedido** e **Nome**, depois copie o endereço de e-mail e o rascunho.
4. Anexe os **arquivos de log solicitados** (a ferramenta indica quais) e uma **foto da configuração** (Mini-KVM + conexões host/alvo claramente visíveis).
5. Envie o e-mail ao suporte.

Instruções passo a passo: [Guia de Autoverificação Diagnóstica (macOS)](/product/minikvm/support/diagnostic-self-check/) ou [Guia de Autoverificação Diagnóstica (Windows)](/product/minikvm/support/diagnostic-self-check-windows/).

**:material-chat-question:{ .faq } Problemas de hub USB**

Use um **hub alimentado** para evitar quedas de tensão. Hubs não alimentados podem causar fornecimento insuficiente e comportamento errático do HID (teclado/mouse). Veja [Solução de problemas de controle de teclado e mouse](/product/minikvm/support/keyboard-mouse-control/).

**:material-chat-question:{ .faq } Aplicativo não mostra vídeo ou controle não responde**

1. Desconecte todos os cabos, aguarde alguns segundos, reconecte.
2. Verifique [Solução de problemas de controle de teclado e mouse](/product/minikvm/support/keyboard-mouse-control/) para problemas HID (cabos, hubs, redefinição HID).
3. Execute a [autoverificação diagnóstica](/product/minikvm/support/diagnostic-self-check/) (macOS) ou [Hardware Diagnostics](/product/minikvm/support/diagnostic-self-check-windows/) (Windows) para verificar o dispositivo.
4. Se não resolvido, verifique o firmware ou atualize o aplicativo host.

**:material-chat-question:{ .faq } Resoluções estranhas como 43184x24228@44Hz**

O firmware de captura provavelmente reverteu para fábrica.  
Re-flashe o firmware via [lançamentos GitHub](https://github.com/TechxArtisanStudio/Openterface_QT/releases).

**:material-chat-question:{ .faq } Re-flashado mas ainda quebrado?**

-   Verifique a enumeração USB correta (`USB Tree Viewer` ou `lsusb -v`)
-   Confirme o aplicativo host mais recente
-   Execute a [autoverificação diagnóstica](/product/minikvm/support/diagnostic-self-check/) para capturar logs
-   Se ainda falhar, contate o suporte com seu ID do Pedido, logs de diagnóstico e foto da configuração — veja [Como reporto um problema de hardware ao suporte?](#como-reporto-um-problema-de-hardware-ao-suporte)
