# Openterface Android

## 개요

Openterface Mini-KVM은 Android 기반 인터페이스를 통해 장치를 제어하기 위한 기본 KVM(키보드, 비디오, 마우스) 기능을 제공하도록 설계된 오픈 소스 하드웨어 및 소프트웨어 솔루션입니다. 이 저장소에는 Android 애플리케이션 소스 코드, 빌드 구성 및 프로젝트 설정 및 배포를 위한 지원 스크립트가 포함되어 있습니다.

우리는 오픈 하드웨어와 오픈 소스 소프트웨어에 전념하고 있으며, [GNU Affero General Public License v3](LICENSE) 하에 라이선스가 부여됩니다.

## 기능 모듈

### 1. 비디오 디스플레이

#### 주요 기능

- 연결된 대상 장치의 비디오 출력을 Android 화면에 실시간으로 스트리밍합니다.
- 최적의 시청을 위한 이미지 조정을 지원합니다.

![image](https://assets.openterface.com/images/android/videoConnect.webp)

#### 사용자 인터페이스 설명

- 메인 화면은 대상 장치의 비디오 피드를 표시하며, 인터페이스의 대부분을 차지합니다.
- 측면의 툴바는 조정 컨트롤(밝기, 대비, 색조)을 제공합니다.

#### 작동 흐름

1. Mini-KVM 하드웨어를 HDMI 및 USB를 통해 대상 장치에 연결합니다.
2. Mini-KVM을 USB-C를 통해 Android 장치에 연결합니다.
3. 앱을 실행하면 비디오 피드가 자동으로 나타납니다.
4. 필요에 따라 툴바 슬라이더를 사용하여 밝기, 대비 또는 색조를 조정합니다.

![image](https://assets.openterface.com/images/android/colorSetting.webp)

#### 특별 기능

- 두 손가락으로 확대하여 디스플레이를 더 잘 보이게 합니다.

![image](https://assets.openterface.com/images/android/enlargeAndSideBar.webp)

---

### 2. 마우스 제어

#### 주요 기능

- 대상 장치의 인터페이스와 상호 작용하기 위한 절대 및 상대 마우스 제어를 제공합니다.
- 왼쪽 및 오른쪽 클릭을 지원합니다.
- 오른쪽 메뉴에서 모드를 선택합니다.

#### 사용자 인터페이스 설명

- 비디오 피드는 마우스 입력을 위한 터치패드로도 사용됩니다.
- 플로팅 액션 버튼(FAB)은 마우스와 키보드 모드 간 전환을 제공합니다.

#### 작동 흐름

1. 장치가 성공적으로 연결되었는지 확인합니다.
2. 화면을 탭하여 마우스 커서를 해당 위치로 이동합니다(절대 제어).
3. 한 손가락으로 두 번 클릭하여 왼쪽 클릭, 두 손가락 클릭으로 오른쪽 클릭을 수행합니다.
4. 드래그 모드는 왼쪽 버튼을 누른 상태로 유지하는 것입니다.

#### 특별 기능

- 상대 마우스 제어(개발 중, 사용 가능 시 설정을 통해 전환).

## ![image](https://assets.openterface.com/images/android/mouseThouchMode.webp)

### 3. 키보드 입력

#### 주요 기능

- 키보드 키를 클릭하여 장치에 입력합니다.

#### 사용자 인터페이스 설명

- 키보드 아이콘은 오른쪽 하단에 있습니다.
- 키보드는 단축키, 시스템 키, 표준 키 및 기능 키(F1-F12)를 포함합니다.

#### 작동 흐름

1. 오른쪽 하단의 키보드 아이콘을 클릭하여 키보드를 불러옵니다.
2. 필요에 따라 텍스트를 입력하거나 기능 키를 누릅니다.

#### 특별 기능 또는 단축키

- **단축키**: Ctrl+C、Ctrl+V、Ctrl+Z、Ctrl+X、Ctrl+A、Ctrl+S、
  Win+Tab、Win+S、Win+E、Win+R、Win+D、Win+L、Alt+F4、Ctrl+Alt+Del、Alt+PrtScr.
- **기능 키**: F1-F12、기호 키.
- **표준 키**: 0-9、A-Z、Enter、Space、delete.

![image](https://assets.openterface.com/images/android/enlargeAndKeyBoard.webp)
![image](https://assets.openterface.com/images/android/keyBoardFunction.webp)
![image](https://assets.openterface.com/images/android/keyBoardSystem.webp)

---

그동안, 오픈 소스 **GitHub 저장소**: [Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android)를 탐색하여 최신 코드, 업데이트, 예제 및 문제를 보고하세요.

또한, [Discord 커뮤니티](/discord)에 가입하여 개발 팀 및 다른 멋진 사용자들과 KVM 관련 주제를 논의할 수 있습니다.

직접 지원이 필요하시면 [support@openterface.com](mailto:support@openterface.com)으로 이메일을 보내주세요.

---

**이 페이지에 대한 피드백이 있습니까?** [여기에서 알려주세요.](https://forms.gle/wmxoR2C1VdG36mT69)