# Openterface QT para Windows e Linux

Este documento fornece uma visão geral de um software KVM (Teclado, Vídeo, Mouse) multiplataforma desenvolvido usando Qt, compatível com sistemas operacionais Linux e Windows. O software facilita o controle sobre um dispositivo alvo a partir de um sistema host, oferecendo uma variedade de recursos acessíveis através de sua barra de menu e funcionalidades adicionais.

## Recursos da Barra de Menu Principal

### Preferências

O menu Preferências permite aos usuários personalizar configurações através de um diálogo com quatro páginas:<br>
![Preferences Gernal](https://assets.openterface.com/images/qt/preferenceGernal.webp)

-   **Geral** Esta página configura o filtro de logs de depuração e a inibição ou não do protetor de tela quando o aplicativo está em execução. As categorias de log incluem:

    -   Core
    -   Serial
    -   UserInterface
    -   host

    Os usuários podem escolher salvar logs em um arquivo .txt e inibir ou não o protetor de tela.<br>

![Preferences Video](https://assets.openterface.com/images/qt/preferenceVideo.webp)

-   **Vídeo** Esta página permite aos usuários:

    -   Selecionar quais dados da câmera capturar.
    -   Definir a resolução.
    -   Escolher o formato do stream de vídeo.

-   **Áudio** Esta página está atualmente em desenvolvimento.<br>

![Preferences TargetControl](https://assets.openterface.com/images/qt/preferenceTargetControl.webp)

-   **Controle do Alvo** Esta página fornece opções para configurar modos de controle para o dispositivo alvo:

    -   **Modos de controle:**

        -   **Teclado + Mouse + dispositivo USB HID**
        -   **Teclado USB**
        -   **Teclado + Mouse**
        -   **Dispositivo USB HID**

    -   **Definir o ID do Fornecedor (VID) e ID do Produto (PID) lidos do alvo.**
    -   **Definir o descritor USB para o alvo.**

### Editar

-   **Colar:** Tanto a opção Colar no menu Editar quanto o botão colar no canto superior esquerdo permitem aos usuários colar texto da área de transferência do host para o dispositivo alvo.

### Controle

Este menu fornece opções para:<br>

-   Definir modos de movimento do mouse: Absoluto ou Relativo. **Controle >> Modo do Mouse >> Absoluto ou Relativo.**
-   Alternar a visibilidade do cursor do mouse do host. **Controle >> Visibilidade do Mouse >> Ocultar Automaticamente ou Sempre Mostrar.**
-   Alternar uma porta USB no hardware entre uso do alvo e do host. **Controle >> USB Comutável >> Para Alvo ou Para Host.**
-   Ajustar a taxa de transmissão do chip. **Controle >> Taxa de Transmissão >> 9600, 115200.**

### Avançado

O menu Avançado inclui as seguintes opções:<br>
![Advance menu](https://assets.openterface.com/images/qt/menuAdvance.webp)

-   **Verificação de Ambiente:** Verifica se os drivers necessários para o software estão instalados.
-   **Redefinir Porta Serial:** Reinicia a porta serial.
-   **Redefinir Teclado e Mouse:** Redefine as configurações do teclado e mouse.
-   **Redefinição de Fábrica do Chip HID:** Restaura o chip HID para suas configurações de fábrica.<br>
    ![Advance SerialConsole](https://assets.openterface.com/images/qt/advanceSerialConsole.webp)
-   **Console Serial:** Abre uma nova janela para monitorar todas as mensagens enviadas para a porta serial, com filtros para mensagens enviadas/recebidas.<br>
    ![Advance ScriptTool](https://assets.openterface.com/images/qt/advanceScriptTool.webp)
-   **Ferramenta de Script:** Executa scripts AutoHotkey (AHK). Este recurso imita o AutoHotkey mas suporta apenas um subconjunto de funções de mouse/teclado e capacidades de captura de tela. Os scripts afetam o dispositivo alvo.
-   **Servidor TCP:** Recebe comandos AutoHotkey via TCP para executá-los no dispositivo alvo.
-   **Atualização de Firmware:** Obtém o firmware mais recente de um servidor remoto, permitindo que os usuários escolham se desejam gravá-lo no dispositivo.

### Idiomas

A interface pode ser configurada para:

-   Dinamarquês
-   Inglês
-   Alemão
-   Francês
-   Japonês
-   Sueco

### Ajuda

O menu Ajuda fornece: <br>
![Help menu](https://assets.openterface.com/images/qt/menuHelp.webp)

-   Links para o site oficial e formulários de feedback para problemas de software/hardware.
-   Informações sobre compra de hardware.
-   Uma descrição do ambiente do software.
-   Sobre: Detalhes sobre a organização.
-   Atualizar: Verifica atualizações do software.

## Funções da Barra de Menu (Da Esquerda para a Direita)

A barra de menu, da esquerda para a direita, inclui as seguintes funcionalidades:<br>

![MenuBar](https://assets.openterface.com/images/qt/menubar.webp)

-   Seleção de Layout do Teclado: Escolha o layout do teclado.
-   Controles de Zoom: Aumentar, diminuir ou redefinir a exibição do stream de vídeo capturado.
-   Teclado Virtual: Inclui teclas de função e combinações de atalhos predefinidas.
-   Captura de Tela: Captura toda a tela do alvo e salva em uma pasta padrão.
-   Modo Tela Cheia: Alterna a exibição em tela cheia.
-   Colar: Cola texto da área de transferência do host para o alvo.
-   Dança do Mouse: Aciona o mouse para realizar movimentos predefinidos.
-   Indicador de Dispositivo USB: Mostra se um dispositivo USB está atribuído ao alvo ou ao host.

Enquanto isso, sinta-se à vontade para explorar nosso **repositório GitHub** de código aberto: [Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) para obter o código mais recente, atualizações, exemplos e relatar problemas.

Você também pode participar da nossa [comunidade Discord](/discord) para se conectar com nossa equipe de desenvolvimento e outros usuários incríveis para discutir qualquer tópico relacionado a KVM.

Para suporte direto, sinta-se à vontade para nos enviar um e-mail em [support@openterface.com](mailto:support@openterface.com).

---

**Tem feedback sobre esta página?** [Nos avise aqui.](https://forms.gle/wmxoR2C1VdG36mT69)
