---
draft: false
date: 2026-02-03
title: "KVM-GOでのmicroSD EXPRESS：互換性テストと実測転送速度"
description: "KVM-GO microSD EXPRESS互換性テスト、SanDisk 128GBカード使用。確認：検出と読み書き正常。実測速度は約30 MB/s書き込み、20 MB/s読み取り、USB 2.0ブリッジによる制限。UHS-IカードでKVM-GOのmicroSDパスに十分。"
keywords: "KVM-GO microSD, microSD EXPRESS KVM-GO, KVM-GO ストレージ, SanDisk microSD EXPRESS, KVM-GO 互換性, USB 2.0 microSD, KVM-GO 転送速度, microSDカード KVM-GO, Openterface KVM-GO"
author: "Openterface チーム | TechxArtisan"
category: "製品更新"
tags: ["KVM-GO", "製品更新", "microSD", "ストレージ", "互換性", "パフォーマンス"]
featured: false
social:
  image: "https://assets2.openterface.com/images/blog/SD-card.webp"
  title: "KVM-GOでのmicroSD EXPRESS：互換性と速度テスト"
  description: "SanDisk microSD EXPRESSカードをKVM-GOでテスト。動作するが、速度はUSB 2.0ブリッジで制限—UHS-Iで十分。"
---

# KVM-GOでのmicroSD EXPRESS：互換性テストと実測転送速度

コミュニティメンバーからKVM-GOがmicroSD EXPRESSカードをサポートするか質問がありました。推測せず、実際のmicroSD EXPRESSカードを入手してシンプルな互換性と速度チェックを実施しました。

---

## テスト内容

- **カード：** SanDisk microSD EXPRESS 128GB  

![テスト用カード：SanDisk microSD EXPRESS 128GB。](https://assets2.openterface.com/images/blog/SD-card.webp)  
*テスト用カード：SanDisk microSD EXPRESS 128GB。*

- **目的：** 基本互換性（検出＋読み書き）の確認と、KVM-GOのmicroSDパス経由の実測転送速度の計測。

---

## テスト環境

シンプルな「実使用」スタイルの転送テストでした：

1. microSD EXPRESSカードをKVM-GOのmicroSDスロットに挿入。  
2. Windows PCで、大容量のフォルダ/ファイルセットをmicroSDカードにコピーし、持続書き込み速度を観察。  
3. microSDカードからPCへデータをコピーし、持続読み取り速度を観察。  
4. 通常のOSファイルコピーを使用し、Windows転送ダイアログに表示される速度を記録。

![テスト環境：読み書きチェックのためmicroSD EXPRESSをKVM-GOに挿入。](https://assets2.openterface.com/images/blog/plug.webp)  
*テスト環境：読み書きチェックのためmicroSD EXPRESSをKVM-GOに挿入。*

---

## 互換性結果

KVM-GOはSanDisk microSD EXPRESSカードを正常に認識できます。  
読み書きともに問題なく動作します。

つまり「動く？」という質問への答えは **はい** です。

---

## 転送速度結果

カードはmicroSD EXPRESSですが、ここで得られる転送速度はKVM-GO内部のストレージパスに依存します。

テストではおおよそ以下を観察しました：

- **書き込み速度：** 約 **30 MB/s** 

![書き込みテスト（PC → microSD）：ファイルコピー中に約28 MB/sを観察。](https://assets2.openterface.com/images/blog/Performance.webp) 
*書き込みテスト（PC → microSD）：ファイルコピー中に約28 MB/sを観察。*

- **読み取り速度：** 約 **20 MB/s**

![読み取りテスト（microSD → PC）：ファイルコピー中に約22 MB/sを観察。](https://assets2.openterface.com/images/blog/Performance2.webp)  
*読み取りテスト（microSD → PC）：ファイルコピー中に約22 MB/sを観察。*

これらの数値はファイルサイズ、大小ファイルの混在、OSキャッシュの挙動、全体のワークロードにより変動しますが、一貫して観察された範囲です。

---

## Express速度が出ない理由

microSD EXPRESSカードは適切な環境でははるかに高い性能を発揮できますが、KVM-GOのmicroSDストレージパスはmicroSD-USBストレージ用の内部ブリッジ/コントローラで制限されています。

KVM-GOでは、そのブリッジはUSB 2.0で動作します。USB 2.0は480 Mbps（理論値）と説明されることが多いですが、実際のファイル転送ではプロトコルオーバーヘッドと実装の詳細により、持続スループットは通常かなり低くなります。

![USB 2.0ストレージパス参考。](https://assets2.openterface.com/images/blog/USB.webp)
*microSDストレージブリッジはUSB 2.0（理論480 Mbps）。実際のファイル転送スループットは低い。*

そのため、microSD EXPRESSはKVM-GOで正常に動作しますが、このmicroSDパス経由でExpressレベルの速度は期待できません。

---

## 実用的なまとめ

1. **microSD EXPRESSはKVM-GOと互換**  
   正常に検出され、読み書きが動作します。

2. **KVM-GOのmicroSDパス経由ではExpressレベルの速度は出ない**  
   ボトルネックは内部USB 2.0ストレージブリッジであり、カード自体ではありません。

3. **どのカードを買うべきか**  
   KVM-GOのmicroSD機能用に主に購入する場合、このシナリオではインターフェースが制限要因となるため、良いUHS-I microSDカードで十分です。

4. **Express速度が必要な場合**  
   より高速なUSBインターフェースの専用microSD EXPRESSリーダーを使用（KVM-GOとは別に）。

---

## 他のカードをテストしてほしい場合

特定のmicroSD EXPRESSモデル（ブランド＋容量＋型番）について知りたい場合は、共有していただければ同じチェックを実施して結果を追加します。
