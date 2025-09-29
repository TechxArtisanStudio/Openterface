---
title: "Pin di estensione"
description: "Esplora il potenziale dei pin di estensione di Openterface Mini-KVM per lo sviluppo hardware personalizzato e i progetti open source."
keywords: "Mini-KVM pin di estensione, sviluppo personalizzato, modifica hardware, KVM open source"
---

# **Pin di estensione** | Modalità sviluppatore | Openterface Mini-KVM

![mini-kvm-pins-port](https://assets.openterface.com/images/product/mini-kvm-pins-port.webp){:style="max-height:360px"}
![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="max-height:300px"}

Openterface Mini-KVM dispone di pin di estensione per lo sviluppo avanzato e la sperimentazione con [Open Software](/app). Questi pin non sono esposti nella configurazione standard del case.

## Come accedere ai pin

1. Smonta il dispositivo.
2. Sostituisci il coperchio originale del case con uno specifico «Extension Pin Cap».
3. Scarica il [modello 3D](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models) per l’Extension Pin Cap.
4. Consulta il nostro [repository GitHub hardware](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware).

![change-cap](https://assets.openterface.com/images/product/change-cap.svg#only-light){:style="max-height:300px"}
![change-cap](https://assets.openterface.com/images/product/change-cap_1.svg#only-dark){:style="max-height:300px"}

!!! warning "Garanzia nulla"
    La rimozione del case originale può invalidare la garanzia del prodotto. Qualsiasi modifica o smontaggio è a rischio e pericolo dell’utente.

!!! note "Funzionalità sperimentali"
    Le funzionalità sviluppate utilizzando questi pin sono sperimentali e non sono state completamente testate. Openterface non è responsabile per eventuali danni, lesioni o malfunzionamenti derivanti da modifiche, esposizione dei pin di estensione o altre alterazioni del dispositivo.

## Configurazione dei pin

![target-side](https://assets.openterface.com/images/product/extension-pins-1.svg#only-light){:style="max-height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2.svg#only-light){:style="max-height:200px"}
![target-side](https://assets.openterface.com/images/product/extension-pins-1_1.svg#only-dark){:style="max-height:200px"}
![host-side](https://assets.openterface.com/images/product/extension-pins-2_1.svg#only-dark){:style="max-height:200px"}

I pin di estensione forniscono le seguenti connessioni:

1. Alimentazione USB 5V per componenti esterni
2. Dato positivo verso l’hub USB dell’host
3. Dato negativo verso l’hub USB dell’host
4. Dato positivo verso l’hub USB del target
5. Dato negativo verso l’hub USB del target
6. Massa (GND)

!!! danger "Connessioni errate causano danni"
    Confondere VCC e GND può causare gravi danni al dispositivo e ai componenti collegati. Controlla sempre attentamente le connessioni dei pin prima di alimentare il dispositivo.

## Extension Pin Cap

![pin-cap](https://assets.openterface.com/images/product/part/pin-cap.webp){:style="max-height:360px"}

Questo cappuccio dei pin di estensione stampato in 3D sostituisce il cappuccio originale dell’Openterface Mini-KVM e consente agli utenti avanzati di esporre e accedere ai pin di estensione per lo sviluppo personalizzato. Puoi scaricare i file del modello 3D dal nostro repository GitHub e stampare il cappuccio autonomamente.

- **Uso**: fornisce accesso ai pin di estensione per lo sviluppo hardware avanzato.
- **Download**: [File del modello 3D](https://github.com/TechxArtisanStudio/Openterface_Mini-KVM_Hardware/tree/main/models)

## Partecipa allo sviluppo

Man mano che continuiamo a sviluppare e sperimentare, aggiorneremo questa sezione con ulteriori informazioni su cosa possono fare questi pin e su come possono essere utilizzati in modo creativo. La tua creatività e competenza possono spingere oltre i limiti di ciò che è possibile con Openterface Mini-KVM. Partecipa:

1. **Condividi le tue idee**: hai un’idea interessante per l’utilizzo di questi pin? Vogliamo sentirla!
2. **Contribuisci con progetti DIY**: se hai creato qualcosa di interessante, valuta di condividerlo con la nostra comunità [Discord Openterface](/discord).
3. **Unisciti alla discussione**: entra in contatto con altri sviluppatori ed appassionati per fare brainstorming e collaborare.

Costruiamo e innoviamo insieme!
