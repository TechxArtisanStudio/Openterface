---
draft: false
date: 2024-08-22
description: "重要的Openterface Mini-KVM更新：CE认证完成，生产进行中，新ETA一月中旬。硬件V1.9最终确定，包含扩展引脚、Android应用开发、改进包装和多语言手册进行中。"
keywords: "Openterface Mini-KVM, CE认证, 硬件V1.9, 生产更新, 发货时间表, Android应用开发, 扩展引脚, KVM-over-IP, 质量控制, 产品包装, 多语言手册, USB KVM, 科技制造, 开源硬件, 交付更新"
---

# 克服障碍：进度更新和新时间表

大家好，

希望大家都好。距离我们上次更新已经有一段时间了。我希望我能说Openterface一切顺利，但我们遇到了一些障碍，会延迟我们的交付时间表。虽然这不是我们预期的，但我们正在正面应对这些挑战，并取得了稳定的进展，有很多好消息要分享。这篇文章大约**7分钟阅读**，所以让我们深入了解细节，这样你们就知道事情的确切状况和接下来会发生什么。

## 法规、生产和质量

在我们开始生产之前，我们必须根据法规通过必要的质量测试，特别是CE认证。由于我们的工具包版本不仅包括Mini-KVM，还包括几个配件，每个部分都需要进行CE测试。这些测试比预期的时间更长（事实证明电缆可能相当挑剔），但好消息是**我们已经通过了Mini-KVM及其所有组件的CE认证！**下面是我们所有部件认证的概述：Mini-KVM、HDMI电缆、橙色Type-C电缆、黑色短Type-C电缆和VGA2HDMI电缆。有了认证在手，我们的生产时间表现在是确定的，我们的制造商**目前正在生产所有部件**，正如我所说。

![240823-0](https://www.crowdsupply.com/img/fcb5/db59e179-2413-4d57-8462-2285c007fcb5/openterface-240823-0_jpg_gallery-lg.jpg)
*UKCA和CE要求对我们的电子产品是相同的，CE还涵盖RoHS合规性。*

两周前，我们访问了我们的一个制造商，在他们将橙色电缆运给我们之前，培训他们的生产线经理进行质量控制。现在，所有的橙色电缆都已经生产完成，正坐在我们工作室的一个角落里。
![240823-1](https://www.crowdsupply.com/img/28dc/34844b54-0e02-414d-b58b-d40e8abe28dc/openterface-240823-1_jpg_gallery-lg.jpg)
*Kevin和Shawn正在解释测试方法，以确保橙色电缆与我们的Openterface Mini-KVM正常工作。*

我们将在本周进行同样的任务，为其他部件的生产前线培训QA。以下是额外电缆的样品。
![240823-2](https://www.crowdsupply.com/img/e703/abb8ffa5-eb85-4eb9-b5f8-d8a3d349e703/openterface-240823-2_jpg_md-xl.jpg)
*自豪地标记着我们的TechxArtisan标志，这些是HDMI电缆、短Type-C电缆和VGA-to-HDMI电缆的样品。*

我们预计其他部件和Mini-KVM很快就会从我们的制造商那里到达，届时我们将仔细检查每个组件的质量，并在发货前在我们的工作室正确包装它们。换句话说，**我们的团队将亲自确保质量**，然后它才会到达你们的手中。

## 发货、潜在延迟和新ETA

**当前的不确定性在于发货过程**。在调查了几家运输公司后，我们发现运输需要额外的时间，因为我们可能会在到达Crowd Supply的仓库之前通过仓库转移包裹。我们仍在争论是选择海运还是空运——请再给我们几天时间来安排。

清关是另一个可能造成意外延迟的潜在障碍。一旦我们的产品到达Crowd Supply在美国的仓库，它们将根据每个订单在全球范围内发货一到两周。对于美国以外的支持者，个别包裹仍需要通过全球运输和目的地国家的清关。

考虑到当前情况并增加一些缓冲时间，我仍然谨慎乐观地认为我们将在今年年底前完成交付，**新的ETA为一月中旬**。对于造成的不便，我深表歉意，并感谢你们在这次变化中的支持和耐心。

## 最终确定的硬件V1.9

正如你们可能从我们之前的[Reddit帖子](https://www.reddit.com/r/Openterface_miniKVM/comments/1e25pco/openterface_minikvm_v19_with_pins_for_more/)中了解到的，我们决定**将硬件升级到V1.9**，包括一套可破解的扩展引脚。这不是众筹活动原始计划的一部分，但我们相信它显著增强了硬件的**更广泛使用潜力**。

![240823-3](https://www.crowdsupply.com/img/77d7/09a9d0e5-3065-4f3e-8b61-bae66b5c77d7/openterface-240823-3_jpg_md-xl.jpg)
*VCC、GND、Target D+、Target D-、Host D+和Host D-引脚——其中'D'代表USB数据。*

一个关键动机是**能够在软件级别切换USB开关**。为什么这很重要？在我们的路线图上，我们**旨在支持KVM-over-IP解决方案**，如VNC，在未来。这个想法是将本地KVM控制与VNC协议匹配，允许用户通过主机计算机远程控制目标计算机。在这种远程场景中，用户切换USB端口的能力是必不可少的，特别是当主机和目标之间需要文件传输时。

**扩展引脚还为更多可能性打开了大门**，如与iPadOS集成、ATX控制、网络桥接和音频旁路。虽然我不会在这里深入所有细节，但我鼓励你们加入我们的Openterface社区，与我们进一步讨论。

这个硬件升级可能会将我们的Openterface解决方案扩展到通过IP操作，并包含更高级的功能，同时仍然保持其作为即插即用KVM-over-USB工具的核心优势——非常适合在不确定的IT环境中导航的IT专业人士，如不熟悉的数据中心。

我很高兴地报告V1.9已经通过了我们的内部基本测试，并将作为我们所有支持者的正式版本最终确定。然而，这个硬件升级需要进一步测试，基于这些扩展引脚的任何开发都将是实验性的，可能会有错误。这就是你们可以贡献的地方。我们依靠开源社区帮助我们共同改进Openterface。

## 更多软件更新

在软件方面，我们正在取得令人兴奋的进展。我们现在正在深入**Openterface Android应用**！查看这个[推文](https://x.com/TechxArtisan/status/1825460088922071398)的早期演示，显示流畅的KVM控制、鼠标移动和点击操作。更多功能即将推出，一如既往，一旦我们进一步完善代码，**这个应用也将在我们的GitHub仓库[Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android)上开源**。
![240823-4](https://www.crowdsupply.com/img/7007/b192f260-1e1f-4dab-905b-fb0a6d927007/openterface-240823-4_jpg_md-xl.jpg)
*仅用我们的指尖从Android平板电脑KVM控制Linux计算机。太好了！*

我们的QT版本刚刚得到了一个方便的更新——你现在可以[将文本从主机传输到目标](https://x.com/TechxArtisan/status/1825919721960780131)！所以现在这个功能在macOS、Windows和Linux主机应用上都受支持。

此外，我们还计划添加一个有趣的功能——[自动鼠标移动以防止你的目标计算机休眠](https://x.com/TechxArtisan/status/1825471186668847241)。我们应该选择在屏幕上弹跳的乒乓球还是经典的DVD屏幕保护程序效果？投票并评论[推文](https://x.com/TechxArtisan/status/1825470086800691459)😃

## 包装设计、标签和手册

我们一直在[尝试各种模型和包装设计](https://www.reddit.com/r/Openterface_miniKVM/comments/1elm4vq/almost_ready_to_finalize_our_package_design/)，以在几个关键因素之间找到完美平衡：

- 选择足够坚固的材料来保护产品及其部件在运输过程中，
- 创建信息丰富的标签，帮助用户一目了然地理解产品，
- 确保符合法规，
- 使包装在视觉上吸引人，
- 通过尽可能减少塑料使用来环保。

此外，我们对旧工具包包进行了几项改进，包括：

- 更大的存储空间，
- 时尚的橙色拉链，
- 升级的外部和内部材料，
- 超级有弹性的网眼口袋。

我们选择这种材料是因为它在预算友好、触感愉悦和足够耐用以保护内部物品之间达到了理想的平衡。**我们相信你们会喜欢它**。

![240823-5](https://www.crowdsupply.com/img/099a/75e16f52-bd0c-4652-af27-08caf448099a/openterface-240823-5_jpg_md-xl.jpg)

我们还在更新铝制外壳上的标签，使其尽可能信息丰富和视觉吸引人。我们希望这些增强功能将改善你们的用户体验，并使开始使用Openterface变得更容易。

![240823-6](https://www.crowdsupply.com/img/94d8/441a5757-2d6a-4c79-885b-7b5b3a7094d8/openterface-240823-6_jpg_md-xl.jpg)

我们正在最终确定Openterface手册，它将提供英语、德语、法语、日语和中文版本。如果我们错过了你们的语言，我们深表歉意——我们的盒子不是TARDIS大小的（神秘博士的警亭）！但我们会尽力在我们的网站上添加更多翻译。

![240823-7](https://www.crowdsupply.com/img/e2d9/2e5a2086-20f0-47ec-a27b-288d10d0e2d9/openterface-240823-7_jpg_md-xl.jpg)

## 社区语言审查

我一直在使用ChatGPT来协助翻译，但它有时可能会在措辞和用词上偏离目标。如果不太麻烦的话，我非常感谢你们在审查其他语言内容方面的任何帮助，特别是对于我们即将最终确定的印刷材料。我已经更新了我们在GitHub文件夹[product-printed-materials](https://github.com/TechxArtisanStudio/Openterface/tree/main/product-printed-materials)中包装的所有文本内容，你们可以在那里审查并提交任何改进。你们也可以直接私信我。谢谢！

## 最终评论和持续进展

我们再次为延迟和产品ETA的变化道歉。感谢你们的耐心和坚持与我们在一起——我们正在努力尽快将产品送到你们手中！一旦我们的发货安排好了，我会立即更新你们。更多更新即将到来，所以请加入我们的Openterface社区并保持关注！

干杯，

Billy Wang  
产品经理  
Openterface团队 | TechxArtisan
