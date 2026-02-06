---
titlu: „Openterface Mini-KVM (Windows) - Ghid pentru verificare auto-diagnostic hardware"
descriere: „Ghid pas cu pas pentru rularea verificării auto-diagnostice hardware în aplicația Openterface pentru Windows. Învață cum să testezi conexiunile USB, să detectezi probleme și să trimiti rapoarte de diagnostic către suport."
cuvinte cheie: „Openterface Mini-KVM, Windows, diagnostic hardware, verificare auto-diagnostic, depanare KVM, diagnostic USB KVM, suport Mini-KVM, testare dispozitiv KVM, Windows KVM, raport de defect KVM, ghid pentru depanare Mini-KVM"
---

# Openterface Mini-KVM (Windows) — Ghid pentru verificare auto-diagnostic hardware

Acest ghid explică cum să rulați verificarea auto-diagnostic **Hardware** în versiunea **Windows** a aplicației Openterface, și cum să trimiteți raportul de diagnostic către suport dacă este detectată o problemă.

<iframe width="560" height="315" src="https://www.youtube.com/embed/uSq3BDc_SBU?si=rREugsUxX1FzDGqm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Înainte de a începe

- **Actualizați aplicația:** Asigurați-vă că aveți cea mai recentă versiune a [aplicației Openterface pentru Windows](/app) instalată înainte de a rula diagnosticele. Verificați meniul aplicației pentru actualizări.
- Conectați Mini-KVM la **Gazdă** și **Țintă**.
- Păstrați dispozitivul țintă inactiv în timpul testării (în special în timpul Testului de Stres).

> **Important (Windows):** Diagnosticul **nu avansează automat**.  
> Pentru a trece între teste, folosiți **Next** (bara de jos) **sau** faceți clic pe un element de test din **panoul din stânga**.  
> Fiecare test se execută făcând clic pe **Verifică Acum**.

![next_webp](https://assets2.openterface.com/images/next.webp)

---

## Unitate funcțională (PASS)

### Pasul 1 — Deschideți Diagnostic Hardware (Windows)
În aplicația Openterface pentru Windows, deschideți: **Avansat → Diagnostic Hardware**.  

### Pasul 2 — Rulați verificarea auto
În fereastra Diagnostic Hardware, faceți clic pe **Verifică Acum** pentru a rula pasul de diagnostic curent.  

### Pasul 3 — Target Plug & Play (urmați instrucțiunile)
Când **Target Plug & Play** vă solicită să reconectați cablul țintă, urmați instrucțiunile de pe ecran.  
Unele configurații pot solicita să **deconectați/reconectați de mai multe ori** (de ex. de două ori).  

![Target-plug&play](https://assets2.openterface.com/images/Target-plug%26play.webp)

### Pasul 4 — Host Plug & Play (urmați instrucțiunile)
Urmați instrucțiunile de pe ecran pentru partea gazdă.  

![Host-plug&play](https://assets2.openterface.com/images/Host-plug%26play.webp)

### Pasul 5 — Test de Stres (nu atingeți ținta)
În timpul **Testului de Stres**, mausul țintă se poate în mișca automat pentru detectare.  
**Nu operați asupra țintei** în timp ce testul rulează.  

> **Notă:** Mausul se poate mișca rapid — nu atingeți ținta.

![stress-test](https://assets2.openterface.com/images/stress-test.webp)

### Pasul 6 — Confirmați PASS
Continuați până când verificarea auto se completează. Dacă totul este normal, rezultatele vor afișa **PASS / Toate testele au trecut**.  

---

## Detectat o problemă (Exemplu tastatură/maus)

Dacă este detectată o problemă, unul sau mai multe elemente pot afișa **ECHEC**.

### Pasul 1 — Rulați același Diagnostic Hardware
Deschideți **Avansat → Diagnostic Hardware**, apoi faceți clic pe **Verifică Acum** pentru a începe.  

### Pasul 2 — Continuați prin verificări
Continuați prin testele rămase până când diagnosticul se finalizează.  

### Pasul 3 — E-mailul de suport se deschide automat
Când diagnosticul se finalizează cu o problemă, o fereastră **E-mail Suport** se va deschide automat.  

---

## Trimiterea logurilor către Suport (Windows)

### Pasul 4 — Aplicați ID comandă + Nume
Introduceți **ID-ul comenzi** și **Numele**, apoi faceți clic pe **Aplicare** pentru a le insera în ciorna e-mailului. 

![ID+Name](https://assets2.openterface.com/images/ID+Name.webp)

### Pasul 5 — Copiați adresa de e-mail și ciorna
- Faceți clic pe **Copiază E-mail** pentru a copia adresa de e-mail pentru suport.
- Faceți clic pe **Copiază Ciornă** pentru a copia conținutul e-mailului precompletat (inclusiv ID comandă + Nume).  
Lipiți ambele în clientul de e-mail (Gmail/Outlook/etc.).  

![copy](https://assets2.openterface.com/images/copy.webp)

### Pasul 6 — Atașați fișierele de log corecte
Faceți clic pe **Deschide Folder Fișiere**. Instrumentul va indica ce fișiere să atașați.  
**Atașați doar fișierele de log solicitate** (folderul poate conține multe alte loguri).  

![list](https://assets2.openterface.com/images/list.webp)

![compress](https://assets2.openterface.com/images/compress.webp)

### Pasul 7 — De asemenea atașați o fotografie a configurării
În același e-mail, atașați o **fotografie clară a configurării** care arată:
- dispozitivul Mini-KVM,
- ambele conexiuni **Gazdă** și **Țintă**,
- porturi și cabluri clar vizibile.  

### Pasul 8 — Trimiteți e-mailul
Trimiteți e-mailul către suport (text ciornă + loguri solicitate + fotografie configurație atașate).  

---

## Ce să includeți când contactați suportul

- **ID comandă**
- **Fișiere solicitate de log de diagnostic**
- **Fotografie configurație** (Mini-KVM + cablare gazdă/țintă)
