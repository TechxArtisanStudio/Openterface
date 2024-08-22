---
date: 2024-08-22
authors:
  - Openterface
categories:
  - Updates
---

# Overcoming Hurdles: Progress Update & New Timeline

Hey everyone,

I hope you’re all doing well. It’s been a while since our last update. I wish I could say everything’s been smooth sailing for Openterface, but we’ve hit a couple of speed bumps that will delay our delivery timeline. While this wasn’t what we expected, we’re tackling these challenges head-on and making steady progress with plenty of good news to share. Let’s dive into the details so you know exactly where things stand and what’s coming next.

## Regulation, Production, and Quality

Before we could kick off production, we had to pass necessary quality tests according to regulations, particularly CE certification. Since our toolkit version includes not just the Mini-KVM but also several accessories, each part needed to undergo CE testing. These tests took longer than expected (turns out cables can be quite picky), but the great news is that **we’ve passed CE for our Mini-KVM and all its components!** Below is an overview of the certifications for all our parts: Mini-KVM, HDMI cable, orange Type-C cable, black short Type-C cable, and VGA2HDMI cable. With certification in hand, our production timeline is now certain, and our manufacturers are **currently producing all parts** as I speak.

Two weeks ago, we visited one of our manufacturers to train their line managers on quality control for the orange cable. All the orange cables have since been produced and are now sitting in a corner of our studio.
![240823-1](pic/240823-1.jpg)
*Kevin and Shawn were explaining how to test if the orange cable works with the Openterface Mini-KVM.*

We're doing the same task to train QA at the production frontline for other parts as well. Here are samples of additional cables.
![240823-2](pic/240823-2.jpg)
*Samples of the HDMI cable, the short Type-C cable, and the VGA-to-HDMI cable, with TechxArtisan trademark*

We’re expecting the other parts and Mini-KVMs to arrive soon, at which point we’ll double-check the quality of every component and pack them properly at our studio before shipment. In other words, **we’ll personally ensure the quality** before it reaches your hands.

## Shipment, Potential Delays, and New ETA

**The current uncertainty lies in the shipment process**. After investigating several shipping companies, we found that shipping will take extra time as we will likely transfer parcels through a warehouse before reaching Crowd Supply’s warehouse. We’re still debating whether to choose sea or air freight—please bear with us for a few more days while we sort out the arrangements.

Customs clearance is another potential hurdle that might cause unexpected delays. Once our products arrive at Crowd Supply's warehouse in the US, they’ll take one to two weeks to ship out globally based on each order. For backers outside the US, individual parcels will still need to go through global shipping and customs clearance in the destination country.

Accounting for the current situation and adding some buffer time, I remain cautiously optimistic that we’ll complete delivery before the end of this year, with **a new ETA of mid-December**. I’m truly sorry for the inconvenience and appreciate your support and patience during this change.

## Finalised Hardware V1.9

As you may know from our previous [Reddit post](https://www.reddit.com/r/Openterface_miniKVM/comments/1e25pco/openterface_minikvm_v19_with_pins_for_more/), we decided to **upgrade our hardware to V1.9**, including a set of hackable expansion pins. This wasn’t part of the original plan for the crowdfunding campaign, but we believe it significantly enhances the hardware’s potential for broader use.

![240823-3](pic/240823-3.jpg)
*The VCC, GND, Target D+, Target D-, Host D+, and Host D- pins—where ‘D’ stands for USB data.*


One key motivation was to enable the USB switch to be toggled at the software level. Why is this important? In our roadmap, we also **aim to support KVM-over-IP solution**, such as VNC in the future. The idea is to match local KVM control to the VNC protocol, allowing users to remotely control the target computer via the host computer. This could potentially extend our Openterface solution to be over IP while maintaining its core strength as a plug-and-play KVM-over-USB tool — perfect for IT pros braving uncertain IT dungeons, like unfamiliar data centres.

**The expansion pins also open up possibilities for more**, like teaming up with iPadOS, ATX control, network bridging, and audio bypass. While I won’t dive into all the details here, I encourage you to join our Openterface community to discuss further.

This hardware upgrade required additional testing, but I’m happy to report that V1.9 has passed our internal basic tests and will be finalised as the official version for all our backers. Please note that any development based on these expansion pins will be experimental and may still have bugs. We’re counting on the open-source community to help us improve Openterface together.

## Software Updates

On the software front, we’re making exciting strides. We’re **developing an Android version** of our Openterface Mini-KVM app, and this [tweet](https://x.com/TechxArtisan/status/1825460088922071398) is an early demo showing smooth KVM control, mouse movement, and clicks in action! More features are on the way, and as always, **the Android app will be open-sourced** once we’ve polished the code a bit more.
![240823-4](pic/240823-4.jpg)

Our QT version just got a handy update—you can now [transfer text from the host to the target](https://x.com/TechxArtisan/status/1825919721960780131)! So now this feature is supported on macOS, Windows, and Linux host apps.

Moreover, We’re also planning to add a fun feature — [an auto mouse movement to prevent your target computer from sleeping](https://x.com/TechxArtisan/status/1825470086800691459). Should we go with the ping-pong ball bouncing around the screen or the classic DVD screensaver effect? Vote and comment the tweet 😃

## Design and Packaging

We’ve been working on some mock-up and experimental packages for the toolkit version, and we recently sent out beta kits to our Japanese friends to test the packaging. Unfortunately, it didn’t go well—one of the packages got a bit smashed during shipment. As you can see from the image below [image], we’ll need to roll back our design and opt for something similar to our previous design [image] using cardboard paper.

I know some people might not care much about how the package looks, but for us, as a producer, it’s crucial to balance several factors in packaging design: using materials sturdy enough to protect the product and parts during shipment, ensuring informative labelling that helps users understand the product from the outside, and complying with regulations. We also want the packaging to look good and be eco-friendly by avoiding plastic as much as possible.

We’re also finalising the manual for Openterface, which will be available in English, German, French, Japanese, and Chinese. Sorry if we missed your language—our box isn’t TARDIS-sized (Doctor Who’s police box)! But we’ll do our best to add more on our website.

Speaking of printed materials, our website supports several languages, but as English is our primary language, there may be some delays in updating content in other languages. Additionally, I’ve been using ChatGPT to help with translations, but it can sometimes mess up the phrasing and wording. If it’s not too much trouble, I’d appreciate it if anyone could help review the content in other languages, especially for the printed materials we’re about to finalise. I’ve updated all text content for the package on this GitHub repo [link], where you can review it and submit any improvements. You can also DM me. Thanks!

We’re also updating the labels on the aluminium casing, keeping them as informative and visually appealing as possible. I hope this labelling will enhance the user experience and make it easier to start using Openterface.

Finally, we’ve made several improvements over the old bag design, including a stylish orange zipper, better outside and inside materials, and a super stretchy mesh pocket. [images] We chose this material because it offers a good balance of being budget-friendly, having a nice touch, and being sturdy enough to protect the items inside. We’re confident you’ll all like it.

Thanks for your patience and for sticking with us—we’re working hard to get this out to you as soon as possible! More updates are on the way, so please join our Openterface community and stay tuned.

Cheers,  
Billy Wang
Product Manager
Openterface Team