# Quick Start

## Product Overview

Our **Openterface Mini-KVM** is open-source app and device that allows to control two computers without the need for extra keyboard, mouse and monitor. 
It allows a macOS host to control a target device, compatible with Windows, macOS, Linux, Android, iOS.
It is designed to seamlessly integrate your workflow. It offers an efficient and clutter-free solution for managing multiple computers. 

## Connection

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

    
## Use Guidelines

* The mini-KVM captures screen streaming from the target computer and display on the app at the host computer;
* User can navigate mouse to the app windows at the host and start controlling the mouse cursor of the target device, just like VNC.
* When the app is focused, whatever user type via keyboard at the host also convert to the target device. 
* Keyboard and mouse inputs in the app are converted into Human Interface Device (HID) control signals for the target computer;
* The app aligns the target computer’s screen and cursor with the host computer's display.

## Advantages
* Plug-and-Play: No software installations or configurations are required on the target computer.
* Stable & Fast Control: wired solution is stable and fast.
* No Networks Required: Operates without network connectivity.
* No Residue: Leaves no software traces on the target computer after disconnection.

## Hardware Components
* Serial communication module: connected to the host via USB interface and bridging communication with CH9329 module.
* CH9329 chip: responsible to decode serial signals from the host computer into keyboard and mouse events, acted as a keyboard mouse simulator and controlling the target computer.
* HDMI Capture module: responsible to capture video signal of the target’s screen via HDMI cable, do video transcoding and deliver video steaming as a webcam-like signal to the host via USB interface.