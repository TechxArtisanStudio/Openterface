# Openterface KVM 扩展用于 uConsole

![KVM Extension Connected to Target Device 2](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-2.webp){:style="height:300px"}

## 概述

通过这个即插即用的扩展板，将您的 uConsole 转换为**便携式 KVM（键盘、视频、鼠标）控制台**。

**Openterface KVM 扩展**替换您 uConsole 扩展槽中的原始 4G/LTE 调制解调器，并提供直接的**HDMI 输入和 USB HID 控制**，让您可以在移动中管理无头设备——无需外部显示器、键盘或网络配置。

![KVM Extension Board Front Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:300px"}
![KVM Extension Board Backm Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:300px"}


## 功能特点

- **完美外形**  
    匹配 4G/LTE 模块的 37×77 mm 尺寸，实现无缝硬件集成。

- **直接 HDMI + USB HID**  
    使用 uConsole 的内置输入和屏幕实现对连接设备的响应式控制。

- **低延迟**  
    适用于 BIOS 级故障排除和实时交互。

- **真正便携**  
    使 uConsole 成为开发者、工程师和技术人员的移动工具。

- **开源友好**  
    基于 [Openterface KVM](https://github.com/techxArtisanStudio/openterface_qt) 平台构建。欢迎社区贡献。


## 使用场景

- **系统管理**  
    无需笨重的 KVM 切换器即可访问和排除服务器或嵌入式设备故障。

- **硬件开发**  
    直接测试和调试树莓派、单板计算机或微控制器。

- **现场部署**  
    在数据中心或远程位置执行维护或配置。


## 硬件安装

按照以下硬件安装步骤，用 Openterface KVM 扩展板替换您 uConsole 中的 4G/LTE 模块，并确保安全安装。

### 您需要的物品

- 您的 Openterface KVM 扩展板
- 提供的垫片（塑料垫片） 
- 六角螺丝刀（用于板的安装螺丝）
- ESD 预防措施（腕带或接地表面）——推荐

### 安装扩展板

1. 断电和断开连接

    关闭 uConsole 并断开所有电源和电缆。

2. 移除现有模块

    使用六角螺丝刀移除固定 4G/LTE 模块或现有扩展板的两个螺丝。

    小心地垂直抬起板子，避免弯曲弹簧接触器。

3. 安装 KVM 扩展板

    - Openterface KVM 扩展板厚度为 1.0 mm（比原始 4G/LTE 的 1.2 mm 更薄）。因此，我们建议将提供的垫片放在螺丝柱上（PCB 和安装支架之间），使垫片在放置板子之前位于螺丝柱下方。这补偿了更薄的 PCB 并有助于确保适当的弹簧接触器压力。
    - 如果您想先检查，可以在没有垫片的情况下放置板子并验证均匀的弹簧接触；如果接触不均匀或板子放置松散，请添加垫片并重新放置板子。

<div style="display:flex;gap:1rem;align-items:flex-start;flex-wrap:wrap">
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-gasket-1.webp" alt="Installing KVM Extension gasket" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp" alt="Installing KVM Extension into uConsole" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
</div>

4. 重新插入螺丝

    重新插入两个螺丝并用六角螺丝刀拧紧。拧紧即可——不要过度拧紧。

5. 验证安装

    板子应该平整放置，没有明显移动。验证弹簧接触器在焊盘上均匀接触。

6. 测试硬件

    重新连接电源，启动系统，并测试 HDMI、音频和 USB HID 设备以确认正常运行。

## 软件设置指南

要使用 KVM 扩展，请在您的 uConsole 上安装**Openterface 应用**。

选项 1 - 使用 Flatpak 版本 Openterface
- 📖 按照我们的 [Flatpak 安装指南](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) 获取详细的设置步骤。

![KVM Extension Connected to Target Device](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1c.webp){:style="height:300px"}

选项 2 - 从 Rex 安装社区版本

如果您想要 Rex 维护的社区构建，请添加他的存储库并使用下面的命令安装包。

1. 添加存储库 GPG 密钥和存储库

```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. 更新和安装

```bash
sudo apt update
sudo apt install openterfaceqt
```

注意：这些命令需要 sudo。存储库针对 arm64 Bookworm 包；安装前请验证与您设备的兼容性。

## 预发布状态

- 📦 第一批目前正在准备中  
- ⏳ 预计发货开始于**2024年8月初**  
- 🛒 数量有限——[立即预订](https://shop.techxartisan.com/products/openterface-kvm-ext-for-uconsole) 以保留您的设备

> **预订通知**  
> 此商品目前处于预订状态，预计交货时间为**约2个月**。  
> 如果您需要其他商品更快发货，请下**单独订单**。组合订单将在此产品准备就绪时发货。

## 社区和支持

- 🗨️ 加入讨论：[Discord 服务器](https://discord.gg/ruAD9kcYbq)  
- 📧 邮件支持：[info@openterface.com](mailto:info@openterface.com)


## 常见问题

**问：KVM 扩展板如何工作？**  
它捕获目标设备的 HDMI 输出并在 uConsole 上显示。同时，uConsole 的键盘和轨迹球用于通过 USB HID 仿真控制目标设备。

**问：我可以在安装 4G/LTE 模块的情况下使用这个吗？**  
不可以。此板占用相同的扩展槽。您需要在蜂窝连接或 KVM 功能之间选择。

**问：软件是开源的吗？**  
是的！我们的**Openterface Connect**应用完全开源，可在我们的 [GitHub 存储库](https://github.com/TechxArtisanStudio/Openterface_QT) 中找到。
