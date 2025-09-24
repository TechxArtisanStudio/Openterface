---
title: "硬件安装"
description: "Openterface KVM Extension for uConsole 的逐步硬件安装指南。学习如何在 uConsole 的扩展槽中正确安装扩展板，并提供详细的安全指南。"
keywords: "KVM扩展安装, uConsole硬件设置, 扩展板安装, uConsole扩展槽, KVM硬件指南, 物理安装"
---

# **硬件安装** | Openterface KVM Extension for uConsole

## 概述
KVM Extension 替换 uConsole 扩展槽中的 4G/LTE 模块，添加直接 HDMI 输入和 USB HID 控制。

## 您需要的物品
- 安装前请检查您的[包装内容](whats-in-the-box.md)  
- Openterface KVM Extension 板  
- 提供的**垫圈**（确保稳定安装和均匀压力）  
- 六角螺丝刀（用于安装螺丝）  
- ESD 保护（防静电手环或接地表面）— 推荐  

## 安装步骤

### **1. 断电**
关闭 uConsole 并断开所有电源和电缆。

### **2. 移除现有模块**
使用六角螺丝刀移除两个螺丝。  
**垂直向上**提起板子，避免弯曲弹簧接触器。

### **3. 安装 KVM Extension**
- 将**垫圈**放在螺丝柱上。  
- 将 KVM Extension 牢固地插入扩展槽。  
- 垫圈补偿了稍薄的 PCB（1.0 mm vs 1.2 mm），保持适当的弹簧接触压力。

??? note "最终安装前检查适配性"
    您可以先**不使用垫圈**将板子插入以测试适配性。如果板子感觉松动或接触不均匀，请添加垫圈并重新插入板子。Openterface KVM Extension 厚度为 1.0 mm，比原始 LTE 模块（1.2 mm）稍薄。使用提供的垫圈可确保稳定安装和可靠的弹簧接触。  
    ![extension-slot-loose](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-slot-loose.webp){:style="height:220px"}

### **4. 固定板子**
重新插入螺丝并**轻柔地**拧紧 — **不要过度拧紧**，因为这可能会损坏板子或损坏螺纹。

![extension-screw-washer-installed](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installed.jpg){:style="height:220px"}
![extension-screw-washer-installing](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installing.jpg){:style="height:220px"}
![extension-install-1](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp){:style="height:220px"}

### **5. 验证安装**
板子应该**平整稳定**，所有焊盘上的弹簧接触均匀。不应该有明显的摆动或移动。

### **6. 安装扩展槽盖**
重新安装扩展槽盖以保护 KVM Extension 板并保持 uConsole 的原始外观。

??? note "扩展槽盖上的文字方向"
    从某些角度观看时，扩展槽盖上的文字可能看起来"倒置"。这是有意的设计 - 文字的方向是为了在您手持 uConsole 并从顶部到底部查看端口时能够阅读，这是使用设备时的自然观看位置。
    ![expansion-slot-text-orientation](https://assets.openterface.com/images/product/openterface-kvm-uconsole-expansion-slot-text-orientation.webp){:style="height:220px"}

---

**下一步**

1. 前往[软件设置](/product/uconsole-kvm-extension/software-setup/)安装 Openterface App。  
2. 前往[连接到目标设备](/product/uconsole-kvm-extension/connect-to-target/)连接您的目标设备。  
3. 查看[功能与规格](/product/uconsole-kvm-extension/features/)了解详细技术规格。
