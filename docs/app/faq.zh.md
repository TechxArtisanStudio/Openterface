# 应用常见问题

欢迎来到我们应用的常见问题页面。如果您找不到需要的答案，请**发邮件至 [info@openterface.com](mailto:info@openterface.com)** 或**加入我们的社区** [Discord](/discord) 或 [Reddit](/reddit) 与我们的开发团队和其他用户联系。

⚠️ *常见问题可能会过时——如果您发现任何需要更新的内容，请告诉我们！*

### :material-clipboard-list: 问题列表

- [在哪里可以下载主机应用程序？](#host-app-download)
- [为什么不同主机应用的功能有所不同？](#host-app-differences)
- [目前哪个主机应用提供最佳体验？](#best-host-app)
- [是否有支持ChromeOS的主机应用？](#host-app-chromeos)
- [是否有支持Apple移动设备的主机应用？](#host-app-ios)
- [如果F11在macOS应用中不起作用怎么办？](#f11-macos-issue)

#### :material-chat-question:{ .faq } 在哪里可以下载主机应用程序？ {: #host-app-download }

访问我们的[安装主机应用程序页面](/quick-start/#install-host-application)获取支持**MacOS、Windows、Linux和Android**的官方下载。

??? warning "隐私与安全：使用第三方主机应用时请谨慎"
    由于我们的项目是开源的，您可能会发现其他人开发的与我们Mini-KVM兼容的主机应用程序的替代版本。虽然这些可以提供额外功能，但请确保您审查其安全和隐私实践。**Openterface团队无法保证或对第三方应用程序的安全性负责**。

#### :material-chat-question:{ .faq } 为什么不同主机应用的功能有所不同？ {: #host-app-differences }

我们的开发团队积极维护macOS、Linux、Windows和Android的主机应用程序，但由于平台特定的挑战和有限的资源，开发进度各不相同。这意味着某些功能可能首先出现在一个平台上，而在其他平台上需要更长时间才能到达。

我们正在尽最大努力在所有平台上同步功能开发，但这仍在进行中。

您的反馈在塑造我们的开发路线图方面发挥着重要作用——无论是通过我们的[社区](/community/)还是[GitHub仓库](/app/)。每个建议都帮助我们优先考虑对您最重要的事情！

如果您是开发者，您的贡献非常有价值——我们很乐意您的帮助来加速这个过程！

#### :material-chat-question:{ .faq } 目前哪个主机应用提供最佳体验？ {: #best-host-app }

截至2025年3月，基于Qt的Windows和Linux主机应用提供最全面的功能集。macOS版本因其最流畅和最精致的用户体验而脱颖而出，这得益于更深的系统集成和UI增强。Android应用在移动中是一个方便的选择，更多功能正在稳步赶上。

#### :material-chat-question:{ .faq } 是否有我可以在Chrome或其他平台上使用的网络应用？ {: #host-app-chromeos }

是的！我们的一位出色的社区成员[Kashall](https://github.com/kashalls/openterface-viewer/)构建了**一个轻量级的开源网络应用**，您可以直接在浏览器中使用：[openterface-viewer.pages.dev](https://openterface-viewer.pages.dev)。它还不是我们官方文档的一部分，但我们的开发团队试用了一下，发现它稳定、易用且超级方便——特别是在Chrome上或当您想要快速且基于浏览器的解决方案时。试试看！

#### :material-chat-question:{ .faq } 是否有支持Apple移动设备的主机应用？ {: #host-app-ios }

我们目前正在探索与Apple移动系统（如iOS和iPadOS）的兼容性。由于Apple的严格控制，这些平台可能不支持与第三方设备的有线连接。但是，情况可能会改变，或者可能有潜在的解决方案。如果您有任何见解或建议，我们欢迎您加入我们的社区与我们讨论。我们致力于通过支持尽可能多的系统来增强我们设备的便利性。如果您热衷于帮助我们的开发，请来社区与我们交流或给我们发邮件！

#### :material-chat-question:{ .faq } 如果F11在macOS应用中不起作用怎么办？ {: #f11-macos-issue }

在macOS上，按F11会显示macOS桌面，而不是将F11键传递给应用程序和目标计算机。要修复此问题，您可以从"显示桌面"功能中解绑F11。

???+ info "修复macOS上的F11键问题"
    1. 转到**系统设置**。
    2. 选择**桌面与程序坞**。
    3. 向下滚动并点击**"快捷键…"**按钮。
    4. 找到**"显示桌面"**并将其设置为下拉列表底部的连字符**(-)**。
    5. 此更改将允许F11键传递到目标计算机上的应用程序。
