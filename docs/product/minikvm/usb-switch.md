---
title: "Switchable USB Port"
description: "Learn about the dual hardware-software USB switching system in Openterface Mini-KVM. Understand the four operational states, safety guidelines, and future remote access capabilities."
keywords: "USB switching, KVM switch, hardware switch, software switch, USB port control, KVM over USB, KVM over IP, remote access, USB device management, computer peripherals, USB power management"
---

# **USB Port Switching Guide** | Openterface Mini-KVM

The mini-KVM device has a single USB-A 2.0 port that can **connect to either** the host or the target computer, but **never both at once**. 

Control comes from two switches:

- **Hardware Switch**: A physical two-position toggle on the device ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t.svg#only-light){:style="height:20px"} ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t_1.svg#only-dark){:style="height:20px"} (inward = host, outward = target).  
- **Software Switch**: A toggle button in the host app that instantly redirects the USB port to either host or target.

## Operational States

The USB-A port's connection depends on both the **Hardware Switch** and the **Software Switch** positions. The following table summarizes the four possible states:

| **State** | **Hardware Switch** | **Software Switch** | **Port Connected To** | **Sync Status**       |
|-----------|---------------------|---------------------|------------------------|------------------------|
| 1         | Host                | Host                | Host                   | Synced                |
| 2         | Target              | Target              | Target                 | Synced                |
| 3         | Target              | Host                | Host                   | Out of Sync (→ Host)  |
| 4         | Host                | Target              | Target                 | Out of Sync (→ Target) |

- **Synced** means hardware and software settings match.  
- **Out of Sync** means software overrides the hardware switch temporarily until the hardware switch is moved again.

Any manual movement of the hardware switch will update the software display and return to a synced state.

At startup, the device defaults to the host connection. The software detects the hardware switch's position and syncs accordingly.

!!! warning "Remember to eject the flash drive before toggling the switch"
    If the USB port is being used by a flash drive, ensure you eject the flash drive before toggling the switch to transfer the port's use to another computer.

??? note "How to share a USB stick/disk between the Host and Target devices?"
    Files can be transferred between the host and target by following these steps:

    1. Mount a USB stick drive on the host when the small black switch is set to the side of the host's Type-C port.
    2. Copy the files onto this mounted drive.
    3. After copying, unmount the drive without physically unplugging it.
    4. Flip the small black switch to the other side. This action switches the USB-A port's connection to the target.
    5. Mount the USB stick on the target device and copy/move files off the drive, completing the transfer process of files from host to target.

    This method can also be used in the opposite direction.

!!! Note "User Guidance"
    - **Software Switch Priority**: Regardless of the hardware switch position, clicking the software switch will immediately change the circuit direction.

    - **Hardware Switch Sync**: Any manual toggle of the Hardware Switch will align its state with the Software Switch, transitioning to either State 1 or State 2 from the out-of-sync State 3 or State 4. However, this synchronization does not necessarily alter the actual circuit connection.

    - **Hardware Switch Monitoring**: The Hardware Switch, despite being physical, is monitored by software and does not directly control the circuit direction. Instead, the software interprets the switch position and manages the actual circuit switching.