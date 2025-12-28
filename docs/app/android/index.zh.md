# Openterface Android

## 概述

Openterface Mini-KVM 是一个开源硬件和软件解决方案，旨在通过基于 Android 的界面提供基本的 KVM（键盘、视频、鼠标）功能来控制设备。此仓库包含 Android 应用程序源代码、构建配置和支持脚本来设置和部署项目。

我们致力于开源硬件和开源软件，采用 [GNU Affero General Public License v3](https://github.com/TechxArtisanStudio/Openterface_Android/blob/main/LICENSE)。

## 功能模块

### 1. 视频显示

#### 主要功能

-   将连接的目标设备的视频输出实时流式传输到 Android 屏幕。
-   支持图像调整以获得最佳观看效果。

![image](https://assets.openterface.com/images/android/videoConnect.webp)

#### 用户界面描述

-   主屏幕显示目标设备的视频源，占据界面的大部分。
-   侧边工具栏提供调整控制（亮度、对比度、色调）。

#### 操作流程

1. 通过 HDMI 和 USB 将 Mini-KVM 硬件连接到目标设备。
2. 通过 USB-C 将 Mini-KVM 插入您的 Android 设备。
3. 启动应用程序；视频源会自动出现。
4. 使用工具栏滑块根据需要调整亮度、对比度或色调。

![image](https://assets.openterface.com/images/android/colorSetting.webp)

#### 特殊功能

-   双指缩放使显示效果更好

![image](https://assets.openterface.com/images/android/enlargeAndSideBar.webp)

---

### 2. 鼠标控制

#### 主要功能

-   提供绝对和相对鼠标控制来与目标设备的界面交互。
-   支持左键和右键点击。
-   从右侧菜单选择模式。

#### 用户界面描述

-   视频源兼作鼠标输入的触摸板。
-   浮动操作按钮（FAB）在鼠标和键盘模式之间切换。

#### 操作流程

1. 确保设备连接成功。
2. 点击屏幕将鼠标光标移动到该位置（绝对控制）。
3. 单指双击为左键点击，双指点击为右键点击。
4. 拖拽模式是按住左键不松开。

#### 特殊功能

-   相对鼠标控制（开发中，可用时通过设置切换）。

## ![image](https://assets.openterface.com/images/android/mouseThouchMode.webp)

### 3. 键盘输入

#### 主要功能

-   通过点击键盘按键向设备输入。

#### 用户界面描述

-   键盘图标位于右下角。
-   键盘包括快捷键、系统键、标准键和功能键（F1-F12）。

#### 操作流程

1. 点击右下角的键盘图标调出键盘。
2. 根据需要输入文本或按功能键。

#### 特殊功能或快捷键

-   **快捷键**：Ctrl+C、Ctrl+V、Ctrl+Z、Ctrl+X、Ctrl+A、Ctrl+S、
    Win+Tab、Win+S、Win+E、Win+R、Win+D、Win+L、Alt+F4、Ctrl+Alt+Del、Alt+PrtScr。
-   **功能键**：F1-F12、符号键。
-   **标准键**：0-9、A-Z、Enter、Space、delete。

![image](https://assets.openterface.com/images/android/enlargeAndKeyBoard.webp)
![image](https://assets.openterface.com/images/android/keyBoardFunction.webp)
![image](https://assets.openterface.com/images/android/keyBoardSystem.webp)

---

同时，欢迎探索我们的开源 **GitHub 仓库**：[Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) 获取最新代码、更新、示例，并报告问题。

您也可以加入我们的 [Discord 社区](/discord) 与我们的开发团队和其他优秀用户联系，讨论任何与 KVM 相关的话题。

如需直接支持，请随时通过 [support@openterface.com](mailto:support@openterface.com) 给我们发邮件。

---

**对此页面有反馈？** [请在此处告诉我们。](https://forms.gle/wmxoR2C1VdG36mT69)

