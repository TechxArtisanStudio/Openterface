---
draft: false
date: 2026-05-21
title: "KeyCmd 0.19：应用品牌更名、KM Pro 输入模式、多语言支持及各模式引导教程"
description: "KeyCmd 0.19 带来从 KeyMod 到 KeyCmd 的重大品牌更名、全新 KM Pro 输入模式（支持 Unicode HID 发送）、多语言 UI（韩语、意大利语、俄语、巴西葡语）、各模式交互式引导教程，以及数十项 UX 优化。"
keywords: "KeyCmd 0.19, KeyCmd 发布, 应用更名, 输入模式, Unicode HID 发送, 多语言, 交互式引导教程, Openterface KeyCmd 更新, HID 模拟器, 虚拟键盘, Android 键盘应用"
author: "TechxArtisan Studio"
category: "Product Updates"
tags: ["KeyCmd", "Product Updates", "Release", "Compose", "i18n", "Android"]
featured: false
social:
  image: "https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp"
  title: "KeyCmd 0.19 发布 — 输入模式、品牌更名、多语言、引导教程"
  description: "KeyCmd 0.19 带来全新的输入模式、KeyCmd 品牌更名、4 种新语言、交互式引导教程以及大量 UX 优化。"
---

# KeyCmd 0.19：应用品牌更名、KM Pro 输入模式、多语言支持及各模式引导教程

KeyCmd **0.19**（`versionCode` **19**）是一次重大更新，带来了从 KeyMod 到 KeyCmd 的**应用品牌更名**、支持 Unicode 感知 HID 发送的全新 **KM Pro 输入模式**、扩展的**多语言 UI**（包括韩语、意大利语、俄语和巴西葡语）、**各模式交互式引导教程**，以及键盘、游戏手柄和演示模式中的数十项 UX 优化。

## 应用品牌更名：KeyMod → KeyCmd

应用显示名称现已在所有入口点统一为 **KeyCmd**。此次更名清晰区分了 **KeyMod 硬件**与其配套的 **KeyCmd 应用**。

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Welcome-Screen-landscape.webp" alt="KeyCmd 欢迎页面" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">

### 变更内容

- **应用显示名称**：启动器图标和系统 UI 现在显示"KeyCmd"
- **欢迎流程**：从 KeyMod 更新为 KeyCmd 的品牌标识和文案
- **CI 产物和 APK 文件名**：使用 **KeyCmd** 前缀
- `applicationId` 仍为 **`com.openterface.keymod`**，确保无缝原地升级

老用户：你的设置、配置文件和已配对设备均已保留，升级过程无缝衔接。

## 键盘与鼠标：全屏体验

KeyCmd 提供全屏键盘、触控板和数字键盘体验 — 针对竖屏和横屏方向均进行了优化。

<div class="slideshow-container" id="slideshow-keycmd-019-kbm-zh" data-auto-slide="true" data-auto-slide-interval="3000">
  <div class="slideshow-wrapper">
    <div class="slide active">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Full-Keyboard-landscape.webp" alt="横屏全屏键盘" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-landscape.webp" alt="横屏数字键盘" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-NumPad-portrait.webp" alt="竖屏数字键盘" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Keyboard-TouchPad-portrait.webp" alt="竖屏键盘和触控板" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-km-basic-Touchpad.webp" alt="横屏触控板" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Remote-Coding-portrait.webp" alt="使用 KeyCmd 远程编程" style="max-height:320px;" loading="lazy">
    </div>
    <div class="slide">
      <img src="https://assets2.openterface.com/images/keymod/KeyCmd-Settings-screen.webp" alt="KeyCmd 设置页面" style="max-height:320px;" loading="lazy">
    </div>
  </div>

  <div class="slideshow-navigation">
    <button class="nav-arrow left" onclick="changeSlide('slideshow-keycmd-019-kbm-zh', -1)">❮</button>
    <div class="slideshow-dots">
      <span class="dot active" onclick="currentSlide('slideshow-keycmd-019-kbm-zh', 1)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-zh', 2)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-zh', 3)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-zh', 4)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-zh', 5)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-zh', 6)"></span>
      <span class="dot" onclick="currentSlide('slideshow-keycmd-019-kbm-zh', 7)"></span>
    </div>
    <button class="nav-arrow right" onclick="changeSlide('slideshow-keycmd-019-kbm-zh', 1)">❯</button>
  </div>
</div>

## KM Pro：输入模式

0.19 版本中最重要的新功能是 KM Pro 中的**输入模式** — 一个专用的文本编辑器，可让你输入长段文字并将其作为 HID 按键发送到目标机器。

<img src="https://assets2.openterface.com/images/keymod/KeyCmd-Script-Running-portrait.webp" alt="输入模式中的脚本运行" style="max-width:100%; border-radius:8px; margin:16px 0;" loading="lazy">

<p><strong>Compose &amp; Send demo (YouTube Short)</strong></p>

<iframe width="560" height="315" loading="lazy" src="https://www.youtube.com/embed/_rJF-hTF3_E" title="KeyCmd Compose &amp; Send demo (YouTube Short)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


### 输入编辑器

- **顶部快捷栏 + 输入操作行**，包含**清除**和**撤销/清除**控件
- **草稿保留**：你的文本在子模式切换甚至成功发送后均会保留
- **输入法集成**：使用手机键盘输入，以干净的 HID 按键形式发送
- **确定性发送进度**：长 HID 缓冲区的可见进度条，让你清楚知道发送进度

### 感知 Unicode 的 HID 发送

- **双模式风险审查**：在发送非 ASCII 文本之前，对话框会警告 Unicode 兼容性并提供检查/预览操作
- **macOS Unicode 十六进制流程**：在 macOS 主机上，应用使用 Option+十六进制代码输入法输入扩展字符
- **更安全的发送对话框**：审查页面会根据缓冲区是纯 ASCII 还是包含 Unicode 字符自适应内容
- **字符检查工具**：发送风险对话框提供**检查**和**预览**操作，macOS 主机还包含专用的 **Unicode 十六进制路径审核**入口

### KM Basic 范围

在 0.19 版本中，**输入模式仍然是键盘与鼠标 Pro 的功能**。KM Basic 专注于全屏键盘、触控板和数字键盘工作流。

## 多语言支持

KeyCmd 现已支持 **11 种应用 UI 语言**。本次更新新增了四种本地化：

- **韩语 (ko)**：完整 UI 翻译
- **意大利语 (it)**：完整 UI 翻译
- **俄语 (ru)**：完整 UI 翻译
- **巴西葡萄牙语 (pt-BR)**：完整 UI 翻译

加上现有的英语、简体中文、繁体中文、日语、法语、德语和西班牙语，KeyCmd 现已覆盖我们绝大部分全球用户群体。

### 变更内容

- **设置中的语言选择器**，使用标准应用语言名称
- **蓝牙标题**和**按键点击预览**已本地化
- **发布 lint**修复了所有语言中输入警告标签的问题

## 交互式引导教程

每个模式现在都有**内置的交互式引导教程**，逐步带你了解其功能。

### 可用教程

- **快捷中心教程**：打开默认配置，涵盖详情 UI、分类标签和快捷方式管理
- **游戏手柄教程**：解释游戏手柄布局、模块管理和预设系统
- **KM Pro 教程**：涵盖输入模式、快捷面板和 Pro 专属功能
- **KM Basic 教程**：解释全屏键盘、修饰键按住滑动和数字键盘

### 教程功能

- **各模式独立引导**：每个模式都有量身定制的教程
- **回放面板**：随时通过**模式引导**按钮（连接状态图标左侧的图标）重访任何教程
- **i18n 支持**：教程内容已本地化为全部应用语言
- **横屏优化**：底部面板布局在横屏方向下正确适配

## UX 优化

### 键盘

- **按键点击预览**：在点击之前就能看到将要发送的内容。通过设置启用。默认启用。
- **快速点击 HID 修复**：改进了键盘点击释放时间和合并释放事件，实现更快的打字体验
- **替代字符触摸处理**：长按 `a` 键现在显示替代字符 ¥（上）、£（左）、€（右），并带有改进的视觉反馈
- **修饰键按住滑动**：在 KM Basic/Pro 教程中，新增步骤教授按住滑动手势以快速访问修饰键

### 游戏手柄

- **编辑会话栏已移除**：更简洁的游戏手柄界面，去除了旧的编辑会话工具栏
- **游戏手柄界面和教程**：全新视觉打磨和集成的引导教程
- **模式引导图标**：放置在连接状态图标左侧，方便访问

### 演示模式

- **竖屏锁定**：演示模式被限制为竖屏和反向竖屏方向，以确保稳定的演示控制

### UI 与主题

- **强调色色板**：将主题色族选择器替换为可视化强调色色板，更方便颜色选择
- **UI 强调色对齐**：所有 UI 强调色现在跟随主题色族（而非旧版主色）
- **头部右侧集群**：改进了主应用和 KM Basic 界面中连接图标的尺寸
- **输入发送按钮样式**：对齐了亮色模式下非 ASCII 发送按钮的外观

### 设置

- **设置重组**：标准应用语言名称；重命名了模拟器安装脚本以提高清晰度
- **开发者辅助脚本**：重命名以更清晰地标识设备和操作命名
- **FAQ 文档**：更新了 `docs/FAQ.md` 以反映当前应用行为

## 真实使用场景

### 远程编程

KeyCmd 不仅仅用于服务器管理。开发者用它进行**远程编程会话** — 从手机或平板控制无头开发机，配备完整的键盘、触控板和数字键盘支持。

## 不变的部分

**键盘与鼠标 Pro**（包含快捷中心条、分割布局和丰富的输入法行为的复合模式）依然是之前的完整功能体验。所有现有配置、预设和已配对设备均已保留。

## 获取更新

**此版本 (0.19)：** [KeyCmd-release-0.19.apk](https://assets2.openterface.com/data/KeyCmd-release-0.19.apk)

> **Beta 提示：** KeyCmd Android 应用仍处于活跃 Beta 阶段。源代码仓库尚未公开 — 我们计划在众筹活动成功后开源。如果你是 Beta 测试者并需要最新的 APK，请在 Discord 上联系我们，我们会为你提供构建版本。

现有安装可原地升级。

## 兼容 Mini-KVM 和 KVM-Go

KeyCmd 应用不仅限于 KeyMod 硬件。现有 Openterface 用户也可以试用：

- **KVM-Go**：通过**蓝牙**或 **USB** 连接
- **Mini-KVM**：通过 **USB** 连接

## 升级说明

- **品牌更名**：应用名称从 KeyMod 更改为 KeyCmd。你的数据已保留。
- **输入模式**：键盘与鼠标 Pro 新增功能。
- **引导教程**：在任何模式下点击引导图标（连接状态图标左侧）即可开始交互式教程。
- **语言**：前往设置更改应用语言。KeyCmd 现支持 11 种应用 UI 语言。

此致，

Openterface Team | TechxArtisan
