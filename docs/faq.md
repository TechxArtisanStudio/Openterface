---
comments: true
tags:
  - File Transfer
  - mini-KVM
  - Switchable USB
  - BIOS
---

# Frequently Asked Questions (FAQs)

We're absolutely delighted to have you here! 🌟 This section is designed to address frequently asked questions about the Openterface Mini-KVM, which our team organises periodically. 

Let's delve into the most frequent questions about the Openterface Mini-KVM.

### List of Questions

##### Basic
- [What is Openterface Mini-KVM?](#what-is-openterface-mini-kvm)
- [Why does Openterface Mini-KVM make a difference?](#why-openterface-mini-kvm-make-a-difference)
- [What are the use cases for this mini-KVM?](#what-are-use-cases-for-this-mini-kvm)
- [What host computers are compatible with the Openterface Mini-KVM?](#what-host-computers-are-compatible-with-the-openterface-mini-kvm)
- [What target devices are compatible with the Openterface Mini-KVM?](#what-target-devices-are-compatible-with-the-openterface-mini-kvm)
- [Will there be technical support and documentation available for the Openterface Mini-KVM?](#will-there-be-technical-support-and-documentation-available-for-the-openterface-mini-kvm)

##### Software  

- [Where can I download the host applications?](#where-can-i-download-the-host-applications)
- [When will the host app for Android be available?](#when-will-the-host-app-for-android-be-available)
- [Is there a host app supporting ChromeOS?](#is-there-a-host-app-supporting-chromeos)
- [Is there a host app supporting Apple's mobile devices?](#is-there-a-host-app-supporting-apples-mobile-devices)
- [What if F11 doesn't work on MacOS applications?](#what-if-f11-doesnt-work-on-macos-applications)

##### Switchable USB Port & File Transfer
- [Can the Openterface Mini-KVM support file transfers?](#can-the-openterface-mini-kvm-support-file-transfers)
- [Can the switchable USB-A port be toggled at the software level?](#can-the-switchable-usb-a-port-be-toggled-at-the-software-level)
- [Why USB 2.0 but not USB 3.0 for this switchable USB port?](#why-usb-20-but-not-usb-30-for-this-switchable-usb-port)  

##### Technical
- [Is the Openterface Mini-KVM open-source?](#is-the-openterface-mini-kvm-open-source)
- [Can I access a device's BIOS settings?](#can-i-access-a-devices-bios-settings)
- [How is video/data transmitted between devices?](#how-is-videodata-transmitted-between-devices)
- [How does the Openterface Mini-KVM handle power?](#how-does-the-openterface-mini-kvm-handle-power)

##### Control Mechanism
- [Are there plans for a version with wireless or Ethernet connectivity?](#are-there-plans-for-a-version-with-wireless-or-ethernet-connectivity)
- [How is this different from other KVM solutions like traditional KVMs, KVM-over-IP, VNC, etc?](#how-is-this-different-from-other-kvm-solutions-like-traditional-kvms-kvm-over-ip-and-vnc-etc)
- [Does it work with a target computer requiring PS/2?](#does-it-work-with-a-target-computer-requiring-ps2)
- [Can I use multiple Mini-KVMs to control multiple target devices from one master computer?](#can-i-use-multiple-mini-kvms-to-control-multiple-target-devices-from-one-master-computer)  

##### Video Related
- [What about video latency and resolution?](#what-about-video-latency-and-resolution)
- [Is the Openterface Mini-KVM suitable for high-quality gaming?](#is-the-openterface-mini-kvm-suitable-for-high-quality-gaming)
- [Will there be support for high-quality display in future versions of the Openterface Mini-KVM?](#will-there-be-support-for-high-quality-display-in-future-versions-of-the-openterface-mini-kvm)
- [Why doesn't Openterface Mini-KVM stream video over local IP?](#why-doesnt-openterface-mini-kvm-stream-video-over-local-ip)
- [Can it work with different video outputs like VGA, DVI, DisplayPort, etc.?](#can-it-work-with-different-video-outputs-like-vga-dvi-displayport-etc)
- [Why can't I add the VGA-to-HDMI cable to my order on Crowd Supply for shipping to the EU/UK?](#why-cant-i-add-the-vga-to-hdmi-cable-to-my-order-on-crowd-supply-for-shipping-to-the-euuk)

##### More

- [How can I contribute into this project?](#how-can-i-contribute-into-this-project)
- [Want to Review Our Handy Gadget?](#want-to-review-our-handy-gadget)

### Basic

#### What is Openterface mini-KVM?
The Openterface Mini-KVM is a compact, feature-rich, and open-source KVM gadget driven by [a vibrant community](https://openterface.com/community/). It allows you to use your own laptop to display and control headless devices directly through a [USB and HDMI connection](https://openterface.com/quick-start/#connection-procedure). This KVM-over-USB solution captures video via HDMI and simulates keyboard and mouse inputs. It is particularly useful for [a wide range of applications](https://openterface.com/use-cases/), catering to tech enthusiasts exploring single-board computers, as well as IT professionals troubleshooting headless devices. It eliminates the need for additional monitors, keyboards, and mice, providing a convenient solution in environments where network connections are unreliable or unavailable.

#### Why Openterface Mini-KVM Make a Difference?
Our [Openterface Mini-KVM features](https://openterface.com/#product-features) a **portable design, plug-and-play ease, fast response time, and direct BIOS-level access with a switchable USB-A port**, all shared between host and target devices. It ensures a reliable and speedy control experience via HDMI and USB connection, free from the constraints of network dependency, making it suitable for various [use scenarios](https://openterface.com/use-cases/), especially for on-the-fly IT tasks and troubleshooting.

Moreover, unlike traditional KVM consoles that often come with a hefty price tag, our mini-KVM is designed to be accessible and **afforadable** to a broader spectrum of users, from IT professionals to tech enthusiasts.

But the real magic lies in our commitment to **open-source development** and **community engagement**. By embracing these principles, we’re building a vibrant ecosystem where users can collaborate, contribute, and customize the device to meet their unique needs, fostering innovation and pushing the boundaries of what’s possible.

#### What are use cases for this mini-KVM?
Please check out this page: [Use Cases](https://openterface.com/use-cases/)

#### What host computers are compatible with the Openterface Mini-KVM?
To use this mini-KVM, the host computer must install one of these [host applications](https://openterface.com/quick-start/#install-host-application) to support MacOS, Windows and Linux. A web-based extension and Android apps are currently under development.

#### What target devices are compatible with the Openterface Mini-KVM?
No pre-installation or configuration is required on the target device. As long as the target device supports UI operations with video output (e.g., HDMI, VGA) and has a USB port to receive emulated keyboard and mouse control (HID) signals, it can be used. Thus, supported target device platforms include Windows, MacOS, Linux, Android, and iOS.

#### Will there be technical support and documentation available for the Openterface Mini-KVM?
Extensive documentation for the Openterface Mini-KVM can be found on our website at [Openterface.com](https://www.openterface.com/). We continuously update these resources to optimize your experience with the device.  
For technical support, we invite you to join our [community](https://openterface.com/community/) for sharing queries and insights among fellow users and our expert team. If your issue remains unresolved, our team is available to provide further technical assistance. You can reach out via this email: info@techxartisan.com.

### Software

#### Where can I download the host applications?
Visit our [Install Host Application page](https://openterface.com/quick-start/#install-host-application) for official downloads. As our project is open source, you may find alternative versions of host applications compatible with our mini-KVM developed by the community. While these can offer additional features, please ensure you review their security and privacy practices. TechxArtisan Studio cannot guarantee the safety of third-party applications. Thank you!

#### When will the host app for Android be available?
We are currently developing the host app for Android, but it is a lower priority compared to versions for mainstream operating systems like macOS, Windows, and Linux. We appreciate your patience and encourage you to stay tuned for updates. If you are interested in assisting with development, feel free to join our community or contact us via email!

#### Is there a host app supporting ChromeOS?
Yes, but it is currently under development. We are planning to create a web extension designed to support both Chrome and Firefox browsers. Although its development priority is slightly lower than that for mainstream operating systems such as macOS, Windows, and Linux, we are actively working on it. Please bear with us and stay tuned for updates! If you're keen to help out with our development, come hang out with us in the community or shoot us an email!

#### Is there a host app supporting Apple's mobile devices?
We are currently exploring compatibility with Apple's mobile systems, such as iOS and iPadOS. Due to Apple's stringent controls, these platforms may not support wired connections with third-party devices. However, the situation could change, or there might be potential workarounds. If you have any insights or suggestions, we welcome you to join our community to discuss them with us. We are committed to enhancing the convenience of our device by supporting as many systems as possible. If you're keen to help out with our development, come hang out with us in the community or shoot us an email!

#### What if F11 doesn't work on macOS applications?
On macOS, pressing F11 shows the macOS desktop instead of passing the F11 key to the app and the target computer. To fix this, you can unbind F11 from the "Show Desktop" function. Here’s how:

1. Go to System Settings.
2. Select Desktop & Dock.
3. Scroll down and click the "Shortcuts…" button.
4. Find "Show Desktop" and set it to the hyphen (-) at the bottom of the dropdown list.
5. This change will let the F11 key pass through to your application on the target computer.

### Switchable USB Port and File Transfer

#### Can the Openterface Mini-KVM support file transfers?
Yes, the Openterface Mini-KVM includes a switchable USB-A port shared between the host and target devices. With a USB stick/disk plugged into this port, files can be transferred between host and target by following these steps:

1. Mount a USB stick drive on the host when the small black switch is set to the side of the host's Type-C port.
2. Copy the files onto this mounted drive.
3. After copying, unmount the drive without physically unplugging it.
4. Flip the small black switch to the other side. This action switches the USB-A port's connection to the target.
5. Mount the USB stick on the target device and copy/move files off the drive, completing the transfer process of files from host to target.

This method can also be used in the opposite direction.

#### Can the switchable USB-A port be toggled at the software level?
The current design does not support toggling at the software level; it can only be physically flipped for now. 

Implementing toggling at the software level would necessitate a new design, incorporating a button and an LED indicator (either green/blue or on/off) to signify whether the USB port is set to the host or target mode. 

Additionally, this would require the integration of an additional chip, leading to increased costs in both hardware and software development. The existing design represents a compromise, aimed at balancing cost-efficiency and basic functionality. Despite the potential for increased costs, we are interested in incorporating this feature in a future version for better user experience.

#### Why USB 2.0 but not USB 3.0 for this switchable usb port?
USB 2.0 is fully capable of handling video capture at 1080p@30Hz, transmitting HID signals (for keyboard and mouse), and managing standard-speed file transfers between the target and host computers. This makes our product a speedy, lightweight, and portable solution, exactly as designed.

Using USB 3.0 would make the PCB design much more complex and significantly increase production costs. Additionally, while USB 3.0 does offer faster file transfers, it also generates more heat, which could shorten the lifespan of the device.

We are considering the application of USB 3.0 for the next version, targeting more professional use scenarios and stationary KVM solutions.

### Technical

#### Is the Openterface Mini-KVM open-source?
Yes! We will open source both [hardware](/how-it-works/#explore-hardware-details) and [software](https://openterface.com/quick-start/#install-host-application). Just bear with us a little longer; We need to tidy quite some things up for opening up. If you are interested in [contributing](/contributing/), please do tell us via this email: info@techxartisan.com. Stay tuned!

#### Can I access a device's BIOS settings?
Yes, the direct connection of the Openterface Mini-KVM enables access to low-level BIOS or firmware settings.

This feature stands in contrast to software-based KVM solutions or remote control applications like TeamViewer and Zoom, which are typically not capable of BIOS-level interactions.

#### Why doesn't the keyboard control work at the BIOS level for some older target computers?
It seems that some old computers' BIOS can't recognize our device's USB hub, which can cause issues with our emulated keyboard and mouse not working properly at the BIOS level. We're keeping an eye on this problem.

We've had a report that on one specific HP computer, the HP Engage Flex Pro, the keyboard doesn't work at the BIOS screen, though it functions normally once the operating system boots up.

If you encounter the same issue, please report it to us via a GitHub issue.

#### How is video/data transmitted between devices?
Video data is captured via HDMI and transmitted over USB 2.0 to the host computer for display. The switchable USB 2.0 port allows USB drive or other USB device sharing between the target and the host.

#### How does the Openterface Mini-KVM handle power?
The device does not require an external power supply, as it is designed to be powered through its USB Type-C connections from the host, enhancing its portability. In scenarios where the target device is a low-power micro-computer, such as a Raspberry Pi, it could be powered through the host via the Mini-KVM's switchable USB port. However, this is not recommended. The standard method of operation is to have an external power supply to the target device.

#### Can I DIY this device?
Absolutely! We're a bunch of passionate makers who love to DIY, and we are making sure this project is open source, both hardware and software, and updating its docs. You can technically build it from scratch. We’re even thinking about posting a guide on how to DIY a breadboard version of our product that would also be compatible with our software.

Our community is already experimenting with different hardware versions. Check out our community posts to learn more, or share your own DIY experiences! It could really enrich our community. Plus, you might find that with a few tweaks to the code, our software could work seamlessly with your creative DIY setup!

### Control Mechanism

#### Are there plans for a version with wireless or Ethernet connectivity?
Currently, we're not planning to add wireless or Ethernet connectivity to our Openterface products. We’re focused on providing fast, stable control over USB directly to your target device, so you don’t have to worry about network issues. 

But hey, we’re always open to feedback! If you think there’s a real need for this feature, or if you’re struggling to find a good KVM-over-IP solution, drop us an email: info@techxartisan.com. And remember, if we decide to expand our connectivity options, our [community](https://www.reddit.com/r/Openterface_miniKVM/) will be the first to know.

#### How is this different from other KVM solutions like traditional KVMs, KVM-over-IP, and VNC, etc?
Curious about how the Openterface Mini-KVM stacks up against other solutions? Check out our detailed [Comparison](https://openterface.com/comparison) page.

#### Does it work with a target computer requiring PS/2?
No. We are aware that there are still many old headless computers out there that require PS/2 keyboards and mice. As far as we know, there isn't yet an elegant solution for converting USB HID signals to split into PS/2 keyboard and mouse signals. We are still investigating this matter and considering how to support PS/2 in future versions of the Mini-KVM. If you know of any solutions that could elegantly work with our Mini-KVM, please share them with us. Thank you!

#### Can I use multiple Mini-KVMs to control multiple target deives from one master computer?
Yes, you can! Our Mini-KVM can technically handle this, but we’re still tweaking the code and running tests. We're focusing on making sure that our software can automatically link up the keyboard and mouse with the right video source when you use more than one Mini-KVM at a time. Also, we’re sprucing up the software's UI to make it better for this kind of setup. Stay tuned to our community updates for when we roll out this feature!

### Video Related

#### What about video latency and resolution?
Our device handles 1080p video with under 140 milliseconds of latency, making your control experience smooth and seamless.

#### Is the Openterface Mini-KVM suitable for high-quality gaming?
The current design focuses on technical and IT operations, providing reliable control for device configuration and troubleshooting rather than high-resolution gaming. While it’s great for many tasks, this mini-KVM might not meet the display needs of high-quality gaming.

#### Will there be support for high-quality display in future versions of the Openterface Mini-KVM?
We know a lot of you are looking for top-notch display features. While it’s not our main focus right now, based on your feedback, we’re considering adding enhanced display capabilities in a professional version of the Openterface Mini-KVM.

#### Why doesn't Openterface Mini-KVM stream video over local IP?
The Openterface Mini-KVM has been engineered to ensure reliable and stable performance through wired connections, using HDMI and USB. While it is technically feasible to stream video over a network via our host applications, we are considering adding a VLC, and even VNC feature to our host applications in the future.

#### Can it work with different video outputs like VGA, DVI, DisplayPort, etc.??
Sort of. The Openterface Mini-KVM captures video through an HDMI port. However, you can use various video adapters like [VGA-to-HDMI](https://openterface.com/use-cases/#streamlined-server-management), [DVI-to-HDMI](https://openterface.com/use-cases/#unified-control-for-diverse-devices), [miniHDMI-to-HDMI](https://openterface.com/use-cases/#simplified-setup-for-tech-enthusiasts), or DP-to-HDMI, to connect different video sources.

#### Why can't I add the VGA-to-HDMI cable to my order on Crowd Supply for shipping to the EU/UK?
We're still working on getting the CE certificate we need to sell and ship this cable to places like the EU and UK. Things are looking up, and we’re hopeful we’ll have it sorted out in a couple of weeks, maybe three, but definitely before June, so you’ll be able to add it to your orders soon. Keep an eye on [our community posts](https://www.reddit.com/r/Openterface_miniKVM/comments/1cjf8zi/working_on_ce_for_vgatohdmi_cable_for_euuk_backers/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) for updates. Thanks for hanging in there with us!

### More

#### How can I contribute into this project?
Absolutely! There are loads of ways you can chip in:

- If you're into coding, help us out by reporting and fixing bugs. 
- Good with words and tech? You could lend a hand with our documentation. 
- And if you’re a wizard with languages, why not help translate our docs to help more folks get on board?
- If design’s your thing, we’re always looking for fresh takes on graphic design, app UI, and making our device even more user-friendly. 
- Fancy helping to keep our community buzzing? We could use your skills there too.

Your support and [contributions](https://openterface.com/contributing/) are what keep Openterface Mini-KVM growing. Thanks for being part of our adventure! 🚀 Got the urge to help but don’t see a perfect fit? Just shoot us an email!

#### Want to Review Our Handy Gadget?
Hey, we love making noise and spreading the word about our Mini-KVM! If you're from the press or rocking it on social media and fancy taking our product for a spin, we're all ears. Whether you're into detailed reviews, unboxing videos, or just want to give us a shoutout, we're here for it and let's make some waves together! 🎉 Just drop us an email NOW!


--------

Your curiosity and support fuel our progress, and we want to ensure that every one of your questions finds an answer. Please note that as time progresses, the content above in our FAQs may become outdated. If your query isn't covered in this FAQ, always check our website [openterface.com](https://openterface.com/) for the most current information. Also please don’t hesitate to join our enthusiastic community. We’re active on our Subreddit at [/r/Openterface_miniKVM/](https://www.reddit.com/r/Openterface_miniKVM/) and our Discord server, [TechxArtisan](https://discord.gg/sFTJD6a3R8), where you can ask questions, share ideas, or just have a chat about all things tech.

Moreover, feel free to reach out directly to our dedicated team by sending an email to info@techxartisan.com. We love hearing from you and are always here to help!


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