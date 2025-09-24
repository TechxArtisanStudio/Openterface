---
title: "软件设置"
description: "Openterface KVM Extension for uConsole 的完整软件设置指南。学习如何在您的 uConsole 上安装和配置 Openterface App，以实现无缝 KVM 功能。"
keywords: "Openterface应用安装, uConsole软件设置, KVM应用设置, uConsole应用配置, 软件安装指南"
---

# **软件设置** | Openterface KVM Extension for uConsole

## 安装概述

Openterface App 使您的 uConsole 能够作为 KVM 接口运行，允许您通过内置屏幕、键盘和轨迹球控制目标设备。

!!! note "要求"
    - **uConsole**：需要安装 Openterface App
    - **目标设备**：无需应用 - 支持 Windows、macOS、Linux、Android、iOS
    - **视频**：使用标准 HDMI 电缆。使用标准 HDMI 电缆。通过供电的 HDMI 转换器，它还支持其他格式，如 **VGA**、**DP** 等。*提示：确保转换器正确供电；否则，您可能会遇到黑屏。*

## 安装方法

### **选项 1：Flatpak 安装**

按照我们的 [Flatpak 安装指南](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) 进行详细的设置步骤。

### **选项 2：社区仓库（推荐）**

如果您更喜欢 Rex 维护的社区构建：

1. **添加仓库**：
```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. **安装包**：
```bash
sudo apt update
sudo apt install openterfaceqt
```

!!! warning "仓库说明"
    这些命令需要 sudo。仓库针对 arm64 Bookworm 包；安装前请验证与您设备的兼容性。

## 使用说明

### **启动 KVM 会话**
1. 在您的 uConsole 上启动 Openterface App
2. 应用将自动检测 KVM Extension 板
3. 通过 HDMI 连接您的目标设备
4. 使用 uConsole 的内置键盘和轨迹球控制目标设备

### **控制功能**
- **键盘**：完整键盘模拟，包括多媒体键
- **鼠标**：绝对和相对鼠标定位
- **音频**：HDMI 音频直通到 uConsole 扬声器

### **高级功能**
- **文本传输**：通过模拟按键快速传输文本—非常适合用户名、密码和代码片段
- **可切换 USB**：使用主机应用轻松在 uConsole 和目标设备之间切换 USB 访问
