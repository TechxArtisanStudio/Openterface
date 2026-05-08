---
draft: false
date: 2026-05-09
title: "KeyMod 0.15: 게임패드 프리셋 파이프라인, 키보드 & 마우스 (Basic) 티어, 멀티 터치패드 레이아웃"
description: "KeyMod 0.15는 스키마 v7의 게임패드 프리셋 파이프라인, 멀티 터치패드 레이아웃, 전체 화면 키보드가 포함된 키보드 & 마우스 (Basic) 티어, 앱 전반의 KeyMod 브랜딩을 제공합니다. 정제된 입력 환경을 향한 중요한 발전입니다."
keywords: "KeyMod 0.15, KeyMod 릴리즈, 게임패드 프리셋, 멀티 터치패드, 키보드 마우스 basic, KeyMod 브랜딩, Openterface KeyMod 업데이트, HID 에뮬레이터, 가상 게임패드, Android 키보드 앱"
author: "TechxArtisan Studio"
category: "제품 업데이트"
tags: ["KeyMod", "제품 업데이트", "릴리즈", "게임패드", "키보드", "Android"]
featured: false
social:
  image: "https://assets.openterface.com/images/keymod/keymod-015-release.jpg"
  title: "KeyMod 0.15 릴리즈 — 게임패드 프리셋, basic 티어, 멀티 터치패드"
  description: "KeyMod 0.15는 게임패드 프리셋 파이프라인 v7, 전용 키보드 & 마우스 (Basic) 티어, 멀티 터치패드 레이아웃, 새로운 KeyMod 브랜딩을 제공합니다."
---

# KeyMod 0.15: 게임패드 프리셋 파이프라인, 키보드 & 마우스 (Basic) 티어, 멀티 터치패드 레이아웃

KeyMod **0.15**(`versionCode` **15**)는 세 가지 주요 기능을 제공하는 마일스톤 릴리즈입니다: 레이아웃 스키마 **v6-v7**의 **게임패드 프리셋 파이프라인**, 전용 **키보드 & 마우스 (Basic)** 티어, 그리고 **멀티 터치패드** 레이아웃. 이 업데이트는 웰컴 흐름과 빌드 아티팩트 전반에 **KeyMod** 브랜딩도 도입합니다.

## 게임패드: 프리셋 파이프라인 v7

이제 게임패드에서 커스텀 컨트롤러 레이아웃을 저장, 로드, 가져오기, 내보내기 할 수 있는 **프리셋 시스템**을 사용합니다.

### 변경 사항

- **Preset store v7**가 기존 내장 레이아웃을 대체합니다. 클래식 팩토리 프리셋(`preset_classic_*`)과 **Two buttons**(`preset_two_buttons`)이 디스크에서 제거되었습니다. 삭제 보호된 팩토리 레이아웃으로 **`preset_default`**만 남습니다.
- **스키마 v7**에서 **`stick_left`**가 선택 사항이 되었습니다. 이제 레이아웃에 왼쪽 엄지 모듈이 전혀 없어도 됩니다. **Add module** 메뉴는 **`stick_left`**, **`stick_left_2`**, **`stick_left_3`** 등을 삽입합니다.
- **멀티 터치패드 지원**: 프리셋에 여러 터치패드(`touchpad_1`, `touchpad_2`)를 포함할 수 있습니다. 터치패드를 추가하면 약간 오프셋된 앵커로 다음 사용 가능한 id가 할당됩니다. 번들 L/M/R 마우스 버튼은 모든 터치패드에서 공유됩니다.
- **터치패드 마우스 버튼 크기**: 마우스 버튼이 이제 더 큰 기본 그리기 반경을 사용합니다. 터치패드에서 길게 눌러 **Mouse button size**로 크기를 조정하거나, 개별 마우스 모듈에서 **This button size**로 조정할 수 있습니다.
- **보조 스틱 기본값**: **`stick_left_2+`**가 기본값으로 D-pad 십자 + WASD 매핑입니다.

### 프리셋 관리

- 도구 모음에서 Preset 칩을 **탭**하여 사용 가능한 레이아웃을 순환
- **길게 누르기**로 가져오기, 모듈 추가, 내보내기 옵션이 있는 전체 프리셋 목록 표시
- 번들 **emu-6** 레이아웃이 스타터 프리셋으로 포함
- 내보내기 생성기는 언어 간 프리셋 공유를 위한 i18n을 지원

## 키보드 & 마우스 (Basic)

앱 헤더 없이 집중된 타자를 위한 전용 전체 화면 키보드 티어입니다.

### 기능

- 앱 메인 헤더가 없는 **전체 화면 키보드**로 더 넓은 화면 공간
- **세로 및 가로 넘패드**: 세로 모드에서 5x8 그리드(PrtSc / ScrLk / Pause / Home / End), 가로 모드에서 8x5 그리드(큰 +, Enter, 00 포함)
- **IME ASCII 전용 전송 게이트**: compose 모드에서 긴 텍스트를 입력하고 깔끔한 HID 키스트로크로 전송
- **길게 눌러 반복**: 문자/기능 키를 길게 눌러 자동 반복(~400ms 지연, ~50ms 반복)
- **키 미리보기**: 키를 누르면 키 위에 효과적인 라벨을 표시하는 플로팅 버블
- **햅틱 피드백** 및 **테마 대응** 키 표면

### Sticky 수식키 vs Chord 수식키

설정에서 Basic 키보드의 **sticky 수식키**(탭으로 고정)와 **순간 + 길게 눌러 chord**(기본값) 중 선택 가능

## 브랜딩

- 앱 표시 이름이 이제 **KeyMod**
- 웰컴 화면에 **KeyMod** 워드마크 표시
- CI 아티팩트 및 APK 파일명에 **KeyMod** 접두사 사용
- `applicationId`는 인플레이스 업그레이드를 위해 **`com.openterface.keymod`**로 유지

## 변경 없는 부분

**키보드 & 마우스 Pro**(Shortcut Hub 스트립, 분할 레이아웃, 풍부한 IME 동작이 있는 컴포지트 모드)는 이전과 동일한 풀 기능 경험으로 유지됩니다.

## 업데이트 받기

**이 버전 (0.15):** [KeyMod-release-0.15.apk](https://assets2.openterface.com/data/KeyMod-release-0.15.apk)

> **Beta 안내:** KeyMod Android 앱은 현재 활성 Beta 단계입니다. 소스 리포지토리는 아직 공개되지 않았습니다 — 크라우드펀딩 캠페인 성공 후 정식으로 오픈소스화할 예정입니다. 베타 테스터로서 최신 APK가 필요하시면 Discord로 연락해 주세요. 빌드를 보내드리겠습니다.

> **알려진 문제:** 이 버전에는 게임패드 프리셋 시스템과 Basic 키보드 티어에 대한 대폭적인 변경이 포함되어 있습니다. 개발 팀이 아직 내부 테스트 중이므로 버그를 마주칠 수 있습니다. 예상치 못한 동작이 있으면 Discord에서 보고해 주세요 — 여러분의 피드백이 더 빠른 안정화에 도움이 됩니다.

기존 설치는 인플레이스로 업그레이드됩니다.

## Mini-KVM 및 KVM-Go에서도 사용 가능

KeyMod 앱은 KeyMod 하드웨어에만 한정되지 않습니다. 기존 Openterface 사용자도 사용해 볼 수 있습니다:

- **KVM-Go**: **Bluetooth** 또는 **USB** 연결
- **Mini-KVM**: **USB** 연결

## 업그레이드 참고

- **게임패드**: 이전의 두 버튼 선호도는 첫 실행 시 자동으로 **Two buttons** 프리셋을 활성화합니다. 기존 1 Button / 2 Buttons 컨트롤 대신 **Preset**(탭으로 순환, 길게 눌러 목록)을 사용하세요.
- **키보드 & 마우스 (Basic)**: Basic을 열어 전체 화면 키보드를 경험하세요. Pro 모드는 탐색 서랍에서 완전한 Shortcut Hub 경험으로 이용 가능합니다.

감사합니다,

Openterface Team | TechxArtisan
