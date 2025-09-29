---
title: "Extension Pins"
description: "Explore the potential of Openterface Mini-KVM's extension pins for custom hardware development and open-source projects."
keywords: "Mini-KVM extension pins, custom development, hardware modification, open-source KVM"
---

# **Extension Pins** | Developer Mode | Openterface Mini-KVM

![mini-kvm-pins-port](https://assets.openterface.com/images/product/mini-kvm-pins-port.webp){:style="max-height:360px"}
![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="max-height:300px"}

The Openterface Mini-KVM features extension pins for advanced development and [Open Software](/app) experimentation. These pins are not exposed in the standard case configuration. 

## How to Access the Pins

1. Disassemble the device.
2. Replace the original case cover with a specialized Extension Pin Cap.
3. Download the [3D model](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models) for the Extension Pin Cap.
4. Check out our [Hardware GitHub repository](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware).

![change-cap](https://assets.openterface.com/images/product/change-cap.svg#only-light){:style="max-height:300px"}
![change-cap](https://assets.openterface.com/images/product/change-cap_1.svg#only-dark){:style="max-height:300px"}

!!! warning "Warranty Void"
    Removing the original case may void the product warranty. All modifications or disassembly are undertaken at the user's own risk.

!!! note "Experimental Features"
    Features developed using these pins are experimental and have not been fully tested. Openterface is not liable for any damage, injury, or malfunction resulting from modifications, exposure of the extension pins, or other alterations to the device.

## Pin Configuration

![target-side](https://assets.openterface.com/images/product/extension-pins-1.svg#only-light){:style="max-height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2.svg#only-light){:style="max-height:200px"}
![target-side](https://assets.openterface.com/images/product/extension-pins-1_1.svg#only-dark){:style="max-height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2_1.svg#only-dark){:style="max-height:200px"}

The extension pins provide the following connections:

1. USB 5V Power supply for external components
2. Data positive to the USB hub of the host
3. Data negative to the USB hub of the host
4. Data positive to the USB hub of the target
5. Data negative to the USB hub of the target
6. Ground

!!! danger "Incorrect Connections Cause Damage"
    Mixing up VCC and GND can cause severe damage to the device and connected components. Always double-check pin connections before powering the device.

## Extension Pin Cap

![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="max-height:360px"}

This 3D-printed Extension Pin Cap replaces the original cap on the Openterface Mini-KVM, allowing advanced users to expose and access extension pins for custom development. You can download the 3D model files from our GitHub repository and print the cap yourself.

- **Use**: Provides access to extension pins for advanced hardware development.
- **Download**: [3D Model Files](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models)

## Get Involved in Development

As we continue to develop and experiment, we'll be updating this section with more information about what these pins can do and how they can be used creatively. Your creativity and expertise can help push the boundaries of what's possible with the Openterface Mini-KVM. Please get involved:

1. **Share Your Ideas**: Have a cool concept for using these pins? We'd love to hear it!
2. **Contribute DIY Projects**: If you've created something interesting, consider sharing it with our [Discord Openterface](/discord) community.
3. **Join the Discussion**: Connect with other developers and enthusiasts to brainstorm and collaborate.

Let's build and innovate together!