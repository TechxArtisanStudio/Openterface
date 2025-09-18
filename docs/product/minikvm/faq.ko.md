---
title: Openterface Mini-KVM 자주 묻는 질문
description: Mini-KVM에 대한 자주 묻는 질문으로, 기능, 호환성, 문제 해결 및 향후 계획을 다룹니다.
keywords: Mini-KVM, Openterface, KVM 스위치, 오픈소스, 문제 해결, 비디오 캡처, USB, 호환성
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

네 — [OSHWA](https://certification.oshwa.org/cn000015.html)에서 인증받았습니다. 하드웨어와 소프트웨어는 [GitHub](/contributing/)에 있습니다.

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

**:material-chat-question:{ .faq } USB 허브 문제**

전압 강하로 인한 불안정성을 피하기 위해 **전원 공급 허브**를 사용하세요.

**:material-chat-question:{ .faq } 앱에 비디오가 표시되지 않거나 제어가 응답하지 않음**

모든 케이블을 분리하고, 기다린 후 다시 연결하세요.  
해결되지 않으면 펌웨어를 확인하거나 호스트 앱을 업데이트하세요.

**:material-chat-question:{ .faq } 43184x24228@44Hz 같은 이상한 해상도**

캡처 펌웨어가 공장 설정으로 되돌아갔을 가능성이 있습니다.  
[GitHub 릴리스](https://github.com/TechxArtisanStudio/Openterface_QT/releases)를 통해 펌웨어를 다시 플래시하세요.

**:material-chat-question:{ .faq } 다시 플래시했지만 여전히 고장?**

-   올바른 USB 열거 확인(`USB Tree Viewer` 또는 `lsusb -v`)
-   최신 호스트 앱 확인
-   여전히 실패하면 진단/교체를 위해 지원팀에 문의하세요.
