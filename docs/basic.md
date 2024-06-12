---
comments: true
---

# Basic KVM Control

## Host App Demos

### Windows App
<iframe width="560" height="315" src="https://www.youtube.com/embed/ERzpGtRvP2o?si=2DQrHqk-GhzvvL24" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Linux App
<iframe width="560" height="315" src="https://www.youtube.com/embed/_ScpI6TC0Pk?si=nQuAAwpm5ipvx9yn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### MacOS App
<iframe width="560" height="315" src="https://www.youtube.com/embed/m7OpUem0zqY?si=3kHl1kmk6VQRnPu7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Compatibility 💻

=== "Users"

    - **Host Software**: Install our [host app](/quick-start/#install-host-application) for macOS, Windows, and Linux to control your target devices. Ensure your host system is compatible with the corresponding app version.
    - **Target Device Compatibility**: No pre-installation or configuration is required on the target device. As long as the target device supports UI operations with video output (e.g., HDMI, VGA) and has a USB port to receive emulated keyboard and mouse control (HID) signals, it can be used. Supported target platforms include Windows, macOS, Linux, Android, and iOS.

=== "🛠️ Test & Dev"

    - **OS Support**: Verify that different OS versions can use the corresponding host app.
    - **Performance Testing**: Evaluate performance on various host systems.
    - **OS Version Testing**: Ensure compatibility across different OS versions.
    - **Device-Specific Issues**: Identify and resolve issues specific to certain devices or OS versions.

## Mouse Control 🖱

=== "Users"

    - **Absolute Mode**: The target’s mouse cursor is mapped directly to a specific position on the host’s screen via our app. This means that wherever you move the host’s mouse within our app, the target’s mouse will follow the same movement. Note that there might be a slight delay in the cursor movements. You can choose to hide or display the host’s mouse cursor while it is on our app.

    - **Relative Mode**: The target’s mouse movement is relative to the current position of the host’s mouse. This means that moving the host’s mouse will shift the target’s cursor by a certain distance in the same direction, without a fixed start or end point. You can exit this relative mode using a specific shortcut.

=== "🛠️ Test & Dev"

    <div class="annotate" markdown>

    - **Movement Latency**: Ensure smooth and responsive control.
    - **Mouse Buttons**: Test left, right, and middle mouse buttons; click & drag.
    - **Scrolling**: Evaluate scrolling speed and direction.
    - **Accuracy** of mouse position mapping in *Absolute* mode (1)
    - **Sensitivity** of mouse movement in *Relative* mode (2)
    
    </div>

    1. Ensure the target's mouse position is accurately mapped to the host's. This can be impacted by the target's resolution and changes in app window size.
    2. Ensure the mouse movement meets intuitive expectations.


## Keyboard ⌨️

=== "Users"

    When the app is focused, you can type anything directly, and these keystrokes will be passed to the target’s computer.

=== "🛠️ Test & Dev"

    <div class="annotate" markdown>

    - **Typing Responsiveness**: Ensure it meets intuitive expectations.
    - **Full Keyboard Mapping**: Especially for various special symbols.
    - **Modifiers**: Keys like `Ctrl`, `Shift`, `Alt` and `Cmd`, or `Win`.
    - **Key Combinations**: Technically supports up to 8 modifier keys and 6 additional keys pressed simultaneously.
    - **Media & ACPI Keys**: Keys like `Volume-`, `Volume+`, `Mute`, `Wake-up`, `Sleep` and `Power`.
    - **Keyboard Layouts**: Ensure consistent pairing for various layouts. (1)

    !!! tip

        - **Keyboard Tester**: You can utilize an online keyboard testing tool on both the host and target computers to verify whether their keystrokes are synchronized.
        - **CH9329 Chip**: Check [the details](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/CH9329) to understand the limits of keyboard/mouse control in the Openterface Mini-KVM.

    </div>

    1. ⌨️ 🌏 Keyboard layouts vary globally across regions and languages, with popular types like QWERTY, AZERTY, QWERTZ, and Dvorak.


## BIOS-Level Access ⚙️
=== "Users"

    - **BIOS Access**: Use our app to access the BIOS of your target devices. This allows you to control and configure settings directly from the BIOS.

    ??? tip "Key strokes to enter BIOS for different motherboards"

        - F2: Dell, Lenovo, ASUS, Acer, Toshiba, Samsung, Sony
        - F1: Lenovo
        - Del: ASUS, Acer, Gigabyte, MSI
        - F10: HP
        - Assist button: Sony
        - Option (⌥) key: Apple (to access the start manager)

=== "🛠️ Test & Dev"

    - **BIOS Entry**: Test entering BIOS during the boot sequence.
    - **Functionality**: Ensure full keyboard and mouse control within the BIOS.
    - **Compatibility**: Verify BIOS access across different motherboard brands and models.

## Sound 🔊

=== "Users"

    - **Audio Transmission**: The target computer’s audio is transmitted via the HDMI input port of the mini-KVM. When using our app, the sound from the target computer will be played through the host computer, ensuring you hear everything seamlessly.

=== "🛠️ Test & Dev"

    - **Sound Quality**: Evaluate the clarity and synchronisation of audio playback.
    - **Latency**: Measure any delays between actions and their corresponding sound.
    - **Compatibility**: Test various audio outputs on different operating systems.

## Video 🎥

=== "Users"

    - **Video Display**: Our app allows you to view the target computer’s screen seamlessly. It supports video resolutions up to 1920x1080 at 30Hz for display within the app. The maximum video input supported is up to 3840x2160 at 30Hz via HDMI. Additionally, with the use of an adapter, it can also accommodate VGA, Micro HDMI, DVI, and other video input sources.

=== "🛠️ Test & Dev"

    - **Resolution Support**: Test various screen resolutions and aspect ratios.
    - **Frame Rate**: Assess performance at different refresh rates.
    - **Display Quality**: Check for any visual artefacts or latency issues.

## Switchable USB Port & Its Toggle Switch 🔄

=== "Users"

    - **Using the USB Port**: Only one computer can utilise the USB port at a time. Toggle the switch to change the port’s connection to another computer.

    ??? note "Remember to eject the flash drive before toggling the switch"
        If the USB port is being used by a flash drive, ensure you eject the flash drive before toggling the switch to transfer the port’s use to another computer.

    ??? warning "Power supply limitation at around 5V2A"
        The USB port provides 5V power to an external USB device but has a limited power supply capacity of approximately 10W. This may not be sufficient to power certain external devices, such as a Jetson Nano running GPU-intensive tasks.

=== "🛠️ Test & Dev"

    - **Toggle Switch Testing**: Test the toggle switch under various scenarios for reliability.
    - **Port Compatibility**: Ensure the USB-A 2.0 port supports various USB devices like flash drives and webcams.
    - **Power Limitations**: Confirm the port’s power supply capacity and its adequacy for different devices.

## Plug & Un-Plug 🔌

=== "Users"

    - **Connection Sequence**: Follow the recommended device connection sequence for optimal performance. This helps in maintaining a stable connection and ensuring smooth operation.

=== "🛠️ Test & Dev"

    - **Connection Testing**: Test scenarios with different connection and disconnection sequences.
    - **Error Handling**: Ensure device recognises and recovers from improper connections.
    - **Stability**: Verify stability when devices are plugged and unplugged repeatedly.

# Additional

=== "Users"

    - **User Interface**: The host application interface is designed to be intuitive and user-friendly, providing easy access to essential features and settings.
    - **Documentation**: Review the user manuals and documentation for clear instructions on setup, operation, and troubleshooting.

=== "🛠️ Test & Dev"

    - **Error Handling**: Test error handling mechanisms for graceful recovery from disruptions.
    - **Performance**: Assess the mini-KVM’s performance under various workload scenarios.
    - **Stability**: Conduct stress tests for long-term stability and reliability.