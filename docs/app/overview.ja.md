# ソフトウェア

Openterface™ KVMガジェットを起動して実行するには、ホストコンピューターに以下にリストされたアプリのいずれかをインストールする必要があります。これらのアプリは、さまざまなアプリプラットフォームから取得するか、提供されたリンクをクリックするだけです。冒険的になりたい場合は、GitHubリポジトリを使用してソースからビルドすることもできます！

![use-case-pc-angled-view](https://assets.openterface.com/images/product/use-case-pc-angled-view.webp){ width=600 }

## ダウンロードとインストール

<div class="grid cards" markdown>

-   ### :fontawesome-brands-windows:{ .lg } __Windows__

    ---

    **Openterface QT Win**をダウンロードまたはソースからビルド：

    [:octicons-download-24: {{qt_version}} インストーラーをダウンロード](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.windows.amd64.installer.exe)  <br>
    [:octicons-download-24: {{qt_version}} ポータブルEXEをダウンロード](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT-portable.exe)  <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT)  <br>
    [:octicons-play-24: デモを見る](https://youtu.be/ERzpGtRvP2o?si=e9k402f0nxsD8o2j)

-   ### :fontawesome-brands-apple:{ .lg } __macOS__

    ---

    **Openterface MacOS**をダウンロードまたはソースからビルド：

    [:octicons-arrow-right-24: App Storeからインストール](/appstore) <br>
    [:octicons-download-24: ポータブルDMGをダウンロード](macos/dmg-installation.md) <br>
    [:octicons-mark-github-16: Openterface_MacOS](https://github.com/TechxArtisanStudio/Openterface_MacOS) <br>
    [:octicons-play-24: デモを見る](https://youtu.be/m7OpUem0zqY?si=tclfl0Jl77tmE6_e)

-   ### :fontawesome-brands-linux:{ .lg } __Linux__

    ---

    **Openterface QT Linux**をダウンロードまたはソースからビルド：

    [:octicons-download-24: {{qt_version}} AMD64 DEBをダウンロード](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.linux.amd64.deb)  <br>
    [:octicons-download-24: {{qt_version}} AMD64 RPMをダウンロード](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.linux.amd64.rpm)  <br>
    [:octicons-download-24: {{qt_version}} AMD64 AppImageをダウンロード](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.linux.amd64.AppImage)  <br>
    [:octicons-download-24: {{qt_version}} ARM64 DEBをダウンロード](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.linux.arm64.deb)  <br>
    [:octicons-download-24: {{qt_version}} ARM64 RPMをダウンロード](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.linux.arm64.rpm)  <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT)  <br>
    [:octicons-play-24: デモを見る](https://youtu.be/_ScpI6TC0Pk?si=FSg7A2zmST8QbFec)

-   ### :fontawesome-brands-android:{ .lg } __Android__

    ---

    **Android APK**をダウンロードまたはソースからビルド：

    [:octicons-download-24: {{android_version}}をダウンロード](https://github.com/TechxArtisanStudio/Openterface_Android/releases/download/{{android_version}}/OpenterfaceAndroid-release.apk)  <br>
    [:octicons-mark-github-16: Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android)  <br>
    [:octicons-play-24: デモを見る](https://x.com/TechxArtisan/status/1825460088922071398)

</div>

???+ warning "注意：サードパーティアプリのプライバシーとセキュリティを確認してください"
    すべてのアプリがオープンソースであるため、他の人がOpenterfaceデバイス用に作成したホストアプリケーションの代替バージョンに遭遇する可能性があります。これらは非常にクールで、追加機能を提供する場合がありますが、ここで親切なリマインダーです：セキュリティとプライバシーの実践を注意深く確認してください—特にKVM制御には画面、キーボード、マウスからのイベントが含まれるためです。Openterfaceチームはこれらのサードパーティアプリの安全性を保証することはできませんので、注意して進めてください！

## 基本ホストアプリコントロール

### 💻 互換性

- **ホストソフトウェア**：macOS、Windows、またはLinux用のホストアプリをインストール。
- **ターゲットデバイス**：セットアップ不要—ビデオ出力（HDMI、VGAなど）とキーボード/マウス制御用のUSBポートを持つ任意のデバイスを接続。Windows、macOS、Linux、Android、iOSで動作。

### 🖱 マウスモード

- **絶対モード**：ホストマウスがターゲット画面位置に直接マッピング。
- **相対モード**：現在位置を基準にターゲットカーソルを移動。ショートカットで終了。

### ⌨️ キーボード
アプリにフォーカスがあるとき、ホストからのキーストロークがターゲットに直接送信されます。

### ⚙️ BIOSアクセス
ターゲットBIOSを直接制御。
一般的なキー：F2（Dell/Lenovo/ASUS）、F10（HP）、Del（ASUS/Gigabyte/MSI）、⌥（Apple）。

### 🔊 オーディオ
ターゲットオーディオがHDMIを通じてストリーミングされ、ホストコンピューターで再生されます。

### 🎥 ビデオ
アプリ内でターゲット画面を直接表示。

- **現在のモデル**：アプリ内で最大**1080p 30Hz**表示、HDMI経由で**4K 30Hz入力**をサポート。
- **その他の入力**：適切なアダプターを使用する場合、VGA、DVI、Micro HDMIなどと互換性があります。
- **将来のモデル**：新しいハードウェアバージョンがリリースされると、より高い解像度とフレームレートがサポートされます。

### 🔄 切り替え可能ポート
一部のOpenterfaceデバイスには、**ホストとターゲット間で切り替え可能**なポートが含まれています。USB 2.0ポートやmicro-SDカードスロット（今後のモデル）などです。

- **一度に一つずつ使用**：一度に片側（ホストまたはターゲット）のみがポートにアクセスできます。
- **切り替え方法**：
    - **ハードウェアトグル** — デバイス上の物理スイッチ
    - **ソフトウェアボタン** — ホストアプリ経由で制御
- **重要**：
    - 切り替え前にストレージデバイス（USBドライブやmicro-SDカード）を安全に取り出してください。
    - 不安定性や損傷を防ぐため、高電力デバイスの接続を避けてください。
    - 詳細とロジック図については、[切り替え可能ポートガイド](/usb-switch)をご覧ください。
