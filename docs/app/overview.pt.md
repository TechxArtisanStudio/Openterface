# Software

Para colocar seus gadgets Openterface™ KVM em funcionamento, você precisará instalar um dos aplicativos listados abaixo no seu computador host. Você pode baixar esses aplicativos de diferentes plataformas de apps ou simplesmente clicar nos links fornecidos. Se você está se sentindo aventureiro, também pode construí-los a partir do código-fonte usando nossos repositórios GitHub!

![use-case-pc-angled-view](https://assets.openterface.com/images/product/use-case-pc-angled-view.webp){ width=600 }

## Download e Instalação

<div class="grid cards" markdown>

-   ### :fontawesome-brands-windows:{ .lg } **Windows**

    ***

    Baixar ou construir a partir do código-fonte para **Openterface QT Win**:

    [:octicons-download-24: Baixar Instalador {{qt_version}}](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_windows_amd64_installer.exe) <br>
    [:octicons-download-24: Baixar EXE Portátil {{qt_version}}](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_windows_amd64_portable.exe) <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) <br>
    [:octicons-play-24: Assistir Demo](https://youtu.be/ERzpGtRvP2o?si=e9k402f0nxsD8o2j)

-   ### :fontawesome-brands-apple:{ .lg } **macOS**

    ***

    Baixar ou construir a partir do código-fonte para **Openterface MacOS**:

    [:octicons-arrow-right-24: Instalar da App Store](/appstore) <br>
    [:octicons-download-24: Baixar DMG Portátil](macos/dmg-installation.md) <br>
    [:octicons-mark-github-16: Openterface_MacOS](https://github.com/TechxArtisanStudio/Openterface_MacOS) <br>
    [:octicons-play-24: Assistir Demo](https://youtu.be/m7OpUem0zqY?si=tclfl0Jl77tmE6_e)

-   ### :fontawesome-brands-linux:{ .lg } **Linux**

    ***

    Baixar ou construir a partir do código-fonte para **Openterface QT Linux**:

    [:octicons-download-24: Baixar {{qt_version}} AMD64 DEB](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_amd64.deb) <br>
    [:octicons-download-24: Baixar {{qt_version}} AMD64 RPM](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_amd64.rpm) <br>
    [:octicons-download-24: Baixar {{qt_version}} AMD64 AppImage](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_amd64.AppImage) <br>
    [:octicons-download-24: Baixar {{qt_version}} ARM64 DEB](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_arm64.deb) <br>
    [:octicons-download-24: Baixar {{qt_version}} ARM64 AppImage](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_arm64.AppImage) <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) <br>
    [:octicons-play-24: Assistir Demo](https://youtu.be/_ScpI6TC0Pk?si=FSg7A2zmST8QbFec)

-   ### :fontawesome-brands-android:{ .lg } **Android**

    ***

    Baixar ou construir a partir do código-fonte para **Android APK**:

    [:octicons-arrow-right-24: Baixar na Google Play Store](https://play.google.com/store/apps/details?id=com.openterface.AOS)<br>
    [:octicons-download-24: Baixar {{android_version}}](https://github.com/TechxArtisanStudio/Openterface_Android/releases/download/{{android_version}}/OpenterfaceAndroid-release.apk) <br>
    [:octicons-mark-github-16: Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) <br>
    [:octicons-play-24: Assistir Demo](https://x.com/TechxArtisan/status/1825460088922071398)

</div>

???+ warning "Atenção: Verifique Privacidade e Segurança com Apps de Terceiros"
Como todos os nossos apps são open source, você pode encontrar versões alternativas de aplicações host para dispositivos Openterface criadas por outros. Elas podem ser bem legais e oferecer recursos extras, mas aqui está um lembrete amigável: revise cuidadosamente suas práticas de segurança e privacidade—especialmente porque o controle KVM envolve eventos da sua tela, teclado e mouse. A Equipe Openterface não pode garantir a segurança desses apps de terceiros, então proceda com cautela!

## Controles Básicos do App Host

### 💻 Compatibilidade

-   **Software Host**: Instale nosso app host para macOS, Windows ou Linux.
-   **Dispositivos Target**: Nenhuma configuração necessária—apenas conecte qualquer dispositivo com saída de vídeo (HDMI, VGA, etc.) e uma porta USB para controle de teclado/mouse. Funciona com Windows, macOS, Linux, Android e iOS.

### 🖱 Modos do Mouse

-   **Modo Absoluto**: O mouse host mapeia diretamente para a posição da tela target.
-   **Modo Relativo**: Move o cursor target relativamente à posição atual. Saia com um atalho.

### ⌨️ Teclado

Teclas pressionadas do host são enviadas diretamente para o target quando o app está focado.

### ⚙️ Acesso ao BIOS

Controle o BIOS target diretamente.  
Teclas comuns: F2 (Dell/Lenovo/ASUS), F10 (HP), Del (ASUS/Gigabyte/MSI), ⌥ (Apple).

### 🔊 Áudio

O áudio target é transmitido via HDMI e reproduzido no seu computador host.

### 🎥 Vídeo

Visualize sua tela target diretamente dentro do app.

-   **Modelos Atuais**: Display de até **1080p 30Hz** no app, com suporte para entrada **4K 30Hz** via HDMI.
-   **Outras Entradas**: Compatível com VGA, DVI, Micro HDMI e mais quando usando adaptadores apropriados.
-   **Modelos Futuros**: Resoluções e taxas de quadros mais altas serão suportadas conforme novas versões de hardware forem lançadas.

### 🔄 Portas Comutáveis

Alguns dispositivos Openterface incluem portas que podem ser **comutadas entre host e target**, como portas USB 2.0 ou slots de cartão micro-SD (em modelos futuros).

-   **Uso Um de Cada Vez**: Apenas um lado (host ou target) pode acessar a porta por vez.
-   **Métodos de Comutação**:
    -   **Toggle Hardware** — interruptor físico no dispositivo
    -   **Botão Software** — controle via app host
-   **Importante**:
    -   Ejecte com segurança dispositivos de armazenamento (drives USB ou cartões micro-SD) antes de comutar.
    -   Evite conectar dispositivos de alta potência para prevenir instabilidade ou danos.
    -   Veja o [Guia de Portas Comutáveis](/usb-switch) para detalhes e diagramas lógicos.


## Atualizações

<!-- AUTO-GENERATED: This section is automatically generated by scripts/update-post-tool/generate_app_overview_updates.py -->
<!-- DO NOT EDIT MANUALLY -->

- Dec 18, 2025: [Velocidade do Mouse e Desempenho em Jogos do Openterface Mini-KVM no macOS](updates/20251218-macos-mouse-speed.pt.md)

[:octicons-arrow-right-24: Ler mais atualizações](/app/updates)

<!-- END AUTO-GENERATED -->

