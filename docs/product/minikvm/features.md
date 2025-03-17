---
title: "Features & Capabilities"
description: "Explore Openterface Mini-KVM's powerful features: BIOS-level access, 4K video support, cross-platform compatibility, and USB sharing. A comprehensive overview of capabilities for headless computer control with no network required."
keywords: "Mini-KVM features, KVM switch capabilities, BIOS access, headless control, 4K KVM, USB sharing, cross-platform KVM, text transfer, plug and play KVM, open source KVM"
---

# **Features & Capabilities** | Openterface Mini-KVM

<iframe 
  width="560" 
  height="315" 
  src="https://www.youtube.com/embed/r3HNUflWGOY?si=84Ek6F9ocHmmGTqW" 
  title="YouTube video player" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
  referrerpolicy="strict-origin-when-cross-origin" 
  allowfullscreen>
</iframe>

- **BIOS-Level Access**  
  Provides direct access to the target device's BIOS, firmware, or startup management.

- **Network Independence**  
  Offers stable and fast, headless control using HDMI video capture and emulated keyboard/mouse (HID) input. No network connection required.

- **Full HD Output with Low Latency & 4K Input**  
  Supports displaying up to 1920×1080 @ 30 Hz on the host app with under 140 ms latency, while capturing target video input at up to 4K. Also compatible with VGA, Micro HDMI, DVI, and other inputs via adapters. For more details, visit our [specifications](specifications) page.

- **Switchable USB Type-A Port**  
  Toggle USB access between the host and target to share a USB drive without replugging. Learn more on the [Switchable USB Port](../usb-switch) page.

- **Host App Across All Platforms**  
  Our [Host apps](/app) are compatible with macOS, Windows, Linux, and Android, ensuring seamless integration and optimal performance.

- **Text Transfer**  
  Effortlessly transmit text from the host computer to the target device by simulating keystrokes. This feature is particularly useful for quickly entering usernames, passwords, or snippets of code. It supports a wide range of ASCII characters, including symbols, punctuation, and non-alphanumeric characters, ensuring versatility in text input.

!!! warning "Limitations of the Text Transfer Feature"
    - **No Clipboard Integration**  
      This functionality solely emulates typing; it does not facilitate the transfer of non-textual content, such as images or formatted documents.

    - **Language Limitations**  
      Currently, it is limited to ASCII-based characters, which means it does not support languages that utilize non-ASCII scripts, such as Chinese, Japanese, or Korean.

    - **Text Length Considerations**  
      While this feature excels at transferring short text entries (like usernames, complex passwords, or code snippets), attempting to send large blocks of text may lead to performance issues or errors.

- **Plug-and-Play Convenience**  
  No additional software installation or configuration on the target device—control begins immediately upon connection, and no software traces are left behind.

- **Ultra-Portable Design**  
  Compact and lightweight, perfect for professionals who need to work on various systems while on the move.

- **Audio Integration**  
  Captures and plays audio from the target device directly on the host computer.

- **Extension Pins for Further Development**  
  The Openterface Mini-KVM includes [extension pins](../extension-pins) that allow for advanced development and experimentation. These pins enable users to explore new functionalities and customize their device for specific needs.

- **Completely Open-Source**  
  The Openterface Mini-KVM is [fully open-source](/compliance), with both hardware and software available for study, modification, and distribution. This commitment to open-source principles ensures transparency and encourages [community-driven innovation](/discord).
