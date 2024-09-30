# How to Connect

## Interfaces

![host-side](images/product/host-htc.svg#only-light){:style="width:360px"}

![target-side](images/product/target-htc.svg#only-light){:style="width:360px"}

![host-side](images/product/host-htc_1.svg#only-dark){:style="width:360px"}

![target-side](images/product/target-htc_1.svg#only-dark){:style="width:360px"}

① ![Type-C to Host](images/shell-icons/host.svg#only-light){:style="height:15px"} ![Type-C to Host](images/shell-icons/host_1.svg#only-dark){:style="height:15px"} - **Host USB-C Port** (Female): As a USB device port, connecting to the Host computer for data transfer via built-in USB hub

② ![Type-C to Target](images/shell-icons/target.svg#only-light){:style="height:18px"} ![Type-C to Target](images/shell-icons/target_1.svg#only-dark){:style="height:18px"} - **Target USB-C Port** (Female): As a USB device port, connecting to the Host computer for emulating keyboard and mouse HID output via built-in USB hub

③ ![HDMI Input](images/shell-icons/input.svg#only-light){:style="height:18px"} ![HDMI Input](images/shell-icons/input_1.svg#only-dark){:style="height:18px"} - **HDMI Input Port** (Female): HDMI source input from the Target computer

④ ![USB-A Port](images/shell-icons/switchable-usb.svg#only-light){:style="height:26px"} ![USB-A Port](images/shell-icons/switchable-usb_1.svg#only-dark){:style="height:26px"} - **Switchable USB-A 2.0 Port** (Female): As a USB host port, utilized by either the host computer or the target computer at any given time, but not simultaneously.

!!! warning "Tight Fit"
    Please note that this USB-A female port is designed with a locking mechanism, which requires a bit more force to plug in and unplug your USB devices.

⑤ ![Toggle Switch](images/shell-icons/toggle-h-t.svg#only-light){:style="height:20px"} ![Toggle Switch](images/shell-icons/toggle-h-t_1.svg#only-dark){:style="height:20px"} - **Toggle Switch**: For toggling the connection of the USB-A 2.0 port between the host and the target computer

⑥ ![Extension Pins](images/shell-icons/pins.svg#only-light){:style="height:15px"} ![Extension Pins](images/shell-icons/pins_1.svg#only-dark){:style="height:15px"} - **Extension Pins**: For more information, please check [Extension Pins](/extension-pin) for developer use.

## Connection Steps

![to-host](images/product/to-host.svg#only-light){:style="height:260px"} ![to-host](images/product/to-host_1.svg#only-dark){:style="height:260px"}
![to-target](images/product/to-target.svg#only-light){:style="height:260px"} ![to-target](images/product/to-target_1.svg#only-dark){:style="height:260px"}

To set up your Mini-KVM, follow these steps in order:

1. **Host Computer Connection** (Orange Side):
    - Connect the host computer to the mini-KVM using the orange 1.5m Type-C USB cable. Plug it into the Type-C female port on the orange side of the mini-KVM.

    !!! note "Host App Required"
        The host computer needs to have the host app installed. For more information and download links, please refer to the [App Documentation](/app).

2. **Target Device Connection** (Black Side):
    - Connect the target device to the mini-KVM using the black 0.3m Type-C USB cable. Plug it into the Type-C female port on the black side of the mini-KVM.

3. **Target Video Output Connection** (Black Side):
    - Connect the target device's video output port to the HDMI female port on the black side of the mini-KVM. Use the black 0.3m HDMI cable, or any other appropriate video-source-to-HDMI cable, such as a VGA-to-HDMI converter cable.

    !!! note "No App Required for the Target"
        No pre-installation or configuration is required on the target device. As long as the target device supports UI operations with video output (HDMI, VGA, e.g.) and has a USB port to receive emulated keyboard and mouse control (HID) signals, it can be used. Thus, supported target device platforms include Windows, macOS, Linux, Android, and iOS.

4. **Switchable USB-A 2.0 Port Connection** (Optional):
    - If you want to connect a usb device to the Switchable USB-A 2.0 Port, it's recommended to do so after completing the above three connections and ensuring the host app is open.

