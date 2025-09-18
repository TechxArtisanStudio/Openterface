---
title: "Pini de extensie"
description: "Explorați potențialul pinilor de extensie ai Openterface Mini-KVM pentru dezvoltare hardware personalizată și proiecte open-source."
keywords: "Mini-KVM pini de extensie, dezvoltare personalizată, modificare hardware, KVM open-source"
---

# **Pini de extensie** | Mod dezvoltator | Openterface Mini-KVM

![mini-kvm-pins-port](https://assets.openterface.com/images/product/mini-kvm-pins-port.webp){:style="height:360px"}
![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="height:300px"}

Openterface Mini-KVM dispune de pini de extensie pentru dezvoltare avansată și experimente cu [Open Software](/app). Acești pini nu sunt expuși în configurația standard a carcasei.

## Cum să accesați pinilor

1. Dezasamblați dispozitivul.
2. Înlocuiți capacul original al carcasei cu un capac special Extension Pin Cap.
3. Descărcați [modelul 3D](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models) pentru Extension Pin Cap.
4. Consultați [repository-ul nostru Hardware pe GitHub](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware).

![change-cap](https://assets.openterface.com/images/product/change-cap.svg#only-light){:style="height:300px"}
![change-cap](https://assets.openterface.com/images/product/change-cap_1.svg#only-dark){:style="height:300px"}

!!! warning "Garanție anulată"
    Îndepărtarea carcasei originale poate anula garanția produsului. Orice modificare sau dezasamblare se efectuează pe propria răspundere a utilizatorului.

!!! note "Funcționalități experimentale"
    Funcționalitățile dezvoltate folosind acești pini sunt experimentale și nu au fost testate complet. Openterface nu este răspunzător pentru nicio daună, vătămare sau defecțiune rezultată din modificări, expunerea pinilor de extensie sau alte alterări ale dispozitivului.

## Configurația pinilor

![target-side](https://assets.openterface.com/images/product/extension-pins-1.svg#only-light){:style="height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2.svg#only-light){:style="height:200px"}
![target-side](https://assets.openterface.com/images/product/extension-pins-1_1.svg#only-dark){:style="height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2_1.svg#only-dark){:style="height:200px"}

Pinii de extensie oferă următoarele conexiuni:

1. Alimentare USB 5 V pentru componente externe
2. Date pozitive către hub-ul USB al host-ului
3. Date negative către hub-ul USB al host-ului
4. Date pozitive către hub-ul USB al target-ului
5. Date negative către hub-ul USB al target-ului
6. Masă (GND)

!!! danger "Conexiunile incorecte provoacă daune"
    Inversarea VCC și GND poate provoca daune grave dispozitivului și componentelor conectate. Verificați întotdeauna conexiunile pinilor înainte de a alimenta dispozitivul.

## Capac pentru pini de extensie

![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="height:360px"}

Acest capac pentru pini de extensie imprimat 3D înlocuiește capacul original al Openterface Mini-KVM, permițând utilizatorilor avansați să expună și să acceseze pinilor de extensie pentru dezvoltare personalizată. Puteți descărca fișierele modelului 3D din repository-ul nostru GitHub și să tipăriți singuri capacul.

- **Utilizare**: oferă acces la pini de extensie pentru dezvoltare hardware avansată.
- **Descărcare**: [Fișiere model 3D](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models)

## Implicați-vă în dezvoltare

Pe măsură ce continuăm să dezvoltăm și să experimentăm, vom actualiza această secțiune cu mai multe informații despre ce pot face acești pini și cum pot fi utilizați creativ. Creativitatea și expertiza dvs. pot împinge limitele a ceea ce este posibil cu Openterface Mini-KVM. Implicați-vă:

1. **Împărtășiți-vă ideile**: aveți un concept interesant pentru utilizarea acestor pini? Am vrea să-l auzim!
2. **Contribuiți cu proiecte DIY**: dacă ați creat ceva interesant, luați în considerare partajarea în comunitatea noastră [Discord Openterface](/discord).
3. **Alăturați-vă discuției**: conectați-vă cu alți dezvoltatori și pasionați pentru a face brainstorming și a colabora.

Haideți să construim și să inovăm împreună!
