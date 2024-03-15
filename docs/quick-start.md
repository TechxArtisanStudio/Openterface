# Quick Start

## Product Overview

Our **Openterface™ Mini-KVM** allows you to control a nearby headless computer (which we refer to as the **Target**) directly from your own laptop or desktop (referred to as the **Host**), via usb and HDMI connection, without the need for an extra keyboard, mouse, monitor or network.

We’re starting our official crowdfunding campaign on **Crowd Supply** soon for the Openterface mini-KVM, and we're eager to make it a success. By subscribing to the [pre-launch]((https://www.crowdsupply.com/techxartisan/openterface-mini-kvm)) and being our backer, you'll bring us closer to our goal and, ultimately, to delivering Mini-KVM Openterface to you faster. 

Stay tuned for updates and [join our community](https://www.reddit.com/r/Openterface_miniKVM/) to be part of this exciting journey! ❤️


## Why Openterface Mini-KVM ?

Whether you're an IT professional troubleshooting servers, a developer orchestrating multiple test environments on edge computing devices, a tech enthusiast exploring single-board computers, or someone keen on decluttering their workspace, the Openterface Mini-KVM offers a versatile solution tailored to your needs.

Embrace efficiency and simplicity with our innovative approach to managing your technological environment. 🎉

## Product Features

- **Host App Compatibility**: Currently supports macOS, with support for Windows and Linux in development.

- **Plug-and-Play Convenience**: Headless control via HDMI and emulated keyboard/mouse, without network concern.

- **Portability**: Its compact and lightweight design makes it the perfect tool for professionals on the go.

- **Text Transfer from Host to Target**: Ideal for copying usernames, passwords, and small chunks of code to the target computer via our host applications.

- **Full HD with Low Latency**: Captures video via HDMI at a 1920x1080 resolution at 30fps, with under 140 milliseconds of latency. With the help of a video adapter, it can also support DisplayPort and DVI video sources.

- **Audio Integration**: Captures and plays the target device's audio directly on the host computer.

- **BIOS-Level Access**: Provides direct access to the target device's BIOS, firmware, or startup management.

- **Switchable USB Type-A Port**: This allows you to toggle USB access between the host and the target, ideal for sharing a USB drive without replugging.

- **Clean Setup**: Leaves no software on the target computer.


## Connection
![Type-C to Host](images/product/connection_demo.png)
The Openterface Mini-KVM features ports on both black and orange ends:

![Type-C to Host](images/type-c-to-host-2.svg)
:   A Type-C port for connecting to the host device.

![Type-C to Target](images/type-c-to-target-2.svg)
:   A Type-C port to connect to the target device.

![HDMI Port](images/hdmi-port-2.svg)
:   An HDMI input port to capture screen streaming from the target device.

![Switchable USB-A Port](images/switchable-usb-a-port-2.svg)
:   A USB-A 2.0 port, switchable between the host and target device.

![Switcher](images/switcher-2.svg)
:   A switcher to toggle the USB-A port's connection between the host or target device.

## Host Applications

The host computer needs to install our host application to use this device, while the target device requires no pre-installation. 

It is compatible with any target device that has an HDMI output and can receive USB-emulated HID signals. Therefore, the target device can be Windows, macOS, Linux, Android, iOS.

The host application has not yet reached a stable release. The macOS version is nearly complete, while support for Windows and Linux remains in development. We are diligently coding as we speak! 💪🛠️🚀

## Open Source

 In line with our belief in community collaboration, we plan to open source our host application. We hope this will inspire like-minded individuals to join us in perfecting Mini-KVM Openterface. 👨‍💻🤝👩‍💻

## How It Works

* The mini-KVM captures the screen stream from the target computer and displays it on the app on the host computer.
* Users can move the mouse to the app window on the host and start controlling the mouse cursor of the target device, similar to VNC, operating two systems simultaneously on one screen.
* When the app is focused, whatever users type via the keyboard on the host is also transmitted to the target device.
* Keyboard and mouse inputs in the app are converted into Human Interface Device (HID) control signals for the target computer.
* The app synchronizes the target computer’s screen and cursor with the display of the host computer.