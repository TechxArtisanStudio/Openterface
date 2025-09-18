# Întrebări Frecvente pentru Aplicații

Bun venit la întrebările frecvente pentru aplicațiile noastre. Dacă nu găsiți răspunsul de care aveți nevoie, **trimiteți-ne un email la [info@openterface.com](mailto:info@openterface.com)** sau **alăturați-vă comunității noastre** pe [Discord](/discord) sau [Reddit](/reddit) pentru a vă conecta cu echipa noastră de dezvoltare și alți utilizatori.

⚠️ *Întrebările frecvente pot deveni învechite — vă rugăm să ne anunțați dacă observați ceva care trebuie actualizat!*

### :material-clipboard-list: Lista Întrebărilor

- [Unde pot descărca aplicațiile host?](#host-app-download)
- [De ce funcționalitățile diferă între diferite aplicații host?](#host-app-differences)
- [Care aplicație host oferă în prezent cea mai bună experiență?](#best-host-app)
- [Există o aplicație host care să suporte ChromeOS?](#host-app-chromeos)
- [Există o aplicație host care să suporte dispozitivele mobile Apple?](#host-app-ios)
- [Ce să fac dacă F11 nu funcționează în aplicațiile macOS?](#f11-macos-issue)

#### :material-chat-question:{ .faq } Unde pot descărca aplicațiile host? {: #host-app-download }

Vizitați pagina noastră [Instalare Aplicație Host](/quick-start/#install-host-application) pentru descărcări oficiale care suportă **MacOS, Windows, Linux și Android**.

??? warning "Confidențialitate și Securitate: Fiți atenți când folosiți aplicații host de la terți"
    Deoarece proiectul nostru este open source, s-ar putea să găsiți versiuni alternative de aplicații host compatibile cu Mini-KVM-ul nostru dezvoltate de alții. Deși acestea pot oferi funcționalități suplimentare, vă rugăm să vă asigurați că le examinați practicile de securitate și confidențialitate. **Echipa Openterface nu poate garanta sau fi responsabilă pentru siguranța aplicațiilor de la terți**.

#### :material-chat-question:{ .faq } De ce funcționalitățile diferă între diferite aplicații host? {: #host-app-differences }

Echipa noastră de dezvoltare menține activ aplicații host pentru macOS, Linux, Windows și Android, dar din cauza provocărilor specifice platformei și resurselor limitate, progresul dezvoltării variază. Aceasta înseamnă că unele funcționalități s-ar putea să apară mai întâi pe o platformă și să dureze mai mult să ajungă pe altele.

Facem tot posibilul să sincronizăm dezvoltarea funcționalităților pe toate platformele, dar este o muncă în progres.

Feedback-ul vostru joacă un rol important în formarea drumului nostru de dezvoltare — fie prin [comunitatea](/community/) noastră, fie prin [depozitul nostru GitHub](/app/). Fiecare sugestie ne ajută să prioritizăm ceea ce vă pasă cel mai mult!

Dacă sunteți dezvoltatori, contribuțiile voastre sunt incredibil de valoroase — și ne-ar plăcea ajutorul vostru pentru a accelera procesul!

#### :material-chat-question:{ .faq } Care aplicație host oferă în prezent cea mai bună experiență? {: #best-host-app }

În martie 2025, aplicațiile host bazate pe Qt pentru Windows și Linux oferă cel mai cuprinzător set de funcționalități în general. Versiunea macOS se remarcă prin cea mai fluidă și rafinată experiență de utilizator, datorită integrării mai profunde în sistem și îmbunătățirilor UI. Aplicația Android este o opțiune convenabilă în mișcare, cu mai multe funcționalități care recuperează constant terenul.

#### :material-chat-question:{ .faq } Există o aplicație web pe care o pot folosi pe Chrome sau alte platforme? {: #host-app-chromeos }

Da! Unul dintre membrii fantastici ai comunității noastre, [Kashall](https://github.com/kashalls/openterface-viewer/), a construit **o aplicație web open source ușoară** pe care o puteți folosi direct în browser-ul vostru: [openterface-viewer.pages.dev](https://openterface-viewer.pages.dev). Nu face încă parte din documentația noastră oficială, dar echipa noastră de dezvoltare a încercat-o și a găsit-o solidă, ușor de folosit și super practică — mai ales pe Chrome sau când vreți ceva rapid și bazat pe browser. Încercați-o!

#### :material-chat-question:{ .faq } Există o aplicație host care să suporte dispozitivele mobile Apple? {: #host-app-ios }

Explorăm în prezent compatibilitatea cu sistemele mobile Apple, cum ar fi iOS și iPadOS. Din cauza controlurilor stricte ale Apple, aceste platforme s-ar putea să nu suporte conexiuni prin cablu cu dispozitive de la terți. Cu toate acestea, situația s-ar putea schimba, sau ar putea exista soluții alternative potențiale. Dacă aveți perspective sau sugestii, vă invităm să vă alăturați comunității noastre pentru a le discuta cu noi. Suntem angajați să îmbunătățim conveniența dispozitivului nostru suportând cât mai multe sisteme posibil. Dacă sunteți dornici să ajutați cu dezvoltarea noastră, veniți să petreceți timp cu noi în comunitate sau să ne trimiteți un email!

#### :material-chat-question:{ .faq } Ce să fac dacă F11 nu funcționează în aplicațiile macOS? {: #f11-macos-issue }

Pe macOS, apăsarea tastei F11 afișează desktop-ul macOS în loc să transmită tasta F11 către aplicație și computerul țintă. Pentru a corecta acest lucru, puteți să dezlegați F11 de la funcția "Afișare Desktop".

???+ info "Corectarea problemei tastei F11 pe macOS"
    1. Mergeți la **Setări Sistem**.
    2. Selectați **Desktop și Dock**.
    3. Derulați în jos și faceți clic pe butonul **"Scurtături…"**.
    4. Găsiți **"Afișare Desktop"** și setați-l la cratima **(-)** în partea de jos a listei derulante.
    5. Această modificare va permite tastei F11 să treacă către aplicația voastră pe computerul țintă.
