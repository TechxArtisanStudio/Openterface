# FAQs for Apps

Welcome to the FAQ for our apps. If you don’t find the answer you need, **email us at [info@openterface.com](mailto:info@openterface.com)** or **join our community** on [Discord](/discord) or [Reddit](/reddit) to connect with our dev team and fellow users.

⚠️ *FAQs may become outdated — please let us know if you spot anything that needs updating!*

### :material-clipboard-list: List of Questions

- [Where can I download the host applications?](#host-app-download)
- [Why do features differ across different host apps?](#host-app-differences)
- [Which host app currently offers the best experience?](#best-host-app)
- [Is there a host app supporting ChromeOS?](#host-app-chromeos)
- [Is there a host app supporting Apple's mobile devices?](#host-app-ios)
- [What if F11 doesn't work on macOS applications?](#f11-macos-issue)

#### :material-chat-question:{ .faq } Where can I download the host applications? {: #host-app-download }

Visit our [Install Host Application page](/quick-start/#install-host-application) for official downloads to support **MacOS, Windows, Linux and Android**. 

??? warning "Privacy & Security: Be cautious when using third-party host app"
    As our project is open source, you may find alternative versions of host applications compatible with our Mini-KVM developed by others. While these can offer additional features, please ensure you review their security and privacy practices. **The Openterface Team cannot guarantee or be responsible for the safety of third-party applications**.

#### :material-chat-question:{ .faq } Why do features differ across different host apps? {: #host-app-differences }

Our dev team actively maintains host applications for macOS, Linux, Windows, and Android, but due to platform-specific challenges and limited resources, development progress varies. That means some features might appear first on one platform and take longer to arrive on others.

We're doing our best to sync feature development across all platforms, but it’s a work in progress. 

Your feedback plays a big role in shaping our development roadmap — whether through our [community](/community/) or [GitHub repository](/app/). Every suggestion helps us prioritize what matters most to you!

If you're a developer, your contributions are incredibly valuable — and we’d love your help in speeding up the process!

#### :material-chat-question:{ .faq } Which host app currently offers the best experience? {: #best-host-app }

As of March 2025, the Qt-based host apps for Windows and Linux offer the most comprehensive feature set overall. The macOS version stands out for its smoothest and most refined user experience, thanks to deeper system integration and UI enhancements. The Android app is a convenient option on the go, with more features steadily catching up.

#### :material-chat-question:{ .faq } Is there a web app I can use on Chrome or other platforms? {: #host-app-chromeos }

Yes! One of our awesome community members, [Kashall](https://github.com/kashalls/openterface-viewer/), built **a lightweight open-source web app** you can use directly in your browser: [openterface-viewer.pages.dev](https://openterface-viewer.pages.dev). It’s not yet part of our official documentation, but our dev team gave it a spin and found it solid, easy to use, and super handy — especially on Chrome or when you want something quick and browser-based. Give it a try!

#### :material-chat-question:{ .faq } Is there a host app supporting Apple's mobile devices? {: #host-app-ios }

We are currently exploring compatibility with Apple's mobile systems, such as iOS and iPadOS. Due to Apple's stringent controls, these platforms may not support wired connections with third-party devices. However, the situation could change, or there might be potential workarounds. If you have any insights or suggestions, we welcome you to join our community to discuss them with us. We are committed to enhancing the convenience of our device by supporting as many systems as possible. If you're keen to help out with our development, come hang out with us in the community or shoot us an email!

#### :material-chat-question:{ .faq } What if F11 doesn't work on macOS applications? {: #f11-macos-issue }

On macOS, pressing F11 shows the macOS desktop instead of passing the F11 key to the app and the target computer. To fix this, you can unbind F11 from the "Show Desktop" function.

???+ info "Fixing F11 Key Issue on macOS"
    1. Go to **System Settings**.  
    2. Select **Desktop & Dock**.  
    3. Scroll down and click the **"Shortcuts…"** button.  
    4. Find **"Show Desktop"** and set it to the hyphen **(-)** at the bottom of the dropdown list.  
    5. This change will allow the F11 key to pass through to your application on the target computer.  