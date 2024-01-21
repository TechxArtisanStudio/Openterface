# Hardware Explanation

## Hardware Components
* Serial communication module: connected to the host via USB interface and bridging communication with CH9329 module.
* CH9329 chip: responsible to decode serial signals from the host computer into keyboard and mouse events, acted as a keyboard mouse simulator and controlling the target computer.
* HDMI Capture module: responsible to capture video signal of the target’s screen via HDMI cable, do video transcoding and deliver video steaming as a webcam-like signal to the host via USB interface.