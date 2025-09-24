---
draft: false
date: 2024-08-22
description: "Actualizare importantă Openterface Mini-KVM: certificarea CE completată, producția în desfășurare, noua ETA mijlocul lunii ianuarie. Hardware V1.9 finalizat cu pini de expansiune, dezvoltarea aplicației Android, ambalaj îmbunătățit și manual multilingv în progres."
keywords: "Openterface Mini-KVM, certificare CE, hardware V1.9, actualizare producție, cronogramă expediere, dezvoltare aplicație Android, pini expansiune, KVM-over-IP, control calitate, ambalaj produs, manual multilingv, USB KVM, fabricație tech, hardware open source, actualizare livrare"
---

# Depășind obstacolele: Actualizare progres și nouă cronologie

Salut tuturor,

Sper că vă descurcați bine. A trecut ceva timp de la ultima noastră actualizare. Aș vrea să pot spune că totul a mers fără probleme pentru Openterface, dar am întâlnit câteva obstacole care vor întârzia cronograma noastră de livrare. Deși nu era ceea ce ne așteptam, abordăm aceste provocări direct și facem progres constant cu multe vești bune de împărtășit. Acest post este o **lectură de 7 minute**, deci să ne scufundăm în detalii ca să știți exact unde stau lucrurile și ce urmează.

## Reglementare, producție și calitate

Înainte de a putea începe producția, a trebuit să trecem testele de calitate necesare conform reglementărilor, în special certificarea CE. Deoarece versiunea noastră toolkit include nu doar Mini-KVM-ul ci și mai multe accesorii, fiecare parte a trebuit să treacă prin teste CE. Aceste teste au durat mai mult decât ne așteptam (se pare că cablurile pot fi destul de pretențioase), dar vestea mare este că **am trecut CE pentru Mini-KVM-ul nostru și toate componentele sale!** Mai jos este o privire de ansamblu asupra certificărilor pentru toate părțile noastre: Mini-KVM, cablu HDMI, cablu Type-C portocaliu, cablu Type-C scurt negru și cablu VGA2HDMI. Cu certificarea în mână, cronograma noastră de producție este acum sigură, și producătorii noștri **produc în prezent toate părțile** în timp ce vorbesc.

![240823-0](https://www.crowdsupply.com/img/fcb5/db59e179-2413-4d57-8462-2285c007fcb5/openterface-240823-0_jpg_gallery-lg.jpg)
*Cerințele UKCA și CE sunt aceleași pentru produsele noastre electronice, cu CE acoperind și conformitatea RoHS.*

Acum două săptămâni, am vizitat unul dintre producătorii noștri pentru a-i instrui pe managerii lor de linie în controlul calității pentru cablurile portocalii înainte să ni le trimită. Acum, TOATE cablurile portocalii au fost produse și stau într-un colț al studioului nostru.
![240823-1](https://www.crowdsupply.com/img/28dc/34844b54-0e02-414d-b58b-d40e8abe28dc/openterface-240823-1_jpg_gallery-lg.jpg)
*Kevin și Shawn explicau metodele de testare pentru a se asigura că cablul portocaliu funcționează corect cu Openterface Mini-KVM-ul nostru.*

Vom face aceeași sarcină săptămâna aceasta pentru a instrui QA în prima linie de producție și pentru celelalte părți. Iată probe de cabluri suplimentare.
![240823-2](https://www.crowdsupply.com/img/e703/abb8ffa5-eb85-4eb9-b5f8-d8a3d349e703/openterface-240823-2_jpg_md-xl.jpg)
*Marcați cu mândrie cu logo-ul nostru TechxArtisan, acestea sunt probe ale cablului HDMI, cablului Type-C scurt și cablului VGA-to-HDMI.*

Ne așteptăm ca celelalte părți și Mini-KVM-urile să sosească în curând de la producătorii noștri, moment în care vom verifica din nou calitatea fiecărui component și le vom ambala corespunzător în studioul nostru înainte de expediere. Cu alte cuvinte, **echipa noastră va asigura personal calitatea** înainte să ajungă în mâinile voastre.

## Expediere, întârzieri potențiale și noua ETA

**Incertitudinea actuală se află în procesul de expediere**. După investigarea mai multor companii de expediere, am descoperit că expedierea va lua timp suplimentar deoarece probabil vom transfera pachetele printr-un depozit înainte de a ajunge la depozitul Crowd Supply. Încă dezbatem dacă să alegem transportul maritim sau aerian—vă rugăm să aveți răbdare cu noi încă câteva zile în timp ce rezolvăm aranjamentele.

Vămuirea este un alt obstacol potențial care ar putea cauza întârzieri neașteptate. Odată ce produsele noastre ajung la depozitul Crowd Supply din SUA, vor lua una sau două săptămâni pentru a fi expediate global bazat pe fiecare comandă. Pentru susținătorii din afara SUA, pachetele individuale vor trebui încă să treacă prin expedierea globală și vămuirea în țara de destinație.

Ținând cont de situația actuală și adăugând ceva timp de buffer, rămân prudent optimist că vom completa livrarea înainte de sfârșitul acestui an, cu **o nouă ETA de mijlocul lunii ianuarie**. Îmi pare cu adevărat rău pentru inconveniență și apreciez sprijinul și răbdarea voastră în timpul acestei schimbări.

## Hardware V1.9 finalizat

După cum ați putea ști din [postul nostru anterior de pe Reddit](https://www.reddit.com/r/Openterface_miniKVM/comments/1e25pco/openterface_minikvm_v19_with_pins_for_more/), am decis să **actualizăm hardware-ul nostru la V1.9**, incluzând un set de pini de expansiune hackabili. Acest lucru nu făcea parte din planul original pentru campania de crowdfunding, dar credem că îmbunătățește semnificativ **potențialul pentru utilizare mai largă** a hardware-ului.

![240823-3](https://www.crowdsupply.com/img/77d7/09a9d0e5-3065-4f3e-8b61-bae66b5c77d7/openterface-240823-3_jpg_md-xl.jpg)
*Pinii VCC, GND, Target D+, Target D-, Host D+ și Host D-—unde 'D' înseamnă date USB.*

O motivație cheie era să **permitem comutatorului USB să fie comutat la nivel de software**. De ce este acest lucru important? Pe harta noastră de drum, **vrem să suportăm o soluție KVM-over-IP**, cum ar fi VNC, în viitor. Ideea este să potrivim controlul KVM local cu protocolul VNC, permițând utilizatorilor să controleze de la distanță computerul țintă prin computerul gazdă. Într-un astfel de scenariu la distanță, capacitatea pentru utilizatori de a comuta portul USB este esențială, mai ales când sunt necesare transferuri de fișiere între gazdă și țintă.

**Pinii de expansiune deschid și posibilități pentru mai mult**, cum ar fi integrarea cu iPadOS, controlul ATX, bridging-ul de rețea și bypass-ul audio. Deși nu voi intra în toate detaliile aici, vă încurajez să vă alăturați comunității noastre Openterface pentru a discuta mai mult cu noi.

Această actualizare de hardware ar putea extinde potențial soluția noastră Openterface să opereze peste IP și să includă funcții mai avansate în timp ce își menține încă puterea sa centrală ca instrument KVM-over-USB plug-and-play—perfect pentru profesioniștii IT care navighează în medii IT incerte, cum ar fi centrele de date nefamiliare.

Sunt fericit să raportez că V1.9 a trecut testele noastre interne de bază și va fi finalizat ca versiunea oficială pentru toți susținătorii noștri. Cu toate acestea, această actualizare de hardware va necesita teste suplimentare, și orice dezvoltare bazată pe acești pini de expansiune va fi experimentală și probabil va avea bug-uri. Aici puteți contribui. Contăm pe comunitatea open-source să ne ajute să îmbunătățim Openterface împreună.

## Mai multe actualizări software

Pe frontul software, facem progrese emoționante. Ne scufundăm acum în **aplicația Openterface Android**! Aruncați o privire la acest [tweet](https://x.com/TechxArtisan/status/1825460088922071398) pentru o demonstrație timpurie care arată controlul KVM fluid, mișcarea mouse-ului și clicurile în acțiune. Mai multe funcții sunt pe drum, și ca întotdeauna, odată ce am lustruit codul puțin mai mult, **această aplicație va fi și ea open-sourced** în repo-ul nostru GitHub [Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android).
![240823-4](https://www.crowdsupply.com/img/7007/b192f260-1e1f-4dab-905b-fb0a6d927007/openterface-240823-4_jpg_md-xl.jpg)
*Folosind doar vârfurile degetelor pentru a controla KVM un computer Linux de pe o tabletă Android. Frumos!*

Versiunea noastră QT tocmai a primit o actualizare utilă—acum puteți [transfera text de la gazdă la țintă](https://x.com/TechxArtisan/status/1825919721960780131)! Deci acum această funcție este suportată pe aplicațiile gazdă macOS, Windows și Linux.

Mai mult, planificăm și să adăugăm o funcție distractivă—[o mișcare automată a mouse-ului pentru a preveni ca computerul vostru țintă să adoarmă](https://x.com/TechxArtisan/status/1825471186668847241). Ar trebui să mergem cu mingea de ping-pong care sare în jurul ecranului sau efectul clasic al screensaver-ului DVD? Votați și comentați [tweet-ul](https://x.com/TechxArtisan/status/1825470086800691459) 😃

## Design pachet, etichetare și manual

Am [experimentat cu diverse mock-up-uri și designuri de ambalare](https://www.reddit.com/r/Openterface_miniKVM/comments/1elm4vq/almost_ready_to_finalize_our_package_design/) pentru a găsi echilibrul perfect între mai mulți factori cheie:

- Selectarea materialelor suficient de robuste pentru a proteja produsul și părțile sale în timpul expedierii,
- Crearea etichetării informative care ajută utilizatorii să înțeleagă produsul dintr-o privire,
- Asigurarea conformității cu reglementările,
- Făcerea ambalajului vizual atractiv,
- Și fiind eco-friendly prin minimizarea utilizării plasticului oriunde este posibil.

În plus, am făcut mai multe îmbunătățiri la vechea geantă toolkit, incluzând:

- Spațiu de stocare mai mare,
- Un fermoar portocaliu elegant,
- Materiale exterioare și interioare actualizate,
- Și o buzunar de plasă super elastică.

Am ales acest material pentru că atinge echilibrul ideal între a fi prietenos cu bugetul, plăcut la atingere și suficient de durabil pentru a proteja articolele din interior. **Suntem încrezători că o veți iubi**.

![240823-5](https://www.crowdsupply.com/img/099a/75e16f52-bd0c-4652-af27-08caf448099a/openterface-240823-5_jpg_md-xl.jpg)

Actualizăm și etichetele pe carcasa de aluminiu pentru a le face cât mai informative și vizual atractive posibil. Sperăm că aceste îmbunătățiri vor îmbunătăți experiența voastră de utilizator și vor face mai ușor să începeți cu Openterface.

![240823-6](https://www.crowdsupply.com/img/94d8/441a5757-2d6a-4c79-885b-7b5b3a7094d8/openterface-240823-6_jpg_md-xl.jpg)

Finalizăm manualul Openterface, care va fi disponibil în engleză, germană, franceză, japoneză și chineză. Scuze dacă am ratat limba voastră—cutia noastră nu este de mărimea TARDIS (cutia de poliție a Doctor Who)! Dar vom face tot posibilul să adăugăm mai multe traduceri pe site-ul nostru.

![240823-7](https://www.crowdsupply.com/img/e2d9/2e5a2086-20f0-47ec-a27b-288d10d0e2d9/openterface-240823-7_jpg_md-xl.jpg)

## Revizuirea limbii comunității

Am folosit ChatGPT pentru a ajuta cu traducerile, dar uneori poate rata ținta cu frazele și alegerea cuvintelor. Dacă nu este prea multă problemă, aș aprecia foarte mult orice ajutor în revizuirea conținutului în alte limbi, în special pentru materialele tipărite pe care suntem pe cale să le finalizăm. Am actualizat tot conținutul textual pentru ambalare în folderul nostru GitHub [product-printed-materials](https://github.com/TechxArtisanStudio/Openterface/tree/main/product-printed-materials), unde puteți revizui și trimite orice îmbunătățire. Puteți să-mi trimiteți și DM direct. Mulțumesc!

## Observații finale și progres în desfășurare

Ne scuzăm din nou pentru întârzierile și schimbarea în ETA-ul produsului nostru. Mulțumesc pentru răbdarea și pentru că rămâneți cu noi—lucrăm din greu să vi-l aducem cât mai repede posibil! Vă voi actualiza imediat odată ce expedierea noastră va fi aranjată. Mai multe actualizări sunt pe drum, deci alăturați-vă comunității noastre Openterface și rămâneți conectați!

Noroc,

Billy Wang  
Manager Produs  
Echipa Openterface | TechxArtisan
