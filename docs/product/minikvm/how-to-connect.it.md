---
title: "Come connettersi"
description: "Guida passo-passo per configurare Openterface Mini-KVM. Impara come collegare il tuo computer host e il dispositivo target con istruzioni dettagliate per le connessioni USB-C, HDMI e periferiche. Include descrizioni dell'interfaccia e suggerimenti importanti per la configurazione."
keywords: "Configurazione Mini-KVM, guida connessione KVM, configurazione KVM USB-C, connessione KVM HDMI, guida installazione KVM, configurazione periferiche computer, connessione dispositivo USB, guida interfaccia KVM, configurazione computer headless, configurazione KVM"
---

# **Come connettersi** | Guida alla configurazione | Openterface Mini-KVM

## Configurazione rapida

![to-host](https://assets.openterface.com/images/product/to-host.svg#only-light){:style="max-height:200px"} ![to-host](https://assets.openterface.com/images/product/to-host_1.svg#only-dark){:style="max-height:200px"}
![to-target](https://assets.openterface.com/images/product/to-target.svg#only-light){:style="max-height:200px"} ![to-target](https://assets.openterface.com/images/product/to-target_1.svg#only-dark){:style="max-height:200px"}

**Configurazione in 4 semplici passaggi:**

1. **Connessione Host** (lato arancione): Collegare il computer host usando cavo Type-C da 1,5m
2. **Connessione Target** (lato nero): Collegare il dispositivo target usando cavo Type-C da 0,3m
3. **Connessione Video** (lato nero): Collegare l'output video del target alla porta HDMI
4. **Dispositivo USB** (opzionale): Collegare alla porta USB-A dopo aver completato i passaggi 1-3

!!! note "Requisiti" - **Host**: Richiede l'installazione di [Openterface App](/app) - **Target**: Nessuna app necessaria - supporta Windows, macOS, Linux, Android, iOS - **Video**: Usare il cavo HDMI fornito o il convertitore VGA-to-HDMI

## Guida alle porte

![host-side](https://assets.openterface.com/images/product/host-htc.svg#only-light){:style="max-width:300px"} ![target-side](https://assets.openterface.com/images/product/target-htc.svg#only-light){:style="max-width:300px"}
![host-side](https://assets.openterface.com/images/product/host-htc_1.svg#only-dark){:style="max-width:300px"} ![target-side](https://assets.openterface.com/images/product/target-htc_1.svg#only-dark){:style="max-width:300px"}

- ① **Host USB-C**: Trasferimento dati al computer host
- ② **Target USB-C**: Output controllo tastiera/mouse
- ③ **Ingresso HDMI**: Ingresso video dal dispositivo target
- ④ **Porta USB-A**: Commutabile tra host/target

!!! warning "Note importanti" - **Alimentazione**: I dispositivi USB non dovrebbero superare 1,5W di consumo - **Blocco USB-A**: Richiede forza extra per inserire/rimuovere (evitare dispositivi piccoli) - **Hub USB**: Usare solo hub alimentati esternamente; evitare alberi USB profondi - **Commutazione**: Vedi [Guida commutazione porta USB](../usb-switch) per i dettagli

⑤ ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t.svg#only-light){:style="max-height:20px"} ![Toggle Switch](https://assets.openterface.com/images/shell-icons/toggle-h-t_1.svg#only-dark){:style="max-height:20px"} **Interruttore**: Commutare la porta USB-A tra host/target

⑥ ![Extension Pins](https://assets.openterface.com/images/shell-icons/pins.svg#only-light){:style="max-height:15px"} ![Extension Pins](https://assets.openterface.com/images/shell-icons/pins_1.svg#only-dark){:style="max-height:15px"} **Pin di estensione**: Accesso sviluppatori (vedi [Pin di estensione](../extension-pins))
