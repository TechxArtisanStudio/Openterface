---
title: "Openterface Mini-KVM - 診断自己チェックガイド（macOS）"
description: "macOSアプリでOpenterface Mini-KVMデバイスの診断自己チェックを実行するためのステップバイステップガイド。USB接続のテスト、問題の検出、サポートへの欠陥報告の送信方法を学びましょう。"
keywords: "Openterface Mini-KVM, macOS, 診断自己チェック, KVMトラブルシューティング, USB KVM診断, Mini-KVMサポート, KVMデバイステスト, USB接続テスト, KVM欠陥報告, Mini-KVMトラブルシューティングガイド, KVM診断ツール, ヘッドレスサーバー診断, ITトラブルシューティングツール"
---

# Openterface Mini-KVM - 診断自己チェックガイド（macOS）

このガイドは、Openterface Mini-KVMデバイスで診断自己チェックを実行するためのステップバイステップの指示を提供します。

<iframe width="560" height="315" src="https://www.youtube.com/embed/-K6Idzky3fY?si=r7pZgCkBzzZXgrLT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## 良好なユニット

**ステップ1:** Openterfaceアプリで、設定 → 設定…を開きます。

**ステップ2:** 設定ウィンドウで、高度な設定 & デバッグに移動します。

**ステップ3:** 診断ツールを開くをクリックします。

**ステップ4:** プロンプトが表示されたら、診断ログを有効にするために「Enable」をクリックします。

**ステップ5:** 「Check Now」をクリックして自己チェックを開始します。

**ステップ6:** 「Start Test」をクリックし、求められたら黒いUSB-C（ターゲット側）を抜き差しします。

![minikvm-support-target](https://assets.openterface.com/images/minikvm/support/target.webp)

**ステップ7:** 「Start Test」をクリックし、求められたらオレンジのUSB-C（ホスト側）を抜き差しします。

![minikvm-support-host](https://assets.openterface.com/images/minikvm/support/host.webp)

**ステップ8:** 「Start Test」をクリックし、テストが完了するのをお待ちください。

**ステップ9:** 「Reset Now」をクリックし、完了するまでお待ちください。

**ステップ10:** 「Change Now」をクリックし、ボーレートの切り替えが完了するまでお待ちください。

**ステップ11:** 「Start Test」をクリックし、約30秒お待ちください。テストが実行中の間はターゲットを操作しないでください。

> **注意:** マウスが急速に動くことがあります。ターゲットを触れないでください。

![minikvm-support-stress_test](https://assets.openterface.com/images/minikvm/support/stress_test.gif)

**ステップ12:** すべての項目が緑色のチェックマークを表示し、進行状況が完了していることを確認してください。

**ステップ13:** Diagnosticsウィンドウを閉じるには、右上隅の ❌ をクリックします。

---

## 問題が検出された場合（キーボード/マウスの例）

まず「Good Unit」でステップ1～11を実施してください。以下のノートは、キーボード/マウスの問題が検出されたときに表示される内容を説明しています。

## この問題の表示方法

この例では、ターゲット側のキーボード/マウス（HID）の問題により、全体的なチェックが最初に「FAIL」を表示します。これは早期の指標であり、個別の問題ではありません。（左側に「Overall Connection」の隣にFAILステータスが強調表示されます。）

- **全体的な接続:** ターゲット側の問題により、ここに最初に「FAIL」が表示されます。

![minikvm-support-overall_connection](https://assets.openterface.com/images/minikvm/support/overall_connection.webp)

- **ターゲットの即席接続:** このステップを実行した後、ターゲット側の問題がより明確に表示されることがあります。

> **ヒント:** ステップで「FAIL」が表示された場合、診断は停止しませんが、自動進行が止まることがありますので、手動で進める必要があります。

## 追加の最終テスト（問題タイプによります）

**ステップ12:** ストレステスト後、検出された問題に応じて診断が追加の最終テストを表示することがあります。このキーボード/マウスの例では、ターゲットポートチェックに続きます。

**ステップ13:** 「Detect Devices」をクリックしてターゲットポートチェックを開始し、画面の指示に従ってください。

![minikvm-support-target_port_checking](https://assets.openterface.com/images/minikvm/support/target_port_checking.webp)

## 問題が検出されたときの処理

**ステップ14:** 続けるには、下部バーの「Next」をクリックするか、左パネルから次のテストを選択してください。

![minikvm-support-target_plug_n_play](https://assets.openterface.com/images/minikvm/support/target_plug_n_play.webp)

## ログをサポートに送信する

**ステップ15:** サポートへの欠陥報告を準備するために「Send Defect Report to Support」をクリックします。

![minikvm-support-send_defect_report_to_support](https://assets.openterface.com/images/minikvm/support/send_defect_report_to_support.webp)

**ステップ16:** 欠陥報告ウィンドウで、**注文ID**と**名前**を入力し、**適用**をクリックしてメールの下書きに挿入してください。

**ステップ17:** メールアドレスと下書きをコピーします：
- **メールをコピー**をクリックしてサポートのメールアドレスをコピーします。
- **下書きをコピー**をクリックして事前記入されたメール内容（注文ID + 名前を含む）をコピーします。
- 両方をメールクライアント（Gmail/Outlookなど）に貼り付けてください。

![minikvm-support-support](https://assets.openterface.com/images/minikvm/support/support.webp)

**ステップ18:** **ログフォルダを開く**をクリックします。ツールが添付するファイルを表示します。**要求されたログファイルのみを添付してください**（フォルダには他の多くのログが含まれている場合があります）。

**ステップ19:** 同じメールに、明確な**設定写真**を添付してください。写真には以下が写っている必要があります：
- Mini-KVMデバイス、
- **ホスト**と**ターゲット**の両方の接続、
- ポートとケーブルがはっきり見えること。

**ステップ20:** サポートにメールを送信してください（下書きテキスト + 要求されたログ + 設定写真を添付）。

**ステップ21:** Diagnosticsウィンドウを閉じるには、右上隅の ❌ をクリックします。