---
title: Openterface Mini-KVM 常见问题
description: 关于 Mini-KVM 的常见问题，涵盖功能、兼容性、故障排除和未来计划。
keywords: Mini-KVM, Openterface, KVM 切换器, 开源, 故障排除, 视频捕获, USB, 兼容性
---

# Openterface Mini-KVM 常见问题

欢迎来到我们旗舰产品 **Openterface Mini-KVM** 的常见问题页面。  
如果您找不到需要的信息，请**发送邮件至 [info@openterface.com](mailto:info@openterface.com)** 或**加入我们的社区** [Discord](/discord) 或 [Reddit](/reddit)。

⚠️ _常见问题可能已过时 — 如果您发现需要更新的内容，请告知我们。_

---

## :material-clipboard-list: 快速导航

-   [USB 端口和文件传输](#usb-端口和文件传输)
-   [技术](#技术)
-   [控制](#控制)
-   [视频](#视频)
-   [故障排除](#故障排除)
-   [更多](#更多)

---

## USB 端口和文件传输

**:material-chat-question:{ .faq } 可以传输文件吗？**

可以 — 通过主机和目标设备之间共享的可切换 USB-A 端口。

**:material-chat-question:{ .faq } 我可以通过软件切换 USB 端口吗？**

可以，在硬件版本 **v1.9+** 上。

**:material-chat-question:{ .faq } 为什么使用 USB 2.0 而不是 3.0？**

USB 2.0 足以支持 1080p@30Hz 视频 + HID + 标准速度文件传输，同时保持紧凑、更凉爽和更经济实惠。  
USB 3.0 可能会出现在未来的专业型号中。

---

## 技术

**:material-chat-question:{ .faq } 开源吗？**

是的 — 已通过 [OSHWA](https://certification.oshwa.org/cn000015.html) 认证。硬件和软件都在 [GitHub](/contributing/) 上。

**:material-chat-question:{ .faq } BIOS 访问**

直接 USB 连接允许完整的 BIOS 级别控制，与仅远程工具（VNC、TeamViewer）不同。  
较旧的机器可能在识别我们的 USB 集线器时遇到 BIOS 问题 — 请报告此类情况。

**:material-chat-question:{ .faq } 视频/数据传输**

视频通过 HDMI 捕获并通过 USB 2.0 发送。  
可切换的 USB 端口允许您共享驱动器或其他设备。

**:material-chat-question:{ .faq } 电源处理**

Mini-KVM 可以从**任一侧**（主机或目标）获取电源。**较短电缆**的一侧通常成为主要电源。  
对于低功耗目标（例如 Raspberry Pi），请使用专用电源而不是通过 Mini-KVM 反向供电。

**:material-chat-question:{ .faq } 电缆长度限制**

-   保持**橙色主机 USB-C 电缆 ≤1.5m**。
-   对于更长的电缆，通过以下方式注入电源：
    -   USB-A 公对公电缆
    -   [扩展引脚](/product/minikvm/extension-pins/)
    -   USB-C Y 分线器
-   同样的规则适用于**黑色目标电缆**。

---

## 控制

**:material-chat-question:{ .faq } 无线或以太网版本？**

没有内置。使用无头计算机（例如 Raspberry Pi）+ 远程桌面进行远程控制。

**:material-chat-question:{ .faq } PS/2 兼容性？**

不支持 — PS/2 支持可能在未来的版本中探索。

**:material-chat-question:{ .faq } 一台计算机上使用多个 Mini-KVM？**

可以，QT 应用程序（Windows/Linux）中的实验性功能。

**:material-chat-question:{ .faq } 电源开关控制？**

不直接支持，但[扩展引脚](/product/minikvm/extension-pins/)允许未来的 ATX 控制模块。

---

## 视频

**:material-chat-question:{ .faq } 延迟和分辨率**

-   以 **1080p@30Hz** 捕获
-   延迟低于 **140ms** → 流畅控制

**:material-chat-question:{ .faq } 输入与捕获分辨率**

-   接受高达 **4K@30Hz** 的输入
-   以 **1080p** 捕获，更高的输入会被降采样（可能看起来稍微模糊）。
-   最佳实践：**将目标设置为 1080p**。

**:material-chat-question:{ .faq } 游戏适用性**

不适合 AAA 游戏。对于 Minecraft 或模拟器等轻量游戏效果良好。

**:material-chat-question:{ .faq } 通过互联网远程控制**

没有内置，但可以将 Mini-KVM 与主机上的远程桌面软件配对。

**:material-chat-question:{ .faq } 其他视频格式**

使用适配器支持 VGA、DVI、DisplayPort 等。

---

## 故障排除

**:material-chat-question:{ .faq } USB 集线器问题**

使用**有源集线器**以避免电压下降导致不稳定。

**:material-chat-question:{ .faq } 应用程序显示无视频或控制无响应**

断开所有电缆，等待，重新连接。  
如果问题未解决，检查固件或更新主机应用程序。

**:material-chat-question:{ .faq } 奇怪的分辨率如 43184x24228@44Hz**

捕获固件可能已恢复到出厂设置。  
通过 [GitHub 发布](https://github.com/TechxArtisanStudio/Openterface_QT/releases) 重新刷写固件。

**:material-chat-question:{ .faq } 重新刷写但仍然损坏？**

-   验证正确的 USB 枚举（`USB Tree Viewer` 或 `lsusb -v`）
-   确认最新的主机应用程序
-   如果仍然失败，请联系支持进行诊断/更换。
