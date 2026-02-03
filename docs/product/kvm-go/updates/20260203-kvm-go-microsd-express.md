---
draft: false
date: 2026-02-03
title: "microSD EXPRESS on KVM-GO: Compatibility Test and Real Transfer Speeds"
description: "KVM-GO microSD EXPRESS compatibility test with SanDisk 128GB card. Confirmed: detection and read/write work. Real-world speeds ~30 MB/s write, ~20 MB/s read due to USB 2.0 bridge. UHS-I cards are sufficient for KVM-GO's microSD path."
keywords: "KVM-GO microSD, microSD EXPRESS KVM-GO, KVM-GO storage, SanDisk microSD EXPRESS, KVM-GO compatibility, USB 2.0 microSD, KVM-GO transfer speed, microSD card KVM-GO, Openterface KVM-GO"
author: "Openterface Team | TechxArtisan"
category: "Product Updates"
tags: ["KVM-GO", "Product Updates", "microSD", "Storage", "Compatibility", "Performance"]
featured: false
social:
  image: "https://assets2.openterface.com/images/blog/SD-card.webp"
  title: "microSD EXPRESS on KVM-GO: Compatibility & Speed Test"
  description: "We tested a SanDisk microSD EXPRESS card on KVM-GO. It works, but speeds are limited by the USB 2.0 bridge—UHS-I is enough for this use case."
---

# microSD EXPRESS on KVM-GO: Compatibility Test and Real Transfer Speeds

A community member asked whether KVM-GO supports microSD EXPRESS cards. Instead of guessing, we picked up a real microSD EXPRESS card and ran a simple compatibility + speed check.

---

## What we tested

- **Card:** SanDisk microSD EXPRESS 128GB  

![Test card used: SanDisk microSD EXPRESS 128GB.](https://assets2.openterface.com/images/blog/SD-card.webp)  
*Test card used: SanDisk microSD EXPRESS 128GB.*

- **Goal:** Confirm basic compatibility (detection + read/write) and measure real transfer speeds through KVM-GO's microSD path.

---

## Test setup

This was a straightforward "real usage" style transfer test:

1. Insert the microSD EXPRESS card into KVM-GO's microSD slot.  
2. On a Windows PC, copy a large folder/file set to the microSD card to observe sustained write speed.  
3. Copy data from the microSD card back to the PC to observe sustained read speed.  
4. We used normal OS file copy, and recorded the speed shown in the Windows transfer dialog.

![Test setup: inserting microSD EXPRESS into KVM-GO for read/write checks.](https://assets2.openterface.com/images/blog/plug.webp)  
*Test setup: inserting microSD EXPRESS into KVM-GO for read/write checks.*

---

## Compatibility result

KVM-GO can recognize the SanDisk microSD EXPRESS card normally.  
Read and write both work without issues.

So if your question is simply "Does it work?" the answer is **yes**.

---

## Transfer speed result

Even though the card is microSD EXPRESS, the transfer speed you get here depends on the internal storage path inside KVM-GO.

In our test, we observed approximately:

- **Write speed:** around **30 MB/s** 

![Write test (PC → microSD): ~28 MB/s observed during file copy.](https://assets2.openterface.com/images/blog/Performance.webp) 

*Write test (PC → microSD): ~28 MB/s observed during file copy.*

- **Read speed:** around **20 MB/s**

![Read test (microSD → PC): ~22 MB/s observed during file copy.](https://assets2.openterface.com/images/blog/Performance2.webp)  

*Read test (microSD → PC): ~22 MB/s observed during file copy.*

These numbers can vary depending on file sizes, the mix of small vs large files, OS caching behavior, and overall workload, but this is the range we consistently saw.

---

## Why it does not run at Express speeds

microSD EXPRESS cards are capable of much higher performance in the right setup, but KVM-GO's microSD storage path is limited by the internal bridge/controller used for microSD-to-USB storage.

In KVM-GO, that bridge operates at USB 2.0. USB 2.0 is often described as 480 Mbps (theoretical), but in real-world file transfers the sustained throughput is typically much lower due to protocol overhead and implementation details.

![USB 2.0 storage path reference.](https://assets2.openterface.com/images/blog/USB.webp)
*The microSD storage bridge is USB 2.0 (480 Mbps theoretical). Real-world file transfer throughput is lower.*

This is why microSD EXPRESS works fine on KVM-GO, but you should not expect Express-level speeds through this specific microSD path.

---

## Practical takeaway

1. **microSD EXPRESS is compatible with KVM-GO**  
   It is detected normally and read/write works.

2. **Express-level speed will not show up through KVM-GO's microSD path**  
   The bottleneck is the internal USB 2.0 storage bridge, not the card itself.

3. **What card makes sense to buy**  
   If you are buying a card mainly for use with KVM-GO's microSD feature, a good UHS-I microSD card is usually enough, since the interface is the limiting factor in this scenario.

4. **If you need Express speeds**  
   Use a dedicated microSD EXPRESS reader on a faster USB interface (separate from KVM-GO).

---

## If you want us to test another card

If you have a specific microSD EXPRESS model you care about (brand + capacity + model number), share it and we can run the same check and add the results.
