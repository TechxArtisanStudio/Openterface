---
title: "Configuração de software"
description: "Guia completo de configuração de software para Openterface KVM Extension for uConsole. Aprenda como instalar e configurar o App Openterface no seu uConsole para funcionalidade KVM perfeita."
keywords: "instalação app Openterface, configuração software uConsole, configuração app KVM, configuração app uConsole, guia instalação software"
---

# **Configuração de software** | Openterface KVM Extension for uConsole

## Visão geral da instalação

O App Openterface permite que seu uConsole funcione como uma interface KVM, permitindo que você controle dispositivos alvo através da tela integrada, teclado e trackball.

!!! note "Requisitos"
    - **uConsole**: Requer instalação do App Openterface
    - **Alvo**: Nenhum app necessário - suporta Windows, macOS, Linux, Android, iOS
    - **Vídeo**: Use um cabo HDMI padrão. Use um cabo HDMI padrão. Com um conversor HDMI alimentado, também suporta outros formatos como **VGA**, **DP** e mais. *Dica: Certifique-se de que o conversor esteja adequadamente alimentado; caso contrário, você pode experimentar uma tela preta.*

## Métodos de instalação

### **Opção 1: Instalação Flatpak**

Siga nosso [Guia de instalação Flatpak](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) para etapas de configuração detalhadas.

### **Opção 2: Repositório da comunidade (Recomendado)**

Se você prefere a build da comunidade mantida pelo Rex:

1. **Adicionar repositório**:
```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. **Instalar pacote**:
```bash
sudo apt update
sudo apt install openterfaceqt
```

!!! warning "Notas do repositório"
    Esses comandos requerem sudo. O repositório visa pacotes arm64 Bookworm; verifique a compatibilidade com seu dispositivo antes de instalar.

## Instruções de uso

### **Iniciar sessão KVM**
1. Lance o App Openterface no seu uConsole
2. O app detectará automaticamente a placa Extension KVM
3. Conecte seu dispositivo alvo via HDMI
4. Use o teclado e trackball integrados do uConsole para controlar o dispositivo alvo

### **Recursos de controle**
- **Teclado**: Emulação completa do teclado incluindo teclas multimídia
- **Mouse**: Posicionamento absoluto e relativo do mouse
- **Áudio**: Pass-through de áudio HDMI para os alto-falantes do uConsole

### **Recursos avançados**
- **Transferência de texto**: Transfira rapidamente texto simulando pressionamentos de teclas—ideal para nomes de usuário, senhas e trechos de código
- **USB comutável**: Mude facilmente o acesso USB entre uConsole e dispositivo alvo usando o app host
