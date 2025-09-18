---
title: "扩展引脚"
description: "探索 Openterface Mini-KVM 扩展引脚在自定义硬件开发和开源项目中的潜力。"
keywords: "Mini-KVM 扩展引脚, 自定义开发, 硬件改装, 开源 KVM"
---

# **扩展引脚** | 开发者模式 | Openterface Mini-KVM

![mini-kvm-pins-port](https://assets.openterface.com/images/product/mini-kvm-pins-port.webp){:style="height:360px"}
![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="height:300px"}

Openterface Mini-KVM 配备用于高级开发和 [Open Software](/app) 实验的扩展引脚。这些引脚在标准外壳配置中不会外露。

## 如何访问引脚

1. 拆解设备。
2. 将原装外壳上盖替换为专用的扩展引脚盖（Extension Pin Cap）。
3. 下载扩展引脚盖的 [3D 模型](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models)。
4. 查看我们的 [硬件 GitHub 仓库](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware)。

![change-cap](https://assets.openterface.com/images/product/change-cap.svg#only-light){:style="height:300px"}
![change-cap](https://assets.openterface.com/images/product/change-cap_1.svg#only-dark){:style="height:300px"}

!!! warning "保修失效"
    拆除原装外壳可能导致产品保修失效。所有改装或拆解行为均由用户自行承担风险。

!!! note "实验性功能"
    使用这些引脚开发的功能属于实验性，尚未经过充分测试。因改装、暴露扩展引脚或对设备进行其他更改而导致的任何损坏、伤害或故障，Openterface 概不负责。

## 引脚配置

![target-side](https://assets.openterface.com/images/product/extension-pins-1.svg#only-light){:style="height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2.svg#only-light){:style="height:200px"}
![target-side](https://assets.openterface.com/images/product/extension-pins-1_1.svg#only-dark){:style="height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2_1.svg#only-dark){:style="height:200px"}

扩展引脚提供以下连接：

1. 为外部组件提供 USB 5V 供电
2. Host 侧 USB 集线器的数据正极
3. Host 侧 USB 集线器的数据负极
4. Target 侧 USB 集线器的数据正极
5. Target 侧 USB 集线器的数据负极
6. 地（GND）

!!! danger "错误连接会造成损坏"
    混淆 VCC 与 GND 可能会对设备及连接的组件造成严重损害。为设备通电前请务必再次核对引脚连接。

## 扩展引脚盖（Extension Pin Cap）

![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="height:360px"}

该 3D 打印的扩展引脚盖用于替换 Openterface Mini-KVM 的原装上盖，使高级用户能够暴露并访问扩展引脚以进行自定义开发。你可以从我们的 GitHub 仓库下载 3D 模型文件并自行打印此盖子。

- **用途**：为高级硬件开发提供扩展引脚的访问。
- **下载**：[3D 模型文件](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models)

## 参与开发

随着我们不断开发与实验，我们将持续更新本节，介绍这些引脚的更多潜能及其创造性的使用方式。你的创意与专长将助力拓展 Openterface Mini-KVM 的可能性。欢迎参与：

1. **分享你的想法**：对这些引脚有酷炫的使用构想吗？我们很想听到！
2. **贡献 DIY 项目**：如果你做出了有趣的作品，欢迎在我们的 [Discord Openterface](/discord) 社区分享。
3. **加入讨论**：与其他开发者和爱好者一起头脑风暴并协作。

让我们一起构建与创新！
