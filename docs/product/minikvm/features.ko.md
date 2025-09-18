---
title: "기능 및 사양"
description: "Openterface Mini-KVM 완전 개요: BIOS 레벨 액세스, 4K 비디오 지원, 크로스 플랫폼 호환성, USB 공유 및 상세한 기술 사양을 포함한 강력한 기능. 이 헤드리스 컴퓨터 제어 솔루션에 대해 알아야 할 모든 것."
keywords: "Mini-KVM 기능, KVM 사양, BIOS 액세스, 헤드리스 제어, 4K KVM, USB 공유, 크로스 플랫폼 KVM, 텍스트 전송, 플러그 앤 플레이 KVM, 오픈 소스 KVM, 기술 사양"
---

# **기능 및 사양** | Openterface Mini-KVM

<iframe 
  width="560" 
  height="315" 
  src="https://www.youtube.com/embed/r3HNUflWGOY?si=84Ek6F9ocHmmGTqW" 
  title="YouTube video player" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
  referrerpolicy="strict-origin-when-cross-origin" 
  allowfullscreen>
</iframe>

## 핵심 기능

### **BIOS 레벨 액세스**

네트워크 의존성 없이 대상 디바이스의 BIOS, 펌웨어 및 시작 관리에 직접 액세스.

### **네트워크 독립성**

HDMI 비디오 캡처와 에뮬레이션된 키보드/마우스(HID) 입력을 사용한 안정적인 헤드리스 제어. 네트워크 연결 불필요.

### **고성능 비디오**

- **입력**: HDMI를 통해 최대 4K (3840×2160) @ 30Hz
- **출력**: 풀 HD (1920×1080) @ 30Hz, 140ms 미만 지연
- **압축**: YUV 및 MJPEG 지원
- **호환성**: 어댑터를 통한 VGA, DVI, Micro HDMI 지원

### **전환 가능한 USB 포트**

호스트와 대상 디바이스 간 USB 액세스를 전환하여 원활한 USB 드라이브 공유를 실현. [전환 가능한 USB 포트](../usb-switch) 페이지에서 자세히 알아보세요.

### **크로스 플랫폼 지원**

[호스트 앱](/app)이 macOS, Windows, Linux, Android와 호환되어 범용 통합을 실현.

### **텍스트 전송**

키스트로크를 시뮬레이션하여 텍스트를 쉽게 전송—사용자명, 비밀번호, 코드 스니펫에 완벽. 기호와 구두점을 포함한 ASCII 문자 지원.

!!! warning "텍스트 전송 제한사항" - **클립보드 통합 없음**: 타이핑만 에뮬레이션, 이미지나 문서 전송 불가 - **ASCII만**: ASCII 문자로 제한 (중국어, 일본어, 한국어 지원 없음) - **길이 고려사항**: 짧은 텍스트에 최적; 큰 블록은 성능 문제를 일으킬 수 있음

### **플러그 앤 플레이 편의성**

대상 디바이스에 소프트웨어 설치 불필요. 연결 즉시 제어 시작, 소프트웨어 흔적 없음.

### **오디오 통합**

완전한 멀티미디어 경험을 위한 HDMI 임베디드 오디오 패스스루.

### **확장 핀**

[확장 핀](../extension-pins)으로 특정 요구사항에 대한 고급 개발과 사용자 정의가 가능.

### **오픈 소스**

투명성과 [커뮤니티 혁신](/discord)을 위한 [완전 오픈 소스](/compliance) 하드웨어와 소프트웨어.

## 기술 사양

### **물리적 치수**

- **크기**: 61 × 53 × 13.5 mm (2.40 × 2.09 × 0.53 인치)
- **무게**: ~48g
- **재질**: 알루미늄 합금, PLA 케이싱

### **연결 및 전원**

- **전원**: USB-C 전원 공급 (외부 전원 공급 장치 불필요)
- **USB 속도**: 12Mbps 풀 스피드 전송
- **호스트 호환성**: Windows, macOS, Linux, Android
- **대상**: 소프트웨어 설치 불필요

### **비디오 및 오디오**

- **최대 입력**: 3840×2160@30Hz (HDMI)
- **최대 출력**: 1920×1080@30Hz
- **지연**: 140ms 미만
- **오디오**: HDMI 임베디드 오디오 패스스루

### **입력 기능**

- 완전한 키보드 및 마우스 에뮬레이션 (절대 및 상대)
- 멀티미디어 키 지원
- 사용자 정의 HID 기능
- 컴퓨터 웨이크업 기능

### **환경 조건**

- **작동**: 0°C ~ 40°C
- **보관**: -10°C ~ 50°C
- **습도**: 80% RH

## 제품 모델

- **베이직**: OP-MINIKVM-BASIC
- **툴킷**: OP-MINIKVM-TOOLKIT

## 문서 다운로드

- **[빠른 시작 가이드](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/minikvm_quick_start_guide_20240928.pdf)** (PDF)
- **[데이터시트 (영어)](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/Openterface-Mini-KVM-Basic-and-Toolkit-Datasheet-Eng-20250313.pdf)** (PDF)

![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front.svg#only-light){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back.svg#only-light){:style="max-height:260px"}
![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front_1.svg#only-dark){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back_1.svg#only-dark){:style="max-height:260px"}
