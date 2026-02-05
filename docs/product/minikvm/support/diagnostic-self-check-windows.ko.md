---
title: "Openterface Mini-KVM (Windows) - 하드웨어 진단 자기 점검 가이드"
description: "Windows Openterface 앱에서 하드웨어 진단 자기 점검을 실행하는 단계별 가이드입니다. USB 연결 테스트, 문제 감지 및 지원팀에 진단 보고서를 보내는 방법을 학습하세요."
keywords: "Openterface Mini-KVM, Windows, 하드웨어 진단, 진단 자기 점검, KVM 문제 해결, USB KVM 진단, Mini-KVM 지원, KVM 장치 테스트, Windows KVM, KVM 결함 보고, Mini-KVM 문제 해결 가이드"
---

# Openterface Mini-KVM (Windows) — 하드웨어 진단 자기 점검 가이드

이 가이드는 **Windows** 버전 Openterface 앱에서 **하드웨어 진단** 자기 점검을 실행하는 방법과 문제가 감지된 경우 지원팀에 진단 보고서를 보내는 방법을 설명합니다.

<iframe width="560" height="315" src="https://www.youtube.com/embed/uSq3BDc_SBU?si=rREugsUxX1FzDGqm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## 시작하기 전에

- Mini-KVM을 **호스트**와 **대상** 모두에 연결하세요.
- 테스트 중(특히 스트레스 테스트 중)에는 대상 장치를 유휴 상태로 유지하세요.

> **중요 (Windows):** 진단은 **자동으로 진행되지 않습니다**.  
> 테스트 간 이동하려면 **Next**(하단 바)를 사용하거나 **왼쪽 패널**의 테스트 항목을 클릭하세요.  
> 각 테스트는 **Check Now**를 클릭하여 실행합니다.

![next_webp](https://assets2.openterface.com/images/next.webp)

---

## 정상 작동 상태 (PASS)

### 단계 1 — 하드웨어 진단 열기 (Windows)
Windows Openterface 앱에서 **Advanced → Hardware Diagnostics**를 엽니다.  

### 단계 2 — 자기 점검 실행
하드웨어 진단 창에서 **Check Now**를 클릭하여 현재 진단 단계를 실행합니다.  

### 단계 3 — 대상 Plug & Play (프롬프트 따르기)
**Target Plug & Play**가 대상 케이블 재연결을 요청하면 화면의 지시사항을 따르세요.  
일부 설정에서는 **한 번 이상** (예: 두 번) 뽑았다가 다시 꽂으라고 요청할 수 있습니다.  

![Target-plug&play](https://assets2.openterface.com/images/Target-plug%26play.webp)

### 단계 4 — 호스트 Plug & Play (프롬프트 따르기)
호스트 측 화면의 지시사항을 따르세요.  

![Host-plug&play](https://assets2.openterface.com/images/Host-plug%26play.webp)

### 단계 5 — 스트레스 테스트 (대상 장치에 손대지 마세요)
**Stress Test** 중 대상 마우스가 감지를 위해 자동으로 움직일 수 있습니다.  
테스트가 실행되는 동안 **대상 장치를 조작하지 마세요**.  

> **참고:** 마우스가 빠르게 움직일 수 있습니다 — 대상 장치에 손을 대지 마세요.

![stress-test](https://assets2.openterface.com/images/stress-test.webp)

### 단계 6 — PASS 확인
자기 점검이 완료될 때까지 계속하세요. 모든 것이 정상이면 결과에 **PASS / All Tests Passed**가 표시됩니다.  

---

## 문제 감지 (키보드/마우스 예시)

문제가 감지되면 하나 이상의 항목에 **FAIL**이 표시될 수 있습니다.

### 단계 1 — 동일한 하드웨어 진단 실행
**Advanced → Hardware Diagnostics**를 열고 **Check Now**를 클릭하여 시작하세요.  

### 단계 2 — 점검 계속 진행
진단이 완료될 때까지 나머지 테스트를 계속하세요.  

### 단계 3 — 지원 이메일이 자동으로 열림
문제가 있는 상태로 진단이 완료되면 **Support Email** 창이 자동으로 열립니다.  

---

## 로그를 지원팀에 보내기 (Windows)

### 단계 4 — 주문 번호 + 이름 적용
**주문 번호**와 **이름**을 입력한 후 **적용**을 클릭하여 이메일 초안에 삽입하세요. 

![ID+Name](https://assets2.openterface.com/images/ID+Name.webp)

### 단계 5 — 이메일 주소와 초안 복사
- **Copy Email**을 클릭하여 지원 이메일 주소를 복사합니다.
- **Copy Draft**를 클릭하여 미리 작성된 이메일 내용(주문 번호 + 이름 포함)을 복사합니다.  
둘 다 이메일 클라이언트(Gmail/Outlook 등)에 붙여넣으세요.  

![copy](https://assets2.openterface.com/images/copy.webp)

### 단계 6 — 올바른 로그 파일 첨부
**Open File Folder**를 클릭하세요. 도구가 첨부할 파일을 표시합니다.  
**요청된 로그 파일만 첨부하세요** (폴더에 다른 많은 로그가 포함되어 있을 수 있습니다).  

![list](https://assets2.openterface.com/images/list.webp)

![compress](https://assets2.openterface.com/images/compress.webp)

### 단계 7 — 설치 사진도 첨부
같은 이메일에 명확한 **설치 사진**을 첨부하세요. 사진에는 다음이 보여야 합니다:
- Mini-KVM 장치,
- **호스트**와 **대상** 연결 모두,
- 포트와 케이블이 선명하게 보여야 합니다.  

### 단계 8 — 이메일 보내기
지원팀에 이메일을 보내세요 (초안 텍스트 + 요청된 로그 + 설치 사진 첨부).  

---

## 지원팀에 연락할 때 포함할 내용

- **주문 번호**
- **요청된 진단 로그 파일**
- **설치 사진** (Mini-KVM + 호스트/대상 배선)
