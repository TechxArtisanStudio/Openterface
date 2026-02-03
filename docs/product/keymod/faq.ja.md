---
title: Openterface KeyMod シリーズ よくある質問
description: KeyMod シリーズに関するよくある質問。機能、互換性、プラットフォーム、プレローンチ情報をカバーしています。
keywords: KeyMod, Openterface, HIDエミュレーター, Bluetoothキーボード, スマホキーボード, オープンソース, プレローンチ, Android, iPadOS
---

# Openterface KeyMod よくある質問

**Openterface KeyMod**のよくある質問へようこそ。  
必要な情報が見つからない場合は、**[info@openterface.com](mailto:info@openterface.com) までメールでお問い合わせ**いただくか、[Discord](/discord) または [Reddit](/reddit) で**コミュニティに参加**してください。

⚠️ **注意**：KeyModは現在プレローンチ開発中です。製品の最終化に伴い、機能、仕様、デザインは変更される可能性があります。

---

## :material-clipboard-list: クイックナビゲーション

- [Openterface KeyMod よくある質問](#openterface-keymod-よくある質問)
  - [:material-clipboard-list: クイックナビゲーション](#material-clipboard-list-クイックナビゲーション)
  - [一般](#一般)
  - [接続](#接続)
  - [機能](#機能)
  - [プレローンチ](#プレローンチ)

---

## 一般

**:material-chat-question:{ .faq } KeyModとは何ですか？**

KeyModは、スマートフォンをポータブルキーボードとトラックパッドに変えるコンパクトなUSB + Bluetooth HID（キーボードとマウス）エミュレーターです。キーボード/マウス入力が必要なデバイス—キオスク、スマートTV、セットトップボックス、屋外ディスプレイ—を、フルキーボードを持ち歩かずにコントロールできます。

**:material-chat-question:{ .faq } KeyModアプリはどのプラットフォームをサポートしていますか？**

KeyModコントローラーアプリは**Android**と**iPadOS**に焦点を当てています。Openterfaceエコシステム全体では、**WindowsとmacOS**のソフトウェアによるデスクトップコントロールの拡張も進めています。

**:material-chat-question:{ .faq } ターゲットデバイスにソフトウェアは必要ですか？**

いいえ。KeyModは標準のUSBキーボードとマウスをエミュレートします。ターゲットデバイスはプラグアンドプレイのHIDハードウェアとして認識します—ドライバーやソフトウェアのインストールは不要です。

**:material-chat-question:{ .faq } KeyModはオープンソースですか？**

はい。KeyModはオープンハードウェアおよびオープンソースソフトウェアです。プロジェクトの進展に伴い、回路図、PCBファイル、ファームウェア、ソフトウェア、BOMを公開します。

---

## 接続

**:material-chat-question:{ .faq } USBとBluetooth—どちらを使うべきですか？**

- **USB**：より信頼性が高く、レイテンシが低い。最も安定した接続が必要な場合に使用。
- **Bluetooth**：ケーブル不要。より軽いセットアップが必要で、シナリオがワイヤレスを許容する場合に使用。

**:material-chat-question:{ .faq } どのようなハードウェアバリアントが計画されていますか？**

1. **2-in-1コネクター** — 幅広い互換性のためのUSB A + USB C複合プラグ
2. **USB Cバージョン** — モダンデバイス向けの専用USB Cプラグ

---

## 機能

**:material-chat-question:{ .faq } どのゲームパッドレイアウトがサポートされていますか？**

KeyModは**Xboxレイアウト**、**PlayStationレイアウト**、**NESレイアウト**で仮想ゲームコントローラーとして機能できます。

**:material-chat-question:{ .faq } カスタムプロファイルとマクロを作成できますか？**

はい。オープンソースのモバイルアプリは、カスタム入力プロファイル、マクロ、ホットキー、ワークフローショートカットをサポートしています。テンキーやゲームパッドモードも使用できます。

**:material-chat-question:{ .faq } プログラム可能なハードウェアボタンとは何ですか？**

KeyModには、クイックトリガーやシンプルなマクロスタイルのワークフローなどのオンデバイスアクション用のプログラム可能なハードウェアボタンが含まれています。この機能はまだ実験的で、コミュニティのフィードバックを通じて改良されます。

---

## プレローンチ

**:material-chat-question:{ .faq } KeyModはいつリリースされますか？**

KeyModはプレローンチ開発中です。[製品ページ](/product/keymod/)でローンチ通知とアップデートを受け取れます。

**:material-chat-question:{ .faq } KeyModはMini-KVMやKVM-Goとどのように関係していますか？**

KeyModはOpenterface Mini-KVMの実績あるHIDコアを使用しています。同じハードウェアベースのキーボードとマウスエミュレーションアプローチを共有していますが、異なるユースケース向けに設計されています：スマートフォンをポータブルキーボード/トラックパッドに変えてローカルデバイス制御を行うもので、KVM-over-USBビデオキャプチャではありません。
