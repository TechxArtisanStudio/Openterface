# uConsole용 Openterface KVM 확장

![KVM Extension Connected to Target Device 2](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-2.webp){:style="height:300px"}

## 개요

이 플러그 앤 플레이 확장 보드로 uConsole을 **휴대용 KVM(키보드, 비디오, 마우스) 콘솔**로 변환하세요.

**Openterface KVM 확장**은 uConsole의 확장 슬롯에 있는 원래 4G/LTE 모뎀을 교체하고 직접적인 **HDMI 입력 및 USB HID 제어**를 제공하여 외부 모니터, 키보드 또는 네트워크 구성 없이 이동 중에 헤드리스 장치를 관리할 수 있습니다.

![KVM Extension Board Front Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:300px"}
![KVM Extension Board Backm Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:300px"}


## 기능

- **완벽한 폼 팩터**  
    원활한 하드웨어 통합을 위해 4G/LTE 모듈의 37×77 mm 크기와 일치합니다.

- **직접 HDMI + USB HID**  
    uConsole의 내장 입력과 화면을 사용하여 연결된 장치의 반응성 제어를 가능하게 합니다.

- **낮은 지연 시간**  
    BIOS 수준 문제 해결 및 실시간 상호 작용에 적합합니다.

- **진정한 휴대성**  
    uConsole을 개발자, 엔지니어 및 기술자를 위한 모바일 도구로 만듭니다.

- **오픈 소스 친화적**  
    [Openterface KVM](https://github.com/techxArtisanStudio/openterface_qt) 플랫폼을 기반으로 구축되었습니다. 커뮤니티 기여를 환영합니다.


## 사용 사례

- **시스템 관리**  
    부피가 큰 KVM 스위치 없이 서버 또는 임베디드 장치에 액세스하고 문제를 해결합니다.

- **하드웨어 개발**  
    Raspberry Pi, SBC 또는 마이크로컨트롤러를 직접 테스트하고 디버그합니다.

- **현장 배포**  
    데이터 센터 또는 원격 위치에서 유지보수 또는 구성을 수행합니다.


## 하드웨어 설치

uConsole의 4G/LTE 모듈을 Openterface KVM 확장 보드로 교체하고 안전한 장착을 보장하기 위해 다음 하드웨어 설치 단계를 따르세요.

### 필요한 것

- Openterface KVM 확장 보드
- 제공된 개스킷(플라스틱 심) 
- 육각 드라이버(보드 장착 나사용)
- ESD 예방 조치(손목 스트랩 또는 접지된 표면) — 권장

### 확장 보드 설치

1. 전원 끄기 및 연결 해제

    uConsole을 종료하고 모든 전원과 케이블을 분리합니다.

2. 기존 모듈 제거

    육각 드라이버를 사용하여 4G/LTE 모듈 또는 기존 확장 보드를 고정하는 두 개의 나사를 제거합니다.

    스프링 접촉자를 구부리지 않도록 보드를 곧게 들어 올리세요.

3. KVM 확장 보드 설치

    - Openterface KVM 확장 보드는 1.0 mm 두께입니다(원래 4G/LTE 1.2 mm보다 얇음). 이 때문에 제공된 개스킷을 나사 포스트(PCB와 장착 스탠드오프 사이)에 배치하여 보드를 장착하기 전에 개스킷이 나사 포스트 아래에 위치하도록 하는 것을 권장합니다. 이는 더 얇은 PCB를 보상하고 적절한 스프링 접촉자 압력을 보장하는 데 도움이 됩니다.
    - 먼저 확인하려면 개스킷 없이 보드를 장착하고 균등한 스프링 접촉을 확인하세요; 접촉이 불균등하거나 보드가 느슨하게 장착되면 개스킷을 추가하고 보드를 다시 장착하세요.

<div style="display:flex;gap:1rem;align-items:flex-start;flex-wrap:wrap">
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-gasket-1.webp" alt="Installing KVM Extension gasket" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp" alt="Installing KVM Extension into uConsole" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
</div>

4. 나사 재삽입

    두 개의 나사를 재삽입하고 육각 드라이버로 조입니다. 꽉 조이는 것으로 충분합니다 — 과도하게 조이지 마세요.

5. 장착 확인

    보드는 눈에 띄는 움직임 없이 평평하게 장착되어야 합니다. 스프링 접촉자가 패드 전체에 균등하게 접촉하고 있는지 확인하세요.

6. 하드웨어 테스트

    전원을 다시 연결하고 시스템을 부팅한 다음 HDMI, 오디오 및 USB HID 장치를 테스트하여 올바른 작동을 확인하세요.

## 소프트웨어 설정 가이드

KVM 확장을 사용하려면 uConsole에 **Openterface 앱**을 설치하세요.

옵션 1 - Flatpak 버전 Openterface 사용
- 📖 자세한 설정 단계는 [Flatpak 설치 가이드](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md)를 따르세요.

![KVM Extension Connected to Target Device](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1c.webp){:style="height:300px"}

옵션 2 - Rex에서 커뮤니티 버전 설치

Rex가 유지 관리하는 커뮤니티 빌드를 원한다면 그의 저장소를 추가하고 아래 명령으로 패키지를 설치하세요.

1. 저장소 GPG 키 및 저장소 추가

```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. 업데이트 및 설치

```bash
sudo apt update
sudo apt install openterfaceqt
```

참고: 이 명령은 sudo가 필요합니다. 저장소는 arm64 Bookworm 패키지를 대상으로 합니다; 설치 전에 장치와의 호환성을 확인하세요.

## 사전 출시 상태

- 📦 첫 번째 배치가 현재 준비 중  
- ⏳ 예상 배송 시작: **2024년 8월 초**  
- 🛒 제한된 수량 – [지금 사전 주문](https://shop.techxartisan.com/products/openterface-kvm-ext-for-uconsole)하여 유닛을 예약하세요

> **사전 주문 안내**  
> 이 항목은 현재 사전 주문 중이며 예상 리드 타임은 **약 2개월**입니다.  
> 다른 항목을 더 빨리 필요로 한다면 **별도 주문**을 해주세요. 결합 주문은 이 제품이 준비될 때 배송됩니다.

## 커뮤니티 및 지원

- 🗨️ 토론 참여: [Discord 서버](https://discord.gg/ruAD9kcYbq)  
- 📧 이메일 지원: [info@openterface.com](mailto:info@openterface.com)


## 자주 묻는 질문

**Q: KVM 확장 보드는 어떻게 작동하나요?**  
대상 장치의 HDMI 출력을 캡처하여 uConsole에 표시합니다. 동시에 uConsole의 키보드와 트랙볼이 USB HID 에뮬레이션을 통해 대상 장치를 제어하는 데 사용됩니다.

**Q: 4G/LTE 모듈이 설치된 상태에서 이것을 사용할 수 있나요?**  
아니요. 이 보드는 동일한 확장 슬롯을 차지합니다. 셀룰러 연결 또는 KVM 기능 중에서 선택해야 합니다.

**Q: 소프트웨어가 오픈 소스인가요?**  
네! **Openterface Connect** 앱은 완전히 오픈 소스이며 [GitHub 저장소](https://github.com/TechxArtisanStudio/Openterface_QT)에서 사용할 수 있습니다.
