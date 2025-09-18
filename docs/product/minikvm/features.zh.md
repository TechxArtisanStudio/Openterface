---
title: "功能与规格"
description: "Openterface Mini-KVM 完整概览：强大功能包括 BIOS 级访问、4K 视频支持、跨平台兼容性、USB 共享以及详细技术规格。关于这款无头计算机控制解决方案，您需要了解的一切。"
keywords: "Mini-KVM 功能, KVM 规格, BIOS 访问, 无头控制, 4K KVM, USB 共享, 跨平台 KVM, 文本传输, 即插即用 KVM, 开源 KVM, 技术规格"
---

# **功能与规格** | Openterface Mini-KVM

<iframe 
  width="560" 
  height="315" 
  src="https://www.youtube.com/embed/r3HNUflWGOY?si=84Ek6F9ocHmmGTqW" 
  title="YouTube video player" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
  referrerpolicy="strict-origin-when-cross-origin" 
  allowfullscreen>
</iframe>

## 核心功能

### **BIOS 级访问**

直接访问目标设备 BIOS、固件和启动管理，无需网络依赖。

### **网络独立性**

使用 HDMI 视频捕获和模拟键盘/鼠标（HID）输入实现稳定的无头控制。无需网络连接。

### **高性能视频**

- **输入**：通过 HDMI 最高支持 4K (3840×2160) @ 30Hz
- **输出**：全高清 (1920×1080) @ 30Hz，延迟低于 140ms
- **压缩**：支持 YUV 和 MJPEG
- **兼容性**：通过适配器支持 VGA、DVI、Micro HDMI

### **可切换 USB 端口**

在主机和目标设备之间切换 USB 访问，实现无缝 USB 驱动器共享。在[可切换 USB 端口](../usb-switch)页面了解更多。

### **跨平台支持**

[主机应用](/app)兼容 macOS、Windows、Linux 和 Android，实现通用集成。

### **文本传输**

通过模拟按键轻松传输文本——非常适合用户名、密码和代码片段。支持 ASCII 字符，包括符号和标点。

!!! warning "文本传输限制" - **无剪贴板集成**：仅模拟输入，不支持图像或文档传输 - **仅 ASCII**：仅限于 ASCII 字符（不支持中文、日文、韩文） - **长度考虑**：最适合短文本；大块文本可能导致性能问题

### **即插即用便利性**

目标设备无需安装软件。连接后立即开始控制，不留任何软件痕迹。

### **音频集成**

HDMI 嵌入式音频直通，提供完整的多媒体体验。

### **扩展引脚**

[扩展引脚](../extension-pins)支持高级开发和特定需求的自定义。

### **开源**

[完全开源](/compliance)的硬件和软件，确保透明度和[社区创新](/discord)。

## 技术规格

### **物理尺寸**

- **尺寸**：61 × 53 × 13.5 mm (2.40 × 2.09 × 0.53 英寸)
- **重量**：~48g
- **材质**：铝合金、PLA 外壳

### **连接与电源**

- **电源**：USB-C 供电（无需外部电源）
- **USB 速度**：12Mbps 全速传输
- **主机兼容性**：Windows、macOS、Linux、Android
- **目标**：无需安装软件

### **视频与音频**

- **最大输入**：3840×2160@30Hz (HDMI)
- **最大输出**：1920×1080@30Hz
- **延迟**：低于 140ms
- **音频**：HDMI 嵌入式音频直通

### **输入功能**

- 完整键盘和鼠标模拟（绝对和相对）
- 多媒体按键支持
- 自定义 HID 功能
- 计算机唤醒功能

### **环境条件**

- **工作温度**：0°C 至 40°C
- **存储温度**：-10°C 至 50°C
- **湿度**：80% RH

## 产品型号

- **基础版**：OP-MINIKVM-BASIC
- **工具包版**：OP-MINIKVM-TOOLKIT

## 文档下载

- **[快速入门指南](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/minikvm_quick_start_guide_20240928.pdf)** (PDF)
- **[数据手册（英文）](https://raw.githubusercontent.com/TechxArtisanStudio/Openterface/main/product-printed-materials/Openterface-Mini-KVM-Basic-and-Toolkit-Datasheet-Eng-20250313.pdf)** (PDF)

![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front.svg#only-light){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back.svg#only-light){:style="max-height:260px"}
![lig-front](https://assets.openterface.com/images/product/minikvm-v1-9-front_1.svg#only-dark){:style="max-height:260px"}
![lig-back](https://assets.openterface.com/images/product/minikvm-v1-9-back_1.svg#only-dark){:style="max-height:260px"}
