# Basic Control

![use-case-pc-angled-view](images/product/use-case-pc-angled-view.jpg)

## 💻 Compatibility

- **Host Software**: Install our [host app](/app) for macOS, Windows, and Linux to control your target devices. Ensure your host system is compatible with the corresponding app version.
- **Target Device Compatibility**: No pre-installation or configuration is required on the target device. As long as the target device supports UI operations with video output (e.g., HDMI, VGA) and has a USB port to receive emulated keyboard and mouse control (HID) signals, it can be used. Supported target platforms include Windows, macOS, Linux, Android, and iOS.

## 🖱 Mouse Control

- **Absolute Mode**: The target's mouse cursor is mapped directly to a specific position on the host's screen via our app. This means that wherever you move the host's mouse within our app, the target's mouse will follow the same movement. Note that there might be a slight delay in the cursor movements. You can choose to hide or display the host's mouse cursor while it is on our app.

- **Relative Mode**: The target's mouse movement is relative to the current position of the host's mouse. This means that moving the host's mouse will shift the target's cursor by a certain distance in the same direction, without a fixed start or end point. You can exit this relative mode using a specific shortcut.

## ⌨️ Keyboard

When the app is focused, you can type anything directly, and these keystrokes will be passed to the target's computer.

## ⚙️ BIOS-Level Access

- **BIOS Access**: Use our app to access the BIOS of your target devices. This allows you to control and configure settings directly from the BIOS.

??? tip "Key strokes to enter BIOS for different motherboards"

    - F2: Dell, Lenovo, ASUS, Acer, Toshiba, Samsung, Sony
    - F1: Lenovo
    - Del: ASUS, Acer, Gigabyte, MSI
    - F10: HP
    - Assist button: Sony
    - Option (⌥) key: Apple (to access the start manager)

## 🔊 Sound

- **Audio Transmission**: The target computer's audio is transmitted via the HDMI input port of the mini-KVM. When using our app, the sound from the target computer will be played through the host computer, ensuring you hear everything seamlessly.

## 🎥 Video

- **Video Display**: Our app allows you to view the target computer's screen seamlessly. It supports video resolutions up to 1920x1080 at 30Hz for display within the app. The maximum video input supported is up to 3840x2160 at 30Hz via HDMI. Additionally, with the use of an adapter, it can also accommodate VGA, Micro HDMI, DVI, and other video input sources.

## 🔄 Switchable USB Port

- **Using the USB Port**: The mini-KVM features a switchable USB-A 2.0 port that can be toggled between the host and target computers, but not both simultaneously.
- **Switching Methods**: 
    - Hardware Switch: A physical toggle on the device
    - Software Switch: A button in the host application
- **Switch Logic**: For more detailed information on the logic of how the switchable USB port operates, including the interaction between hardware and software switches, initial setup, operational states, and state transitions, please refer to the [USB Switch documentation](usb-switch.md).

!!! warning "Important"
    - Remember to eject any connected USB drives before switching the port's connection.
    - The USB port has power limitations. Do not connect devices that require a lot of power, as this may result in unstable operation or potential damage.
