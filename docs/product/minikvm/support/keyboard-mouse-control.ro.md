# **Rezolvarea problemelor cu tastatura și mouse-ul care nu pot controla computerul țintă**

Ocazional, utilizatorii pot întâmpina situații în care funcțiile de tastatură și mouse ale dispozitivului Openterface nu funcționează conform așteptărilor. Acest document descrie cele mai frecvente cauze și cum le puteți rezolva sau preveni.

**Feedback software:** Atunci când Openterface nu poate stabili comunicația HID din cauza unei conexiuni țintă lipsă sau incorecte, interfața utilizatorului evidențiază starea pentru ca să puteți acționa rapid.

- Pe **macOS**, pictograma de tastatură și mouse din colțul din dreapta sus al utilitarului Openterface devine **portocalie**.  

    <img src="https://assets.openterface.com/images/software/inactive_keyboardmoue_macos.webp" alt="Inactive keyboard and mouse (macOS)" width="200" />

- Pe **Windows/Linux**, pictograma corespunzătoare din partea de jos a ferestrei devine **roșie**.  

    <img src="https://assets.openterface.com/images/software/inactive_keyboardmoue_windows.webp" alt="Inactive keyboard and mouse (Windows)" width="200" />

Videoclipul continuă să apară în Openterface, dar tastatura și mouse-ul nu răspund — puteți vedea desktopul țintă, dar nu îl puteți controla. Aceasta înseamnă de obicei că comunicația HID nu a fost stabilită (de exemplu, cablu țintă incorect, hub fără alimentare sau cip HID defect); verificați lista de verificare și secțiunile de mai jos. Software-ul blochează, de asemenea, conexiunile suplimentare de tastatură/mouse până când cablajul/problema se rezolvă.

---

## **1. Conectare incorectă a cablului**

**Problemă:**  
Surprinzător de frecvent: utilizatorii uită să conecteze portul Openterface Target Type-C la computerul țintă.

**Soluție:**  
✅ Verificați întotdeauna:
- **Cablul Type-C țintă** este conectat în siguranță de la **portul țintă** Openterface la **computerul țintă** pe care doriți să îl controlați.
- **Cablul USB-A/USB-C gazdă** este conectat la **computerul gazdă/controller** (unde rulează OpenterfaceQt sau software-ul de control).

> **Sfat:** Etichetați cablurile pentru a evita confuzia în configurații complexe.
- Conectați cablul negru pe partea neagră a conectatorului țintă.
- Conectați cablul portocaliu pe partea acoperită de portocaliu a conectatorului țintă.


## **2. Utilizarea hub-urilor USB fără alimentare**

**Problemă:**  
Conectarea Openterface printr-un hub USB fără alimentare poate duce la **insuficient furnizare de energie** (cădere de tensiune VBUS). Aceasta poate determina dispozitivul să se comporte neregulat sau să nu inițializeze funcțiile HID (tastatură/mouse).

**Soluție:**  
✅ **Evitați hub-urile USB fără alimentare** între Openterface și computerul țintă.  
✅ Dacă este necesar un hub, utilizați un **hub USB de înaltă calitate alimentat extern** care poate furniza o alimentare stabilă de 5V.

> **Notă:** Alimentarea USB este critică pentru funcționarea fiabilă a cipului HID. Căderea tensiunii poate declanșa defecte interne.

---

## **3. Cip-ul HID intră în "stare zombie"**

**Problemă:**  
În anumite condiții — cum ar fi rafale de comenzi rapide combinate cu alimentare marginală — cipul HID intern (de exemplu, CH9329) poate intra într-o **"stare zombie".** În această stare:
- Cip-ul HID se blochează și oprește trimiterea datelor de răspuns serial la computerul gazdă.
- Păstrează o stare de eroare internă care previne reinitializarea normală de către software-ul gazdă.
- Dispozitivul poate părea conectat (video prezent) în timp ce intrările rămân fără răspuns.
- Software-ul gazdă (de exemplu, OpenterfaceQt) nu poate reinitializa corect dispozitivul.
- Reconnectarea tuturor cablurilor sau ciclul de alimentare al conexiunii USB nu șterge de obicei această eroare internă; este necesară o resetare de fabrică a cipului HID.

**Soluție:**  
Efectuați o **resetare de fabrică a cipului HID**:

- Pe **macOS**: Utilizați **Instrumentul de resetare serială** disponibil în **Meniu avansat** al utilitarului macOS.  

    <img src="https://assets.openterface.com/images/software/MacOS_FactoryResetHID.webp" alt="Serial Reset Tool (macOS)" width="150" />

- În **OpenterfaceQt** (aplicație desktop): Accesați **Meniu avansat → Resetare de fabrică cip HID**.

    <img src="https://assets.openterface.com/images/software/OpenterfaceQT_FactoryResetHID.webp" alt="Factory Reset HID Chip (OpenterfaceQt)" width="150" />

> Aceasta șterge starea internă a cipului și restabilește funcționarea normală.

---

## **4. Sensibilitatea ratei de transmisie în medii zgomotoase**

**Problemă:**  
Openterface utilizează implicit o rată de transmisie de **115200 bps** pentru transmiterea mai rapidă a datelor mouse-ului. Cu toate acestea, în mediile zgomotoase din punct de vedere electric (de exemplu, alimentări comutate sau cabluri lungi/neecranate), această rată de transmisie ridicată poate duce la **erori de comunicare serială**, cauzând pierderea sau coruperea comenzilor HID.

**Soluție:**  
Comutați la o rată de transmisie de **9600 bps**:
- Aceasta îmbunătățește semnificativ **fiabilitatea comunicației** în configurații zgomotoase.
- Impactul asupra latență este **neglijabil** în utilizarea tipică (de exemplu, captura video la 30 fps și control).

> **Recomandare:** Dacă experimentați probleme intermitente de intrare fără probleme de alimentare sau conexiune, încercați să reduceți rata de transmisie în configurația Openterface.

---

## **Lista de verificare rezumată**

Dacă tastatura/mouse-ul nu funcționează:

1. ✅ Confirmați că **cablul Type-C țintă** corect este conectat la **computerul țintă**.
2. ✅ Evitați hub-urile USB fără alimentare — utilizați conexiune directă sau un **hub alimentat**.
3. ✅ Dacă dispozitivul pare "înghețat", **resetați cipul HID** prin software.
4. ✅ În medii instabile, **reduceți rata de transmisie la 9600** pentru comunicație mai robustă.
5. ✅ Dacă încercările de mai sus nu ajută, încercați un port USB diferit pe gazdă sau reporniți computerul gazdă — OS-ul poate dezactiva un port sau hub-ul după ce primește prea multe pachete de eroare USB. Comutarea porturilor sau repornirea gazdei restabilește de obicei conexiunea.

---

Prin abordarea acestor patru domenii, majoritatea problemelor intermitente de HID pot fi prevenite sau rezolvate rapid. Pentru probleme persistente, vă rog contactați suportul (support@openterface.com) cu detaliile configurației și jurnalele dumneavoastră.
