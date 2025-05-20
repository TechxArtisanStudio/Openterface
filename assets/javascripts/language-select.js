(function() {
  // Only run on the homepage
  if (window.location.pathname !== '/' && window.location.pathname !== '') {
    return;
  }

  const langMap = {
    'en': 'https://openterface.com/',
    'de': 'https://de.openterface.com/',
    'fr': 'https://fr.openterface.com/',
    'es': 'https://es.openterface.com/',
    'it': 'https://it.openterface.com/',
    'ja': 'https://jp.openterface.com/',
    'ko': 'https://kr.openterface.com/',
    'pt': 'https://pt.openterface.com/',
    'ru': 'https://ru.openterface.com/',
    'zh': 'https://cn.openterface.com/',
  };
  const langNames = { de: "Deutsch", en: "English", zh: "中文", fr: "Français", es: "Español", it: "Italiano", ja: "日本語", ko: "한국어", pt: "Português", ru: "Русский" };
  const userLang = (navigator.language || navigator.userLanguage || '').toLowerCase().slice(0,2);
  const currentBase = window.location.origin + '/';

  if (langMap[userLang] && currentBase !== langMap[userLang]) {
    // Create overlay
    const overlay = document.createElement('div');
    overlay.style.position = 'fixed';
    overlay.style.top = 0;
    overlay.style.left = 0;
    overlay.style.width = '100vw';
    overlay.style.height = '100vh';
    overlay.style.background = 'rgba(0,0,0,0.45)';
    overlay.style.display = 'flex';
    overlay.style.alignItems = 'center';
    overlay.style.justifyContent = 'center';
    overlay.style.zIndex = 9999;

    // Create modal box
    const modal = document.createElement('div');
    modal.style.background = '#fff';
    modal.style.borderRadius = '12px';
    modal.style.boxShadow = '0 8px 32px rgba(0,0,0,0.18)';
    modal.style.padding = '2em 2.5em 1.5em 2.5em';
    modal.style.maxWidth = '90vw';
    modal.style.textAlign = 'center';
    modal.style.fontFamily = 'inherit';

    const targetLang = langNames[userLang] || userLang;
    modal.innerHTML = `
      <div style="font-size:2em; margin-bottom:0.5em;">🌐</div>
      <div style="font-size:1.2em; margin-bottom:1em; color:#222;">
        We detected your browser language is <b>${targetLang}</b>.<br>
        Do you want to switch to the <b>${targetLang}</b> site?
      </div>
      <div style="margin-top:1.5em;">
        <button id="lang-switch-yes" style="background:#eb8025fa;color:#fff;border:none;padding:0.7em 2em;border-radius:6px;font-size:1em;cursor:pointer;margin-right:1em;">Switch</button>
        <button id="lang-switch-no" style="background:#e0e0e0;color:#222;border:none;padding:0.7em 2em;border-radius:6px;font-size:1em;cursor:pointer;">Stay</button>
      </div>
    `;

    overlay.appendChild(modal);
    document.body.appendChild(overlay);

    // Auto-close after 10 seconds
    let autoCloseTimer = setTimeout(function() {
      if (document.body.contains(overlay)) {
        document.body.removeChild(overlay);
      }
    }, 10000);

    document.getElementById('lang-switch-yes').onclick = function() {
      clearTimeout(autoCloseTimer);
      window.location.href = langMap[userLang];
    };
    document.getElementById('lang-switch-no').onclick = function() {
      clearTimeout(autoCloseTimer);
      document.body.removeChild(overlay);
    };
  }
})();