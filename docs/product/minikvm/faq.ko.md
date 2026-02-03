---
title: Openterface Mini-KVM 자주 묻는 질문
description: Mini-KVM에 대한 자주 묻는 질문으로, 기능, 호환성, 문제 해결 및 향후 계획을 다룹니다.
keywords: Mini-KVM, Openterface, KVM 스위치, 오픈소스, 문제 해결, 비디오 캡처, USB, 호환성, 진단 자기 점검, 키보드 마우스 제어, 하드웨어 진단, 지원
---

# Openterface Mini-KVM 자주 묻는 질문

우리의 플래그십 제품 **Openterface Mini-KVM**에 대한 자주 묻는 질문에 오신 것을 환영합니다.  
필요한 정보를 찾지 못하셨다면 **[info@openterface.com](mailto:info@openterface.com)으로 이메일**을 보내거나 [Discord](/discord) 또는 [Reddit](/reddit)에서**커뮤니티에 참여**해 주세요.

⚠️ _자주 묻는 질문이 오래되었을 수 있습니다 — 업데이트가 필요한 내용을 발견하시면 알려주세요._

---

## :material-clipboard-list: 빠른 탐색

-   [USB 포트 및 파일 전송](#usb-포트-및-파일-전송)
-   [기술](#기술)
-   [제어](#제어)
-   [비디오](#비디오)
-   [문제 해결](#문제-해결)
-   [기타](#기타)

---

## USB 포트 및 파일 전송

**:material-chat-question:{ .faq } 파일을 전송할 수 있나요?**

네 — 호스트와 대상 간에 공유되는 전환 가능한 USB-A 포트를 통해 가능합니다.

**:material-chat-question:{ .faq } 소프트웨어로 USB 포트를 전환할 수 있나요?**

네, 하드웨어 버전 **v1.9+**에서 가능합니다.

**:material-chat-question:{ .faq } USB 3.0 대신 2.0을 사용하는 이유는?**

USB 2.0은 1080p@30Hz 비디오 + HID + 표준 속도 파일 전송에 충분하며, 컴팩트하고 더 시원하며 더 저렴합니다.  
USB 3.0은 향후 프로 모델에 등장할 수 있습니다.

---

## 기술

**:material-chat-question:{ .faq } 오픈소스인가요?**

네 — [OSHWA](https://certification.oshwa.org/cn000015.html)에서 인증받았습니다. 하드웨어와 소프트웨어는 [GitHub](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware)에 있습니다.

**:material-chat-question:{ .faq } BIOS 접근**

직접 USB 연결을 통해 원격 전용 도구(VNC, TeamViewer)와 달리 완전한 BIOS 레벨 제어가 가능합니다.  
구형 머신에서는 USB 허브 인식에 BIOS 문제가 있을 수 있습니다 — 해당 사례를 보고해 주세요.

**:material-chat-question:{ .faq } 비디오/데이터 전송**

비디오는 HDMI를 통해 캡처되고 USB 2.0을 통해 전송됩니다.  
전환 가능한 USB 포트를 통해 드라이브나 기타 장치를 공유할 수 있습니다.

**:material-chat-question:{ .faq } 전원 처리**

Mini-KVM은 **양쪽** (호스트 또는 대상)에서 전원을 가져올 수 있습니다. **짧은 케이블** 쪽이 일반적으로 메인 전원이 됩니다.  
저전력 대상(예: Raspberry Pi)의 경우 Mini-KVM을 통한 역전원 대신 전용 전원 공급 장치를 사용하세요.

**:material-chat-question:{ .faq } 케이블 길이 제한**

-   **주황색 호스트 USB-C 케이블 ≤1.5m**를 유지하세요.
-   더 긴 케이블의 경우 다음을 통해 전원을 주입하세요:
    -   USB-A 수-수 케이블
    -   [확장 핀](/product/minikvm/extension-pins/)
    -   USB-C Y 스플리터
-   같은 규칙이 **검은색 대상 케이블**에도 적용됩니다.

---

## 제어

**:material-chat-question:{ .faq } 키보드와 마우스로 대상 컴퓨터를 제어할 수 없음**

대상 데스크톱은 보이지만 키보드와 마우스 입력이 응답하지 않으면, 일반적으로 HID 통신이 설정되지 않았음을 의미합니다. 다음 단계를 시도하세요:

1. **케이블 연결 확인** — 대상 Type-C 케이블이 대상 컴퓨터에 연결되어 있는지, 호스트 케이블이 제어 컴퓨터에 연결되어 있는지 확인하세요.
2. **무전원 USB 허브 피하기** — 직접 연결 또는 전원 공급 허브를 사용하세요.
3. **HID 칩 리셋** — 장치가 "멈춘" 것처럼 보이면 **고급 메뉴 → HID 칩 공장 초기화** (OpenterfaceQt) 또는 **시리얼 리셋 도구** (macOS)를 사용하세요.
4. **다른 USB 포트 시도 또는 재부팅** — 호스트 OS가 USB 오류 후 포트를 비활성화했을 수 있습니다.
5. **보드레이트 낮추기** — 노이즈가 많은 환경에서는 더 안정적인 통신을 위해 9600 bps로 전환하세요.

자세한 내용은 [키보드 및 마우스 제어 문제 해결](/product/minikvm/support/keyboard-mouse-control/)을 참조하세요.

**:material-chat-question:{ .faq } 무선 또는 이더넷 버전?**

내장되어 있지 않습니다. 원격 제어를 위해 헤드리스 컴퓨터(예: Raspberry Pi) + 원격 데스크톱을 사용하세요.

**:material-chat-question:{ .faq } PS/2 호환성?**

지원하지 않습니다 — PS/2 지원은 향후 버전에서 탐색될 수 있습니다.

**:material-chat-question:{ .faq } 한 컴퓨터에서 여러 Mini-KVM 사용?**

네, QT 앱(Windows/Linux)의 실험적 기능입니다.

**:material-chat-question:{ .faq } 전원 켜기/끄기 제어?**

직접적으로는 안 되지만, [확장 핀](/product/minikvm/extension-pins/)을 통해 향후 ATX 제어 모듈이 가능합니다.

---

## 비디오

**:material-chat-question:{ .faq } 지연 시간 및 해상도**

-   **1080p@30Hz**로 캡처
-   **140ms 미만**의 지연 시간 → 부드러운 제어

**:material-chat-question:{ .faq } 입력 대 캡처 해상도**

-   **4K@30Hz**까지의 입력을 받아들임
-   **1080p**로 캡처, 더 높은 입력은 다운샘플링됩니다(약간 흐릿하게 보일 수 있음).
-   모범 사례: **대상을 1080p로 설정**하세요.

**:material-chat-question:{ .faq } 게임 적합성**

AAA 게임에는 적합하지 않습니다. Minecraft나 에뮬레이터 같은 가벼운 게임에는 잘 작동합니다.

**:material-chat-question:{ .faq } 인터넷을 통한 원격 제어**

내장되어 있지 않지만, Mini-KVM을 호스트의 원격 데스크톱 소프트웨어와 페어링할 수 있습니다.

**:material-chat-question:{ .faq } 기타 비디오 형식**

VGA, DVI, DisplayPort 등에는 어댑터를 사용하세요.

---

## 문제 해결

**:material-chat-question:{ .faq } Mini-KVM이 정상 작동하는지 진단하려면?**

USB 연결을 확인하고 하드웨어 문제를 감지하려면 내장 진단 자기 점검을 실행하세요:

- **macOS:** [진단 자기 점검 가이드 (macOS)](/product/minikvm/support/diagnostic-self-check/) — 설정 → 고급 및 디버그 → 진단 도구 열기
- **Windows:** [진단 자기 점검 가이드 (Windows)](/product/minikvm/support/diagnostic-self-check-windows/) — 고급 → 하드웨어 진단

진단은 대상/호스트 플러그 앤 플레이, 스트레스 테스트 등을 테스트합니다. 모든 테스트가 통과하면 장치가 정상 작동합니다.

**:material-chat-question:{ .faq } 하드웨어 문제를 지원팀에 보고하려면?**

진단 자기 점검에서 하나 이상의 테스트가 **실패**로 표시되면:

1. 나머지 진단 단계를 완료하세요 (도구가 안내합니다).
2. 문제가 감지되면 **지원 이메일** 또는 **결함 보고** 창이 열립니다.
3. **주문 번호**와 **이름**을 입력한 후 이메일 주소와 초안을 복사하세요.
4. **요청된 로그 파일** (도구가 표시)과 **설치 사진** (Mini-KVM + 호스트/대상 연결이 선명하게 보이는)을 첨부하세요.
5. 지원팀에 이메일을 보내세요.

단계별 설명은 [진단 자기 점검 가이드 (macOS)](/product/minikvm/support/diagnostic-self-check/) 또는 [진단 자기 점검 가이드 (Windows)](/product/minikvm/support/diagnostic-self-check-windows/)를 참조하세요.

**:material-chat-question:{ .faq } USB 허브 문제**

전압 강하로 인한 불안정성을 피하기 위해 **전원 공급 허브**를 사용하세요. 무전원 허브는 전력 공급 부족과 HID(키보드/마우스) 동작 불안정을 유발할 수 있습니다. 자세한 내용은 [키보드 및 마우스 제어 문제 해결](/product/minikvm/support/keyboard-mouse-control/)을 참조하세요.

**:material-chat-question:{ .faq } 앱에 비디오가 표시되지 않거나 제어가 응답하지 않음**

1. 모든 케이블을 분리하고 몇 초 기다린 후 다시 연결하세요.
2. HID 문제(케이블, 허브, HID 리셋)에 대해 [키보드 및 마우스 제어 문제 해결](/product/minikvm/support/keyboard-mouse-control/)을 확인하세요.
3. 장치를 검증하려면 [진단 자기 점검](/product/minikvm/support/diagnostic-self-check/) (macOS) 또는 [하드웨어 진단](/product/minikvm/support/diagnostic-self-check-windows/) (Windows)을 실행하세요.
4. 해결되지 않으면 펌웨어를 확인하거나 호스트 앱을 업데이트하세요.

**:material-chat-question:{ .faq } 43184x24228@44Hz 같은 이상한 해상도**

캡처 펌웨어가 공장 설정으로 되돌아갔을 가능성이 있습니다.  
[GitHub 릴리스](https://github.com/TechxArtisanStudio/Openterface_QT/releases)를 통해 펌웨어를 다시 플래시하세요.

**:material-chat-question:{ .faq } 다시 플래시했지만 여전히 고장?**

-   올바른 USB 열거 확인(`USB Tree Viewer` 또는 `lsusb -v`)
-   최신 호스트 앱 확인
-   [진단 자기 점검](/product/minikvm/support/diagnostic-self-check/)을 실행하여 로그 캡처
-   여전히 실패하면 주문 번호, 진단 로그, 설치 사진을 첨부하여 지원팀에 문의 — [하드웨어 문제를 지원팀에 보고하려면?](#하드웨어-문제를-지원팀에-보고하려면) 참조
