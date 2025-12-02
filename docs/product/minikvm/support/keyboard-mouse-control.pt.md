# **Resolução de problemas de teclado e mouse que não conseguem controlar o computador de destino**

Ocasionalmente, os usuários podem experimentar situações em que as funções de teclado e mouse do dispositivo Openterface não funcionam como esperado. Este documento descreve as causas mais comuns e como resolvê-las ou evitá-las.

**Feedback do software:** Quando o Openterface não consegue estabelecer comunicação HID devido a uma conexão de destino ausente ou incorreta, a interface destaca o status para que você possa agir rapidamente.

- No **macOS**, o ícone de teclado e mouse no canto superior direito do utilitário Openterface fica **laranja**.  

    <img src="https://assets.openterface.com/images/software/inactive_keyboardmoue_macos.webp" alt="Inactive keyboard and mouse (macOS)" width="200" />

- No **Windows/Linux**, o ícone correspondente na parte inferior da janela fica **vermelho**.  

    <img src="https://assets.openterface.com/images/software/inactive_keyboardmoue_windows.webp" alt="Inactive keyboard and mouse (Windows)" width="200" />

O vídeo ainda aparece no Openterface, mas o teclado e o mouse não respondem — você consegue ver a área de trabalho de destino, mas não consegue controlá-la. Isso geralmente significa que a comunicação HID não foi estabelecida (por exemplo, cabo de destino errado, hub sem alimentação ou chip HID com defeito); verifique a lista de verificação e as seções abaixo. O software também bloqueia conexões de teclado/mouse adicionais até que o cabeamento/problema seja resolvido.

---

## **1. Conexão de cabo incorreta**

**Problema:**  
Surpreendentemente comum: os usuários esquecem de conectar a porta Openterface Target Type-C ao computador de destino.

**Solução:**  
✅ Sempre verifique:
- O **cabo Type-C de destino** está conectado com segurança da **porta de destino** Openterface ao **computador de destino** que você deseja controlar.
- O **cabo USB-A/USB-C do host** está conectado ao seu **computador host/controlador** (onde OpenterfaceQt ou o software de controle é executado).

> **Dica:** Rotule os cabos para evitar confusão em configurações complexas.
- Conecte o cabo preto ao lado preto do conector de destino.
- Conecte o cabo laranja ao lado coberto de laranja do conector de destino.


## **2. Uso de hubs USB sem alimentação**

**Problema:**  
Conectar o Openterface através de um hub USB sem alimentação pode levar a **fornecimento de energia insuficiente** (queda de tensão VBUS). Isso pode fazer com que o dispositivo se comporte de forma errática ou não inicialize as funções HID (teclado/mouse).

**Solução:**  
✅ **Evite hubs USB sem alimentação** entre o Openterface e o computador de destino.  
✅ Se um hub for necessário, use um **hub USB de alta qualidade com alimentação externa** que possa fornecer alimentação estável de 5V.

> **Nota:** O fornecimento de energia USB é crítico para o funcionamento confiável do chip HID. Quedas de tensão podem desencadear falhas internas.

---

## **3. Chip HID entra em "estado zumbi"**

**Problema:**  
Em certas condições — como rajadas de comandos rápidos combinadas com alimentação marginal — o chip HID interno (por exemplo, CH9329) pode entrar em um **"estado zumbi".** Neste estado:
- O chip HID se trava e interrompe o envio de dados de resposta em série para o computador host.
- Mantém um estado de erro interno que impede a reinicialização normal pelo software host.
- O dispositivo pode parecer conectado (vídeo presente) enquanto as entradas permanecem sem resposta.
- O software host (por exemplo, OpenterfaceQt) não consegue reinicializar o dispositivo corretamente.
- A reconexão de todos os cabos ou o ciclo de energia da conexão USB normalmente não limpam esse erro interno; é necessária uma redefinição de fábrica do chip HID.

**Solução:**  
Execute uma **redefinição de fábrica do chip HID**:

- No **macOS**: Use a **Ferramenta de reinicialização serial** disponível no **Menu avançado** do utilitário macOS.  

    <img src="https://assets.openterface.com/images/software/MacOS_FactoryResetHID.webp" alt="Serial Reset Tool (macOS)" width="150" />

- No **OpenterfaceQt** (aplicativo desktop): Vá para **Menu avançado → Redefinição de fábrica do chip HID**.

    <img src="https://assets.openterface.com/images/software/OpenterfaceQT_FactoryResetHID.webp" alt="Factory Reset HID Chip (OpenterfaceQt)" width="150" />

> Isto limpa o estado interno do chip e restaura o funcionamento normal.

---

## **4. Sensibilidade da taxa de transmissão em ambientes ruidosos**

**Problema:**  
O Openterface usa por padrão uma taxa de transmissão de **115200 bps** para transmissão de dados de mouse mais rápida. No entanto, em ambientes eletricamente ruidosos (por exemplo, fontes de alimentação comutadas ou cabos longos/mal blindados), essa taxa de transmissão alta pode levar a **erros de comunicação serial**, causando perda ou corrupção de comandos HID.

**Solução:**  
Mude para uma taxa de transmissão de **9600 bps**:
- Isto melhora significativamente a **confiabilidade da comunicação** em configurações ruidosas.
- O impacto na latência é **negligenciável** sob uso típico (por exemplo, captura de vídeo de 30 fps e controle).

> **Recomendação:** Se você experimentar problemas intermitentes de entrada sem problemas de alimentação ou conexão, tente reduzir a taxa de transmissão na configuração do Openterface.

---

## **Lista de verificação de resumo**

Se o teclado/mouse não estiver funcionando:

1. ✅ Confirme que o **cabo Type-C de destino** correto está conectado ao **computador de destino**.
2. ✅ Evite hubs USB sem alimentação — use conexão direta ou um **hub com alimentação**.
3. ✅ Se o dispositivo parecer "congelado", **reinicie o chip HID** via software.
4. ✅ Em ambientes instáveis, **reduza a taxa de transmissão para 9600** para comunicação mais robusta.
5. ✅ Se as tentativas acima não ajudarem, tente uma porta USB diferente no host ou reinicie o computador host — o SO pode desabilitar uma porta ou o hub após receber muitos pacotes de erro USB. Trocar de porta ou reiniciar o host geralmente restaura a conexão.

---

Ao abordar essas quatro áreas, a maioria dos problemas intermitentes de HID pode ser evitada ou resolvida rapidamente. Para problemas persistentes, entre em contato com o suporte (support@openterface.com) com os detalhes de sua configuração e logs.
