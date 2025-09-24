---
title: "대상 디바이스에 연결"
description: "Openterface KVM Extension for uConsole에 대상 디바이스를 연결하는 방법을 배우세요. 하드웨어 설치 및 소프트웨어 설정 후 USB 제어 및 비디오 입력 설정에 대한 완전한 가이드입니다."
keywords: "KVM 연결 설정, 대상 디바이스 연결, USB 제어 설정, HDMI 입력 설정, uConsole KVM 확장 연결"
---

# **대상 디바이스에 연결** | Openterface KVM Extension for uConsole

## 연결 개요

![extension-use-case-1a](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1a.webp){:style="height:480px"}

## 사전 요구사항

대상 디바이스를 연결하기 전에 다음이 완료되었는지 확인하세요:

1. [하드웨어 설치](/product/uconsole-kvm-extension/hardware-installation/) - KVM Extension 보드의 물리적 설치
2. [소프트웨어 설정](/product/uconsole-kvm-extension/software-setup/) - Openterface App 설치

## 연결 단계

### **USB 제어**
Type-C 암 포트를 대상 디바이스의 USB 포트에 연결하여 키보드와 마우스 신호를 에뮬레이션합니다.

### **비디오 입력**
대상 디바이스의 비디오 출력을 KVM Extension의 HDMI 포트에 연결합니다:

- HDMI 출력 디바이스의 경우 표준 HDMI 케이블 사용
- VGA 출력 디바이스의 경우 VGA-to-HDMI 변환 케이블 사용.
    - *참고*: 정상 작동을 위해 변환기가 USB 커넥터를 통해 전원이 공급되는지 확인하세요.
- 다른 비디오 신호 타입의 경우 적절한 다른 어댑터 사용

## 연결 테스트

1. 전원을 켜고 uConsole 부팅
2. Openterface QT app 실행
3. HDMI, 오디오 및 USB HID 기능을 테스트하여 정상 작동 확인
