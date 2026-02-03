---
draft: false
date: 2026-02-03
title: "KVM-GO의 microSD EXPRESS: 호환성 테스트 및 실제 전송 속도"
description: "KVM-GO microSD EXPRESS 호환성 테스트, SanDisk 128GB 카드 사용. 확인: 감지 및 읽기/쓰기 정상. 실제 속도 약 30 MB/s 쓰기, 20 MB/s 읽기, USB 2.0 브리지로 인한 제한. UHS-I 카드로 KVM-GO microSD 경로에 충분."
keywords: "KVM-GO microSD, microSD EXPRESS KVM-GO, KVM-GO 스토리지, SanDisk microSD EXPRESS, KVM-GO 호환성, USB 2.0 microSD, KVM-GO 전송 속도, microSD 카드 KVM-GO, Openterface KVM-GO"
author: "Openterface 팀 | TechxArtisan"
category: "제품 업데이트"
tags: ["KVM-GO", "제품 업데이트", "microSD", "스토리지", "호환성", "성능"]
featured: false
social:
  image: "https://assets2.openterface.com/images/blog/SD-card.webp"
  title: "KVM-GO의 microSD EXPRESS: 호환성 및 속도 테스트"
  description: "SanDisk microSD EXPRESS 카드를 KVM-GO에서 테스트했습니다. 작동하지만 속도는 USB 2.0 브리지로 제한—UHS-I로 충분합니다."
---

# KVM-GO의 microSD EXPRESS: 호환성 테스트 및 실제 전송 속도

커뮤니티 멤버가 KVM-GO가 microSD EXPRESS 카드를 지원하는지 물었습니다. 추측하지 않고 실제 microSD EXPRESS 카드를 구입하여 간단한 호환성 및 속도 테스트를 진행했습니다.

---

## 테스트 내용

- **카드:** SanDisk microSD EXPRESS 128GB  

![테스트용 카드: SanDisk microSD EXPRESS 128GB.](https://assets2.openterface.com/images/blog/SD-card.webp)  
*테스트용 카드: SanDisk microSD EXPRESS 128GB.*

- **목표:** 기본 호환성(감지 + 읽기/쓰기) 확인 및 KVM-GO microSD 경로를 통한 실제 전송 속도 측정.

---

## 테스트 환경

간단한 "실제 사용" 스타일 전송 테스트였습니다:

1. microSD EXPRESS 카드를 KVM-GO의 microSD 슬롯에 삽입.  
2. Windows PC에서 대용량 폴더/파일 세트를 microSD 카드에 복사하여 지속 쓰기 속도 관찰.  
3. microSD 카드에서 PC로 데이터를 복사하여 지속 읽기 속도 관찰.  
4. 일반 OS 파일 복사를 사용하고 Windows 전송 대화상자에 표시되는 속도를 기록.

![테스트 환경: 읽기/쓰기 검사를 위해 microSD EXPRESS를 KVM-GO에 삽입.](https://assets2.openterface.com/images/blog/plug.webp)  
*테스트 환경: 읽기/쓰기 검사를 위해 microSD EXPRESS를 KVM-GO에 삽입.*

---

## 호환성 결과

KVM-GO는 SanDisk microSD EXPRESS 카드를 정상적으로 인식합니다.  
읽기와 쓰기 모두 문제 없이 작동합니다.

따라서 "작동하나요?"라는 질문에 대한 답은 **예**입니다.

---

## 전송 속도 결과

카드가 microSD EXPRESS이지만, 여기서 얻는 전송 속도는 KVM-GO 내부의 스토리지 경로에 따라 달라집니다.

테스트에서 대략 다음을 관찰했습니다:

- **쓰기 속도:** 약 **30 MB/s** 

![쓰기 테스트 (PC → microSD): 파일 복사 중 약 28 MB/s 관찰.](https://assets2.openterface.com/images/blog/Performance.webp) 
*쓰기 테스트 (PC → microSD): 파일 복사 중 약 28 MB/s 관찰.*

- **읽기 속도:** 약 **20 MB/s**

![읽기 테스트 (microSD → PC): 파일 복사 중 약 22 MB/s 관찰.](https://assets2.openterface.com/images/blog/Performance2.webp)  
*읽기 테스트 (microSD → PC): 파일 복사 중 약 22 MB/s 관찰.*

이 수치는 파일 크기, 대소 파일 혼합, OS 캐싱 동작, 전체 워크로드에 따라 달라질 수 있지만, 일관되게 관찰된 범위입니다.

---

## Express 속도가 나오지 않는 이유

microSD EXPRESS 카드는 적절한 환경에서 훨씬 높은 성능을 발휘할 수 있지만, KVM-GO의 microSD 스토리지 경로는 microSD-USB 스토리지용 내부 브리지/컨트롤러로 제한됩니다.

KVM-GO에서 해당 브리지는 USB 2.0으로 동작합니다. USB 2.0은 480 Mbps(이론적)로 설명되지만, 실제 파일 전송에서는 프로토콜 오버헤드와 구현 세부사항으로 인해 지속 처리량이 일반적으로 훨씬 낮습니다.

![USB 2.0 스토리지 경로 참조.](https://assets2.openterface.com/images/blog/USB.webp)
*microSD 스토리지 브리지는 USB 2.0(이론적 480 Mbps). 실제 파일 전송 처리량은 낮음.*

그래서 microSD EXPRESS는 KVM-GO에서 잘 작동하지만, 이 microSD 경로를 통해 Express 수준의 속도를 기대하면 안 됩니다.

---

## 실용적 요약

1. **microSD EXPRESS는 KVM-GO와 호환**  
   정상적으로 감지되며 읽기/쓰기가 작동합니다.

2. **KVM-GO의 microSD 경로를 통해 Express 수준 속도는 나오지 않음**  
   병목은 내부 USB 2.0 스토리지 브리지이며, 카드 자체가 아닙니다.

3. **어떤 카드를 구매할지**  
   KVM-GO의 microSD 기능용으로 주로 구매하는 경우, 이 시나리오에서는 인터페이스가 제한 요인이므로 좋은 UHS-I microSD 카드로 충분합니다.

4. **Express 속도가 필요한 경우**  
   더 빠른 USB 인터페이스의 전용 microSD EXPRESS 리더 사용(KVM-GO와 별도).

---

## 다른 카드 테스트 요청

특정 microSD EXPRESS 모델(브랜드 + 용량 + 모델 번호)에 대해 알고 싶다면 공유해 주시면 동일한 검사를 실행하고 결과를 추가하겠습니다.
