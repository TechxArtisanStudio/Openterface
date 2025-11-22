# Software

To get your Openterface™ KVM gadgets up and running, you'll need to install one of the apps listed below on your host computer. You can grab these apps from different app platforms or just click the links provided. If you're feeling adventurous, you can also build them from source using our GitHub repositories!

![use-case-pc-angled-view](https://assets.openterface.com/images/product/use-case-pc-angled-view.webp){ width=600 }

## Download & Installation

<div class="grid cards" markdown>

-   ### :fontawesome-brands-windows:{ .lg } **Windows**

    ***

    Download or build from source for **Openterface QT Win**:

    [:octicons-download-24: Download {{qt_version}} Installer](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_windows_amd64_installer.exe) <br>
    [:octicons-download-24: Download {{qt_version}} Portable EXE](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_windows_amd64_portable.exe) <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) <br>
    [:octicons-play-24: Watch Demo](https://youtu.be/ERzpGtRvP2o?si=e9k402f0nxsD8o2j)

-   ### :fontawesome-brands-apple:{ .lg } **macOS**

    ***

    Download or build from source for **Openterface MacOS**:

    [:octicons-arrow-right-24: Install from App Store](/appstore) <br>
    [:octicons-download-24: Download portable DMG](macos/dmg-installation.md) <br>
    [:octicons-mark-github-16: Openterface_MacOS](https://github.com/TechxArtisanStudio/Openterface_MacOS) <br>
    [:octicons-play-24: Watch Demo](https://youtu.be/m7OpUem0zqY?si=tclfl0Jl77tmE6_e)

-   ### :fontawesome-brands-linux:{ .lg } **Linux**

    ***

    Download or build from source for **Openterface QT Linux**:

    [:octicons-download-24: Download {{qt_version}} AMD64 DEB](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_amd64.deb) <br>
    [:octicons-download-24: Download {{qt_version}} AMD64 RPM](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_amd64.rpm) <br>
    [:octicons-download-24: Download {{qt_version}} AMD64 AppImage](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_amd64.AppImage) <br>
    [:octicons-download-24: Download {{qt_version}} ARM64 DEB](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_arm64.deb) <br>
    [:octicons-download-24: Download {{qt_version}} ARM64 AppImage](https://github.com/TechxArtisanStudio/Openterface_QT/releases/download/{{qt_version}}/openterfaceQT_linux_arm64.AppImage) <br>
    [:octicons-mark-github-16: Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) <br>
    [:octicons-play-24: Watch Demo](https://youtu.be/_ScpI6TC0Pk?si=FSg7A2zmST8QbFec)

-   ### :fontawesome-brands-android:{ .lg } **Android**

    ***

    Download or build from source for **Android APK**:

    [:octicons-download-24: Download {{android_version}}](https://github.com/TechxArtisanStudio/Openterface_Android/releases/download/{{android_version}}/OpenterfaceAndroid-release.apk) <br>
    [:octicons-mark-github-16: Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) <br>
    [:octicons-play-24: Watch Demo](https://x.com/TechxArtisan/status/1825460088922071398)

</div>

???+ warning "Heads Up: Check Privacy & Security with Third-Party Apps"
Since all our apps are open source, you might come across alternative versions of host applications for Openterface devices created by others. They can be quite cool and may offer extra features, but here’s a friendly reminder: review their security and privacy practices carefully—especially because KVM control involves events from your screen, keyboard, and mouse. The Openterface Team cannot vouch for the safety of these third-party apps, so proceed with caution!

## Basic Host App Controls

### 💻 Compatibility

-   **Host Software**: Install our host app for macOS, Windows, or Linux.
-   **Target Devices**: No setup needed—just connect any device with video output (HDMI, VGA, etc.) and a USB port for keyboard/mouse control. Works with Windows, macOS, Linux, Android, and iOS.

### 🖱 Mouse Modes

-   **Absolute Mode**: Host mouse directly maps to target screen position.
-   **Relative Mode**: Moves target cursor relative to current position. Exit with a shortcut.

### ⌨️ Keyboard

Keystrokes from the host are sent directly to the target when the app is focused.

### ⚙️ BIOS Access

Control target BIOS directly.  
Common keys: F2 (Dell/Lenovo/ASUS), F10 (HP), Del (ASUS/Gigabyte/MSI), ⌥ (Apple).

### 🔊 Audio

Target audio streams through HDMI and plays on your host computer.

### 🎥 Video

View your target screen directly inside the app.

-   **Current Models:** Up to **1080p 30Hz** display in-app, with support for **4K 30Hz input** via HDMI.
-   **Other Inputs:** Compatible with VGA, DVI, Micro HDMI, and more when using appropriate adapters.
-   **Future Models:** Higher resolutions and frame rates will be supported as new hardware versions are released.

### 🔄 Switchable Ports

Some Openterface devices include ports that can be **switched between the host and target**, such as USB 2.0 ports or micro-SD card slots (on upcoming models).

-   **One-at-a-time Use:** Only one side (host or target) can access the port at a time.
-   **Switch Methods:**
    -   **Hardware toggle** — physical switch on the device
    -   **Software button** — control via the host app
-   **Important:**
    -   Safely eject storage devices (USB drives or micro-SD cards) before switching.
    -   Avoid connecting high-power devices to prevent instability or damage.
    -   See the [Switchable Ports Guide](/usb-switch) for details and logic diagrams.
