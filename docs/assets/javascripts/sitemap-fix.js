/**
 * Sitemap URL Fix for Material for MkDocs
 * 
 * Intercepts fetch/XMLHttpRequest calls to sitemap.xml files and:
 * - Normalizes URLs (fixes double slashes)
 * - Redirects language-specific sitemap requests to root /sitemap.xml
 * - Silently handles 404 errors to prevent console noise
 * 
 * This script must run early, before Material's search code loads.
 */

(function() {
  'use strict';

  // Prevent double-initialization
  if (window.__sitemapFixLoaded) return;
  window.__sitemapFixLoaded = true;

  /**
   * Normalizes sitemap URLs:
   * - Fixes double slashes: //lang/sitemap.xml -> /sitemap.xml
   * - Redirects language-specific to root: /lang/sitemap.xml -> /sitemap.xml
   * - Handles absolute URLs with language paths
   */
  function normalizeSitemapUrl(url) {
    if (typeof url !== 'string') return url;

    // First, handle the double-slash case explicitly (e.g., //ro/sitemap.xml)
    // This can happen if URL construction adds an extra slash
    let normalized = url;
    
    // Fix double slashes after protocol (https:/// -> https://)
    normalized = normalized.replace(/^(https?:\/)\/+/i, '$1');
    
    // Fix double slashes in path (//lang/ -> /lang/)
    // But preserve single slash at start of path
    normalized = normalized.replace(/([^:]\/)\/+/g, '$1');

    try {
      // Handle both absolute and relative URLs
      let urlObj;
      if (normalized.startsWith('http://') || normalized.startsWith('https://')) {
        urlObj = new URL(normalized);
      } else {
        // Relative URL - construct absolute URL
        urlObj = new URL(normalized, window.location.origin);
      }
      
      const pathname = urlObj.pathname;

      // Check if this is a sitemap.xml request
      if (!pathname || !pathname.includes('sitemap.xml')) {
        return url; // Not a sitemap request, return original
      }

      // Normalize path (remove multiple consecutive slashes)
      let normalizedPath = pathname.replace(/\/+/g, '/');

      // Check if it's a language-specific sitemap (e.g., /zh/sitemap.xml, /es/sitemap.xml)
      // Also handle double-slash cases like //ro/sitemap.xml (which becomes /ro/sitemap.xml after normalization)
      // Language codes: en, zh, ja, ko, fr, de, it, es, pt, ro
      const langPattern = /^\/(?:zh|ja|ko|fr|de|it|es|pt|ro)\/sitemap\.xml$/i;
      
      if (langPattern.test(normalizedPath)) {
        // Redirect to root sitemap
        normalizedPath = '/sitemap.xml';
      }

      // Also check for just /sitemap.xml - ensure it's normalized to root
      if (normalizedPath === '/sitemap.xml' || normalizedPath === 'sitemap.xml') {
        normalizedPath = '/sitemap.xml';
      }

      // Reconstruct URL with normalized path
      urlObj.pathname = normalizedPath;
      return urlObj.toString();
    } catch (e) {
      // If URL parsing fails, try simple string replacement
      // Fix double slashes
      normalized = normalized.replace(/\/+/g, '/');
      
      // Fix double slashes in protocol (https:/// -> https://)
      normalized = normalized.replace(/^([a-z]+:\/)\/+/i, '$1');
      
      // Redirect language-specific sitemaps (handle both /lang/ and //lang/)
      normalized = normalized.replace(/\/\/?(?:zh|ja|ko|fr|de|it|es|pt|ro)\/sitemap\.xml$/i, '/sitemap.xml');
      
      return normalized;
    }
  }

  /**
   * Check if a URL is a sitemap.xml request
   */
  function isSitemapRequest(url) {
    if (typeof url !== 'string') return false;
    return url.includes('sitemap.xml');
  }

  /**
   * Patch the global fetch() function
   */
  if (typeof window.fetch !== 'undefined') {
    const originalFetch = window.fetch;
    
    window.fetch = function(input, init) {
      // Handle both string URLs and Request objects
      let url = typeof input === 'string' ? input : input.url;
      const request = typeof input === 'string' ? null : input;

      if (isSitemapRequest(url)) {
        const normalizedUrl = normalizeSitemapUrl(url);
        
        // If URL changed, update the request
        if (normalizedUrl !== url) {
          if (request) {
            // Create new Request with normalized URL
            input = new Request(normalizedUrl, request);
          } else {
            // Use normalized URL string
            input = normalizedUrl;
          }
        }

        // Make the request - if it fails, suppress 404 errors for sitemap requests
        return originalFetch.call(this, input, init).then(function(response) {
          // If response is OK or we redirected to root sitemap, return it normally
          return response;
        }).catch(function(error) {
          // Check if this is a 404 error (which would be expected if redirect didn't work)
          // Only suppress actual network/404 errors, not other types
          if (error.name === 'TypeError' && error.message.includes('404')) {
            // Suppress console logging by returning a rejected promise with a generic message
            // The error won't propagate further, preventing console spam
            return Promise.reject(new Error('Sitemap request failed (suppressed)'));
          }
          // For other errors, let them through normally
          throw error;
        });
      }

      // Not a sitemap request, use original fetch
      return originalFetch.call(this, input, init);
    };
  }

  /**
   * Patch XMLHttpRequest
   */
  if (typeof XMLHttpRequest !== 'undefined') {
    const OriginalXHR = XMLHttpRequest;
    const originalOpen = XMLHttpRequest.prototype.open;
    const originalSend = XMLHttpRequest.prototype.send;

    XMLHttpRequest.prototype.open = function(method, url, async, user, password) {
      // Store original URL and normalize if needed
      this._originalUrl = url;
      
      if (isSitemapRequest(url)) {
        url = normalizeSitemapUrl(url);
        this._sitemapRequest = true;
      }

      // Call original open with potentially normalized URL
      return originalOpen.call(this, method, url, async !== false, user, password);
    };

    XMLHttpRequest.prototype.send = function(body) {
      const xhr = this;

      // Override onerror and onloadend to suppress console errors for sitemap 404s
      if (xhr._sitemapRequest) {
        const originalOnError = xhr.onerror;
        const originalOnLoadEnd = xhr.onloadend;

        xhr.onerror = function(e) {
          // Suppress console logging for sitemap 404s
          if (xhr.status === 404 || xhr.status === 0) {
            // Silently handle - don't log to console
            if (originalOnError) {
              try {
                originalOnError.call(xhr, e);
              } catch (err) {
                // Suppress errors in error handler
              }
            }
            return;
          }
          
          // For other errors, call original handler
          if (originalOnError) {
            originalOnError.call(xhr, e);
          }
        };

        xhr.onloadend = function(e) {
          // Suppress console logging for 404s
          if (xhr.status === 404) {
            if (originalOnLoadEnd) {
              try {
                originalOnLoadEnd.call(xhr, e);
              } catch (err) {
                // Suppress errors in loadend handler
              }
            }
            return;
          }
          
          if (originalOnLoadEnd) {
            originalOnLoadEnd.call(xhr, e);
          }
        };
      }

      return originalSend.call(this, body);
    };
  }

  // Also patch console.error to suppress sitemap-related 404 errors
  if (typeof console !== 'undefined' && console.error) {
    const originalConsoleError = console.error;
    
    console.error = function() {
      // Check if any argument mentions sitemap and 404
      const args = Array.prototype.slice.call(arguments);
      const message = args.join(' ');
      
      if (message.includes('sitemap') && (message.includes('404') || message.includes('Not Found'))) {
        // Suppress this error - it's expected
        return;
      }
      
      // Call original console.error for other messages
      return originalConsoleError.apply(console, arguments);
    };
  }

  // Log that the fix is loaded (in development, can be removed in production)
  // console.log('Sitemap URL fix loaded');
})();

