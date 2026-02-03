---
title: Ubuntu 복사/붙여넣기 팁 (macOS → Ubuntu)
description: Openterface로 macOS에서 Ubuntu를 제어할 때 붙여넣기 단축키 수정 방법. Ctrl 스타일 붙여넣기를 위해 Windows 모드를 사용하거나, Mac 모드에서는 편집 → 붙여넣기를 대안으로 사용하세요.
keywords: Openterface, macOS, Ubuntu, 복사 붙여넣기, 키보드 모드, Windows 모드, Mac 모드, KVM, 원격 데스크톱
author: Openterface
date: 2026-02-03
tags:
  - macOS
  - Ubuntu
  - keyboard
  - copy-paste
---

# Ubuntu 복사/붙여넣기 팁 (macOS → Ubuntu)

**Openterface**를 사용해 **macOS**에서 **Ubuntu**를 제어할 때 **Mac 모드**에서는 단축키 붙여넣기가 안정적으로 작동하지 않을 수 있습니다. 이 가이드에서는 권장 수정 방법과 간단한 대안을 안내합니다.

![setting](https://assets2.openterface.com/images/setting.webp)

---

## 빠른 수정 (Ubuntu/Linux 권장)

1. macOS에서 **Openterface**를 엽니다.
2. **설정**으로 이동합니다.
3. **대상 장치 키보드 레이아웃 모드**를 찾습니다.
4. **Windows 모드**를 선택합니다.

![win-mode](https://assets2.openterface.com/images/win-mode.webp)


✅ 결과: Ubuntu에서 붙여넣기 단축키가 예상대로 작동합니다 (Ctrl 스타일 동작).

![win-ctrl+v](https://assets2.openterface.com/images/win-ctrl+v.webp)

---

## 대안 (Mac 모드를 유지하려는 경우)

**Mac 모드**를 유지하려면 메뉴를 통해 안정적으로 붙여넣을 수 있습니다:

- **편집 → 붙여넣기**

![edit-paste](https://assets2.openterface.com/images/edit-paste.webp)

✅ 결과: Mac 모드에서 단축키 붙여넣기가 불안정해도 메뉴 붙여넣기는 안정적으로 작동합니다.

![workaround](https://assets2.openterface.com/images/workaround.webp)

---

## 왜 이런 현상이 발생하는가

대부분의 Ubuntu 앱은 붙여넣기에 **Ctrl 기반** 단축키를 사용합니다. 일부 환경에서는 **Mac 모드** 단축키 매핑이 붙여넣기를 일관되게 트리거하지 않을 수 있지만, **편집 → 붙여넣기**는 안정적으로 작동합니다.

---

## 빠른 요약

- **Ubuntu/Linux 최상의 경험:** **Windows 모드** 사용
- **Mac 모드 유지 시:** **편집 → 붙여넣기** 사용

---

## 어떤 모드를 사용해야 할지 모르시나요?

어떤 모드를 사용해야 할지 확실하지 않다면 다음 간단한 기준을 참고하세요:

- 대상 OS가 **Ubuntu/Linux**인 경우 **Windows 모드**로 시작하세요 (일반적인 단축키에서 가장 일관적입니다).
- 주로 **macOS 대상**을 제어하고 Mac 스타일 단축키를 원한다면 **Mac 모드**를 사용하세요.

다양한 대상 OS를 자주 전환한다면 이 페이지를 북마크해 두세요. 보통 한 번의 클릭으로 수정할 수 있습니다.

---

## 자주 묻는 질문

**Windows 모드가 Mac 단축키를 변경하나요?**  
Openterface가 **대상 장치**에 보내는 단축키 방식을 변경하므로 Ubuntu는 예상되는 **Ctrl 스타일** 동작을 받습니다.

**모든 모드에서 메뉴 붙여넣기를 사용할 수 있나요?**  
예 — **편집 → 붙여넣기**는 두 모드 모두에서 안정적인 옵션입니다.

**Raspberry Pi OS에도 영향을 미치나요?**  
영향을 덜 받는 경우가 많지만, 유사한 동작이 보이면 동일한 수정이 적용됩니다.
