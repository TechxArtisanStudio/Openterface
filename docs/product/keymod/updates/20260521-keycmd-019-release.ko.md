---
draft: false
date: 2026-05-21
title: "KeyCmd 0.19: 앱 브랜딩 변경, KM Pro Compose 모드, 다국어 지원 및 모드별 가이드 투어"
description: "KeyCmd 0.19는 KeyMod에서 KeyCmd로의 주요 앱 브랜딩 변경, Unicode 호환 HID 전송을 지원하는 새로운 KM Pro Compose 모드, 다국어 UI(한국어, 이탈리아어, 러시아어, pt-BR), 모드별 인터랙티브 가이드 투어 및 수십 가지 UX 개선을 제공합니다."
keywords: "KeyCmd 0.19, KeyCmd 출시, 앱 브랜딩 변경, Compose 모드, Unicode HID 전송, 다국어, 인터랙티브 가이드 투어, Openterface KeyCmd 업데이트, HID 에뮬레이터, 가상 키보드, Android 키보드 앱"
author: "TechxArtisan Studio"
category: "Product Updates"
tags: ["KeyCmd", "Product Updates", "Release", "Compose", "i18n", "Android"]
featured: false
social:
  image: "https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp"
  title: "KeyCmd 0.19 출시 — Compose 모드, 앱 브랜딩 변경, 다국어, 가이드 투어"
  description: "KeyCmd 0.19는 새로운 Compose 모드, KeyCmd 앱 브랜딩 변경, 4개 신규 언어, 인터랙티브 가이드 투어 및 대폭적인 UX 개선을 제공합니다."
---

# KeyCmd 0.19: 앱 브랜딩 변경, KM Pro Compose 모드, 다국어 지원 및 모드별 가이드 투어

KeyCmd **0.19**(`versionCode` **19**)는 KeyMod에서 KeyCmd로의 **앱 브랜딩 변경**, Unicode 호환 HID 전송 기능을 갖춘 완전 새로운 **KM Pro Compose 모드**, 확장된 **다국어 UI**(한국어, 이탈리아어, 러시아어, 브라질 포르투갈어 포함), **모드별 인터랙티브 가이드 투어**, 그리고 키보드, 게임패드 및 프레젠테이션 모드에서의 수십 가지 UX 개선을 제공하는 주요 업데이트입니다.

## 앱 브랜딩 변경: KeyMod → KeyCmd

앱 표시 이름이 이제 모든 진입점에서 **KeyCmd**로 통일되었습니다. 이 브랜딩 변경으로 **KeyMod 하드웨어**와 **KeyCmd 동반 앱**의 구분이 명확해졌습니다.

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp" alt="KeyCmd 환영 화면" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">

### 변경 사항

- **앱 표시 이름**: 런처 아이콘과 시스템 UI에 이제 "KeyCmd"가 표시됩니다
- **환영 플로우**: KeyMod에서 KeyCmd로 워드마크 및 문구 업데이트
- **CI 아티팩트 및 APK 파일명**: **KeyCmd** 접두사 사용
- `applicationId`는 **`com.openterface.keymod`**로 유지되어 원활한 현장 업그레이드가 가능합니다

기존 사용자: 설정, 프로필 및 페어링된 기기가 모두 보존됩니다. 업그레이드는 원활합니다.

## 키보드 및 마우스: 전체 화면 경험

KeyCmd는 전체 화면 키보드, 터치패드 및 숫자 패드 경험을 제공합니다 — 세로 및 가로 방향 모두에 최적화되어 있습니다.

<div class="slideshow-container" id="slideshow-keycmd-019-kbm-ko" data-auto-slide="true" data-auto-slide-interval="3000">
  <div class="slideshow-wrapper">
    <div class="slide active">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Full-Keyboard-landscape.webp" alt="가로 전체 화면 키보드" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape.webp" alt="가로 숫자 패드" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-portrait.webp" alt="세로 숫자 패드" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait.webp" alt="세로 키보드 및 터치패드" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-km-basic-Touchpad.webp" alt="가로 터치패드" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Remote-Coding-portrait.webp" alt="KeyCmd로 원격 코딩" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Settings-screen.webp" alt="KeyCmd 설정 화면" style="max-height:320px;" loading="lazy">
    </div>
  </div>

  <div class="slideshow-navigation">
    <button class="nav-arrow left" onclick="changeSlide('slideshow-keycmd-019-kbm-ko', -1)">❮</button>
    <div class="slideshow-dots">
      <span class="dot active" onclick="currentSlide('slideshow-keycmd-019-kbm-ko', 1)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ko', 2)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ko', 3)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ko', 4)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ko', 5)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ko', 6)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ko', 7)"></span>
    </div>
    <button class="nav-arrow right" onclick="changeSlide('slideshow-keycmd-019-kbm-ko', 1)">❯</button>
  </div>
</div>

## KM Pro: Compose & Send 모드

0.19에서 가장 큰 신규 기능은 KM Pro의 **Compose 모드**입니다. 긴 텍스트를 입력하고 HID 키스트로크로 대상 머신에 보낼 수 있는 전용 텍스트 편집기입니다.

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait.webp" alt="Compose 모드에서 스크립트 실행" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">

<p><strong>Compose &amp; Send demo (YouTube Short)</strong></p>

<iframe width="560" height="315" loading="lazy" src="https://www.youtube.com/embed/_rJF-hTF3_E" title="KeyCmd Compose &amp; Send demo (YouTube Short)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


### Compose 편집기

- **상단 바로 가기 스트립 + 컴포즈 액션 행**에 **지우기** 및 **실행 취소/지우기** 컨트롤
- **초안 보존**: 하위 모드 전환 및 전송 성공 후에도 텍스트가 보존됩니다
- **IME 통합**: 스마트폰 키보드로 입력하고 깔끔한 HID 키스트로크로 전송
- **결정적 전송 진행률**: 긴 HID 버퍼에 대해 진행률 표시줄이 있어 전송이 얼마나 진행되었는지 정확히 알 수 있습니다

### Unicode 호환 HID 전송

- **듀얼 모드 위험 검토**: 비 ASCII 텍스트를 전송하기 전에 Unicode 호환성에 대해 경고하고 검사 및 미리보기 작업을 제공하는 대화 상자
- **macOS Unicode 16진수 플로우**: macOS 호스트에서 확장 문자에 Option+16진수 코드 입력 방법을 사용
- **더 안전한 전송 대화 상자**: 버퍼가 순수 ASCII인지 Unicode 문자를 포함하는지에 따라 내용을 조정하는 검토 화면
- **문자 검사 도구**: 전송 위험 대화 상자는 **검사** 및 **미리보기** 작업을 제공하며, macOS 호스트에는 전용 **Unicode 16진수 경로 감사** 항목 포함

### KM Basic 범위

0.19에서 **Compose & Send는 키보드 및 마우스 Pro의 기능**입니다. KM Basic은 전체 화면 키보드, 터치패드 및 숫자 패드 워크플로우에 집중합니다.

## 다국어 지원

KeyCmd는 이제 **11가지 앱 UI 언어**를 지원합니다. 이 릴리스에는 4가지 새로운 현지화가 추가되었습니다:

- **한국어 (ko)**: 전체 UI 번역
- **이탈리아어 (it)**: 전체 UI 번역
- **러시아어 (ru)**: 전체 UI 번역
- **브라질 포르투갈어 (pt-BR)**: 전체 UI 번역

기존 영어, 중국어 간체, 중국어 번체, 일본어, 프랑스어, 독일어, 스페인어와 함께 KeyCmd는 이제 전 세계 사용자 기반의 대부분을 커버합니다.

### 변경 사항

- 설정의 **언어 선택기**에 표준 앱 언어 이름 사용
- **Bluetooth 헤더** 및 **키 탭 미리보기** 현지화
- 모든 언어에서 Compose 경고 탭에 대한 **릴리스 lint** 수정

## 모드별 인터랙티브 가이드 투어

각 모드에는 이제 기능을 단계별로 안내하는 **내장 인터랙티브 가이드 투어**가 있습니다.

### 사용 가능한 투어

- **Shortcut Hub 투어**: 기본 프로필을 열고 세부 UI, 카테고리 탭 및 바로 가기 관리를 다룹니다
- **게임패드 투어**: 게임패드 레이아웃, 모듈 관리 및 프리셋 시스템을 설명합니다
- **KM Pro 투어**: Compose 모드, 바로 가기 패널 및 Pro 전용 기능을 다룹니다
- **KM Basic 투어**: 전체 화면 키보드, 수식어 키 길게 누른 스와이프 및 숫자 패드를 설명합니다

### 투어 기능

- **모드별 가이드**: 각 모드에 맞춰진 자체 가이드
- **재생 시트**: **모드 가이드** 버튼(연결 크롬 왼쪽의 아이콘)을 통해 언제든지 투어 다시 방문
- **i18n 지원**: 투어 콘텐츠는 앱 전체 언어로 현지화됨
- **가로 최적화**: 하단 시트 레이아웃이 가로 방향에서 올바르게 적응

## UX 개선

### 키보드

- **키 탭 미리보기**: 탭하기 전에 정확히 무엇이 전송될지 확인. 설정에서 활성화 가능. 기본 활성화.
- **빠른 탭 HID 수정**: 키 탭 해제 타이밍 개선 및 해제 이벤트 통합으로 더 빠른 타이핑 가능
- **대체 문자 탭 처리**: `a` 키를 길게 누르면 이제 ¥(위), £(왼쪽), €(오른쪽) 대체 문자가 개선된 시각적 피드백과 함께 표시
- **수식어 키 길게 누른 스와이프**: KM Basic/Pro 투어에서 수식어 키 빠른 액세스를 위한 길게 누른 스와이프 제스처를 가르치는 새로운 단계 추가

### 게임패드

- **편집 세션 바 제거**: 기존 편집 세션 도구 모음 없이 더 깔끔한 게임패드 크롬
- **게임패드 크롬 및 투어**: 새로운 시각적 폴리시 및 통합 가이드 투어
- **모드 가이드 아이콘**: 연결 크롬 왼쪽에 배치하여 쉽게 액세스

### 프레젠테이션

- **세로 쌍 잠금**: 프레젠테이션 모드는 안정적인 프레젠터 제어를 위해 세로 및 역세로 방향으로 제한

### UI 및 테마

- **액센트 견본**: 테마 색상 패밀리 스피너를 시각적 액센트 견본으로 교체하여 더 쉬운 색상 선택
- **UI 액센트 정렬**: 모든 UI 액센트가 이제 테마 색상 패밀리를 따름(기존 기본 색상 아님)
- **헤더 오른쪽 클러스터**: 기본 앱과 KM Basic 크롬 모두에서 연결 아이콘의 치수 개선
- **Compose 전송 버튼 스타일**: 라이트 모드에서 비 ASCII 전송 버튼 모양 정렬

### 설정

- **설정 재구성**: 표준 앱 언어 이름; 명확성을 위해 에뮬레이터 설치 스크립트 이름 변경
- **개발 헬퍼 스크립트**: 더 명확한 기기 식별 및 작업 이름 변경을 위해 이름 변경
- **FAQ 문서**: 현재 앱 동작을 반영하여 `docs/FAQ.md` 업데이트

## 실제 사용 사례

### 원격 코딩

KeyCmd는 서버 관리만을 위한 것이 아닙니다. 개발자는 **원격 코딩 세션**에 사용합니다. 전체 키보드, 터치패드 및 숫자 패드 지원과 함께 스마트폰 또는 태블릿에서 헤드리스 개발 박스를 제어할 수 있습니다.

## 변경되지 않은 부분

**키보드 및 마우스 Pro**(Shortcut Hub 바, 분할 레이아웃 및 풍부한 IME 동작을 갖춘 컴포지트 모드)는 이전과 동일한 완전한 기능 경험을 유지합니다. 기존 프로필, 프리셋 및 페어링된 기기가 모두 보존됩니다.

## 업데이트 받기

**이 버전 (0.19):** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

> **Beta 참고:** KeyCmd Android 앱은 아직 활발한 Beta 단계에 있습니다. 소스 저장소는 아직 공개되지 않았습니다. 성공적인 크라우드펀딩 캠페인 후 오픈소스로 전환할 예정입니다. Beta 테스트 사용자이며 최신 APK가 필요하시면 Discord에서 연락해 주세요. 빌드를 보내드리겠습니다.

기존 설치 프로그램은 현장에서 업그레이드됩니다.

## Mini-KVM 및 KVM-Go와 호환

KeyCmd 앱은 KeyMod 하드웨어에 국한되지 않습니다. 기존 Openterface 사용자도 사용해 볼 수 있습니다:

- **KVM-Go**: **Bluetooth** 또는 **USB**로 연결
- **Mini-KVM**: **USB**로 연결

## 업그레이드 참고

- **브랜딩 변경**: 앱 이름이 KeyMod에서 KeyCmd로 변경됩니다. 데이터는 보존됩니다.
- **Compose 모드**: 키보드 및 마우스 Pro에 새로 추가.
- **가이드 투어**: 모든 모드에서 가이드 아이콘(연결 크롬 왼쪽)을 탭하여 인터랙티브 투어를 시작하세요.
- **언어**: 설정에서 앱 언어를 변경하세요. KeyCmd는 이제 11가지 앱 UI 언어를 지원합니다.

감사합니다,

Openterface Team | TechxArtisan
