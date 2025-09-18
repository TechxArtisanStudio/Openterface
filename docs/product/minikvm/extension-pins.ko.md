---
title: "확장 핀"
description: "Openterface Mini-KVM의 확장 핀을 통해 맞춤 하드웨어 개발과 오픈 소스 프로젝트의 가능성을 탐색하세요."
keywords: "Mini-KVM 확장 핀, 커스텀 개발, 하드웨어 개조, 오픈 소스 KVM"
---

# **확장 핀** | 개발자 모드 | Openterface Mini-KVM

![mini-kvm-pins-port](https://assets.openterface.com/images/product/mini-kvm-pins-port.webp){:style="height:360px"}
![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="height:300px"}

Openterface Mini-KVM에는 고급 개발 및 [Open Software](/app) 실험을 위한 확장 핀이 제공됩니다. 이러한 핀은 기본 케이스 구성에서는 노출되지 않습니다.

## 핀에 접근하는 방법

1. 기기를 분해합니다.
2. 기본 케이스 커버를 전용 확장 핀 캡(Extension Pin Cap)으로 교체합니다.
3. 확장 핀 캡용 [3D 모델](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models)을 다운로드합니다.
4. 우리의 [Hardware GitHub 저장소](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware)를 확인하세요.

![change-cap](https://assets.openterface.com/images/product/change-cap.svg#only-light){:style="height:300px"}
![change-cap](https://assets.openterface.com/images/product/change-cap_1.svg#only-dark){:style="height:300px"}

!!! warning "보증 무효"
    기본 케이스를 제거하면 제품 보증이 무효가 될 수 있습니다. 모든 개조나 분해는 사용자 본인의 책임하에 진행됩니다.

!!! note "실험적 기능"
    이 핀을 사용하여 개발된 기능은 실험적이며 완전히 테스트되지 않았습니다. 확장 핀 노출 또는 기타 개조로 인한 손상, 부상, 오작동에 대해 Openterface는 책임을 지지 않습니다.

## 핀 구성

![target-side](https://assets.openterface.com/images/product/extension-pins-1.svg#only-light){:style="height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2.svg#only-light){:style="height:200px"}
![target-side](https://assets.openterface.com/images/product/extension-pins-1_1.svg#only-dark){:style="height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2_1.svg#only-dark){:style="height:200px"}

확장 핀은 다음 연결을 제공합니다:

1. 외부 구성 요소용 USB 5V 전원 공급
2. 호스트의 USB 허브로 연결되는 데이터 플러스
3. 호스트의 USB 허브로 연결되는 데이터 마이너스
4. 타깃의 USB 허브로 연결되는 데이터 플러스
5. 타깃의 USB 허브로 연결되는 데이터 마이너스
6. 접지 (GND)

!!! danger "잘못된 연결은 손상을 유발"
    VCC와 GND를 혼동하면 기기 및 연결된 구성 요소에 심각한 손상을 초래할 수 있습니다. 전원을 인가하기 전에 항상 핀 연결을 다시 확인하세요.

## 확장 핀 캡(Extension Pin Cap)

![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="height:360px"}

이 3D 프린트된 확장 핀 캡은 Openterface Mini-KVM의 기본 캡을 대체하여, 고급 사용자가 커스텀 개발을 위해 확장 핀을 노출하고 액세스할 수 있게 해줍니다. GitHub 저장소에서 3D 모델 파일을 다운로드하여 직접 인쇄할 수 있습니다.

- **사용**: 고급 하드웨어 개발을 위한 확장 핀 접근 제공
- **다운로드**: [3D 모델 파일](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models)

## 개발 참여

우리는 계속해서 개발과 실험을 진행하며, 이 핀으로 무엇을 할 수 있는지 및 창의적인 활용 방법에 대한 정보를 본 섹션에 업데이트할 예정입니다. 여러분의 창의성과 전문성은 Openterface Mini-KVM의 가능성을 넓히는 데 큰 도움이 됩니다. 다음과 같이 참여해 주세요:

1. **아이디어 공유**: 이 핀을 활용한 멋진 아이디어가 있으신가요? 듣고 싶습니다!
2. **DIY 프로젝트 기여**: 흥미로운 것을 만들었다면 우리 [Discord Openterface](/discord) 커뮤니티에 공유해 보세요.
3. **토론 참여**: 다른 개발자 및 열성 사용자들과 연결하여 함께 아이디어를 구상하고 협업하세요.

함께 만들고 혁신합시다!
