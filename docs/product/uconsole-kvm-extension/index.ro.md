# Extensie KVM Openterface pentru uConsole

![KVM Extension Connected to Target Device 2](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-2.webp){:style="height:300px"}

## Prezentare Generală

Transformați uConsole-ul în **consolă KVM (Tastatură, Video, Mouse) portabilă** cu această placă de extensie plug-and-play.

**Extensia KVM Openterface** înlocuiește modemul 4G/LTE original în slotul de expansiune al uConsole-ului și oferă **intrare HDMI directă și control USB HID**, permițându-vă să gestionați dispozitive headless în mișcare—fără nevoia de monitoare externe, tastaturi sau configurare de rețea.

![KVM Extension Board Front Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension.webp){:style="height:300px"}
![KVM Extension Board Backm Side](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-back.webp){:style="height:300px"}


## Caracteristici

- **Factor de Formă Perfect**  
    Se potrivește cu dimensiunea 37×77 mm a modulului 4G/LTE pentru integrare hardware perfectă.

- **HDMI Direct + USB HID**  
    Permite control reactiv al dispozitivelor conectate folosind intrarea și ecranul integrat ale uConsole-ului.

- **Latență Mică**  
    Potrivit pentru depanarea la nivel BIOS și interacțiunea în timp real.

- **Cu Adevărat Portabil**  
    Face din uConsole un instrument mobil pentru dezvoltatori, ingineri și tehnicieni.

- **Prietenos cu Open Source**  
    Construit pe platforma [Openterface KVM](https://github.com/techxArtisanStudio/openterface_qt). Contribuțiile comunității sunt binevenite.


## Cazuri de Utilizare

- **Administrare Sistem**  
    Accesați și depanați servere sau dispozitive embedded fără un switch KVM voluminos.

- **Dezvoltare Hardware**  
    Testați și depanați Raspberry Pi, SBC-uri sau microcontrolere direct.

- **Implementare Teren**  
    Efectuați întreținere sau configurare în centre de date sau locații remote.


## Instalare Hardware

Urmăriți acești pași de instalare hardware pentru a înlocui modulul 4G/LTE din uConsole cu placa Extensie KVM Openterface și pentru a asigura o montare sigură.

### Ce Veți Avea Nevoie

- Placa dvs. de extensie KVM Openterface
- Garnitura furnizată (șpărtură din plastic) 
- O cheie hexagonală (pentru șuruburile de montare ale plăcii)
- Precații ESD (curea de încheietură sau suprafață împământată) — recomandat

### Instalarea Plăcii de Extensie

1. Oprire și Deconectare

    Opriți uConsole-ul și deconectați toată alimentarea și cablurile.

2. Eliminarea Modulului Existent

    Folosiți o cheie hexagonală pentru a elimina cele două șuruburi care țin modulul 4G/LTE sau placa de extensie existentă.

    Ridicați cu atenție placa drept în sus pentru a evita îndoirea contactorilor cu arc.

3. Instalarea Plăcii de Extensie KVM

    - Placa de Extensie KVM Openterface are grosimea de 1.0 mm (mai subțire decât 4G/LTE original de 1.2 mm). Din această cauză, recomandăm plasarea garniturii furnizate pe posturile de șuruburi (între PCB și distanțierii de montare) astfel încât garnitura să se așeze sub posturile de șuruburi înainte de așezarea plăcii. Aceasta compensează PCB-ul mai subțire și ajută la asigurarea presiunii adecvate a contactorului cu arc.
    - Dacă preferați să verificați mai întâi, așezați placa fără garnitură și verificați contactul uniform cu arcul; dacă contactul este neuniform sau placa se așează lăsăcios, adăugați garnitura și repoziționați placa.

<div style="display:flex;gap:1rem;align-items:flex-start;flex-wrap:wrap">
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-gasket-1.webp" alt="Installing KVM Extension gasket" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
    <div style="flex:1;min-width:200px">
        <img src="https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-install-1.webp" alt="Installing KVM Extension into uConsole" style="max-height:300px;width:100%;height:auto;object-fit:contain" />
    </div>
</div>

4. Reinserarea Șuruburilor

    Reinserați cele două șuruburi și strângeți cu cheia hexagonală. Strâns este suficient — nu strângeți prea mult.

5. Verificarea Montajului

    Placa ar trebui să se așeze plat fără mișcare notabilă. Verificați că contactorii cu arc fac contact uniform prin pad-uri.

6. Testarea Hardware-ului

    Reconectați alimentarea, porniți sistemul și testați dispozitive HDMI, audio și USB HID pentru a confirma funcționarea corectă.

## Ghid de Configurare Software

Pentru a folosi Extensia KVM, instalați **App Openterface** pe uConsole-ul dvs.

Opțiunea 1 - Folosiți versiunea Flatpak Openterface
- 📖 Urmăriți [Ghidul nostru de Instalare Flatpak](https://github.com/TechxArtisanStudio/Openterface_QT/blob/main/doc/flatpak_installation.md) pentru pași de configurare detaliați.

![KVM Extension Connected to Target Device](https://assets.openterface.com/images/product/openterface-kvm-uconsole-extension-use-case-1c.webp){:style="height:300px"}

Opțiunea 2 - Instalați versiunea comunității de la Rex

Dacă vreți build-ul comunității menținut de Rex, adăugați repository-ul său și instalați pachetul cu comenzile de mai jos.

1. Adăugați cheia GPG a repository-ului și repository-ul

```bash
wget -q -O- https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm/KEY.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/ak-rex.gpg
sudo add-apt-repository -y "deb [arch=arm64] https://raw.githubusercontent.com/ak-rex/ClockworkPi-apt/main/bookworm stable main"
```

2. Actualizați și instalați

```bash
sudo apt update
sudo apt install openterfaceqt
```

Note: aceste comenzi necesită sudo. Repository-ul vizează pachete arm64 Bookworm; verificați compatibilitatea cu dispozitivul dvs. înainte de instalare.

## Status Pre-Lansare

- 📦 Primul lot în pregătire în prezent  
- ⏳ Expedierea estimată începe **la începutul lunii august 2024**  
- 🛒 Cantitate limitată – [Pre-comandați acum](https://shop.techxartisan.com/products/openterface-kvm-ext-for-uconsole) pentru a vă rezerva unitatea

> **Notificare Pre-comandă**  
> Acest articol este în prezent în pre-comandă cu un timp de livrare estimat de **aproximativ 2 luni**.  
> Dacă aveți nevoie de alte articole mai devreme, vă rugăm să faceți o **comandă separată**. Comenzile combinate vor fi expediate când acest produs este gata.

## Comunitate și Suport

- 🗨️ Alăturați-vă discuției: [Server Discord](https://discord.gg/ruAD9kcYbq)  
- 📧 Suport email: [info@openterface.com](mailto:info@openterface.com)


## Întrebări Frecvente

**Î: Cum funcționează Placa de Extensie KVM?**  
Ea capturează ieșirea HDMI de la un dispozitiv țintă și o afișează pe uConsole. În același timp, tastatura și trackball-ul uConsole-ului sunt folosite pentru a controla dispozitivul țintă prin emulare USB HID.

**Î: Pot folosi acest lucru cu modulul 4G/LTE instalat?**  
Nu. Această placă ocupă același slot de expansiune. Va trebui să alegeți între conectivitatea celulară sau funcționalitatea KVM.

**Î: Software-ul este open source?**  
Da! App-urile noastre **Openterface Connect** sunt complet open source și disponibile în [repository-ul nostru GitHub](https://github.com/TechxArtisanStudio/Openterface_QT).
