# KVM-GO Beta Quick Start Guide

> Drafted with ❤️ by [Iker](https://github.com/IkerGarcia) from the Openterface community — thank you for helping us build better docs!

Welcome to [the KVM-GO beta](/product/kvm-go/updates/251007-kvm-go-beta-test-kits-sent-1/)! Below is a quick guide version of the beta feedback questionnaire. Follow each section, capture your findings, and please submit everything through the [Google Form beta feedback questionnaire](https://openterface.com/product/kvm-go/beta-questions) when you're done.

Congratulations on being selected as a beta tester! We are really excited to get your feedback; we are sure you will be able to thoroughly test this device in different scenarios!

This test allows for flexible testing, but we’d love for you to focus on a few specific scenarios.

Your feedback is incredibly valuable to us, and while you’re welcome to test other aspects of the device, here are some key areas we'd like to explore:

1. **Extended Idle Testing**

    1. Launch the software and connect to a target
    2. Leave the software running without interaction for an extended period (several hours)
    3. Return and attempt to use mouse and keyboard controls
    - After leaving the software idle, did the mouse and keyboard work normally when you returned?

2. **Hot-Plug Testing**

    - Please test unplugging and reconnecting the device while the software is running.

3. **BIOS & Low-Level Access**

4. **Copy & Paste (both short and long text)**

5. **Device Simulation Settings (Windows/Linux)**

    - 5.1. Display EDID Configuration
    - 5.2. USB Device Identification (VID/PID)
    - 5.3. SD Card Functionality
        - Use Case 1 - System Installation: We recommend trying Ventoy - a tool that allows multiple ISO files on one SD card and lets you choose which to boot. Did you try writing a system image on HOST, then switching to TARGET for installation (without removing the card)?
        - Use Case 2 - File Transfer:  Did you use SD card for file transfer between HOST and TARGET?

These are some examples of things that will be asked in the beta feedback form, together with general information about audio/video/keyboard/mouse consistency or heat management.

Thank you for your help!

!!! reminder "Don't forget"
    Submit your completed observations via the Google Form so the team can review them promptly.
