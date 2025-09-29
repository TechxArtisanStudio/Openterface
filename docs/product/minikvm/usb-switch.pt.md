---
title: "Porta USB Comutável"
description: "Aprenda sobre o sistema duplo de comutação USB hardware-software no Openterface Mini-KVM. Compreenda os quatro estados operacionais, diretrizes de segurança e futuras capacidades de acesso remoto."
keywords: "comutação USB, comutador KVM, comutador hardware, comutador software, controle de porta USB, KVM over USB, KVM over IP, acesso remoto, gerenciamento de dispositivos USB, periféricos de computador, gerenciamento de energia USB"
---

# **Guia de Comutação da Porta USB** | Openterface Mini-KVM

O dispositivo mini-KVM tem uma única porta USB-A 2.0 que pode **conectar-se tanto** ao host quanto ao computador alvo, mas **nunca a ambos simultaneamente**.

O controle vem de dois comutadores:

- **Comutador Hardware**: Um interruptor físico de duas posições no dispositivo ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t.svg#only-light){:style="max-height:20px"} ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t_1.svg#only-dark){:style="max-height:20px"} (para dentro = host, para fora = alvo).
- **Comutador Software**: Um botão de alternância no aplicativo host que redireciona instantaneamente a porta USB para o host ou alvo.

## Estados Operacionais

A conexão da porta USB-A depende das posições tanto do **Comutador Hardware** quanto do **Comutador Software**. A tabela a seguir resume os quatro estados possíveis:

| **Estado** | **Comutador Hardware** | **Comutador Software** | **Porta Conectada A** | **Status de Sincronização** |
| ---------- | ---------------------- | ---------------------- | --------------------- | --------------------------- |
| 1          | Host                   | Host                   | Host                  | Synced                      |
| 2          | Target                 | Target                 | Target                | Synced                      |
| 3          | Target                 | Host                   | Host                  | Out of Sync (→ Host)        |
| 4          | Host                   | Target                 | Target                | Out of Sync (→ Target)      |

- **Synced** significa que as configurações de hardware e software correspondem.
- **Out of Sync** significa que o software substitui temporariamente o comutador hardware até que o comutador hardware seja movido novamente.

Qualquer movimento manual do comutador hardware atualizará a exibição do software e retornará a um estado sincronizado.

Na inicialização, o dispositivo conecta-se por padrão ao host. O software detecta a posição do comutador hardware e sincroniza correspondentemente.

!!! warning "Lembre-se de ejetar o pen drive antes de alternar o comutador"
Se a porta USB estiver sendo usada por um pen drive, certifique-se de ejetar o pen drive antes de alternar o comutador para transferir o uso da porta para outro computador.

??? note "Como compartilhar um pen drive/disco USB entre os dispositivos Host e Alvo?"
Os arquivos podem ser transferidos entre o host e o alvo seguindo estes passos:

    1. Monte um pen drive no host quando o pequeno comutador preto estiver configurado ao lado da porta Type-C do host.
    2. Copie os arquivos para esta unidade montada.
    3. Após copiar, desmonte a unidade sem desconectá-la fisicamente.
    4. Vire o pequeno comutador preto para o outro lado. Esta ação alterna a conexão da porta USB-A para o alvo.
    5. Monte o pen drive no dispositivo alvo e copie/mova os arquivos da unidade, completando o processo de transferência de arquivos do host para o alvo.

    Este método também pode ser usado na direção oposta.

!!! Note "Orientação do Usuário" - **Prioridade do Comutador Software**: Independentemente da posição do comutador hardware, clicar no comutador software mudará imediatamente a direção do circuito.

    - **Sincronização do Comutador Hardware**: Qualquer alternância manual do Comutador Hardware alinhará seu estado com o Comutador Software, transitando do Estado 3 ou 4 não sincronizado para o Estado 1 ou 2. No entanto, esta sincronização não necessariamente altera a conexão do circuito real.

    - **Monitoramento do Comutador Hardware**: O Comutador Hardware, apesar de ser físico, é monitorado pelo software e não controla diretamente a direção do circuito. Em vez disso, o software interpreta a posição do comutador e gerencia a comutação real do circuito.
