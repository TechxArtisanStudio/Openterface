---
title: "MicroSD 카드 전환 가이드"
description: "Openterface KVM-Go의 이중 하드웨어-소프트웨어 MicroSD 전환 시스템 사용 방법을 배웁니다. 4가지 작동 상태, LED 표시등, 안전 지침 및 파일 전송 기능을 이해합니다."
keywords: "MicroSD 전환, KVM 스위치, 하드웨어 스위치, 소프트웨어 스위치, MicroSD 카드 제어, KVM over USB, 파일 전송, USB 장치 관리, 컴퓨터 주변기기, MicroSD 전원 관리, LED 표시등"
---

# **MicroSD 카드 전환 가이드** | Openterface KVM-Go

**Openterface KVM-Go**는 호스트 컴퓨터와 대상 장치 간에 공유할 수 있는 단일 MicroSD 카드 슬롯을 포함하지만 동시에 둘 다 사용할 수는 없습니다.

이 디자인을 통해 카드를 물리적으로 제거하지 않고도 **파일 전송**을 위해 장치 간 빠르게 전환할 수 있어 워크플로우가 더 빠르고 효율적입니다. 일반 **MicroSD 카드 리더**로도 사용할 수 있습니다.

## **MicroSD 카드 설치**

![kvm-go-install-sd](https://assets.openterface.com/images/kvm-go/install-sd.webp){:style="max-height:260px;width:auto"}

!!! note "올바른 MicroSD 카드 설치"
    MicroSD 카드를 **딸깍** 소리가 날 때까지 단단히 삽입하여 안전하게 장착되고 잠겼음을 확인하십시오.

## **제어 방법**

KVM-Go는 호스트와 대상 간에 MicroSD 카드를 전환하는 두 가지 방법을 제공합니다:

- **하드웨어 버튼** — 수동 제어를 위한 장치의 물리적 버튼.  
- **소프트웨어 스위치** — 즉시 전환을 위한 호스트 앱 내의 토글 버튼.


## **스위치 버튼 및 LED 표시등** 

![kvm-go-led-indicator](https://assets.openterface.com/images/kvm-go/led-indicator.webp){:style="max-height:260px;width:auto"}

**이중 컬러 LED 표시등**은 현재 MicroSD 연결 상태를 표시합니다*（참고: 개발 중/변경 가능）*:

- **🔵 파란색 LED 켜짐** — MicroSD 카드가 **대상 장치**에 마운트됨  
- **🟢 초록색 LED 켜짐** — MicroSD 카드가 **호스트 컴퓨터**에 마운트됨  
- **LED 꺼짐** — MicroSD 카드가 삽입되지 않았거나 장치 전원이 꺼짐  
- **LED 깜박임** — 데이터 전송 진행 중(읽기/쓰기 활동)

!!! note "자동 마운트 기능(실험적)"
    기본적으로 장치가 처음 전원이 켜지면 MicroSD 카드는 **호스트**에 마운트됩니다.  
    향후 실험적 기능을 통해 먼저 연결되는 쪽(호스트 또는 대상)으로 **자동 마운트**가 가능해져 더욱 원활한 경험을 제공합니다.


