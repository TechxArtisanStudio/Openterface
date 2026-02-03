---
title: Openterface Mini-KVM よくある質問
description: Mini-KVM に関するよくある質問。機能、互換性、トラブルシューティング、将来の計画について説明します。
keywords: Mini-KVM, Openterface, KVM スイッチ, オープンソース, トラブルシューティング, ビデオキャプチャ, USB, 互換性, 診断自己チェック, キーボードマウス制御, ハードウェア診断, サポート
---

# Openterface Mini-KVM よくある質問

私たちのフラッグシップ製品 **Openterface Mini-KVM** のよくある質問へようこそ。  
必要な情報が見つからない場合は、**[info@openterface.com](mailto:info@openterface.com) にメール**を送信するか、[Discord](/discord) や [Reddit](/reddit) で**コミュニティに参加**してください。

⚠️ _よくある質問は古くなっている可能性があります — 更新が必要な内容を見つけた場合はお知らせください。_

---

## :material-clipboard-list: クイックナビゲーション

-   [USB ポートとファイル転送](#usb-ポートとファイル転送)
-   [技術](#技術)
-   [制御](#制御)
-   [ビデオ](#ビデオ)
-   [トラブルシューティング](#トラブルシューティング)
-   [その他](#その他)

---

## USB ポートとファイル転送

**:material-chat-question:{ .faq } ファイル転送はできますか？**

はい — ホストとターゲット間で共有される切り替え可能な USB-A ポート経由で可能です。

**:material-chat-question:{ .faq } USB ポートをソフトウェアで切り替えることはできますか？**

はい、ハードウェアバージョン **v1.9+** で可能です。

**:material-chat-question:{ .faq } USB 3.0 ではなく 2.0 を使用する理由は？**

USB 2.0 は 1080p@30Hz ビデオ + HID + 標準速度ファイル転送に十分で、コンパクト、冷却性、価格の面で優れています。  
USB 3.0 は将来のプロモデルに登場する可能性があります。

---

## 技術

**:material-chat-question:{ .faq } オープンソースですか？**

はい — [OSHWA](https://certification.oshwa.org/cn000015.html) に認定されています。ハードウェアとソフトウェアは [GitHub](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware) にあります。

**:material-chat-question:{ .faq } BIOS アクセス**

直接 USB 接続により、リモート専用ツール（VNC、TeamViewer）とは異なり、完全な BIOS レベル制御が可能です。  
古いマシンでは、USB ハブの認識で BIOS の問題が発生する可能性があります — そのような場合は報告してください。

**:material-chat-question:{ .faq } ビデオ/データ伝送**

ビデオは HDMI 経由でキャプチャされ、USB 2.0 経由で送信されます。  
切り替え可能な USB ポートにより、ドライブやその他のデバイスを共有できます。

**:material-chat-question:{ .faq } 電源処理**

Mini-KVM は**どちら側**（ホストまたはターゲット）からも電源を取得できます。**短いケーブル**の側が通常メイン電源になります。  
低電力ターゲット（例：Raspberry Pi）の場合は、Mini-KVM 経由の逆給電ではなく、専用電源を使用してください。

**:material-chat-question:{ .faq } ケーブル長制限**

-   **オレンジ色のホスト USB-C ケーブル ≤1.5m** を維持してください。
-   より長いケーブルの場合、以下で電源を注入してください：
    -   USB-A オス-オスケーブル
    -   [拡張ピン](/product/minikvm/extension-pins/)
    -   USB-C Y スプリッター
-   同じルールが**黒いターゲットケーブル**にも適用されます。

---

## 制御

**:material-chat-question:{ .faq } キーボードとマウスでターゲットコンピューターを制御できない**

ターゲットデスクトップは表示されるがキーボードとマウスの入力が反応しない場合、通常は HID 通信が確立されていないことを意味します。次の手順を試してください：

1. **ケーブル接続を確認** — ターゲット Type-C ケーブルがターゲットコンピューターに接続されていること、ホストケーブルが制御コンピューターに接続されていることを確認してください。
2. **無電源 USB ハブを避ける** — 直接接続または有源ハブを使用してください。
3. **HID チップをリセット** — デバイスが「フリーズ」しているように見える場合は、**詳細メニュー → HID チップ工場リセット**（OpenterfaceQt）または **シリアルリセットツール**（macOS）を使用してください。
4. **別の USB ポートを試すか再起動** — ホスト OS が USB エラー後にポートを無効にしている可能性があります。
5. **ボーレートを下げる** — ノイズの多い環境では、より信頼性の高い通信のために 9600 bps に切り替えてください。

詳細は[キーボードとマウス制御のトラブルシューティング](/product/minikvm/support/keyboard-mouse-control/)をご覧ください。

**:material-chat-question:{ .faq } ワイヤレスまたはイーサネット版？**

内蔵されていません。リモート制御にはヘッドレスコンピューター（例：Raspberry Pi）+ リモートデスクトップを使用してください。

**:material-chat-question:{ .faq } PS/2 互換性？**

対応していません — PS/2 サポートは将来のバージョンで検討される可能性があります。

**:material-chat-question:{ .faq } 1 台のコンピューターで複数の Mini-KVM？**

はい、QT アプリ（Windows/Linux）の実験的機能です。

**:material-chat-question:{ .faq } 電源オン/オフ制御？**

直接はできませんが、[拡張ピン](/product/minikvm/extension-pins/)により将来の ATX 制御モジュールが可能になります。

---

## ビデオ

**:material-chat-question:{ .faq } レイテンシと解像度**

-   **1080p@30Hz** でキャプチャ
-   **140ms 未満**のレイテンシ → スムーズな制御

**:material-chat-question:{ .faq } 入力とキャプチャ解像度**

-   **4K@30Hz** までの入力を受け入れ
-   **1080p** でキャプチャ、より高い入力はダウンサンプリングされます（少しぼやけて見える場合があります）。
-   ベストプラクティス：**ターゲットを 1080p に設定**してください。

**:material-chat-question:{ .faq } ゲーム適性**

AAA ゲームには適していません。Minecraft やエミュレーターなどの軽いゲームには良好に動作します。

**:material-chat-question:{ .faq } インターネット経由のリモート制御**

内蔵されていませんが、Mini-KVM をホスト上のリモートデスクトップソフトウェアと組み合わせることができます。

**:material-chat-question:{ .faq } その他のビデオフォーマット**

VGA、DVI、DisplayPort などにはアダプターを使用してください。

---

## トラブルシューティング

**:material-chat-question:{ .faq } Mini-KVM が正常に動作しているか診断するには？**

USB 接続を検証し、ハードウェアの問題を検出するには、組み込みの診断自己チェックを実行してください：

- **macOS：** [診断自己チェックガイド（macOS）](/product/minikvm/support/diagnostic-self-check/) — 設定 → 高度な設定 & デバッグ → 診断ツールを開く
- **Windows：** [診断自己チェックガイド（Windows）](/product/minikvm/support/diagnostic-self-check-windows/) — 高度な設定 → ハードウェア診断

診断はターゲット/ホスト プラグ & プレイ、ストレステストなどをテストします。すべてのテストが通過すれば、デバイスは正常に動作しています。

**:material-chat-question:{ .faq } ハードウェアの問題をサポートに報告するには？**

診断自己チェックで 1 つ以上のテストが**失敗**と表示された場合：

1. 残りの診断の手順を完了してください（ツールが案内します）。
2. 問題が検出されると、**サポートメール**または**欠陥報告**ウィンドウが開きます。
3. **注文ID**と**名前**を入力し、メールアドレスと下書きをコピーしてください。
4. **要求されたログファイル**（ツールが指示）と**設定写真**（Mini-KVM + ホスト/ターゲット接続が明確に写っている）を添付してください。
5. サポートにメールを送信してください。

ステップバイステップの説明は [診断自己チェックガイド（macOS）](/product/minikvm/support/diagnostic-self-check/) または [診断自己チェックガイド（Windows）](/product/minikvm/support/diagnostic-self-check-windows/) をご覧ください。

**:material-chat-question:{ .faq } USB ハブの問題**

電圧降下による不安定性を避けるため、**有源ハブ**を使用してください。無電源ハブは電力供給不足や HID（キーボード/マウス）の不安定な動作を引き起こす可能性があります。詳細は[キーボードとマウス制御のトラブルシューティング](/product/minikvm/support/keyboard-mouse-control/)をご覧ください。

**:material-chat-question:{ .faq } アプリにビデオが表示されない、または制御が応答しない**

1. すべてのケーブルを切断し、数秒待ってから再接続してください。
2. HID の問題（ケーブル、ハブ、HID リセット）については[キーボードとマウス制御のトラブルシューティング](/product/minikvm/support/keyboard-mouse-control/)をご確認ください。
3. デバイスを検証するには[診断自己チェック](/product/minikvm/support/diagnostic-self-check/)（macOS）または[ハードウェア診断](/product/minikvm/support/diagnostic-self-check-windows/)（Windows）を実行してください。
4. 解決しない場合は、ファームウェアを確認するか、ホストアプリを更新してください。

**:material-chat-question:{ .faq } 43184x24228@44Hz のような奇妙な解像度**

キャプチャファームウェアが工場出荷状態に戻った可能性があります。  
[GitHub リリース](https://github.com/TechxArtisanStudio/Openterface_QT/releases) 経由でファームウェアを再フラッシュしてください。

**:material-chat-question:{ .faq } 再フラッシュしてもまだ壊れている？**

-   正しい USB 列挙を確認（`USB Tree Viewer` または `lsusb -v`）
-   最新のホストアプリを確認
-   [診断自己チェック](/product/minikvm/support/diagnostic-self-check/)を実行してログをキャプチャ
-   それでも失敗する場合は、注文ID、診断ログ、設定写真を添えてサポートに連絡 — [ハードウェアの問題をサポートに報告するには？](#ハードウェアの問題をサポートに報告するには) を参照
