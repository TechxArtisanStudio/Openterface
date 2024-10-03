# Switchable USB Port Mechanics

![switch-graphics](images/product/switch-graphics.svg#only-light){:style="width:460px"}
![switch-graphics](images/product/switch-graphics_1.svg#only-dark){:style="width:460px"}

The mini-KVM device features a switchable USB-A 2.0 port that can be toggled between the host and target computers, but not both simultaneously. This functionality is controlled by both a physical toggle switch and a software switch in the host application. This document explains the mechanics and logic behind these switches.

## Switch Types

- **Software Switch**: A toggle button in the host application.
      - Toggles the USB port connection between host and target computers

- ![Toggle Switch](images/shell-icons/toggle-h-t.svg#only-light){:style="height:20px"} ![Toggle Switch](images/shell-icons/toggle-h-t_1.svg#only-dark){:style="height:20px"} **Hardware Switch**: A physical two-position toggle switch on the device.
      - Inward position: Connects to the host computer
      - Outward position: Connects to the target computer

## Initial Setup and Synchronization

When the mini-KVM is properly connected and the host app is launched:

1. The device's actual USB port connection (circuit) initially defaults to the host connection.
2. The host app detects the current position of the hardware switch, which is set to either the Host or Target computer.
3. The software switch synchronizes with the hardware switch position.
4. The actual circuit connection is updated to match the switch positions.

!!! warning "Hardware Limitation"
    If a USB drive is already plugged into the device before powering on or launching the host application, the host computer will issue a warning about unsafe USB device removal. This is a hardware limitation for v1.9. Thus, it is recommended not to connect any USB device before powering up the device or starting our host app.

## Operational States

Due to the presence of both hardware and software switches, four possible states can occur:

- **State 1** (Synchronized, Connected to Host):
      - Hardware Switch: Points to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}
      - Software Switch: Points to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}
      - USB Port Connection: Connected to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}

- **State 2** (Synchronized, Connected to Target):
      - Hardware Switch: Points to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}
      - Software Switch: Points to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}
      - USB Port Connection: Connected to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}

- **State 3** (Out of Sync, USB Connected to Host):
      - Hardware Switch: Points to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}
      - Software Switch: Points to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}
      - USB Port Connection: Connected to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}

- **State 4** (Out of Sync, USB Connected to Target):
      - Hardware Switch: Points to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}
      - Software Switch: Points to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}
      - USB Port Connection: Connected to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}

## State Transitions and Logic

### From **State 1** (Sync to Host)

- ^^***Scenario 1a***^^: User Moves Hardware Switch to Target
      - Update internal state variable to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}
      - Update host application display to show Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}
      - Switch actual circuit connection to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}
      - Transition to State 2, sync

- ***Scenario 1b***: User Clicks Software Switch to Target
      - Update internal state variable to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}
      - Hardware switch position remains unchanged (pointing to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"})
      - Switch actual circuit connection to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}
      - Transition to State 3, out of sync

### From **State 2** (Sync to Target)

- ^^***Scenario 2a***^^: User Moves Hardware Switch to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}:
      - Update internal state variable to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}
      - Update software switch display to show Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}
      - Switch actual circuit connection to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}
      - Transition to State 1, sync

- ***Scenario 2b***: User Clicks Software Switch to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}:
      - Update internal state variable to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}
      - Hardware switch position remains unchanged (pointing to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"})
      - Switch actual circuit connection to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}
      - Transition to State 4, out of sync

### From **State 3** (Out of Sync, USB Connected to Host)

- ^^***Scenario 3a***^^: User Moves Hardware Switch to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}:
      - No changes to variables
      - Transition to State 2, sync

- ***Scenario 3b***: User Clicks Software Switch to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}:
      - Update internal state variable to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}
      - Hardware switch position remains unchanged (pointing to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"})
      - Switch actual circuit connection to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}
      - Transition to State 1, sync

### From **State 4** (Out of Sync, USB Connected to Target)

- ^^***Scenario 4a***^^: User Moves Hardware Switch to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"}:
      - No changes to variables
      - Transition to State 1, sync

- ***Scenario 4b***: User Clicks Software Switch to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}:
      - Update internal state variable to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}
      - Hardware switch position remains unchanged (pointing to Host ![host-computer](images/shell-icons/host-computer.svg#only-light){:style="height:18px"} ![host-computer](images/shell-icons/host-computer_1.svg#only-dark){:style="height:18px"})
      - Switch actual circuit connection to Target ![target-computer](images/shell-icons/target-computer.svg#only-light){:style="height:18px"} ![target-computer](images/shell-icons/target-computer_1.svg#only-dark){:style="height:18px"}
      - Transition to State 2, sync

!!! warning "Remember to eject the flash drive before toggling the switch"
    If the USB port is being used by a flash drive, ensure you eject the flash drive before toggling the switch to transfer the port's use to another computer.

!!! warning "USB power limitations"
    The power supplied by the USB port depends on the Host motherboard. It is not recommended to connect USB devices that require a lot of power. Typically, the power consumption should not exceed 1.5W. Connecting high-power devices may result in unstable operation or potential damage.

!!! Note "User Guidance"
    - **Software Switch Priority**: Regardless of the hardware switch position, clicking the software switch will immediately change the circuit direction.

    - **Hardware Switch Sync**: Any manual toggle of the Hardware Switch will align its state with the Software Switch, transitioning to either State 1 or State 2 from the out-of-sync State 3 or State 4. However, this synchronization does not necessarily alter the actual circuit connection.

    - **Hardware Switch Monitoring**: The Hardware Switch, despite being physical, is monitored by software and does not directly control the circuit direction. Instead, the software interprets the switch position and manages the actual circuit switching.

## Why Software-Controlled USB Switching Matters

The software-controlled USB switching enhancement introduced in v1.9 is a pivotal feature for our future development plans, particularly in supporting KVM-over-IP solutions like VNC (which we have not yet implemented). This capability allows users to remotely toggle and share the USB port between the target and host computers, which is especially crucial for facilitating file transfers in a remote setup.

This feature opens up a world of possibilities for remote management and control. For instance, it enables file transfers between devices without physical intervention, enhancing the efficiency of remote troubleshooting and system management.

Do you have creative ideas on how to leverage this feature? We'd love to chat with you! Join Openterface [community](/community/) and share your thoughts 😃
