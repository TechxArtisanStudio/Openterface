# Extension Pins Guideline

![change-cap](images/product/change-cap.svg#only-light){:style="height:300px"}
![change-cap](images/product/change-cap_1.svg#only-dark){:style="height:300px"}

The Openterface Mini-KVM features extension pins for advanced development and [Open Software](/app) experimentation. These pins are not exposed in the standard case configuration.

### Accessing Extension Pins for Development

To access the extension pins:

1. Disassemble the device
2. Replace the original case cover with a specialized Extension Pin Cap
3. Download the 3D model for the Extension Pin Cap from our [GitHub repository](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware)

!!! warning "Warranty Void"
    Removing the original case voids the product warranty. All modifications or disassembly are undertaken at the user's own risk.

!!! note "Experimental Features"
    Features developed using these pins are experimental and have not been fully tested. Openterface is not liable for any damage, injury, or malfunction resulting from modifications, exposure of the extension pins, or other alterations to the device.

### Pin Layout

![target-side](images/product/extension-pins-1.svg#only-light){:style="height:200px"}
![host-side](images/product/extension-pins-2.svg#only-light){:style="height:200px"}
![target-side](images/product/extension-pins-1_1.svg#only-dark){:style="height:200px"}
![host-side](images/product/extension-pins-2_1.svg#only-dark){:style="height:200px"}

The extension pins provide the following connections:

1. USB 5V Power supply for external components
2. Data positive to the USB hub of the host
3. Data negative to the USB hub of the host
4. Data positive to the USB hub of the target
5. Data negative to the USB hub of the target
6. Ground

!!! danger "Incorrect Connections"
    Mixing up VCC and GND can cause severe damage to the device and connected components. Always double-check pin connections before powering the device.
