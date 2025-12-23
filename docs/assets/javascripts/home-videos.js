/**
 * Home Videos Carousel
 * Handles pause on hover and positions cards to overlap footer
 */

(function() {
  document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.getElementById('home-videos-carousel');
    if (!carousel) return;
    
    // Pause animation on hover
    carousel.addEventListener('mouseenter', function() {
      carousel.style.animationPlayState = 'paused';
    });
    
    carousel.addEventListener('mouseleave', function() {
      carousel.style.animationPlayState = 'running';
    });
    
    // Position cards and thumbnails dynamically to allow overlap with footer
    // Only on desktop screens (not mobile)
    function isMobileScreen() {
      return window.innerWidth <= 768;
    }
    
    // Clean up any existing clones (in case of resize or initial load on mobile)
    function cleanupClones() {
      const existingClones = document.querySelectorAll('.home-video-thumbnail-clone, .home-video-card[style*="position: fixed"]');
      existingClones.forEach(function(clone) {
        if (clone.parentNode) {
          clone.parentNode.removeChild(clone);
        }
      });
    }
    
    // Clean up on initial load if mobile
    if (isMobileScreen()) {
      cleanupClones();
    }
    
    const videoItems = carousel.querySelectorAll('.home-video-item');
    videoItems.forEach(function(item) {
      const card = item.querySelector('.home-video-card');
      const thumbnail = item.querySelector('.home-video-thumbnail');
      const thumbnailImg = thumbnail ? thumbnail.querySelector('img') : null;
      if (!card || !thumbnail || !thumbnailImg) return;
      
      let cardClone = null;
      let thumbnailClone = null;
      
      // Skip cloning on mobile - use CSS positioning instead
      if (isMobileScreen()) {
        // Ensure original elements are visible and not modified
        thumbnail.style.opacity = '';
        thumbnail.style.pointerEvents = '';
        thumbnail.style.transform = '';
        thumbnail.style.boxShadow = '';
        card.style.visibility = '';
        card.style.opacity = '';
        card.style.transform = '';
        return;
      }
      
      item.addEventListener('mouseenter', function() {
        // Double check - skip on mobile
        if (isMobileScreen()) {
          cleanupClones();
          return;
        }
        const rect = item.getBoundingClientRect();
        const thumbnailRect = thumbnail.getBoundingClientRect();
        
        // Create a clone of the thumbnail and append to body for true overlap
        thumbnailClone = thumbnail.cloneNode(true);
        
        // Get computed styles from original
        const computedStyle = window.getComputedStyle(thumbnail);
        
        // Apply all necessary styles to clone
        // Note: position fixed is relative to viewport, not document
        thumbnailClone.style.position = 'fixed';
        thumbnailClone.style.top = thumbnailRect.top + 'px';
        thumbnailClone.style.left = thumbnailRect.left + 'px';
        thumbnailClone.style.width = thumbnailRect.width + 'px';
        thumbnailClone.style.height = thumbnailRect.height + 'px';
        thumbnailClone.style.zIndex = '99998';
        thumbnailClone.style.transform = 'scale(1.15)';
        thumbnailClone.style.transformOrigin = 'center center';
        thumbnailClone.style.boxShadow = '0 8px 24px rgba(0, 0, 0, 0.2)';
        thumbnailClone.style.pointerEvents = 'none';
        thumbnailClone.style.opacity = '1';
        thumbnailClone.style.transition = 'none';
        thumbnailClone.style.margin = '0';
        thumbnailClone.style.padding = '0';
        thumbnailClone.style.borderRadius = computedStyle.borderRadius || '8px';
        thumbnailClone.style.overflow = 'hidden';
        thumbnailClone.style.backgroundColor = computedStyle.backgroundColor || 'transparent';
        thumbnailClone.style.display = 'block';
        thumbnailClone.style.visibility = 'visible';
        thumbnailClone.className = 'home-video-thumbnail home-video-thumbnail-clone';
        
        // Ensure the cloned image has the same dimensions and styles
        const clonedImg = thumbnailClone.querySelector('img');
        if (clonedImg) {
          // Ensure image source is set
          if (!clonedImg.src || clonedImg.src === window.location.href) {
            clonedImg.src = thumbnailImg.src || thumbnailImg.getAttribute('src') || '';
          }
          clonedImg.style.width = '100%';
          clonedImg.style.height = '100%';
          clonedImg.style.objectFit = 'cover';
          clonedImg.style.display = 'block';
          clonedImg.style.opacity = '1';
          clonedImg.style.visibility = 'visible';
          clonedImg.style.margin = '0';
          clonedImg.style.padding = '0';
        }
        
        // Append clone to body
        document.body.appendChild(thumbnailClone);
        
        // Wait for clone to be rendered and image to be ready
        const checkClone = function() {
          if (thumbnailClone && thumbnailClone.parentNode) {
            const cloneRect = thumbnailClone.getBoundingClientRect();
            const cloneImg = thumbnailClone.querySelector('img');
            // Check if clone is visible and has dimensions
            if (cloneRect.width > 0 && cloneRect.height > 0) {
              // Hide original only if clone is successfully rendered
              thumbnail.style.opacity = '0';
              thumbnail.style.pointerEvents = 'none';
            } else {
              // If clone isn't rendering, keep original visible
              console.warn('Thumbnail clone not rendering properly, keeping original visible');
            }
          }
        };
        
        // Check immediately and after a short delay
        requestAnimationFrame(checkClone);
        setTimeout(checkClone, 50);
        
        // Create a clone of the card and append to body for true overlap
        cardClone = card.cloneNode(true);
        cardClone.style.position = 'fixed';
        // Note: position fixed is relative to viewport, not document
        cardClone.style.top = (rect.bottom + 8) + 'px';
        cardClone.style.left = rect.left + 'px';
        cardClone.style.zIndex = '99999';
        cardClone.style.width = card.offsetWidth + 'px';
        cardClone.style.opacity = '1';
        cardClone.style.visibility = 'visible';
        cardClone.style.transform = 'translateY(0)';
        cardClone.style.maxHeight = '300px';
        cardClone.style.pointerEvents = 'none';
        document.body.appendChild(cardClone);
        
        // Hide original card
        card.style.visibility = 'hidden';
      });
      
      item.addEventListener('mouseleave', function() {
        // Skip on mobile
        if (isMobileScreen()) {
          return;
        }
        // Immediately restore original thumbnail visibility BEFORE removing clone
        // This ensures smooth transition back to normal size
        if (thumbnail) {
          thumbnail.style.opacity = '1';
          thumbnail.style.pointerEvents = '';
          thumbnail.style.zIndex = '10000';
          thumbnail.style.position = 'relative';
        }
        
        // Remove cloned thumbnail immediately (original is now visible)
        if (thumbnailClone && thumbnailClone.parentNode) {
          thumbnailClone.parentNode.removeChild(thumbnailClone);
          thumbnailClone = null;
        }
        
        // Immediately restore original card visibility BEFORE removing clone
        // This ensures smooth transition back to hidden state
        card.style.visibility = 'visible';
        card.style.opacity = '1';
        card.style.transform = 'translateY(0)';
        card.style.maxHeight = '300px';
        card.style.zIndex = '9999';
        
        // Remove cloned card immediately (original is now visible)
        if (cardClone && cardClone.parentNode) {
          cardClone.parentNode.removeChild(cardClone);
          cardClone = null;
        }
        
        // Now let CSS handle the transition back to hidden state
        // Use requestAnimationFrame to ensure the visible state is rendered first
        requestAnimationFrame(function() {
          // Reset to let CSS transitions handle the fade out
          card.style.visibility = '';
          card.style.opacity = '';
          card.style.transform = '';
          card.style.maxHeight = '';
          card.style.zIndex = '';
          
          // Reset thumbnail z-index after transition completes
          setTimeout(function() {
            if (thumbnail) {
              thumbnail.style.zIndex = '';
              thumbnail.style.position = '';
            }
          }, 300);
        });
      });
      
      // Update position on scroll/resize
      let updatePosition = function() {
        // Skip on mobile
        if (isMobileScreen()) {
          // Clean up any clones if we switched to mobile
          if (thumbnailClone && thumbnailClone.parentNode) {
            thumbnailClone.parentNode.removeChild(thumbnailClone);
            thumbnailClone = null;
          }
          if (cardClone && cardClone.parentNode) {
            cardClone.parentNode.removeChild(cardClone);
            cardClone = null;
          }
          if (thumbnail) {
            thumbnail.style.opacity = '';
            thumbnail.style.pointerEvents = '';
          }
          if (card) {
            card.style.visibility = '';
            card.style.opacity = '';
            card.style.transform = '';
          }
          return;
        }
        
        if (item.matches(':hover')) {
          const rect = item.getBoundingClientRect();
          const thumbnailRect = thumbnail.getBoundingClientRect();
          
          if (thumbnailClone) {
            thumbnailClone.style.top = thumbnailRect.top + 'px';
            thumbnailClone.style.left = thumbnailRect.left + 'px';
          }
          
          if (cardClone) {
            cardClone.style.top = (rect.bottom + 8) + 'px';
            cardClone.style.left = rect.left + 'px';
          }
        }
      };
      
      window.addEventListener('scroll', updatePosition, true);
      window.addEventListener('resize', function() {
        updatePosition();
        // Also cleanup on resize to mobile
        if (isMobileScreen()) {
          cleanupClones();
        }
      });
    });
  });
})();

