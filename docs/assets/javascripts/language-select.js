(function() {
  // Only run on the homepage
  if (window.location.pathname !== '/' && window.location.pathname !== '') {
    return;
  }

  const baseUrl = window.location.origin;
  const langMap = {
    'en': baseUrl + '/',
    'de': baseUrl + '/de/',
    'fr': baseUrl + '/fr/',
    'es': baseUrl + '/es/',
    'it': baseUrl + '/it/',
    'ja': baseUrl + '/ja/',
    'ko': baseUrl + '/ko/',
    'pt': baseUrl + '/pt/',
    'ru': baseUrl + '/ru/',
    'zh': baseUrl + '/zh/',
  };
  const langNames = { de: "Deutsch", en: "English", zh: "中文", fr: "Français", es: "Español", it: "Italiano", ja: "日本語", ko: "한국어", pt: "Português", ru: "Русский" };
  const userLang = (navigator.language || navigator.userLanguage || '').toLowerCase().slice(0,2);
  const currentBase = window.location.origin + '/';
  const currentLang = Object.keys(langMap).find(key => langMap[key] === currentBase);

  // Check if user has permanently dismissed the reminder
  const langReminderDismissedKey = 'lang-reminder-dismissed-' + userLang;
  const langReminderDismissed = localStorage.getItem(langReminderDismissedKey);

  // Only show the prompt if the user's language is different from the current site language
  // and reminder hasn't been permanently dismissed
  if (langMap[userLang] && currentBase !== langMap[userLang] && currentLang !== userLang && !langReminderDismissed) {
    // Wait for DOM to be ready to access Gibby dialogue
    function showLanguageReminder() {
      const gibbyDialogue = document.querySelector('.gibby-dialogue');
      if (!gibbyDialogue) {
        // Retry if Gibby dialogue not yet available
        setTimeout(showLanguageReminder, 100);
        return;
      }

      // Store original content to restore later
      const originalContent = gibbyDialogue.innerHTML;
      gibbyDialogue.setAttribute('data-original-content', originalContent);
      gibbyDialogue.classList.add('lang-reminder-active');

      const targetLang = langNames[userLang] || userLang;
      const currentLangName = langNames[currentLang] || currentLang || 'English';

      // Create language reminder content
      gibbyDialogue.innerHTML = `
        <p style="margin: 0 0 12px 0; font-size: 0.9rem; line-height: 1.4;">
          Switch to <b>${targetLang}</b>?
        </p>
        <div style="display: flex; gap: 8px; justify-content: center; flex-wrap: wrap;">
          <a href="${langMap[userLang]}" class="gibby-link lang-switch-btn" style="padding: 6px 16px; border-radius: 6px; background-color: var(--md-primary-fg-color); color: var(--md-primary-bg-color); text-decoration: none; font-size: 0.85rem; white-space: nowrap;">Switch</a>
          <button class="lang-stay-btn" style="padding: 6px 16px; border-radius: 6px; background-color: transparent; color: var(--md-default-fg-color); border: 1px solid var(--md-default-fg-color); cursor: pointer; font-size: 0.85rem; white-space: nowrap;">Stay</button>
        </div>
      `;

      // Show the dialogue
      gibbyDialogue.style.display = 'block';

      // Auto-hide after 15 seconds
      let autoHideTimer = setTimeout(function() {
        hideLanguageReminder();
      }, 15000);

      // Handle switch button click
      const switchBtn = gibbyDialogue.querySelector('.lang-switch-btn');
      if (switchBtn) {
        switchBtn.addEventListener('click', function(e) {
          clearTimeout(autoHideTimer);
          // Navigation will happen via href
        });
      }

      // Handle stay button click - permanently dismiss when clicked
      const stayBtn = gibbyDialogue.querySelector('.lang-stay-btn');
      if (stayBtn) {
        stayBtn.addEventListener('click', function(e) {
          e.preventDefault();
          clearTimeout(autoHideTimer);
          // Permanently dismiss the reminder for this language
          localStorage.setItem(langReminderDismissedKey, 'true');
          hideLanguageReminder();
        });
      }

      function hideLanguageReminder() {
        if (gibbyDialogue && gibbyDialogue.classList.contains('lang-reminder-active')) {
          // Restore original content
          const original = gibbyDialogue.getAttribute('data-original-content');
          if (original) {
            gibbyDialogue.innerHTML = original;
          }
          gibbyDialogue.classList.remove('lang-reminder-active');
          gibbyDialogue.style.display = 'none';
        }
      }
    }

    // Start showing reminder when DOM is ready
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', showLanguageReminder);
    } else {
      showLanguageReminder();
    }
  }
})();