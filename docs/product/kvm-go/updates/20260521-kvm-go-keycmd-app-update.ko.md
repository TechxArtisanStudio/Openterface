---
draft: false
date: 2026-05-21
title: "KVM-GO 업데이트: KeyCmd 0.19로 휴대폰에서 대상 기기 제어하기"
description: "USB 또는 블루투스를 통해 KVM-GO와 KeyCmd 0.19를 함께 사용해 보세요. KM Basic 및 Pro 키보드, 작성(Compose) 모드, 게임패드 프리셋, 단축키 허브(Shortcut Hub), 프레젠테이션 제어 기능을 지원하며 HID 입력을 위한 별도의 비디오 동글이 필요하지 않습니다."
keywords: "KVM-GO KeyCmd, KeyCmd 0.19, KVM-GO 안드로이드 앱, KVM-over-USB 휴대폰 제어, Openterface KeyCmd, 가상 키보드 KVM, KVM-GO 블루투스 USB, KM Pro 작성 모드, KVM-GO HDMI DP VGA, Openterface KVM 앱, 휴대용 KVM 입력"
author: "Openterface Team | TechxArtisan"
category: "제품 업데이트"
tags: ["KVM-GO", "KeyCmd", "제품 업데이트", "Android", "USB", "블루투스", "키보드", "게임패드", "릴리스"]
featured: false
social:
  image: "https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp"
  title: "KVM-GO + KeyCmd 0.19 — 휴대폰으로 대상 기기를 제어하세요"
  description: "KeyCmd 0.19는 USB 또는 블루투스를 통해 KVM-GO와 페어링되어 키보드, 마우스, 게임패드, 단축키 및 작성(Compose) 기능을 제공합니다. 비디오 표시가 필요한 경우 Openterface KVM 앱이 이를 담당합니다."
---

# KVM-GO 업데이트: KeyCmd 0.19로 휴대폰에서 대상 기기 제어하기

안녕하세요,

**KVM-GO**를 후원해 주시고 제품 생산 및 배송 기간 동안 기다려 주신 모든 분께 감사드립니다. 많은 분이 여전히 하드웨어를 기다리고 계신다는 것을 잘 알고 있으며, 제품을 받으시는 첫날부터 완벽한 환경을 경험하실 수 있기를 바랍니다.

휴대폰이나 태블릿에서 비디오 출력과 전체 KVM 제어를 가능하게 하는 **Openterface KVM** 앱과 더불어, 저희는 키보드, 마우스, 게임패드 및 단축키 입력을 위한 보조 앱인 **KeyCmd**를 지속적으로 개선해 왔습니다. 현재 KVM-GO를 사용하시는 분들께는 **KeyCmd 0.19** 버전을 권장합니다. **USB** 또는 **블루투스**를 통해 페어링할 수 있으며, 이전 버전 위에 덮어쓰기 방식으로 설치해도 설정, 프로필 및 페어링된 장치 정보가 그대로 유지됩니다.

![노트북의 KVM-GO와 휴대폰의 KeyCmd 키보드 조합](https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp)

아래는 KeyCmd가 KVM-GO와 함께 수행하는 작업, 용도에 따른 모드 선택 방법, 그리고 실제 대상 기기에서 이를 최대한 활용하는 방법에 대한 안내입니다.

![KeyCmd 시작 화면](https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape_1.webp)

## 모드 및 사용 방법

### 키보드 및 마우스 (기본형 - Basic)

다른 방해 요소 없이 **심플한 전체 화면 키보드**만 사용하고 싶을 때 선택하세요.

**용도:** BIOS 비밀번호 입력, 짧은 쉘(Shell) 명령어, 숫자 패드 입력 또는 KVM-GO로 화면을 보면서 넓은 터치패드로 마우스를 제어할 때 적합합니다.

**사용 방법:**

- 네비게이션 메뉴에서 **KM Basic**을 엽니다.
- 필요에 따라 화면 키보드, **숫자 패드**(세로 또는 가로), **터치패드** 탭을 사용합니다.
- **설정**에서 **고정 키(Sticky modifiers)**(탭하여 Shift/Ctrl 잠금) 또는 조합 입력을 선호하는 경우 **코드 스타일(Chord-style)** 수정 키를 선택할 수 있습니다.

**장점:** 키 입력을 위한 화면 공간이 더 넓고 인터페이스가 단순하며, 단축키가 아닌 순수 입력만 필요할 때 더 빠릅니다.

![KM Basic 전체 화면 키보드](https://assets2.openterface.com/images/keymod/KM-Basic-Keyboard_1.webp)

![가로 모드의 KeyCmd 숫자 패드](https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape_1.webp)

### 키보드 및 마우스 (전문가용 - Pro)

![가로 모드의 KM Pro 분리형 키보드](https://assets2.openterface.com/images/keymod/KM-Pro-Keyboard-landscape-split_1.webp)

![세로 모드의 KeyCmd 키보드와 터치패드](https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait_1.webp)

KVM-GO에 연결된 기기에서 **일상적인 관리 작업**을 수행할 때 사용하세요. 분리형 키보드, IME, 단축키 허브(Shortcut Hub) 바, 그리고 **작성(Compose)** 에디터를 지원합니다.

**용도:** 긴 타이핑 세션, 매크로 및 단축키 사용, KVM 뷰를 통해 결과를 확인하면서 호스트 기기에 텍스트 블록이나 스크립트를 전송할 때 유용합니다.

![스크립트를 전송 중인 작성(Compose) 모드](https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait_1.webp)

명령어나 스크립트를 자주 붙여넣는다면 **작성(Compose)** 기능을 꼭 사용해 보세요. 휴대폰에서 텍스트를 작성하고 검토한 후 호스트에 키 입력 방식으로 전송할 수 있습니다. [YouTube의 짧은 데모 영상](https://www.youtube.com/watch?v=_rJF-hTF3_E)에서 전체 흐름을 확인하실 수 있습니다.

**사용 방법:**

- 네비게이션 메뉴에서 **KM Pro**를 엽니다.
- Basic 모드처럼 키보드와 터치패드를 사용하며, 상단의 **단축키 허브(Shortcut Hub)** 카테고리를 통해 프로필에 설정한 동작을 원터치로 실행할 수 있습니다.
- **작성(Compose)**을 열어 휴대폰에서 장문을 초안으로 작성하고 검토한 후 HID 키 입력으로 **전송(Send)**합니다. 긴 텍스트 전송 시 진행 표시줄이 나타납니다. 텍스트에 비 ASCII 문자가 포함된 경우 전송 전 경고가 표시되어 호스트 호환성을 확인할 수 있습니다(특히 macOS에서 유용합니다).

**장점:** 타이핑, 포인팅, 단축키, 붙여넣기 방식의 워크플로우를 한곳에서 처리할 수 있어 대상 기기로 풀 사이즈 키보드를 들고 갈 필요가 없습니다.

### 게임패드 (Gamepad)

게임이나 게임패드 입력을 요구하는 대상 기기의 앱을 위해 화면에 **가상 컨트롤러** 레이아웃을 띄우고 싶을 때 사용하세요.

**용도:** 에뮬레이터, 캐주얼 게임, 또는 KVM-GO가 화면 출력을 담당하는 동안 스틱과 버튼이 있는 컴팩트한 제어 표면으로 활용하기에 좋습니다.

**사용 방법:**

- **Gamepad** 모드로 전환합니다.
- 툴바의 **Preset**을 탭하여 저장된 레이아웃을 **순환**합니다. **Preset을 길게 누르면** 전체 목록이 열리며, **가져오기/내보내기** 또는 **모듈 추가**(스틱, 버튼, 터치패드)가 가능합니다.
- 기본 포함된 **emu-6** 프리셋에서 시작하여 편집해 보세요. 하나의 레이아웃에 **여러 개의 터치패드**와 추가 스틱 모듈을 배치할 수 있습니다.

**장점:** 정해진 레이아웃에 얽매이지 않고 게임별 또는 기기별로 레이아웃을 저장하고 프리셋을 다른 사람과 공유할 수 있습니다.

![게임패드 프리셋 레이아웃](https://assets2.openterface.com/images/keymod/Gamepad-perset-1_1.webp)

![마인크래프트에서 사용 중인 게임패드 프리셋](https://assets2.openterface.com/images/keymod/Gamepad-perset-minecraft_1.webp)

*마인크래프트용으로 커스텀된 프리셋.*

### 단축키 허브 (Shortcut Hub)

KM Pro 내부의 **프로필 및 단축키** 관리 센터입니다. 카테고리, 상세 패널, 그리고 바에 할당한 단축키들이 포함됩니다.

**용도:** KVM-GO의 비디오 연결을 유지한 상태에서 대상 기기에서의 반복 작업(터미널 열기, 명령어 체인 붙여넣기, 설정 전환 등)을 수행할 때 적합합니다.

**사용 방법:**

- KM Pro에서 **Default** 프로필(또는 직접 만든 프로필)로 작업합니다.
- 카테고리 탭과 상세 UI를 사용하여 단축키를 관리합니다.
- 프로필 구성 방식이 생소하다면 **단축키 허브 가이드 투어**를 실행해 보세요.

### 프레젠테이션 (Presentation)

휴대폰을 회전해도 버튼 위치가 바뀌지 않도록 **세로 모드**로 고정된 단순한 **프레젠터 스타일**의 제어 화면입니다.

**용도:** 대상 기기에서 슬라이드를 넘기거나 가벼운 프레젠테이션 제어가 필요할 때 유용합니다.

![Google 프레젠테이션을 제어 중인 프레젠테이션 모드](https://assets2.openterface.com/images/keymod/KeyCmd-Presentation-Google-Slides.webp)

---

## 지원 언어

앱 UI는 **11개 언어**를 지원합니다. 최근 한국어, 이탈리아어, 러시아어, 브라질 포르투갈어가 추가되었습니다.

**Settings** → **App language**에서 언어를 변경할 수 있습니다.

---

## KeyCmd 0.19 다운로드 및 KVM-GO 연결

**다운로드:** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

기존 앱이 설치되어 있다면 그대로 덮어쓰기 설치하세요. 데이터를 삭제할 필요는 없습니다.

**KVM-GO 연결 (비디오 포트는 연결하지 않아도 됩니다):**

**KVM-GO의 세 가지 모델**(HDMI, VGA, DP) 모두 KeyCmd 입력을 위해서 **동글의 비디오 커넥터**를 연결할 필요는 없습니다. HDMI, VGA 또는 DP 포트는 비워두어도 무방합니다. 아래의 두 가지 설정 중 하나를 선택하세요.

**옵션 A — 블루투스 (대상 기기에서 KVM-GO에 전원 공급)**

1. **짧은 검은색 USB 케이블**을 KVM-GO의 **Target** 포트와 제어하려는 기기에 연결합니다. 이 연결만으로 KVM-GO에 **전원**이 공급됩니다.
2. 휴대폰에서 **KeyCmd**를 열고 **블루투스**를 통해 KVM-GO를 찾습니다.

**옵션 B — 안드로이드 휴대폰에 USB 연결 (Host 포트)**

1. KVM-GO의 **Host** 포트에서 **긴 주황색 케이블**을 안드로이드 휴대폰에 연결합니다.
2. **KeyCmd**를 열고 앱 내에서 **USB** 연결을 선택합니다.

![짧은 검은색 USB 케이블로 노트북에 연결된 KVM-GO Target 포트](https://assets2.openterface.com/images/kvm-go/kvm-go-target-port-laptop-power.webp)

전체 화면 비디오와 입력을 동시에 사용하려면 대상 화면 출력용으로 **Openterface KVM**을, 키보드/마우스/단축키용으로 **KeyCmd**를 사용하세요. 대상 기기에 이미 전용 디스플레이가 있고 입력 제어만 필요한 경우에는 KeyCmd만으로 충분합니다.

두 기기를 모두 사용 중이라면 USB를 통해 **Mini-KVM**에서도 작동합니다.

> **아직 베타 버전입니다.** 게임패드 프리셋 및 작성(Compose) 전송 기능은 호스트 OS에 따라 다르게 작동할 수 있습니다. KVM-GO 사용 중 이상 현상이 발생하면 스크린샷, 사용 중인 KVM-GO 모델(HDMI / DP / VGA), 그리고 기대했던 동작 내용을 적어 **Discord**로 문의해 주세요.

> **소스 코드:** 아직 공개되지 않았습니다. 관련 프로젝트의 크라우드펀딩 마일스톤 완료 후 오픈 소스화할 계획입니다. APK를 찾는 데 도움이 필요하면 Discord에서 문의해 주세요.

---

## KeyMod에 대하여 (선택 사항, KVM-GO와 별개)

저희는 동일한 KeyCmd 앱을 위한 전용 USB 및 블루투스 HID 동글인 **[KeyMod](https://openterface.com/product/keymod/)**도 개발 중입니다. KVM-GO 후원자분들은 위의 워크플로우를 위해 KeyMod가 따로 필요하지 않으며, 현재 저희가 권장하는 방식은 KVM-GO를 통한 KeyCmd 사용입니다.

KVM 이외의 환경에서 사용할 독립형 동글이 궁금하시다면 [Crowd Supply의 KeyMod 캠페인](https://www.crowdsupply.com/techxartisan/openterface-keymod)을 팔로우해 주세요. 이는 KVM-GO 배송과는 별개의 프로젝트입니다.

---

## 여러분의 피드백을 기다립니다

잠시 시간을 내어 **KeyCmd 0.19**를 설치하고 KVM-GO(또는 Mini-KVM)에 연결해 보신 후, 여전히 불편한 점을 알려주세요. 서버실 긴급 점검이나 홈랩(Homelab) 사용 사례에서 보내주신 보고는 다음 릴리스에 직접적으로 반영됩니다.

KVM-GO 프로젝트를 돕는 실질적인 방법들:

- Discord나 커뮤니티에서 **잘 작동하는 부분들을 공유**해 주세요 (BIOS 팁, 블루투스 페어링, 즐겨 쓰는 모드 등)
- 모니터 없는 기기를 관리하며 포켓 사이즈 KVM이 필요한 **동료에게 알려주세요**
- **솔직한 피드백**, 특히 개선이 필요한 부분을 계속 보내주세요. 단순한 응원보다 제품을 완성하는 데 더 큰 힘이 됩니다

KVM-GO를 후원해 주시고, 휴대용 KVM-over-USB를 모두에게 더 나은 제품으로 만드는 데 도움을 주셔서 다시 한번 감사드립니다.

감사합니다.

**Openterface 팀 | TechxArtisan**
