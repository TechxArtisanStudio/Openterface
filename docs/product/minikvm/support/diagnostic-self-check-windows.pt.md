---
title: "Openterface Mini-KVM (Windows) - Guia de Autoverificação Diagnóstica de Hardware"
description: "Guia passo a passo para executar a autoverificação diagnóstica de hardware no aplicativo Openterface para Windows. Aprenda como testar conexões USB, detectar problemas e enviar relatórios de diagnóstico para o suporte."
keywords: "Openterface Mini-KVM, Windows, diagnóstico de hardware, autoverificação diagnóstica, solução de problemas KVM, diagnóstico USB KVM, suporte Mini-KVM, teste do dispositivo KVM, Windows KVM, relatório de defeito KVM, guia de solução de problemas Mini-KVM"
---

# Openterface Mini-KVM (Windows) — Guia de Autoverificação Diagnóstica de Hardware

Este guia explica como executar a autoverificação **Diagnóstico de Hardware** na versão **Windows** do aplicativo Openterface e como enviar o relatório de diagnóstico ao suporte se um problema for detectado.

<iframe width="560" height="315" src="https://www.youtube.com/embed/uSq3BDc_SBU?si=rREugsUxX1FzDGqm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Antes de começar

- Conecte o Mini-KVM ao **Host** e ao **Alvo**.
- Mantenha o dispositivo alvo inativo durante os testes (especialmente durante o Teste de Estresse).

> **Importante (Windows):** Os diagnósticos **não avançam automaticamente**.  
> Para mover entre os testes, use **Próximo** (barra inferior) **ou** clique em um item de teste no **painel esquerdo**.  
> Cada teste é executado clicando em **Verificar Agora**.

![next_webp](https://assets2.openterface.com/images/next.webp)

---

## Unidade Funcionando (PASS)

### Passo 1 — Abrir Diagnóstico de Hardware (Windows)
No aplicativo Openterface para Windows, abra: **Avançado → Diagnóstico de Hardware**.  

### Passo 2 — Executar a autoverificação
Na janela de Diagnóstico de Hardware, clique em **Verificar Agora** para executar o passo de diagnóstico atual.  

### Passo 3 — Target Plug & Play (seguir as instruções)
Quando **Target Plug & Play** pedir para reconectar o cabo do alvo, siga as instruções na tela.  
Algumas configurações podem pedir para **desconectar/reconectar mais de uma vez** (por ex., duas vezes).  

![Target-plug&play](https://assets2.openterface.com/images/Target-plug%26play.webp)

### Passo 4 — Host Plug & Play (seguir as instruções)
Siga as instruções na tela para o lado do host.  

![Host-plug&play](https://assets2.openterface.com/images/Host-plug%26play.webp)

### Passo 5 — Teste de Estresse (não toque no alvo)
Durante o **Teste de Estresse**, o mouse do alvo pode se mover automaticamente para detecção.  
**Não opere o alvo** enquanto o teste estiver em execução.  

> **Nota:** O mouse pode se mover rapidamente — não toque no alvo.

![stress-test](https://assets2.openterface.com/images/stress-test.webp)

### Passo 6 — Confirmar PASS
Continue até que a autoverificação seja concluída. Se tudo estiver normal, os resultados mostrarão **PASS / Todos os testes passaram**.  

---

## Problema Detectado (Exemplo: Teclado/Mouse)

Se um problema for detectado, um ou mais itens podem mostrar **FAIL**.

### Passo 1 — Executar o mesmo Diagnóstico de Hardware
Abra **Avançado → Diagnóstico de Hardware**, depois clique em **Verificar Agora** para iniciar.  

### Passo 2 — Continuar com as verificações
Continue com os testes restantes até que os diagnósticos sejam concluídos.  

### Passo 3 — E-mail de suporte abre automaticamente
Quando os diagnósticos terminarem com um problema, uma janela de **E-mail de Suporte** será aberta automaticamente.  

---

## Enviando logs para o Suporte (Windows)

### Passo 4 — Aplicar ID do Pedido + Nome
Insira seu **ID do Pedido** e **Nome**, depois clique em **Aplicar** para inseri-los no rascunho do e-mail. 

![ID+Name](https://assets2.openterface.com/images/ID+Name.webp)

### Passo 5 — Copiar endereço de e-mail e rascunho
- Clique em **Copiar E-mail** para copiar o endereço de e-mail do suporte.
- Clique em **Copiar Rascunho** para copiar o conteúdo do e-mail pré-preenchido (incluindo ID do Pedido + Nome).  
Cole ambos no seu cliente de e-mail (Gmail/Outlook/etc.).  

![copy](https://assets2.openterface.com/images/copy.webp)

### Passo 6 — Anexar os arquivos de log corretos
Clique em **Abrir Pasta de Arquivos**. A ferramenta indicará quais arquivos anexar.  
**Anexe apenas os arquivos de log solicitados** (a pasta pode conter muitos outros logs).  

![list](https://assets2.openterface.com/images/list.webp)

![compress](https://assets2.openterface.com/images/compress.webp)

### Passo 7 — Também anexar uma foto da configuração
No mesmo e-mail, anexe uma **foto clara da configuração** mostrando:
- o dispositivo Mini-KVM,
- ambas as conexões **Host** e **Alvo**,
- portas e cabos claramente visíveis.  

### Passo 8 — Enviar o e-mail
Envie o e-mail ao suporte (texto do rascunho + logs solicitados + foto da configuração anexados).  

---

## O que incluir ao entrar em contato com o suporte

- **ID do Pedido**
- **Arquivos de log de diagnóstico solicitados**
- **Foto da configuração** (Mini-KVM + fiação host/alvo)
