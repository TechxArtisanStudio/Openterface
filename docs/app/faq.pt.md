# FAQs para Apps

Bem-vindos às FAQs das nossas apps. Se não encontrarem a resposta de que precisam, **enviem-nos um email para [info@openterface.com](mailto:info@openterface.com)** ou **juntem-se à nossa comunidade** no [Discord](/discord) ou [Reddit](/reddit) para se conectarem com a nossa equipa de desenvolvimento e outros utilizadores.

⚠️ *As FAQs podem ficar desatualizadas — por favor informem-nos se encontrarem algo que precisa de ser atualizado!*

### :material-clipboard-list: Lista de Perguntas

- [Onde posso descarregar as aplicações host?](#host-app-download)
- [Por que é que as funcionalidades diferem entre diferentes apps host?](#host-app-differences)
- [Qual app host oferece atualmente a melhor experiência?](#best-host-app)
- [Há uma app host que suporte ChromeOS?](#host-app-chromeos)
- [Há uma app host que suporte os dispositivos móveis da Apple?](#host-app-ios)
- [O que fazer se F11 não funcionar nas aplicações macOS?](#f11-macos-issue)

#### :material-chat-question:{ .faq } Onde posso descarregar as aplicações host? {: #host-app-download }

Visitem a nossa [página de instalação de aplicação host](/quick-start/#install-host-application) para descarregamentos oficiais que suportam **MacOS, Windows, Linux e Android**.

??? warning "Privacidade e Segurança: Tenham cuidado ao usar apps host de terceiros"
    Como o nosso projeto é open source, podem encontrar versões alternativas de aplicações host compatíveis com o nosso Mini-KVM desenvolvidas por outros. Embora estas possam oferecer funcionalidades adicionais, certifiquem-se de rever as suas práticas de segurança e privacidade. **A equipa Openterface não pode garantir ou ser responsável pela segurança de aplicações de terceiros**.

#### :material-chat-question:{ .faq } Por que é que as funcionalidades diferem entre diferentes apps host? {: #host-app-differences }

A nossa equipa de desenvolvimento mantém ativamente aplicações host para macOS, Linux, Windows e Android, mas devido a desafios específicos da plataforma e recursos limitados, o progresso de desenvolvimento varia. Isto significa que algumas funcionalidades podem aparecer primeiro numa plataforma e demorar mais tempo a chegar a outras.

Estamos a fazer o nosso melhor para sincronizar o desenvolvimento de funcionalidades em todas as plataformas, mas é um trabalho em progresso.

O vosso feedback desempenha um papel importante na formação da nossa rota de desenvolvimento — seja através da nossa [comunidade](/community/) ou do nosso [repositório GitHub](/app/). Cada sugestão ajuda-nos a priorizar o que mais vos importa!

Se são desenvolvedores, as vossas contribuições são incrivelmente valiosas — e adoraríamos a vossa ajuda para acelerar o processo!

#### :material-chat-question:{ .faq } Qual app host oferece atualmente a melhor experiência? {: #best-host-app }

Em março de 2025, as apps host baseadas em Qt para Windows e Linux oferecem o conjunto de funcionalidades mais abrangente no geral. A versão macOS destaca-se pela sua experiência de utilizador mais suave e refinada, graças a uma integração de sistema mais profunda e melhorias de UI. A app Android é uma opção conveniente em movimento, com mais funcionalidades a recuperar terreno constantemente.

#### :material-chat-question:{ .faq } Há uma app web que posso usar no Chrome ou outras plataformas? {: #host-app-chromeos }

Sim! Um dos nossos fantásticos membros da comunidade, [Kashall](https://github.com/kashalls/openterface-viewer/), construiu **uma app web open source leve** que podem usar diretamente no vosso navegador: [openterface-viewer.pages.dev](https://openterface-viewer.pages.dev). Ainda não faz parte da nossa documentação oficial, mas a nossa equipa de desenvolvimento testou-a e achou-a sólida, fácil de usar e super prática — especialmente no Chrome ou quando querem algo rápido e baseado em navegador. Experimentem!

#### :material-chat-question:{ .faq } Há uma app host que suporte os dispositivos móveis da Apple? {: #host-app-ios }

Estamos atualmente a explorar compatibilidade com os sistemas móveis da Apple, como iOS e iPadOS. Devido aos controlos rigorosos da Apple, estas plataformas podem não suportar ligações com fios a dispositivos de terceiros. No entanto, a situação pode mudar, ou pode haver potenciais soluções alternativas. Se têm insights ou sugestões, convidamo-vos a juntarem-se à nossa comunidade para as discutir connosco. Estamos comprometidos a melhorar a conveniência do nosso dispositivo suportando tantos sistemas quanto possível. Se estão ansiosos para ajudar com o nosso desenvolvimento, venham passar tempo connosco na comunidade ou enviem-nos um email!

#### :material-chat-question:{ .faq } O que fazer se F11 não funcionar nas aplicações macOS? {: #f11-macos-issue }

No macOS, pressionar F11 mostra o desktop macOS em vez de passar a tecla F11 para a app e o computador alvo. Para corrigir isto, podem desvincular F11 da função "Mostrar Desktop".

???+ info "Corrigindo o problema da tecla F11 no macOS"
    1. Vão para **Definições do Sistema**.
    2. Selecionem **Desktop e Dock**.
    3. Deslizem para baixo e cliquem no botão **"Atalhos…"**.
    4. Encontrem **"Mostrar Desktop"** e definam-no para o hífen **(-)** na parte inferior da lista pendente.
    5. Esta mudança permitirá que a tecla F11 passe para a vossa aplicação no computador alvo.
