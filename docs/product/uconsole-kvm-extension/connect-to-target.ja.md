---
title: "ターゲットデバイスに接続"
description: "Openterface KVM Extension for uConsoleにターゲットデバイスを接続する方法を学びます。ハードウェアインストールとソフトウェア設定後のUSB制御とビデオ入力設定の完全ガイド。"
keywords: "KVM接続設定, ターゲットデバイス接続, USB制御設定, HDMI入力設定, uConsole KVM拡張接続"
---

# **ターゲットデバイスに接続** | Openterface KVM Extension for uConsole

## 接続概要

![extension-use-case-1a](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1a.webp){:style="height:480px"}

## 前提条件

ターゲットデバイスを接続する前に、以下が完了していることを確認してください：

1. [ハードウェアインストール](/product/uconsole-kvm-extension/hardware-installation/) - KVM Extensionボードの物理的インストール
2. [ソフトウェア設定](/product/uconsole-kvm-extension/software-setup/) - Openterface Appのインストール

## 接続手順

### **USB制御**
Type-CメスポートをターゲットデバイスのUSBポートに接続して、キーボードとマウス信号をエミュレートします。

### **ビデオ入力**
ターゲットデバイスのビデオ出力をKVM ExtensionのHDMIポートに接続します：

- HDMI出力デバイスの場合は、標準HDMIケーブルを使用
- VGA出力デバイスの場合は、VGA-to-HDMI変換ケーブルを使用。
    - *注意*：正常動作のために、変換器がUSBコネクタ経由で電源供給されていることを確認してください。
- 異なるビデオ信号タイプには、他の適切なアダプターを使用

## 接続のテスト

1. 電源を入れ、uConsoleを起動
2. Openterface QT appを実行
3. HDMI、オーディオ、USB HID機能をテストして正常動作を確認
