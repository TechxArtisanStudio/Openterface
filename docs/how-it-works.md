# How It Works

## Process Breakdown

- **Screen Streaming**: The mini-KVM captures the screen stream from the target computer and displays it on the host computer’s app. This allows users to view and manage the target system directly from their host machine.
- **Cursor and Mouse Control**: By moving the mouse to the app window on the host computer, users can control the cursor on the target device as if they were using a VNC. This functionality enables operating two systems simultaneously on one screen.
- **Keyboard Input**: When the app window is active, any keystrokes made on the host computer’s keyboard are transmitted to the target device, allowing for seamless typing and command entry.
- **HID Signal Conversion**: All keyboard and mouse inputs within the app are converted into Human Interface Device (HID) control signals, which are then sent to the target computer.
- **Synchronization**: The app ensures that the target computer’s screen and cursor are synchronized with the host computer’s display, facilitating a unified user experience.

## Explore Hardware Details

- [Openterface_Mini-KVM_Hardware](https://github.com/TechxArtisan/Openterface_Mini-KVM_Hardware): Explore our comprehensive hardware design, schematics, and components.

![openterface-mini-kvm-product-with-PCB](/images/product/openterface-mini-kvm-product-with-PCB.jpg)

<section class="dialogue-section-white" id="dialogues-section">
    <div class="container">
        <div class="callout-button-container">
            <div class="dialogue-bubble" id="op-bubble">
                <img src="/images/op-avatar.jpg" alt="Avatar" class="avatar" draggable="false">
                <p>Read more 📖</p>
                <a href="/faq" class="md-button md-button--primary" id="join-waitlist-button">FAQs</a>
            </div>
            <div class="dialogue-bubble" id="op-bubble">
                <img src="/images/op-avatar.jpg" alt="Avatar" class="avatar" draggable="false">
                <p>Question?🤔</p>
                <a href="https://www.reddit.com/r/Openterface_miniKVM/" class="md-button md-button--primary" id="join-waitlist-button">Ask in Subreddit</a>
            </div>
        </div>
    </div>
</section>