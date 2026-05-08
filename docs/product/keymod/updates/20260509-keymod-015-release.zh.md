---
draft: false
date: 2026-05-09
title: "KeyMod 0.15：游戏手柄预设管线、键盘与鼠标（Basic）层级、多点触控板布局"
description: "KeyMod 0.15 搭载游戏手柄预设管线（schema v7）、多点触控板布局、全屏键盘的键盘与鼠标（Basic）层级，以及全应用范围的 KeyMod 品牌标识。向精致的输入体验迈出重要一步。"
keywords: "KeyMod 0.15, KeyMod 发布, 游戏手柄预设, 多点触控板, 键盘鼠标 Basic, KeyMod 品牌, Openterface KeyMod 更新, HID 模拟器, 虚拟手柄, Android 键盘应用"
author: "TechxArtisan Studio"
category: "产品更新"
tags: ["KeyMod", "产品更新", "发布", "游戏手柄", "键盘", "Android"]
featured: false
social:
  image: "https://assets.openterface.com/images/keymod/keymod-015-release.jpg"
  title: "KeyMod 0.15 发布 — 游戏手柄预设、Basic 层级、多点触控板"
  description: "KeyMod 0.15 带来游戏手柄预设管线 v7、专用的键盘与鼠标（Basic）层级、多点触控板布局以及全新的 KeyMod 品牌标识。"
---

# KeyMod 0.15：游戏手柄预设管线、键盘与鼠标（Basic）层级、多点触控板布局

KeyMod **0.15**（`versionCode` **15**）是一个里程碑式的版本，包含三大核心功能：**游戏手柄预设管线**（布局 schema **v6-v7**）、专用的**键盘与鼠标（Basic）**层级以及**多点触控板**布局。此更新还在欢迎流程和构建产物中全面引入了 **KeyMod** 品牌标识。

## 游戏手柄：预设管线 v7

游戏手柄现在使用了真正的**预设系统**，你可以保存、加载、导入和导出自定义手柄布局。

### 变更内容

- **Preset store v7** 替代了旧的内置布局。经典出厂预设（`preset_classic_*`）和**Two buttons**（`preset_two_buttons`）已从磁盘中移除。仅保留 **`preset_default`** 作为受删除保护的出厂布局。
- **Schema v7** 使 **`stick_left`** 变为可选。布局现在可以完全没有左侧摇杆模块。**Add module** 菜单会插入 **`stick_left`**、**`stick_left_2`**、**`stick_left_3`** 等。
- **多点触控板支持**：预设可包含多个触控板（`touchpad_1`、`touchpad_2`）。添加触控板会分配下一个可用 ID，锚点略微偏移。内置的 L/M/R 鼠标按钮在所有触控板之间共享。
- **触控板鼠标按钮大小调整**：鼠标按钮现在使用更大的默认绘制半径。你可以通过长按触控板上的 **Mouse button size** 调整大小，或在单个鼠标模块上长按 **This button size**。
- **辅助摇杆默认值**：**`stick_left_2+`** 默认为方向键十字 + WASD 映射。

### 预设管理

- **轻触**工具栏中的 Preset 芯片可切换可用布局
- **长按**可打开完整的预设列表，包含导入、添加模块和导出选项
- 附带的 **emu-6** 布局作为初始预设
- 导出创建器支持 i18n，便于跨语言分享预设

## 键盘与鼠标（Basic）

专为专注打字设计的全屏键盘层级，无应用顶部标题栏。

### 功能

- **全屏键盘**：无应用主标题栏，提供更多屏幕空间
- **竖屏和横屏数字键盘**：竖屏 5x8 网格（PrtSc / ScrLk / Pause / Home / End），横屏 8x5 网格（带加高的 +、Enter 和 00）
- **IME 纯 ASCII 发送门**：在 compose 模式下输入长文本，以干净的 HID 按键发送
- **长按重复**：按住字符/功能键可自动重复（约 400ms 延迟，约 50ms 重复间隔）
- **按键预览**：按下按键时，浮动气泡会在按键上方显示实际标签
- **触觉反馈**和**主题自适应**按键表面

### 粘滞修饰符 vs 组合键修饰符

设置中可选择 Basic 键盘使用**粘滞修饰符**（轻触锁定）或**瞬时 + 长按组合键**（默认）。

## 品牌标识

- 应用显示名称现已改为 **KeyMod**
- 欢迎屏幕显示 **KeyMod** 标识
- CI 产物和 APK 文件名使用 **KeyMod** 前缀
- `applicationId` 保持为 **`com.openterface.keymod`**，支持原地升级

## 未变更内容

**键盘与鼠标 Pro**（复合模式，含 Shortcut Hub 条行、分割布局和完整的 IME 行为）保持不变，仍是功能完整的体验。

## 获取更新

**此版本（0.15）：** [KeyMod-release-0.15.apk](https://assets2.openterface.com/data/KeyMod-release-0.15.apk)

> **Beta 说明：** KeyMod Android 应用仍处于活跃 Beta 阶段。源码仓库尚未公开 — 我们计划在众筹成功后正式开源。如果你是 Beta 测试者并需要最新 APK，请在 Discord 上联系我们，我们会发送构建给你。

> **已知问题：** 此版本对游戏手柄预设系统和 Basic 键盘层级进行了大量改动。我们的开发团队仍在内部测试中，可能会遇到一些 bug。如果遇到任何异常情况，请在 Discord 上报告 — 你的反馈能帮助我们更快稳定版本。

已安装用户可直接原地升级。

## 升级说明

- **游戏手柄**：你之前的双按钮偏好会在首次启动时自动激活 **Two buttons** 预设。请使用 **Preset**（轻触切换，长按查看列表）替代旧的 1 Button / 2 Buttons 控件。
- **键盘与鼠标（Basic）**：打开 Basic 即可体验全屏键盘。Pro 模式可通过导航抽屉获取完整的 Shortcut Hub 体验。

此致，

Openterface Team | TechxArtisan
