---
title: "機能と仕様"
description: "Openterface Mini-KVM の完全な概要：BIOS レベルアクセス、4K ビデオサポート、クロスプラットフォーム互換性、USB 共有、詳細な技術仕様など強力な機能。このヘッドレスコンピュータ制御ソリューションについて知っておくべきすべて。"
keywords: "Mini-KVM 機能, KVM 仕様, BIOS アクセス, ヘッドレス制御, 4K KVM, USB 共有, クロスプラットフォーム KVM, テキスト転送, プラグアンドプレイ KVM, オープンソース KVM, 技術仕様"
---

# **機能と仕様** | Openterface Mini-KVM

<iframe 
  width="560" 
  height="315" 
  src="https://www.youtube.com/embed/r3HNUflWGOY?si=84Ek6F9ocHmmGTqW" 
  title="YouTube video player" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
  referrerpolicy="strict-origin-when-cross-origin" 
  allowfullscreen>
</iframe>

## コア機能

### **BIOS レベルアクセス**

ネットワーク依存なしで、ターゲットデバイスの BIOS、ファームウェア、起動管理に直接アクセス。

### **ネットワーク独立性**

HDMI ビデオキャプチャとエミュレートされたキーボード/マウス（HID）入力を使用した安定したヘッドレス制御。ネットワーク接続は不要。

### **高性能ビデオ**

- **入力**：HDMI 経由で最大 4K (3840×2160) @ 30Hz
- **出力**：フル HD (1920×1080) @ 30Hz、140ms 未満の遅延
- **圧縮**：YUV と MJPEG サポート
- **互換性**：アダプター経由で VGA、DVI、Micro HDMI に対応

### **切り替え可能 USB ポート**

ホストとターゲットデバイス間で USB アクセスを切り替え、シームレスな USB ドライブ共有を実現。[切り替え可能 USB ポート](../usb-switch)ページで詳細をご覧ください。

### **クロスプラットフォームサポート**

[ホストアプリ](/app)は macOS、Windows、Linux、Android に対応し、ユニバーサル統合を実現。

### **テキスト転送**

キーストロークをシミュレートしてテキストを簡単に転送—ユーザー名、パスワード、コードスニペットに最適。記号や句読点を含む ASCII 文字をサポート。

!!! warning "テキスト転送の制限" - **クリップボード統合なし**：タイピングのみエミュレート、画像やドキュメント転送は不可 - **ASCII のみ**：ASCII 文字に限定（中国語、日本語、韓国語はサポートなし） - **長さの考慮**：短いテキストに最適；大きなブロックはパフォーマンスの問題を引き起こす可能性

### **プラグアンドプレイの利便性**

ターゲットデバイスにソフトウェアインストールは不要。接続と同時に制御開始、ソフトウェアの痕跡は残りません。

### **オーディオ統合**

完全なマルチメディア体験のための HDMI 埋め込みオーディオパススルー。

### **拡張ピン**

[拡張ピン](../extension-pins)により、特定のニーズに応じた高度な開発とカスタマイズが可能。

### **オープンソース**

透明性と[コミュニティイノベーション](/discord)のための[完全オープンソース](/compliance)ハードウェアとソフトウェア。

## 技術仕様

### **物理寸法**

- **サイズ**：61 × 53 × 13.5 mm (2.40 × 2.09 × 0.53 インチ)
- **重量**：~48g
- **材質**：アルミニウム合金、PLA ケーシング

### **接続と電源**

- **電源**：USB-C 給電（外部電源不要）
- **USB 速度**：12Mbps フルスピード伝送
- **ホスト互換性**：Windows、macOS、Linux、Android
- **ターゲット**：ソフトウェアインストール不要

### **ビデオとオーディオ**

- **最大入力**：3840×2160@30Hz (HDMI)
- **最大出力**：1920×1080@30Hz
- **遅延**：140ms 未満
- **オーディオ**：HDMI 埋め込みオーディオパススルー

### **入力機能**

- 完全なキーボードとマウスエミュレーション（絶対と相対）
- マルチメディアキーサポート
- カスタム HID 機能
- コンピュータウェイクアップ機能

### **環境条件**

- **動作温度**：0°C から 40°C
- **保管温度**：-10°C から 50°C
- **湿度**：80% RH

## 製品モデル

- **ベーシック**：OP-MINIKVM-BASIC
- **ツールキット**：OP-MINIKVM-TOOLKIT

## ドキュメントダウンロード

- **[クイックスタートガイド](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/minikvm_quick_start_guide_20240928.pdf)** (PDF)
- **[データシート（英語）](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/Openterface-Mini-KVM-Basic-and-Toolkit-Datasheet-Eng-20250313.pdf)** (PDF)

![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front.svg#only-light){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back.svg#only-light){:style="max-height:260px"}
![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front_1.svg#only-dark){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back_1.svg#only-dark){:style="max-height:260px"}
