---
title: "Hardware Installation"
description: "Step-by-step hardware installation guide for Openterface KVM Extension for uConsole. Learn how to properly install the extension board in your uConsole's expansion slot with detailed safety guidelines."
keywords: "KVM extension installation, uConsole hardware setup, expansion board installation, uConsole expansion slot, KVM hardware guide, physical installation"
---

# **Hardware Installation** | Openterface KVM Extension for uConsole

## Overview
The KVM Extension replaces the 4G/LTE module in the uConsole’s expansion slot, adding direct HDMI input and USB HID control.

## What You’ll Need
- Check your [Package Contents](whats-in-the-box.md) before installation  
- Openterface KVM Extension board  
- Provided **washers** (to ensure stable mounting and even pressure)  
- Hex screwdriver (for mounting screws)  
- ESD protection (wrist strap or grounded surface) — recommended  

## Installation Steps

### **1. Power Off**
Shut down the uConsole and disconnect all power and cables.

### **2. Remove Existing Module**
Use a hex screwdriver to remove the two screws.  
Lift the board **straight up** to avoid bending the spring contactors.

### **3. Install the KVM Extension**
- Place the **washer** on the screw post.  
- Seat the KVM Extension firmly into the expansion slot.  
- The washer compensates for the slightly thinner PCB (1.0 mm vs 1.2 mm), maintaining proper spring contact pressure.

??? note "Check fit before final installation"
    You can first seat the board **without the washer** to test the fit. If the board feels loose or contacts are uneven, add the washer and reseat the board. The Openterface KVM Extension is 1.0 mm thick, slightly thinner than the original LTE module (1.2 mm). Using the provided washer ensures stable mounting and reliable spring contact.  
    ![extension-slot-loose](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-slot-loose.webp){:style="height:220px"}

### **4. Secure the Board**
Reinsert screws and tighten **gently** — **do not overtighten**, as this may damage the board or strip the threads.

![extension-screw-washer-installed](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installed.jpg){:style="height:220px"}
![extension-screw-washer-installing](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-screw-washer-installing.jpg){:style="height:220px"}
![extension-install-1](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp){:style="height:220px"}

### **5. Verify Installation**
The board should sit **flat and stable**, with even spring contact across all pads. There should be no noticeable wobble or movement.

### **6. Install Expansion Slot Cover**
Reinstall the expansion slot cover to protect the KVM Extension board and maintain the uConsole's original appearance.

??? note "Text Orientation on Expansion Slot Cover"
    The text on the expansion slot cover may appear "upside down" when viewed from certain angles. This is intentional design - the text is oriented to be readable when you're holding the uConsole and looking at the ports from top to bottom, which is the natural viewing position when using the device.
    ![expansion-slot-text-orientation](https://assets.openterface.com/images/product/openterface-kvm-uconsole-expansion-slot-text-orientation.webp){:style="height:220px"}

---

**Next Steps**

1. Go to [Software Setup](/product/uconsole-kvm-extension/software-setup/) to install the Openterface App.  
2. Go to [Connect to Target Device](/product/uconsole-kvm-extension/connect-to-target/) to connect your target device.  
3. Review [Features & Specifications](/product/uconsole-kvm-extension/features/) for detailed technical specs.