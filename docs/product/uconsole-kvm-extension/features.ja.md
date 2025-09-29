---
title: "機能と仕様"
description: "Openterface KVM Extension for uConsole の完全な概要：直接 HDMI 入力、USB HID 制御、完璧なフォームファクター、詳細な技術仕様を含む強力な機能。このポータブル KVM ソリューションについて知っておくべきすべて。"
keywords: "KVM拡張機能, uConsole KVM, HDMI KVM, USB HID制御, ポータブルKVM, headless制御, 4G LTE置換, 技術仕様, uConsole拡張"
---

# **機能と仕様** | Openterface KVM Extension for uConsole

![PCB-front](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="max-height:320px"}
![PCB-Back](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="max-height:320px"}

## コア機能

- **直接 HDMI + USB HID**：uConsole の内蔵画面とコントロールを活用し、直接 HDMI 入力と USB HID エミュレーションを提供。
- **プラグアンドプレイ**：ソフトウェアのインストールやターゲットデバイスへの痕跡を残すことなく、即座に制御。
- **低遅延**：BIOS レベルのトラブルシューティングとリアルタイムインタラクションに最適化。
- **ポータブル**：オールインワンのモバイルツール—追加のモニター、キーボード、ネットワーク設定は不要。
- **ネットワーク不要**：HDMI キャプチャと HID 入力による安定した headless 制御、ネットワークは不要。
- **テキスト転送**：キーストロークをシミュレートしてテキストを迅速に転送—ユーザー名、パスワード、コードスニペットに最適。記号や句読点を含む完全な ASCII をサポート。[詳細はアプリをご確認ください](/app)。
- **オープンソース**：[Openterface KVM QT](https://github.com/techxArtisanStudio/openterface_qt) をベースに構築され、活発なコミュニティサポートを提供。

## 技術仕様

### 物理寸法

- **サイズ：** 37 × 77 mm（4G/LTE モジュールと一致）
- **厚さ：** 1.0 mm（元の 4G/LTE モジュールの 1.2 mm より薄い）
- **材質：** スプリングコンタクタ付き高品質 PCB

### フルキーボード＆マウスエミュレーション

- **USB HID：** 絶対および相対マウス位置、フルキーボードサポート、マルチメディアキー。
- **接続：** 拡張ボードの Type-C メスポート経由でターゲットに USB リンク。

### ビデオ＆オーディオ

- **入力：** HDMI 経由で最大 4K (3840×2160) @ 30Hz
- **出力：** 140ms 未満の遅延でフル HD (1920×1080) @ 30Hz
- **ディスプレイ：** uConsole の内蔵画面を使用
- **圧縮：** YUV と MJPEG サポート
- **互換性：** VGA、DVI、Micro HDMI（アダプター経由）
- **オーディオ：** HDMI 埋め込みオーディオパススルー

### 切り替え可能 USB 2.0 ポート

- **共有ポート**：ホストアプリを使用して uConsole とターゲットデバイス（例：フラッシュドライブ）間で USB アクセスを簡単に切り替え。
- **USB 速度：** 12Mbps フルスピード伝送

### 接続性と電源

- **電源：** uConsole の拡張スロットから直接電力を供給（外部電源不要）
- **ターゲット互換性：** Windows、macOS、Linux、Android、iOS
- **ターゲットソフトウェア：** インストール不要
