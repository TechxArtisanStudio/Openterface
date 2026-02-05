---
title: "Openterface Mini-KVM (Windows) - 硬件诊断自检指南"
description: "在 Windows 版 Openterface 应用中运行硬件诊断自检的逐步指南。学习如何测试 USB 连接，检测问题，并将诊断报告发送给支持团队。"
keywords: "Openterface Mini-KVM, Windows, 硬件诊断, 诊断自检, KVM 故障排除, USB KVM 诊断, Mini-KVM 支持, KVM 设备测试, Windows KVM, KVM 缺陷报告, Mini-KVM 故障排除指南"
---

# Openterface Mini-KVM (Windows) — 硬件诊断自检指南

本指南介绍如何在 **Windows** 版 Openterface 应用中运行**硬件诊断**自检，以及如何在检测到问题时将诊断报告发送给支持团队。

<iframe width="560" height="315" src="https://www.youtube.com/embed/uSq3BDc_SBU?si=rREugsUxX1FzDGqm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## 开始之前

- 将 Mini-KVM 连接到**主机**和**目标**。
- 测试期间（尤其是压力测试期间）保持目标设备空闲。

> **重要（Windows）：** 诊断**不会自动前进**。  
> 要在测试之间移动，请使用**下一步**（底部栏）**或**点击**左侧面板**中的测试项目。  
> 每个测试通过点击**检查现在**来执行。

![next_webp](https://assets2.openterface.com/images/next.webp)

---

## 正常设备（通过）

### 步骤 1 — 打开硬件诊断（Windows）
在 Windows Openterface 应用中，打开：**高级 → 硬件诊断**。  

### 步骤 2 — 运行自检
在硬件诊断窗口中，点击**检查现在**以运行当前诊断步骤。  

### 步骤 3 — 目标即插即用（按提示操作）
当**目标即插即用**要求您重新连接目标线缆时，请按照屏幕上的说明操作。  
某些设置可能要求您**多次**拔插（例如两次）。  

![Target-plug&play](https://assets2.openterface.com/images/Target-plug%26play.webp)

### 步骤 4 — 主机即插即用（按提示操作）
按照屏幕上的说明操作主机侧。  

![Host-plug&play](https://assets2.openterface.com/images/Host-plug%26play.webp)

### 步骤 5 — 压力测试（不要操作目标设备）
在**压力测试**期间，目标鼠标可能会自动移动以进行检测。  
测试运行期间**请勿操作目标设备**。  

> **注意：** 鼠标可能会快速移动 — 不要触碰目标设备。

![stress-test](https://assets2.openterface.com/images/stress-test.webp)

### 步骤 6 — 确认通过
继续直到自检完成。如果一切正常，结果将显示**通过 / 所有测试已通过**。  

---

## 检测到问题（键盘/鼠标示例）

如果检测到问题，一个或多个项目可能显示**失败**。

### 步骤 1 — 运行相同的硬件诊断
打开**高级 → 硬件诊断**，然后点击**检查现在**开始。  

### 步骤 2 — 继续完成检查
继续完成剩余测试，直到诊断完成。  

### 步骤 3 — 支持邮件自动打开
当诊断因问题而完成时，**支持邮件**窗口将自动打开。  

---

## 将日志发送给支持团队（Windows）

### 步骤 4 — 应用订单号 + 姓名
输入您的**订单号**和**姓名**，然后点击**应用**将其插入到邮件草稿中。 

![ID+Name](https://assets2.openterface.com/images/ID+Name.webp)

### 步骤 5 — 复制邮箱地址和草稿
- 点击**复制邮箱**以复制支持邮箱地址。
- 点击**复制草稿**以复制预填写的邮件内容（包括订单号 + 姓名）。  
将两者粘贴到您的邮件客户端（Gmail/Outlook 等）中。  

![copy](https://assets2.openterface.com/images/copy.webp)

### 步骤 6 — 附加正确的日志文件
点击**打开文件文件夹**。工具会指示需要附加哪些文件。  
**仅附加所请求的日志文件**（文件夹中可能包含许多其他日志）。  

![list](https://assets2.openterface.com/images/list.webp)

![compress](https://assets2.openterface.com/images/compress.webp)

### 步骤 7 — 同时附加设置照片
在同一封邮件中，附加一张清晰的**设置照片**，显示：
- Mini-KVM 设备，
- **主机**和**目标**的连接，
- 端口和线缆清晰可见。  

### 步骤 8 — 发送邮件
将邮件发送给支持团队（草稿文本 + 请求的日志 + 设置照片已附加）。  

---

## 联系支持时需包含的内容

- **订单号**
- **请求的诊断日志文件**
- **设置照片**（Mini-KVM + 主机/目标接线）
