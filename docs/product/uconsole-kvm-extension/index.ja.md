# uConsole用Openterface KVM拡張

![KVM Extension Connected to Target Device 2](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-2.webp){:style="height:300px"}

## 概要

このプラグアンドプレイ拡張ボードで、uConsoleを**ポータブルKVM（キーボード、ビデオ、マウス）コンソール**に変換します。

**Openterface KVM拡張**は、uConsoleの拡張スロットにある元の4G/LTEモデムを置き換え、直接的な**HDMI入力とUSB HID制御**を提供し、外部モニター、キーボード、またはネットワーク設定なしで、移動中にヘッドレスデバイスを管理できます。

![KVM Extension Board Front Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:300px"}
![KVM Extension Board Backm Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:300px"}


## 機能

- **完璧なフォームファクター**  
    シームレスなハードウェア統合のために、4G/LTEモジュールの37×77 mmサイズに一致します。

- **直接HDMI + USB HID**  
    uConsoleの内蔵入力と画面を使用して、接続されたデバイスの応答性の高い制御を可能にします。

- **低遅延**  
    BIOSレベルのトラブルシューティングとリアルタイムインタラクションに適しています。

- **真にポータブル**  
    uConsoleを開発者、エンジニア、技術者のためのモバイルツールにします。

- **オープンソースフレンドリー**  
    [Openterface KVM](https://github.com/techxArtisanStudio/openterface_qt)プラットフォーム上に構築されています。コミュニティの貢献を歓迎します。


## 使用例

- **システム管理**  
    かさばるKVMスイッチなしでサーバーや組み込みデバイスにアクセスし、トラブルシューティングを行います。

- **ハードウェア開発**  
    Raspberry Pi、SBC、またはマイクロコントローラーを直接テストおよびデバッグします。

- **フィールド展開**  
    データセンターやリモートロケーションでメンテナンスや設定を実行します。


## ハードウェアインストール

uConsoleの4G/LTEモジュールをOpenterface KVM拡張ボードに置き換え、安全な取り付けを確保するために、これらのハードウェアインストール手順に従ってください。

### 必要なもの

- Openterface KVM拡張ボード
- 提供されたガスケット（プラスチックシム） 
- 六角ドライバー（ボードの取り付けネジ用）
- ESD予防措置（リストストラップまたは接地表面）—推奨

### 拡張ボードのインストール

1. 電源オフと切断

    uConsoleをシャットダウンし、すべての電源とケーブルを切断します。

2. 既存モジュールの削除

    六角ドライバーを使用して、4G/LTEモジュールまたは既存の拡張ボードを保持している2つのネジを削除します。

    スプリングコンタクターを曲げないように、ボードをまっすぐ上に持ち上げてください。

3. KVM拡張ボードのインストール

    - Openterface KVM拡張ボードは1.0 mm厚（元の4G/LTE 1.2 mmより薄い）です。このため、提供されたガスケットをネジポスト（PCBとマウントスタンドオフの間）に配置し、ボードを配置する前にガスケットがネジポストの下に座るようにすることをお勧めします。これにより、より薄いPCBを補償し、適切なスプリングコンタクター圧力を確保するのに役立ちます。
    - 最初に確認したい場合は、ガスケットなしでボードを配置し、均等なスプリング接触を確認してください；接触が不均等またはボードが緩く座っている場合は、ガスケットを追加してボードを再配置してください。

<div style="display:flex;gap:1rem;align-items:flex-start;flex-wrap:wrap">
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-gasket-1.webp" alt="Installing KVM Extension gasket" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp" alt="Installing KVM Extension into uConsole" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
</div>

4. ネジの再挿入

    2つのネジを再挿入し、六角ドライバーで締めます。きつく締めるだけで十分です—過度に締めすぎないでください。

5. 取り付けの確認

    ボードは目立った動きなしに平らに座るべきです。スプリングコンタクターがパッド全体で均等に接触していることを確認してください。

6. ハードウェアのテスト

    電源を再接続し、システムを起動し、HDMI、オーディオ、USB HIDデバイスをテストして、適切な動作を確認してください。

## ソフトウェアセットアップガイド

KVM拡張を使用するには、uConsoleに**Openterfaceアプリ**をインストールしてください。

オプション1 - Flatpak版Openterfaceを使用
- 📖 詳細なセットアップ手順については、[Flatpakインストールガイド](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md)に従ってください。

![KVM Extension Connected to Target Device](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1c.webp){:style="height:300px"}

オプション2 - Rexからコミュニティ版をインストール

Rexが維持するコミュニティビルドが必要な場合は、彼のリポジトリを追加し、以下のコマンドでパッケージをインストールしてください。

1. リポジトリGPGキーとリポジトリを追加

```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. 更新とインストール

```bash
sudo apt update
sudo apt install openterfaceqt
```

注意：これらのコマンドにはsudoが必要です。リポジトリはarm64 Bookwormパッケージを対象としています；インストール前にデバイスとの互換性を確認してください。

## プレローンチステータス

- 📦 第1バッチは現在準備中  
- ⏳ 出荷開始予定：**2024年8月上旬**  
- 🛒 数量限定—[今すぐ予約](https://shop.techxartisan.com/products/openterface-kvm-ext-for-uconsole)してユニットを確保

> **予約通知**  
> この商品は現在予約受付中で、予想リードタイムは**約2ヶ月**です。  
> 他の商品をより早く必要とする場合は、**別注文**をしてください。組み合わせ注文は、この商品が準備できたときに出荷されます。

## コミュニティとサポート

- 🗨️ ディスカッションに参加：[Discordサーバー](https://discord.gg/ruAD9kcYbq)  
- 📧 メールサポート：[info@openterface.com](mailto:info@openterface.com)


## よくある質問

**Q: KVM拡張ボードはどのように動作しますか？**  
ターゲットデバイスからのHDMI出力をキャプチャし、uConsoleに表示します。同時に、uConsoleのキーボードとトラックボールがUSB HIDエミュレーションを介してターゲットデバイスを制御するために使用されます。

**Q: 4G/LTEモジュールがインストールされた状態でこれを使用できますか？**  
いいえ。このボードは同じ拡張スロットを占有します。セルラー接続またはKVM機能のいずれかを選択する必要があります。

**Q: ソフトウェアはオープンソースですか？**  
はい！**Openterface Connect**アプリは完全にオープンソースで、[GitHubリポジトリ](https://github.com/TechxArtisanStudio/Openterface_QT)で利用できます。
