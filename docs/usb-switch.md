# Switchable USB Port Mechanics

The mini-KVM device features a switchable USB-A 2.0 port that can be toggled between the host and target computers, but not both simultaneously. This functionality is controlled by both a physical toggle switch and a software switch in the host application. This document explains the mechanics and logic behind these switches.

## Switch Types

- **Software Switch**: A toggle button in the host application.
      - Toggles the USB port connection between host and target computers

- **Hardware Switch**: A physical two-position toggle switch on the device.
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

- **State 1 (Synchronized, Connected to Host):**
      - Hardware Switch: Points to Host
      - Software Switch: Points to Host
      - USB Port Connection: Connected to Host

- **State 2 (Synchronized, Connected to Target):**
      - Hardware Switch: Points to Target
      - Software Switch: Points to Target
      - USB Port Connection: Connected to Target

- **State 3 (Out of Sync, USB Connected to Host):**
      - Hardware Switch: Points to Target
      - Software Switch: Points to Host
      - USB Port Connection: Connected to Host

- **State 4 (Out of Sync, USB Connected to Target):**
      - Hardware Switch: Points to Host
      - Software Switch: Points to Target
      - USB Port Connection: Connected to Target

## State Transitions and Logic

### From State 1 (Both switches point to Host)

- ***Scenario 1A***: User Moves Hardware Switch to Target
      - Update internal state variable to Target
      - Update host application display to show Target
      - Switch actual circuit connection to Target 
      - Transition to State 2

- ***Scenario 1B***: User Clicks Software Switch to Target
      - Update internal state variable to Target
      - Hardware switch position remains unchanged (pointing to Host)
      - Switch actual circuit connection to Target 
      - Transition to State 3

### From State 2 (Both switches point to Target)

- ***Scenario 2A***: User Moves Hardware Switch to Host:
      - Update internal state variable to Host
      - Update software switch display to show Host
      - Switch actual circuit connection to Host 
      - Transition to State 1

- ***Scenario 2B***: User Clicks Software Switch to Host:
      - Update internal state variable to Host
      - Hardware switch position remains unchanged (pointing to Target)
      - Switch actual circuit connection to Host 
      - Transition to State 4

### From State 3 (Hardware: Target, Software: Host)

- ***Scenario 3A***: User Moves Hardware Switch to Target:
      - No changes to variables
      - Transition to State 2

- ***Scenario 3B***: User Clicks Software Switch to Host:
      - Update internal state variable to Host
      - Hardware switch position remains unchanged (pointing to Target)
      - Switch actual circuit connection to Host 
      - Transition to State 1

### From State 4 (Hardware: Host, Software: Target)

- ***Scenario 4A***: User Moves Hardware Switch to Host:
      - No changes to variables
      - Transition to State 1

- ***Scenario 4B***: User Clicks Software Switch to Target:
      - Update internal state variable to Target
      - Hardware switch position remains unchanged (pointing to Host)
      - Switch actual circuit connection to Target 
      - Transition to State 2

!!! Note "User Guidance"
    - **Resolving Mismatched States:** Any manual toggle of the Hardware Switch will resolve the out-of-sync condition present in State 3 or 4, aligning its state with the Software Switch to either State 1 or 2. However, this synchronization does not necessarily alter the actual circuit connection.
    
    - **Software Switch Controls the USB Connection:** Regardless of the hardware switch position, clicking the software switch will immediately change the circuit direction.

    - The Hardware Switch, while physical, is monitored by software and does not directly control the circuit direction. The software interprets the switch position and manages the actual circuit switching.