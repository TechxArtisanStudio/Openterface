---
title: "Openterface Mini-KVM - 진단 자기 점검 가이드 (macOS)"
description: "macOS 앱으로 Openterface Mini-KVM 장치에서 진단 자기 점검을 실행하는 단계별 가이드입니다. USB 연결 테스트, 문제 감지 및 지원팀에 결함 보고서를 보내는 방법을 학습하세요."
keywords: "Openterface Mini-KVM, macOS, 진단 자기 점검, KVM 문제 해결, USB KVM 진단, Mini-KVM 지원, KVM 장치 테스트, USB 연결 테스트, KVM 결함 보고, Mini-KVM 문제 해결 가이드, KVM 진단 도구, 헤드리스 서버 진단, IT 문제 해결 도구"
---

# Openterface Mini-KVM - 진단 자기 점검 가이드 (macOS)

이 가이드는 Openterface Mini-KVM 장치에서 진단 자기 점검을 실행하는 단계별 지침을 제공합니다.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-K6Idzky3fY?si=r7pZgCkBzzZXgrLT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## 정상 작동 상태

**단계 1:** Openterface 앱에서 설정 → 설정...을 열어주세요.

**단계 2:** 설정 창에서 고급 및 디버그로 이동합니다.

**단계 3:** 진단 도구를 열기 클릭합니다.

**단계 4:** 프롬프트가 나타나면 진단 로깅을 활성화하기 위해 Enable을 클릭합니다.

**단계 5:** Check Now를 클릭하여 자기 점검을 시작합니다.

**단계 6:** Start Test를 클릭한 후, 요청 시 검은색 USB-C (대상 측)을 뽑고 다시 꽂아주세요.

![minikvm-support-target](https://assets.openterface.com/images/minikvm/support/target.webp)

**단계 7:** Start Test를 클릭한 후, 요청 시 주황색 USB-C (호스트 측)을 뽑고 다시 꽂아주세요.

![minikvm-support-host](https://assets.openterface.com/images/minikvm/support/host.webp)

**단계 8:** Start Test를 클릭하고 테스트가 완료될 때까지 기다리세요.

**단계 9:** Reset Now를 클릭하고 완료될 때까지 기다리세요.

**단계 10:** Change Now를 클릭하고 baudrate 전환 완료까지 기다리세요.

**단계 11:** Start Test를 클릭하고 약 30초 정도 기다리세요. 테스트가 진행되는 동안 대상 장치를 조작하지 마세요.

> **참고:** 마우스가 빠르게 움직일 수 있습니다. 대상 장치에 손을 대지 마세요.

![minikvm-support-stress_test](https://assets.openterface.com/images/minikvm/support/stress_test.gif)

**단계 12:** 모든 항목이 녹색 확인 표시로 나타나고 진행률이 완료되었는지 확인하세요.

**단계 13:** Diagnostics 창을 닫기 위해 상단 오른쪽의 ❌를 클릭합니다.

---

## 문제 감지 (키보드/마우스 예시)

"정상 작동 상태" 섹션의 단계 1~11을 먼저 따르세요. 아래 노트는 키보드/마우스 문제 감지 시 보게 되는 내용을 설명합니다.

## 이 문제가 어떻게 나타나는가

이 예시에서 전체 연결이 처음에는 FAIL로 표시되는데, 이는 대상 측 키보드/마우스(HID) 문제로 인한 것으로, 전체 점검에 영향을 줍니다. 이는 초기 지표이며 별도의 문제는 아닙니다.(왼쪽에 "전체 연결" 옆에 FAIL 상태가 강조 표시됩니다.)

- **전체 연결:** 대상 측 문제로 인해 여기서 처음으로 FAIL이 표시됩니다.

![minikvm-support-overall_connection](https://assets.openterface.com/images/minikvm/support/overall_connection.webp)

- **대상 플러그 앤 플레이:** 이 단계를 실행한 후, 대상 측 문제를 더 명확하게 보여줄 수 있습니다.

> **팁:** 단계가 FAIL을 표시하면 진단이 중지되지 않지만, 자동 진행이 멈출 수 있으므로 계속 수동으로 진행해야 합니다.

## 추가 최종 테스트 (문제 유형에 따라 다름)

**단계 12:** 스트레스 테스트 후, 감지된 문제에 따라 진단이 추가 최종 테스트를 표시할 수 있습니다. 이 키보드/마우스 예시에서는 Target Port Checking으로 계속됩니다.

**단계 13:** "장치 감지"를 클릭하여 Target Port Checking을 시작하고 화면의 지시사항을 따르세요.

![minikvm-support-target_port_checking](https://assets.openterface.com/images/minikvm/support/target_port_checking.webp)

## 문제 감지 시 발생하는 일

**단계 14:** 계속하려면 하단 바의 Next를 클릭하거나 왼쪽 패널에서 다음 테스트를 선택하세요.

![minikvm-support-target_plug_n_play](https://assets.openterface.com/images/minikvm/support/target_plug_n_play.webp)

## 로그를 지원팀에 보내기

**단계 15:** 지원팀으로 결함 보고서를 준비하기 위해 Send Defect Report to Support을 클릭하세요.

![minikvm-support-send_defect_report_to_support](https://assets.openterface.com/images/minikvm/support/send_defect_report_to_support.webp)

**단계 16:** Defect Report 창에서 **주문 번호**와 **이름**을 입력한 후 **적용**을 클릭하여 이메일 초안에 삽입하세요.

**단계 17:** 이메일 주소와 초안을 복사합니다:
- **이메일 복사**를 클릭하여 지원 이메일 주소를 복사합니다.
- **초안 복사**를 클릭하여 미리 작성된 이메일 내용(주문 번호 + 이름 포함)을 복사합니다.
- 둘 다 이메일 클라이언트(Gmail/Outlook 등)에 붙여넣으세요.

![minikvm-support-support](https://assets.openterface.com/images/minikvm/support/support.webp)

**단계 18:** **로그 폴더 열기**를 클릭하세요. 도구가 첨부할 파일을 표시합니다. **요청된 로그 파일만 첨부하세요** (폴더에 다른 많은 로그가 포함되어 있을 수 있습니다).

**단계 19:** 같은 이메일에 명확한 **설치 사진**을 첨부하세요. 사진에는 다음이 보여야 합니다:
- Mini-KVM 장치,
- **호스트**와 **대상** 연결 모두,
- 포트와 케이블이 선명하게 보여야 합니다.

**단계 20:** 지원팀에 이메일을 보내세요 (초안 텍스트 + 요청된 로그 + 설치 사진 첨부).

**단계 21:** Diagnostics 창을 닫기 위해 상단 오른쪽의 ❌를 클릭합니다.