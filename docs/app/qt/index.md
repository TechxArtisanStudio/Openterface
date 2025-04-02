# Openterface QT for Win & Linux

This document provides an overview of a cross-platform KVM (Keyboard, Video, Mouse) software developed using Qt, compatible with both Linux and Windows operating systems. The software facilitates control over a target device from a host system, offering a variety of features accessible through its menu bar and additional functionalities.

## Main Menu Bar Features

### Preferences

The Preferences menu allows users to customize settings via a dialog with four pages:<br>
![Preferences Gernal](/docs//images/qt/preferenceGernal.png)
- **General** This page configures debugging logs filter and the screen saver inhibit or not when the application is running. Log categories include:
  - Core
  - Serial
  - UserInterface
  - host

  Users can choose to save logs to a .txt file and the screen saver inhibit or not.<br>

![Preferences Video](/docs//images/qt/preferenceVideo.png)
- **Video** This page enables users to:
  - Select which camera's data to capture.
  - Set the resolution.
  - Choose the video stream format.

- **Audio** This page is currently under development.<br>
![Preferences TargetControl](/docs//images/qt/preferenceTargetControl.png)
- **Target Control** This page provides options to configure control modes for the target device:
  - **Control modes:**
    - **Keyboard + Mouse + USB HID device**
    - **USB keyboard**
    - **Keyboard + Mouse**
    - **USB HID device**

  - **Set the Vendor ID (VID) and Product ID (PID) read from the target.**
  - **Define the USB descriptor for the target.**

### Edit
- **Paste:** Both the Paste option in the Edit menu and the paste button in the top-left corner allow users to paste text from the host clipboard to the target device.

### Control
This menu provides options to:<br>
  
  - Set mouse movement modes: Absolute or Relative.  **Control >> MouseMode >> Absolute or Relative.**
  - Toggle visibility of the host's mouse cursor. **Control >> Mouse Visibility >> Auto Hide or Always Show.**
  - Switch a USB port on the hardware between target and host usage. **Control >> Switchable USB >> TO Target or To Host.**
  - Adjust the baud rate for chip transmission. **Control >> Baudrate >> 9600, 115200.**

### Advance
The Advance menu includes the following options:<br>
  ![Advance menu](/docs//images/qt/menuAdvance.png)
  - **Environment Checking:** Verifies if required drivers for the software are installed.
  - **Reset Serial Port:** Restarts the serial port.
  - **Reset Keyboard and Mouse:** Resets the keyboard and mouse settings.
  - **Factory Reset HID Chip:** Restores the HID chip to its factory settings.<br>
  ![Advance SerialConsole](/docs//images/qt/advanceSerialConsole.png)
  - **Serial Console:** Opens a new window to monitor all messages sent to the serial port, with filters for sent/received messages.<br>
  ![Advance ScriptTool](/docs//images/qt/advanceScriptTool.png)
  - **Script Tool:** Runs AutoHotkey (AHK) scripts. This feature mimics AutoHotkey but supports only a subset of mouse/keyboard functions and screenshot capabilities. Scripts affect the target device.
  - **TCP Server:** Receives AutoHotkey commands via TCP to execute them on the target device.
  - **Firmware Update:** Pulls the latest firmware from a remote server, allowing users to choose whether to flash it to the device.

### Languages
The interface language can be set to:
- Danish
- English
- German
- French
- Japanese
- Swedish

### Help
The Help menu provides: <br>
![Help menu](/docs//images/qt/menuHelp.png)
- Links to the official website and feedback forms for software/hardware issues.
- Information on purchasing hardware.
- A description of the software’s environment.
- About: Details about the organization.
- Update: Checks for software updates.


## Menu Bar Functions (Left to Right)
The menu bar, from left to right, includes the following functionalities:<br>

![MenuBar](/docs//images/qt/menubar.png)
- Keyboard Layout Selection: Choose the keyboard layout.
- Zoom Controls: Zoom in, zoom out, or reset the display of the captured video stream.
- Virtual Keyboard: Includes function keys and preset shortcut combinations.
- Screenshot: Captures the entire target screen and saves it to a default folder.
- Full-Screen Mode: Toggles full-screen display.
- Paste: Pastes text from the host clipboard to the target.
- Mouse Dance: Triggers the mouse to perform preset movements.
- USB Device Indicator: Displays whether a USB device is assigned to the target or host.

In the meantime, feel free to explore our open-source **GitHub repository**: [Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) for the latest code, updates, examples, and to report issues.

You can also join our [Discord community](/discord) to connect with our dev team and other awesome users to discuss any KVM-related topics.

For direct support, feel free to email us at [support@openterface.com](mailto:support@openterface.com).
