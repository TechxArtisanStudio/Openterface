---
title: "MicroSD Card Switching Guide"
description: "Learn about the dual hardware-software MicroSD switching system in Openterface KVM-Go. Understand the four operational states, LED indicators, safety guidelines, and file transfer capabilities."
keywords: "MicroSD switching, KVM switch, hardware switch, software switch, MicroSD card control, KVM over USB, file transfer, USB device management, computer peripherals, MicroSD power management, LED indicators"
---

# **MicroSD Card Switching Guide** | Openterface KVM-Go

The KVM-Go device features a single MicroSD card slot that can **connect to either** the host or the target computer, but **never both at once**. 

Control comes from two switches:

- **Hardware Button**: A physical button on the device that toggles between host and target connections.  
- **Software Switch**: A toggle button in the host app that instantly redirects the MicroSD slot to either host or target.

## LED Status Indicators

The device includes **dual-color LED indicators** to show the current connection state:

- **🔵 Blue LED ON**: MicroSD card is mounted to the **target device**
- **🟢 Green LED ON**: MicroSD card is mounted to the **host device**  
- **LED OFF**: No MicroSD card inserted or device powered off
- **LED FLASHING**: MicroSD card is being read from or written to (data transfer in progress)

!!! note "Auto-Mounting Feature (Experimental)"
    Currently, the device defaults to mounting the MicroSD card to the **host** when first connected. However, we're developing an experimental feature where the MicroSD card will automatically mount to whichever port (host or target) connects first. This will make the device even more user-friendly.