---
title: "接続方法"
description: "Openterface KVM-Go のセットアップ手順ガイド。内蔵ビデオコネクタを使用してホストコンピューターとターゲットデバイスを接続し、超シンプルな直接プラグイン体験を学びましょう。"
keywords: "KVM-Go セットアップ, 超コンパクト KVM セットアップ, 内蔵 HDMI 接続, KVM インストールガイド, キーホルダー KVM セットアップ, USB KVM 接続, ヘッドレスコンピューターセットアップ, ポータブル KVM セットアップ"
---

# **接続方法** | セットアップガイド | Openterface KVM-Go

## **接続の概要**

![KVM-Go 接続概要](https://assets.openterface.com/images/kvm-go/step-0-overview.webp){:style="max-height:360px"}

上の画像は、[**KVM-Go**](/product/kvm-go)、ホストコンピューター、ターゲットデバイス間のすべての接続を示しています。

- **ホストコンピューター**：[Openterface アプリ](/app)のインストールが必要です。  
- **ターゲットデバイス**：ソフトウェアや事前設定は不要です。
- **ビデオ**：内蔵コネクタがターゲットデバイスに直接接続されるため、追加のビデオケーブルを持ち運んだり管理したりする必要はありません。

## **接続に必要なもの**

![KVM-Go 全部品](https://assets.openterface.com/images/kvm-go/step-0-all-parts.webp){:style="max-height:360px"}

**KVM-Go** をセットアップするには、以下のコンポーネントが必要です：

- **KVM-Go (HDMI / DP / VGA)** — **ターゲットデバイス**に接続（ビデオキャプチャ用）  
- **黒い短い USB-C ケーブル** — **ターゲットデバイス**に接続（キーボードとマウスのエミュレーション用）
- **オレンジ色の長い USB-C ケーブル** — **ホストコンピューター**に接続（[Openterface アプリ](/app)を実行）

!!! note "ケーブル長に関する免責事項"
    **公式 KVM-Go パッケージ**に含まれる正確なケーブル長は**まだ確定していません**ので、ここに示されているものとは若干異なる場合があります。  
    このガイドで使用されているケーブルは *クラシック Mini-KVM ツールキット* のもので、説明目的のみに使用されています。

!!! warning "独自のケーブルを使用する場合"
    独自のケーブルを使用する場合は、**高品質でデータ転送可能な USB ケーブル**であることを確認してください。低品質または充電専用ケーブルを使用すると、以下の問題が発生する可能性があります：
    
    - 黒い画面の問題
    - キーボードまたはマウス入力が無反応
    - 断続的な接続切断
    - ちらつきや不安定なディスプレイ出力

## **ステップバイステップセットアップ**

### **ステップ 1 — USB ケーブルを KVM-Go に接続**
![USB ケーブルの接続](https://assets.openterface.com/images/kvm-go/step-1-plugged.webp){:style="max-height:360px"}

- **黒い USB-C ケーブル** → KVM-Go ケース上の ![ターゲットアイコン](https://assets.openterface.com/images/shell-icons/target-computer.svg#only-light){:style="max-height:20px"} ![ターゲットアイコン](https://assets.openterface.com/images/shell-icons/target-computer_1.svg#only-dark){:style="max-height:20px"} **Target** とラベル付けされたポートに差し込みます。  
- **オレンジ色の USB-C ケーブル** → ![ホストアイコン](https://assets.openterface.com/images/shell-icons/host-computer.svg#only-light){:style="max-height:20px"} ![ホストアイコン](https://assets.openterface.com/images/shell-icons/host-computer_1.svg#only-dark){:style="max-height:20px"} **Host** とラベル付けされたポートに差し込みます。

!!! warning
    両方の USB-C ポートは物理的に同一です。  
    混同を避けるため、常にケース表面の**ラベルを再確認**してください。

### **ステップ 2 — ビデオをターゲットに接続**
![HDMI コネクタの接続](https://assets.openterface.com/images/kvm-go/step-3-hdmi-plugged.webp){:style="max-height:360px"}

**内蔵オスビデオコネクタ**をターゲットデバイスのビデオ出力ポートに直接差し込みます。

### **ステップ 3 — ターゲット USB ポートに接続**
**黒い USB ケーブル**をターゲットデバイスに接続して HID 制御を行います。

- **オプション A：** USB-A ポートに直接接続  
  ![ターゲット USB-A](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-b.webp){:style="max-height:360px"}

- **オプション B：** USB-C アダプターを使用  
  ![ターゲット USB-C](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-a.webp){:style="max-height:360px"}

!!! note "USB-C 接続チェック"
    一部の USB-C ポートは安全な接続を提供しない場合があります。断続的なキーボード/マウス制御の問題が発生した場合は、アダプター接続を軽く揺らして、適切に装着され接触していることを確認してください。


### **ステップ 4 — ホスト USB ポートに接続**
**オレンジ色の USB ケーブル**をホストコンピューターに接続します。

- USB-C ポートに直接接続**または** USB-C から USB-A アダプター経由で接続。  
  ![ホスト USB の接続](https://assets.openterface.com/images/kvm-go/step-5-plug-in-host-computer-1.webp){:style="max-height:360px"}

