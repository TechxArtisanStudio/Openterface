(function () {
  function text(el) {
    return (el && el.textContent ? el.textContent : "").trim();
  }

  function parseAbbrevNumber(raw) {
    const s = String(raw || "").replace(/,/g, "");
    const m = s.match(/(\d+(?:\.\d+)?)\s*([KMB])?/i);
    if (!m) return 0;
    let n = parseFloat(m[1]);
    const u = (m[2] || "").toUpperCase();
    if (u === "K") n *= 1e3;
    else if (u === "M") n *= 1e6;
    else if (u === "B") n *= 1e9;
    return Number.isFinite(n) ? Math.round(n) : 0;
  }

  function extractViews(card) {
    // Prefer stable data attribute if present (generated from youtube.csv)
    const dv = card && card.dataset ? card.dataset.views : "";
    if (dv && /^\d+$/.test(dv)) return parseInt(dv, 10);

    // Fallback: parse the "👁️ ..." stat line (e.g. "👁️ 60.1K views")
    const items = card ? card.querySelectorAll(".youtube-video-stats .youtube-stat-item") : [];
    for (const it of items) {
      const t = text(it);
      if (t.includes("👁")) return parseAbbrevNumber(t);
    }
    return 0;
  }

  function extractISODate(card) {
    const items = card.querySelectorAll(".youtube-video-stats .youtube-stat-item");
    for (const it of items) {
      const m = text(it).match(/(\d{4}-\d{2}-\d{2})/);
      if (m) return m[1];
    }
    return "";
  }

  function toTime(isoDate) {
    const t = Date.parse(isoDate);
    return Number.isFinite(t) ? t : 0;
  }

  function extractTag(card, selector) {
    const el = card.querySelector(selector);
    return text(el);
  }

  function languageNameFromCode(code) {
    const c = (code || "").toLowerCase();
    const map = {
      en: "English",
      zh: "Chinese",
      ja: "Japanese",
      ko: "Korean",
      fr: "French",
      de: "German",
      it: "Italian",
      es: "Spanish",
      pt: "Portuguese",
      ro: "Romanian",
    };
    return map[c] || (code ? code.toUpperCase() : "");
  }

  function uniqSorted(values) {
    return Array.from(new Set(values.filter(Boolean))).sort((a, b) =>
      a.localeCompare(b, undefined, { sensitivity: "base" })
    );
  }

  function populateSelect(selectEl, options) {
    if (!selectEl) return;
    const first = selectEl.querySelector("option"); // keep the first option (All ...)
    selectEl.innerHTML = "";
    if (first) selectEl.appendChild(first);

    for (const optItem of options) {
      const opt = document.createElement("option");
      opt.value = optItem.value;
      opt.textContent = optItem.label;
      selectEl.appendChild(opt);
    }
  }

  function setStatNumber(page, statKey, value) {
    const el = page.querySelector(`.youtube-stat-card[data-stat="${statKey}"] .number`);
    if (el) el.textContent = String(value);
  }

  function hasOption(selectEl, value) {
    if (!selectEl) return false;
    return Array.from(selectEl.options).some((o) => o.value === value);
  }

  function applyUrlState(sortEl, productEl, languageEl) {
    const sp = new URLSearchParams(window.location.search);
    const p = sp.get("p") || "";
    const l = sp.get("l") || "";
    const s = sp.get("s") || "";

    if (sortEl && (s === "newest" || s === "oldest" || s === "views")) sortEl.value = s;
    if (productEl && p && hasOption(productEl, p)) productEl.value = p;
    if (languageEl && l && hasOption(languageEl, l)) languageEl.value = l;
  }

  function syncUrlFromState(sortEl, productEl, languageEl) {
    const url = new URL(window.location.href);
    const sp = url.searchParams;

    const p = productEl ? productEl.value : "";
    const l = languageEl ? languageEl.value : "";
    const s = sortEl ? sortEl.value : "newest";

    if (p) sp.set("p", p);
    else sp.delete("p");

    if (l) sp.set("l", l);
    else sp.delete("l");

    if (s && s !== "newest") sp.set("s", s);
    else sp.delete("s");

    const qs = sp.toString();
    const next = `${url.pathname}${qs ? `?${qs}` : ""}${url.hash || ""}`;
    window.history.replaceState(null, "", next);
  }

  function detectPageLanguage() {
    // Extract language from URL path (e.g., /ja/videos -> "ja", /zh/videos -> "zh")
    const path = window.location.pathname;
    const langMatch = path.match(/^\/([a-z]{2})\//);
    return langMatch ? langMatch[1] : "en";
  }

  function init() {
    const page = document.querySelector(".youtube-videos-page");
    if (!page) return;

    const grid = page.querySelector(".youtube-videos-grid");
    if (!grid) return;

    const sortEl = page.querySelector("#yt-sort");
    const productEl = page.querySelector("#yt-filter-product");
    const languageEl = page.querySelector("#yt-filter-language");
    const visibleEl = page.querySelector("#yt-results-visible");
    const totalEl = page.querySelector("#yt-results-total");

    // Detect page language from URL
    const pageLanguage = detectPageLanguage();

    const cards = Array.from(grid.querySelectorAll(".youtube-video-card"));
    const meta = new Map();

    for (const card of cards) {
      const iso = card.dataset.date || extractISODate(card);
      const product = card.dataset.product || extractTag(card, ".youtube-video-tags .youtube-tag.product");
      const languageCode = card.dataset.language || "";
      const languageName =
        card.dataset.languageName ||
        (languageCode ? languageNameFromCode(languageCode) : extractTag(card, ".youtube-video-tags .youtube-tag.language"));

      meta.set(card, {
        dateISO: iso,
        dateTime: toTime(iso),
        viewsCount: extractViews(card),
        product,
        languageCode,
        languageName,
        // Store page language for prioritization
        pageLanguage: pageLanguage,
      });
    }

    // Update stat numbers (kept separate from translation)
    setStatNumber(page, "total_videos", cards.length);
    setStatNumber(page, "languages", uniqSorted(cards.map((c) => meta.get(c).languageCode || meta.get(c).languageName)).length);
    setStatNumber(page, "products", uniqSorted(cards.map((c) => meta.get(c).product)).length);

    // Populate filters from stable data-* attributes
    // Known products always shown (even with 0 videos); merge with products from cards
    const knownProducts = ["minikvm", "kvm-go", "uconsole-kvm-extension", "keymod"];
    const productDisplayNames = {
      minikvm: "Mini-KVM",
      "kvm-go": "KVM-Go",
      "uconsole-kvm-extension": "uConsole KVM Extension",
      keymod: "KeyMod",
    };
    const productsFromCards = cards.map((c) => meta.get(c).product).filter(Boolean);
    const allProducts = uniqSorted([...knownProducts, ...productsFromCards]);
    const productOptions = allProducts.map((p) => ({
      value: p,
      label: productDisplayNames[p] || p,
    }));
    populateSelect(productEl, productOptions);

    // Language: value is code (stable), label is name
    const langMap = new Map();
    for (const c of cards) {
      const m = meta.get(c);
      if (m.languageCode) langMap.set(m.languageCode, m.languageName || languageNameFromCode(m.languageCode));
    }
    const languageOptions = Array.from(langMap.entries())
      .map(([code, name]) => ({ value: code, label: name }))
      .sort((a, b) => a.label.localeCompare(b.label, undefined, { sensitivity: "base" }));
    populateSelect(languageEl, languageOptions);

    // Apply initial URL state after options exist
    applyUrlState(sortEl, productEl, languageEl);

    function apply() {
      const sortMode = sortEl ? sortEl.value : "newest";
      const wantProduct = productEl ? productEl.value : "";
      const wantLanguageCode = languageEl ? languageEl.value : "";
      
      // Prioritize by language when:
      // 1. No language filter is active (user hasn't selected a language filter)
      // 2. Page has a language prefix (e.g., /ja/videos)
      const shouldPrioritizeLanguage = !wantLanguageCode && pageLanguage && pageLanguage !== "en";

      const filtered = cards.filter((card) => {
        const m = meta.get(card);
        if (wantProduct && m.product !== wantProduct) return false;
        if (wantLanguageCode && m.languageCode !== wantLanguageCode) return false;
        return true;
      });

      filtered.sort((a, b) => {
        const ma = meta.get(a);
        const mb = meta.get(b);

        // Language prioritization: only when no explicit sort and no language filter
        if (shouldPrioritizeLanguage) {
          const aMatches = ma.languageCode && ma.languageCode.toLowerCase() === pageLanguage.toLowerCase();
          const bMatches = mb.languageCode && mb.languageCode.toLowerCase() === pageLanguage.toLowerCase();
          if (aMatches !== bMatches) {
            return aMatches ? -1 : 1; // Matching language comes first
          }
        }

        if (sortMode === "views") {
          const va = ma.viewsCount || 0;
          const vb = mb.viewsCount || 0;
          // Missing views (0) should go last
          if (va === 0 && vb !== 0) return 1;
          if (vb === 0 && va !== 0) return -1;
          if (vb !== va) return vb - va;
          // Tie-break: newest first
          return (mb.dateTime || 0) - (ma.dateTime || 0);
        }

        const da = ma.dateTime;
        const db = mb.dateTime;
        // Missing date (0) should go last in "newest", first in "oldest"
        if (da === 0 && db !== 0) return sortMode === "oldest" ? -1 : 1;
        if (db === 0 && da !== 0) return sortMode === "oldest" ? 1 : -1;
        return sortMode === "oldest" ? da - db : db - da;
      });

      // IMPORTANT: actually filter by removing non-matching cards from the DOM.
      // Sorting works by moving nodes; filtering must clear the container first.
      grid.innerHTML = "";
      const frag = document.createDocumentFragment();
      for (const el of filtered) frag.appendChild(el);
      grid.appendChild(frag);

      if (visibleEl) visibleEl.textContent = String(filtered.length);
      if (totalEl) totalEl.textContent = String(cards.length);
    }

    function applyAndSync() {
      apply();
      syncUrlFromState(sortEl, productEl, languageEl);
    }

    if (sortEl) sortEl.addEventListener("change", applyAndSync);
    if (productEl) productEl.addEventListener("change", applyAndSync);
    if (languageEl) languageEl.addEventListener("change", applyAndSync);

    apply();
  }

  document.addEventListener("DOMContentLoaded", init);
})();


