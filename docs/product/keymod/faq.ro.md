---
title: Întrebări frecvente despre Openterface KeyMod Series
description: Întrebări frecvente despre KeyMod Series: funcționalități, compatibilitate, platforme și informații despre pre-lansare.
keywords: KeyMod, Openterface, emulator HID, tastatură Bluetooth, tastatură telefon, open source, pre-lansare, Android, iPadOS
---

# Întrebări frecvente despre Openterface KeyMod

Bine ați venit la întrebările frecvente despre **Openterface KeyMod**.  
Dacă nu găsiți ce aveți nevoie, **trimiteți-ne un e-mail la [info@openterface.com](mailto:info@openterface.com)** sau **alăturați-vă comunității noastre** pe [Discord](/discord) sau [Reddit](/reddit).

⚠️ **Notă**: KeyMod este în prezent în dezvoltare pre-lansare. Funcționalitățile, specificațiile și designul pot fi modificate pe măsură ce finalizăm produsul.

---

## :material-clipboard-list: Navigare rapidă

- [Întrebări frecvente despre Openterface KeyMod](#întrebări-frecvente-despre-openterface-keymod)
  - [:material-clipboard-list: Navigare rapidă](#material-clipboard-list-navigare-rapidă)
  - [General](#general)
  - [Conectivitate](#conectivitate)
  - [Funcționalități](#funcționalități)
  - [Pre-lansare](#pre-lansare)

---

## General

**:material-chat-question:{ .faq } Ce este KeyMod?**

KeyMod este un emulator HID (tastatură și mouse) compact USB + Bluetooth care transformă telefonul într-o tastatură și trackpad portabile. Folosiți-l pentru a controla dispozitive care necesită intrare tastatură/mouse—kioscuri, smart TV-uri, set-top box-uri, afișaje exterioare—fără a transporta o tastatură completă.

**:material-chat-question:{ .faq } Ce platforme suportă aplicația KeyMod?**

Aplicația controler KeyMod se concentrează pe **Android** și **iPadOS**. Extindem și controlul desktop cu software **Windows și macOS** în ecosistemul nostru Openterface mai larg.

**:material-chat-question:{ .faq } Dispozitivul țintă are nevoie de software?**

Nu. KeyMod emulează o tastatură și mouse USB standard. Dispozitivul țintă îl recunoaște ca hardware HID plug-and-play—fără drivere sau instalare software necesară.

**:material-chat-question:{ .faq } KeyMod este open source?**

Da. KeyMod este hardware și software deschise. Vom publica scheme, fișiere PCB, firmware, software și BOM pe măsură ce proiectul evoluează.

---

## Conectivitate

**:material-chat-question:{ .faq } USB sau Bluetooth—ce ar trebui să folosesc?**

- **USB**: Mai fiabil, latență mai mică. Folosiți când doriți cea mai stabilă conexiune.
- **Bluetooth**: Fără cablu. Folosiți când doriți o configurare mai ușoară și scenariul permite wireless.

**:material-chat-question:{ .faq } Ce variante hardware sunt planificate?**

1. **Conector 2-în-1** — Conector USB A + USB C combinat pentru compatibilitate largă
2. **Versiune USB C** — Conector USB C dedicat pentru dispozitive moderne

---

## Funcționalități

**:material-chat-question:{ .faq } Ce layout-uri de gamepad sunt suportate?**

KeyMod poate acționa ca un controler de joc virtual cu **layout Xbox**, **layout PlayStation** și **layout NES**.

**:material-chat-question:{ .faq } Pot crea profile și macro-uri personalizate?**

Da. Aplicația mobilă open source suportă profile de intrare personalizate, macro-uri, taste rapide și shortcut-uri pentru fluxul de lucru. Puteți folosi și moduri tastatură numerică și gamepad.

**:material-chat-question:{ .faq } Ce sunt butoanele hardware programabile?**

KeyMod include butoane hardware programabile pentru acțiuni pe dispozitiv precum declanșatoare rapide și fluxuri de lucru simple în stil macro. Această capacitate este încă experimentală și va fi rafinată prin feedback-ul comunității.

---

## Pre-lansare

**:material-chat-question:{ .faq } Când va fi lansat KeyMod?**

KeyMod este în dezvoltare pre-lansare. Abonați-vă la [pagina produsului](/product/keymod/) pentru notificări de lansare și actualizări.

**:material-chat-question:{ .faq } Cum se raportează KeyMod la Mini-KVM și KVM-Go?**

KeyMod folosește nucleul HID dovedit al Openterface Mini-KVM. Partajează aceeași abordare de emulare tastatură și mouse bazată pe hardware, dar este proiectat pentru un caz de utilizare diferit: transformarea telefonului într-o tastatură/trackpad portabilă pentru controlul local al dispozitivelor, în loc de captură video KVM-over-USB.
