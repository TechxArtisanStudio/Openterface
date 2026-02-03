---
title: Openterface KeyMod 자주 묻는 질문
description: KeyMod에 대한 자주 묻는 질문. 기능, 호환성, 플랫폼 및 출시 전 정보를 다룹니다.
keywords: KeyMod, Openterface, HID 에뮬레이터, 블루투스 키보드, 폰 키보드, 오픈소스, 출시 전, Android, iPadOS
---

# Openterface KeyMod 자주 묻는 질문

**Openterface KeyMod** 자주 묻는 질문에 오신 것을 환영합니다.  
필요한 정보를 찾지 못하셨다면 **[info@openterface.com](mailto:info@openterface.com)으로 이메일**을 보내주시거나 [Discord](/discord) 또는 [Reddit](/reddit)에서 **커뮤니티에 참여**해 주세요.

⚠️ **참고**: KeyMod는 현재 출시 전 개발 단계입니다. 제품을 완성하는 과정에서 기능, 사양 및 디자인이 변경될 수 있습니다.

---

## :material-clipboard-list: 빠른 탐색

- [Openterface KeyMod 자주 묻는 질문](#openterface-keymod-자주-묻는-질문)
  - [:material-clipboard-list: 빠른 탐색](#material-clipboard-list-빠른-탐색)
  - [일반](#일반)
  - [연결](#연결)
  - [기능](#기능)
  - [출시 전](#출시-전)

---

## 일반

**:material-chat-question:{ .faq } KeyMod란 무엇인가요?**

KeyMod는 휴대폰을 휴대용 키보드와 트랙패드로 바꾸는 컴팩트한 USB + 블루투스 HID(키보드 및 마우스) 에뮬레이터입니다. 키보드/마우스 입력이 필요한 기기—키오스크, 스마트 TV, 셋톱박스, 야외 디스플레이—를 전체 키보드를 들고 다니지 않고 제어할 수 있습니다.

**:material-chat-question:{ .faq } KeyMod 앱은 어떤 플랫폼을 지원하나요?**

KeyMod 컨트롤러 앱은 **Android**와 **iPadOS**에 중점을 둡니다. 더 넓은 Openterface 생태계에서 **Windows 및 macOS** 소프트웨어로 데스크톱 제어도 확장하고 있습니다.

**:material-chat-question:{ .faq } 대상 기기에 소프트웨어가 필요하나요?**

아니요. KeyMod는 표준 USB 키보드와 마우스를 에뮬레이션합니다. 대상 기기는 플러그 앤 플레이 HID 하드웨어로 인식합니다—드라이버나 소프트웨어 설치가 필요하지 않습니다.

**:material-chat-question:{ .faq } KeyMod는 오픈소스인가요?**

예. KeyMod는 오픈 하드웨어 및 오픈 소프트웨어입니다. 프로젝트가 발전함에 따라 회로도, PCB 파일, 펌웨어, 소프트웨어 및 BOM을 게시할 예정입니다.

---

## 연결

**:material-chat-question:{ .faq } USB와 블루투스—어떤 것을 사용해야 하나요?**

- **USB**: 더 안정적이고 지연 시간이 낮음. 가장 안정적인 연결이 필요할 때 사용.
- **블루투스**: 케이블 없음. 더 가벼운 설정이 필요하고 시나리오가 무선을 허용할 때 사용.

**:material-chat-question:{ .faq } 어떤 하드웨어 변형이 계획되어 있나요?**

1. **2-in-1 커넥터** — 광범위한 호환성을 위한 USB A + USB C 복합 플러그
2. **USB C 버전** — 현대 기기용 전용 USB C 플러그

---

## 기능

**:material-chat-question:{ .faq } 어떤 게임패드 레이아웃이 지원되나요?**

KeyMod는 **Xbox 레이아웃**, **PlayStation 레이아웃**, **NES 레이아웃**으로 가상 게임 컨트롤러 역할을 할 수 있습니다.

**:material-chat-question:{ .faq } 사용자 정의 프로필과 매크로를 만들 수 있나요?**

예. 오픈소스 모바일 앱은 사용자 정의 입력 프로필, 매크로, 단축키 및 워크플로우 단축키를 지원합니다. 키패드 및 게임패드 모드도 사용할 수 있습니다.

**:material-chat-question:{ .faq } 프로그래밍 가능한 하드웨어 버튼이란 무엇인가요?**

KeyMod에는 빠른 트리거 및 간단한 매크로 스타일 워크플로우와 같은 기기 내 작업을 위한 프로그래밍 가능한 하드웨어 버튼이 포함되어 있습니다. 이 기능은 아직 실험적이며 커뮤니티 피드백을 통해 개선될 예정입니다.

---

## 출시 전

**:material-chat-question:{ .faq } KeyMod는 언제 출시되나요?**

KeyMod는 출시 전 개발 단계입니다. [제품 페이지](/product/keymod/)에서 출시 알림 및 업데이트를 받아보세요.

**:material-chat-question:{ .faq } KeyMod는 Mini-KVM 및 KVM-Go와 어떻게 관련되어 있나요?**

KeyMod는 Openterface Mini-KVM의 검증된 HID 코어를 사용합니다. 동일한 하드웨어 기반 키보드 및 마우스 에뮬레이션 접근 방식을 공유하지만, 다른 사용 사례를 위해 설계되었습니다: KVM-over-USB 비디오 캡처가 아닌 로컬 기기 제어를 위해 휴대폰을 휴대용 키보드/트랙패드로 바꾸는 것입니다.
