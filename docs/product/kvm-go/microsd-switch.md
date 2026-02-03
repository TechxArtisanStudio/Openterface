---
title: "MicroSD Card Switching Guide"
description: "Learn how to use the dual hardware-software MicroSD switching system in Openterface KVM-Go. Understand the four operational states, LED indicators, safety guidelines, and file transfer capabilities."
keywords: "MicroSD switching, KVM switch, hardware switch, software switch, MicroSD card control, KVM over USB, file transfer, USB device management, computer peripherals, MicroSD power management, LED indicators"
---

# **MicroSD Card Switching Guide** | Openterface KVM-Go

The **Openterface KVM-Go** includes a single MicroSD card slot that can be shared between the host computer and the target device, but never both at the same time.

This design allows you to quickly switch between devices for **file transfer**, without physically removing the card, making your workflow faster and more efficient. It can also just serve as your **regular MicroSD card reader**.

## **Install the MicroSD Card**

![kvm-go-install-sd](https://assets.openterface.com/images/kvm-go/install-sd.webp){:style="max-height:260px;width:auto"}

!!! note "Proper MicroSD Card Installation"
    Insert the MicroSD card firmly until you feel a **click**, indicating it is securely seated and locked in place.

## **Control Methods**

KVM-Go provides two ways to switch the MicroSD card between host and target:

- **Hardware Button** – A physical button on the device for manual control.  
- **Software Switch** – A toggle button within the host app for instant switching.


## **Switch Button & LED Indicators** 

![kvm-go-led-indicator](https://assets.openterface.com/images/kvm-go/led-indicator.webp){:style="max-height:260px;width:auto"}

The **dual-color LED indicators** display the current MicroSD connection state *(Note: Under Development / Subject to Change)*:

- **🔵 Blue LED ON** – MicroSD card is mounted to the **target device**  
- **🟢 Green LED ON** – MicroSD card is mounted to the **host computer**  
- **LED OFF** – No MicroSD card inserted or device powered off  
- **LED FLASHING** – Data transfer in progress (read/write activity)

!!! note "Auto-Mounting Feature (Experimental)"
    By default, the MicroSD card mounts to the **host** when the device is first powered on.  
    An upcoming experimental feature will allow **auto-mounting** to whichever side (host or target) connects first, making the experience even more seamless.

---

## Related

- [microSD EXPRESS on KVM-GO: Compatibility Test and Real Transfer Speeds](updates/20260203-kvm-go-microsd-express.md) — Compatibility test with SanDisk microSD EXPRESS card and real-world transfer speeds
