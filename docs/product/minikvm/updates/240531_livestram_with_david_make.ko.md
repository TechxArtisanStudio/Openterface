---
draft: false
date: 2024-05-31
description: "MAKE: Magazine의 David Groom과의 라이브스트림을 시청하세요. 우리는 Openterface Mini-KVM의 기원 스토리에 대해 논의했습니다. 기술 예술 프로젝트부터 커뮤니티 주도 개발, 그리고 헤드리스 디바이스 관리를 위한 오픈소스 솔루션을 만드는 여정까지 다뤘습니다."
keywords: "Openterface Mini-KVM, MAKE Magazine, David Groom, 기술 예술 프로젝트, 오픈소스 하드웨어, 헤드리스 컴퓨터 제어, Raspberry Pi 관리, TechxArtisan 스튜디오, 메이커 커뮤니티, 크라우드펀딩 캠페인, DIY 전자제품, 하드웨어 개발, 라이브스트림 인터뷰"
---

# MAKE: Magazine의 David Groom과의 캐주얼 채팅: Openterface Mini-KVM의 스토리

안녕하세요, 여러분!

MAKE: Magazine의 David Groom과 함께 멋진 [YouTube 라이브스트림](https://www.youtube.com/live/lwitzvmxsgc?si=s9a1t5_Sce5v22e1)을 마무리했습니다! 세션 동안 우리는 Openterface Mini-KVM의 배경 스토리에 대해 깊이 있게 다뤘습니다. 이는 노트북만으로 Raspberry Pi와 같은 헤드리스 디바이스와 싱글보드 컴퓨터를 쉽게 제어하도록 설계된 혁신적인 오픈소스 하드웨어 솔루션입니다. 자세한 내용은 YouTube 라이브스트림을 확인하시거나 아래 스토리를 읽어보세요.

![youtube-with-david-2](https://www.crowdsupply.com/img/2b83/081f1376-b266-4e83-b1af-5628dbe62b83/youtube-with-david_jpg_gallery-lg.jpg)

## 아이디어의 탄생

Mini-KVM의 여정은 중국 광저우의 번화한 도시에 있는 TechxArtisan 스튜디오에서 시작되었습니다. 지난 5년 동안 우리는 지역 및 국제 아티스트들을 위한 수많은 기술 예술 프로젝트에 깊이 관여해왔습니다. 우리의 작업에는 AI 감지를 갖춘 인터랙티브 조명 설치, 연극 공연을 위한 로봇 팔, 무작위 미로를 해결하는 자율주행 미니카, 그리고 사막과 숲과 같은 무인지대를 탐험하도록 설계된 로봇 개까지 포함됩니다.

![techxartisan_tech_art](https://www.crowdsupply.com/img/bce8/9c580077-993a-42b2-b781-a30d34acbce8/techxartisan-tech-art_jpg_gallery-lg.jpg)

### 공통적인 골칫거리
우리 작업에서 반복적으로 발생하는 도전은 Raspberry Pi와 Jetson Nano와 같은 수많은 헤드리스 컴퓨터를 관리하는 것이었습니다. 이들은 모니터, 키보드 또는 네트워크 연결이 부족하여 가혹한 조건에서 이러한 디바이스를 문제 해결하고 접근하기 위해 예비 모니터와 키보드를 찾아다니는 일이 자주 발생했습니다.

### 임시 해결책
처음에는 배터리 팩으로 구동되고 터치패드가 있는 무선 미니 키보드와 결합된 임시 휴대용 모니터 솔루션에 의존했습니다. 그러나 이것들은 종종 잊어버리거나 분실되어, 코딩과 설정을 위해 항상 가지고 다니는 노트북을 활용할 수 있는 전용 하드웨어 솔루션의 필요성이 생겼습니다.

![diy-monitor-keyboard](https://www.crowdsupply.com/img/2efd/4459eff9-2d01-4552-ac91-a1941ed82efd/diy-monitor-keyboard_jpg_gallery-lg.jpg)
*현장 프로젝트에서는 이 두 가젯을 반드시 휴대해야 합니다.*

### 첫 번째 프로토타입
우리의 첫 번째 DIY 프로토타입은 헤드리스 디바이스에서 비디오를 가져오는 캡처 카드와 USB 키보드/마우스 시뮬레이터의 조합으로, 단순하면서도 효과적이었습니다. 이 모든 것이 노트북에 연결하는 단일 USB 케이블에 통합되어 있었습니다.

![/early-mini-kvm-pcb](https://www.crowdsupply.com/img/1f7e/fb91d879-dee7-45cc-bbdc-dc3ea5731f7e/early-mini-kvm-pcb_jpg_gallery-lg.jpg)
*mini-KVM PCB의 초기 버전 중 하나*

2023년 11월 선전 메이커 페어에서 우리의 멋진 기술 예술 프로젝트를 전시했고, David에게 mini-KVM 프로토타입을 보여주려고 했습니다. 하지만 David의 선물에 너무 흥분해서 그것을 잊어버렸습니다!

![techxartisan_team_with_david_groom](https://www.crowdsupply.com/img/bc4e/17bdcc6e-0a34-4f2f-bf64-fee0b8d6bc4e/techxartisan-team-with-david-groom_jpg_gallery-lg.jpg)
*MAKE: Magazine의 스티커와 엽서는 정말 멋집니다!*

## 커뮤니티 피드백과 개발
Reddit에서 우리의 프로토타입을 공유한 후, [커뮤니티](/community/)로부터 귀중한 피드백을 받았고, 솔루션을 개선하고 완성된 제품으로 개발하도록 격려받았습니다. 이 커뮤니티 지원은 우리의 임시 장치를 홈랩러, 시스템 관리자, 기술 애호가, 그리고 헤드리스 컴퓨터를 다루는 모든 사람을 위한 세련되고 효율적인 도구로 변환하는 데 필수적이었습니다.

![got_feedback_from_reddit](https://www.crowdsupply.com/img/b24b/e04dfa15-1e5b-4bfb-b97c-acdba784b24b/got-feedback-from-reddit_jpg_gallery-lg.jpg)
*홈랩러들로부터 엄청난 양의 피드백을 받았습니다*

## 의구심 극복
기존의 유사한 솔루션과 경쟁하는 것에 대한 초기 의구심에도 불구하고, 온라인 커뮤니티의 긍정적인 반응과 건설적인 제안은 잠재적인 사용 사례를 명확히 하고 우리의 자신감을 높였습니다. 이러한 지원과 우리의 노력에 대한 확신이 없다면, 프로젝트를 더 진행하지 않았을 수도 있습니다.

## 크라우드펀딩과 미래 계획
Crowd Supply에서의 Openterface Mini-KVM 크라우드펀딩 캠페인이 본격적으로 진행되고 있으며, 약 2주 정도 남았습니다. 이 캠페인은 단순히 Mini-KVM을 개발하는 것만이 아닙니다. 커뮤니티 주도 혁신의 힘을 증명하는 것입니다. 다음으로 우리는 생산 관리, 소프트웨어 개선, 그리고 이 편리한 가젯을 우리의 멋진 백커들에게 전달하는 것에 집중할 것입니다—모든 것이 우리의 놀라운 오픈소스 커뮤니티에 의해 추진됩니다.

![techxartisan_openterface_discord](https://www.crowdsupply.com/img/8d7a/58e213e7-7a81-47b4-9d6b-69be3c698d7a/techxartisan-openterface-discord_jpg_gallery-lg.jpg)
*베타 테스터들이 TechxArtisan의 Discord에서 일상적인 기술 작업에서 Openterface Mini-KVM 사용을 공유하고 있습니다*

## 오픈소스 비전 수용

Openterface Mini-KVM은 우리의 창의성과 인내, 그리고 지원적인 오픈소스 커뮤니티의 증거입니다. 우리의 개인적인 도전에 대한 단순한 솔루션으로 시작된 것이 전 세계의 해커, 틴커러, 기술 애호가들에게 이익이 될 다재다능한 오픈소스 도구로 진화했습니다. Mini-KVM이 공식 출시에 가까워지면서 더 많은 업데이트를 기대해 주세요!
