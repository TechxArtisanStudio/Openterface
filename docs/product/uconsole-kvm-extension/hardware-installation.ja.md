---
title: "ハードウェアインストール"
description: "Openterface KVM Extension for uConsole のステップバイステップハードウェアインストールガイド。詳細な安全ガイドラインとともに、uConsole の拡張スロットに拡張ボードを正しくインストールする方法を学びます。"
keywords: "KVM拡張インストール, uConsoleハードウェアセットアップ, 拡張ボードインストール, uConsole拡張スロット, KVMハードウェアガイド, 物理インストール"
---

# **ハードウェアインストール** | Openterface KVM Extension for uConsole

## 概要
KVM Extension は uConsole の拡張スロット内の 4G/LTE モジュールを置き換え、直接 HDMI 入力と USB HID 制御を追加します。

## 必要なもの
- インストール前に[パッケージ内容](whats-in-the-box.md)を確認してください  
- Openterface KVM Extension ボード  
- 提供された**ワッシャー**（安定したマウントと均等な圧力を確保）  
- 六角レンチ（マウントスクリュー用）  
- ESD 保護（リストストラップまたは接地表面）— 推奨  

## インストール手順

### **1. 電源オフ**
uConsole をシャットダウンし、すべての電源とケーブルを切断します。

### **2. 既存モジュールの取り外し**
六角レンチを使用して2つのスクリューを取り外します。  
ボードを**真っ直ぐ上に**持ち上げて、スプリングコンタクタを曲げないようにします。

### **3. KVM Extension のインストール**
- **ワッシャー**をスクリューポストに配置します。  
- KVM Extension を拡張スロットにしっかりと装着します。  
- ワッシャーは少し薄い PCB（1.0 mm vs 1.2 mm）を補償し、適切なスプリングコンタクト圧力を維持します。

??? note "最終インストール前にフィットを確認"
    まず**ワッシャーなしで**ボードを装着してフィットをテストできます。ボードが緩い感じがしたり、コンタクトが不均一な場合は、ワッシャーを追加してボードを再装着してください。Openterface KVM Extension は 1.0 mm の厚さで、元の LTE モジュール（1.2 mm）より少し薄いです。提供されたワッシャーを使用することで、安定したマウントと信頼性の高いスプリングコンタクトを確保します。  
    ![extension-slot-loose](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-slot-loose.webp){:style="height:220px"}

### **4. ボードの固定**
スクリューを再挿入し、**優しく**締めます — **締めすぎないでください**。これによりボードが損傷したり、ネジ山が削れたりする可能性があります。

![extension-screw-washer-installed](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installed.jpg){:style="height:220px"}
![extension-screw-washer-installing](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installing.jpg){:style="height:220px"}
![extension-install-1](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp){:style="height:220px"}

### **5. インストールの確認**
ボードは**平らで安定**しており、すべてのパッドで均等なスプリングコンタクトがあるはずです。目立つ揺れや動きはないはずです。

### **6. 拡張スロットカバーのインストール**
KVM Extension ボードを保護し、uConsole の元の外観を維持するために拡張スロットカバーを再インストールします。

??? note "拡張スロットカバーのテキスト方向"
    特定の角度から見ると、拡張スロットカバーのテキストが「逆さま」に見える場合があります。これは意図的なデザインです - テキストは、uConsole を持ってポートを上から下に見る際に読み取れるように向けられており、これはデバイスを使用する際の自然な視点です。
    ![expansion-slot-text-orientation](https://assets.openterface.com/images/product/openterface-kvm-uconsole-expansion-slot-text-orientation.webp){:style="height:220px"}

---

**次のステップ**

1. [ソフトウェアセットアップ](/product/uconsole-kvm-extension/software-setup/)に移動して Openterface App をインストールします。  
2. [ターゲットデバイスに接続](/product/uconsole-kvm-extension/connect-to-target/)に移動してターゲットデバイスを接続します。  
3. [機能と仕様](/product/uconsole-kvm-extension/features/)を確認して詳細な技術仕様を確認します。
