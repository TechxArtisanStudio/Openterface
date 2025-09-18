# Openterface Android

## Visão Geral

O Openterface Mini-KVM é uma solução de hardware e software de código aberto projetada para fornecer funcionalidade básica de KVM (Teclado, Vídeo, Mouse) para controlar dispositivos através de uma interface baseada em Android. Este repositório contém o código-fonte do aplicativo Android, configurações de compilação e scripts de suporte para configurar e implantar o projeto.

Estamos comprometidos com hardware aberto e software de código aberto, licenciado sob a [GNU Affero General Public License v3](LICENSE).

## Módulos de Recursos

### 1. Exibição de Vídeo

#### Funcionalidade Principal

-   Transmite a saída de vídeo do dispositivo conectado para a tela Android em tempo real.
-   Suporta ajustes de imagem para visualização ideal.

![image](https://assets.openterface.com/images/android/videoConnect.webp)

#### Descrição da Interface do Usuário

-   A tela principal exibe o feed de vídeo do dispositivo alvo, ocupando a maior parte da interface.
-   Uma barra de ferramentas na lateral fornece controles de ajuste (brilho, contraste, matiz).

#### Fluxo de Operação

1. Conecte o hardware Mini-KVM ao dispositivo alvo via HDMI e USB.
2. Conecte o Mini-KVM ao seu dispositivo Android via USB-C.
3. Inicie o aplicativo; o feed de vídeo aparece automaticamente.
4. Use os controles deslizantes da barra de ferramentas para ajustar brilho, contraste ou matiz conforme necessário.

![image](https://assets.openterface.com/images/android/colorSetting.webp)

#### Recursos Especiais

-   O zoom com dois dedos melhora a visualização do display

![image](https://assets.openterface.com/images/android/enlargeAndSideBar.webp)

---

### 2. Controle do Mouse

#### Funcionalidade Principal

-   Fornece controle absoluto e relativo do mouse para interagir com a interface do dispositivo alvo.
-   Suporta cliques esquerdo e direito.
-   Selecione o modo no menu direito.

#### Descrição da Interface do Usuário

-   O feed de vídeo funciona como um touchpad para entrada do mouse.
-   Um botão de ação flutuante (FAB) alterna entre os modos de mouse e teclado.

#### Fluxo de Operação

1. Certifique-se de que o dispositivo está conectado com sucesso.
2. Toque na tela para mover o cursor do mouse para essa posição (controle absoluto).
3. Clique duplo com um dedo para clique esquerdo, clique com dois dedos para clique direito.
4. O modo de arrastar é manter pressionado o botão esquerdo sem soltá-lo.

#### Recursos Especiais

-   Controle relativo do mouse (em desenvolvimento, alterne via configurações quando disponível).

## ![image](https://assets.openterface.com/images/android/mouseThouchMode.webp)

### 3. Entrada de Teclado

#### Funcionalidade Principal

-   Digite no dispositivo clicando nas teclas do teclado.

#### Descrição da Interface do Usuário

-   O ícone do teclado está no canto inferior direito.
-   O teclado inclui teclas de atalho, teclas do sistema, teclas padrão e teclas de função (F1-F12).

#### Fluxo de Operação

1. Clique no ícone do teclado no canto inferior direito para exibir o teclado.
2. Digite texto ou pressione teclas de função conforme necessário.

#### Recursos Especiais ou Atalhos

-   **Teclas de Atalho**: Ctrl+C、Ctrl+V、Ctrl+Z、Ctrl+X、Ctrl+A、Ctrl+S、
    Win+Tab、Win+S、Win+E、Win+R、Win+D、Win+L、Alt+F4、Ctrl+Alt+Del、Alt+PrtScr.
-   **Teclas de Função**: F1-F12、Teclas de Símbolos.
-   **Teclas Padrão**: 0-9、A-Z、Enter、Espaço、delete.

![image](https://assets.openterface.com/images/android/enlargeAndKeyBoard.webp)
![image](https://assets.openterface.com/images/android/keyBoardFunction.webp)
![image](https://assets.openterface.com/images/android/keyBoardSystem.webp)

---

Enquanto isso, sinta-se à vontade para explorar nosso **repositório GitHub** de código aberto: [Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) para o código mais recente, atualizações, exemplos e para relatar problemas.

Você também pode se juntar à nossa [comunidade Discord](/discord) para se conectar com nossa equipe de desenvolvimento e outros usuários incríveis para discutir qualquer tópico relacionado a KVM.

Para suporte direto, sinta-se à vontade para nos enviar um e-mail para [support@openterface.com](mailto:support@openterface.com).

---

**Tem feedback sobre esta página?** [Deixe-nos saber aqui.](https://forms.gle/wmxoR2C1VdG36mT69)