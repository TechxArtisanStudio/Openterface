---
title: "Extension Pins"
description: "Explore Openterface Mini-KVM's extension pins for custom development. Learn about pin configuration, hardware modifications, and open-source development opportunities. Includes safety guidelines and community collaboration options."
keywords: "Mini-KVM extension pins, KVM hardware development, developer mode, open source KVM, hardware customization, USB pin configuration, KVM modifications, DIY KVM projects, hardware hacking, KVM development guide"
date: 2025-03-18
---

# **Extension Pins** | Developer Mode | Openterface Mini-KVM

![mini-kvm-pins-port](/images/product/mini-kvm-pins-port.png){:style="height:360px"}
![pin-cap](/images/product/part/pin-cap.jpg){:style="height:300px"}

The Openterface Mini-KVM features extension pins for advanced development and [Open Software](/app) experimentation. These pins are not exposed in the standard case configuration. 

## How to Access the Pins

1. Disassemble the device.
2. Replace the original case cover with a specialized Extension Pin Cap.
3. Download the [3D model](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models) for the Extension Pin Cap.
4. Check out our [Hardware GitHub repository](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware).

![change-cap](/images/product/change-cap.svg#only-light){:style="height:300px"}
![change-cap](/images/product/change-cap_1.svg#only-dark){:style="height:300px"}

!!! warning "Warranty Void"
    Removing the original case may void the product warranty. All modifications or disassembly are undertaken at the user's own risk.

!!! note "Experimental Features"
    Features developed using these pins are experimental and have not been fully tested. Openterface is not liable for any damage, injury, or malfunction resulting from modifications, exposure of the extension pins, or other alterations to the device.

## Pin Configuration

![target-side](/images/product/extension-pins-1.svg#only-light){:style="height:200px"}
![host-side](/images/product/extension-pins-2.svg#only-light){:style="height:200px"}
![target-side](/images/product/extension-pins-1_1.svg#only-dark){:style="height:200px"}
![host-side](/images/product/extension-pins-2_1.svg#only-dark){:style="height:200px"}

The extension pins provide the following connections:

1. USB 5V Power supply for external components
2. Data positive to the USB hub of the host
3. Data negative to the USB hub of the host
4. Data positive to the USB hub of the target
5. Data negative to the USB hub of the target
6. Ground

!!! danger "Incorrect Connections Cause Damage"
    Mixing up VCC and GND can cause severe damage to the device and connected components. Always double-check pin connections before powering the device.

## Get Involved in Development

As we continue to develop and experiment, we'll be updating this section with more information about what these pins can do and how they can be used creatively. Your creativity and expertise can help push the boundaries of what's possible with the Openterface Mini-KVM. Please get involved:

1. **Share Your Ideas**: Have a cool concept for using these pins? We'd love to hear it!
2. **Contribute DIY Projects**: If you've created something interesting, consider sharing it with our [Discord Openterface](/discord) community.
3. **Join the Discussion**: Connect with other developers and enthusiasts to brainstorm and collaborate.

Let's build and innovate together!

*Updated: {{ page.meta.date }}*