# How It Works

## Process Breakdown

- **Screen Streaming**: The mini-KVM captures the screen stream from the target computer and displays it on the host computer’s app. This allows users to view and manage the target system directly from their host machine.
- **Cursor and Mouse Control**: By moving the mouse to the app window on the host computer, users can control the cursor on the target device as if they were using a VNC. This functionality enables operating two systems simultaneously on one screen.
- **Keyboard Input**: When the app window is active, any keystrokes made on the host computer’s keyboard are transmitted to the target device, allowing for seamless typing and command entry.
- **HID Signal Conversion**: All keyboard and mouse inputs within the app are converted into Human Interface Device (HID) control signals, which are then sent to the target computer.
- **Synchronization**: The app ensures that the target computer’s screen and cursor are synchronized with the host computer’s display, facilitating a unified user experience.

You may explore Openterface Open-source [Software](/app) and [Hardware](/open-hardware) for more details.