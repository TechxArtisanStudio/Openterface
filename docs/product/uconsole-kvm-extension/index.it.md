# Estensione KVM Openterface per uConsole

![KVM Extension Connected to Target Device 2](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-2.webp){:style="height:300px"}

## Panoramica

Trasforma il tuo uConsole in una **console KVM (Tastiera, Video, Mouse) portatile** con questa scheda di estensione plug-and-play.

L'**Estensione KVM Openterface** sostituisce il modem 4G/LTE originale nello slot di espansione del tuo uConsole e fornisce **ingresso HDMI diretto e controllo USB HID**, permettendoti di gestire dispositivi headless in movimento—senza bisogno di monitor esterni, tastiere o configurazione di rete.

![KVM Extension Board Front Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:300px"}
![KVM Extension Board Backm Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:300px"}


## Caratteristiche

- **Fattore di Forma Perfetto**  
    Corrisponde alle dimensioni 37×77 mm del modulo 4G/LTE per un'integrazione hardware perfetta.

- **HDMI Diretto + USB HID**  
    Abilita il controllo reattivo dei dispositivi connessi utilizzando l'input e lo schermo integrati dell'uConsole.

- **Bassa Latenza**  
    Adatto per la risoluzione dei problemi a livello BIOS e l'interazione in tempo reale.

- **Veramente Portatile**  
    Rende l'uConsole uno strumento mobile per sviluppatori, ingegneri e tecnici.

- **Amichevole Open-Source**  
    Costruito sulla piattaforma [Openterface KVM](https://github.com/techxArtisanStudio/openterface_qt). Contributi della comunità benvenuti.


## Casi d'Uso

- **Amministrazione di Sistema**  
    Accedi e risolvi problemi di server o dispositivi embedded senza un interruttore KVM ingombrante.

- **Sviluppo Hardware**  
    Testa e debugga Raspberry Pi, SBC o microcontrollori direttamente.

- **Distribuzione sul Campo**  
    Esegui manutenzione o configurazione in data center o località remote.


## Installazione Hardware

Segui questi passaggi di installazione hardware per sostituire il modulo 4G/LTE nel tuo uConsole con la scheda Estensione KVM Openterface e assicurare un montaggio sicuro.

### Cosa Ti Servirà

- La tua scheda di estensione KVM Openterface
- La guarnizione fornita (spessore di plastica) 
- Un cacciavite esagonale (per le viti di montaggio della scheda)
- Precauzioni ESD (braccialetto o superficie collegata a terra) — raccomandato

### Installazione della Scheda di Estensione

1. Spegnimento e Disconnessione

    Spegni l'uConsole e disconnetti tutta l'alimentazione e i cavi.

2. Rimozione del Modulo Esistente

    Usa un cacciavite esagonale per rimuovere le due viti che tengono il modulo 4G/LTE o la scheda di estensione esistente.

    Solleva attentamente la scheda dritto verso l'alto per evitare di piegare i contattori a molla.

3. Installazione della Scheda di Estensione KVM

    - La scheda di Estensione KVM Openterface è spessa 1.0 mm (più sottile dell'originale 4G/LTE 1.2 mm). Per questo motivo, raccomandiamo di posizionare la guarnizione fornita sui perni delle viti (tra il PCB e i distanziatori di montaggio) in modo che la guarnizione si sieda sotto i perni delle viti prima di posizionare la scheda. Questo compensa il PCB più sottile e aiuta a garantire la pressione adeguata del contattore a molla.
    - Se preferisci controllare prima, posiziona la scheda senza la guarnizione e verifica il contatto uniforme della molla; se il contatto è irregolare o la scheda si siede allentata, aggiungi la guarnizione e riposiziona la scheda.

<div style="display:flex;gap:1rem;align-items:flex-start;flex-wrap:wrap">
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-gasket-1.webp" alt="Installing KVM Extension gasket" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp" alt="Installing KVM Extension into uConsole" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
</div>

4. Reinserimento delle Viti

    Reinserisci le due viti e stringi con il cacciavite esagonale. Snug è sufficiente — non stringere troppo.

5. Verifica del Montaggio

    La scheda dovrebbe sedersi piatta senza movimento notevole. Verifica che i contattori a molla stiano facendo contatto uniforme attraverso i pad.

6. Test dell'Hardware

    Riconnetti l'alimentazione, avvia il sistema e testa dispositivi HDMI, audio e USB HID per confermare il funzionamento corretto.

## Guida alla Configurazione del Software

Per usare l'Estensione KVM, installa l'**App Openterface** sul tuo uConsole.

Opzione 1 - Usa la versione Flatpak di Openterface
- 📖 Segui la nostra [Guida all'Installazione Flatpak](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) per passaggi di configurazione dettagliati.

![KVM Extension Connected to Target Device](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1c.webp){:style="height:300px"}

Opzione 2 - Installa la versione comunitaria da Rex

Se vuoi la build comunitaria mantenuta da Rex, aggiungi il suo repository e installa il pacchetto con i comandi qui sotto.

1. Aggiungi la chiave GPG del repository e il repository

```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. Aggiorna e installa

```bash
sudo apt update
sudo apt install openterfaceqt
```

Note: questi comandi richiedono sudo. Il repository punta a pacchetti arm64 Bookworm; verifica la compatibilità con il tuo dispositivo prima di installare.

## Stato Pre-Lancio

- 📦 Primo lotto attualmente in preparazione  
- ⏳ Spedizione stimata inizia **all'inizio di agosto 2024**  
- 🛒 Quantità limitata – [Pre-ordina ora](https://shop.techxartisan.com/products/openterface-kvm-ext-for-uconsole) per riservare la tua unità

> **Avviso Pre-Ordine**  
> Questo articolo è attualmente in pre-ordine con un tempo di consegna stimato di **circa 2 mesi**.  
> Se hai bisogno di altri articoli più presto, per favore fai un **ordine separato**. Gli ordini combinati verranno spediti quando questo prodotto sarà pronto.

## Comunità e Supporto

- 🗨️ Unisciti alla discussione: [Server Discord](https://discord.gg/ruAD9kcYbq)  
- 📧 Supporto email: [info@openterface.com](mailto:info@openterface.com)


## FAQ

**D: Come funziona la Scheda di Estensione KVM?**  
Cattura l'output HDMI da un dispositivo target e lo visualizza sull'uConsole. Allo stesso tempo, la tastiera e il trackball dell'uConsole vengono utilizzati per controllare il dispositivo target tramite emulazione USB HID.

**D: Posso usare questo con il modulo 4G/LTE installato?**  
No. Questa scheda occupa lo stesso slot di espansione. Dovrai scegliere tra connettività cellulare o funzionalità KVM.

**D: Il software è open source?**  
Sì! Le nostre App **Openterface Connect** sono completamente open source e disponibili nel nostro [repository GitHub](https://github.com/TechxArtisanStudio/Openterface_QT).
