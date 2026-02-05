---
title: Openterface KeyMod 系列常见问题
description: 关于 KeyMod 系列的常见问题，涵盖功能、兼容性、平台和预发布信息。
keywords: KeyMod, Openterface, HID 模拟器, 蓝牙键盘, 手机键盘, 开源, 预发布, Android, iPadOS
---

# Openterface KeyMod 常见问题

欢迎访问 **Openterface KeyMod** 的常见问题页面。  
如果您没有找到所需的答案，**请发送邮件至 [info@openterface.com](mailto:info@openterface.com)** 或**加入我们的社区** [Discord](/discord) 或 [Reddit](/reddit)。

⚠️ **注意**：KeyMod 目前处于预发布开发阶段。随着我们完善产品，功能、规格和设计可能会有所变化。

---

## :material-clipboard-list: 快速导航

- [Openterface KeyMod 常见问题](#openterface-keymod-常见问题)
  - [:material-clipboard-list: 快速导航](#material-clipboard-list-快速导航)
  - [常规问题](#常规问题)
  - [连接](#连接)
  - [功能](#功能)
  - [预发布](#预发布)

---

## 常规问题

**:material-chat-question:{ .faq } 什么是 KeyMod？**

KeyMod 是一款紧凑的 USB + 蓝牙 HID（键盘和鼠标）模拟器，可将您的手机变成便携式键盘和触控板。用于控制需要键盘/鼠标输入的设备——如信息亭、智能电视、机顶盒、户外显示屏——无需携带完整键盘。

**:material-chat-question:{ .faq } KeyMod 应用支持哪些平台？**

KeyMod Series 控制器应用主要支持 **Android**、**iOS** 和 **iPadOS**。我们也在更广泛的 Openterface 生态系统中通过 **Windows 和 macOS** 软件扩展桌面控制。

**:material-chat-question:{ .faq } 目标设备需要安装软件吗？**

不需要。KeyMod 模拟标准 USB 键盘和鼠标。目标设备将其识别为即插即用 HID 硬件——无需安装驱动程序或软件。

**:material-chat-question:{ .faq } KeyMod 是开源的吗？**

是的。KeyMod 是开源硬件和开源软件。随着项目的发展，我们将发布电路图、PCB 文件、固件、软件和 BOM。

---

## 连接

**:material-chat-question:{ .faq } USB 还是蓝牙——应该选择哪个？**

- **USB**：更可靠，延迟更低。当您需要最稳定的连接时使用。
- **蓝牙**：无线连接。当您需要更轻便的设置且场景允许无线时使用。

**:material-chat-question:{ .faq } 计划有哪些硬件版本？**

1. **2 合 1 连接器** — 组合 USB A + USB C 插头，广泛兼容
2. **USB C 版本** — 专用于现代设备的 USB C 插头

---

## 功能

**:material-chat-question:{ .faq } 可以创建自定义配置和宏吗？**

可以。开源移动应用支持自定义输入配置、宏、快捷键和工作流快捷方式。您还可以使用数字键盘。

---

## 预发布

**:material-chat-question:{ .faq } KeyMod 何时发布？**

KeyMod 处于预发布开发阶段。在[产品页面](/product/keymod/)订阅以获取发布通知和更新。

**:material-chat-question:{ .faq } KeyMod 与 Mini-KVM 和 KVM-Go 有什么关系？**

KeyMod 使用 Openterface Mini-KVM 的成熟 HID 核心。它采用相同的基于硬件的键盘和鼠标模拟方法，但针对不同的使用场景设计：将您的手机变成便携式键盘/触控板用于本地设备控制，而不是 KVM-over-USB 视频采集。
