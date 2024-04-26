---
comments: true
tags:
  - File Transfer
  - mini-KVM
  - Switchable USB
  - BIOS
---

# Frequently Asked Questions (FAQs)

We're absolutely delighted to have you here! 🌟 This section is designed to address frequently asked questions about the Openterface Mini-KVM, which our team organises periodically. Feel free to drop your comments below. You can ask new questions directly too if you cannot find what you're looking for. 📝 Additionally, why not join our vibrant community on our subreddit at [/r/Openterface_miniKVM/](https://www.reddit.com/r/Openterface_miniKVM/) or our Discord Server [TechxArtisan](https://discord.gg/4khsrbGS), to engage and chat with fellow enthusiasts? If you would like to contact our team directly, please use this [Google form](https://forms.gle/rwDDsMbs5pFwq7227). We'd LOVE to hear from you! ❤️

## Basic

???+ faq "Basic"
      <details class="faq">
         <summary>What is the Openterface mini-KVM?</summary>
         The Openterface Mini-KVM is a portable device that allows control over another computer through [USB and HDMI connection](/quick-start/#connection). This KVM-over-USB solution captures video via HDMI and simulates a keyboard and mouse input. It enables to use your own laptop to display and control the target device directly. This tool is handy for tech enthusiasts and IT professionals for configuring or troubleshooting headless devices without the need for extra monitor, keyboard and mouse, especially in cases where the network connection is unreliable or not available at all.
      </details>
      <details class="faq">
         <summary>What are the unique selling points of the Openterface Mini-KVM compared to similar products?</summary>
         The Openterface Mini-KVM stands out for its plug-and-play functionality, direct BIOS-level access, portable design, and a switchable USB-A port shared between host and target. It offers a stable and fast control experience without network dependency, making it ideal for uncertain situations where network access is limited or unreliable. It is about using your own laptop effectivly to do configuring for headless device: plug in, do things, and then move on to next one, without concern of network.
      </details>
      <details class="faq">
         <summary>What are use cases for this mini-KVM?</summary>
         Please check out this page: [Use Cases](/use-cases)
      </details>
      <details class="faq">
         <summary>What host computers are compatible with the Openterface Mini-KVM?</summary>
         To use this mini-KVM, the host computer must install one of these [host applications](/quick-start/#install-host-application) to support MacOS, Windows and Linux. Web-based extension and Android apps are currently under development.
      </details>
      <details class="faq">
         <summary>What target devices are compatible with the Openterface Mini-KVM?</summary>
         No pre-installation or configuration is required on the target device. As long as the target device supports UI operations with video output (HDMI, VGA, e.g.) and has a USB port to receive emulated keyboard and mouse control (HID) signals, it can be used. Thus, Supported target device platforms include Windows, macOS, Linux, Android, and iOS.
      </details>
      <details class="faq">
         <summary>Can the Openterface Mini-KVM support file transfers between the host and target device?</summary>
         <p>Yes, the Openterface Mini-KVM includes a switchable USB-A port shared between the host and target devices. With a USB stick/disk plugged into this port, files can be transferred between host and target by following these steps:</p>
         <ol>
            <li>Mount a USB stick drive on the host when the small black switch is on the side of the host's Type-C port.</li>
            <li>Copy the files onto this mounted drive.</li>
            <li>After copying, unmount the drive without physically unplugging it.</li>
            <li>Flip the small black switch to the other side. This action switches the USB-A port's connection to the target.</li>
            <li>Mount the USB stick on the target device and copy/move files off the drive, completing the transfer process of files from host to target.</li>
         </ol>
         <p>This method can also be used in the opposite direction.</p>
      </details>
      <details class="faq">
         <summary>Can the switchable USB-A port be toggled at the software level? Could this be achieved through a button instead?</summary>
         The current design does not support toggling at the software level; it can only be physically flipped for now. Implementing toggling at the software level would necessitate a new design, incorporating a button and an LED indicator (either green/blue or on/off) to signify whether the USB port is set to the host or target mode. Additionally, this would require the integration of an additional chip, leading to increased costs in both hardware and software development. The existing design represents a compromise, aimed at balancing between cost-efficiency and basic functionality. Despite the potential for increased costs, we are interested in incorporating this feature in a future version for better user experience.
      </details>
      <details class="faq">
         <summary>Will there be technical support and documentation available for the Openterface Mini-KVM?</summary>
         <ul>
            <li>Extensive documentation for the Openterface Mini-KVM can be found on our website at <a href="https://www.openterface.com/">Openterface.com</a>. We continuously update these resources to optimize your experience with the device.</li>
            <li>For technical support, we invite you to join our <a href="https://www.reddit.com/r/Openterface_miniKVM/">subreddit</a>, a community-driven platform for sharing queries and insights among fellow users and our expert team.</li>
            <li>If your issue remains unresolved, our team is available to provide further technical assistance. You can reach out via this <a href="https://forms.gle/rwDDsMbs5pFwq7227">form</a>.</li>
         </ul>
      </details>
      <details class="faq">
         <summary>What is the expected price point?</summary>
         Pricing is still being determined and will depend on production costs and demand. We're exploring options like crowdfunding. Knowing how many people would like to buy this Openterface mini-KVM in advance will be very helpful for us to plan and control production costs more effectively, leading to a more affordable price. Thus, if you are interested into buying our product, please join this [Be Our Backer](https://www.crowdsupply.com/techxartisan/openterface-mini-kvm).
      </details>

## Technical

???+ faq "Technical"
      <details class="faq">
         <summary>Is the Openterface Mini-KVM open-source?</summary>
         Plans to open-source the project are under consideration. Just bear with us a little longer; We need to tidy quite some things up for opening up. If you are interested into contributing, please do tell us via this [form](https://forms.gle/rwDDsMbs5pFwq7227). Stay tuned!
      </details>
      <details class="faq">
         <summary>Can I access a device's BIOS/firmware settings?</summary>
         Yes, the direct connection of the Openterface Mini-KVM enables access to low-level BIOS or firmware settings. This feature stands in contrast to software-based KVM solutions or remote control applications like TeamViewer and Zoom, which are typically not able to do BIOS-level interactions.
      </details>
      <details class="faq">
         <summary>How is video/data transmitted between devices?</summary>
         Video data is captured via HDMI and transmitted over USB 2.0 to the host computer for display. The switchable USB 2.0 port allows basic peripheral sharing. Future versions may offer higher throughput connections with USB 3.
      </details>
      <details class="faq">
         <summary>How does the Openterface Mini-KVM handle power supply and consumption?</summary>
         The device does not require an external power supply, as it is designed to be powered through its Type-C connections from the host, enhancing its portability. In scenarios where the target device is a low-power micro-computer, such as a Raspberry Pi, it could be powered through the host via the Mini-KVM's switchable USB port. However, this is not recommended. The standard method of operation is to have an external power supply to the target device.
      </details>

## Control Mechanism

???+ faq "Control Mechanism"
      <details class="faq">
         <summary>Are there plans for a version with wireless or Ethernet connectivity?</summary>
         <ul>
            <li>There are no immediate plans for us to support wireless or Ethernet connectivity in our Openterface products, as the focus of this mini-KVM is on fast, stable, direct control over USB to a target device, without concern of network condition.</li>
            <li>If we change our mind on this matter, we will keep [our community](https://www.reddit.com/r/Openterface_miniKVM/) updated 😃</li>
            <li>Nevertheless, please feel free to [share](https://forms.gle/rwDDsMbs5pFwq7227) your thoughts with us, if you really can not find a satisfying KVM-over-IP out there in the market.</li>
         </ul>
      </details>
      <details class="faq">
         <summary>How is this different from other KVM solutions like traditional KVMs, KVM-over-IP and VNC, etc?</summary>
         Please go to the page [Comparison](/comparison) for more details there.
      </details>
      <details class="faq">
         <summary>Does it work with PS/2 output to control the target?</summary>
         Consideration for supporting a built-in PS/2 interfaces is part of our future development plan.
      </details>

## Video Related

???+ faq "Video Related"
      <details class="faq">
         <summary>What about video latency and resolution?</summary>
         The device is engineered to handle 1080p video with minimal latency, ensuring a seamless control experience.
      </details>
      <details class="faq">
         <summary>Is the Openterface Mini-KVM suitable for high-quality gaming?</summary>
         Currently, our device is designed with a focus on providing direct control of target devices for technical / IT operations rather than prioritising high-resolution display output for gaming. As such, while the Openterface Mini-KVM facilitates efficient device configuration and troubleshooting, it may not support the high-quality display requirements necessary for an optimal gaming experience. Our priority is on reliability and functionality for technical tasks rather than gaming.
      </details>
      <details class="faq">
         <summary>Will there be support for high-quality display in future versions of the Openterface Mini-KVM?</summary>
         Yes, we are aware that there is significant interest in high-quality display capabilities among our users. While it is not our main focus at the moment, we are considering the inclusion of enhanced display features for a professional version of the Openterface Mini-KVM. We value the feedback from our community and aim to cater to the needs of our users in future product developments.
      </details>
      <details class="faq">
         <summary>Why doesn't the Openterface Mini-KVM stream video over local IP or wireless video broadcast and support wireless keyboard and mouse control?</summary>
         The design philosophy behind the Openterface Mini-KVM emphasizes stable, wired control to ensure reliability and performance. By prioritizing direct connections through HDMI and USB, we aim to provide a seamless and efficient user experience, free from the potential instabilities and latency associated with wireless communications and network streaming. However, we are open to exploring these features in future versions of our device, as we continue to assess user needs and technological advancements.
      </details>
      <details class="faq">
         <summary>Does it work with analog video outputs like VGA?</summary>
         Currently it only captures digital video via HDMI. VGA support may be added in the future. Simple analog conversion can be achieved using HDMI-to-VGA adapters.
      </details>
      <details class="faq">
         <summary>Does the Openterface Mini-KVM support VLC for streaming video?</summary>
         No, the Openterface Mini-KVM does not support VLC for streaming video. This is because the device is not designed as a network-based solution, which is typically required for streaming applications like VLC. Our focus is on direct USB connectivity for device control and management, rather than network-dependent functionalities.
      </details>

<section class="dialogue-section-white" id="dialogues-section">
    <div class="container">
    <div class="callout-button-container">
        <div class="dialogue-bubble" id="op-bubble">
         <img src="/images/op-avatar.jpg" alt="Avatar" class="avatar" draggable="false">
         <p>Question?🤔</p>
         <a href="https://www.reddit.com/r/Openterface_miniKVM/" class="md-button md-button--primary" id="join-waitlist-button">Ask in Subreddit</a>
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