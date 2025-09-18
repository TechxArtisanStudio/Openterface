# 软件

要让您的Openterface™ KVM设备运行起来，您需要在主机上安装下面列出的应用程序之一。您可以从不同的应用平台获取这些应用，或者直接点击提供的链接。如果您喜欢冒险，也可以使用我们的GitHub仓库从源代码构建它们！

![use-case-pc-angled-view](https://assets.openterface.com/images/product/use-case-pc-angled-view.webp){ width=600 }

## 下载与安装

<div class="grid cards" markdown>

-   ### :fontawesome-brands-windows:{ .lg } __Windows__

    ---

    下载或从源代码构建**Openterface QT Win**：

    [:octicons-download-24: 下载 {{qt_version}} 安装程序](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.windows.amd64.installer.exe)  <br>
    [:octicons-download-24: 下载 {{qt_version}} 便携版EXE](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT-portable.exe)  <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT)  <br>
    [:octicons-play-24: 观看演示](https://youtu.be/ERzpGtRvP2o?si=e9k402f0nxsD8o2j)

-   ### :fontawesome-brands-apple:{ .lg } __macOS__

    ---

    下载或从源代码构建**Openterface MacOS**：

    [:octicons-arrow-right-24: 从App Store安装](/appstore) <br>
    [:octicons-download-24: 下载便携版DMG](macos/dmg-installation.md) <br>
    [:octicons-mark-github-16: Openterface_MacOS](https://github.com/TechxArtisanStudio/Openterface_MacOS) <br>
    [:octicons-play-24: 观看演示](https://youtu.be/m7OpUem0zqY?si=tclfl0Jl77tmE6_e)

-   ### :fontawesome-brands-linux:{ .lg } __Linux__

    ---

    下载或从源代码构建**Openterface QT Linux**：

    [:octicons-download-24: 下载 {{qt_version}} AMD64 DEB](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.linux.amd64.deb)  <br>
    [:octicons-download-24: 下载 {{qt_version}} AMD64 RPM](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.linux.amd64.rpm)  <br>
    [:octicons-download-24: 下载 {{qt_version}} AMD64 AppImage](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.linux.amd64.AppImage)  <br>
    [:octicons-download-24: 下载 {{qt_version}} ARM64 DEB](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.linux.arm64.deb)  <br>
    [:octicons-download-24: 下载 {{qt_version}} ARM64 RPM](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT.linux.arm64.rpm)  <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT)  <br>
    [:octicons-play-24: 观看演示](https://youtu.be/_ScpI6TC0Pk?si=FSg7A2zmST8QbFec)

-   ### :fontawesome-brands-android:{ .lg } __Android__

    ---

    下载或从源代码构建**Android APK**：

    [:octicons-download-24: 下载 {{android_version}}](https://github.com/TechxArtisanStudio/Openterface_Android/releases/download/{{android_version}}/OpenterfaceAndroid-release.apk)  <br>
    [:octicons-mark-github-16: Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android)  <br>
    [:octicons-play-24: 观看演示](https://x.com/TechxArtisan/status/1825460088922071398)

</div>

???+ warning "注意：使用第三方应用时请检查隐私与安全"
    由于我们所有的应用都是开源的，您可能会遇到其他人为Openterface设备创建的替代版本主机应用程序。它们可能很酷，并提供额外功能，但这里有一个友好的提醒：仔细审查它们的安全和隐私实践——特别是因为KVM控制涉及来自您屏幕、键盘和鼠标的事件。Openterface团队无法为这些第三方应用的安全性担保，所以请谨慎行事！

## 基本主机应用控制

### 💻 兼容性

- **主机软件**：为macOS、Windows或Linux安装我们的主机应用。
- **目标设备**：无需设置——只需连接任何具有视频输出（HDMI、VGA等）和USB端口用于键盘/鼠标控制的设备。适用于Windows、macOS、Linux、Android和iOS。

### 🖱 鼠标模式

- **绝对模式**：主机鼠标直接映射到目标屏幕位置。
- **相对模式**：相对于当前位置移动目标光标。通过快捷键退出。

### ⌨️ 键盘
当应用获得焦点时，来自主机的按键直接发送到目标。

### ⚙️ BIOS访问
直接控制目标BIOS。
常用键：F2（Dell/Lenovo/ASUS）、F10（HP）、Del（ASUS/Gigabyte/MSI）、⌥（Apple）。

### 🔊 音频
目标音频通过HDMI流传输并在您的主机上播放。

### 🎥 视频
直接在应用内查看您的目标屏幕。

- **当前型号**：应用内显示最高**1080p 30Hz**，支持通过HDMI输入**4K 30Hz**。
- **其他输入**：使用适当的适配器时兼容VGA、DVI、Micro HDMI等。
- **未来型号**：随着新硬件版本的发布，将支持更高的分辨率和帧率。

### 🔄 可切换端口
一些Openterface设备包括可以在**主机和目标之间切换**的端口，如USB 2.0端口或micro-SD卡插槽（在即将推出的型号上）。

- **一次使用一个**：一次只能有一侧（主机或目标）访问端口。
- **切换方法**：
    - **硬件切换** — 设备上的物理开关
    - **软件按钮** — 通过主机应用控制
- **重要**：
    - 切换前安全弹出存储设备（USB驱动器或micro-SD卡）。
    - 避免连接高功率设备以防止不稳定或损坏。
    - 有关详细信息和逻辑图，请参阅[可切换端口指南](/usb-switch)。
