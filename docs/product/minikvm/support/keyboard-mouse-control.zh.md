# **排查键盘和鼠标无法控制目标计算机的问题**

偶尔，用户可能会遇到 Openterface 设备的键盘和鼠标功能无法正常工作的情况。本文档概述了最常见的原因及其解决或预防方法。

**软件反馈：** 当 Openterface 因缺少或错误的目标连接而无法建立 HID 通信时，UI 会突出显示状态，以便您快速采取行动。

- 在 **macOS** 上，Openterface 实用程序右上角的键盘和鼠标图标变为 **橙色**。  

    <img src="https://assets.openterface.com/images/software/inactive_keyboardmoue_macos.webp" alt="Inactive keyboard and mouse (macOS)" width="200" />

- 在 **Windows/Linux** 上，窗口底部的相应图标变为 **红色**。  

    <img src="https://assets.openterface.com/images/software/inactive_keyboardmoue_windows.webp" alt="Inactive keyboard and mouse (Windows)" width="200" />

Openterface 中仍有视频显示，但键盘和鼠标无响应——您可以看到目标桌面但无法控制它。这通常意味着 HID 通信未建立（例如，错误的目标电缆、电源不足的集线器或有缺陷的 HID 芯片）；请检查下面的清单和部分。软件还会阻止进一步的键盘/鼠标连接，直到解决布线/问题。

---

## **1. 不正确的电缆连接**

**问题：**  
令人惊讶的是很常见：用户忘记将 Openterface 目标 Type-C 端口连接到目标计算机。

**解决方案：**  
✅ 始终验证：
- **目标 Type-C 电缆** 从 Openterface **目标端口** 安全连接到您希望控制的 **目标计算机**。
- **主机 USB-A/USB-C 电缆** 已连接到您的 **主机/控制计算机**（运行 OpenterfaceQt 或控制软件的地方）。

> **提示：** 在复杂设置中标记电缆以避免混淆。
- 将黑色电缆连接到目标连接器的黑色一侧。
- 将橙色电缆连接到目标连接器的橙色覆盖一侧。


## **2. 使用无电源 USB 集线器**

**问题：**  
通过无电源 USB 集线器连接 Openterface 可能导致 **电源供应不足**（VBUS 电压下降）。这可能导致设备行为异常或无法初始化 HID（键盘/鼠标）功能。

**解决方案：**  
✅ **避免使用无电源 USB 集线器** 在 Openterface 和目标计算机之间。  
✅ 如果需要集线器，请使用 **高质量、外接电源的 USB 集线器**，能够提供稳定的 5V 电源。

> **注意：** USB 电源供应对 HID 芯片的可靠运行至关重要。电压下降会触发内部故障。

---

## **3. HID 芯片进入"僵尸状态"**

**问题：**  
在某些条件下——例如快速命令突发结合边际电源——内部 HID 芯片（例如 CH9329）可能进入 **"僵尸状态"。** 在此状态下：
- HID 芯片锁定，停止向主计算机发送串行响应数据。
- 它保持内部错误状态，防止主机软件正常重新初始化。
- 设备可能看起来已连接（视频存在），而输入仍无响应。
- 主机软件（例如 OpenterfaceQt）无法正确重新初始化设备。
- 重新插入所有电缆或电源循环 USB 连接通常无法清除此内部错误；需要 HID 芯片的出厂重置。

**解决方案：**  
执行 **HID 芯片的出厂重置**：

- 在 **macOS** 上：使用 macOS 实用程序的 **高级菜单** 中提供的 **串行重置工具**。  

    <img src="https://assets.openterface.com/images/software/MacOS_FactoryResetHID.webp" alt="Serial Reset Tool (macOS)" width="150" />

- 在 **OpenterfaceQt**（桌面应用）中：转到 **高级菜单 → HID 芯片出厂重置**。

    <img src="https://assets.openterface.com/images/software/OpenterfaceQT_FactoryResetHID.webp" alt="Factory Reset HID Chip (OpenterfaceQt)" width="150" />

> 这会清除芯片的内部状态并恢复正常操作。

---

## **4. 嘈杂环境中的波特率敏感性**

**问题：**  
Openterface 默认为 **115200 bps** 波特率以实现更快的鼠标数据传输。但是，在电气噪声环境中（例如，开关电源或长/屏蔽不足的电缆），这种高波特率可能导致 **串行通信错误**，导致 HID 命令丢失或损坏。

**解决方案：**  
切换到 **9600 bps** 波特率：
- 这在嘈杂设置中大大提高了 **通信可靠性**。
- 对延迟的影响在典型使用中 **可忽略不计**（例如，30 FPS 视频捕获和控制）。

> **建议：** 如果您在没有电源或连接问题的情况下遇到间歇性输入故障，请尝试在 Openterface 配置中降低波特率。

---

## **摘要清单**

如果键盘/鼠标不工作：

1. ✅ 确认正确的 **目标 Type-C 电缆** 已连接到 **目标计算机**。
2. ✅ 避免使用无电源 USB 集线器——使用直接连接或 **电源集线器**。
3. ✅ 如果设备看起来"冻结"，通过软件 **重置 HID 芯片**。
4. ✅ 在不稳定的环境中，**将波特率降低到 9600** 以获得更强大的通信。
5. ✅ 如果上述尝试没有帮助，请尝试主机上的其他 USB 端口或重启主计算机——操作系统可能在收到过多 USB 错误数据包后禁用端口或集线器。切换端口或重启主机通常会恢复连接。

---

通过解决这四个方面，可以预防或快速解决大多数间歇性 HID 问题。如有持续问题，请与支持 (support@openterface.com) 联系并提供您的设置详情和日志。
