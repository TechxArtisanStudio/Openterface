---
title: Openterface KVM-Go 시리즈 자주 묻는 질문
description: KVM-Go 시리즈에 대한 자주 묻는 질문으로, 기능, 호환성 및 사전 출시 정보를 다룹니다.
keywords: KVM-Go, Openterface, 초소형 KVM, HDMI 내장, 키체인 KVM, 오픈소스, 사전 출시, 비디오 캡처, USB, 호환성, MicroSD
---

# Openterface KVM-Go 시리즈 자주 묻는 질문

차세대 **Openterface KVM-Go 시리즈**의 FAQ에 오신 것을 환영합니다.  
필요한 정보를 찾지 못하셨다면, **[info@openterface.com](mailto:info@openterface.com)으로 이메일을 보내주시거나** [Discord](/discord) 또는 [Reddit](/reddit)에서 **커뮤니티에 참여**해 주세요.

⚠️ **참고**: KVM-Go는 현재 사전 출시 개발 단계입니다. 제품을 완성하는 과정에서 기능, 사양 및 디자인이 변경될 수 있습니다.

---

## :material-clipboard-list: 빠른 탐색

- [Openterface KVM-Go 시리즈 자주 묻는 질문](#openterface-kvm-go-시리즈-자주-묻는-질문)
  - [:material-clipboard-list: 빠른 탐색](#material-clipboard-list-빠른-탐색)
  - [일반](#일반)
  - [MicroSD 및 파일 전송](#microsd-및-파일-전송)
  - [기술](#기술)
  - [사전 출시](#사전-출시)

---

## 일반

**:material-chat-question:{ .faq } KVM-Go란 무엇인가요?**

KVM-Go는 차세대 초소형 KVM-over-USB 솔루션입니다. 키체인 크기로 비디오 커넥터(HDMI, DisplayPort 또는 VGA)가 내장되어 별도의 케이블이 필요하지 않습니다.

**:material-chat-question:{ .faq } 얼마나 작나요?**

초소형 크기: **18 × 18 × 55 mm** (0.71 × 0.71 × 2.17 인치) — 키체인에 넣을 수 있을 만큼 작습니다. 무게는 약 **25g (0.9 온스)**입니다.

**:material-chat-question:{ .faq } 어떤 모델이 있나요?**

- **KVM-Go HDMI Male** — 최신 장치를 위한 직접 HDMI 연결
- **KVM-Go DisplayPort Male** — 고성능 DisplayPort 지원  
- **KVM-Go VGA Male** — 레거시 시스템 호환성 (출시 예정)

**:material-chat-question:{ .faq } Mini-KVM과 비교하면 어떤가요?**

주요 개선 사항:

- **크기**: 18×18×55mm vs 61×53×13.5mm (훨씬 작음)
- **무게**: 25g vs 48g (더 가벼움)
- **비디오**: 4K@60Hz vs 1080p@30Hz (더 나은 성능)
- **USB**: USB 3.0 vs USB 2.0 (더 빠름)
- **설치**: 내장 커넥터 vs 별도 케이블 (더 쉬움)

**:material-chat-question:{ .faq } 시작 속도는 얼마나 빠른가요?**

하드웨어 시작 시간이 1초 미만이므로 워크플로를 지연하거나 방해하지 않고 즉시 문제를 해결할 수 있습니다.

---

## MicroSD 및 파일 전송

**:material-chat-question:{ .faq } 파일 전송이 가능한가요?**

예 — **전환 가능한 MicroSD 슬롯**을 통해 호스트와 타겟 장치 간에 공유할 수 있어, 카드를 물리적으로 제거하지 않고도 빠른 파일 전송이 가능합니다.

**:material-chat-question:{ .faq } MicroSD 방향을 전환하는 방법은?**

두 가지 편리한 방법:
1. **하드웨어 버튼** – 수동 제어를 위한 장치의 물리적 버튼
2. **소프트웨어 스위치** – 즉시 전환을 위한 호스트 앱 내의 토글 버튼

**:material-chat-question:{ .faq } LED 표시등은 무엇을 의미하나요?**

**이중 색상 LED 표시등**은 현재 MicroSD 연결 상태를 표시합니다:

- **🔵 파란색 LED 켜짐** – MicroSD 카드가 **타겟 장치**에 마운트됨  
- **🟢 녹색 LED 켜짐** – MicroSD 카드가 **호스트 컴퓨터**에 마운트됨  
- **LED 꺼짐** – MicroSD 카드가 삽입되지 않았거나 장치 전원이 꺼짐  
- **LED 깜박임** – 데이터 전송 진행 중 (읽기/쓰기 활동)

**:material-chat-question:{ .faq } MicroSD 카드를 올바르게 설치하려면 어떻게 해야 하나요?**

**딸깍** 소리가 날 때까지 MicroSD 카드를 단단히 삽입하여 안전하게 장착되고 제자리에 고정되었음을 나타냅니다. 이 촉각 피드백은 올바른 연결을 확인합니다.

---

## 기술

**:material-chat-question:{ .faq } 비디오 성능은 어떻습니까?**

- **입력**: 최대 4096×2160 @ 60 Hz (YUV420), 4096×2160 @ 30 Hz (YUV444)
- **출력**: 4096×2160 @ 60 Hz (MJPEG), 3840×2160 @ 30 Hz (YUV420)
- **기본값**: 최적의 안정성과 성능을 위한 1080p@60Hz
- **지연 시간**: 원활한 제어를 위해 140ms 미만

**:material-chat-question:{ .faq } 4K 모드에 제한이 있나요?**

예 — 4K 모드는 실험적이며 추가 열을 발생시킵니다. 장시간 4K 작동 중에 장치 표면이 상당히 뜨거워질 수 있습니다. 최적의 안정성과 성능을 위해 기본 1080p@60Hz 모드를 권장합니다.

**:material-chat-question:{ .faq } 오픈소스인가요?**

예 — [OSHWA](https://certification.oshwa.org/cn000015.html)에서 인증받았습니다. 하드웨어와 소프트웨어는 [GitHub](https://github.com/TechxArtisanStudio/Openterface_KVM-GO_Hardware)에 있습니다.

**:material-chat-question:{ .faq } BIOS 액세스**

직접 USB 연결을 통해 원격 전용 도구(VNC, TeamViewer)와 달리 완전한 BIOS 수준 제어가 가능합니다.

**:material-chat-question:{ .faq } 크로스 플랫폼 지원?**

[호스트 앱](/app)은 macOS, Windows, Linux, Android 및 Chrome 웹 앱과 호환되어 범용 통합이 가능합니다.

**:material-chat-question:{ .faq } iPad에서 사용할 수 있나요?**

예 — iPadOS 지원은 Apple App Store에서 사용 가능한 네이티브 앱을 통해 곧 출시될 예정입니다. 이는 KVM-GO의 내장 Bluetooth 기능으로 가능하며, iPad에서 기본적으로 작동하는 몇 안 되는 KVM 중 하나입니다.

**:material-chat-question:{ .faq } 웹 기반 앱이 있나요?**

예 — [Openterface Viewer](https://openterface-viewer.pages.dev/)를 방문하여 설치가 필요 없는 브라우저 기반 앱(Chrome, Edge, Safari에서 작동)을 사용하세요. 빠른 액세스나 호스트 컴퓨터에 소프트웨어를 설치할 수 없는 경우에 완벽합니다. 이 프로젝트를 시작한 [@kashalls](https://github.com/kashalls)을 비롯한 놀라운 커뮤니티에 감사드립니다.

**:material-chat-question:{ .faq } 어떤 비디오 커넥터를 선택해야 하나요?**

- **HDMI**: 최신 장치, 서버, 워크스테이션에 최적
- **DisplayPort**: 고해상도 디스플레이, 전문 설정용
- **VGA**: 레거시 시스템, 구형 서버 (출시 예정)

---

## 사전 출시

**:material-chat-question:{ .faq } KVM-Go는 언제 출시되나요?**

KVM-Go는 현재 소규모 배치 생산 테스트 중이며, 실제 검증을 위해 베타 테스터에게 유닛을 보냈습니다.

**생산 일정**:

- **2025년 11월**: 캠페인 시작
- **2025년 12월**: 생산 설정 및 구성 요소 소싱 완료
- **2026년 1-3월**: 대량 생산 및 품질 관리
- **2026년 4월**: 후원자에게 첫 출하

진행 상황을 확인하고 조기 액세스를 받으려면 [대기 목록]({{ config.extra.kvmgo_purchase_link }})에 가입하세요.

**:material-chat-question:{ .faq } 가격은 얼마인가요?**

가격은 공식 출시 캠페인 중에 발표될 예정입니다. 초기 지원자는 특별 할인 및 우선 액세스를 받게 됩니다.

**:material-chat-question:{ .faq } 베타 테스터가 될 수 있나요?**

예! 하드웨어 및 소프트웨어 테스트 경험이 있으시다면 [여기](https://forms.gle/yaS1F5E5MSo8DWNZ6)에서 베타 테스트 프로그램에 신청하실 수 있습니다.

**:material-chat-question:{ .faq } 사양이 확정되었나요?**

아니요, 개발 중 제품을 완성하면서 기능, 사양 및 디자인은 변경될 수 있습니다.

