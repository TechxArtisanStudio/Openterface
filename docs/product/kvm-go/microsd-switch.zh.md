---
title: "MicroSD 卡切换指南"
description: "了解如何使用 Openterface KVM-Go 中的双硬件软件 MicroSD 切换系统。了解四种操作状态、LED 指示灯、安全指南和文件传输功能。"
keywords: "MicroSD 切换, KVM 切换, 硬件切换, 软件切换, MicroSD 卡控制, KVM over USB, 文件传输, USB 设备管理, 计算机外设, MicroSD 电源管理, LED 指示灯"
---

# **MicroSD 卡切换指南** | Openterface KVM-Go

**Openterface KVM-Go** 包含一个 MicroSD 卡插槽，可在主机和目标设备之间共享，但不能同时使用。

此设计允许您在设备之间快速切换进行**文件传输**，无需物理移除卡，使您的工作流程更快、更高效。它也可以作为您的**常规 MicroSD 读卡器**使用。

## **安装 MicroSD 卡**

![kvm-go-install-sd](https://assets.openterface.com/images/kvm-go/install-sd.webp){:style="max-height:260px;width:auto"}

!!! note "正确安装 MicroSD 卡"
    牢固插入 MicroSD 卡，直到感觉到**咔嚓声**，表明它已安全就位并锁定。

## **控制方法**

KVM-Go 提供两种在主机和目标之间切换 MicroSD 卡的方式：

- **硬件按钮** — 设备上的物理按钮，用于手动控制。  
- **软件切换** — 主机应用程序中的切换按钮，可即时切换。


## **切换按钮和 LED 指示灯** 

![kvm-go-led-indicator](https://assets.openterface.com/images/kvm-go/led-indicator.webp){:style="max-height:260px;width:auto"}

**双色 LED 指示灯**显示当前 MicroSD 连接状态*（注意：开发中/可能变更）*：

- **🔵 蓝色 LED 亮起** — MicroSD 卡已挂载到**目标设备**  
- **🟢 绿色 LED 亮起** — MicroSD 卡已挂载到**主机**  
- **LED 熄灭** — 未插入 MicroSD 卡或设备已关闭电源  
- **LED 闪烁** — 正在进行数据传输（读/写活动）

!!! note "自动挂载功能（实验性）"
    默认情况下，当设备首次上电时，MicroSD 卡会挂载到**主机**。  
    即将推出的实验性功能将允许**自动挂载**到首先连接的一侧（主机或目标），使体验更加无缝。

---

## 相关

- [KVM-GO 上的 microSD EXPRESS：兼容性测试与实际传输速度](updates/20260203-kvm-go-microsd-express.zh.md) — SanDisk microSD EXPRESS 卡兼容性测试与实际传输速度

