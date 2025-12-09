# KVM-Go Firmware Upgrade

## Overview

KVM-Go uses the CH32V208 chip from WCH for keyboard and mouse emulation. Currently, firmware flashing requires WCH's official programming tool, which is only available for Windows. Therefore, firmware updates must be performed on a Windows system at this time.

We're actively working on a cross-platform, self-developed firmware upgrade solution that will be integrated directly into the device. Once ready, it will support firmware updates across all major operating systems—without requiring third-party tools.

> **Note:** This manual firmware upgrade procedure is a temporary solution for early development units. For official production products, firmware updates will be seamlessly integrated into our software, allowing you to update firmware directly through the application without requiring any third-party tools or manual procedures.

## Prerequisites

Before proceeding, ensure you have:

- A Windows computer
- The WCH ISP Tool installed
- The firmware file (`.hex` format) ready for flashing

### Download Firmware

Download the latest KVM-Go firmware file:

- [BLE_USB.hex](https://download.openterface.com/BLE_USB_20251209.hex) — Latest firmware for KVM-Go keyboard and mouse emulation (CH32V208 chip)

Save the firmware file to an easily accessible location on your Windows computer before proceeding with the upgrade process.

### Download WCH ISP Tool

Download and install the [WCHISPTool](https://www.wch.cn/downloads/WCHISPTool_Setup_exe.html?spm=a2ty_o01.29997173.0.0.697cc921DiYWE0 "WCHISPTool") (Windows only).

Thank you for your patience and support!

## Step-by-Step Instructions

### Step 1: Download and Open the Tool in Windows

Launch the WCH ISP Tool on your Windows computer.

![WCH ISP Tool interface](https://assets.openterface.com/images/post/kvmgo-firmware/image-1763953443609.webp)

### Step 2: Prepare the KVM-Go for Flashing

To flash firmware on the KVM-Go:

1. Ensure the device is powered off
2. Press and hold the button while connecting it to a USB Type-C port

**Tip:** You can flash the firmware using either port, but the "target" port tends to be more stable during flash.

![KVM-Go wiring and connection setup](https://assets.openterface.com/images/post/kvmgo-firmware/image-1763982667349.webp)

### Step 3: Select the Firmware File

If the connection is successful, the tool will automatically detect the chip model (CH32V20X series). 

1. Click the "..." button to browse and select the firmware file you wish to flash
2. Select the `.hex` firmware file
3. **Important:** Remember to check the box next to the firmware file

![Chip model detected in WCH ISP Tool](https://assets.openterface.com/images/post/kvmgo-firmware/image-1763954642761.webp)

![Browse and select firmware file](https://assets.openterface.com/images/post/kvmgo-firmware/image-1763954858836.webp)

![Firmware file selected with checkbox checked](https://assets.openterface.com/images/post/kvmgo-firmware/image-1763955070638.webp)

### Step 4: Deprotect Current Firmware

Before flashing new firmware, you need to remove write protection from the current firmware:

1. Click the "Deprotect" option in the tool
2. Briefly press the physical button on the KVM-Go to enter flashing mode
3. Wait for the deprotection process to complete

![Deprotect firmware option in tool](https://assets.openterface.com/images/post/kvmgo-firmware/image-1763955617253.webp)

![Press button on KVM-Go to enter flashing mode](https://assets.openterface.com/images/post/kvmgo-firmware/image-1763955858115.webp)

### Step 5: Download and Flash the Firmware

Once the firmware is deprotected and selected:

1. Click the "Download" button in the flashing tool
2. Wait for the flashing process to complete
3. The tool will indicate when the firmware has been successfully flashed

![Download and flash firmware process](https://assets.openterface.com/images/post/kvmgo-firmware/image-1763956095046.webp)

## Further Reading

- [Openterface KVM-Go Review Guide](review-guide.md) — Important notes and known issues for engineering prototype units
