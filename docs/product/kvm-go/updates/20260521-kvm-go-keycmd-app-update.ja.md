---
draft: false
date: 2026-05-21
title: "KVM-GO アップデート：KeyCmd 0.19 でスマホからターゲットマシンを操作"
description: "USB または Bluetooth 経由で KeyCmd 0.19 と KVM-GO を併用：KM Basic/Pro キーボード、Compose モード、ゲームパッドプリセット、Shortcut Hub、プレゼンテーション操作に対応。HID 入力にビデオドングルは不要です。"
keywords: "KVM-GO KeyCmd, KeyCmd 0.19, KVM-GO Android アプリ, KVM-over-USB スマホ操作, Openterface KeyCmd, 仮想キーボード KVM, KVM-GO Bluetooth USB, KM Pro Compose モード, KVM-GO HDMI DP VGA, Openterface KVM アプリ, ポータブル KVM 入力"
author: "Openterface Team | TechxArtisan"
category: "製品アップデート"
tags: ["KVM-GO", "KeyCmd", "製品アップデート", "Android", "USB", "Bluetooth", "キーボード", "ゲームパッド", "リリース"]
featured: false
social:
  image: "https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp"
  title: "KVM-GO + KeyCmd 0.19 — スマホからターゲットを操作"
  description: "KeyCmd 0.19 は USB または Bluetooth で KVM-GO とペアリングし、キーボード、マウス、ゲームパッド、ショートカット、Compose 機能を提供します。ビデオ表示が必要な場合は Openterface KVM アプリが担当します。"
---

# KVM-GO アップデート：KeyCmd 0.19 でスマホからターゲットマシンを操作

みなさん、こんにちは。

**KVM-GO** へのご支援、ならびに製品の製造と発送をお待ちいただき、誠にありがとうございます。多くの方がハードウェアの到着を心待ちにされていることと思いますが、お手元に届いた初日から完璧なセットアップを体験していただきたいと考えています。

**Openterface KVM** アプリ（スマホやタブレットでビデオ表示と完全な KVM 操作を実現）と並行して、キーボード、マウス、ゲームパッド、ショートカット入力用のコンパニオンアプリ **KeyCmd** の改良を続けてきました。現在、KVM-GO をお使いの方には **KeyCmd 0.19** を推奨しています。**USB** または **Bluetooth** でペアリング可能で、以前のビルドに上書きインストールしても、設定やプロファイル、ペアリング済みのデバイスはそのまま引き継がれます。

![ノートパソコン上の KVM-GO とスマホ上の KeyCmd キーボード](https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp){:style="max-width:720px;width:100%;height:auto"}

以下では、KeyCmd と KVM-GO を組み合わせることで何ができるのか、用途に合わせたモードの選び方、そして実際のターゲットマシンでの活用方法について説明します。

![KeyCmd ウェルカム画面](https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape_1.webp){:style="max-height:320px;width:auto"}

## 各モードと使用方法

### キーボード＆マウス（Basic）

**シンプルな全画面キーボード**だけが必要で、他の要素を排除したいときに使用します。

**用途：** BIOS パスワードの入力、短いシェルコマンド、テンキー入力、あるいは KVM-GO で画面を確認しながら広いタッチパッドでマウス操作を行いたい場合。

**使い方：**

- ナビゲーションドロワーから **KM Basic** を開きます。
- 必要に応じて、画面上のキーボード、**テンキー**（縦・横対応）、または**タッチパッド**タブを使用します。
- **設定**から、**固定キー**（タップで Shift/Ctrl をロック）または、ホールド＆タップのコンボを好む場合は**コードスタイル**の修飾キーを選択できます。

**メリット：** キー表示のための画面スペースが広く、UI がシンプル。ショートカットではなく入力だけが必要な場合に迅速に操作できます。

![KM Basic 全画面キーボード](https://assets2.openterface.com/images/keymod/KM-Basic-Keyboard_1.webp){:style="max-height:320px;width:auto"}

![横向きの KeyCmd テンキー](https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape_1.webp){:style="max-height:320px;width:auto"}

### キーボード＆マウス（Pro）

![横向きの KM Pro 分割キーボード](https://assets2.openterface.com/images/keymod/KM-Pro-Keyboard-landscape-split_1.webp){:style="max-height:320px;width:auto"}

![縦向きの KeyCmd キーボードとタッチパッド](https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait_1.webp){:style="max-height:320px;width:auto"}

KVM-GO の背後にあるマシンでの**日常的な管理作業**に使用します。分割キーボード、IME、Shortcut Hub バー、そして **Compose** エディタに対応しています。

**用途：** 長時間のタイピング、マクロやショートカットの利用、KVM ビューで結果を確認しながらホストへテキストブロックやスクリプトを送信する場合。

![スクリプト送信中の Compose モード](https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait_1.webp){:style="max-height:320px;width:auto"}

コマンドやスクリプトを頻繁に貼り付ける場合は、**Compose** をぜひお試しください。スマホ上で入力・確認し、キーストロークとしてホストに送信できます。[YouTube のデモ動画](https://www.youtube.com/watch?v=_rJF-hTF3_E)で一連の流れをご確認いただけます。

**使い方：**

- ナビゲーションドロワーから **KM Pro** を開きます。
- Basic と同様にキーボードとタッチパッドを使えるほか、上部の **Shortcut Hub** カテゴリから、プロファイルで設定したアクションをワンタップで実行できます。
- **Compose** を開いてスマホで長文を起草・確認し、HID キーストロークとして**送信**します。長いテキストの送信中はプログレスバーが表示されます。非 ASCII 文字が含まれる場合、送信前に警告が表示されるため、ホスト側の互換性を確認できます（特に macOS で便利です）。

**メリット：** タイピング、ポインティング、ショートカット、ペーストのようなワークフローが一つにまとまっており、ターゲットマシンの場所までフルキーボードを持ち運ぶ必要がありません。

### ゲームパッド

ゲームや、ゲームパッド入力を期待するターゲット上のアプリに最適化された**仮想コントローラー**レイアウトを使用したいときに開きます。

**用途：** エミュレータ、カジュアルゲーム、あるいは KVM-GO で画面を表示しながら、スティックとボタンを備えたコンパクトな操作パネルとして。

**使い方：**

- **Gamepad** モードに切り替えます。
- ツールバーの **Preset** をタップして、保存されたレイアウトを**切り替え**ます。**Preset を長押し**するとフルリストが開き、**インポート/エクスポート**や**モジュールの追加**（スティック、ボタン、タッチパッド）が可能です。
- 同梱の **emu-6** プリセットから始めて編集していくのがおすすめです。一つのレイアウトに**複数のタッチパッド**や追加のスティックモジュールを配置できます。

**メリット：** 標準のレイアウトに縛られません。ゲームごと、あるいはマシンごとにレイアウトを保存し、プリセットを他の方と共有することも可能です。

![ゲームパッドのプリセットレイアウト](https://assets2.openterface.com/images/keymod/Gamepad-perset-1_1.webp){:style="max-height:320px;width:auto"}

![Minecraft で使用中のゲームパッドプリセット](https://assets2.openterface.com/images/keymod/Gamepad-perset-minecraft_1.webp){:style="max-height:320px;width:auto"}

*Minecraft 用にカスタマイズされたプリセット。*

### Shortcut Hub

これは KM Pro 内の**プロファイルとショートカット**の管理画面です。カテゴリ、詳細パネル、そしてバーに割り当てるショートカットが含まれます。

**用途：** KVM-GO でビデオ接続を維持したまま、ターゲット上での繰り返し作業（ターミナルを開く、コマンドチェーンを貼り付ける、設定を切り替えるなど）を行う場合。

**使い方：**

- KM Pro から **Default** プロファイル（または自作のもの）で作業します。
- カテゴリタブと詳細 UI を使用してショートカットを管理します。
- プロファイルの構成に慣れていない場合は、**Shortcut Hub ガイドツアー**を実行してください。

### プレゼンテーション

スマホを回転させたときにボタンが飛ばないよう、**縦向き**に固定されたシンプルな**プレゼンター風**操作パネルです。

**用途：** ターゲットマシンでのスライド送りや、軽いプレゼンテーション操作。

![Google スライドを操作中のプレゼンテーションモード](https://assets2.openterface.com/images/keymod/KeyCmd-Presentation-Google-Slides.webp){:style="max-height:320px;width:auto"}

---

## 対応言語

アプリの UI は **11 言語**に対応しています。最近、韓国語、イタリア語、ロシア語、ブラジルポルトガル語が追加されました。

**Settings** → **App language** から切り替え可能です。

---

## KeyCmd 0.19 の入手と KVM-GO への接続

**ダウンロード：** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

既存のアプリがある場合は、そのまま上書きインストールしてください。データを消去する必要はありません。

**KVM-GO への接続（ビデオポートは未接続でも可）：**

**KVM-GO の 3 つのバリアント**（HDMI、VGA、DP）すべてにおいて、KeyCmd の入力だけであれば、**ドングルのビデオコネクタ**を何かに接続する必要はありません。HDMI、VGA、DP ポートは空のままでも大丈夫です。以下のいずれかの方法を選択してください。

**オプション A — Bluetooth（ターゲットから KVM-GO に給電）**

1. **短い黒の USB ケーブル**を KVM-GO の **Target** ポートと操作対象のマシンに接続します。この接続だけで KVM-GO に**給電**されます。
2. スマホで **KeyCmd** を開き、**Bluetooth** 経由で KVM-GO を探します。

**オプション B — Android スマホへの USB 接続（Host ポート）**

1. KVM-GO の **Host** ポートから**長いオレンジのケーブル**を Android スマホに接続します。
2. アプリ内で **KeyCmd** を開き、**USB** 経由で接続します。

![短い黒の USB ケーブルでノートパソコンに接続された KVM-GO Target ポート](https://assets2.openterface.com/images/kvm-go/kvm-go-target-port-laptop-power.webp){:style="max-height:360px;width:auto"}

全画面ビデオと入力を併用する場合は、ターゲットの表示に **Openterface KVM** を使い、キーボード、マウス、ショートカットに **KeyCmd** を使用してください。ターゲットにすでに独自のディスプレイがあり、入力だけが必要な場合は KeyCmd だけで十分です。

両方のデバイスをお持ちであれば、USB 経由で **Mini-KVM** でも動作します。

> **ベータ版です。** ゲームパッドのプリセットや Compose の送信機能は、ホスト OS によって挙動が異なる場合があります。KVM-GO で何か不具合が発生した場合は、スクリーンショット、お使いの KVM-GO バリアント（HDMI / DP / VGA）、および期待していた挙動を添えて **Discord** までご連絡ください。

> **ソースコード：** まだ公開されていません。関連プロジェクトのクラウドファンディングの節目を終えた後にオープンソース化する予定です。APK の場所がわからない場合は Discord でお尋ねください。

---

## KeyMod について（オプション、KVM-GO とは別製品）

私たちは、同じ KeyCmd アプリで動作する専用の USB/Bluetooth HID ドングル **[KeyMod](https://openterface.com/product/keymod/)** も開発しています。KVM-GO のバッカーの方は、上記のワークフローのために KeyMod を購入する必要はありません。現在私たちが推奨する使い方は、KVM-GO での KeyCmd 利用です。

KVM 以外のセットアップでスタンドアロンドングルに興味がある方は、[Crowd Supply の KeyMod キャンペーン](https://www.crowdsupply.com/techxartisan/openterface-keymod)をフォローしてください。こちらは KVM-GO の配送とは別プロジェクトとなります。

---

## フィードバックをお待ちしております

お時間があれば、**KeyCmd 0.19** をインストールして KVM-GO（または Mini-KVM）に接続し、使いにくい点などを教えてください。データセンターのトラブル対応やホームラボでの使用報告は、次回のリリースに直接反映されます。

KVM-GO プロジェクトを支援する具体的な方法：

- Discord やコミュニティで、**うまく機能している点**（BIOS のコツ、Bluetooth ペアリング、お気に入りのモードなど）を共有する
- サーバー等のヘッドレス機器を管理していて、ポケットサイズの KVM を必要としている**同僚に紹介する**
- **率直なフィードバック**、特に使いにくい部分を送り続ける。それは称賛よりも製品をより良く形作ります。

KVM-GO へのご支援、そしてポータブルな KVM-over-USB をすべての人にとってより良いものにするためのご協力に、改めて感謝いたします。

今後ともよろしくお願いいたします。

**Openterface Team | TechxArtisan**
