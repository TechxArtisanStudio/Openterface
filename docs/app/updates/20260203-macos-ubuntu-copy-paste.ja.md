---
title: Ubuntu コピー/ペーストのヒント（macOS → Ubuntu）
description: Openterface で macOS から Ubuntu を操作する際のペーストショートカットの修正方法。Ctrl スタイルのペーストには Windows モードを、Mac モードのままの場合は編集 → 貼り付けを代替手段として使用。
keywords: Openterface, macOS, Ubuntu, コピー貼り付け, キーボードモード, Windows モード, Mac モード, KVM, リモートデスクトップ
author: Openterface
date: 2026-02-03
tags:
  - macOS
  - Ubuntu
  - keyboard
  - copy-paste
---

# Ubuntu コピー/ペーストのヒント（macOS → Ubuntu）

**Openterface** を使って **macOS** から **Ubuntu** を操作する場合、**Mac モード**ではショートカットでのペーストが安定して動作しないことがあります。本ガイドでは推奨される修正方法と簡単な代替手段を紹介します。

![setting](https://assets2.openterface.com/images/setting.webp)

---

## クイック修正（Ubuntu/Linux 推奨）

1. macOS で **Openterface** を開く。
2. **設定** に移動する。
3. **ターゲットデバイスのキーボードレイアウトモード** を探す。
4. **Windows モード** を選択する。

![win-mode](https://assets2.openterface.com/images/win-mode.webp)


✅ 結果：Ubuntu でペーストショートカットが期待通りに動作します（Ctrl スタイルの動作）。

![win-ctrl+v](https://assets2.openterface.com/images/win-ctrl+v.webp)

---

## 代替手段（Mac モードのままの場合）

**Mac モード**のままにしたい場合は、メニューから確実にペーストできます：

- **編集 → 貼り付け**

![edit-paste](https://assets2.openterface.com/images/edit-paste.webp)

✅ 結果：Mac モードでショートカットペーストが不安定でも、メニューからのペーストは確実に動作します。

![workaround](https://assets2.openterface.com/images/workaround.webp)

---

## なぜこうなるのか

多くの Ubuntu アプリはペーストに **Ctrl ベース**のショートカットを使用しています。一部の環境では、**Mac モード**のショートカットマッピングがペーストを一貫してトリガーしないことがありますが、**編集 → 貼り付け**は確実に動作します。

---

## クイックまとめ

- **Ubuntu/Linux で最良の体験：** **Windows モード**を使用
- **Mac モードのままの場合：** **編集 → 貼り付け**を使用

---

## どのモードを使うか迷っている場合

どのモードを使うかわからない場合は、次の簡単な目安を参考にしてください：

- ターゲット OS が **Ubuntu/Linux** の場合は、**Windows モード**から始める（一般的なショートカットで最も一貫性があります）。
- 主に **macOS ターゲット**を操作し、Mac スタイルのショートカットを使いたい場合は、**Mac モード**を使用。

異なるターゲット OS を頻繁に切り替える場合は、このページをブックマークしておくと便利です。通常はワンクリックで修正できます。

---

## よくある質問

**Windows モードは Mac のショートカットを変更しますか？**  
Openterface が**ターゲットデバイス**に送信するショートカットの方法を変更するため、Ubuntu は期待される **Ctrl スタイル**の動作を受け取ります。

**どのモードでもメニューからのペーストは使えますか？**  
はい — **編集 → 貼り付け**は両方のモードで確実な選択肢です。

**Raspberry Pi OS にも影響しますか？**  
影響は少ないことが多いですが、同様の動作が見られる場合は、同じ修正が適用されます。
