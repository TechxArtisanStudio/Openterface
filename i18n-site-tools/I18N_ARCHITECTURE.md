# Openterface Website i18n Architecture

**Comprehensive Guide to Internationalization Management**

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Single Source of Truth](#single-source-of-truth)
4. [Two i18n Methods](#two-i18n-methods)
5. [When to Use Which Method](#when-to-use-which-method)
6. [File Structure](#file-structure)
7. [Adding a New Language](#adding-a-new-language)
8. [Client-Side i18n Guide](#client-side-i18n-guide)
9. [Build-Time i18n Guide](#build-time-i18n-guide)
10. [Best Practices](#best-practices)
11. [Troubleshooting](#troubleshooting)

---

## Overview

The Openterface website uses a **hybrid internationalization (i18n) system** with two complementary methods:

1. **Client-Side i18n** - Dynamic translation at runtime (for forms, UI components)
2. **Build-Time Static i18n** - Pre-generated translated HTML (for content pages)

Both methods are governed by a **single source of truth**: `docs/assets/i18n-sites/i18n.yml`

**Currently Supported Languages:** 10
- English (en) - Default
- Chinese (zh)
- Japanese (ja)
- Korean (ko)
- French (fr)
- German (de)
- Italian (it)
- Spanish (es)
- Portuguese (pt)
- Romanian (ro)

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│         i18n.yml (Single Source of Truth)               │
│         Defines: en, zh, ja, ko, fr, de, it, es, pt, ro │
└──────────────────┬──────────────────┬───────────────────┘
                   │                  │
         ┌─────────▼────────┐  ┌─────▼──────────────┐
         │  Client-Side     │  │  Build-Time        │
         │  i18n Method     │  │  Static Method     │
         └──────────────────┘  └────────────────────┘
                   │                  │
         ┌─────────▼────────┐  ┌─────▼──────────────┐
         │  forms.json      │  │  home.json         │
         │  (UI/Forms)      │  │  videos.json       │
         │                  │  │  (Content Pages)   │
         │  i18n-handler.js │  │  generate_static_  │
         │  Translates:     │  │  pages.py          │
         │  - Footer form   │  │  Generates:        │
         │  - Product form  │  │  - home.html       │
         │  - Feedback msg  │  │  - home.zh.html    │
         │                  │  │  - videos.html     │
         └──────────────────┘  └────────────────────┘
```

---

## Single Source of Truth

**File:** `docs/assets/i18n-sites/i18n.yml`

```yaml
default_language: en
languages:
- en
- zh
- ja
- ko
- fr
- de
- it
- es
- pt
- ro
```

**Purpose:**
- Defines all supported languages across the entire site
- Governs both client-side and build-time i18n methods
- Single point of control for adding/removing languages

**Validation:**
- All JSON translation files must include languages from this list
- `generate_static_pages.py` validates against this file
- Adding a language here makes it available to both methods

---

## Two i18n Methods

### Method 1: Client-Side i18n (Runtime Translation)

**Technology:** JavaScript (`i18n-handler.js`) + JSON translations

**How it Works:**
1. Detects language from URL path (e.g., `/zh/`, `/ja/`)
2. Loads JSON translations from `/assets/i18n-sites/{filename}.json`
3. Updates elements with `data-i18n-key` attributes at runtime
4. Zero build step required

**Used For:**
- Footer subscription form
- Product signup forms
- Dynamic feedback messages
- UI components and labels

**Pros:**
- ✅ Fast and flexible
- ✅ Works with Jinja2 partials
- ✅ No build step needed
- ✅ Instant updates
- ✅ Perfect for forms/UI

**Cons:**
- ❌ Not indexed by search engines (but acceptable for forms)
- ❌ Requires JavaScript
- ❌ Small runtime overhead

### Method 2: Build-Time Static i18n (Pre-Generation)

**Technology:** Python script (`generate_static_pages.py`) + JSON translations

**How it Works:**
1. Reads template with `data-i18n-key` attributes
2. Reads JSON translations for all languages
3. Generates separate HTML file for each language
4. Static files are served directly (no JS needed)

**Used For:**
- Home page (landing page)
- Videos page
- Marketing/content pages
- Any SEO-critical content

**Pros:**
- ✅ Perfect SEO - fully indexed
- ✅ Zero runtime overhead
- ✅ No JavaScript required
- ✅ Fast page loads
- ✅ Search engine friendly

**Cons:**
- ❌ Requires build step
- ❌ Not suitable for partials
- ❌ Updates require regeneration

---

## When to Use Which Method

### Use Client-Side i18n When:

✅ **Content is in reusable partials/components**
- Example: Footer, header, sidebar components

✅ **Content is form fields, buttons, UI labels**
- Example: Subscription forms, contact forms

✅ **Content is dynamic feedback messages**
- Example: "Processing...", "Success!", error messages

✅ **SEO indexing is not important**
- Forms and UI elements don't need to be indexed

✅ **You need runtime flexibility**
- Dynamic content, user interactions

### Use Build-Time Static i18n When:

✅ **Content is marketing/landing pages**
- Example: Home page, product pages

✅ **SEO is critical for the content**
- Content that needs to rank in search engines

✅ **Content is relatively static**
- Not frequently changing

✅ **You want zero JavaScript overhead**
- Maximum performance

✅ **Full page templates (not partials)**
- Complete standalone pages

### Don't Mix Methods:

❌ **Don't use both on the same element** unless necessary  
❌ **Don't use client-side for SEO-critical content**  
❌ **Don't use build-time for partials** (won't work)

---

## File Structure

```
docs/
├── assets/
│   ├── i18n-sites/                    # i18n Configuration & Translations
│   │   ├── i18n.yml                   # ⭐ Single Source of Truth
│   │   ├── forms.json                 # Client-side: Forms translations
│   │   ├── home.json                  # Build-time: Home page translations
│   │   └── videos.json                # Build-time: Videos page translations
│   │
│   └── javascripts/
│       ├── i18n-handler.js            # Client-side translation engine
│       └── subscribe.js               # Uses i18n API for feedback
│
├── overrides/
│   ├── main.html                      # Loads i18n-handler.js globally
│   ├── home.html                      # Generated (English)
│   ├── home.zh.html                   # Generated (Chinese)
│   ├── home.ja.html                   # Generated (Japanese)
│   └── partials/
│       └── footer.html                # Uses data-i18n-key attributes
│
└── partials/
    └── product-signup.html            # Uses data-i18n-key attributes

i18n-site-tools/
├── generate_static_pages.py           # Build-time generator
├── i18n_config.py                     # Shared configuration
└── templates/
    ├── home-base.html                 # Template with data-i18n-key
    └── videos-base.html               # Template with data-i18n-key
```

---

## Adding a New Language

**Example: Adding Dutch (nl)**

### Step 1: Update i18n.yml (Single Source of Truth)

```bash
# Edit: docs/assets/i18n-sites/i18n.yml
vim docs/assets/i18n-sites/i18n.yml
```

```yaml
default_language: en
languages:
- en
- zh
- ja
- ko
- fr
- de
- it
- es
- pt
- ro
- nl  # ← Add new language
```

### Step 2: Add Translations to JSON Files

**For Client-Side i18n:** Add to `forms.json`

```bash
vim docs/assets/i18n-sites/forms.json
```

```json
{
  "supported_languages": ["en", "zh", "ja", "ko", "fr", "de", "it", "es", "pt", "ro", "nl"],
  "translations": {
    "nl": {
      "footer_name_placeholder": "Uw Naam",
      "footer_email_placeholder": "Uw E-mailadres *",
      "footer_submit_button": "✉️ Abonneer op het Laatste Nieuws! 🐝",
      "footer_footnote": "Niet meer dan één e-mail per maand...",
      "product_description": "Schrijf u in voor updates...",
      "product_name_placeholder": "Uw Naam",
      "product_email_placeholder": "Uw E-mailadres *",
      "product_submit_button": "✉️ Abonneren! 🐝",
      "subscribe_processing": "Verwerken... ⏳",
      "subscribe_success": "✓ Succesvol geabonneerd! 🎉",
      "subscribe_error": "✗ Er is een fout opgetreden. Probeer opnieuw.",
      "subscribe_failed": "✗ Abonnement mislukt. Probeer opnieuw."
    }
  }
}
```

**For Build-Time i18n:** Add to `home.json` and `videos.json`

```bash
vim docs/assets/i18n-sites/home.json
vim docs/assets/i18n-sites/videos.json
```

### Step 3: Regenerate Static Pages (Build-Time Only)

```bash
python i18n-site-tools/generate_static_pages.py --all
```

This generates:
- `docs/overrides/home.nl.html`
- `docs/partials/videos.nl.html`

### Step 4: Test

**Client-Side:** Visit `/nl/` - forms automatically translate  
**Build-Time:** Visit `/nl/` - static pages are pre-translated

---

## Client-Side i18n Guide

### How to Use

1. **Add container with data-i18n-file**

```html
<div data-i18n-file="forms">
  <!-- Translatable content here -->
</div>
```

2. **Add data-i18n-key to elements**

```html
<!-- Text content -->
<p data-i18n-key="product_description">
  Sign up to receive updates...
</p>

<!-- Attribute (placeholder) -->
<input type="text" 
       data-i18n-key="footer_name_placeholder"
       data-i18n-attr="placeholder"
       placeholder="Your Name">

<!-- Attribute (value) -->
<input type="submit" 
       data-i18n-key="footer_submit_button"
       data-i18n-attr="value"
       value="✉️ Subscribe! 🐝">

<!-- HTML content (use cautiously) -->
<p data-i18n-key="footer_footnote"
   data-i18n-html="true">
  No more than one email... <a href="mailto:...">contact</a>
</p>
```

### API Usage in JavaScript

```javascript
// Get translation programmatically
const translation = window.OpenterfaceI18n.getTranslation(
  'forms',              // filename (without .json)
  'subscribe_success',  // translation key
  'Success!'            // fallback text
);

// Check current language
const currentLang = window.OpenterfaceI18n.currentLanguage; // 'en', 'zh', etc.

// Manually process a container
window.OpenterfaceI18n.processContainer(containerElement);
```

### Attributes Reference

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `data-i18n-file="forms"` | Specifies JSON file | Container element |
| `data-i18n-key="key"` | Translation key | Any translatable element |
| `data-i18n-attr="placeholder"` | Translate attribute | Input fields |
| `data-i18n-html="true"` | Allow HTML content | Rich text paragraphs |

---

## Build-Time i18n Guide

### Creating a New Static Page

**Example: Creating a "about" page**

#### Step 1: Create Template

```bash
vim i18n-site-tools/templates/about-base.html
```

```html
{% extends "main.html" %}

{% block content %}
<div class="about-page">
  <h1 data-i18n-key="about_title">About Openterface</h1>
  <p data-i18n-key="about_intro">
    We create innovative KVM solutions...
  </p>
</div>
{% endblock %}
```

#### Step 2: Create Translation JSON

```bash
vim docs/assets/i18n-sites/about.json
```

```json
{
  "supported_languages": ["en", "zh", "ja", "ko", "fr", "de", "it", "es", "pt", "ro"],
  "translations": {
    "en": {
      "about_title": "About Openterface",
      "about_intro": "We create innovative KVM solutions..."
    },
    "zh": {
      "about_title": "关于 Openterface",
      "about_intro": "我们创造创新的 KVM 解决方案..."
    }
    // ... other languages
  }
}
```

#### Step 3: Generate Static Files

```bash
# Generate all languages
python i18n-site-tools/generate_static_pages.py --template about

# Generate specific language
python i18n-site-tools/generate_static_pages.py --template about --language zh
```

Output:
```
docs/overrides/about.html       (English)
docs/overrides/about.zh.html    (Chinese)
docs/overrides/about.ja.html    (Japanese)
...
```

### Regenerating All Pages

```bash
python i18n-site-tools/generate_static_pages.py --all
```

---

## Best Practices

### General

1. ✅ **Always update i18n.yml first** when adding languages
2. ✅ **Keep translation keys semantic** (`footer_email_placeholder` not `field_3`)
3. ✅ **Provide fallback text** in HTML/JavaScript (English)
4. ✅ **Test all languages** after making changes
5. ✅ **Commit generated files** to Git (they're the source of truth for production)

### Client-Side i18n

1. ✅ **Use for forms, UI, dynamic content**
2. ✅ **Always provide data-i18n-attr** for input fields
3. ✅ **Use data-i18n-html="true" sparingly** (security risk)
4. ✅ **Test with JavaScript disabled** (ensure fallback works)
5. ✅ **Keep JSON files organized** by feature (forms, modals, etc.)

### Build-Time i18n

1. ✅ **Use for SEO-critical content** (home, product pages)
2. ✅ **Regenerate after translation updates**
3. ✅ **Keep templates DRY** (one template → all languages)
4. ✅ **Validate generated HTML** before deploying
5. ✅ **Integrate into CI/CD** pipeline

### Translation Quality

1. ✅ **Use professional translators** for critical content
2. ✅ **Maintain translation consistency** across all JSON files
3. ✅ **Include context** in translation keys (e.g., `footer_email_placeholder` vs `email`)
4. ✅ **Test RTL languages** if supported (Arabic, Hebrew)
5. ✅ **Verify HTML entities** in translations (don't break HTML)

---

## Troubleshooting

### Client-Side i18n Issues

**Problem:** Translations not loading

```bash
# Check browser console
# Expected: "i18n-handler: Initialized with language 'zh'"
# If not appearing, check:
1. Is i18n-handler.js loaded? (Check Network tab)
2. Is forms.json accessible? (Check /assets/i18n-sites/forms.json)
3. Are data-i18n-file and data-i18n-key attributes correct?
```

**Problem:** Wrong language detected

```javascript
// Debug current language
console.log('Current language:', window.OpenterfaceI18n.currentLanguage);
console.log('URL pathname:', window.location.pathname);

// Language is detected from first URL segment
// /zh/product/ → 'zh'
// /product/ → 'en' (default)
```

**Problem:** Attributes not translating

```html
<!-- ❌ Wrong (missing data-i18n-attr) -->
<input data-i18n-key="name" placeholder="Name">

<!-- ✅ Correct -->
<input data-i18n-key="name" 
       data-i18n-attr="placeholder" 
       placeholder="Name">
```

### Build-Time i18n Issues

**Problem:** Template not found

```bash
# Error: Template not found: home-base.html
# Solution: Check template file exists
ls i18n-site-tools/templates/home-base.html
```

**Problem:** Translation JSON errors

```bash
# Validate JSON
python -m json.tool docs/assets/i18n-sites/forms.json

# Common issues:
# - Trailing comma
# - Unescaped quotes
# - Missing closing brace
```

**Problem:** Generated files have wrong content

```bash
# Regenerate with verbose output
python i18n-site-tools/generate_static_pages.py --template home

# Check:
1. Are translation keys correct in template?
2. Are translations present in JSON for that language?
3. Did you commit the generated files?
```

### Performance Issues

**Problem:** Slow page load (client-side)

```javascript
// Preload translations in <head>
<link rel="prefetch" href="/assets/i18n-sites/forms.json">
```

**Problem:** Large JSON files

```bash
# Split by feature
forms.json         → Form-related translations only
modals.json        → Modal dialogs
notifications.json → System messages
```

---

## Additional Resources

- **i18n-handler.js API:** See `docs/assets/javascripts/i18n-handler.js`
- **Static Generator:** See `i18n-site-tools/README.md`
- **Language Config:** See `docs/assets/i18n-sites/i18n.yml`
- **Adding Languages:** See `i18n-tools/ADD_NEW_LANGUAGE_GUIDE.md`

---

## Summary

**Hybrid i18n Architecture:**
- 🎯 **Single source of truth** → `i18n.yml`
- 🌐 **10 languages supported** → en, zh, ja, ko, fr, de, it, es, pt, ro
- ⚡ **Client-side** → Forms, UI (runtime translation)
- 🔍 **Build-time** → Content pages (SEO-friendly static)
- 📦 **Centralized management** → All translations in JSON files
- 🚀 **Production-ready** → Battle-tested, scalable

**Questions?** Contact the development team or check the documentation links above.

---

*Last Updated: December 2024*  
*Version: 1.0*

