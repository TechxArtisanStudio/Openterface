---
comments: true
---

# Basic Operation Tests

## Mouse 🖱

- Absolute & Relative Mode
    - Movement latency, to ensure smooth and responsive control.
    - Accuracy of mouse position mapping
    - Click test (single click, double clicks)
    - Drag test

## Keyboard ⌨️
- Keyboard mapping test, especially for various special symbols
- Typing responsive test
- Multi-key press test
- Function key test
- Testing with different country keyboard layouts to ensure consistent pairing

!!! tip

    You can utilize online keyboard testing tool on both the host and target computers to verify whether their keystrokes are synchronized.

## Text Transfer 📝
- Text Transfer Functionality: Verify that the host application can successfully transfer text from the host computer to the target device using [ASCII codes](https://theasciicode.com.ar/).
- Content Integrity: Ensure that the text content transferred from the host to the target device remains intact and is accurately reproduced.
- Special Characters Handling: Test the text transfer feature with various ASCII characters, including symbols, punctuation marks, and non-alphanumeric characters, to ensure proper handling and reproduction on the target device.
- Text Length Testing: Test the text transfer feature with text of varying lengths, ranging from short strings to longer paragraphs, to verify that it can accommodate different text sizes without issues.
- Error Handling: Test error scenarios, such as loss of connection or interruption during text transfer, to ensure that the host application handles these situations gracefully and provides appropriate feedback to the user.
- Performance Testing: Evaluate the performance of the text transfer feature under various conditions, including on older or slower computers, to identify any potential issues with mis-receiving HID input signals and ensure smooth operation.
- User Interface Testing: Ensure that the user interface of the host application provides intuitive controls and feedback for initiating and monitoring text transfer operations, making it easy for users to understand and use this feature effectively.

!!! note
    The text transfer feature is designed to emulate typing behavior to reproduce text content on the target computer. It does not support clipboard integration, thus, it cannot transfer non-textual content, such as images. This feature exclusively supports transferring text based on ASCII codes. Therefore, it does not support languages that are not based on ASCII codes, such as Chinese, Japanese, Korean characters, etc. Additionally, it is not recommended to transfer too much text at one time.

## BIOS-Level Access ⚙️
- Whether the app can access to BIOS of different target device.

## Sound 🔊
- Whether the sound from the target computer can be played normally on the controlling computer

## Video 🎥
- Whether the app can display the target computer properly with different resolutions and frequencies

## Plug & Un-Plug 🔌
- Recommended device connection sequence
- Disrupting the sequence according to the above recommendations, testing different scenarios to ensure normal operation

## Switchable USB Port & Its Toggle Switch 🔄
- Toggle Switch Testing: Test the toggle switch under various scenarios to ensure it operates reliably and effectively switches between host and target computer connections.
- Port Compatibility: Verify that the USB-A 2.0 port supports connection with both the host and target computers as intended for various USB devices, such as a flash drive or webcam.


!!! note

    Only one computer can use the port at a time. If the port is being used by a flash drive, make sure to eject the flash drive before toggling the switch to switch the port's use to another computer.

!!! warning
    The USB port can provide 5V power to an external USB device, but it has a very limited power supply capacity, approximately 10W. Be aware that this may not be sufficient to power certain external devices, such as a Jetson Nano running GPU-intensive tasks.

## Different Target 💻🎯
- Testing different target devices, such as different versions of macOS, Windows, Linux, Android, iOS, etc.

## Different Host 💻👑
- Testing our currently released internal test software, such as supported versions for macOS, Windows, or Linux
- Testing whether different OS versions can use the corresponding host app

# Additional Tests
- User Interface Testing: Verify that the user interface of the host applications is intuitive and user-friendly, providing easy access to essential features and settings.
- Error Handling Testing: Test error handling mechanisms to ensure graceful recovery from unexpected situations, such as connection disruptions or device malfunctions.
- Documentation Review: Review user manuals and documentation to ensure they are comprehensive, accurate, and easy to understand, providing clear instructions for setup, operation, and troubleshooting.
- Performance Testing: Evaluate the performance of the mini-KVM device under various workload scenarios to ensure it meets the required performance standards and does not degrade system performance during operation.
- Stability Testing: Conduct stress tests and long-duration tests to assess the stability and reliability of the mini-KVM device under continuous use.