---
draft: false
category: "USB KVM DIY Contest 2024"
date: 2025-05-20
description: "Openterface Mini-KVM을 위한Veera Pendyala의 혁신적인Audio Bridge 개념을 발견하세요. 이는 양방향 오디오 통신과AI 워크플로우를 가능하게 합니다. 이NVIDIA 엔지니어의 비전은USB 오디오 동글, Jetson Nano, KVM 기술을 결합하여 대화형AI와홈 자동화를 위한제로 인프라 솔루션을만듭니다."
keywords: "Audio Bridge, 양방향 오디오, USB KVM, Jetson Nano, NVIDIA 엔지니어, 대화형AI, 홈 자동화, USB 오디오 동글, ALSA, PulseAudio, 헤드리스 디바이스, 원격 제어, AI 워크플로우, USB 사운드 어댑터, 오디오 라우팅, Mini-KVM, USB-KVM DIY 챌린지, 제로 인프라, 오디오 스트리밍, 디바이스 제어, USB 인터페이스, HDMI 오디오, 원격 지원, 홈 모니터링, AI 추론, 소프트웨어 엔지니어링, 하드웨어 통합, 오디오 캡처, 마이크 라우팅, Jetson 구동AI, USB gadget 모드"
---

# Audio Bridge 개념: 양방향 사운드와AI 워크플로우 영감

Veera Pendyala의"Audio Bridge"개념은실제 실험을통해입증되어Mini-KVM에서양방향 오디오와Jetson 구동AI에대한선견지명이있는아이디어를자극했습니다. 15년 이상의소프트웨어 엔지니어링 경험을가진NVIDIA의시니어 소프트웨어 엔지니어로서, Veera는비전을탐구했습니다: 호스트↔타겟 오디오, 대화형AI, 홈 자동화 워크플로우를USB KVM에가져오는것입니다.

Veera Pendyala는USB-KVM DIY 챌린지2024에선견지명이있는아이디어를가져왔습니다. Openterface Mini-KVM으로양방향 오디오를가능하게하는그의개념은특히Jetson Nano와같은싱글 보드 컴퓨터에대해원격 제어와AI 구동 애플리케이션을향상시키는것을목표로합니다. Veera의USB 오디오 동글 실험과그의인터뷰는홈 자동화와대화형AI 워크플로우에서오디오 브리징의잠재력에대한영감을주는토론을자극했습니다.

![Billy와Kevin과오디오 브리지 아이디어를논의하는Veera](https://assets.openterface.com/images/blog/Veera-audio-bridge-chat-with-veera.webp)

## 도전

-   **단방향 사운드**
    Mini-KVM의HDMI는_타겟→호스트_오디오만스트리밍하며, 호스트마이크가원격 디바이스에도달하는경로가없습니다

-   **제로 인프라 목표**
    모든솔루션은인터넷, 외부전원, 또는부피가큰추가장비없이실행되어야합니다

-   **AI와자동화 사용사례**
    Veera는대화형AI, 원격지원, 홈모니터링 시나리오를위해헤드리스 디바이스에라이브 음성을상상합니다

## 제안된브리지 아키텍처

1. **듀얼USB 사운드 어댑터**

    - **호스트측 동글**은로컬마이크/오디오를캡처
    - **타겟측 동글**은해당오디오를원격머신의마이크잭에주입

2. **오디오 라우터로서의Jetson Nano**

    - 두동글간매핑을위해ALSA/PulseAudio 실행
    - KVM 제어와잠재적AI 추론을위해OpenterfaceQT 호스팅

3. **비디오와제어를위한Mini-KVM**
    - HDMI는비디오와타겟오디오를호스트로전달
    - 단일USB 링크가키보드/마우스와(미래의)오디오 채널을처리
4. **소프트웨어 채널 매핑**
    - 여러USB 인터페이스를노출하기위해OpenterfaceQT 확장제안
    - KVM 스트림과함께호스트마이크→타겟라우팅을활성화하는UI 토글

## 영향과커뮤니티

Veera의실험은Mini-KVM 생태계에오디오를추가함으로써잠금해제를기다리고있는사용사례의폭을강조합니다. 그의개념은AI 구동워크플로우, 홈자동화, 더풍부한원격IT 경험을위한우리의로드맵과밀접하게일치합니다.

그의비전을공유하고우리의차세대Mini-KVM 기능에영감을준Veera Pendyala에게특별한감사를표합니다. USB-KVM DIY 챌린지2024 페이지에서다른참가작에대해더알아보고탐색하세요:

-   [Crowd Supply 챌린지](https://www.crowdsupply.com/techxartisan/usb-kvm-diy-challenge-2024)

Openterface Mini-KVM과대회의훌륭한아이디어에대해더알아보기위해Helen Leigh, Billy R.B. Wang, Kevin Peng와의Crowd Supply Teardown YouTube 스트리밍토크에참여하세요:
[https://youtu.be/Tp4f_uxEo6E](https://youtu.be/Tp4f_uxEo6E)
