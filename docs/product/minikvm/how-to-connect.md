---
title: "How to Connect"
description: "Step-by-step guide for setting up Openterface Mini-KVM. Learn how to connect your host computer and target device with detailed instructions for USB-C, HDMI, and peripheral connections. Includes interface descriptions and important setup tips."
keywords: "Mini-KVM setup, KVM connection guide, USB-C KVM setup, HDMI KVM connection, KVM installation guide, computer peripheral setup, USB device connection, KVM interface guide, headless computer setup, KVM configuration"
---

# **How to Connect** | Setup Guide | Openterface Mini-KVM

## Connection Steps

![to-host](/images/product/to-host.svg#only-light){:style="height:260px"} ![to-host](/images/product/to-host_1.svg#only-dark){:style="height:260px"}
![to-target](/images/product/to-target.svg#only-light){:style="height:260px"} ![to-target](/images/product/to-target_1.svg#only-dark){:style="height:260px"}

To set up your Mini-KVM, follow these steps in order:

1. **Host Computer Connection** (Orange Side):
    - Connect the host computer to the mini-KVM using the orange 1.5m Type-C USB cable. Plug it into the Type-C female port on the orange side of the mini-KVM.

    !!! note "Host App Required"
        The host computer needs to have the host app installed. For more information and download links, please refer to the [App](/app) page.

2. **Target Device Connection** (Black Side):
    - Connect the target device to the mini-KVM using the black 0.3m Type-C USB cable. Plug it into the Type-C female port on the black side of the mini-KVM.

3. **Target Video Output Connection** (Black Side):
    - Connect the target device's video output port to the HDMI female port on the black side of the mini-KVM. Use the black 0.3m HDMI cable, or any other appropriate video-source-to-HDMI cable, such as a VGA-to-HDMI converter cable.

    !!! note "No App Required for the Target"
        No pre-installation or configuration is required on the target device. As long as the target device supports UI operations with video output (HDMI, VGA, e.g.) and has a USB port to receive emulated keyboard and mouse control (HID) signals, it can be used. Thus, supported target device platforms include Windows, macOS, Linux, Android, and iOS.

4. **Switchable USB-A 2.0 Port Connection** (Optional):
    - If you want to connect a usb device to the Switchable USB-A 2.0 Port, it's recommended to do so after completing the above three connections and ensuring the host app is open.


## Interfaces

![host-side](/images/product/host-htc.svg#only-light){:style="width:360px"}

![target-side](/images/product/target-htc.svg#only-light){:style="width:360px"}

![host-side](/images/product/host-htc_1.svg#only-dark){:style="width:360px"}

![target-side](/images/product/target-htc_1.svg#only-dark){:style="width:360px"}

① ![Type-C to Host](/images/shell-icons/host.svg#only-light){:style="height:15px"} ![Type-C to Host](/images/shell-icons/host_1.svg#only-dark){:style="height:15px"} - **Host USB-C Port** (Female): As a USB device port, connecting to the Host computer for data transfer via built-in USB hub

② ![Type-C to Target](/images/shell-icons/target.svg#only-light){:style="height:18px"} ![Type-C to Target](/images/shell-icons/target_1.svg#only-dark){:style="height:18px"} - **Target USB-C Port** (Female): As a USB device port, connecting to the Host computer for emulating keyboard and mouse HID output via built-in USB hub

③ ![HDMI Input](/images/shell-icons/input.svg#only-light){:style="height:18px"} ![HDMI Input](/images/shell-icons/input_1.svg#only-dark){:style="height:18px"} - **HDMI Input Port** (Female): HDMI source input from the Target computer

④ ![USB-A Port](/images/shell-icons/switchable-usb.svg#only-light){:style="height:26px"} ![USB-A Port](/images/shell-icons/switchable-usb_1.svg#only-dark){:style="height:26px"} - **Switchable USB-A 2.0 Port** (Female): As a USB host port, utilized by either the host computer or the target computer at any given time, but not simultaneously. Please check [USB Port Switching Guide](../usb-switch) for more.

!!! warning "USB power limitations"
    The power supplied by the USB port depends on the Host motherboard. It is not recommended to connect USB devices that require a lot of power. Typically, the power consumption should not exceed 1.5W. Connecting high-power devices may result in unstable operation or potential damage.

!!! warning "USB-A Port Has Firm Locking Mechanism"
    The USB-A port includes a locking mechanism that requires extra force when plugging in or removing devices. This is intentional and ensures a secure connection. **Avoid using very small USB devices** (like ultra-compact USB drives), as they may be difficult to grip and remove, potentially leading to damage.

!!! warning "Extra USB Hub Requires External Power and May Affect Compatibility"
    The mini-KVM already includes a built-in USB hub that connects to both the host and the target computer. If you connect an additional external USB hub to the USB-A port, any USB devices attached to it will operate at a deeper level in the USB device tree. Some computers may have limitations on USB tree depth, which can cause compatibility issues or prevent certain devices from working correctly.

    Additionally, make sure any connected USB hub is externally powered. Unpowered hubs may cause instability or malfunction of the entire mini-KVM setup.

⑤ ![Toggle Switch](/images/shell-icons/toggle-h-t.svg#only-light){:style="height:20px"} ![Toggle Switch](/images/shell-icons/toggle-h-t_1.svg#only-dark){:style="height:20px"} - **Toggle Switch**: For toggling the connection of the USB-A 2.0 port between the host and the target computer

⑥ ![Extension Pins](/images/shell-icons/pins.svg#only-light){:style="height:15px"} ![Extension Pins](/images/shell-icons/pins_1.svg#only-dark){:style="height:15px"} - **Extension Pins**: Hidden by default and only accessible by replacing the top cover with an alternate cap. For more information, please check [Extension Pins](../extension-pins) for developer use.