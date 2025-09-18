# 소프트웨어

Openterface™ KVM 가젯을 실행하려면 호스트 컴퓨터에 아래 나열된 앱 중 하나를 설치해야 합니다. 다양한 앱 플랫폼에서 이러한 앱을 다운로드하거나 제공된 링크를 클릭할 수 있습니다. 모험을 즐긴다면 GitHub 저장소를 사용하여 소스에서 직접 빌드할 수도 있습니다!

![use-case-pc-angled-view](https://assets.openterface.com/images/product/use-case-pc-angled-view.webp){ width=600 }

## 다운로드 및 설치

<div class="grid cards" markdown>

-   ### :fontawesome-brands-windows:{ .lg } **Windows**

    ***

    **Openterface QT Win**용 다운로드 또는 소스에서 빌드:

    [:octicons-download-24: {{qt_version}} 설치 프로그램 다운로드](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.windows.amd64.installer.exe) <br>
    [:octicons-download-24: {{qt_version}} 포터블 EXE 다운로드](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT-portable.exe) <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) <br>
    [:octicons-play-24: 데모 보기](https://youtu.be/ERzpGtRvP2o?si=e9k402f0nxsD8o2j)

-   ### :fontawesome-brands-apple:{ .lg } **macOS**

    ***

    **Openterface MacOS**용 다운로드 또는 소스에서 빌드:

    [:octicons-arrow-right-24: App Store에서 설치](/appstore) <br>
    [:octicons-download-24: 포터블 DMG 다운로드](macos/dmg-installation.md) <br>
    [:octicons-mark-github-16: Openterface_MacOS](https://github.com/TechxArtisanStudio/Openterface_MacOS) <br>
    [:octicons-play-24: 데모 보기](https://youtu.be/m7OpUem0zqY?si=tclfl0Jl77tmE6_e)

-   ### :fontawesome-brands-linux:{ .lg } **Linux**

    ***

    **Openterface QT Linux**용 다운로드 또는 소스에서 빌드:

    [:octicons-download-24: {{qt_linux_stable}} AMD64 DEB 다운로드](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_linux_stable}}/openterfaceQT.linux.amd64.deb) <br>
    [:octicons-download-24: {{qt_linux_stable}} AMD64 RPM 다운로드](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_linux_stable}}/openterfaceQT.linux.amd64.rpm) <br>
    [:octicons-download-24: {{qt_linux_stable}} AMD64 AppImage 다운로드](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_linux_stable}}/openterfaceQT.linux.amd64.AppImage) <br>
    [:octicons-download-24: {{qt_linux_stable}} ARM64 DEB 다운로드](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_linux_stable}}/openterfaceQT.linux.arm64.deb) <br>
    [:octicons-download-24: {{qt_linux_stable}} ARM64 RPM 다운로드](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_linux_stable}}/openterfaceQT.linux.arm64.rpm) <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) <br>
    [:octicons-play-24: 데모 보기](https://youtu.be/_ScpI6TC0Pk?si=FSg7A2zmST8QbFec)

-   ### :fontawesome-brands-android:{ .lg } **Android**

    ***

    **Android APK**용 다운로드 또는 소스에서 빌드:

    [:octicons-download-24: {{android_version}} 다운로드](https://github.com/TechxArtisanStudio/Openterface_Android/releases/download/{{android_version}}/OpenterfaceAndroid-release.apk) <br>
    [:octicons-mark-github-16: Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) <br>
    [:octicons-play-24: 데모 보기](https://x.com/TechxArtisan/status/1825460088922071398)

</div>

???+ warning "주의: 타사 앱의 개인정보 보호 및 보안 확인"
모든 앱이 오픈 소스이기 때문에 다른 사람들이 만든 Openterface 장치용 호스트 애플리케이션의 대안 버전을 접할 수 있습니다. 이들은 꽤 멋지고 추가 기능을 제공할 수 있지만, 친절한 알림입니다: 보안 및 개인정보 보호 관행을 신중하게 검토하세요—특히 KVM 제어가 화면, 키보드, 마우스의 이벤트를 포함하기 때문입니다. Openterface 팀은 이러한 타사 앱의 안전성을 보장할 수 없으므로 주의해서 진행하세요!

## 기본 호스트 앱 컨트롤

### 💻 호환성

-   **호스트 소프트웨어**: macOS, Windows 또는 Linux용 호스트 앱을 설치하세요.
-   **대상 장치**: 설정이 필요하지 않습니다—비디오 출력(HDMI, VGA 등)과 키보드/마우스 제어용 USB 포트가 있는 모든 장치를 연결하기만 하면 됩니다. Windows, macOS, Linux, Android, iOS와 함께 작동합니다.

### 🖱 마우스 모드

-   **절대 모드**: 호스트 마우스가 대상 화면 위치에 직접 매핑됩니다.
-   **상대 모드**: 현재 위치를 기준으로 대상 커서를 이동합니다. 단축키로 종료할 수 있습니다.

### ⌨️ 키보드

앱이 포커스되어 있을 때 호스트의 키 입력이 대상으로 직접 전송됩니다.

### ⚙️ BIOS 접근

대상 BIOS를 직접 제어합니다.  
일반적인 키: F2 (Dell/Lenovo/ASUS), F10 (HP), Del (ASUS/Gigabyte/MSI), ⌥ (Apple).

### 🔊 오디오

대상 오디오가 HDMI를 통해 스트리밍되어 호스트 컴퓨터에서 재생됩니다.

### 🎥 비디오

앱 내에서 대상 화면을 직접 볼 수 있습니다.

-   **현재 모델**: 앱 내에서 최대 **1080p 30Hz** 디스플레이를 지원하며, HDMI를 통한 **4K 30Hz 입력**을 지원합니다.
-   **기타 입력**: 적절한 어댑터를 사용할 때 VGA, DVI, Micro HDMI 등과 호환됩니다.
-   **향후 모델**: 새로운 하드웨어 버전이 출시되면 더 높은 해상도와 프레임 레이트가 지원될 예정입니다.

### 🔄 전환 가능한 포트

일부 Openterface 장치에는 호스트와 대상 간에 **전환할 수 있는** 포트가 포함되어 있습니다. 예를 들어 USB 2.0 포트나 micro-SD 카드 슬롯(출시 예정 모델)이 있습니다.

-   **한 번에 하나씩 사용**: 한 번에 한 쪽(호스트 또는 대상)만 포트에 접근할 수 있습니다.
-   **전환 방법**:
    -   **하드웨어 토글** — 장치의 물리적 스위치
    -   **소프트웨어 버튼** — 호스트 앱을 통한 제어
-   **중요사항**:
    -   전환하기 전에 저장 장치(USB 드라이브 또는 micro-SD 카드)를 안전하게 제거하세요.
    -   불안정성이나 손상을 방지하기 위해 고전력 장치 연결을 피하세요.
    -   자세한 내용과 논리 다이어그램은 [전환 가능한 포트 가이드](/usb-switch)를 참조하세요.
