---
title: "기능 및 사양"
description: "Openterface KVM Extension for uConsole의 완전한 개요: 직접 HDMI 입력, USB HID 제어, 완벽한 폼 팩터, 상세한 기술 사양을 포함한 강력한 기능. 이 휴대용 KVM 솔루션에 대해 알아야 할 모든 것."
keywords: "KVM 확장 기능, uConsole KVM, HDMI KVM, USB HID 제어, 휴대용 KVM, headless 제어, 4G LTE 교체, 기술 사양, uConsole 확장"
---

# **기능 및 사양** | Openterface KVM Extension for uConsole

![PCB-front](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:320px"}
![PCB-Back](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:320px"}

## 핵심 기능

- **직접 HDMI + USB HID**: uConsole의 내장 화면과 컨트롤을 활용하여 직접 HDMI 입력과 USB HID 에뮬레이션을 제공합니다.
- **플러그 앤 플레이**: 소프트웨어 설치나 대상 장치에 흔적을 남기지 않고 즉시 제어합니다.
- **낮은 지연시간**: BIOS 수준 문제 해결과 실시간 상호 작용에 최적화되었습니다.
- **휴대용**: 올인원 모바일 도구—추가 모니터, 키보드 또는 네트워크 설정이 필요하지 않습니다.
- **네트워크 불필요**: HDMI 캡처와 HID 입력을 통한 안정적인 headless 제어, 네트워크가 필요하지 않습니다.
- **텍스트 전송**: 키 입력을 시뮬레이션하여 텍스트를 빠르게 전송—사용자명, 비밀번호, 코드 스니펫에 이상적입니다. 기호와 구두점을 포함한 전체 ASCII를 지원합니다. [앱을 확인하세요](/app) 자세한 내용은.
- **오픈 소스**: 활발한 커뮤니티 지원과 함께 [Openterface KVM QT](https://github.com/techxArtisanStudio/openterface_qt)를 기반으로 구축되었습니다.

## 기술 사양

### 물리적 치수

- **크기**: 37 × 77 mm (4G/LTE 모듈과 일치)
- **두께**: 1.0 mm (원본 4G/LTE 모듈의 1.2 mm보다 얇음)
- **재질**: 스프링 접촉자가 있는 고품질 PCB

### 전체 키보드 및 마우스 에뮬레이션

- **USB HID**: 절대 및 상대 마우스 위치, 전체 키보드 지원, 멀티미디어 키.
- **연결**: 확장 보드의 Type-C 암 포트를 통해 대상에 USB 링크.

### 비디오 및 오디오

- **입력**: HDMI를 통해 최대 4K (3840×2160) @ 30Hz
- **출력**: 140ms 미만의 지연시간으로 풀 HD (1920×1080) @ 30Hz
- **디스플레이**: uConsole의 내장 화면 사용
- **압축**: YUV 및 MJPEG 지원
- **호환성**: VGA, DVI, Micro HDMI (어댑터를 통해)
- **오디오**: HDMI 임베디드 오디오 패스스루

### 전환 가능한 USB 2.0 포트

- **공유 포트**: 호스트 앱을 사용하여 uConsole과 대상 장치(예: 플래시 드라이브) 간에 USB 액세스를 쉽게 전환합니다.
- **USB 속도**: 12Mbps 풀 스피드 전송

### 연결성 및 전원

- **전원**: uConsole의 확장 슬롯에서 직접 전력을 공급받습니다 (외부 공급 장치 불필요)
- **대상 호환성**: Windows, macOS, Linux, Android, iOS
- **대상 소프트웨어**: 설치 불필요
