# Work In Progress

## Product Overview

Our **Openterface Mini-KVM** is designed to seamlessly integrate your workflow. It allows a host device (currently compatible with macOS) to control a target device (compatible with Windows, macOS, Linux, Android, iOS). By eliminating the need for extra keyboards, mice, and monitors, it offers an efficient and clutter-free solution for managing multiple computers.

### Slogan

One Interface, Stable Fast, Cross-OS

## Device Interface & Connection

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

## Core Interfaces
1. A female USB2.0-C port connects to the host computer for capturing target’s video stream and to transmit host’s keyboard and mouse data, which is converted into HID signals for target;
2. A second female USB-C port connects to a target device, where the product is simulated as a keyboard and mouse.
3. An HDMI input port on the target computer for video signal capture, converted into USB streaming video for the host computer.
4. A female USB2.0-A port doubles as a USB port and provides a stable 5V power output, ideal for powering devices such as the Raspberry Pi.
5. An additional female USB-C port can input extra power to backup the above USB port to supply more demanding micro-computers like the Nvidia Jetson Nano.

## Kit Composition
* Core Product: Central unit for KVM control and integration between the host and the target.
* USB Hub: Includes a HDMI output port, a USB3.0-A port, a USB3.0-C port, a USB-C power input port,
* Modular Assembly Adapter: This adapter is for modular assembly of the core and the USB hub by linking their HDMI, USB-A, and USB-C ports, creating a single integrated unit. This allows for a more efficient connection between the host's USB-C port and the target’s USB-C port, reducing the need for multiple cables.
* Accessories:
	+ USB-C male to C male cable
	+ USB-C male to A male cable
	+ HDMI male to HDMI male cable
	+ USB-C female to USB-A male adapter
	+ SB-C female to lightning male adapter

## Visual Design
* Brand Name: Openterface
* Brand Explanation: 

## Hardware Components
* Serial communication module: connected to the host via USB interface and bridging communication with CH9329 module.
* CH9329 chip: responsible to decode serial signals from the host computer into keyboard and mouse events, acted as a keyboard mouse simulator and controlling the target computer.
* HDMI Capture module: responsible to capture video signal of the target’s screen via HDMI cable, do video transcoding and deliver video steaming as a webcam-like signal to the host via USB interface.

## Use Cases
* Ease of Setup for Micro-Computer Enthusiasts: This product simplifies the initial setup process for enthusiasts who often work with micro-computers like Raspberry Pi and Jetson Nano. Users can control these micro-computers directly from a main computer, eliminating the need for extra peripherals like keyboards, mice, and monitors.
* Mobile App Integration for Desktop Use: Our product is especially useful for users who rely on mobile-specific applications like home surveillance app, stock trading platforms, mobile games, or social media apps like TikTok, which may not offer desktop versions. This feature enables users to seamlessly manage mobile app tasks directly from their computer, enhancing convenience and efficiency.
* Unified Interface for Multiple Devices: This product is perfect for users who regularly operate a combination of personal and work computers, along with mobile devices such as iPhones, Android phones, and tablets. It allows for seamless control of a secondary computer, like a laptop, from a primary desktop computer. Users can manage all their devices from a single interface, avoiding the hassle of switching between different keyboards and mice.
* Efficient Server Room Management: For those involved in server room operations and maintenance, this product offers a streamlined solution. It allows for the control of multiple servers from a single workstation, improving operational efficiency and ease of management.
* Enhanced Live Stream Management for Influencers: Highly beneficial for influencers who manage live streams across multiple devices. It efficiently integrates all the live streaming apps from different phones into a single interface on the host computer. This integration allows influencers to effortlessly manage their streams and interact with their audience in real time, all from one central location.