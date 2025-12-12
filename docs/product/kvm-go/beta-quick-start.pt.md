---
title: "Guia rápido KVM-GO Beta | Instruções de teste beta Openterface"
description: "Guia completo de teste beta para Openterface KVM-GO. Aprenda a testar inatividade prolongada, hot-plug, acesso BIOS, copiar-colar e configurações de simulação de dispositivos. Envie feedback através do nosso questionário beta."
keywords: "KVM-GO beta, teste beta Openterface, guia beta KVM-GO, instruções testador beta, feedback KVM-GO, questionário beta, KVM sobre USB beta, teste controle headless, USB KVM beta"
---

# Guia rápido KVM-GO Beta

> Elaborado com ❤️ por [Iker](https://github.com/IkerGarcia) da comunidade Openterface — obrigado por nos ajudar a criar uma documentação melhor!

Bem-vindo à [beta do KVM-GO](/product/kvm-go/updates/251007-kvm-go-beta-test-kits-sent-1/)! A seguir, você encontra uma versão resumida do questionário de feedback da beta. Siga cada seção, registre suas descobertas e, ao finalizar, envie tudo pelo [questionário de feedback da beta no Google Form](https://openterface.com/product/kvm-go/beta-questions).

Parabéns por ter sido selecionado(a) como testador beta! Estamos muito animados para receber seu feedback; temos certeza de que você conseguirá testar o dispositivo a fundo em diferentes cenários.

Este teste oferece flexibilidade, mas gostaríamos que você se concentrasse em alguns cenários específicos.

Seu feedback é extremamente valioso para nós. Você pode testar outros aspectos do dispositivo, mas estes são os principais pontos que queremos explorar:

1. **Teste de inatividade prolongada**

    1. Inicie o software e conecte-o a um alvo
    2. Deixe o software em execução sem interação por um período prolongado (algumas horas)
    3. Retorne e tente usar os controles de mouse e teclado
    - Depois de deixar o software inativo, o mouse e o teclado funcionaram normalmente quando você voltou?

2. **Teste de hot-plug**

    - Teste desconectar e reconectar o dispositivo enquanto o software estiver em execução.

3. **Acesso ao BIOS e a baixo nível**

4. **Copiar e colar (texto curto e longo)**

5. **Configurações de simulação de dispositivo (Windows/Linux)**

    - 5.1. Configuração de EDID do display
    - 5.2. Identificação do dispositivo USB (VID/PID)
    - 5.3. Funcionalidade do cartão SD
        - Caso de uso 1 - Instalação do sistema: recomendamos experimentar o Ventoy, uma ferramenta que permite colocar vários arquivos ISO em um único cartão SD e escolher qual inicializar. Você tentou gravar uma imagem do sistema no HOST e, em seguida, mudar para o TARGET para a instalação (sem remover o cartão)?
        - Caso de uso 2 - Transferência de arquivos: você usou o cartão SD para transferir arquivos entre o HOST e o TARGET?

Esses exemplos correspondem a algumas das perguntas presentes no formulário de feedback da beta, juntamente com informações gerais sobre consistência de áudio/vídeo/teclado/mouse e gerenciamento térmico.

Obrigado pela sua ajuda!

!!! reminder "Não se esqueça"
    Envie suas observações completas pelo Google Form para que a equipe possa analisá-las rapidamente.

