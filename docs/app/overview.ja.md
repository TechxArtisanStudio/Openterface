# ソフトウェア

Openterface™ KVM ガジェットを起動して実行するには、ホストコンピューターに以下にリストされたアプリのいずれかをインストールする必要があります。これらのアプリは、さまざまなアプリプラットフォームから取得するか、提供されたリンクをクリックするだけです。冒険的になりたい場合は、GitHub リポジトリを使用してソースからビルドすることもできます！

![use-case-pc-angled-view](https://assets.openterface.com/images/product/use-case-pc-angled-view.webp){ width=600 }

## ダウンロードとインストール

<div class="grid cards" markdown>

-   ### :fontawesome-brands-windows:{ .lg } **Windows**

    ***

    **Openterface QT Win**をダウンロードまたはソースからビルド：

    [:octicons-download-24: {{qt_version}} インストーラーをダウンロード](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_windows_amd64_installer.exe) <br>
    [:octicons-download-24: {{qt_version}} ポータブル EXE をダウンロード](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_windows_amd64_portable.exe) <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) <br>
    [:octicons-play-24: デモを見る](https://youtu.be/ERzpGtRvP2o?si=e9k402f0nxsD8o2j)

-   ### :fontawesome-brands-apple:{ .lg } **macOS**

    ***

    **Openterface MacOS**をダウンロードまたはソースからビルド：

    [:octicons-arrow-right-24: App Store からインストール](/appstore) <br>
    [:octicons-download-24: ポータブル DMG をダウンロード](macos/dmg-installation.md) <br>
    [:octicons-mark-github-16: Openterface_MacOS](https://github.com/TechxArtisanStudio/Openterface_MacOS) <br>
    [:octicons-play-24: デモを見る](https://youtu.be/m7OpUem0zqY?si=tclfl0Jl77tmE6_e)

-   ### :fontawesome-brands-linux:{ .lg } **Linux**

    ***

    **Openterface QT Linux**をダウンロードまたはソースからビルド：

    [:octicons-download-24: {{qt_version}} AMD64 DEB をダウンロード](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_amd64.deb) <br>
    [:octicons-download-24: {{qt_version}} AMD64 RPM をダウンロード](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_amd64.rpm) <br>
    [:octicons-download-24: {{qt_version}} AMD64 AppImage をダウンロード](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_amd64.AppImage) <br>
    [:octicons-download-24: {{qt_version}} ARM64 DEB をダウンロード](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_aarch64.deb) <br>
    [:octicons-download-24: {{qt_version}} ARM64 AppImage をダウンロード](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_aarch64.AppImage) <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) <br>
    [:octicons-play-24: デモを見る](https://youtu.be/_ScpI6TC0Pk?si=FSg7A2zmST8QbFec)

-   ### :fontawesome-brands-android:{ .lg } **Android**

    ***

    **Android APK**をダウンロードまたはソースからビルド：

    [:octicons-download-24: {{android_version}}をダウンロード](https://github.com/TechxArtisanStudio/Openterface_Android/releases/download/{{android_version}}/OpenterfaceAndroid-release.apk) <br>
    [:octicons-mark-github-16: Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) <br>
    [:octicons-play-24: デモを見る](https://x.com/TechxArtisan/status/1825460088922071398)

</div>

???+ warning "注意：サードパーティアプリのプライバシーとセキュリティを確認してください"
すべてのアプリがオープンソースであるため、他の人が Openterface デバイス用に作成したホストアプリケーションの代替バージョンに遭遇する可能性があります。これらは非常にクールで、追加機能を提供する場合がありますが、ここで親切なリマインダーです：セキュリティとプライバシーの実践を注意深く確認してください—特に KVM 制御には画面、キーボード、マウスからのイベントが含まれるためです。Openterface チームはこれらのサードパーティアプリの安全性を保証することはできませんので、注意して進めてください！

## 基本ホストアプリコントロール

### 💻 互換性

-   **ホストソフトウェア**：macOS、Windows、または Linux 用のホストアプリをインストール。
-   **ターゲットデバイス**：セットアップ不要—ビデオ出力（HDMI、VGA など）とキーボード/マウス制御用の USB ポートを持つ任意のデバイスを接続。Windows、macOS、Linux、Android、iOS で動作。

### 🖱 マウスモード

-   **絶対モード**：ホストマウスがターゲット画面位置に直接マッピング。
-   **相対モード**：現在位置を基準にターゲットカーソルを移動。ショートカットで終了。

### ⌨️ キーボード

アプリにフォーカスがあるとき、ホストからのキーストロークがターゲットに直接送信されます。

### ⚙️ BIOS アクセス

ターゲット BIOS を直接制御。
一般的なキー：F2（Dell/Lenovo/ASUS）、F10（HP）、Del（ASUS/Gigabyte/MSI）、⌥（Apple）。

### 🔊 オーディオ

ターゲットオーディオが HDMI を通じてストリーミングされ、ホストコンピューターで再生されます。

### 🎥 ビデオ

アプリ内でターゲット画面を直接表示。

-   **現在のモデル**：アプリ内で最大**1080p 30Hz**表示、HDMI 経由で**4K 30Hz 入力**をサポート。
-   **その他の入力**：適切なアダプターを使用する場合、VGA、DVI、Micro HDMI などと互換性があります。
-   **将来のモデル**：新しいハードウェアバージョンがリリースされると、より高い解像度とフレームレートがサポートされます。

### 🔄 切り替え可能ポート

一部の Openterface デバイスには、**ホストとターゲット間で切り替え可能**なポートが含まれています。USB 2.0 ポートや micro-SD カードスロット（今後のモデル）などです。

-   **一度に一つずつ使用**：一度に片側（ホストまたはターゲット）のみがポートにアクセスできます。
-   **切り替え方法**：
    -   **ハードウェアトグル** — デバイス上の物理スイッチ
    -   **ソフトウェアボタン** — ホストアプリ経由で制御
-   **重要**：
    -   切り替え前にストレージデバイス（USB ドライブや micro-SD カード）を安全に取り出してください。
    -   不安定性や損傷を防ぐため、高電力デバイスの接続を避けてください。
    -   詳細とロジック図については、[切り替え可能ポートガイド](/usb-switch)をご覧ください。
