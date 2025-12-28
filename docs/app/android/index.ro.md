# Openterface Android

## Prezentare generală

Openterface Mini-KVM este o soluție hardware și software open-source concepută pentru a oferi funcționalitate KVM (Tastatură, Video, Mouse) de bază pentru controlul dispozitivelor printr-o interfață bazată pe Android. Acest repository conține codul sursă al aplicației Android, configurațiile de build și scripturile suport pentru configurarea și implementarea proiectului.

Ne-am angajat să dezvoltăm hardware deschis și software open-source, licențiat sub [GNU Affero General Public License v3](https://github.com/TechxArtisanStudio/Openterface_Android/blob/main/LICENSE).

## Module funcționale

### 1. Afișare video

#### Funcționalitate principală

- Transmite în timp real ieșirea video de la dispozitivul țintă conectat către ecranul Android.
- Suportă ajustări ale imaginii pentru vizualizare optimă.

![imagine](https://assets.openterface.com/images/android/videoConnect.webp)

#### Descrierea interfeței utilizator

- Ecranul principal afișează fluxul video al dispozitivului țintă, ocupând majoritatea interfeței.
- O bară de instrumente laterală oferă controale de ajustare (luminozitate, contrast, nuanță).

#### Flux de operare

1. Conectați hardware-ul Mini-KVM la dispozitivul țintă prin HDMI și USB.
2. Conectați Mini-KVM-ul la dispozitivul Android prin USB-C.
3. Lansați aplicația; fluxul video apare automat.
4. Folosiți glisoarele din bara de instrumente pentru a ajusta luminozitatea, contrastul sau nuanța după necesitate.

![imagine](https://assets.openterface.com/images/android/colorSetting.webp)

#### Caracteristici speciale

- Zoom-ul cu două degete face afișarea să arate mai bine

![imagine](https://assets.openterface.com/images/android/enlargeAndSideBar.webp)

---

### 2. Control mouse

#### Funcționalitate principală

- Oferă control absolut și relativ al mouse-ului pentru a interacționa cu interfața dispozitivului țintă.
- Suportă click stânga și dreapta.
- Selectați modul din meniul din dreapta.

#### Descrierea interfeței utilizator

- Fluxul video funcționează și ca touchpad pentru input-ul mouse-ului.
- Un buton de acțiune flotant (FAB) comută între modurile mouse și tastatură.

#### Flux de operare

1. Asigurați-vă că dispozitivul este conectat cu succes.
2. Atingeți ecranul pentru a muta cursorul mouse-ului în acea poziție (control absolut).
3. Dublu-click cu un deget pentru click stânga, click cu două degete pentru click dreapta.
4. Modul de tragere este pentru a ține apăsat butonul stâng fără a-l elibera.

#### Caracteristici speciale

- Control relativ al mouse-ului (în dezvoltare, comutabil prin setări când va fi disponibil).

![imagine](https://assets.openterface.com/images/android/mouseThouchMode.webp)

### 3. Input tastatură

#### Funcționalitate principală

- Tastați pe dispozitiv apăsând tastele tastaturii.

#### Descrierea interfeței utilizator

- Iconița tastaturii se află în colțul din dreapta jos.
- Tastatura include taste de scurtătură, taste de sistem, taste standard și taste funcționale (F1-F12).

#### Flux de operare

1. Apăsați iconița tastaturii din colțul din dreapta jos pentru a afișa tastatura.
2. Tastați text sau apăsați taste funcționale după necesitate.

#### Scurtături și caracteristici speciale

- **Taste de scurtătură**: Ctrl+C、Ctrl+V、Ctrl+Z、Ctrl+X、Ctrl+A、Ctrl+S、
    Win+Tab、Win+S、Win+E、Win+R、Win+D、Win+L、Alt+F4、Ctrl+Alt+Del、Alt+PrtScr.
- **Taste funcționale**: F1-F12、Taste simbol.
- **Taste standard**: 0-9、A-Z、Enter、Space、delete.

![imagine](https://assets.openterface.com/images/android/enlargeAndKeyBoard.webp)
![imagine](https://assets.openterface.com/images/android/keyBoardFunction.webp)
![imagine](https://assets.openterface.com/images/android/keyBoardSystem.webp)

---

Între timp, vă invităm să explorați **repository-ul nostru GitHub**: [Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android) pentru cel mai recent cod, actualizări, exemple și pentru a raporta probleme.

De asemenea, vă puteți alătura [comunității noastre Discord](/discord) pentru a vă conecta cu echipa noastră de dezvoltare și alți utilizatori minunați pentru a discuta orice subiecte legate de KVM.

Pentru suport direct, nu ezitați să ne trimiteți un email la [support@openterface.com](mailto:support@openterface.com).

---

**Aveți feedback despre această pagină?** [Spuneți-ne aici.](https://forms.gle/wmxoR2C1VdG36mT69)