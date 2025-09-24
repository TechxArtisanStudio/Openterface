---
draft: false
date: 2024-07-16
description: "Openterface Mini-KVM 생산 업데이트: 성공적인 Teardown 2024 쇼케이스, OSHWA 인증 달성, 해킹 가능한 핀과 함께하는 하드웨어 V1.9 출시, 9월 배송 예정. 추가로 Raspberry Pi 호환성과 uConsole 통합!"
keywords: "Openterface Mini-KVM, Teardown 2024, OSHWA 인증, 하드웨어 V1.9, 생산 업데이트, Raspberry Pi 호환성, uConsole 통합, 오픈소스 하드웨어, CE 인증, RoHS 준수, 해킹 가능 하드웨어, USB KVM, 테크 생산, Crowd Supply 이벤트"
---

# Teardown에서 생산으로: 전진하고 있습니다!

안녕하세요, 여러분.

크라우드펀딩 캠페인이 끝난 지 꽤 시간이 지났고, 여러분과 공유할 환상적인 업데이트가 있습니다. Openterface Mini-KVM의 생산 단계에 본격적으로 뛰어들어 진행 상황을 알려드릴 수 있어서 기쁩니다.

## Teardown 2024 하이라이트

먼저, 지난 달 포틀랜드에서 [**Crowd Supply**](https://www.crowdsupply.com/teardown/portland-2024)가 주최한 [Teardown 2024](https://x.com/TechxArtisan/status/1810619822948090092)는 정말 놀라웠습니다. 데모 테이블에서 많은 테크 친구들과 후원자들을 직접 만날 수 있어서 정말 좋았습니다! 여러분의 따뜻한 말씀은 우리에게 큰 격려와 동기부여가 됩니다. 이벤트의 스냅샷들을 보세요:

![openterface-billy-at-teardown2024-2](https://www.crowdsupply.com/img/f0a2/16c34150-c59a-40d0-ab77-7c5dada8f0a2/openterface-billy-at-teardown2024-2_jpg_gallery-lg.jpg)

이벤트 중에 우리 제품을 특집으로 다뤄준 Electromaker에게 큰 감사를 표합니다! 이 비디오에서 우리의 채팅을 확인해보세요:

<iframe width="800" height="450" src="https://www.youtube.com/embed/K0EuMSQEwKo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## 생산이 본격화

현재 우리는 생산을 위해 CH9329와 CH340 같은 **부품과 칩 주문**에 바쁘게 일하고 있습니다. 또한 Mini-KVM과 케이블을 CE, RoHS, UKCA 인증 테스트에 제출하고 있습니다. 모든 것이 잘 진행되면 곧 공장에서 생산을 시작할 예정입니다. 우리 팀은 생산 라인의 모든 단계가 원활하게 진행되도록 보장하여 재미있고 신뢰할 수 있는 최고급 제품을 제공합니다! 오렌지 Type-C 케이블의 RoHS와 CE 테스트 보고서 스냅샷을 보세요:

![openterface-test-report-typec](https://www.crowdsupply.com/img/8d57/cd1d5f8e-820b-40c2-b758-1f075e2e8d57/openterface-test-report-typec_jpg_gallery-lg.jpg)

Mini-KVM과 다른 케이블들이 모두 필요한 인증 기준을 충족하도록 더 많은 유사한 보고서가 있을 예정이니 계속 지켜봐 주세요.

## OSHWA 인증

Openterface Mini-KVM이 이제 공식적으로 **OSHWA** 인증을 받아 완전히 오픈소스가 되었다고 발표할 수 있어서 정말 기쁩니다! 🥳 여기서 인증을 확인할 수 있습니다: [OSHWA UID CN000015](https://certification.oshwa.org/cn000015.html). 우리는 소프트웨어와 하드웨어 모두를 오픈소스로 유지하는 데 전념하여, 테크 애호가들이 USB KVM의 잠재력을 탐구하고, 그 개발에 기여하며, 함께 활기찬 커뮤니티를 구축할 수 있도록 합니다.

![openterface-oshw-cn000015](https://www.crowdsupply.com/img/925a/fbf33f8d-0c0d-405e-bb34-6e0038c9925a/openterface-oshw-cn000015_jpg_md-xl.jpg)

## 하드웨어 업데이트 V1.9

**추가 핀과 함께 하드웨어 V1.9를 출시했습니다: VCC, GND, Target D+, Target D-, Host D+, Host D-**로 더 많은 해킹 가능한 재미를! 이 데이터 핀들은 타겟과 호스트의 USB 허브에 연결되어 있습니다. 이제 Openterface를 위한 DIY 확장이 가능합니다—ATX, 네트워크 브리징, 오디오 바이패스 등을 생각해보세요. 이 핀들로 Mini-KVM을 해킹하는 창의적인 아이디어가 있으신가요? [Reddit](/reddit)이나 [Discord](/discord)에 참여하여 아이디어를 공유하고 우리와 함께 재미있게 코딩해보세요!

![openterface-v1-9-hackable](https://www.crowdsupply.com/img/caf8/7b5bb696-2342-487a-b0e8-aa137e6dcaf8/openterface-v1-9-hackable_jpg_md-xl.jpg)

## Pi에서 Openterface 실행 및 uConsole과 팀업

**Pi 환경에서 QT 호스트 앱 실행에 성공**했습니다! 더욱 흥미로운 것은 우리의 Mini-KVM이 Clockwork의 **uConsole**과 팀업하여 이를 휴대용 KVM 도구로 만드는 방법입니다. 근처의 헤드리스 디바이스에 대한 플러그 앤 플레이와 빠른 문제 해결에 매우 편리합니다.

<iframe width="800" height="450" src="https://www.youtube.com/embed/n7k_FwgM9kA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## 개발 및 최종 마무리

Kevin이 이끄는 개발 팀은 코드를 테스트하고 개선하기 위해 끊임없이 노력하고 있습니다. [Techxartisan의 Discord](/discord)에 참여하여 개발 및 베타 팀과 어울리고 진행 상황을 최신 상태로 유지하세요. 한편, Billy는 모든 서류 작업을 처리하고 제품, 패키징, 제품 매뉴얼의 디자인을 최종화하고 있습니다.

Billy가 일본 도쿄에서 [Kazubu의 트윗](https://x.com/_kazubu/status/1803442407800971612)으로 공유했을 때 보여준 알루미늄 케이스의 업데이트된 인쇄물과 라벨의 미리보기를 보세요:

![openterface-kazubu-tweet-new-look](https://www.crowdsupply.com/img/a680/71cdf2d7-27a3-4b93-8271-b3e82229a680/openterface-kazubu-tweet-new-look_jpg_md-xl.jpg)

## 9월 배송 예정

현재 정확히 일정에 맞춰 진행되고 있으며, 9월 말까지 Mini-KVM을 여러분의 손에 전달하기 위해 열심히 노력하고 있습니다.

Mini-KVM에 대한 소식을 퍼뜨리는 데 도움을 주시면 감사하겠습니다. 더 많은 테크 애호가들에게 도움이 되고, 헤드리스 디바이스를 관리하는 모든 사람의 테크 라이프를 더 쉽게 만들어주기를 바랍니다.

모든 지원과 열정에 정말 감사합니다. 여러분 없이는 할 수 없었습니다!

건배,  
Billy Wang  
Openterface 팀
