# Frequently Asked Questions (FAQs) about Openterface Mini-KVM

We're delighted to have you here! ❤️ This section aims to provide answers to commonly asked questions regarding the Openterface Mini-KVM. 
If you don't find what you're looking for, please join our Openterface [Reddit community](https://www.reddit.com/r/Openterface_miniKVM/) to pose your questions and engage in discussions. Furthermore, feel free to reach out via this [form](https://forms.gle/rwDDsMbs5pFwq7227). 


## Basic

### **What is the Openterface Mini-KVM?**

   - The Openterface Mini-KVM is a portable device that allows you to connect to and control another computer through a USB connection. This KVM-over-USB solution captures video via HDMI and simulates a keyboard and mouse. It enables to use your own laptop to display and control the target device directly. This tool is handy for tech enthusiasts and IT professionals for configuring or troubleshooting headless devices without the need for extra monitor, keyboard and mouse, especially in cases where the network connection is unreliable or not available at all.

### **What are the unique selling points of the Openterface Mini-KVM compared to similar products?**

- The Openterface Mini-KVM stands out for its plug-and-play functionality, direct BIOS-level access, portable design, and a switchable USB-A port shared between host and target. It offers a stable and fast control experience without network dependency, making it ideal for situations where network access is limited or unreliable. It is about using your own laptop to do configuring for headless device quick: plug in, do things, and then move on to next one, without concern of network.

### **What devices are compatible with the Openterface Mini-KVM?**

- Host Computer
    - The application for the host computer is currently compatible with macOS.
    - We are actively developing applications for other operating systems and will include them in our future releases.

- Target Devices
    - The Openterface Mini-KVM is compatible with any device that can output its screen display through an HDMI port and receives simulated Keyboard/Mouse HID control signals via a USB port. Thus, it supports target devices operating on Windows, macOS, Linux, Android, and iOS.

### **Can the device be used with non-macOS hosts?**

   - Currently, it is optimised for macOS hosts at the moment, but development for Windows and other platforms is on the roadmap.

### **Can the Openterface Mini-KVM support file transfers between the host and target device?**

- Yes, the Openterface Mini-KVM includes a switchable USB-A port designed for transferring files between the host and target devices. 
- To transfer files: 
     1. First mount a USB flash drive on one device (for example, the host), then
     2. Copy the files onto this drive. After copying, 
     3. Unmount the drive without physically unplugging it; Instead, 
     4. Simply flip a small black switch on the device. This action switches the USB-A port's connection to the other device (in this case, the target). Next,
     5. Mount the flash drive on the target device to move files off the drive, completing the transfer process. 
     
     This method can also be used in the opposite direction.

### **Will there be technical support and documentation available for the Openterface Mini-KVM?**

- Extensive documentation for the Openterface Mini-KVM can be found on our website at [Openterface.com](https://www.openterface.com/). We continuously update these resources to optimise your experience with the device.
- For technical support, we invite you to join our [Reddit Community](https://www.reddit.com/r/Openterface_miniKVM/), a community-driven platform for sharing queries and insights among fellow users and our expert team.
- If your issue remains unresolved, our team is available to provide further technical assistance. You can  reach out via this [form](https://forms.gle/rwDDsMbs5pFwq7227). 

### **What is the expected price point?**

   - Pricing is still being determined and will depend on production costs and demand. We're exploring options like crowdfunding. Knowing how many people would like to buy this mini-KVM Openterface in advance will be very helpful for us to plan and control production costs more effectively, leading to a more affordable price. Thus, you are interested into buying our product, please join this [waitlist](https://forms.gle/YnuKHrgPzrSZrqEt9).

## Technical

### **Is the Openterface Mini-KVM open-source?**

   - Plans to open-source the project are under consideration.

### **Can I access a device's BIOS/firmware settings?**

   - Yes, the direct hardwired connection of the Openterface Mini-KVM enables access to low-level BIOS or firmware settings. This feature stands in contrast to software-based KVM solutions or remote control applications like TeamViewer and Zoom, which typically do not allow BIOS-level interactions.


### **How is video/data transmitted between devices?**

   - Video data is captured via HDMI and transmitted over USB 2.0 to the host computer for display. 
   - The switchable USB 2.0 port allows basic peripheral sharing. Future versions may offer higher throughput connections.

### **How does the Openterface Mini-KVM handle power supply and consumption?**

- The device does not require an external power supply, as it is designed to be powered through its USB-C connections from the host, enhancing its portability.
- In scenarios where the target device is a low-power micro-computer, such as a Raspberry Pi, it can be powered through the host via the Mini-KVM's switchable USB port. However, this is not recommended. The standard method of operation is to have an external power supply to the target device.

## Control Mechanism 

### **Are there plans for a version with wireless or Ethernet connectivity?**

   - There are no immediate plans for us to support wireless or Ethernet connectivity in our Openterface development, as the focus of this mini-KVM is on fast, stable, direct control over USB to a target device, without concern of network condition. 
   - If we change our mind on this matter, we will keep [our community](https://www.reddit.com/r/Openterface_miniKVM/) updated 😃
   - Nevertheless, please still feel free to [share](https://forms.gle/rwDDsMbs5pFwq7227) your thoughts with us, if you really can not find a satisfying KVM-over-IP out there in the market.

### **Why doesn't the Openterface Mini-KVM stream video over local IP or wireless video broadcast and support wireless keyboard and mouse control?**

- The design philosophy behind the Openterface Mini-KVM emphasizes stable, wired control to ensure reliability and performance. By prioritizing direct connections through HDMI and USB, we aim to provide a seamless and efficient user experience, free from the potential instabilities and latency associated with wireless communications and network streaming. However, we are open to exploring these features in future versions of our device, as we continue to assess user needs and technological advancements.

### **Does it work with PS/2 output to control the target?**

   - Consideration for supporting a built-in PS/2 interfaces is part of our future development plan.

## Video Related

### **What about video latency and resolution?**

   - The device is engineered to handle 1080p video with minimal latency, ensuring a seamless control experience.

### **Is the Openterface Mini-KVM suitable for high-quality gaming?**

- Currently, our device is designed with a focus on providing direct control and management of target devices rather than prioritising high-resolution display output. As such, while the Openterface Mini-KVM facilitates efficient device configuration and troubleshooting, it may not support the high-quality display requirements necessary for an optimal gaming experience. Our priority is on reliability and functionality for technical tasks rather than gaming.

### **Will there be support for high-quality display in future versions of the Openterface Mini-KVM?**

- Yes, we are aware that there is significant interest in high-quality display capabilities among our users. While it is not our main focus at the moment, we are considering the inclusion of enhanced display features for a professional version of the Openterface Mini-KVM. We value the feedback from our community and aim to cater to the needs of our users in future product developments.

### **Does it work with analog video outputs like VGA?**

   - Currently it only captures digital video via HDMI. VGA support may be added in the future. Simple analog conversion can be achieved using HDMI-to-VGA adapters.

### **Does the Openterface Mini-KVM support VLC media player for streaming video?**

- No, the Openterface Mini-KVM does not support VLC media player for streaming video. This is because the device is not designed as a network-based solution, which is typically required for streaming applications like VLC. Our focus is on direct USB connectivity for device control and management, rather than network-dependent functionalities.

## Comparison 

### **How is this Mini-KVM different from KVM-over-IP?**

1. **Network Independence**: Our mini-KVM Openterface uses a direct USB connection for control, whereas KVM-over-IP relies on network connectivity, which requires extra effort and time to set up for new target devices.
2. **Stable Performance**: Mini-KVM offers fast and stable performance without being affected by network quality, in contrast to KVM-over-IP, which can be impacted by network speed and stability.
3. **Portability**: The Mini-KVM is designed for portability and ease of use with nearby headless devices, making it better to deal with uncertain situations where network access is limited or unavailable.
4. **Direct File Transfer**: The Mini-KVM supports direct file transfers between the host and target devices through a switchable USB-A port, a feature that might not be as straightforward with some KVM-over-IP solutions.
6. **Target Audience**: Mini-KVM is particularly suitable for tech enthusiasts and IT professionals who require a quick and reliable solution for configuring or troubleshooting nearby headless devices, whereas KVM-over-IP is often used in environments with a stable network where remote access over IP is a priority.

### **How is this different from traditional KVM solutions?**

1. **Portability:** The Openterface Mini-KVM is designed for portability, making it ideal for tech enthusiasts and IT professionals who need a compact solution. Traditional KVM switches tend to be larger and suited for stationary setups.
2. **Control Mechanism and Integration:** Traditional KVM switches use pure hardware-based switching mechanisms, allowing control of only one computer at a time. In contrast, the Openterface Mini-KVM combines hardware and software, enabling the control of both the host and target devices through a single interface on the host computer, ideally for laptop. This integrated approach facilitates seamless switching between host and target at the window level, significantly improving workflow efficiency.
3. **Functionality:** While the Openterface Mini-KVM focuses on 1-to-1 direct control over USB and HDMI video capture, traditional KVM switches may offer a wider range of functionalities including multi-device control via USB, VGA, DVI, HDMI, audio support, and sometimes even remote access capabilities over the network.
4. **Power Supply:** the mini-KVM does not require an external power supply, as it is designed to be powered through its USB-C connections from the host, enhancing its portability.

### **Comparison between our Mini-KVM, traditional KVM, and VNC**

| Comparison Category        | Openterface Mini-KVM                            | Traditional KVM                                  | Traditional VNC                                     |
|----------------------------|-------------------------------------------------|--------------------------------------------------|-----------------------------------------------------|
| 🎮 Method & Limitation     | Local, cable-limited                         | Local, cable-limited                          | ocal/Remote, network-limited                    |
| 🚀 Portability             | Highly portable, easy setup                  | Stationary, bulky                             | Software-based, not applicable                   |
| 🛠️ Installation Complexity | Plug-and-play, minimal setup                | Moderate setup, peripherals required         | Network and software setup, complex              |
| 🖥️ Control Interface       | Host software interface                      | Physical switch interface                    | Host software interface                          |
| 👁️ User Interface         | Intuitive app-based                          | Physical switching, no software              | Variable software interface                      |
| 🔄 Cross-OS Compatibility  | Fully compatible with multiple OS            | Depends on model and connections              | Compatible software required                     |
| 🖼️ Screen Resolution       | High-quality via HDMI                        | Varies with cable and KVM                     | Varies with software and network                 |
| 🔑 Access to BIOS          | Yes                                           |  Yes                                           | No                                                |
| 📁 File Transfer           | Hardware-based via its switchable USB-A      | Not available                                 | Software-based, network-dependent                |
| 💻 Multi-Device Support    | 1-to-1, by one host and hardware-dependent      | 1-to-N, by one physical setup                   | N-to-N, by network and software-dependent |
| 🔌 Cables & Accessories    | Fewer cables (HDMI, Type-C to USB-A)         | Multiple (Video Cable, Keyboard, Mouse, etc.) | Network required                                 |
| 📱 Software                | macOS host app required                      | No additional software for basic operation    | Client software on both host and target          |
| ⚡️ Power Supply            | No external power needed                     | External power often required                 | Not applicable (software-based)                  |

Our comparison table above is designed to provide a clear overview of how each solution aligns with different user needs, helping you choose the most suitable option for your unique setup.

In summary, the **Openterface Mini-KVM** stands out for its ^^portability, ease of installation, and the intuitive app-based control interface^^. It excels in providing ==a stable, high-quality connection for a one-to-one host-target interaction without requiring network and external power==. In contrast, traditional KVM solutions offer physical switching between multiple devices, but often at the cost of portability and setup simplicity. VNC, while flexible in allowing multiple hosts to connect to multiple devices over a network, relies heavily on software and network quality.