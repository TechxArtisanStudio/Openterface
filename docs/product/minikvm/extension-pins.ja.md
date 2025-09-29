---
title: "拡張ピン"
description: "Openterface Mini-KVM の拡張ピンを活用して、カスタムハードウェア開発やオープンソースプロジェクトの可能性を探りましょう。"
keywords: "Mini-KVM 拡張ピン, カスタム開発, ハードウェア改造, オープンソース KVM"
---

# **拡張ピン** | 開発者モード | Openterface Mini-KVM

![mini-kvm-pins-port](https://assets.openterface.com/images/product/mini-kvm-pins-port.webp){:style="max-height:360px"}
![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="max-height:300px"}

Openterface Mini-KVM には高度な開発や [Open Software](/app) の実験のための拡張ピンが搭載されています。これらのピンは標準のケース構成では露出していません。

## ピンへのアクセス方法

1. デバイスを分解します。
2. 元のケースカバーを専用の拡張ピンキャップ（Extension Pin Cap）に交換します。
3. 拡張ピンキャップ用の [3D モデル](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models) をダウンロードします。
4. 当社の [Hardware GitHub リポジトリ](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware) を確認してください。

![change-cap](https://assets.openterface.com/images/product/change-cap.svg#only-light){:style="max-height:300px"}
![change-cap](https://assets.openterface.com/images/product/change-cap_1.svg#only-dark){:style="max-height:300px"}

!!! warning "保証無効"
    元のケースを取り外すと製品保証が無効になる場合があります。あらゆる改造や分解は、ユーザー自身の責任で行ってください。

!!! note "実験的機能"
    これらのピンを用いて開発された機能は実験段階であり、完全な検証は行われていません。拡張ピンの露出やその他の改造に起因する損傷、怪我、または故障について、Openterface は一切の責任を負いません。

## ピンの構成

![target-side](https://assets.openterface.com/images/product/extension-pins-1.svg#only-light){:style="max-height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2.svg#only-light){:style="max-height:200px"}
![target-side](https://assets.openterface.com/images/product/extension-pins-1_1.svg#only-dark){:style="max-height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2_1.svg#only-dark){:style="max-height:200px"}

拡張ピンは次の接続を提供します：

1. 外部コンポーネント用の USB 5V 電源
2. ホスト側 USB ハブへのデータ（プラス）
3. ホスト側 USB ハブへのデータ（マイナス）
4. ターゲット側 USB ハブへのデータ（プラス）
5. ターゲット側 USB ハブへのデータ（マイナス）
6. グラウンド

!!! danger "誤配線は故障の原因"
    VCC と GND を取り違えると、デバイスおよび接続されたコンポーネントに深刻な損害を与える可能性があります。通電前に必ずピン接続を再確認してください。

## 拡張ピンキャップ（Extension Pin Cap）

![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="max-height:360px"}

この 3D プリントの拡張ピンキャップは、Openterface Mini-KVM の元のキャップを置き換え、上級ユーザーがカスタム開発のために拡張ピンを露出・アクセスできるようにします。GitHub リポジトリから 3D モデルファイルをダウンロードし、自分で印刷できます。

- **用途**: 高度なハードウェア開発のための拡張ピンへのアクセスを提供します。
- **ダウンロード**: [3D モデルファイル](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models)

## 開発への参加

開発と実験を進めるにあたり、これらのピンで何ができるか、また創造的な活用方法について本セクションを随時更新していきます。皆さまの創造性と専門性が、Openterface Mini-KVM の可能性をさらに押し広げます。ぜひご参加ください：

1. **アイデアを共有**：これらのピンの活用に関するクールなアイデアはありますか？ぜひお聞かせください！
2. **DIY プロジェクトに貢献**：面白い作品を作成した場合は、[Discord Openterface](/discord) コミュニティでの共有をご検討ください。
3. **ディスカッションに参加**：他の開発者や愛好家とつながり、ブレインストーミングやコラボレーションを行いましょう。

一緒に創造し、革新していきましょう！
