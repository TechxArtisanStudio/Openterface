---
title: "Openterface Mini-KVM - 诊断自检指南（macOS）"
description: "使用 macOS 应用运行 Openterface Mini-KVM 设备诊断自检的逐步指南。学习如何测试 USB 连接，检测问题，并将缺陷报告发送给支持团队。"
keywords: "Openterface Mini-KVM, macOS, 诊断自检, KVM 故障排除, USB KVM 诊断, Mini-KVM 支持, KVM 设备测试, USB 连接测试, KVM 缺陷报告, Mini-KVM 故障排除指南, KVM 诊断工具, 无头服务器诊断, IT 故障排除工具"
---

# Openterface Mini-KVM - 诊断自检指南（macOS）

本指南提供运行 Openterface Mini-KVM 设备诊断自检的逐步说明。

<iframe width="560" height="315" src="https://www.youtube.com/embed/-K6Idzky3fY?si=r7pZgCkBzzZXgrLT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## 正常设备

**步骤 1:** 在 Openterface 应用中，打开 设置 → 高级设置。

**步骤 2:** 在设置窗口中，进入 高级与调试。

**步骤 3:** 点击 打开诊断工具。

**步骤 4:** 当提示时，点击 启用以开启诊断日志记录。

**步骤 5:** 点击 检查现在 开始自检。

**步骤 6:** 点击 开始测试，然后按照提示拔下并重新插入黑色 USB-C（目标侧）。

![minikvm-support-target](https://assets.openterface.com/images/minikvm/support/target.webp)

**步骤 7:** 点击 开始测试，然后按照提示拔下并重新插入橙色 USB-C（主机侧）。

![minikvm-support-host](https://assets.openterface.com/images/minikvm/support/host.webp)

**步骤 8:** 点击 开始测试，等待测试完成。

**步骤 9:** 点击 重置现在，等待其完成。

**步骤 10:** 点击 更改现在，等待波特率切换完成。

**步骤 11:** 点击 开始测试，然后等待约30秒。测试运行期间不要操作目标设备。

> **注意:** 鼠标可能会快速移动，不要触碰目标设备。

![minikvm-support-stress_test](https://assets.openterface.com/images/minikvm/support/stress_test.gif)

**步骤 12:** 确认所有项目显示绿色对勾，并且进度完成。

**步骤 13:** 点击 ❌（右上角）关闭诊断窗口。

---

## 检测到问题（键盘/鼠标示例）

首先按照“正常设备”中的步骤 1–11 操作。以下说明解释了当检测到键盘/鼠标问题时您将看到的内容。

## 问题显示方式

在此示例中，由于目标侧键盘/鼠标（HID）问题影响整体检查，首先显示“整体连接”为失败。这是早期指标，并非单独问题。（您将在左侧看到“整体连接”旁边的失败状态突出显示。）

- **整体连接:** 由于目标侧问题，此处首先显示失败。

![minikvm-support-overall_connection](https://assets.openterface.com/images/minikvm/support/overall_connection.webp)

- **目标即插即用:** 运行此步骤后，结果可以更清晰地显示目标侧问题。

> **提示:** 如果某一步显示失败，诊断不会停止，但可能会停止自动前进——因此您需要手动继续。

## 额外最终测试（取决于问题类型）

**步骤 12:** 压力测试后，根据检测到的问题，诊断可能会显示额外的最终测试；在此键盘/鼠标示例中，它将继续进行目标端口检查。

**步骤 13:** 点击“检测设备”以开始目标端口检查，然后按照屏幕上的说明操作。

![minikvm-support-target_port_checking](https://assets.openterface.com/images/minikvm/support/target_port_checking.webp)

## 检测到问题时会发生什么

**步骤 14:** 要继续，点击底部的“下一步”或从左侧面板选择下一个测试。

![minikvm-support-target_plug_n_play](https://assets.openterface.com/images/minikvm/support/target_plug_n_play.webp)

## 将日志发送给支持团队

**步骤 15:** 点击 发送缺陷报告至支持，准备向支持团队发送报告。

![minikvm-support-send_defect_report_to_support](https://assets.openterface.com/images/minikvm/support/send_defect_report_to_support.webp)

**步骤 16:** 在缺陷报告窗口中，输入您的 **订单号** 和 **姓名**，然后点击 **应用** 将其插入到邮件草稿中。

**步骤 17:** 复制邮箱地址和草稿：
- 点击 **复制邮箱** 以复制支持邮箱地址。
- 点击 **复制草稿** 以复制预填写的邮件内容（包括订单号 + 姓名）。
- 将两者粘贴到您的邮件客户端（Gmail/Outlook 等）中。

![minikvm-support-support](https://assets.openterface.com/images/minikvm/support/support.webp)

**步骤 18:** 点击 **打开日志文件夹**。工具会指示需要附加哪些文件。**仅附加所请求的日志文件**（文件夹中可能包含许多其他日志）。

**步骤 19:** 在同一封邮件中，附加一张清晰的 **设置照片**，显示：
- Mini-KVM 设备，
- **主机** 和 **目标** 的连接，
- 端口和线缆清晰可见。

**步骤 20:** 将邮件发送给支持团队（草稿文本 + 请求的日志 + 设置照片已附加）。

**步骤 21:** 点击 ❌（右上角）关闭诊断窗口。