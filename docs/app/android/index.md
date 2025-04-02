# Openterface Android

## Overview

Openterface Mini-KVM is an open-source hardware and software solution designed to provide basic KVM (Keyboard, Video, Mouse) functionality for controlling devices via an Android-based interface. This repository contains the Android application source code, build configurations, and supporting scripts to set up and deploy the project.

We are committed to open hardware and open-source software, licensed under the [GNU Affero General Public License v3](LICENSE).
## Feature Modules

### 1. Video Display
#### Main Functionality
- Streams video output from the connected target device to the Android screen in real-time.
- Supports image adjustments for optimal viewing.

![image](docs/images/android/videoConnect.jpg)

#### User Interface Description
- The main screen displays the target device's video feed, occupying most of the interface.
- A toolbar at the side provides adjustment controls (brightness, contrast, hue).

#### Operation Flow
1. Connect the Mini-KVM hardware to the target device via HDMI and USB.
2. Plug the Mini-KVM into your Android device via USB-C.
3. Launch the app; the video feed appears automatically.
4. Use the toolbar sliders to adjust brightness, contrast, or hue as needed.

![image](docs/images/android/colorSetting.jpg)

#### Special Features
- Pair-finger zooming makes the display look better

![image](docs/images/android/enlargeAndSideBar.jpg)

---

### 2. Mouse Control
#### Main Functionality
- Provides absolute and relative mouse control to interact with the target device’s interface.
- Supports left and right clicks.
- Select mode from the right menu.

#### User Interface Description
- The video feed doubles as a touchpad for mouse input.
- A floating action button (FAB) toggles between mouse and keyboard modes.

#### Operation Flow
1. Make sure the device is connected successfully.
2. Tap the screen to move the mouse cursor to that position (absolute control).
3. Double-click with one finger for left click, Two-finger click for right click.
4. The drag mode is to hold down the left button without releasing it.

#### Special Features
- Relative mouse control (in development, toggle via settings when available).

![image](docs/images/android/mouseThouchMode.jpg)
---

### 3. Keyboard Input
#### Main Functionality
- Allows text input to the target device via an on-screen keyboard.

#### User Interface Description
- A keyboard icon in the FAB toggles the on-screen keyboard overlay.
- The keyboard includes standard keys and function keys (F1-F12).

#### Operation Flow
1. Tap the keyboard FAB to bring up the on-screen keyboard.
2. Type text or press function keys as needed.

#### Special Features or Shortcuts
- **F1-F12 Keys**: Accessible via a dedicated row on the keyboard.
- **Ctrl+Alt+Del**: Tap a shortcut button on the keyboard overlay.

![image](docs/images/android/enlargeAndKeyBoard.jpg)

---

In the meantime, feel free to explore our open-source **GitHub repository**: [Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) for the latest code, updates, examples, and to report issues.

You can also join our [Discord community](/discord) to connect with our dev team and other awesome users to discuss any KVM-related topics.

For direct support, feel free to email us at [support@openterface.com](mailto:support@openterface.com).
