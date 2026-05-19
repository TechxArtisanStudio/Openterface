---
draft: false
date: 2026-05-21
title: "KVM-GO 更新：使用 KeyCmd 0.19 通过手机控制目标机器"
description: "通过 USB 或蓝牙配合 KVM-GO 使用 KeyCmd 0.19：支持 KM 基础版与专业版键盘、撰写模式、游戏手柄预设、快捷键中心及演示控制——无需视频采集卡即可进行 HID 输入。"
keywords: "KVM-GO KeyCmd, KeyCmd 0.19, KVM-GO 安卓应用, KVM-over-USB 手机控制, Openterface KeyCmd, 虚拟键盘 KVM, KVM-GO 蓝牙 USB, KM Pro 撰写模式, KVM-GO HDMI DP VGA, Openterface KVM 应用, 便携式 KVM 输入"
author: "Openterface Team | TechxArtisan"
category: "产品更新"
tags: ["KVM-GO", "KeyCmd", "产品更新", "Android", "USB", "蓝牙", "键盘", "游戏手柄", "发布"]
featured: false
social:
  image: "https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp"
  title: "KVM-GO + KeyCmd 0.19 —— 通过手机控制目标机器"
  description: "KeyCmd 0.19 通过 USB 或蓝牙与 KVM-GO 配对，支持键盘、鼠标、游戏手柄、快捷键及撰写功能；同时 Openterface KVM 可在需要时处理视频显示。"
---

# KVM-GO 更新：使用 KeyCmd 0.19 通过手机控制目标机器

大家好，

感谢大家支持 **KVM-GO**，也感谢大家在产品生产和运输期间的耐心等待。我们深知许多朋友仍在等待硬件到手，因此我们希望在您收到货的第一天就能拥有完整的体验。

除了 **Openterface KVM** 应用（可在手机或平板上实现视频显示及完整的 KVM 控制）外，我们一直在优化 **KeyCmd**，这是我们用于键盘、鼠标、游戏手柄及快捷键输入的配套应用。**KeyCmd 0.19** 是我们目前推荐配合 KVM-GO 使用的版本。您可以通过 **USB** 或 **蓝牙** 配对，并直接在旧版本上覆盖安装，您的设置、配置文件和已配对设备都将完整保留。

![手机上的 KeyCmd 键盘配合笔记本电脑上的 KVM-GO 使用](https://assets2.openterface.com/images/kvm-go/kvm-go-keycmd-phone-keyboard-setup.webp){:style="max-width:720px;width:100%;height:auto"}

以下是 KeyCmd 配合 KVM-GO 的功能介绍、不同场景下的模式选择，以及如何在目标机器上最大化发挥其效用。

![KeyCmd 欢迎界面](https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape_1.webp){:style="max-height:320px;width:auto"}

## 模式及使用方法

### 键盘与鼠标（基础版）

当您只需要一个**简洁的全屏键盘**，且不希望被其他元素干扰时，请开启此模式。

**适用场景：** 输入 BIOS 密码、简短的 Shell 命令、数字键盘输入，或者在 KVM-GO 显示屏幕时使用大面积触控板控制鼠标。

**使用方法：**

- 从侧边栏菜单打开 **KM Basic**。
- 根据需要使用屏幕键盘、**数字键盘**（横屏或竖屏）或**触控板**标签页。
- 在**设置**中，您可以选择**粘滞修饰键**（点击以锁定 Shift/Ctrl）或**组合修饰键**（长按并点击组合键）。

**核心优势：** 为按键提供更大的屏幕空间，界面简洁，在仅需输入而非快捷键时操作更迅速。

![KM Basic 全屏键盘](https://assets2.openterface.com/images/keymod/KM-Basic-Keyboard_1.webp){:style="max-height:320px;width:auto"}

![KeyCmd 横屏下的数字键盘](https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape_1.webp){:style="max-height:320px;width:auto"}

### 键盘与鼠标（专业版）

![KM Pro 横屏下的分体键盘](https://assets2.openterface.com/images/keymod/KM-Pro-Keyboard-landscape-split_1.webp){:style="max-height:320px;width:auto"}

![KeyCmd 竖屏下的键盘与触控板](https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait_1.webp){:style="max-height:320px;width:auto"}

此模式适用于配合 KVM-GO 对机器进行**日常管理工作**：支持分体键盘、输入法（IME）、快捷键中心（Shortcut Hub）工具栏以及**撰写（Compose）**编辑器。

**适用场景：** 较长时间的文字输入、宏与快捷键操作、在观察 KVM 画面的同时向主机发送大段文本或脚本。

![撰写模式正在发送脚本](https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait_1.webp){:style="max-height:320px;width:auto"}

如果您经常需要粘贴命令或脚本，非常推荐尝试 **撰写（Compose）** 功能：在手机上编写、检查，然后将其模拟为按键发送给主机。[YouTube 上的演示短片](https://www.youtube.com/watch?v=_rJF-hTF3_E) 展示了完整的操作流程。

**使用方法：**

- 从侧边栏打开 **KM Pro**。
- 像基础版一样使用键盘和触控板，此外顶部的 **快捷键中心（Shortcut Hub）** 分类可让您一键执行在配置文件中设置的动作。
- 打开 **撰写（Compose）** 在手机上起草长文本，核对后点击**发送**（以 HID 按键形式）。长文本发送会显示进度条。如果文本包含非 ASCII 字符，应用会在发送前发出警告，以便您检查主机兼容性（对 macOS 特别有用）。

**核心优势：** 集打字、光标控制、快捷键及类似“粘贴”的工作流于一体，无需为目标机器携带实体键盘。

### 游戏手柄

当您希望在屏幕上使用专为游戏或特定应用优化的**虚拟手柄**布局时，请开启此模式。

**适用场景：** 模拟器、休闲游戏，或在 KVM-GO 处理显示时作为带有摇杆和按钮的紧凑控制面板。

**使用方法：**

- 切换到 **Gamepad** 模式。
- 点击工具栏中的 **Preset** 可**轮换**已保存的布局。**长按 Preset** 可打开完整列表进行**导入/导出**或**添加模块**（摇杆、按钮、触控板）。
- 建议从内置的 **emu-6** 预设开始尝试并自行编辑。您可以在一个布局中添加**多个触控板**和额外的摇杆模块。

**核心优势：** 不受出厂布局限制；您可以按游戏或机器保存布局，并与他人分享预设。

![游戏手柄预设布局](https://assets2.openterface.com/images/keymod/Gamepad-perset-1_1.webp){:style="max-height:320px;width:auto"}

![在我的世界中使用游戏手柄预设](https://assets2.openterface.com/images/keymod/Gamepad-perset-minecraft_1.webp){:style="max-height:320px;width:auto"}

*为《我的世界 (Minecraft)》定制的预设。*

### 快捷键中心 (Shortcut Hub)

这是 KM Pro 内部的**配置文件与快捷键**管理中心：包含分类、详情面板以及您分配到工具栏的快捷键。

**适用场景：** 在保持 KVM-GO 视频连接的同时，执行目标机器上的重复性操作（打开终端、粘贴命令链、切换设置）。

**使用方法：**

- 在 KM Pro 中使用 **Default** 配置文件（或您自己的配置）。
- 使用分类标签页和详情界面管理快捷键。
- 如果您是第一次接触配置文件管理，建议运行 **Shortcut Hub 导览**。

### 演示模式 (Presentation)

一个更简洁的**演示器风格**控制界面，固定为**竖屏**显示，以防止旋转手机时按钮位置发生跳变。

**适用场景：** 切换幻灯片或对目标机器进行简单的演示控制。

![演示模式控制 Google Slides](https://assets2.openterface.com/images/keymod/KeyCmd-Presentation-Google-Slides.webp){:style="max-height:320px;width:auto"}

---

## 语言支持

应用界面现已支持 **11 种语言**。最近新增了：韩语、意大利语、俄语和巴西葡萄牙语。

请前往 **Settings** → **App language** 进行切换。

---

## 获取 KeyCmd 0.19 并连接 KVM-GO

**下载地址：** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

如果您已安装旧版本，直接覆盖安装即可，无需清除数据。

**连接 KVM-GO（视频端口可保持空置）：**

对于 **KVM-GO 的所有三种版本**（HDMI、VGA 和 DP），若仅需 KeyCmd 输入，您无需将**转接头上的视频接口**接入任何设备。HDMI、VGA 或 DP 端口可以保持空置。请根据以下两种方案进行连接。

**方案 A —— 蓝牙连接（目标机器为 KVM-GO 供电）**

1. 将**黑色短 USB 线**插入 KVM-GO 的 **Target** 端口，另一端接入您要控制的机器。仅此连接即可为 KVM-GO **供电**。
2. 在手机上打开 **KeyCmd** 并通过**蓝牙**搜索 KVM-GO。

**方案 B —— USB 连接安卓手机（Host 端口）**

1. 将**橙色长线**从 KVM-GO 的 **Host** 端口连接到您的安卓手机。
2. 打开 **KeyCmd** 并在应用中选择通过 **USB** 连接。

![KVM-GO Target 端口通过黑色短 USB 线连接到笔记本电脑供电](https://assets2.openterface.com/images/kvm-go/kvm-go-target-port-laptop-power.webp){:style="max-height:360px;width:auto"}

如需全屏视频加输入，请使用 **Openterface KVM** 查看目标画面，并使用 **KeyCmd** 进行键盘、鼠标和快捷键操作。当目标机器已有显示器而您只需要输入控制时，仅使用 KeyCmd 即可。

如果您同时拥有两款设备，本应用也支持通过 USB 连接 **Mini-KVM**。

> **当前仍为测试版。** 游戏手柄预设和撰写发送功能在不同主机系统上的表现可能有所不同。如果配合 KVM-GO 使用时出现异常，请带上截图、您的 KVM-GO 版本（HDMI / DP / VGA）以及您的预期效果，通过 **Discord** 联系我们。

> **源代码：** 尚未公开。我们计划在相关项目的众筹里程碑完成后进行开源。如在获取 APK 时需要帮助，请在 Discord 中咨询。

---

## 关于 KeyMod（可选，独立于 KVM-GO）

我们同时也在开发 **[KeyMod](https://openterface.com/product/keymod/)**，这是一个专为 KeyCmd 应用设计的独立 USB 和蓝牙 HID 适配器。KVM-GO 的支持者无需购买 KeyMod 即可实现上述工作流；目前我们推荐您使用 KeyCmd 配合 KVM-GO。

如果您对非 KVM 场景下的独立适配器感兴趣，可以关注 [Crowd Supply 上的 KeyMod 众筹项目](https://www.crowdsupply.com/techxartisan/openterface-keymod)。该项目与 KVM-GO 的发货是分开进行的。

---

## 我们期待您的反馈

如果您有几分钟时间，请安装 **KeyCmd 0.19**，连接到您的 KVM-GO（或 Mini-KVM），并告诉我们哪些地方用起来还不顺手。来自机房应急和家庭实验室（homelab）等实际场景的反馈将直接推动我们下一个版本的更新。

帮助 KVM-GO 项目的实际方式：

- 在 Discord 或您的社区中**分享使用心得**（如 BIOS 设置技巧、蓝牙配对经验、最喜欢的模式等）
- **向同事推荐**，特别是那些管理无头设备、需要口袋 KVM 的朋友
- **持续发送真实的反馈**，尤其是那些“粗糙”的地方。相比于赞美，这些反馈对产品的塑造作用更大

再次感谢大家支持 KVM-GO，并帮助我们为每一个人打造更好的便携式 KVM-over-USB 体验。

顺颂商祺，

**Openterface 团队 | TechxArtisan**
