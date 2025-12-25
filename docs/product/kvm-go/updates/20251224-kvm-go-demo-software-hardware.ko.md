---
draft: false
date: 2025-12-24
title: "새로운 데모 영상, 소프트웨어 진행 상황 및 KVM-GO 내부 구성"
description: "KVM-GO의 HDMI/DP/VGA 버전이 실제로 어떻게 작동하는지 보여주는 새로운 데모 영상을 확인해보세요. Mini-KVM과 KVM-GO를 위한 통합 소프트웨어, MS2130S 4K@60Hz 비디오 프로세서 및 CH32V208 MCU를 포함한 하드웨어 업그레이드, 그리고 커스텀 EDID 지원과 같은 예정 기능에 대해 알아보세요. 캠페인 업데이트: 220명 이상의 후원자와 함께 $72k 달성"
keywords: "KVM-GO 데모 영상, KVM-GO 소프트웨어 업데이트, KVM-GO 하드웨어 업그레이드, MS2130S 비디오 프로세서, CH32V208 MCU, 4K@60Hz KVM, KVM-GO vs Mini-KVM, 통합 Openterface 앱, KVM-GO 키보드 마우스 성능, 커스텀 EDID 지원, KVM-GO 스크립트 제어, OSHWA 인증, KVM-GO 크라우드펀딩, Crowd Supply KVM-GO, Openterface KVM-GO, TechxArtisan, KVM-over-USB 하드웨어 비교"
author: "TechxArtisan Studio"
category: "제품 업데이트"
tags: ["KVM-GO", "제품 업데이트", "소프트웨어", "하드웨어", "데모 영상", "크라우드펀딩", "기술적 심층 분석"]
featured: true
social:
  image: "https://assets.openterface.com/images/blog/Gemini_Generated_Image_kvm-go.webp"
  title: "새로운 데모 영상, 소프트웨어 진행 상황 및 KVM-GO 내부 구성"
  description: "KVM-GO의 실제 사용 모습을 확인하고, 통합 소프트웨어 업데이트에 대해 알아보세요. 그리고 우리 다음 세대 KVM-over-USB 장치를 구동하는 하드웨어 업그레이드에 대해 알아보세요."
---

# 새로운 데모 영상, 소프트웨어 진행 상황 및 KVM-GO 내부 구성

안녕하세요, 모두! 조용한 기간에 대해 죄송합니다. 우리는 KVM-GO의 하드웨어와 소프트웨어를 다듬는 데 집중했고, 시간이 정말 빠르게 지나갔습니다. 12월 말 기준, 우리는 **220명 이상의 후원자와 함께 $72k**를 달성했으며, 이는 매우 인상 깊은 일입니다. 우리를 더 많이 돕고 싶으시다면, **소문을 퍼뜨려 주세요!**

여러분의 인내심과 지원에 진심으로 감사드립니다. 네, 크리스마스는 분명히 혼란을 더했습니다 🙂🎄 이제 업데이트를 확인해 보겠습니다.

![blog-Gemini_Generated_Image_kvm-go](https://assets.openterface.com/images/blog/Gemini_Generated_Image_kvm-go.webp)
*Nano Banana를 사용해 실제 KVM-GO 제품 사진을 기반으로 생성한 연말 테마 이미지.*

## 새로운 데모 영상: KVM-GO 실제 사용 모습

우리가 [**새로운 데모 영상**](https://www.youtube.com/watch?v=459rWCQbJRE)을 출시했는데, KVM-GO가 실제 환경에서 어떻게 작동하는지 보여줍니다.


영상에서는 다음과 같은 내용을 확인할 수 있습니다:

* KVM-GO의 **HDMI / DP / VGA** 버전 실제 사용 모습
* 박스에 포함된 **내용물**
* 다양한 대상 장치를 제어하는 방법
* KVM-GO가 실제 워크플로우에 어떻게 적합하게 들어맞는지

더 가벼운, 손으로 직접 테스트하고 실제 사용 사례에 관심이 있으신 분들은 우리 [소셜 미디어](https://openterface.com/about/community/)도 확인해 주세요. 우리는 KVM-GO가 실제 기술 전선에서 어떻게 작동하는지 보여주는 원시 테스트 클립과 실용적인 시나리오를 자주 공유합니다.

## 소프트웨어 진행 상황: Mini-KVM과 KVM-GO를 위한 하나의 앱

소프트웨어 측면에서는 단단한 한 걸음을 내딛었습니다.

최신 업데이트로 인해 **Mini-KVM과 KVM-GO 시리즈 모두와 호환되는 동일한 Openterface 앱**을 사용할 수 있게 되었습니다. 사용자에게는 다음과 같은 이점이 있습니다:

* 제품 간 일관된 경험
* 하나 이상의 Openterface 장치를 사용하는 경우, 분할이 줄어듭니다

우리는 또한 키보드 및 마우스 성능을 개선하는 데 시간을 할애했으며, 특히 다음과 같은 점에 초점을 맞췄습니다:

* 전체 지연 시간 감소
* 연결 상태 및 신호 품질의 더 나은 감지 포함, 입력 처리 안정성 증가
* 빠른 반응 시간, 특히 빠르거나 지속적인 상호작용 시

우리의 KVM 솔루션은 게임이 주요 사용 사례가 아니지만, 실제 시나리오에서 입력 반응성을 매우 중요하게 생각합니다. 기술적 세부 사항에 대해 더 알고 싶으시다면, 특히 macOS에서, 우리는 최근 이에 대한 심층 분석을 여기 게시했습니다:
👉 **[Openterface Mini-KVM 마우스 속도 및 macOS에서의 게임 성능](https://openterface.com/app/updates/20251218-macos-mouse-speed/)**

그 기사에서 논의된 많은 개선 사항이 이제 Mini-KVM과 KVM-GO를 위한 통합 소프트웨어 스택에 직접적으로 반영되고 있습니다.

## KVM-GO의 핵심 하드웨어 업그레이드 (Mini-KVM과 비교)

내부 구조에 관심이 있으신 분들을 위해, Mini-KVM에서 KVM-GO로의 핵심 하드웨어 변경 사항을 간단히 비교합니다.

### 비디오 파이프라인 업그레이드

| 항목           | **MS2109 (Mini-KVM)**    | **MS2130S (KVM-GO)** | 개선 사항           |
| ---------------- | ------------------------ | -------------------- | --------------------- |
| HDMI 입력       | 4K @ 30Hz                | 4K @ 60Hz            | 입력 대역폭 2배 증가 |
| USB 비디오 출력 | 1080p @ 30Hz             | 4K @ 60Hz            | 픽셀 처리량 4배 증가 |
| 내부 스케일링   | 4K → 1080p               | 네이티브 4K            | 강제 다운스케일 없음 |
| 프레임 지연     | 높음 (스케일러 + 버퍼)   | 낮음 (직접 경로)      | 지연 시간 감소       |

### USB 키보드 및 마우스 에뮬레이션 업그레이드

| 항목             | **CH340 + CH9329 (Mini-KVM)** | **CH32V208 (KVM-GO)** | 개선 사항     |
| ------------------ | ----------------------------- | --------------------- | --------------- |
| 칩 수             | 2개                           | 단일 MCU              | 더 간단한 시스템 |
| USB 처리          | USB–Serial 브리지             | 네이티브 USB 장치     | 지연 시간 감소 |
| HID 생성          | 고정 기능                      | 펌웨어 정의           | 완전한 제어    |
| 데이터 경로        | USB → UART → HID              | USB → HID             | 한 단계 제거   |
| BIOS 호환성       | 혼합                          | 우수                  | 더 신뢰성 있음 |

## 개발 중인 고급 기능

최종 KVM-GO 펌웨어에 대한 여러 고급 기능이 계획되고 있으며, 현재 활발히 개발 중입니다. 간단한 미리보기:

* **커스텀 EDID 지원**으로 디스플레이 호환성 문제를 해결
* **스크립트 기반 제어**로 자동화 및 고급 워크플로우를 위한

이러한 기능들이 성숙해질수록 더 많은 세부 사항을 공유할 예정입니다.

## 오픈소스 약속 (언제나)

네, **KVM-GO는 완전히 오픈소스로 유지될 것입니다**.

대량 생산을 위한 하드웨어 설계가 완료되면, 우리는 **OSHWA (오픈소스 하드웨어 협회) 인증**을 신청할 예정입니다.

모든 하드웨어 설계 파일 및 STL 모델은 여기에 게시될 예정입니다:
👉 [https://github.com/TechxArtisanStudio/Openterface_KVM-GO_Hardware](https://github.com/TechxArtisanStudio/Openterface_KVM-GO_Hardware)

투명성과 커뮤니티 협력은 우리가 하는 일의 핵심입니다.

## 캠페인 최종일: 친절한 напоминание

우리는 이제 **캠페인의 최종일**에 접어들었습니다.

크라우드펀딩은 **KVM-GO를 가장 낮은 가격으로 구매할 수 있는 최고의 기회**입니다. 캠페인 종료 후, 우리는 사후 크라우드펀딩 주문으로 이동하게 되며, 가격이 상승할 것입니다.

고민 중이셨다면, 지금이 바로 때입니다.

👉 **캠페인을 지원하고 Crowd Supply에서 KVM-GO 단위를 확보하세요:**
[https://www.crowdsupply.com/techxartisan/openterface-kvm-go](https://www.crowdsupply.com/techxartisan/openter:
[https://www.crowdsupply.com/techxartisan/openterface-kvm-go](https://www.crowdsupply.com/techxartisan/openterface-kvm-go)

다시 한 번, 여러분의 인내심, 신뢰 및 지원에 감사드립니다. 더 많은 업데이트가 곧 올 예정이며, 다시 조용히 있지 않도록 노력하겠습니다. 우리 모두로부터 따뜻한 연말 축하 인사를 드립니다!

**Openterface 팀 | TechxArtisan**