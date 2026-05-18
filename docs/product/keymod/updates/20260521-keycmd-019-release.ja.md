---
draft: false
date: 2026-05-21
title: "KeyCmd 0.19：アプリブランディング変更、KM Pro Compose モード、多言語サポート、モード別ガイドツアー"
description: "KeyCmd 0.19 は KeyMod から KeyCmd への大幅なアプリブランディング変更、Unicode 対応 HID 送信機能を備えた新しい KM Pro Compose モード、多言語 UI（韓国語、イタリア語、ロシア語、ブラジルポルトガル語）、モード別インタラクティブガイドツアー、および数十件の UX 改善を提供します。"
keywords: "KeyCmd 0.19, KeyCmd リリース, アプリブランディング変更, Compose モード, Unicode HID 送信, 多言語, インタラクティブガイドツアー, Openterface KeyCmd アップデート, HID エミュレータ, 仮想キーボード, Android キーボードアプリ"
author: "TechxArtisan Studio"
category: "Product Updates"
tags: ["KeyCmd", "Product Updates", "Release", "Compose", "i18n", "Android"]
featured: false
social:
  image: "https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp"
  title: "KeyCmd 0.19 リリース — Compose モード、ブランディング変更、多言語、ガイドツアー"
  description: "KeyCmd 0.19 は新しい Compose モード、KeyCmd へのアプリブランディング変更、4 つの新言語、インタラクティブガイドツアー、そして大幅な UX 改善をもたらします。"
---

# KeyCmd 0.19：アプリブランディング変更、KM Pro Compose モード、多言語サポート、モード別ガイドツアー

KeyCmd **0.19**（`versionCode` **19**）は、KeyMod から KeyCmd への**アプリブランディング変更**、Unicode 対応 HID 送信機能を備えた全新的な **KM Pro Compose モード**、拡張された**多言語 UI**（韓国語、イタリア語、ロシア語、ブラジルポルトガル語を含む）、**モード別インタラクティブガイドツアー**、そしてキーボード、ゲームパッド、プレゼンテーションモードにおける数十件の UX 改善を提供する大型アップデートです。

## アプリブランディング変更：KeyMod → KeyCmd

アプリの表示名はすべてのエントリポイントで **KeyCmd** に統一されました。このブランディング変更により、**KeyMod ハードウェア**とその companion アプリである **KeyCmd アプリ**の区別が明確になりました。

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp" alt="KeyCmd ウェルカム画面" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">

### 変更内容

- **アプリ表示名**：ランチャーアイコンとシステム UI に「KeyCmd」が表示されるようになりました
- **ウェルカムフロー**：KeyMod から KeyCmd へのワードマークとコピーを更新
- **CI アーティファクトと APK ファイル名**：**KeyCmd** プレフィックスを使用
- `applicationId` は **`com.openterface.keymod`** のままなので、シームレスなその場アップグレードが可能

既存ユーザー：設定、プロファイル、ペアリング済みデバイスはすべて保持されます。アップグレードはシームレスです。

## キーボード＆マウス：フルスクリーン体験

KeyCmd はフルスクリーンのキーボード、タッチパッド、ナンバーパッド体験を提供します — ポートレートとランドスケープの両方の向きに最適化されています。

<div class="slideshow-container" id="slideshow-keycmd-019-kbm-ja" data-auto-slide="true" data-auto-slide-interval="3000">
  <div class="slideshow-wrapper">
    <div class="slide active">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Full-Keyboard-landscape.webp" alt="ランドスケープフルキーボード" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape.webp" alt="ランドスケープナンバーパッド" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-portrait.webp" alt="ポートレートナンバーパッド" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait.webp" alt="ポートレートキーボードとタッチパッド" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-km-basic-Touchpad.webp" alt="ランドスケープタッチパッド" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Remote-Coding-portrait.webp" alt="KeyCmd でのリモートコーディング" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Settings-screen.webp" alt="KeyCmd 設定画面" style="max-height:320px;" loading="lazy">
    </div>
  </div>

  <div class="slideshow-navigation">
    <button class="nav-arrow left" onclick="changeSlide('slideshow-keycmd-019-kbm-ja', -1)">❮</button>
    <div class="slideshow-dots">
      <span class="dot active" onclick="currentSlide('slideshow-keycmd-019-kbm-ja', 1)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ja', 2)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ja', 3)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ja', 4)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ja', 5)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ja', 6)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-ja', 7)"></span>
    </div>
    <button class="nav-arrow right" onclick="changeSlide('slideshow-keycmd-019-kbm-ja', 1)">❯</button>
  </div>
</div>

## KM Pro：Compose & Send モード

0.19 で最大の新機能は KM Pro の **Compose モード** — 長い文章を入力し、HID キーストロークとしてターゲットマシンに送信できる専用テキストエディタです。

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait.webp" alt="Compose モードでのスクリプト実行" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">


### Compose エディタ

- **上部ショートカットストリップ + コマンドアクション行**に**クリア**および**元に戻す/クリア**コントロール
- **ドラフト保持**：テキストはサブモード切り替えや送信成功后も保持されます
- **IME 統合**：スマートフォンのキーボードで入力し、クリーンな HID キーストロークとして送信
- **確定的な送信進行状況**：長い HID バッファーの進行状況バーで、送信の進捗を正確に把握可能

### Unicode 対応 HID 送信

- **デュアルモードリスクレビュー**：非 ASCII テキストを送信する前に、Unicode 互換性についての警告と検査/プレビューアクションを提供するダイアログ
- **macOS Unicode 16 進フロー**：macOS ホストでは、拡張文字に Option+16 進コード入力メソッドを使用
- **安全な送信ダイアログ**：レビュー画面は、バッファーが純粋な ASCII か Unicode 文字を含むかに応じて内容を調整
- **文字検査ツール**：送信リスクダイアログは**検査**および**プレビュー**アクションを提供し、macOS ホストには専用の **Unicode 16 進パス監査**エントリを含む

### KM Basic の範囲

0.19 では、**Compose & Send はキーボード＆マウス Pro の機能**です。KM Basic はフルスクリーンキーボード、タッチパッド、ナンバーパッドのワークフローに注力します。

## 多言語サポート

KeyCmd は現在 **11 種類のアプリ UI 言語**をサポートしています。このリリースでは 4 つの新しいローカライゼーションを追加しました：

- **韓国語 (ko)**：完全な UI 翻訳
- **イタリア語 (it)**：完全な UI 翻訳
- **ロシア語 (ru)**：完全な UI 翻訳
- **ブラジルポルトガル語 (pt-BR)**：完全な UI 翻訳

既存の英語、簡体字中国語、繁体字中国語、日本語、フランス語、ドイツ語、スペイン語と合わせ、KeyCmd はグローバルユーザーベースの大部分をカバーするようになりました。

### 変更内容

- 設定内の**言語ピッカー**に標準的なアプリ言語名を使用
- **Bluetooth ヘッダー**と**キータッププレビュー**のローカライズ
- 全言語での Compose 警告タブの**リリース lint**修正

## インタラクティブガイドツアー

すべてのモードに、機能をステップバイステップで案内する**内蔵インタラクティブガイドツアー**が追加されました。

### 利用可能なツアー

- **Shortcut Hub ツアー**：デフォルトプロファイルを開き、詳細 UI、カテゴリタブ、ショートカット管理をカバー
- **ゲームパッドツアー**：ゲームパッドレイアウト、モジュール管理、プリセットシステムを説明
- **KM Pro ツアー**：Compose モード、ショートカットパネル、Pro 固有の機能をカバー
- **KM Basic ツアー**：フルスクリーンキーボード、モディファイアホールドスワイプ、ナンバーパッドを説明

### ツアー機能

- **モード別ガイド**：各モードに合わせたツアー
- **再生シート**：**モードガイド**ボタン（接続クロムの左側のアイコン）からいつでもツアーを再訪問可能
- **i18n サポート**：ツアーコンテンツはアプリの全言語セットでローカライズ済み
- **ランドスケープ最適化**：ボトムシートレイアウトはランドスケープ向きで正しく適応

## UX 改善

### キーボード

- **キータッププレビュー**：タップする前に送信される内容を正確に確認可能。設定から有効化。デフォルトで有効。
- **高速タップ HID 修正**：キーボードタップの解放タイミングを改善し、解放イベントを統合して高速なタイピングを実現
- **代替文字タッチ処理**：キー `a` を長押しすると、¥（上）、£（左）、€（右）の代替文字が表示され、視覚フィードバックが改善
- **モディファイアホールドスワイプ**：KM Basic/Pro ツアーで、モディファイアへの素早いアクセスのためのホールドスワイプジェスチャを教える新しいステップを追加

### ゲームパッド

- **編集セッションバーを削除**：古い編集セッションツールバーのない、よりクリーンなゲームパッドクロム
- **ゲームパッドクロムとツアー**：新しいビジュアルポリッシュと統合ガイドツアー
- **モードガイドアイコン**：接続クロムの左側に配置して簡単アクセス

### プレゼンテーション

- **ポートレートペアロック**：プレゼンテーションモードは安定したプレゼンターコントロールのためにポートレートおよびリバースポートレート向きに制限

### UI＆テーマ

- **アクセントスウォッチ**：テーマカラーファミリースピナーを視覚的なアクセントスウォッチに置き換え、カラー選択を容易に
- **UI アクセント整列**：すべての UI アクセントはテーマカラーファミリに従う（レガシープライマリカラーではなく）
- **ヘッダー右クラスター**：メインアプリと KM Basic クロムの両方の接続アイコンのディメンションを改善
- **Compose 送信ボタンのスタイリング**：ライトモードでの非 ASCII 送信ボタンの外観を統一

### 設定

- **設定の再編成**：標準的なアプリ言語名；エミュレーターインストールスクリプトを明確化のためにリネーム
- **開発者ヘルパースクリプト**：デバイス識別とアクション命名を明確化するためにリネーム
- **FAQ ドキュメント**：現在のアプリの動作に合わせて `docs/FAQ.md` を更新

## 実際の使用例

### リモートコーディング

KeyCmd はサーバー管理だけのためではありません。開発者は**リモートコーディングセッション**に使用しています — フルキーボード、タッチパッド、ナンバーパッドをサポートしたスマートフォンまたはタブレットからのヘッドレス開発ボックスの制御。

## 変更のない部分

**キーボード＆マウス Pro**（Shortcut Hub ストリップ、分割レイアウト、豊富な IME 動作を備えたコンポジットモード）は以前と同じフル機能の体験のままです。既存のプロファイル、プリセット、ペアリング済みデバイスはすべて保持されます。

## アップデートの入手

**このバージョン (0.19)：** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

> **Beta 注意：** KeyCmd Android アプリはまだアクティブな Beta 段階です。ソースリポジトリはまだ公開されていません — 成功したクラウドファンディングキャンペーン後にオープンソース化する予定です。Beta テスターで最新の APK が必要な場合は、Discord でお問い合わせください。ビルドをお送りします。

既存インストールはその場アップグレードが可能です。

## Mini-KVM および KVM-Go での動作

KeyCmd アプリは KeyMod ハードウェアに限定されません。既存の Openterface ユーザーも試すことができます：

- **KVM-Go**：**Bluetooth** または **USB** で接続
- **Mini-KVM**：**USB** で接続

## アップグレードノート

- **ブランディング変更**：アプリ名が KeyMod から KeyCmd に変更されました。データは保持されます。
- **Compose モード**：キーボード＆マウス Pro に追加。
- **ガイドツアー**：任意のモードでガイドアイコン（接続クロムの左側）をタップしてインタラクティブツアーを開始。
- **言語**：設定でアプリ言語を変更可能。KeyCmd は現在 11 種類のアプリ UI 言語をサポート。

敬具、

Openterface Team | TechxArtisan
