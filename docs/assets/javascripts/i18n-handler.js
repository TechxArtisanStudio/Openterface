/**
 * Openterface i18n Handler
 * 
 * Automatically handles internationalization for elements with data-i18n-key attributes.
 * Detects language from URL path and loads appropriate translations from JSON files.
 * 
 * Usage:
 * 1. Add data-i18n-file="filename" to container element (without .json extension)
 * 2. Add data-i18n-key="key" to translatable elements
 * 3. Place translation JSON in /i18n-sites/filename.json
 * 
 * The handler runs automatically on page load.
 */

(function() {
    'use strict';
    
    // Global API
    window.OpenterfaceI18n = {
        currentLanguage: 'en',
        translations: {},
        
        /**
         * Detect current language from URL path
         * @returns {string} Language code (e.g., 'en', 'zh', 'es')
         */
        detectLanguage: function() {
            const path = window.location.pathname;
            const segments = path.split('/').filter(segment => segment);
            
            // Supported language codes
            const supportedLangs = ['en', 'zh', 'ja', 'ko', 'fr', 'de', 'it', 'es', 'pt', 'ro'];
            
            // Check if first segment is a language code
            if (segments.length > 0 && supportedLangs.includes(segments[0])) {
                return segments[0];
            }
            
            // Default to English if no language code found
            return 'en';
        },
        
        /**
         * Load translations from JSON file
         * @param {string} filename - Name of JSON file (without .json extension)
         * @returns {Promise<Object>} Translation data
         */
        loadTranslations: async function(filename) {
            // Check if already loaded
            if (this.translations[filename]) {
                return this.translations[filename];
            }
            
            try {
                const response = await fetch(`/assets/i18n-sites/${filename}.json`);
                if (!response.ok) {
                    throw new Error(`Failed to load translations: ${response.statusText}`);
                }
                
                const data = await response.json();
                this.translations[filename] = data;
                return data;
            } catch (error) {
                console.warn(`i18n-handler: Could not load translations from /assets/i18n-sites/${filename}.json`, error);
                return null;
            }
        },
        
        /**
         * Update a single element with translation
         * @param {HTMLElement} element - Element to update
         * @param {Object} translationData - Translation data object
         */
        updateElement: function(element, translationData) {
            const key = element.getAttribute('data-i18n-key');
            if (!key) return;
            
            const lang = this.currentLanguage;
            const translations = translationData?.translations;
            
            if (!translations) return;
            
            const t = translations[lang] || translations['en'] || {};
            
            if (t[key]) {
                element.textContent = t[key];
            }
        },
        
        /**
         * Process all elements within a container
         * @param {HTMLElement} container - Container with data-i18n-file attribute
         */
        processContainer: async function(container) {
            const filename = container.getAttribute('data-i18n-file');
            
            if (!filename) {
                // Check for inline translations (backward compatibility)
                const inlineTranslations = container.getAttribute('data-translations');
                if (inlineTranslations) {
                    this.processInlineTranslations(container, inlineTranslations);
                }
                return;
            }
            
            // Load translations from file
            const translationData = await this.loadTranslations(filename);
            
            if (!translationData) return;
            
            // Update all elements with data-i18n-key within this container
            const elements = container.querySelectorAll('[data-i18n-key]');
            elements.forEach(element => {
                this.updateElement(element, translationData);
            });
        },
        
        /**
         * Process inline translations (backward compatibility)
         * @param {HTMLElement} container - Container with data-translations attribute
         * @param {string} translationsJson - JSON string of translations
         */
        processInlineTranslations: function(container, translationsJson) {
            let translations = {};
            
            try {
                // Unescape HTML entities
                const unescaped = translationsJson.replace(/&#39;/g, "'");
                translations = JSON.parse(unescaped);
            } catch (e) {
                console.warn('i18n-handler: Failed to parse inline translations:', e);
                return;
            }
            
            const lang = this.currentLanguage;
            const t = translations[lang] || translations['en'] || {};
            
            // Update all elements with data-i18n-key within this container
            const elements = container.querySelectorAll('[data-i18n-key]');
            elements.forEach(element => {
                const key = element.getAttribute('data-i18n-key');
                if (key && t[key]) {
                    element.textContent = t[key];
                }
            });
        },
        
        /**
         * Initialize i18n for all containers on the page
         */
        init: function() {
            // Detect current language
            this.currentLanguage = this.detectLanguage();
            
            // Find all containers with data-i18n-file or data-translations
            const containers = document.querySelectorAll('[data-i18n-file], [data-translations]');
            
            containers.forEach(container => {
                this.processContainer(container);
            });
        }
    };
    
    // Auto-initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            window.OpenterfaceI18n.init();
        });
    } else {
        // DOM already loaded
        window.OpenterfaceI18n.init();
    }
    
})();

