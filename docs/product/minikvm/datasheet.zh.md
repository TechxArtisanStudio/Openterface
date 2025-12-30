---
title: "Openterface Mini-KVM 产品手册 | 技术规格与产品详情"
description: "Openterface Mini-KVM 的完整技术规格书。查看此 KVM-over-USB 解决方案的规格、尺寸、视频/音频功能、电源需求、配件和连接选项。"
keywords: "Mini-KVM 产品手册, Mini-KVM 规格, KVM over USB 技术规格, Mini-KVM 尺寸, Mini-KVM 配件, HDMI KVM 规格, USB KVM 技术详情, 无头电脑控制规格, KVM 开关规格, 服务器管理工具"
---

# Openterface Mini-KVM 产品手册

## 概述

Openterface™ Mini-KVM 是一款功能丰富、生产级的开源设备，由社区驱动开发。它提供了一种轻量且快速的 KVM-over-USB 解决方案，使您可以通过简单的 USB 和 HDMI 连接，直接从自己的笔记本电脑或台式机（称为 Host 计算机）控制无头计算机（称为 Target 计算机）。这种紧凑的方法消除了对额外键盘、鼠标、显示器或任何网络配置的需求，简化了您的设置并提高了效率。

## 规格

### 一般信息

| 参数 | 特性 |
|-----------|----------------|
| 产品名称 | Openterface Mini-KVM |
| 制造商 | TechxArtisan Limited |

### 产品型号

#### Mini-KVM 基础版 (392-OP-MINIKVM-BASIC)

**内容：**

- Openterface Mini-KVM
- 快速入门指南

#### Mini-KVM 工具包 (392-OPMINIKVMTOOLKIT)

**内容：**

- Openterface Mini-KVM
- 快速入门指南
- 工具包袋（尺寸：165 x 110 x 50mm）
- 延伸针帽
- HDMI 公对公线缆（长度：0.3m）
- Type-C 公对 USB-A 公线缆（长度：0.3m）带 USB-A 母对 Type-C 公适配器
- Type-C 公对公线缆（长度：1.5m）带 USB-C 母对 USB-A 公适配器

### 电源

| 参数 | 特性 |
|-----------|----------------|
| 连接类型 | USB-C 供电，无需外部电源。 |

### 视频

| 参数 | 特性 |
|-----------|----------------|
| 最大视频输入 | 通过 HDMI 支持高达 3840x2160@30Hz<br>(注：使用适配器时，还可支持 VGA、Micro HDMI、DVI 等其他视频输入源) |
| 支持的视频分辨率 | 最高支持 1920x1080@30Hz |
| 视频压缩方法 | YUV、MJPEG |
| 延迟 | 低于 140 毫秒 |

### 音频

| 参数 | 特性 |
|-----------|----------------|
| 音频捕获模式 | HDMI 嵌入式音频 |

### 环境

| 参数 | 特性 |
|-----------|----------------|
| 工作温度 | 0°C 至 40°C |
| 存储温度 | -10°C 至 50°C |
| 湿度 | 80% RH |

### 尺寸和重量

| 参数 | 特性 |
|-----------|----------------|
| 长 x 宽 x 高 | 61 x 13.5 x 53 毫米 |
| 重量 | 48 克 |

## 工具包配件

| 物品 | 型号编号 | 描述 |
|------|--------------|-------------|
| HDMI 公对公线缆 | OP-03-CABLE30-HDMI | 长度：0.3m / ~12"<br>颜色：黑色<br>用途：高清 HDMI 视频传输 |
| Type-C 对 USB-A 线缆带适配器 | OP-04-CABLE30-C2A | 长度：0.3m / ~12"<br>颜色：黑色<br>适配器：USB-A 母对 Type-C 公<br>用途：数据传输 / KVM 控制 |
| 尼龙 Type-C 线缆带适配器 | OP-05-CABLE150-C2C | 长度：1.5m / 4' 11"<br>颜色：橙色<br>适配器：USB-C 对 USB-A<br>数据传输速度：最高 10Gbps<br>充电功率：240W |

## 连接

### 接口 / 连接性

1. **USB-C 端口（母）** ⓵  
   作为 USB 设备端口，通过内置的 USB 集线器连接到 Host 计算机进行数据传输

2. **USB-C 端口（母）** ②  
   作为 USB 设备端口，通过内置的 USB 集线器连接到 Host 计算机以模拟键盘和鼠标 HID 输出

3. **HDMI 输入端口（母）** ③  
   来自 Target 计算机的 HDMI 源输入

4. **可切换 USB-A 2.0 端口（母）** ④  
   作为 USB 主机端口，由 Host 计算机或 Target 计算机在任一时间使用，但不能同时使用

5. **切换开关** ⑤  
   用于在 Host 计算机和 Target 计算机之间切换 USB-A 2.0 端口的连接

6. **扩展针脚** ⑥  
   如需更多信息，请查看开发人员使用的扩展针脚说明。

## 应用场景

Openterface Mini-KVM 是各种用户和场景的理想伴侣：

- IT 专业人员排查服务器问题
- 技术人员维护 ATM、VLT 和自助终端机
- 开发者管理边缘计算设备
- 技术爱好者尝试单板计算机
- 需要网络隔离环境下进行安全本地操作的专业人士，如管理加密货币资产者
- 需要频繁在个人电脑和工作电脑之间集成工作的任何人。

## Host 计算机软件

要在 macOS、Windows、Linux 或 Android 上使用此设备，请从相关应用平台安装我们的可用应用程序，或通过 GitHub 仓库进行源代码构建。

## 开源与合规性

Openterface 应用程序采用 AGPL-3.0 许可证，由 TechxArtisan 持续开发。该设备已获得 OSHWA 认证（UID CN000015），确保 GitHub 上的所有原理图和源代码均可公开访问：[Openterface_Mini-KVM_Hardware](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware)。

## 保持更新

访问 [openterface.com](https://openterface.com)，加入我们的 Discord 社区，以获取最新信息、获得支持并与其他用户协作。