# Openterface QT for Win & Linux

이 문서는 Qt를 사용하여 개발된 크로스 플랫폼 KVM(키보드, 비디오, 마우스) 소프트웨어에 대한 개요를 제공하며, Linux 및 Windows 운영 체제와 호환됩니다. 이 소프트웨어는 호스트 시스템에서 대상 장치를 제어할 수 있도록 하며, 메뉴 바와 추가 기능을 통해 다양한 기능을 제공합니다.

## 메인 메뉴 바 기능

### 환경 설정

환경 설정 메뉴를 통해 사용자는 네 개의 페이지로 구성된 대화 상자를 통해 설정을 사용자 정의할 수 있습니다:<br>
![Preferences Gernal](https://assets.openterface.com/images/qt/preferenceGernal.webp)

-   **일반** 이 페이지는 디버깅 로그 필터와 애플리케이션 실행 시 화면 보호기 억제 여부를 설정합니다. 로그 카테고리에는 다음이 포함됩니다:

    -   Core
    -   Serial
    -   UserInterface
    -   host

    사용자는 로그를 .txt 파일로 저장하고 화면 보호기 억제 여부를 선택할 수 있습니다.<br>

![Preferences Video](https://assets.openterface.com/images/qt/preferenceVideo.webp)

-   **비디오** 이 페이지를 통해 사용자는 다음을 수행할 수 있습니다:

    -   캡처할 카메라 데이터를 선택합니다.
    -   해상도를 설정합니다.
    -   비디오 스트림 형식을 선택합니다.

-   **오디오** 이 페이지는 현재 개발 중입니다.<br>

![Preferences TargetControl](https://assets.openterface.com/images/qt/preferenceTargetControl.webp)

-   **대상 제어** 이 페이지는 대상 장치에 대한 제어 모드를 구성할 수 있는 옵션을 제공합니다:

    -   **제어 모드:**

        -   **키보드 + 마우스 + USB HID 장치**
        -   **USB 키보드**
        -   **키보드 + 마우스**
        -   **USB HID 장치**

    -   **대상에서 읽은 공급업체 ID(VID) 및 제품 ID(PID)를 설정합니다.**
    -   **대상의 USB 디스크립터를 정의합니다.**

### 편집

-   **붙여넣기:** 편집 메뉴의 붙여넣기 옵션과 왼쪽 상단 모서리의 붙여넣기 버튼을 통해 사용자는 호스트 클립보드의 텍스트를 대상 장치에 붙여넣을 수 있습니다.

### 제어

이 메뉴는 다음 옵션을 제공합니다:<br>

-   마우스 이동 모드 설정: 절대 또는 상대. **Control >> MouseMode >> Absolute or Relative.**
-   호스트의 마우스 커서 가시성 전환. **Control >> Mouse Visibility >> Auto Hide or Always Show.**
-   하드웨어의 USB 포트를 대상 및 호스트 사용 간 전환. **Control >> Switchable USB >> TO Target or To Host.**
-   칩 전송을 위한 보드레이트 조정. **Control >> Baudrate >> 9600, 115200.**

### 고급

고급 메뉴에는 다음 옵션이 포함됩니다:<br>
![Advance menu](https://assets.openterface.com/images/qt/menuAdvance.webp)

-   **환경 확인:** 소프트웨어에 필요한 드라이버가 설치되어 있는지 확인합니다.
-   **시리얼 포트 재설정:** 시리얼 포트를 다시 시작합니다.
-   **키보드 및 마우스 재설정:** 키보드 및 마우스 설정을 재설정합니다.
-   **HID 칩 공장 초기화:** HID 칩을 공장 설정으로 복원합니다.<br>
    ![Advance SerialConsole](https://assets.openterface.com/images/qt/advanceSerialConsole.webp)
-   **시리얼 콘솔:** 시리얼 포트로 전송된 모든 메시지를 모니터링할 수 있는 새 창을 엽니다. 전송/수신 메시지에 대한 필터가 있습니다.<br>
    ![Advance ScriptTool](https://assets.openterface.com/images/qt/advanceScriptTool.webp)
-   **스크립트 도구:** AutoHotkey (AHK) 스크립트를 실행합니다. 이 기능은 AutoHotkey를 모방하지만 마우스/키보드 기능 및 스크린샷 기능의 일부만 지원합니다. 스크립트는 대상 장치에 영향을 미칩니다.
-   **TCP 서버:** TCP를 통해 AutoHotkey 명령을 수신하여 대상 장치에서 실행합니다.
-   **펌웨어 업데이트:** 원격 서버에서 최신 펌웨어를 가져와 사용자가 장치에 플래시할지 선택할 수 있습니다.

### 언어

인터페이스 언어는 다음으로 설정할 수 있습니다:

-   덴마크어
-   영어
-   독일어
-   프랑스어
-   일본어
-   스웨덴어

### 도움말

도움말 메뉴는 다음을 제공합니다: <br>
![Help menu](https://assets.openterface.com/images/qt/menuHelp.webp)

-   공식 웹사이트 및 소프트웨어/하드웨어 문제에 대한 피드백 양식 링크.
-   하드웨어 구매에 대한 정보.
-   소프트웨어 환경에 대한 설명.
-   정보: 조직에 대한 세부 정보.
-   업데이트: 소프트웨어 업데이트 확인.

## 메뉴 바 기능 (왼쪽에서 오른쪽으로)

메뉴 바는 왼쪽에서 오른쪽으로 다음 기능을 포함합니다:<br>

![MenuBar](https://assets.openterface.com/images/qt/menubar.webp)

-   키보드 레이아웃 선택: 키보드 레이아웃을 선택합니다.
-   줌 컨트롤: 캡처된 비디오 스트림의 디스플레이를 확대, 축소 또는 재설정합니다.
-   가상 키보드: 기능 키 및 사전 설정된 단축키 조합을 포함합니다.
-   스크린샷: 전체 대상 화면을 캡처하여 기본 폴더에 저장합니다.
-   전체 화면 모드: 전체 화면 디스플레이를 전환합니다.
-   붙여넣기: 호스트 클립보드의 텍스트를 대상에 붙여넣습니다.
-   마우스 댄스: 마우스가 사전 설정된 움직임을 수행하도록 트리거합니다.
-   USB 장치 표시기: USB 장치가 대상 또는 호스트에 할당되었는지 표시합니다.

그동안, 최신 코드, 업데이트, 예제 및 문제 보고를 위해 오픈 소스 **GitHub 저장소**: [Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT)를 자유롭게 탐색하세요.

또한, [Discord 커뮤니티](/discord)에 가입하여 개발 팀 및 다른 멋진 사용자들과 KVM 관련 주제를 논의할 수 있습니다.

직접적인 지원이 필요하시면 [support@openterface.com](mailto:support@openterface.com)으로 이메일을 보내주세요.

---

**이 페이지에 대한 피드백이 있습니까?** [여기에서 알려주세요.](https://forms.gle/wmxoR2C1VdG36mT69)
