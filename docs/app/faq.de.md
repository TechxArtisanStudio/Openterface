# FAQs für Apps

Willkommen bei den FAQs für unsere Apps. Wenn Sie die Antwort nicht finden, die Sie benötigen, **senden Sie uns eine E-Mail an [info@openterface.com](mailto:info@openterface.com)** oder **treten Sie unserer Community** auf [Discord](/discord) oder [Reddit](/reddit) bei, um sich mit unserem Entwicklungsteam und anderen Benutzern zu verbinden.

⚠️ *FAQs können veraltet werden — bitte lassen Sie uns wissen, wenn Sie etwas entdecken, das aktualisiert werden muss!*

### :material-clipboard-list: Fragenliste

- [Wo kann ich die Host-Anwendungen herunterladen?](#host-app-download)
- [Warum unterscheiden sich Funktionen zwischen verschiedenen Host-Apps?](#host-app-differences)
- [Welche Host-App bietet derzeit die beste Erfahrung?](#best-host-app)
- [Gibt es eine Host-App, die ChromeOS unterstützt?](#host-app-chromeos)
- [Gibt es eine Host-App, die Apples mobile Geräte unterstützt?](#host-app-ios)
- [Was ist, wenn F11 bei macOS-Anwendungen nicht funktioniert?](#f11-macos-issue)

#### :material-chat-question:{ .faq } Wo kann ich die Host-Anwendungen herunterladen? {: #host-app-download }

Besuchen Sie unsere [Host-Anwendung installieren Seite](/quick-start/#install-host-application) für offizielle Downloads, die **MacOS, Windows, Linux und Android** unterstützen.

??? warning "Datenschutz & Sicherheit: Seien Sie vorsichtig bei der Verwendung von Drittanbieter-Host-Apps"
    Da unser Projekt Open Source ist, könnten Sie alternative Versionen von Host-Anwendungen finden, die mit unserem Mini-KVM kompatibel sind und von anderen entwickelt wurden. Während diese zusätzliche Funktionen bieten können, stellen Sie sicher, dass Sie ihre Sicherheits- und Datenschutzpraktiken überprüfen. **Das Openterface-Team kann die Sicherheit von Drittanbieter-Anwendungen nicht garantieren oder dafür verantwortlich sein**.

#### :material-chat-question:{ .faq } Warum unterscheiden sich Funktionen zwischen verschiedenen Host-Apps? {: #host-app-differences }

Unser Entwicklungsteam wartet aktiv Host-Anwendungen für macOS, Linux, Windows und Android, aber aufgrund plattformspezifischer Herausforderungen und begrenzter Ressourcen variiert der Entwicklungsfortschritt. Das bedeutet, dass einige Funktionen zuerst auf einer Plattform erscheinen könnten und länger brauchen, um auf anderen anzukommen.

Wir tun unser Bestes, um die Funktionsentwicklung auf allen Plattformen zu synchronisieren, aber es ist ein laufender Prozess.

Ihr Feedback spielt eine große Rolle bei der Gestaltung unserer Entwicklungsroadmap — sei es durch unsere [Community](/community/) oder unser [GitHub-Repository](/app/). Jeder Vorschlag hilft uns zu priorisieren, was Ihnen am wichtigsten ist!

Wenn Sie Entwickler sind, sind Ihre Beiträge unglaublich wertvoll — und wir würden Ihre Hilfe bei der Beschleunigung des Prozesses lieben!

#### :material-chat-question:{ .faq } Welche Host-App bietet derzeit die beste Erfahrung? {: #best-host-app }

Stand März 2025 bieten die Qt-basierten Host-Apps für Windows und Linux insgesamt den umfassendsten Funktionsumfang. Die macOS-Version sticht durch die flüssigste und raffinierteste Benutzererfahrung hervor, dank tieferer Systemintegration und UI-Verbesserungen. Die Android-App ist eine praktische Option unterwegs, mit mehr Funktionen, die stetig aufholen.

#### :material-chat-question:{ .faq } Gibt es eine Web-App, die ich auf Chrome oder anderen Plattformen verwenden kann? {: #host-app-chromeos }

Ja! Eines unserer großartigen Community-Mitglieder, [Kashall](https://github.com/kashalls/openterface-viewer/), hat **eine leichte Open-Source-Web-App** gebaut, die Sie direkt in Ihrem Browser verwenden können: [openterface-viewer.pages.dev](https://openterface-viewer.pages.dev). Es ist noch nicht Teil unserer offiziellen Dokumentation, aber unser Entwicklungsteam hat es ausprobiert und fand es solide, einfach zu verwenden und super praktisch — besonders auf Chrome oder wenn Sie etwas Schnelles und Browser-basiertes wollen. Probieren Sie es aus!

#### :material-chat-question:{ .faq } Gibt es eine Host-App, die Apples mobile Geräte unterstützt? {: #host-app-ios }

Wir erkunden derzeit die Kompatibilität mit Apples mobilen Systemen wie iOS und iPadOS. Aufgrund von Apples strengen Kontrollen unterstützen diese Plattformen möglicherweise keine kabelgebundenen Verbindungen mit Drittanbieter-Geräten. Die Situation könnte sich jedoch ändern, oder es könnte potenzielle Workarounds geben. Wenn Sie Einblicke oder Vorschläge haben, laden wir Sie ein, unserer Community beizutreten, um sie mit uns zu diskutieren. Wir sind verpflichtet, die Bequemlichkeit unseres Geräts zu verbessern, indem wir so viele Systeme wie möglich unterstützen. Wenn Sie daran interessiert sind, bei unserer Entwicklung zu helfen, kommen Sie in der Community vorbei oder senden Sie uns eine E-Mail!

#### :material-chat-question:{ .faq } Was ist, wenn F11 bei macOS-Anwendungen nicht funktioniert? {: #f11-macos-issue }

Auf macOS zeigt das Drücken von F11 den macOS-Desktop an, anstatt die F11-Taste an die App und den Zielcomputer weiterzugeben. Um dies zu beheben, können Sie F11 von der "Desktop anzeigen"-Funktion entkoppeln.

???+ info "F11-Tastenproblem auf macOS beheben"
    1. Gehen Sie zu **Systemeinstellungen**.
    2. Wählen Sie **Desktop & Dock**.
    3. Scrollen Sie nach unten und klicken Sie auf die Schaltfläche **"Tastenkürzel…"**.
    4. Finden Sie **"Desktop anzeigen"** und setzen Sie es auf den Bindestrich **(-)** am Ende der Dropdown-Liste.
    5. Diese Änderung ermöglicht es der F11-Taste, an Ihre Anwendung auf dem Zielcomputer weitergegeben zu werden.
