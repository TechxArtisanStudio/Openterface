// Xmas Progress Bar Snowflake Tracker
// Syncs snowflake icon position with slide 4 progress bar animation
// ============================================================================

(function() {
  let animationFrameId = null;
  let isActive = false;
  let lastWidth = 0;
  let animationStartTime = null;
  const ANIMATION_DURATION = 6000; // 6 seconds, matching carousel interval
  
  function updateSnowflakePosition() {
    const progressBar = document.getElementById('progress-4');
    const snowflake = progressBar?.querySelector('.progress-icon-snowflake');
    
    if (!progressBar || !snowflake) return;
    
    // Get the actual rendered width using getBoundingClientRect
    // This is more reliable during CSS animations than offsetWidth
    const rect = progressBar.getBoundingClientRect();
    const wrapperRect = progressBar.parentElement.getBoundingClientRect();
    let progressWidth = rect.width;
    
    // Also try offsetWidth as primary source
    if (progressBar.offsetWidth > 0) {
      progressWidth = progressBar.offsetWidth;
    }
    
    // Fallback: try computed style if width is 0 but animation is running
    if (progressWidth === 0 && progressBar.classList.contains('progress-bar--active')) {
      const computedStyle = window.getComputedStyle(progressBar);
      const widthStr = computedStyle.width;
      if (widthStr && widthStr !== '0px') {
        const wrapperWidth = wrapperRect.width || progressBar.parentElement.offsetWidth;
        if (widthStr.includes('%')) {
          const percentMatch = widthStr.match(/(\d+(?:\.\d+)?)%/);
          if (percentMatch) {
            progressWidth = (parseFloat(percentMatch[1]) / 100) * wrapperWidth;
          }
        } else if (widthStr.includes('px')) {
          const pxMatch = widthStr.match(/(\d+(?:\.\d+)?)px/);
          if (pxMatch) {
            progressWidth = parseFloat(pxMatch[1]);
          }
        }
      }
    }
    
    // Always update position when active (even if width seems unchanged)
    // This ensures smooth movement during CSS animations
    if (isActive) {
      const snowflakeWidth = 16; // width of snowflake
      const position = Math.max(snowflakeWidth / 2, progressWidth - snowflakeWidth / 2);
      snowflake.style.left = position + 'px';
      lastWidth = progressWidth;
    }
  }
  
  function animateSnowflake() {
    updateSnowflakePosition();
    const progressBar = document.getElementById('progress-4');
    if (progressBar && progressBar.classList.contains('progress-bar--active')) {
      animationFrameId = requestAnimationFrame(animateSnowflake);
    } else {
      animationFrameId = null;
      isActive = false;
    }
  }
  
  function handleProgressBarChange() {
    const progressBar = document.getElementById('progress-4');
    if (!progressBar) return;
    
    const wasActive = isActive;
    isActive = progressBar.classList.contains('progress-bar--active');
    
    if (isActive && !wasActive) {
      // Just became active, start continuous animation
      lastWidth = 0; // Reset to force update
      animationStartTime = Date.now();
      if (!animationFrameId) {
        animateSnowflake();
      }
    } else if (!isActive && wasActive) {
      // Just became inactive, stop animation
      if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
      }
      // Reset snowflake position
      const snowflake = progressBar.querySelector('.progress-icon-snowflake');
      if (snowflake) {
        snowflake.style.left = '8px'; // Reset to beginning (half of snowflake width)
        lastWidth = 0;
      }
      animationStartTime = null;
    }
    
    // Always update position when state changes
    updateSnowflakePosition();
  }
  
  // Watch for progress bar changes
  function initSnowflakeTracker() {
    const progressBar = document.getElementById('progress-4');
    if (!progressBar) return;
    
    isActive = progressBar.classList.contains('progress-bar--active');
    
    // Use MutationObserver to watch for class and style changes
    const observer = new MutationObserver(function(mutations) {
      let shouldUpdate = false;
      mutations.forEach(function(mutation) {
        if (mutation.type === 'attributes') {
          if (mutation.attributeName === 'class' || mutation.attributeName === 'style') {
            shouldUpdate = true;
          }
        }
      });
      
      if (shouldUpdate) {
        handleProgressBarChange();
      }
    });
    
    observer.observe(progressBar, {
      attributes: true,
      attributeFilter: ['style', 'class'],
      childList: false,
      subtree: false
    });
    
    // Also watch for animation events
    progressBar.addEventListener('animationstart', function(e) {
      if (e.animationName === 'fillProgress') {
        handleProgressBarChange();
      }
    });
    
    // Initial update
    updateSnowflakePosition();
    
    // Start animation if already active
    if (isActive) {
      animateSnowflake();
    }
    
    // Also check periodically in case MutationObserver misses updates
    // Use a more frequent interval for smoother tracking during animations
    setInterval(function() {
      const currentActive = progressBar.classList.contains('progress-bar--active');
      if (currentActive !== isActive) {
        handleProgressBarChange();
      } else if (currentActive) {
        // Update position even if state hasn't changed (for smooth animation tracking)
        updateSnowflakePosition();
      }
    }, 16); // Check every ~16ms (roughly 60fps) for smooth animation tracking
  }
  
  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSnowflakeTracker);
  } else {
    // DOM already loaded, initialize immediately
    initSnowflakeTracker();
  }
  
  // Also try to initialize after a short delay in case elements aren't ready yet
  setTimeout(initSnowflakeTracker, 100);
})();

