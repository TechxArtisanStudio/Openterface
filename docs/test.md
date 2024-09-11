# Test & Dev

## 💻 Compatibility

- **OS Support**: Verify that different OS versions can use the corresponding host app.
- **Performance Testing**: Evaluate performance on various host systems.
- **OS Version Testing**: Ensure compatibility across different OS versions.
- **Device-Specific Issues**: Identify and resolve issues specific to certain devices or OS versions.

## 🖱 Mouse Control

<div class="annotate" markdown>

- **Movement Latency**: Ensure smooth and responsive control.
- **Mouse Buttons**: Test left, right, and middle mouse buttons; click & drag.
- **Scrolling**: Evaluate scrolling speed and direction.
- **Accuracy** of mouse position mapping in *Absolute* mode (1)
- **Sensitivity** of mouse movement in *Relative* mode (2)

</div>

1. Ensure the target's mouse position is accurately mapped to the host's. This can be impacted by the target's resolution and changes in app window size.
2. Ensure the mouse movement meets intuitive expectations.

## ⌨️ Keyboard

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

## ⚙️ BIOS-Level Access

- **BIOS Entry**: Test entering BIOS during the boot sequence.
- **Functionality**: Ensure full keyboard and mouse control within the BIOS.
- **Compatibility**: Verify BIOS access across different motherboard brands and models.

## 🔊 Sound

- **Sound Quality**: Evaluate the clarity and synchronisation of audio playback.
- **Latency**: Measure any delays between actions and their corresponding sound.
- **Compatibility**: Test various audio outputs on different operating systems.

## 🎥 Video

- **Resolution Support**: Test various screen resolutions and aspect ratios.
- **Frame Rate**: Assess performance at different refresh rates.
- **Display Quality**: Check for any visual artefacts or latency issues.

## 🔄 Switchable USB Port

- **Toggle Switch Testing**: Test the toggle switch under various scenarios for reliability.
- **Port Compatibility**: Ensure the USB-A 2.0 port supports various USB devices like flash drives and webcams.
- **Power Limitations**: Confirm the port’s power supply capacity and its adequacy for different devices.

## 🔌 Plug & Un-Plug

- **Connection Testing**: Test scenarios with different connection and disconnection sequences.
- **Error Handling**: Ensure device recognises and recovers from improper connections.
- **Stability**: Verify stability when devices are plugged and unplugged repeatedly.

## 📝 Text Transfer

- **Functionality Testing**: Verify that the host application can successfully transfer text from the host computer to the target device using ASCII codes.

- **Content Integrity**: Ensure the text content transferred from the host to the target device remains intact and is accurately reproduced.

- **Special Characters Handling**: Test the text transfer feature with various ASCII characters to ensure proper handling and reproduction on the target device.

- **Text Length Testing**: Test the text transfer feature with text of varying lengths to verify that it can accommodate different text sizes without issues.

- **Error Handling**: Test error scenarios, such as loss of connection or interruption during text transfer, to ensure the host application handles these situations gracefully and provides appropriate feedback to the user.

- **Performance Testing**: Evaluate the performance of the text transfer feature under various conditions, including on older or slower computers, to identify any potential issues with mis-receiving HID input signals and ensure smooth operation.

- **User Interface Testing**: Ensure the user interface of the host application provides intuitive controls and feedback for initiating and monitoring text transfer operations, making it easy for users to understand and use this feature effectively.

## Additional

- **Error Handling**: Test error handling mechanisms for graceful recovery from disruptions.
- **Performance**: Assess the mini-KVM’s performance under various workload scenarios.
- **Stability**: Conduct stress tests for long-term stability and reliability.