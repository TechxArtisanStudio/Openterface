---
title: Perguntas Frequentes para Openterface KVM-Go Series
description: Perguntas frequentes sobre a série KVM-Go, cobrindo recursos, compatibilidade e informações de pré-lançamento.
keywords: KVM-Go, Openterface, KVM ultra-compacto, HDMI integrado, KVM porta-chaves, código aberto, pré-lançamento, captura de vídeo, USB, compatibilidade, MicroSD
---

# Perguntas Frequentes para Openterface KVM-Go Series

Bem-vindo às perguntas frequentes da nossa **série Openterface KVM-Go** de próxima geração.  
Se não encontrar o que precisa, **envie-nos um e-mail para [info@openterface.com](mailto:info@openterface.com)** ou **junte-se à nossa comunidade** no [Discord](/discord) ou [Reddit](/reddit).

⚠️ **Nota**: KVM-Go está atualmente em desenvolvimento de pré-lançamento. Recursos, especificações e design estão sujeitos a alterações conforme finalizamos o produto.

---

## :material-clipboard-list: Navegação Rápida

- [Perguntas Frequentes para Openterface KVM-Go Series](#perguntas-frequentes-para-openterface-kvm-go-series)
  - [:material-clipboard-list: Navegação Rápida](#material-clipboard-list-navegação-rápida)
  - [Geral](#geral)
  - [MicroSD e Transferência de Ficheiros](#microsd-e-transferência-de-ficheiros)
  - [Técnico](#técnico)
  - [Pré-Lançamento](#pré-lançamento)

---

## Geral

**:material-chat-question:{ .faq } O que é KVM-Go?**

KVM-Go é a nossa solução KVM-over-USB ultra-compacta de próxima geração. Tem o tamanho de um porta-chaves com conectores de vídeo integrados (HDMI, DisplayPort ou VGA) que eliminam a necessidade de cabos separados.

**:material-chat-question:{ .faq } Qual é o seu tamanho?**

Dimensões ultra-compactas: **18 × 18 × 55 mm** (0,71 × 0,71 × 2,17 polegadas) — pequeno o suficiente para caber no porta-chaves. O peso é aproximadamente **25g (0,9 oz)**.

**:material-chat-question:{ .faq } Que modelos estão disponíveis?**

- **KVM-Go HDMI Male** — Conexão HDMI direta para dispositivos modernos
- **KVM-Go DisplayPort Male** — Suporte DisplayPort de alto desempenho  
- **KVM-Go VGA Male** — Compatibilidade com sistemas legados (em breve)

**:material-chat-question:{ .faq } Como se compara ao Mini-KVM?**

Melhorias principais:

- **Tamanho**: 18×18×55mm vs 61×53×13,5mm (muito menor)
- **Peso**: 25g vs 48g (mais leve)
- **Vídeo**: 4K@60Hz vs 1080p@30Hz (melhor desempenho)
- **USB**: USB 3.0 vs USB 2.0 (mais rápido)
- **Configuração**: Conectores integrados vs cabos separados (mais fácil)

**:material-chat-question:{ .faq } Qual é a velocidade de arranque?**

O tempo de arranque do hardware é inferior a 1 segundo, permitindo resolução de problemas imediata sem atrasos ou perturbações no fluxo de trabalho.

---

## MicroSD e Transferência de Ficheiros

**:material-chat-question:{ .faq } Pode transferir ficheiros?**

Sim — através da **ranhura MicroSD comutável** que pode ser partilhada entre o anfitrião e dispositivos alvo, permitindo transferências de ficheiros rápidas sem remover fisicamente o cartão.

**:material-chat-question:{ .faq } Como mudo a direção do MicroSD?**

Dois métodos convenientes:
1. **Botão de Hardware** – Botão físico no dispositivo para controlo manual
2. **Interruptor de Software** – Botão de alternância na aplicação anfitriã para mudança instantânea

**:material-chat-question:{ .faq } O que significam os indicadores LED?**

Os **indicadores LED de duas cores** mostram o estado atual da conexão MicroSD:

- **🔵 LED Azul LIGADO** – O cartão MicroSD está montado no **dispositivo alvo**  
- **🟢 LED Verde LIGADO** – O cartão MicroSD está montado no **computador anfitrião**  
- **LED DESLIGADO** – Nenhum cartão MicroSD inserido ou dispositivo desligado  
- **LED A PISCAR** – Transferência de dados em progresso (atividade de leitura/escrita)

**:material-chat-question:{ .faq } Como instalo corretamente o cartão MicroSD?**

Insira o cartão MicroSD firmemente até sentir um **clique**, indicando que está bem colocado e bloqueado. Este feedback táctil confirma a conexão correta.

---

## Técnico

**:material-chat-question:{ .faq } Qual é o desempenho de vídeo?**

- **Entrada**: Até 4096×2160 @ 60 Hz (YUV420), 4096×2160 @ 30 Hz (YUV444)
- **Saída**: 4096×2160 @ 60 Hz (MJPEG), 3840×2160 @ 30 Hz (YUV420)
- **Padrão**: 1080p@60Hz para estabilidade e desempenho ótimos
- **Latência**: Menos de 140ms para controlo suave

**:material-chat-question:{ .faq } O modo 4K tem limitações?**

Sim — o modo 4K é experimental e gera calor adicional. A superfície do dispositivo pode ficar bastante quente durante operações prolongadas em 4K. Para estabilidade e desempenho ótimos, recomenda-se o modo 1080p@60Hz padrão.

**:material-chat-question:{ .faq } É código aberto?**

Sim — certificado pela [OSHWA](https://certification.oshwa.org/cn000015.html). Hardware e software estão no [GitHub](/contributing/).

**:material-chat-question:{ .faq } Acesso ao BIOS**

A conexão USB direta permite controlo completo ao nível do BIOS, ao contrário de ferramentas apenas remotas (VNC, TeamViewer).

**:material-chat-question:{ .faq } Suporte multiplataforma?**

[Aplicações anfitriãs](/app) compatíveis com macOS, Windows, Linux, Android e aplicação web Chrome para integração universal.

**:material-chat-question:{ .faq } Posso usá-lo com um iPad?**

Sim — o suporte iPadOS chegará em breve através de uma aplicação nativa disponível na Apple App Store. Isto é possível graças à capacidade Bluetooth integrada do KVM-GO, tornando-o um dos poucos KVMs que funciona nativamente com iPads.

**:material-chat-question:{ .faq } Existe uma aplicação baseada na web?**

Sim — visite [Openterface Viewer](https://openterface-viewer.pages.dev/) para uma aplicação baseada em navegador sem instalação (funciona no Chrome, Edge, Safari). Perfeita para acesso rápido ou quando não consegue instalar software no computador anfitrião. Obrigado à nossa incrível comunidade, particularmente [@kashalls](https://github.com/kashalls) que iniciou este projeto.

**:material-chat-question:{ .faq } Que conector de vídeo devo escolher?**

- **HDMI**: Melhor para dispositivos modernos, servidores, estações de trabalho
- **DisplayPort**: Ecrãs de alta resolução, configurações profissionais
- **VGA**: Sistemas legados, servidores mais antigos (em breve)

---

## Pré-Lançamento

**:material-chat-question:{ .faq } Quando estará disponível o KVM-Go?**

KVM-Go está atualmente em testes de produção em pequenos lotes com unidades enviadas a testadores beta para validação no mundo real.

**Cronograma de Produção**:

- **Novembro 2025**: Lançamento da campanha
- **Dezembro 2025**: Finalizar configuração de produção e fornecimento de componentes
- **Janeiro-Março 2026**: Produção em massa e controlo de qualidade
- **Abril 2026**: Primeiros envios para apoiantes

Junte-se à nossa [lista de espera]({{ config.extra.kvmgo_purchase_link }}) para se manter atualizado sobre o progresso e obter acesso antecipado.

**:material-chat-question:{ .faq } Quanto custará?**

Os preços serão anunciados durante a campanha de lançamento oficial. Os primeiros apoiantes receberão descontos especiais e acesso prioritário.

**:material-chat-question:{ .faq } Posso tornar-me um testador beta?**

Sim! Se tem experiência em testes de hardware e software, é bem-vindo a candidatar-se ao nosso programa de testes beta [aqui](https://forms.gle/yaS1F5E5MSo8DWNZ6).

**:material-chat-question:{ .faq } As especificações são finais?**

Não, recursos, especificações e design estão sujeitos a alterações conforme finalizamos o produto durante o desenvolvimento.

