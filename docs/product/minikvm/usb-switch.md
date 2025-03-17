---
title: "Switchable USB Port"
description: "Learn about the dual hardware-software USB switching system in Openterface Mini-KVM. Understand the four operational states, safety guidelines, and future remote access capabilities."
keywords: "USB switching, KVM switch, hardware switch, software switch, USB port control, KVM over USB, KVM over IP, remote access, USB device management, computer peripherals, USB power management"
---

# **USB Port Switching Guide** | Openterface Mini-KVM

The mini-KVM device has a single USB-A 2.0 port that can connect to either the host or the target computer, but never both at once. Control comes from two switches:

- **Hardware Switch**: A physical two-position toggle on the device ![Toggle Switch](/images/shell-icons/toggle-h-t.svg#only-light){:style="height:20px"} ![Toggle Switch](/images/shell-icons/toggle-h-t_1.svg#only-dark){:style="height:20px"} (inward = host, outward = target).  
- **Software Switch**: A toggle button in the host app that instantly redirects the USB port to either host or target.

At startup, the device defaults to the host connection. The software detects the hardware switch's position and syncs accordingly.

## Operational States

Because both hardware and software can toggle the connection, there are four possible states:

1. **State 1 (Synced to Host)**  
   Hardware and software both set to Host; port is connected to the Host.  
2. **State 2 (Synced to Target)**  
   Hardware and software both set to Target; port is connected to the Target.  
3. **State 3 (Out of Sync, Port → Host)**  
   Hardware is set to Target, software is set to Host; port remains with Host.  
4. **State 4 (Out of Sync, Port → Target)**  
   Hardware is set to Host, software is set to Target; port remains with Target.

Switching from these states follows a straightforward logic: any manual toggle of the hardware switch updates the software display and moves the system to a "synced" state. Any click on the software switch changes the connection immediately, potentially leaving the hardware and software out of sync until the hardware switch is moved again.

!!! warning "Remember to eject the flash drive before toggling the switch"
    If the USB port is being used by a flash drive, ensure you eject the flash drive before toggling the switch to transfer the port's use to another computer.

!!! warning "USB power limitations"
    The power supplied by the USB port depends on the Host motherboard. It is not recommended to connect USB devices that require a lot of power. Typically, the power consumption should not exceed 1.5W. Connecting high-power devices may result in unstable operation or potential damage.

!!! Note "User Guidance"
    - **Software Switch Priority**: Regardless of the hardware switch position, clicking the software switch will immediately change the circuit direction.

    - **Hardware Switch Sync**: Any manual toggle of the Hardware Switch will align its state with the Software Switch, transitioning to either State 1 or State 2 from the out-of-sync State 3 or State 4. However, this synchronization does not necessarily alter the actual circuit connection.

    - **Hardware Switch Monitoring**: The Hardware Switch, despite being physical, is monitored by software and does not directly control the circuit direction. Instead, the software interprets the switch position and manages the actual circuit switching.

## Why It Matters

Software-driven USB switching (new in v1.9) lays groundwork for future remote-access features, such as KVM-over-IP, enabling remote users to share the USB port between the target and host—ideal for file transfers without physical intervention.