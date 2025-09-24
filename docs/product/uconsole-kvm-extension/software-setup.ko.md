---
title: "소프트웨어 설정"
description: "Openterface KVM Extension for uConsole의 완전한 소프트웨어 설정 가이드입니다. 원활한 KVM 기능을 위해 uConsole에 Openterface App을 설치하고 구성하는 방법을 배워보세요."
keywords: "Openterface 앱 설치, uConsole 소프트웨어 설정, KVM 앱 설정, uConsole 앱 구성, 소프트웨어 설치 가이드"
---

# **소프트웨어 설정** | Openterface KVM Extension for uConsole

## 설치 개요

Openterface App은 uConsole이 KVM 인터페이스로 작동할 수 있게 하여 내장 화면, 키보드 및 트랙볼을 통해 대상 장치를 제어할 수 있습니다.

!!! note "요구사항"
    - **uConsole**: Openterface App 설치 필요
    - **대상 장치**: 앱 불필요 - Windows, macOS, Linux, Android, iOS 지원
    - **비디오**: 표준 HDMI 케이블을 사용하세요. 표준 HDMI 케이블을 사용하세요. 전원이 공급되는 HDMI 변환기를 사용하면 **VGA**, **DP** 등의 다른 형식도 지원합니다. *팁: 변환기가 적절히 전원 공급되는지 확인하세요. 그렇지 않으면 검은 화면이 나타날 수 있습니다.*

## 설치 방법

### **옵션 1: Flatpak 설치**

자세한 설정 단계는 [Flatpak 설치 가이드](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md)를 따르세요.

### **옵션 2: 커뮤니티 저장소 (권장)**

Rex가 유지 관리하는 커뮤니티 빌드를 선호하는 경우:

1. **저장소 추가**:
```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. **패키지 설치**:
```bash
sudo apt update
sudo apt install openterfaceqt
```

!!! warning "저장소 참고사항"
    이러한 명령은 sudo가 필요합니다. 저장소는 arm64 Bookworm 패키지를 대상으로 합니다. 설치 전에 장치와의 호환성을 확인하세요.

## 사용 지침

### **KVM 세션 시작**
1. uConsole에서 Openterface App 실행
2. 앱이 자동으로 KVM Extension 보드를 감지
3. HDMI를 통해 대상 장치 연결
4. uConsole의 내장 키보드와 트랙볼을 사용하여 대상 장치 제어

### **제어 기능**
- **키보드**: 멀티미디어 키를 포함한 전체 키보드 에뮬레이션
- **마우스**: 절대 및 상대 마우스 위치
- **오디오**: HDMI 오디오를 uConsole 스피커로 패스스루

### **고급 기능**
- **텍스트 전송**: 키 입력을 시뮬레이션하여 텍스트를 빠르게 전송—사용자명, 비밀번호, 코드 스니펫에 이상적
- **전환 가능한 USB**: 호스트 앱을 사용하여 uConsole과 대상 장치 간에 USB 액세스를 쉽게 전환
