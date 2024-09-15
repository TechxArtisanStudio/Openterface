# Specifications

![lig-front](images/product/minikvm-v1-9-front.svg){:style="max-height:260px"}
![lig-back](images/product/minikvm-v1-9-back.svg){:style="max-height:260px"}

## Product Information
- Product Name: Openterface Mini-KVM Basic / Toolkit
- Model Name: OP-MINIKVM-BASIC / OP-MINIKVM-TOOLKIT

## Physical
- Device Dimensions (L x W x H): 61 x 53 x 13.5 mm / 2.40 x 2.09 x 0.53 inches
- Device Net Weight: Approximately 48g
- Casing Material: Aluminum alloy, PLA

## Compatibility
- Host: Windows, macOS, Linux, Android (with compatible app)
- Target: No software installation required

## Video
- Max Video Input: Up to 3840x2160@30Hz via HDMI
- Max Video Output: Up to 1920x1080@30Hz
- Video Compression Methods: YUV, MJPEG
- Additional Video Support: VGA, DVI, Micro HDMI (via adapter)
- Latency: Under 140 milliseconds

## Audio
- Audio Capture: HDMI embedded audio passthrough

## Power
- USB-C powered. No external power supply required.

## Connectivity
- USB Transmission: 12Mbps full-speed

## Features
- Full keyboard and mouse emulation (absolute & relative)
- Text transfer
- Multimedia key support
- Custom HID functionality
- Computer wake-up function

## Environmental
- Operating Temperature: 0°C to 40°C
- Storage Temperature: -10°C to 50°C
- Humidity: 80% RH

## Interfaces

![target-side](images/product/minikvm-v1-9-target.svg){:style="max-height:160px"}
![host-side](images/product/minikvm-v1-9-host.svg){:style="max-height:160px"}

- ① **Host USB-C Port** (Female): As a USB device port, connecting to the Host computer for data transfer via built-in USB hub
- ② **Target USB-C Port** (Female): As a USB device port, connecting to the Host computer for emulating keyboard and mouse HID output via built-in USB hub
- ③ **HDMI Input Port** (Female): HDMI source input from the Target computer
- ④ **Switchable USB-A 2.0 Port** (Female): As a USB host port, utilized by either the host computer or the target computer at any given time, but not simultaneously
- ⑤ **Toggle Switch**: For toggling the connection of the USB-A 2.0 port between the host and the target computer
- ⑥ **Extension Pins**: For more information, please check [Extension Pins](/extension-pin) for developer use.