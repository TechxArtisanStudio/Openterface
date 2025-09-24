---
title: "功能与规格"
description: "Openterface KVM Extension for uConsole 的完整概述：强大功能包括直接 HDMI 输入、USB HID 控制、完美外形尺寸，以及详细技术规格。关于这个便携式 KVM 解决方案您需要了解的一切。"
keywords: "KVM扩展功能, uConsole KVM, HDMI KVM, USB HID控制, 便携式KVM, headless控制, 4G LTE替换, 技术规格, uConsole扩展"
---

# **功能与规格** | Openterface KVM Extension for uConsole

![PCB-front](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:320px"}
![PCB-Back](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:320px"}

## 核心功能

- **直接 HDMI + USB HID**：利用 uConsole 的内置屏幕和控件，具有直接 HDMI 输入和 USB HID 模拟。
- **即插即用**：即时控制，无需软件安装或在目标设备上留下痕迹。
- **低延迟**：针对 BIOS 级故障排除和实时交互进行了优化。
- **便携式**：一体化移动工具——无需额外的显示器、键盘或网络设置。
- **无网络**：通过 HDMI 捕获和 HID 输入实现稳定的 headless 控制，无需网络。
- **文本传输**：通过模拟按键快速传输文本——非常适合用户名、密码和代码片段。支持完整 ASCII，包括符号和标点符号。[查看我们的应用](/app)了解详情。
- **开源**：基于 [Openterface KVM QT](https://github.com/techxArtisanStudio/openterface_qt) 构建，拥有活跃的社区支持。

## 技术规格

### 物理尺寸

- **尺寸：** 37 × 77 mm（匹配 4G/LTE 模块）
- **厚度：** 1.0 mm（比原始 4G/LTE 模块的 1.2 mm 更薄）
- **材料：** 带弹簧接触器的高质量 PCB

### 完整键盘和鼠标模拟

- **USB HID：** 绝对和相对鼠标定位，完整键盘支持，多媒体键。
- **连接：** 通过扩展板的 Type-C 母端口 USB 连接到目标设备。

### 视频和音频

- **输入：** 通过 HDMI 最高支持 4K (3840×2160) @ 30Hz
- **输出：** 全高清 (1920×1080) @ 30Hz，延迟低于 140ms
- **显示器：** 使用 uConsole 的内置屏幕
- **压缩：** 支持 YUV 和 MJPEG
- **兼容性：** VGA、DVI、Micro HDMI（通过适配器）
- **音频：** HDMI 嵌入式音频直通

### 可切换 USB 2.0 端口

- **共享端口**：使用主机应用轻松在 uConsole 和目标设备（如闪存驱动器）之间切换 USB 访问。
- **USB 速度：** 12Mbps 全速传输

### 连接和电源

- **电源：** 直接从 uConsole 的扩展槽获取电源（无需外部电源）
- **目标兼容性：** Windows、macOS、Linux、Android、iOS
- **目标软件：** 无需安装
