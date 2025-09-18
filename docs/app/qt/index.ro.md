# Openterface QT pentru Windows și Linux

Acest document oferă o prezentare generală a unui software KVM (Tastatură, Video, Mouse) multi-platformă dezvoltat folosind Qt, compatibil atât cu sistemele de operare Linux cât și Windows. Software-ul facilitează controlul asupra unui dispozitiv țintă de pe un sistem gazdă, oferind o varietate de funcții accesibile prin bara de meniu și funcționalități suplimentare.

## Funcțiile barei principale de meniu

### Preferințe

Meniul Preferințe permite utilizatorilor să personalizeze setările printr-un dialog cu patru pagini:<br>
![Preferințe Generale](https://assets.openterface.com/images/qt/preferenceGernal.webp)

-   **General** Această pagină configurează filtrul jurnalelor de depanare și inhibarea protectorului de ecran când aplicația rulează. Categoriile de jurnale includ:

    -   Core
    -   Serial
    -   InterfațăUtilizator
    -   gazdă

    Utilizatorii pot alege să salveze jurnalele într-un fișier .txt și să activeze sau nu inhibarea protectorului de ecran.<br>

![Preferințe Video](https://assets.openterface.com/images/qt/preferenceVideo.webp)

-   **Video** Această pagină permite utilizatorilor să:

    -   Selecteze datele cărei camere să fie capturate.
    -   Seteze rezoluția.
    -   Aleagă formatul fluxului video.

-   **Audio** Această pagină este în prezent în dezvoltare.<br>

![Preferințe Control Țintă](https://assets.openterface.com/images/qt/preferenceTargetControl.webp)

-   **Control Țintă** Această pagină oferă opțiuni pentru configurarea modurilor de control pentru dispozitivul țintă:

    -   **Moduri de control:**

        -   **Tastatură + Mouse + dispozitiv USB HID**
        -   **Tastatură USB**
        -   **Tastatură + Mouse**
        -   **Dispozitiv USB HID**

    -   **Setarea ID-ului Vânzător (VID) și ID-ului Produs (PID) citite de la țintă.**
    -   **Definirea descriptorului USB pentru țintă.**

### Editare

-   **Lipire:** Atât opțiunea Lipire din meniul Editare cât și butonul de lipire din colțul stânga-sus permit utilizatorilor să lipească text din clipboard-ul gazdă pe dispozitivul țintă.

### Control

Acest meniu oferă opțiuni pentru:<br>

-   Setarea modurilor de mișcare a mouse-ului: Absolut sau Relativ. **Control >> Mod Mouse >> Absolut sau Relativ.**
-   Comutarea vizibilității cursorului mouse-ului gazdă. **Control >> Vizibilitate Mouse >> Ascundere Automată sau Afișare Permanentă.**
-   Comutarea unui port USB de pe hardware între utilizarea țintă și gazdă. **Control >> USB Comutabil >> La Țintă sau La Gazdă.**
-   Ajustarea ratei baud pentru transmisia chip-ului. **Control >> Rată Baud >> 9600, 115200.**

### Avansat

Meniul Avansat include următoarele opțiuni:<br>
![Meniu Avansat](https://assets.openterface.com/images/qt/menuAdvance.webp)

-   **Verificare Mediu:** Verifică dacă driverele necesare pentru software sunt instalate.
-   **Resetare Port Serial:** Repornește portul serial.
-   **Resetare Tastatură și Mouse:** Resetează setările tastaturii și mouse-ului.
-   **Resetare la Fabrică Chip HID:** Restaurează chip-ul HID la setările din fabrică.<br>
    ![Avansat Consolă Serială](https://assets.openterface.com/images/qt/advanceSerialConsole.webp)
-   **Consolă Serială:** Deschide o nouă fereastră pentru monitorizarea tuturor mesajelor trimise la portul serial, cu filtre pentru mesajele trimise/primite.<br>
    ![Avansat Instrument Script](https://assets.openterface.com/images/qt/advanceScriptTool.webp)
-   **Instrument Script:** Rulează scripturi AutoHotkey (AHK). Această funcție imită AutoHotkey dar suportă doar un subset de funcții mouse/tastatură și capabilități de captură de ecran. Scripturile afectează dispozitivul țintă.
-   **Server TCP:** Primește comenzi AutoHotkey prin TCP pentru a le executa pe dispozitivul țintă.
-   **Actualizare Firmware:** Preia cel mai recent firmware de pe un server la distanță, permițând utilizatorilor să aleagă dacă să îl instaleze pe dispozitiv.

### Limbi

Limba interfeței poate fi setată la:

-   Daneză
-   Engleză
-   Germană
-   Franceză
-   Japoneză
-   Suedeză

### Ajutor

Meniul Ajutor oferă: <br>
![Meniu Ajutor](https://assets.openterface.com/images/qt/menuHelp.webp)

-   Link-uri către site-ul oficial și formulare de feedback pentru probleme software/hardware.
-   Informații despre achiziționarea hardware-ului.
-   O descriere a mediului software-ului.
-   Despre: Detalii despre organizație.
-   Actualizare: Verifică actualizările software.

## Funcțiile barei de meniu (de la stânga la dreapta)

Bara de meniu, de la stânga la dreapta, include următoarele funcționalități:<br>

![Bară Meniu](https://assets.openterface.com/images/qt/menubar.webp)

-   Selectare Layout Tastatură: Alegeți layout-ul tastaturii.
-   Controale Zoom: Mărire, micșorare sau resetare a afișării fluxului video captat.
-   Tastatură Virtuală: Include taste funcționale și combinații de scurtături presetate.
-   Captură Ecran: Capturează întregul ecran țintă și îl salvează într-un folder implicit.
-   Mod Ecran Complet: Comută afișarea pe ecran complet.
-   Lipire: Lipește text din clipboard-ul gazdă pe țintă.
-   Dans Mouse: Declanșează mouse-ul să efectueze mișcări presetate.
-   Indicator Dispozitiv USB: Afișează dacă un dispozitiv USB este alocat țintei sau gazdei.

Între timp, vă invităm să explorați **repository-ul nostru GitHub**: [Openterface_QT](https://github.com/TechxArtisanStudio/Openterface_QT) pentru cel mai recent cod, actualizări, exemple și pentru a raporta probleme.

De asemenea, puteți să vă alăturați [comunității noastre Discord](/discord) pentru a vă conecta cu echipa noastră de dezvoltatori și alți utilizatori minunați pentru a discuta orice subiecte legate de KVM.

Pentru suport direct, nu ezitați să ne trimiteți un email la [support@openterface.com](mailto:support@openterface.com).

---

**Aveți feedback despre această pagină?** [Spuneți-ne aici.](https://forms.gle/wmxoR2C1VdG36mT69)
