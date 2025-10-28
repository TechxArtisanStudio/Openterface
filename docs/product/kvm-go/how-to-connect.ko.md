---
title: "연결 방법"
description: "Openterface KVM-Go 설정을 위한 단계별 가이드. 내장 비디오 커넥터를 사용하여 호스트 컴퓨터와 대상 장치를 연결하는 초간단 직접 플러그인 경험을 알아보세요."
keywords: "KVM-Go 설정, 초소형 KVM 설정, 내장 HDMI 연결, KVM 설치 가이드, 열쇠고리 KVM 설정, USB KVM 연결, 헤드리스 컴퓨터 설정, 휴대용 KVM 설정"
---

# **연결 방법** | 설정 가이드 | Openterface KVM-Go

## **연결 개요**

![KVM-Go 연결 개요](https://assets.openterface.com/images/kvm-go/step-0-overview.webp){:style="max-height:360px"}

위 이미지는 [**KVM-Go**](/product/kvm-go), 호스트 컴퓨터 및 대상 장치 간의 모든 연결을 보여줍니다.

- **호스트 컴퓨터**: [Openterface 앱](/app) 설치가 필요합니다.  
- **대상 장치**: 소프트웨어 및 사전 구성이 필요하지 않습니다.
- **비디오**: 내장 커넥터가 대상 장치에 직접 연결되므로 추가 비디오 케이블을 휴대하거나 관리할 필요가 없습니다.

## **연결에 필요한 것**

![KVM-Go 모든 부품](https://assets.openterface.com/images/kvm-go/step-0-all-parts.webp){:style="max-height:360px"}

**KVM-Go**를 설정하려면 다음 구성 요소가 필요합니다:

- **KVM-Go (HDMI / DP / VGA)** — **대상 장치**에 연결 (비디오 캡처용)  
- **검은색 짧은 USB-C 케이블** — **대상 장치**에 연결 (키보드 및 마우스 에뮬레이션용)
- **주황색 긴 USB-C 케이블** — **호스트 컴퓨터**에 연결 ([Openterface 앱](/app) 실행)

!!! note "케이블 길이 면책 조항"
    **공식 KVM-Go 패키지**에 포함된 정확한 케이블 길이는 **아직 확정되지 않았으며** 여기에 표시된 것과 약간 다를 수 있습니다.  
    이 가이드에서 사용된 케이블은 *클래식 Mini-KVM 툴킷*의 것이며 설명 목적으로만 사용됩니다.

!!! warning "자체 케이블 사용 시"
    자체 케이블을 사용하기로 선택한 경우 **고품질 데이터 전송 가능 USB 케이블**인지 확인하십시오. 저품질 또는 충전 전용 케이블은 다음과 같은 문제를 일으킬 수 있습니다:
    
    - 검은 화면 문제
    - 키보드 또는 마우스 입력 무응답
    - 간헐적 연결 끊김
    - 깜박이거나 불안정한 디스플레이 출력

## **단계별 설정**

### **1단계 — USB 케이블을 KVM-Go에 연결**
![USB 케이블 연결](https://assets.openterface.com/images/kvm-go/step-1-plugged.webp){:style="max-height:360px"}

- **검은색 USB-C 케이블** → KVM-Go 케이스에서 ![대상 아이콘](https://assets.openterface.com/images/shell-icons/target-computer.svg#only-light){:style="max-height:20px"} ![대상 아이콘](https://assets.openterface.com/images/shell-icons/target-computer_1.svg#only-dark){:style="max-height:20px"} **Target**으로 표시된 포트에 연결합니다.  
- **주황색 USB-C 케이블** → ![호스트 아이콘](https://assets.openterface.com/images/shell-icons/host-computer.svg#only-light){:style="max-height:20px"} ![호스트 아이콘](https://assets.openterface.com/images/shell-icons/host-computer_1.svg#only-dark){:style="max-height:20px"} **Host**로 표시된 포트에 연결합니다.

!!! warning
    두 USB-C 포트는 물리적으로 동일합니다.  
    혼동을 피하기 위해 항상 케이스 표면의 **라벨을 재확인**하십시오.

### **2단계 — 대상에 비디오 연결**
![HDMI 커넥터 연결](https://assets.openterface.com/images/kvm-go/step-3-hdmi-plugged.webp){:style="max-height:360px"}

**내장 수 비디오 커넥터**를 대상 장치의 비디오 출력 포트에 직접 연결합니다.

### **3단계 — 대상 USB 포트 연결**
**검은색 USB 케이블**을 대상 장치에 연결하여 HID 제어를 수행합니다.

- **옵션 A:** USB-A 포트에 직접 연결  
  ![대상 USB-A](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-b.webp){:style="max-height:360px"}

- **옵션 B:** USB-C 어댑터 사용  
  ![대상 USB-C](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-a.webp){:style="max-height:360px"}

!!! note "USB-C 연결 확인"
    일부 USB-C 포트는 안전한 연결을 제공하지 않을 수 있습니다. 간헐적인 키보드/마우스 제어 문제가 발생하면 어댑터 연결을 가볍게 흔들어 제대로 장착되고 접촉되었는지 확인하십시오.


### **4단계 — 호스트 USB 포트 연결**
**주황색 USB 케이블**을 호스트 컴퓨터에 연결합니다.

- USB-C 포트에 직접 연결 **또는** USB-C to USB-A 어댑터를 통해 연결.  
  ![호스트 USB 연결](https://assets.openterface.com/images/kvm-go/step-5-plug-in-host-computer-1.webp){:style="max-height:360px"}

