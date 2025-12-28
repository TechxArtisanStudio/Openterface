---
title: Openterface KVM-Go 系列常见问题
description: 关于 KVM-Go 系列的常见问题，涵盖功能、兼容性和预发布信息。
keywords: KVM-Go, Openterface, 超紧凑型 KVM, 内置 HDMI, 钥匙扣 KVM, 开源, 预发布, 视频采集, USB, 兼容性, MicroSD
---

# Openterface KVM-Go 系列常见问题

欢迎访问我们下一代 **Openterface KVM-Go 系列**的常见问题页面。  
如果您没有找到所需的答案，**请发送邮件至 [info@openterface.com](mailto:info@openterface.com)** 或**加入我们的社区** [Discord](/discord) 或 [Reddit](/reddit)。

⚠️ **注意**：KVM-Go 目前处于预发布开发阶段。随着我们完善产品，功能、规格和设计可能会有所变化。

---

## :material-clipboard-list: 快速导航

- [Openterface KVM-Go 系列常见问题](#openterface-kvm-go-系列常见问题)
  - [:material-clipboard-list: 快速导航](#material-clipboard-list-快速导航)
  - [常规问题](#常规问题)
  - [MicroSD 和文件传输](#microsd-和文件传输)
  - [技术问题](#技术问题)
  - [预发布问题](#预发布问题)

---

## 常规问题

**:material-chat-question:{ .faq } 什么是 KVM-Go？**

KVM-Go 是我们下一代超紧凑型 KVM-over-USB 解决方案。它只有钥匙扣大小，内置视频连接器（HDMI、DisplayPort 或 VGA），无需单独的线缆。

**:material-chat-question:{ .faq } 它有多小？**

超紧凑尺寸：**18 × 18 × 55 mm**（0.71 × 0.71 × 2.17 英寸）——小到可以挂在钥匙扣上。重量约为 **25克（0.9 盎司）**。

**:material-chat-question:{ .faq } 有哪些型号可选？**

- **KVM-Go HDMI Male** — 适用于现代设备的直接 HDMI 连接
- **KVM-Go DisplayPort Male** — 高性能 DisplayPort 支持  
- **KVM-Go VGA Male** — 兼容旧系统（即将推出）

**:material-chat-question:{ .faq } 与 Mini-KVM 相比如何？**

主要改进：

- **尺寸**：18×18×55mm vs 61×53×13.5mm（更小）
- **重量**：25g vs 48g（更轻）
- **视频**：4K@60Hz vs 1080p@30Hz（性能更好）
- **USB**：USB 3.0 vs USB 2.0（更快）
- **设置**：内置连接器 vs 单独线缆（更简单）

**:material-chat-question:{ .faq } 启动速度有多快？**

硬件启动时间不到 1 秒，可以立即进行故障排除，不会延迟或干扰您的工作流程。

---

## MicroSD 和文件传输

**:material-chat-question:{ .faq } 能传输文件吗？**

可以——通过**可切换的 MicroSD 插槽**，可在主机和目标设备之间共享，无需物理取出卡即可快速传输文件。

**:material-chat-question:{ .faq } 如何切换 MicroSD 方向？**

两种便捷方法：
1. **硬件按钮** – 设备上的物理按钮，用于手动控制
2. **软件开关** – 主机应用程序中的切换按钮，用于即时切换

**:material-chat-question:{ .faq } LED 指示灯是什么意思？**

**双色 LED 指示灯**显示当前的 MicroSD 连接状态：

- **🔵 蓝色 LED 亮起** – MicroSD 卡已挂载到**目标设备**  
- **🟢 绿色 LED 亮起** – MicroSD 卡已挂载到**主机计算机**  
- **LED 熄灭** – 未插入 MicroSD 卡或设备已关闭电源  
- **LED 闪烁** – 正在进行数据传输（读/写活动）

**:material-chat-question:{ .faq } 如何正确安装 MicroSD 卡？**

牢固插入 MicroSD 卡，直到您听到**咔哒**声，表示它已安全就位并锁定。这种触觉反馈确认了正确的连接。

---

## 技术问题

**:material-chat-question:{ .faq } 视频性能如何？**

- **输入**：最高 4096×2160 @ 60 Hz (YUV420)、4096×2160 @ 30 Hz (YUV444)
- **输出**：4096×2160 @ 60 Hz (MJPEG)、3840×2160 @ 30 Hz (YUV420)
- **默认**：1080p@60Hz，以获得最佳稳定性和性能
- **延迟**：低于 140ms，实现流畅控制

**:material-chat-question:{ .faq } 4K 模式有限制吗？**

有的——4K 模式是实验性的，会产生额外的热量。在长时间 4K 运行期间，设备表面可能会变得相当热。为了获得最佳稳定性和性能，建议使用默认的 1080p@60Hz 模式。

**:material-chat-question:{ .faq } 开源吗？**

是的——已通过 [OSHWA](https://certification.oshwa.org/cn000015.html) 认证。硬件和软件都在 [GitHub](https://github.com/TechxArtisanStudio/Openterface_KVM-GO_Hardware) 上。

**:material-chat-question:{ .faq } BIOS 访问**

直接 USB 连接允许完全的 BIOS 级别控制，不同于仅远程工具（VNC、TeamViewer）。

**:material-chat-question:{ .faq } 跨平台支持？**

[主机应用程序](/app)兼容 macOS、Windows、Linux、Android 和 Chrome 网页应用程序，实现通用集成。

**:material-chat-question:{ .faq } 能在 iPad 上使用吗？**

可以——iPadOS 支持即将通过 Apple App Store 上的原生应用程序推出。这得益于 KVM-GO 内置的 Bluetooth 功能，使其成为少数能在 iPad 上原生运行的 KVM 之一。

**:material-chat-question:{ .faq } 有基于网页的应用程序吗？**

有——访问 [Openterface Viewer](https://openterface-viewer.pages.dev/) 获取无需安装的基于浏览器的应用程序（适用于 Chrome、Edge、Safari）。非常适合快速访问或无法在主机计算机上安装软件的情况。感谢我们出色的社区，特别是启动此项目的 [@kashalls](https://github.com/kashalls)。

**:material-chat-question:{ .faq } 应该选择哪种视频连接器？**

- **HDMI**：最适合现代设备、服务器、工作站
- **DisplayPort**：高分辨率显示器、专业设置
- **VGA**：旧系统、老服务器（即将推出）

---

## 预发布问题

**:material-chat-question:{ .faq } KVM-Go 何时上市？**

KVM-Go 目前正在进行小批量生产测试，并已向 beta 测试人员发送设备进行实际验证。

**生产时间表**：

- **2025 年 11 月**：活动启动
- **2025 年 12 月**：完成生产设置和组件采购
- **2026 年 1-3 月**：批量生产和质量控制
- **2026 年 4 月**：首批发货给支持者

加入我们的[等候名单]({{ config.extra.kvmgo_purchase_link }})，随时了解进展并获得早期访问权限。

**:material-chat-question:{ .faq } 价格是多少？**

价格将在正式发布活动期间公布。早期支持者将获得特别折扣和优先访问权。

**:material-chat-question:{ .faq } 我可以成为 beta 测试人员吗？**

可以！如果您有硬件和软件测试经验，欢迎在[此处](https://forms.gle/yaS1F5E5MSo8DWNZ6)申请我们的 beta 测试计划。

**:material-chat-question:{ .faq } 规格最终确定了吗？**

还没有，随着我们在开发过程中完善产品，功能、规格和设计可能会有所变化。

