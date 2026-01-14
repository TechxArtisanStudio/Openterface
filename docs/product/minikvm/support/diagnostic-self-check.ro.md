---
titlu: „Openterface Mini-KVM - Ghid pentru verificare auto-diagnostic”
descriere: „Ghid pas cu pas pentru rularea verificărilor auto-diagnostice pe dispozitivul Openterface Mini-KVM. Învață cum să testezi conexiunile USB, să detectezi probleme și să trimiti rapoarte de defecte către suport.”
cuvinte cheie: „Openterface Mini-KVM, verificare auto-diagnostic, depanare KVM, diagnostic USB KVM, suport Mini-KVM, testare dispozitiv KVM, test conexiune USB, raport de defect KVM, ghid pentru depanare Mini-KVM, instrument diagnostic KVM, diagnostice server headless, unelte pentru depanare IT”
---

# Openterface Mini-KVM - Ghid pentru verificare auto-diagnostic

Acest ghid oferă instrucțiuni pas cu pas pentru rularea verificărilor auto-diagnostice pe dispozitivul Openterface Mini-KVM.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-K6Idzky3fY?si=r7pZgCkBzzZXgrLT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Unitate bună

**Pasul 1:** În aplicația Openterface, deschide Setări → Setări…

**Pasul 2:** În fereastra de setări, mearge la Avansat și Debug.

**Pasul 3:** Clic pe Tool pentru Diagnosticare.

**Pasul 4:** Când este solicitat, clic pe Activare pentru a porni înregistrarea diagnosticului.

**Pasul 5:** Clic pe Verifică Acum pentru a începe verificarea auto.

**Pasul 6:** Clic pe Începe Test, apoi decuplează și recuplează USB-C negru (partea țintă) când este solicitat.

![minikvm-support-target](https://assets.openterface.com/images/minikvm/support/target.webp)

**Pasul 7:** Clic pe Începe Test, apoi decuplează și recuplează USB-C portocaliu (partea gazdă) când este solicitat.

![minikvm-support-host](https://assets.openterface.com/images/minikvm/support/host.webp)

**Pasul 8:** Clic pe Începe Test și așteaptă până când testul se completează.

**Pasul 9:** Clic pe Resetează Acum și așteaptă până când se completează.

**Pasul 10:** Clic pe Schimbă Acum și așteaptă până când comutarea vitezei baud se finalizează.

**Pasul 11:** Clic pe Începe Test, apoi așteaptă aproximativ 30 de secunde. Nu operați asupra țintei în timpul testului.

> **Notă:** Mausul poate se mișca rapid. Nu atingeți ținta.

![minikvm-support-stress_test](https://assets.openterface.com/images/minikvm/support/stress_test.gif)

**Pasul 12:** Confirmați că toate elementele arată marcate cu verde și progresul este complet.

**Pasul 13:** Clic pe ❌ (dreapta sus) pentru a închide fereastra de Diagnosticare.

---

## Detectat o problemă (Exemplu tastatură/maus)

Urmăriți pașii 1–11 din secțiunea „Unitate bună” mai întâi. Notele de mai jos explică ceea ce veți vedea atunci când este detectată o problemă cu tastatura/mausul.

## Cum se manifestă această problemă

În acest exemplu, Conexiunea Generală arată mai întâi ECHEC deoarece o problemă cu tastatura/mausul (HID) din partea țintei afectează verificarea generală. Acesta este un indicator timpuriu, nu o problemă separată. (Veți vedea starea ECHEC evidențiată lângă „Conexiunea Generală” din stânga.)

- **Conexiunea Generală:** ECHEC este arătat mai întâi din cauza problemei de pe partea țintei.

![minikvm-support-overall_connection](https://assets.openterface.com/images/minikvm/support/overall_connection.webp)

- **Conectare Plug & Play la țintă:** După ce rulați acest pas, rezultatul poate arăta problema de pe partea țintei mai clar.

> **Sfat:** Dacă un pas arată ECHEC, diagnosticul nu se oprește, dar poate opri automat avansarea—deci vei avea nevoie să continui manual.

## Test final suplimentar (în funcție de tipul problemei)

**Pasul 12:** După testul de stres, diagnosticul poate arăta un test final suplimentar în funcție de problema detectată; în acest exemplu cu tastatură/maus, continuă la Verificarea Portului Țintă.

**Pasul 13:** Clic pe „Detectare Dispozitive” pentru a începe Verificarea Portului Țintă, apoi urmați instrucțiunile de pe ecran.

![minikvm-support-target_port_checking](https://assets.openterface.com/images/minikvm/support/target_port_checking.webp)

## Ce se întâmplă atunci când este detectată o problemă

**Pasul 14:** Pentru a continua, clic pe Next (bara de jos) sau selectați următorul test din panoul din stânga.

![minikvm-support-target_plug_n_play](https://assets.openterface.com/images/minikvm/support/target_plug_n_play.webp)

## Trimiterea logurilor către Suport

**Pasul 15:** Clic pe Trimite Raport Defect către Suport pentru a pregăti raportul pentru suport.

![minikvm-support-send_defect_report_to_support](https://assets.openterface.com/images/minikvm/support/send_defect_report_to_support.webp)

**Pasul 16:** În fereastra Raport Defect, introduceți **ID-ul comenzi** și **Numele**.

**Pasul 17:** Clic pe **Deschide Folder Loguri**, apoi atașați fișierele de log exportate la e-mailul dumneavoastră.

**Pasul 18:** Copiați **adresa de e-mail pentru suport**, lipiți subiectul și corpul preîncărcat al e-mailului, atașați o **fotografie clară a configurării** (Mini-KVM + conexiuni gazdă/țintă), și trimiteți e-mailul.

![minikvm-support-support](https://assets.openterface.com/images/minikvm/support/support.webp)

**Pasul 19:** Clic pe ❌ (dreapta sus) pentru a închide fereastra de Diagnosticare.