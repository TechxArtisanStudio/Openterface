# Extensão KVM Openterface para uConsole

![KVM Extension Connected to Target Device 2](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-2.webp){:style="height:300px"}

## Visão Geral

Transforme seu uConsole em um **console KVM (Teclado, Vídeo, Mouse) portátil** com esta placa de extensão plug-and-play.

A **Extensão KVM Openterface** substitui o modem 4G/LTE original no slot de expansão do seu uConsole e fornece **entrada HDMI direta e controle USB HID**, permitindo que você gerencie dispositivos headless em movimento—sem necessidade de monitores externos, teclados ou configuração de rede.

![KVM Extension Board Front Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:300px"}
![KVM Extension Board Backm Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:300px"}


## Recursos

- **Fator de Forma Perfeito**  
    Corresponde ao tamanho 37×77 mm do módulo 4G/LTE para integração de hardware perfeita.

- **HDMI Direto + USB HID**  
    Permite controle responsivo de dispositivos conectados usando a entrada e tela integradas do uConsole.

- **Baixa Latência**  
    Adequado para solução de problemas em nível BIOS e interação em tempo real.

- **Verdadeiramente Portátil**  
    Torna o uConsole uma ferramenta móvel para desenvolvedores, engenheiros e técnicos.

- **Amigável ao Open Source**  
    Construído na plataforma [Openterface KVM](https://github.com/techxArtisanStudio/openterface_qt). Contribuições da comunidade são bem-vindas.


## Casos de Uso

- **Administração de Sistema**  
    Acesse e solucione problemas de servidores ou dispositivos embarcados sem um switch KVM volumoso.

- **Desenvolvimento de Hardware**  
    Teste e depure Raspberry Pi, SBCs ou microcontroladores diretamente.

- **Implantações de Campo**  
    Execute manutenção ou configuração em data centers ou locais remotos.


## Instalação de Hardware

Siga estas etapas de instalação de hardware para substituir o módulo 4G/LTE no seu uConsole pela placa de Extensão KVM Openterface e garantir um encaixe seguro.

### O que Você Precisa

- Sua placa de extensão KVM Openterface
- A junta fornecida (espessador de plástico) 
- Uma chave de fenda hexagonal (para os parafusos de montagem da placa)
- Precauções ESD (pulseira ou superfície aterrada) — recomendado

### Instalando a Placa de Extensão

1. Desligar e Desconectar

    Desligue o uConsole e desconecte toda alimentação e cabos.

2. Remover o Módulo Existente

    Use uma chave de fenda hexagonal para remover os dois parafusos que seguram o módulo 4G/LTE ou a placa de extensão existente.

    Levante cuidadosamente a placa para cima para evitar dobrar os contatores de mola.

3. Instalar a Placa de Extensão KVM

    - A placa de Extensão KVM Openterface tem 1.0 mm de espessura (mais fina que o 4G/LTE original de 1.2 mm). Por isso, recomendamos colocar a junta fornecida nos postes de parafuso (entre o PCB e os espaçadores de montagem) para que a junta fique sob os postes de parafuso antes de assentar a placa. Isso compensa o PCB mais fino e ajuda a garantir pressão adequada do contator de mola.
    - Se preferir verificar primeiro, assente a placa sem a junta e verifique contato uniforme da mola; se o contato for desigual ou a placa assentar frouxamente, adicione a junta e reassente a placa.

<div style="display:flex;gap:1rem;align-items:flex-start;flex-wrap:wrap">
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-gasket-1.webp" alt="Installing KVM Extension gasket" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp" alt="Installing KVM Extension into uConsole" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
</div>

4. Reinserir Parafusos

    Reinsira os dois parafusos e aperte com a chave de fenda hexagonal. Apertado é suficiente — não aperte demais.

5. Verificar Encaixe

    A placa deve assentar plana sem movimento notável. Verifique se os contatores de mola estão fazendo contato uniforme através dos pads.

6. Testar o Hardware

    Reconecte a alimentação, inicialize o sistema e teste dispositivos HDMI, áudio e USB HID para confirmar operação adequada.

## Guia de Configuração de Software

Para usar a Extensão KVM, instale o **App Openterface** no seu uConsole.

Opção 1 - Usar versão Flatpak do Openterface
- 📖 Siga nosso [Guia de Instalação Flatpak](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) para etapas de configuração detalhadas.

![KVM Extension Connected to Target Device](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1c.webp){:style="height:300px"}

Opção 2 - Instalar versão da comunidade do Rex

Se você quer a build da comunidade mantida pelo Rex, adicione seu repositório e instale o pacote com os comandos abaixo.

1. Adicionar chave GPG do repositório e repositório

```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. Atualizar e instalar

```bash
sudo apt update
sudo apt install openterfaceqt
```

Notas: estes comandos requerem sudo. O repositório visa pacotes arm64 Bookworm; verifique compatibilidade com seu dispositivo antes de instalar.

## Status Pré-Lançamento

- 📦 Primeiro lote atualmente em preparação  
- ⏳ Envio estimado começa **início de agosto 2024**  
- 🛒 Quantidade limitada – [Pré-encomende agora](https://shop.techxartisan.com/products/openterface-kvm-ext-for-uconsole) para reservar sua unidade

> **Aviso de Pré-encomenda**  
> Este item está atualmente em pré-encomenda com tempo de entrega estimado de **aproximadamente 2 meses**.  
> Se você precisar de outros itens mais cedo, por favor faça um **pedido separado**. Pedidos combinados serão enviados quando este produto estiver pronto.

## Comunidade e Suporte

- 🗨️ Junte-se à discussão: [Servidor Discord](https://discord.gg/ruAD9kcYbq)  
- 📧 Suporte por email: [info@openterface.com](mailto:info@openterface.com)


## FAQs

**P: Como funciona a Placa de Extensão KVM?**  
Ela captura a saída HDMI de um dispositivo alvo e a exibe no uConsole. Ao mesmo tempo, o teclado e trackball do uConsole são usados para controlar o dispositivo alvo via emulação USB HID.

**P: Posso usar isso com o módulo 4G/LTE instalado?**  
Não. Esta placa ocupa o mesmo slot de expansão. Você precisará escolher entre conectividade celular ou funcionalidade KVM.

**P: O software é open source?**  
Sim! Nossos Apps **Openterface Connect** são totalmente open source e disponíveis em nosso [repositório GitHub](https://github.com/TechxArtisanStudio/Openterface_QT).
