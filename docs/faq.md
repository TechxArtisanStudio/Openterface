---
tags:
  - File Transfer
  - mini-KVM
  - Switchable USB
  - BIOS
---

# Frequently Asked Questions (FAQs) about Openterface Mini-KVM

We're delighted to have you here! ❤️ This section aims to provide answers to commonly asked questions regarding the Openterface Mini-KVM. 
If you don't find what you're looking for, please join our Openterface [subreddit](https://www.reddit.com/r/Openterface_miniKVM/) to pose your questions and engage in discussions. Furthermore, feel free to reach out via this [form](https://forms.gle/rwDDsMbs5pFwq7227). 


## Basic

### **What is the Openterface mini-KVM?**

   - The Openterface Mini-KVM is a portable device that allows control over another computer through [USB and HDMI connection](/quick-start/#connection). This KVM-over-USB solution captures video via HDMI and simulates a keyboard and mouse input. It enables to use your own laptop to display and control the target device directly. This tool is handy for tech enthusiasts and IT professionals for configuring or troubleshooting headless devices without the need for extra monitor, keyboard and mouse, especially in cases where the network connection is unreliable or not available at all.

### **What are the unique selling points of the Openterface Mini-KVM compared to similar products?**

   - The Openterface Mini-KVM stands out for its plug-and-play functionality, direct BIOS-level access, portable design, and a switchable USB-A port shared between host and target. It offers a stable and fast control experience without network dependency, making it ideal for uncertain situations where network access is limited or unreliable. It is about using your own laptop effectivly to do configuring for headless device: plug in, do things, and then move on to next one, without concern of network.

### **What are use cases for this mini-KVM?**
   - Please check out this page: [Use Cases](/use-cases)

### **What devices are compatible with the Openterface Mini-KVM?**

- Host Computer
      - The application for the host computer is currently compatible with macOS.
      - We are also working on building host applications to support other operating systems, such as Windows and Linux.
- Target Devices
      - The Openterface Mini-KVM is compatible with any device that can output its screen display through an HDMI port and input simulated Keyboard/Mouse HID control signals via a USB port. Thus, it supports to control over most of devices operating on Windows, macOS, Linux, Android, and iOS.

### **Can the Openterface Mini-KVM support file transfers between the host and target device?**

   - Yes, the Openterface Mini-KVM includes a switchable USB-A port shared between the host and target devices. With a usb stickdisk plugged into this port, files are able to transfer between host and target by following steps:
      1. Mount a usb stick drive on host, when the small black switch is on the side of host type-c port, then
      2. Copy the files onto this mounted drive. After copying, 
      3. Unmount the drive without physically unplugging it; Instead, 
      4. Simply flip the small black switch to other side. This action switches the USB-A port's connection to the the target. Next,
      5. Mount the usb stick on the target device and copy/move files off the drive, completing the transfer process of files from host to target. 
      
      This method can also be used in the opposite direction.

### **Can the switchable USB-A port be toggled at the software level? Could this be achieved through a button instead?**
   - The current design does not support toggling at the software level; it can only be physically flipped for now.
   - Implementing toggling at the software level would necessitate a new design, incorporating a button and an LED indicator (either green/blue or on/off) to signify whether the USB port is set to the host or target mode. Additionally, this would require the integration of an additional chip, leading to increased costs in both hardware and software development. The existing design represents a compromise, aimed at balancing between cost-efficiency and basic functionality. Despite the potential for increased costs, we are interested in incorporating this feature in a future version for better user experience.

### **Will there be technical support and documentation available for the Openterface Mini-KVM?**

   - Extensive documentation for the Openterface Mini-KVM can be found on our website at [Openterface.com](https://www.openterface.com/). We continuously update these resources to optimise your experience with the device.
   - For technical support, we invite you to join our [subreddit](https://www.reddit.com/r/Openterface_miniKVM/), a community-driven platform for sharing queries and insights among fellow users and our expert team.
   - If your issue remains unresolved, our team is available to provide further technical assistance. You can  reach out via this [form](https://forms.gle/rwDDsMbs5pFwq7227). 

### **What is the expected price point?**

   - Pricing is still being determined and will depend on production costs and demand. We're exploring options like crowdfunding. Knowing how many people would like to buy this Openterface mini-KVM in advance will be very helpful for us to plan and control production costs more effectively, leading to a more affordable price. Thus, if you are interested into buying our product, please join this [Be Our Backer](https://www.crowdsupply.com/techxartisan/openterface-mini-kvm).

## Technical

### **Is the Openterface Mini-KVM open-source?**

   - Plans to open-source the project are under consideration. Just bear with us a little longer; We need to tidy quite some things up for opening up. If you are interested into contributing, please do tell us via this [form](https://forms.gle/rwDDsMbs5pFwq7227). Stay tuned!

### **Can I access a device's BIOS/firmware settings?**

   - Yes, the direct connection of the Openterface Mini-KVM enables access to low-level BIOS or firmware settings. This feature stands in contrast to software-based KVM solutions or remote control applications like TeamViewer and Zoom, which are typically not able to do BIOS-level interactions.


### **How is video/data transmitted between devices?**

   - Video data is captured via HDMI and transmitted over USB 2.0 to the host computer for display. 
   - The switchable USB 2.0 port allows basic peripheral sharing. Future versions may offer higher throughput connections with USB 3.

### **How does the Openterface Mini-KVM handle power supply and consumption?**

- The device does not require an external power supply, as it is designed to be powered through its Type-C connections from the host, enhancing its portability.
- In scenarios where the target device is a low-power micro-computer, such as a Raspberry Pi, it could be powered through the host via the Mini-KVM's switchable USB port. However, this is not recommended. The standard method of operation is to have an external power supply to the target device.

## Control Mechanism 

### **Are there plans for a version with wireless or Ethernet connectivity?**

   - There are no immediate plans for us to support wireless or Ethernet connectivity in our Openterface products, as the focus of this mini-KVM is on fast, stable, direct control over USB to a target device, without concern of network condition. 
   - If we change our mind on this matter, we will keep [our community](https://www.reddit.com/r/Openterface_miniKVM/) updated 😃
   - Nevertheless, please feel free to [share](https://forms.gle/rwDDsMbs5pFwq7227) your thoughts with us, if you really can not find a satisfying KVM-over-IP out there in the market.

### **How is this different from other KVM solutions like traditional KVMs, KVM-over-IP and VNC, etc?**
   - Please go to the page [Comparison](/comparison) for more details there.


### **Does it work with PS/2 output to control the target?**

   - Consideration for supporting a built-in PS/2 interfaces is part of our future development plan.

## Video Related

### **What about video latency and resolution?**

   - The device is engineered to handle 1080p video with minimal latency, ensuring a seamless control experience.

### **Is the Openterface Mini-KVM suitable for high-quality gaming?**

   - Currently, our device is designed with a focus on providing direct control of target devices for technical / IT operations rather than prioritising high-resolution display output for gaming. As such, while the Openterface Mini-KVM facilitates efficient device configuration and troubleshooting, it may not support the high-quality display requirements necessary for an optimal gaming experience. Our priority is on reliability and functionality for technical tasks rather than gaming.

### **Will there be support for high-quality display in future versions of the Openterface Mini-KVM?**

   - Yes, we are aware that there is significant interest in high-quality display capabilities among our users. While it is not our main focus at the moment, we are considering the inclusion of enhanced display features for a professional version of the Openterface Mini-KVM. We value the feedback from our community and aim to cater to the needs of our users in future product developments.

### **Why doesn't the Openterface Mini-KVM stream video over local IP or wireless video broadcast and support wireless keyboard and mouse control?**

   - The design philosophy behind the Openterface Mini-KVM emphasizes stable, wired control to ensure reliability and performance. By prioritizing direct connections through HDMI and USB, we aim to provide a seamless and efficient user experience, free from the potential instabilities and latency associated with wireless communications and network streaming. However, we are open to exploring these features in future versions of our device, as we continue to assess user needs and technological advancements.

### **Does it work with analog video outputs like VGA?**

   - Currently it only captures digital video via HDMI. VGA support may be added in the future. Simple analog conversion can be achieved using HDMI-to-VGA adapters.

### **Does the Openterface Mini-KVM support VLC for streaming video?**

   - No, the Openterface Mini-KVM does not support VLC for streaming video. This is because the device is not designed as a network-based solution, which is typically required for streaming applications like VLC. Our focus is on direct USB connectivity for device control and management, rather than network-dependent functionalities.

<section class="dialogue-section-white" id="dialogues-section">
    <div class="container">
    <div class="callout-button-container">
        <div class="dialogue-bubble" id="op-bubble">
         <img src="/images/op-avatar.jpg" alt="Avatar" class="avatar" draggable="false">
         <p>Question?🤔</p>
         <a href="https://www.reddit.com/r/Openterface_miniKVM/" class="md-button md-button--primary" id="join-waitlist-button">Ask in Subreddit</a>
         <!-- <a href="https://forms.gle/rwDDsMbs5pFwq7227" class="md-button md-button--primary" id="join-waitlist-button">Ask NOW</a> -->
        </div>
      <div class="dialogue-bubble" id="op-bubble">
        <img src="/images/op-avatar.jpg" alt="Avatar" class="avatar" draggable="false">
        <p>Read more 📖</p>
        <a href="/quick-start" class="md-button md-button--primary" id="join-waitlist-button">Docs</a>
      </div>
      <div class="dialogue-bubble" id="op-bubble">
        <img src="/images/op-avatar.jpg" alt="Avatar" class="avatar" draggable="false">
        <p>Be Our Backer! ❤️</p>
        <a href="https://www.crowdsupply.com/techxartisan/openterface-mini-kvm" class="md-button md-button--primary" id="join-waitlist-button">Go to Crowd Supply</a>
      </div>
    </div>
</section>