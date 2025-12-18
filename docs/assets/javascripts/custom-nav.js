// Custom Navigation Dropdown JavaScript
(function() {
  'use strict';

  // Preserve query string + hash when switching languages via Material language selector.
  // Use event delegation (capture phase) so it works even if the dropdown links are created
  // dynamically or only exist after opening the selector.
  function shouldHandleLanguageLink(anchor) {
    if (!anchor) return false;
    // Material language selector commonly uses data-md-type="language" and/or md-select.
    return !!(
      anchor.closest('[data-md-component="language"]') ||
      anchor.closest('[data-md-type="language"]') ||
      anchor.closest('.md-select')
    );
  }

  function isModifiedOrNonLeftClick(e, anchor) {
    if (!e) return true;
    if (e.defaultPrevented) return true;
    if (typeof e.button === 'number' && e.button !== 0) return true;
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return true;
    if (anchor && anchor.target && anchor.target !== '_self') return true;
    return false;
  }

  document.addEventListener(
    'click',
    function(e) {
      const anchor = e && e.target ? e.target.closest('a') : null;
      if (!anchor) return;
      if (!shouldHandleLanguageLink(anchor)) return;
      if (isModifiedOrNonLeftClick(e, anchor)) return;

      const keepSearch = window.location.search || '';
      const keepHash = window.location.hash || '';
      if (!keepSearch && !keepHash) return;

      try {
        const dest = new URL(anchor.href, window.location.origin);
        dest.search = keepSearch;
        dest.hash = keepHash;
        e.preventDefault();
        window.location.assign(dest.toString());
      } catch (_err) {
        // If anything is unexpected, fall back to default navigation.
      }
    },
    true
  );

  // Wait for DOM to be ready
  document.addEventListener('DOMContentLoaded', function() {
    initializeCustomNavigation();
  });

  function initializeCustomNavigation() {
    // Add click handlers for dropdown items
    const dropdownItems = document.querySelectorAll('.custom-nav-dropdown');
    
    dropdownItems.forEach(function(dropdown) {
      const navItem = dropdown.querySelector('.nav-item');
      const dropdownContent = dropdown.querySelector('.dropdown-content');
      
      if (navItem && dropdownContent) {
        // Handle click on main nav item
        navItem.addEventListener('click', function(e) {
          // If it's a link, let it navigate normally
          if (navItem.tagName === 'A') {
            return;
          }
          
          // Otherwise, toggle dropdown
          e.preventDefault();
          toggleDropdown(dropdown);
        });

        // Handle hover for better UX
        dropdown.addEventListener('mouseenter', function() {
          showDropdown(dropdown);
        });

        dropdown.addEventListener('mouseleave', function() {
          hideDropdown(dropdown);
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', function(e) {
          if (!dropdown.contains(e.target)) {
            hideDropdown(dropdown);
          }
        });
      }
    });

    // Optional: after language navigation completes, the new page will load anyway.
    // Keep this hook for any future SPA-like behavior / debugging.
    const languageSelectors = document.querySelectorAll('[data-md-component="language"] a, [data-md-type="language"] a');
    languageSelectors.forEach(function(selector) {
      selector.addEventListener('click', function() {
        setTimeout(function() {
          refreshNavigationTranslations();
        }, 100);
      });
    });
  }

  function toggleDropdown(dropdown) {
    const dropdownContent = dropdown.querySelector('.dropdown-content');
    if (dropdownContent) {
      if (dropdownContent.style.opacity === '1') {
        hideDropdown(dropdown);
      } else {
        showDropdown(dropdown);
      }
    }
  }

  function showDropdown(dropdown) {
    const dropdownContent = dropdown.querySelector('.dropdown-content');
    if (dropdownContent) {
      dropdownContent.style.opacity = '1';
      dropdownContent.style.visibility = 'visible';
      dropdownContent.style.transform = 'translateY(0)';
    }
  }

  function hideDropdown(dropdown) {
    const dropdownContent = dropdown.querySelector('.dropdown-content');
    if (dropdownContent) {
      dropdownContent.style.opacity = '0';
      dropdownContent.style.visibility = 'hidden';
      dropdownContent.style.transform = 'translateY(-10px)';
    }
  }

  function refreshNavigationTranslations() {
    // The i18n plugin should handle translations automatically
    // This function can be used for any additional refresh logic if needed
    console.log('Navigation translations refreshed');
  }

  // Handle responsive behavior
  function handleResponsiveNavigation() {
    const customNav = document.querySelector('.custom-nav-container');
    const originalTabs = document.querySelector('.md-tabs');
    
    if (window.innerWidth <= 1220) { // 76.25em = 1220px
      if (customNav) {
        customNav.style.display = 'none';
      }
      if (originalTabs) {
        originalTabs.style.display = 'block';
      }
    } else {
      if (customNav) {
        customNav.style.display = 'flex';
      }
      if (originalTabs) {
        originalTabs.style.display = 'none';
      }
    }
  }

  // Listen for window resize
  window.addEventListener('resize', handleResponsiveNavigation);
  
  // Initial call
  handleResponsiveNavigation();

})();
