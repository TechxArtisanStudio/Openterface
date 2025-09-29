---
title: "하드웨어 설치"
description: "Openterface KVM Extension for uConsole의 단계별 하드웨어 설치 가이드입니다. 상세한 안전 가이드라인과 함께 uConsole의 확장 슬롯에 확장 보드를 올바르게 설치하는 방법을 배워보세요."
keywords: "KVM 확장 설치, uConsole 하드웨어 설정, 확장 보드 설치, uConsole 확장 슬롯, KVM 하드웨어 가이드, 물리적 설치"
---

# **하드웨어 설치** | Openterface KVM Extension for uConsole

## 개요
KVM Extension은 uConsole의 확장 슬롯에 있는 4G/LTE 모듈을 교체하여 직접 HDMI 입력과 USB HID 제어를 추가합니다.

## 필요한 것들
- 설치 전에 [포장 내용](whats-in-the-box.md)을 확인하세요  
- Openterface KVM Extension 보드  
- 제공된 **와셔** (안정적인 마운팅과 균등한 압력을 보장)  
- 육각 드라이버 (마운팅 스크류용)  
- ESD 보호 (손목 스트랩 또는 접지된 표면) — 권장  

## 설치 단계

### **1. 전원 차단**
uConsole을 종료하고 모든 전원과 케이블을 분리합니다.

### **2. 기존 모듈 제거**
육각 드라이버를 사용하여 두 개의 스크류를 제거합니다.  
스프링 접촉자를 구부리지 않도록 보드를 **곧바로 위로** 들어올립니다.

### **3. KVM Extension 설치**
- **와셔**를 스크류 포스트에 놓습니다.  
- KVM Extension을 확장 슬롯에 단단히 장착합니다.  
- 와셔는 약간 더 얇은 PCB(1.0 mm vs 1.2 mm)를 보상하여 적절한 스프링 접촉 압력을 유지합니다.

??? note "최종 설치 전에 맞춤 확인"
    먼저 **와셔 없이** 보드를 장착하여 맞춤을 테스트할 수 있습니다. 보드가 느슨하게 느껴지거나 접촉이 고르지 않다면, 와셔를 추가하고 보드를 다시 장착하세요. Openterface KVM Extension은 1.0 mm 두께로 원래 LTE 모듈(1.2 mm)보다 약간 얇습니다. 제공된 와셔를 사용하면 안정적인 마운팅과 신뢰할 수 있는 스프링 접촉을 보장합니다.  
    ![extension-slot-loose](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-slot-loose.webp){:style="max-height:220px"}

### **4. 보드 고정**
스크류를 다시 삽입하고 **부드럽게** 조입니다 — **과도하게 조이지 마세요**. 이는 보드를 손상시키거나 나사산을 망가뜨릴 수 있습니다.

![extension-screw-washer-installed](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installed.jpg){:style="max-height:220px"}
![extension-screw-washer-installing](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installing.jpg){:style="max-height:220px"}
![extension-install-1](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp){:style="max-height:220px"}

### **5. 설치 확인**
보드는 **평평하고 안정적**이어야 하며, 모든 패드에서 균등한 스프링 접촉이 있어야 합니다. 눈에 띄는 흔들림이나 움직임이 없어야 합니다.

### **6. 확장 슬롯 커버 설치**
KVM Extension 보드를 보호하고 uConsole의 원래 외관을 유지하기 위해 확장 슬롯 커버를 다시 설치합니다.

??? note "확장 슬롯 커버의 텍스트 방향"
    특정 각도에서 볼 때 확장 슬롯 커버의 텍스트가 "거꾸로" 보일 수 있습니다. 이는 의도적인 디자인입니다 - 텍스트는 uConsole을 들고 포트를 위에서 아래로 볼 때 읽을 수 있도록 방향이 설정되어 있으며, 이는 기기를 사용할 때의 자연스러운 시야 위치입니다.
    ![expansion-slot-text-orientation](https://assets.openterface.com/images/product/openterface-kvm-uconsole-expansion-slot-text-orientation.webp){:style="max-height:220px"}

---

**다음 단계**

1. [소프트웨어 설정](/product/uconsole-kvm-extension/software-setup/)으로 이동하여 Openterface App을 설치하세요.  
2. [대상 장치에 연결](/product/uconsole-kvm-extension/connect-to-target/)으로 이동하여 대상 장치를 연결하세요.  
3. [기능 및 사양](/product/uconsole-kvm-extension/features/)을 검토하여 상세한 기술 사양을 확인하세요.
