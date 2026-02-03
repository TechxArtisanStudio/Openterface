---
title: "Openterface Mini-KVM - Guia de Autoverificação Diagnóstica (macOS)"
description: "Guia passo a passo para executar autoverificações diagnósticas no dispositivo Openterface Mini-KVM com o app macOS. Aprenda como testar conexões USB, detectar problemas e enviar relatórios de defeitos para o suporte."
keywords: "Openterface Mini-KVM, macOS, autoverificação diagnóstica, solução de problemas KVM, diagnóstico USB KVM, suporte Mini-KVM, teste do dispositivo KVM, teste de conexão USB, relatório de defeito KVM, guia de solução de problemas Mini-KVM, ferramenta diagnóstica KVM, diagnóstico de servidores headless, ferramentas de solução de problemas IT"
---

# Openterface Mini-KVM - Guia de Autoverificação Diagnóstica (macOS)

Este guia fornece instruções passo a passo para executar autoverificações diagnósticas no dispositivo Openterface Mini-KVM.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-K6Idzky3fY?si=r7pZgCkBzzZXgrLT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Unidade Boa

**Passo 1:** No aplicativo Openterface, abra Configurações → Configurações...

**Passo 2:** Na janela de Configurações, vá para Avançado & Debug.

**Passo 3:** Clique em Abrir Ferramenta de Diagnóstico.

**Passo 4:** Quando solicitado, clique em Ativar para ligar o registro de diagnóstico.

**Passo 5:** Clique em Verificar Agora para iniciar a autoverificação.

**Passo 6:** Clique em Iniciar Teste, depois desplugue e replugue o USB-C preto (lado do alvo) quando solicitado.

![minikvm-support-target](https://assets.openterface.com/images/minikvm/support/target.webp)

**Passo 7:** Clique em Iniciar Teste, depois desplugue e replugue o USB-C laranja (lado do host) quando solicitado.

![minikvm-support-host](https://assets.openterface.com/images/minikvm/support/host.webp)

**Passo 8:** Clique em Iniciar Teste e espere o teste ser concluído.

**Passo 9:** Clique em Reiniciar Agora e espere até que seja concluído.

**Passo 10:** Clique em Alterar Agora e espere até que a troca de taxa de transmissão seja concluída.

**Passo 11:** Clique em Iniciar Teste e espere cerca de 30 segundos. Não opere o alvo enquanto o teste estiver em execução.

> **Nota:** O mouse pode se mover rapidamente. Não toque no alvo.

![minikvm-support-stress_test](https://assets.openterface.com/images/minikvm/support/stress_test.gif)

**Passo 12:** Confirme que todos os itens mostram marcas de verificação verde e o progresso está completo.

**Passo 13:** Clique no ❌ (canto superior direito) para fechar a janela de Diagnóstico.

---

## Problema Detectado (Exemplo: Teclado/Mouse)

Primeiramente, siga os Passos 1–11 em "Unidade Boa". As notas abaixo explicam o que você verá quando um problema de teclado/mouse for detectado.

## Como esse problema aparece

Neste exemplo, a Conexão Geral mostra FAIL primeiro porque um problema de teclado/mouse no lado do alvo (HID) afeta a verificação geral. Isso é um indicador precoce, não um problema separado. (Você verá o status FAIL destacado ao lado de "Conexão Geral" à esquerda.)

- **Conexão Geral:** FAIL é mostrado aqui primeiro devido ao problema no lado do alvo.

![minikvm-support-overall_connection](https://assets.openterface.com/images/minikvm/support/overall_connection.webp)

- **Plug and Play do Alvo:** Após executar este passo, o resultado pode mostrar o problema no lado do alvo com mais clareza.

> **Dica:** Se um passo mostrar FAIL, os diagnósticos não pararão, mas podem parar de avançar automaticamente — então você precisará continuar manualmente.

## Teste final extra (dependendo do tipo de problema)

**Passo 12:** Após o Teste de Estresse, os diagnósticos podem mostrar um teste final extra dependendo do problema detectado; neste exemplo de teclado/mouse, ele continua para a Verificação da Porta do Alvo.

**Passo 13:** Clique em "Detectar Dispositivos" para iniciar a Verificação da Porta do Alvo, depois siga as instruções na tela.

![minikvm-support-target_port_checking](https://assets.openterface.com/images/minikvm/support/target_port_checking.webp)

## O que acontece quando um problema é detectado

**Passo 14:** Para continuar, clique em Próximo (barra inferior) ou selecione o próximo teste no painel esquerdo.

![minikvm-support-target_plug_n_play](https://assets.openterface.com/images/minikvm/support/target_plug_n_play.webp)

## Enviando logs para o Suporte

**Passo 15:** Clique em Enviar Relatório de Defeito para o Suporte para preparar o relatório para o suporte.

![minikvm-support-send_defect_report_to_support](https://assets.openterface.com/images/minikvm/support/send_defect_report_to_support.webp)

**Passo 16:** Na janela de Relatório de Defeito, insira seu **ID do Pedido** e **Nome**, depois clique em **Aplicar** para inseri-los no rascunho do e-mail.

**Passo 17:** Copie o endereço de e-mail e o rascunho:
- Clique em **Copiar E-mail** para copiar o endereço de e-mail do suporte.
- Clique em **Copiar Rascunho** para copiar o conteúdo do e-mail pré-preenchido (incluindo ID do Pedido + Nome).
- Cole ambos no seu cliente de e-mail (Gmail/Outlook/etc.).

![minikvm-support-support](https://assets.openterface.com/images/minikvm/support/support.webp)

**Passo 18:** Clique em **Abrir Pasta de Logs**. A ferramenta indicará quais arquivos anexar. **Anexe apenas os arquivos de log solicitados** (a pasta pode conter muitos outros logs).

**Passo 19:** No mesmo e-mail, anexe uma **foto clara da configuração** mostrando:
- o dispositivo Mini-KVM,
- ambas as conexões **Host** e **Alvo**,
- portas e cabos claramente visíveis.

**Passo 20:** Envie o e-mail ao suporte (texto do rascunho + logs solicitados + foto da configuração anexados).

**Passo 21:** Clique no ❌ (canto superior direito) para fechar a janela de Diagnóstico.