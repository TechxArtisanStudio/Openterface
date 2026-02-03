---
title: "Openterface Mini-KVM (Windows) - ハードウェア診断自己チェックガイド"
description: "Windows版Openterfaceアプリでハードウェア診断自己チェックを実行するためのステップバイステップガイド。USB接続のテスト、問題の検出、サポートへの診断レポートの送信方法を学びましょう。"
keywords: "Openterface Mini-KVM, Windows, ハードウェア診断, 診断自己チェック, KVMトラブルシューティング, USB KVM診断, Mini-KVMサポート, KVMデバイステスト, Windows KVM, KVM欠陥報告, Mini-KVMトラブルシューティングガイド"
---

# Openterface Mini-KVM (Windows) — ハードウェア診断自己チェックガイド

このガイドでは、**Windows**版Openterfaceアプリで**ハードウェア診断**自己チェックを実行する方法と、問題が検出された場合にサポートへ診断レポートを送信する方法を説明します。

---

## 開始前に

- Mini-KVMを**ホスト**と**ターゲット**の両方に接続してください。
- テスト中（特にストレステスト中）はターゲットデバイスをアイドル状態に保ってください。

> **重要（Windows）:** 診断は**自動進行しません**。  
> テスト間を移動するには、**Next**（下部バー）を使用するか、**左パネル**のテスト項目をクリックしてください。  
> 各テストは**Check Now**をクリックして実行します。

![next_webp](https://assets2.openterface.com/images/next.webp)

---

## 正常なユニット（PASS）

### ステップ1 — ハードウェア診断を開く（Windows）
Windows Openterfaceアプリで、**Advanced → Hardware Diagnostics**を開きます。  

### ステップ2 — 自己チェックを実行
ハードウェア診断ウィンドウで、**Check Now**をクリックして現在の診断ステップを実行します。  

### ステップ3 — ターゲット Plug & Play（プロンプトに従う）
**Target Plug & Play**がターゲットケーブルの再接続を求めたら、画面の指示に従ってください。  
一部のセットアップでは、**複数回**（例：2回）抜き差しを求められる場合があります。  

![Target-plug&play](https://assets2.openterface.com/images/Target-plug%26play.webp)

### ステップ4 — ホスト Plug & Play（プロンプトに従う）
ホスト側の画面の指示に従ってください。  

![Host-plug&play](https://assets2.openterface.com/images/Host-plug%26play.webp)

### ステップ5 — ストレステスト（ターゲットに触れない）
**Stress Test**中、ターゲットマウスが検出のために自動的に動くことがあります。  
テスト実行中は**ターゲットを操作しないでください**。  

> **注意:** マウスが急速に動くことがあります — ターゲットに触れないでください。

![stress-test](https://assets2.openterface.com/images/stress-test.webp)

### ステップ6 — PASSを確認
自己チェックが完了するまで続けてください。すべて正常な場合、結果に**PASS / All Tests Passed**と表示されます。  

---

## 問題が検出された場合（キーボード/マウスの例）

問題が検出されると、1つ以上の項目に**FAIL**と表示される場合があります。

### ステップ1 — 同じハードウェア診断を実行
**Advanced → Hardware Diagnostics**を開き、**Check Now**をクリックして開始します。  

### ステップ2 — チェックを続行
診断が完了するまで残りのテストを続けてください。  

### ステップ3 — サポートメールが自動的に開く
問題がある状態で診断が完了すると、**Support Email**ウィンドウが自動的に開きます。  

---

## ログをサポートに送信する（Windows）

### ステップ4 — 注文ID + 名前を適用
**注文ID**と**名前**を入力し、**適用**をクリックしてメールの下書きに挿入します。 

![ID+Name](https://assets2.openterface.com/images/ID+Name.webp)

### ステップ5 — メールアドレスと下書きをコピー
- **Copy Email**をクリックしてサポートのメールアドレスをコピーします。
- **Copy Draft**をクリックして事前記入されたメール内容（注文ID + 名前を含む）をコピーします。  
両方をメールクライアント（Gmail/Outlookなど）に貼り付けてください。  

![copy](https://assets2.openterface.com/images/copy.webp)

### ステップ6 — 正しいログファイルを添付
**Open File Folder**をクリックします。ツールが添付するファイルを表示します。  
**要求されたログファイルのみを添付してください**（フォルダには他の多くのログが含まれている場合があります）。  

![list](https://assets2.openterface.com/images/list.webp)

![compress](https://assets2.openterface.com/images/compress.webp)

### ステップ7 — 設定写真も添付
同じメールに、明確な**設定写真**を添付してください。写真には以下が写っている必要があります：
- Mini-KVMデバイス、
- **ホスト**と**ターゲット**の両方の接続、
- ポートとケーブルがはっきり見えること。  

### ステップ8 — メールを送信
サポートにメールを送信してください（下書きテキスト + 要求されたログ + 設定写真を添付）。  

---

## サポートに連絡する際に含める内容

- **注文ID**
- **要求された診断ログファイル**
- **設定写真**（Mini-KVM + ホスト/ターゲット配線）
