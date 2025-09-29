---
title: "Pinos de extensão"
description: "Explore o potencial dos pinos de extensão do Openterface Mini-KVM para desenvolvimento de hardware personalizado e projetos de código aberto."
keywords: "Mini-KVM pinos de extensão, desenvolvimento personalizado, modificação de hardware, KVM de código aberto"
---

# **Pinos de extensão** | Modo desenvolvedor | Openterface Mini-KVM

![mini-kvm-pins-port](https://assets.openterface.com/images/product/mini-kvm-pins-port.webp){:style="max-height:360px"}
![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="max-height:300px"}

O Openterface Mini-KVM possui pinos de extensão para desenvolvimento avançado e experimentação com [Open Software](/app). Esses pinos não ficam expostos na configuração padrão da carcaça.

## Como acessar os pinos

1. Desmonte o dispositivo.
2. Substitua a tampa original da carcaça por uma tampa especializada (Extension Pin Cap).
3. Baixe o [modelo 3D](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models) da Extension Pin Cap.
4. Consulte nosso [repositório de hardware no GitHub](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware).

![change-cap](https://assets.openterface.com/images/product/change-cap.svg#only-light){:style="max-height:300px"}
![change-cap](https://assets.openterface.com/images/product/change-cap_1.svg#only-dark){:style="max-height:300px"}

!!! warning "Garantia anulada"
    Remover a carcaça original pode anular a garantia do produto. Qualquer modificação ou desmontagem é realizada por conta e risco do usuário.

!!! note "Recursos experimentais"
    Os recursos desenvolvidos usando esses pinos são experimentais e não foram totalmente testados. A Openterface não se responsabiliza por quaisquer danos, lesões ou mau funcionamento resultantes de modificações, exposição dos pinos de extensão ou outras alterações no dispositivo.

## Configuração dos pinos

![target-side](https://assets.openterface.com/images/product/extension-pins-1.svg#only-light){:style="max-height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2.svg#only-light){:style="max-height:200px"}
![target-side](https://assets.openterface.com/images/product/extension-pins-1_1.svg#only-dark){:style="max-height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2_1.svg#only-dark){:style="max-height:200px"}

Os pinos de extensão fornecem as seguintes conexões:

1. Alimentação USB 5 V para componentes externos
2. Dados positivos para o hub USB do host
3. Dados negativos para o hub USB do host
4. Dados positivos para o hub USB do target
5. Dados negativos para o hub USB do target
6. Terra (GND)

!!! danger "Conexões incorretas causam danos"
    Confundir VCC e GND pode causar danos graves ao dispositivo e aos componentes conectados. Sempre verifique as conexões dos pinos antes de ligar o dispositivo.

## Extension Pin Cap

![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="max-height:360px"}

Esta tampa de pinos de extensão impressa em 3D substitui a tampa original do Openterface Mini-KVM, permitindo que usuários avançados exponham e acessem os pinos de extensão para desenvolvimento personalizado. Você pode baixar os arquivos do modelo 3D no nosso repositório do GitHub e imprimir a tampa por conta própria.

- **Uso**: oferece acesso aos pinos de extensão para desenvolvimento de hardware avançado.
- **Download**: [Arquivos do modelo 3D](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models)

## Envolva-se no desenvolvimento

À medida que continuamos a desenvolver e experimentar, atualizaremos esta seção com mais informações sobre o que esses pinos podem fazer e como podem ser utilizados de forma criativa. Sua criatividade e experiência podem ajudar a ampliar os limites do que é possível com o Openterface Mini-KVM. Participe:

1. **Compartilhe suas ideias**: tem um conceito interessante para usar esses pinos? Queremos ouvir!
2. **Contribua com projetos DIY**: se você criou algo interessante, considere compartilhar na nossa comunidade [Discord Openterface](/discord).
3. **Junte-se à discussão**: conecte-se com outros desenvolvedores e entusiastas para fazer brainstorming e colaborar.

Vamos construir e inovar juntos!
