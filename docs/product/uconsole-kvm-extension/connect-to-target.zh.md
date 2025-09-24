---
title: "连接到目标设备"
description: "学习如何将目标设备连接到Openterface KVM Extension for uConsole。硬件安装和软件设置后USB控制和视频输入设置的完整指南。"
keywords: "KVM连接设置, 目标设备连接, USB控制设置, HDMI输入设置, uConsole KVM扩展连接"
---

# **连接到目标设备** | Openterface KVM Extension for uConsole

## 连接概述

![extension-use-case-1a](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1a.webp){:style="height:480px"}

## 前提条件

在连接目标设备之前，请确保您已完成：

1. [硬件安装](/product/uconsole-kvm-extension/hardware-installation/) - KVM Extension板的物理安装
2. [软件设置](/product/uconsole-kvm-extension/software-setup/) - Openterface App的安装

## 连接步骤

### **USB控制**
将Type-C母端口连接到目标设备的USB端口，以模拟键盘和鼠标信号。

### **视频输入**
将目标设备的视频输出连接到KVM Extension上的HDMI端口：

- 对于HDMI输出设备，使用标准HDMI电缆
- 对于VGA输出设备，使用VGA转HDMI转换器电缆。
    - *注意*：确保转换器通过其USB连接器供电以正常运行。
- 对于不同的视频信号类型，使用其他适当的适配器

## 测试连接

1. 开启电源并启动uConsole
2. 运行Openterface QT app
3. 测试HDMI、音频和USB HID功能以确认正常运行
