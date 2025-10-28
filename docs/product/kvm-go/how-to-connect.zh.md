---
title: "如何连接"
description: "设置 Openterface KVM-Go 的分步指南。了解如何使用内置视频接口连接主机和目标设备，体验超简单的直接插入式连接。"
keywords: "KVM-Go 设置, 超紧凑 KVM 设置, 内置 HDMI 连接, KVM 安装指南, 钥匙扣 KVM 设置, USB KVM 连接, 无显示器设置, 便携式 KVM 设置"
---

# **如何连接** | 设置指南 | Openterface KVM-Go

## **连接概述**

![KVM-Go 连接概述](https://assets.openterface.com/images/kvm-go/step-0-overview.webp){:style="max-height:360px"}

上图显示了 [**KVM-Go**](/product/kvm-go)、主机和目标设备之间的所有连接。

- **主机**：需要安装 [Openterface 应用程序](/app)。  
- **目标设备**：无需软件和预配置。
- **视频**：内置接口直接插入目标设备，因此您无需携带或管理额外的视频线缆。

## **连接所需物品**

![KVM-Go 全部组件](https://assets.openterface.com/images/kvm-go/step-0-all-parts.webp){:style="max-height:360px"}

要设置您的 **KVM-Go**，您需要以下组件：

- **KVM-Go (HDMI / DP / VGA)** — 连接到**目标设备**（用于视频采集）  
- **黑色短 USB-C 线缆** — 连接到**目标设备**（用于键盘和鼠标模拟）
- **橙色长 USB-C 线缆** — 连接到**主机**（运行 [Openterface 应用程序](/app)）

!!! note "线缆长度声明"
    **官方 KVM-Go 套装**中包含的确切线缆长度**尚未最终确定**，可能与此处显示的略有不同。  
    本指南中演示的线缆来自*经典 Mini-KVM 工具包*，仅供说明之用。

!!! warning "使用您自己的线缆"
    如果您选择使用自己的线缆，请确保它们是**高质量、支持数据传输的 USB 线缆**。劣质或仅充电线缆可能导致：
    
    - 黑屏问题
    - 键盘或鼠标输入无响应
    - 间歇性连接中断
    - 显示输出闪烁或不稳定

## **分步设置**

### **步骤 1 — 将 USB 线缆连接到 KVM-Go**
![插入 USB 线缆](https://assets.openterface.com/images/kvm-go/step-1-plugged.webp){:style="max-height:360px"}

- **黑色 USB-C 线缆** → 插入 KVM-Go 外壳上标有 ![目标图标](https://assets.openterface.com/images/shell-icons/target-computer.svg#only-light){:style="max-height:20px"} ![目标图标](https://assets.openterface.com/images/shell-icons/target-computer_1.svg#only-dark){:style="max-height:20px"} **Target** 的端口。  
- **橙色 USB-C 线缆** → 插入标有 ![主机图标](https://assets.openterface.com/images/shell-icons/host-computer.svg#only-light){:style="max-height:20px"} ![主机图标](https://assets.openterface.com/images/shell-icons/host-computer_1.svg#only-dark){:style="max-height:20px"} **Host** 的端口。

!!! warning
    两个 USB-C 端口在物理上完全相同。  
    请始终**仔细检查外壳表面上的标签**以避免混淆。

### **步骤 2 — 将视频连接到目标设备**
![插入 HDMI 接口](https://assets.openterface.com/images/kvm-go/step-3-hdmi-plugged.webp){:style="max-height:360px"}

将**内置公头视频接口**直接插入目标设备的视频输出端口。

### **步骤 3 — 连接目标 USB 端口**
将**黑色 USB 线缆**连接到目标设备以进行 HID 控制。

- **选项 A：** 直接插入 USB-A 端口  
  ![目标 USB-A](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-b.webp){:style="max-height:360px"}

- **选项 B：** 使用 USB-C 转接器  
  ![目标 USB-C](https://assets.openterface.com/images/kvm-go/step-4-target-plugged-a.webp){:style="max-height:360px"}

!!! note "USB-C 连接检查"
    某些 USB-C 端口可能无法提供稳固的连接。如果您遇到间歇性键盘/鼠标控制问题，请轻轻晃动转接器连接以确保其正确就位并接触良好。


### **步骤 4 — 连接主机 USB 端口**
将**橙色 USB 线缆**连接到主机。

- 直接连接到 USB-C 端口**或**通过 USB-C 转 USB-A 转接器。  
  ![插入主机 USB](https://assets.openterface.com/images/kvm-go/step-5-plug-in-host-computer-1.webp){:style="max-height:360px"}

