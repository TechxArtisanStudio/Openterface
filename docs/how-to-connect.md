# How to Connect

## Interfaces

![host-side](images/product/host-htc.svg){:style="width:360px"}

![target-side](images/product/target-htc.svg){:style="width:360px"}

① ![Type-C to Host](images/shell-icons/host.svg){:style="height:15px"} - **Host USB-C Port** (Female): As a USB device port, connecting to the Host computer for data transfer via built-in USB hub

② ![Type-C to Target](images/shell-icons/target.svg){:style="height:18px"} - **Target USB-C Port** (Female): As a USB device port, connecting to the Host computer for emulating keyboard and mouse HID output via built-in USB hub

③ ![HDMI Input](images/shell-icons/input.svg){:style="height:18px"} - **HDMI Input Port** (Female): HDMI source input from the Target computer

④ ![USB-A Port](images/shell-icons/switchable-usb.svg){:style="height:26px"} - **Switchable USB-A 2.0 Port** (Female): As a USB host port, utilized by either the host computer or the target computer at any given time, but not simultaneously

⑤ ![Toggle Switch](images/shell-icons/toggle-h-t.svg){:style="height:20px"} - **Toggle Switch**: For toggling the connection of the USB-A 2.0 port between the host and the target computer

⑥ ![Extension Pins](images/shell-icons/pins.svg){:style="height:15px"} - **Extension Pins**: For more information, please check [Extension Pins](/extension-pin) for developer use.

## Connection Steps

![to-host](images/product/to-host.svg){:style="max-height:260px"}
![to-target](images/product/to-target.svg){:style="max-height:260px"}

To set up your Mini-KVM, follow these steps:

- **Host Computer** (Orange Side):

    - **Type-C Connection**: Connect the host computer to the mini-KVM using a Type-C USB cable, plugging it into the Type-C female port on the orange side of the mini-KVM.
    !!! note "Host App Required"
        The host computer needs to have the host app installed. For more information and download links, please refer to the [App Documentation](app.md).

- **Target Device** (Black Side):

    - **Type-C Connection**: Connect the target device to the mini-KVM using a Type-C USB cable, plugging it into the Type-C female port on the black side of the mini-KVM.
    - **Video Output**: Connect the target device's video output port to the HDMI female port on the black side of the mini-KVM using an HDMI cable, a VGA-to-HDMI cable, or any other appropriate video-source-to-HDMI cable.
    
    !!! note "No App Required for the Target"
        No pre-installation or configuration is required on the target device. As long as the target device supports UI operations with video output (HDMI, VGA, e.g.) and has a USB port to receive emulated keyboard and mouse control (HID) signals, it can be used. Thus, supported target device platforms include Windows, macOS, Linux, Android, and iOS.

