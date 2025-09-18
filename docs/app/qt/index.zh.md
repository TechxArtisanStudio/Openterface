# Openterface QT for Win & Linux

本文档提供了一个跨平台KVM（键盘、视频、鼠标）软件的概述，该软件使用Qt开发，兼容Linux和Windows操作系统。该软件便于从主机系统控制目标设备，通过其菜单栏和各种附加功能提供多种功能。

## 主菜单栏功能

### 首选项

首选项菜单允许用户通过包含四个页面的对话框自定义设置：<br>
![Preferences Gernal](https://assets.openterface.com/images/qt/preferenceGernal.webp)

-   **常规** 此页面配置调试日志过滤器和应用程序运行时是否禁止屏幕保护程序。日志类别包括：

    -   Core
    -   Serial
    -   UserInterface
    -   host

    用户可以选择将日志保存到.txt文件以及是否禁止屏幕保护程序。<br>

![Preferences Video](https://assets.openterface.com/images/qt/preferenceVideo.webp)

-   **视频** 此页面允许用户：

    -   选择要捕获哪个摄像头的数据。
    -   设置分辨率。
    -   选择视频流格式。

-   **音频** 此页面目前正在开发中。<br>

![Preferences TargetControl](https://assets.openterface.com/images/qt/preferenceTargetControl.webp)

-   **目标控制** 此页面提供配置目标设备控制模式的选项：

    -   **控制模式：**

        -   **键盘 + 鼠标 + USB HID设备**
        -   **USB键盘**
        -   **键盘 + 鼠标**
        -   **USB HID设备**

    -   **设置从目标读取的供应商ID（VID）和产品ID（PID）。**
    -   **定义目标的USB描述符。**

### 编辑

-   **粘贴：** 编辑菜单中的粘贴选项和左上角的粘贴按钮都允许用户将主机剪贴板中的文本粘贴到目标设备。

### 控制

此菜单提供以下选项：<br>

-   设置鼠标移动模式：绝对或相对。**控制 >> 鼠标模式 >> 绝对或相对。**
-   切换主机鼠标光标的可见性。**控制 >> 鼠标可见性 >> 自动隐藏或始终显示。**
-   在硬件上切换USB端口在目标和主机使用之间。**控制 >> 可切换USB >> 到目标或到主机。**
-   调整芯片传输的波特率。**控制 >> 波特率 >> 9600, 115200。**

### 高级

高级菜单包括以下选项：<br>
![Advance menu](https://assets.openterface.com/images/qt/menuAdvance.webp)

-   **环境检查：** 验证软件所需的驱动程序是否已安装。
-   **重置串口：** 重启串口。
-   **重置键盘和鼠标：** 重置键盘和鼠标设置。
-   **恢复出厂设置HID芯片：** 将HID芯片恢复到出厂设置。<br>
    ![Advance SerialConsole](https://assets.openterface.com/images/qt/advanceSerialConsole.webp)
-   **串口控制台：** 打开新窗口监控发送到串口的所有消息，具有发送/接收消息过滤器。<br>
    ![Advance ScriptTool](https://assets.openterface.com/images/qt/advanceScriptTool.webp)
-   **脚本工具：** 运行AutoHotkey（AHK）脚本。此功能模拟AutoHotkey，但仅支持鼠标/键盘功能和截图功能的子集。脚本影响目标设备。
-   **TCP服务器：** 通过TCP接收AutoHotkey命令以在目标设备上执行它们。
-   **固件更新：** 从远程服务器拉取最新固件，允许用户选择是否将其刷写到设备。

### 语言

界面语言可设置为：

-   丹麦语
-   英语
-   德语
-   法语
-   日语
-   瑞典语

### 帮助

帮助菜单提供：<br>
![Help menu](https://assets.openterface.com/images/qt/menuHelp.webp)

-   软件/硬件问题的官方网站和反馈表单链接。
-   购买硬件的信息。
-   软件环境的描述。
-   关于：组织详情。
-   更新：检查软件更新。

## 菜单栏功能（从左到右）

菜单栏从左到右包括以下功能：<br>

![MenuBar](https://assets.openterface.com/images/qt/menubar.webp)

-   键盘布局选择：选择键盘布局。
-   缩放控制：放大、缩小或重置捕获视频流的显示。
-   虚拟键盘：包括功能键和预设快捷键组合。
-   截图：捕获整个目标屏幕并保存到默认文件夹。
-   全屏模式：切换全屏显示。
-   粘贴：将主机剪贴板中的文本粘贴到目标。
-   鼠标舞蹈：触发鼠标执行预设移动。
-   USB设备指示器：显示USB设备是否分配给目标或主机。

同时，欢迎探索我们的开源**GitHub仓库**：[Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) 获取最新代码、更新、示例和报告问题。

您也可以加入我们的[Discord社区](/discord) 与我们的开发团队和其他优秀用户联系，讨论任何KVM相关话题。

如需直接支持，请随时通过 [support@openterface.com](mailto:support@openterface.com) 联系我们。

---

**对此页面有反馈？** [请在此处告知我们。](https://forms.gle/wmxoR2C1VdG36mT69)
