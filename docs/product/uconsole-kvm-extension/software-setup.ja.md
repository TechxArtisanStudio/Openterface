---
title: "ソフトウェアセットアップ"
description: "Openterface KVM Extension for uConsole の完全なソフトウェアセットアップガイド。シームレスな KVM 機能のために uConsole に Openterface App をインストールして設定する方法を学びます。"
keywords: "Openterfaceアプリインストール, uConsoleソフトウェアセットアップ, KVMアプリセットアップ, uConsoleアプリ設定, ソフトウェアインストールガイド"
---

# **ソフトウェアセットアップ** | Openterface KVM Extension for uConsole

## インストール概要

Openterface App により、uConsole が KVM インターフェースとして機能し、内蔵画面、キーボード、トラックボールを使用してターゲットデバイスを制御できます。

!!! note "要件"
    - **uConsole**：Openterface App のインストールが必要
    - **ターゲット**：アプリ不要 - Windows、macOS、Linux、Android、iOS をサポート
    - **ビデオ**：標準 HDMI ケーブルを使用してください。標準 HDMI ケーブルを使用してください。電源付き HDMI コンバーターを使用すると、**VGA**、**DP** などの他のフォーマットもサポートします。*ヒント：コンバーターが適切に電源供給されていることを確認してください。そうしないと、黒い画面が表示される可能性があります。*

## インストール方法

### **オプション 1：Flatpak インストール**

詳細なセットアップ手順については、[Flatpak インストールガイド](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) に従ってください。

### **オプション 2：コミュニティリポジトリ（推奨）**

Rex が管理するコミュニティビルドを希望する場合：

1. **リポジトリの追加**：
```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. **パッケージのインストール**：
```bash
sudo apt update
sudo apt install openterfaceqt
```

!!! warning "リポジトリの注意事項"
    これらのコマンドには sudo が必要です。リポジトリは arm64 Bookworm パッケージを対象としています。インストール前にデバイスとの互換性を確認してください。

## 使用方法

### **KVM セッションの開始**
1. uConsole で Openterface App を起動
2. アプリは自動的に KVM Extension ボードを検出
3. HDMI でターゲットデバイスを接続
4. uConsole の内蔵キーボードとトラックボールを使用してターゲットデバイスを制御

### **制御機能**
- **キーボード**：マルチメディアキーを含む完全なキーボードエミュレーション
- **マウス**：絶対および相対マウス位置
- **オーディオ**：HDMI オーディオを uConsole スピーカーにパススルー

### **高度な機能**
- **テキスト転送**：キーストロークをシミュレートしてテキストを迅速に転送—ユーザー名、パスワード、コードスニペットに最適
- **切り替え可能 USB**：ホストアプリを使用して uConsole とターゲットデバイス間で USB アクセスを簡単に切り替え
