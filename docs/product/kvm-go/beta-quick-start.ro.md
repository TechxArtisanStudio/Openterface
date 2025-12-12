---
title: "Ghid rapid KVM-GO Beta | Instrucțiuni testare beta Openterface"
description: "Ghid complet de testare beta pentru Openterface KVM-GO. Află cum să testezi inactivitate prelungită, hot-plug, acces BIOS, copiere-lipire și setări de simulare dispozitiv. Trimite feedback prin chestionarul nostru beta."
keywords: "KVM-GO beta, testare beta Openterface, ghid beta KVM-GO, instrucțiuni tester beta, feedback KVM-GO, chestionar beta, KVM peste USB beta, testare control headless, USB KVM beta"
---

# Ghid rapid KVM-GO Beta

> Scris cu ❤️ de [Iker](https://github.com/IkerGarcia) din comunitatea Openterface — îți mulțumim că ne ajuți să îmbunătățim documentația!

Bun venit la [KVM-GO Beta](/product/kvm-go/updates/251007-kvm-go-beta-test-kits-sent-1/)! Mai jos găsești o versiune prescurtată a chestionarului de feedback pentru programul beta. Parcurge fiecare secțiune, notează concluziile tale și, după ce termini, trimite totul prin [formularul Google pentru feedback-ul beta](https://openterface.com/product/kvm-go/beta-questions).

Felicitări pentru că ai fost selectat drept tester beta! Suntem extrem de nerăbdători să aflăm părerile tale și suntem siguri că vei testa dispozitivul în profunzime, în scenarii variate.

Acest test îți permite să explorezi flexibil, însă ne-ar plăcea să te concentrezi pe câteva scenarii specifice.

Feedback-ul tău este foarte valoros pentru noi și, deși ești liber să testezi și alte aspecte ale dispozitivului, acestea sunt zonele principale pe care vrem să le analizăm:

1. **Test de inactivitate prelungită**

    1. Pornește software-ul și conectează-te la un target
    2. Lasă software-ul să ruleze fără interacțiune pentru o perioadă extinsă (câteva ore)
    3. Revino și încearcă să folosești comenzile pentru mouse și tastatură
    - După perioada de inactivitate, mouse-ul și tastatura au funcționat normal când te-ai întors?

2. **Test de hot-plug**

    - Te rugăm să testezi scoaterea și reconectarea dispozitivului în timp ce software-ul rulează.

3. **Acces BIOS și nivel scăzut**

4. **Copiere și lipire (text scurt și text lung)**

5. **Setări de simulare a dispozitivului (Windows/Linux)**

    - 5.1. Configurarea EDID a afișajului
    - 5.2. Identificarea dispozitivului USB (VID/PID)
    - 5.3. Funcționalitatea cardului SD
        - Caz de utilizare 1 - Instalare de sistem: îți recomandăm să încerci Ventoy, un instrument care permite plasarea mai multor fișiere ISO pe un singur card SD și selectarea celui pe care vrei să îl pornești. Ai încercat să scrii o imagine de sistem pe HOST și apoi să treci la TARGET pentru instalare (fără să scoți cardul)?
        - Caz de utilizare 2 - Transfer de fișiere: ai folosit cardul SD pentru a transfera fișiere între HOST și TARGET?

Aceste exemple reflectă o parte dintre întrebările incluse în formularul de feedback beta și sunt însoțite de solicitări privind informații generale despre consistența audio/video/tastatură/mouse sau despre gestionarea temperaturii.

Îți mulțumim pentru ajutor!

!!! reminder "Nu uita"
    Trimite toate observațiile prin Google Form pentru ca echipa să le poată analiza rapid.

