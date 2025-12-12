const carouselState = {};

// ============================================================================
// Image Loading System
// ============================================================================

function loadCarouselImage(img) {
  if (!img || !img.dataset.src) return;
  
  const currentSrc = img.getAttribute('src') || '';
  const isEmptyOrInvalid = !currentSrc || 
                           currentSrc === window.location.href || 
                           currentSrc === window.location.origin + '/' ||
                           img.classList.contains('carousel-lazy-image');
  
  if (isEmptyOrInvalid) {
    // Create new image to preload
    const preloadImg = new Image();
    preloadImg.onload = function() {
      img.src = this.src;
      img.classList.remove('carousel-lazy-image');
      img.removeAttribute('data-src');
    };
    preloadImg.onerror = function() {
      console.error('Failed to load carousel image:', img.dataset.src);
    };
    preloadImg.src = img.dataset.src;
  }
}

function preloadSlideImages(carouselId, slideIndex) {
  const carousel = document.getElementById(carouselId);
  if (!carousel) return;
  
  const slide = carousel.querySelector(`.carousel-slide[data-slide-index="${slideIndex}"]`);
  if (slide) {
    const img = slide.querySelector('img[data-src]');
    if (img) {
      loadCarouselImage(img);
    }
  }
}

// ============================================================================
// Carousel Core Functions
// ============================================================================

function initCarousel(carouselId) {
  const carousel = document.getElementById(carouselId);
  if (!carousel) return;
  
  // Prevent double initialization
  if (carouselState[carouselId] && carouselState[carouselId].initialized) {
    return;
  }

  const autoplay = carousel.getAttribute('data-autoplay') === 'true';
  const interval = parseInt(carousel.getAttribute('data-interval')) || 6000;
  const slides = carousel.querySelectorAll('.carousel-slide');
  
  carouselState[carouselId] = {
    currentSlide: 0, // Start at 0 to ensure goToSlide(1) actually runs
    totalSlides: slides.length,
    autoplayInterval: null,
    autoplay: autoplay,
    interval: interval,
    isTransitioning: false,
    initialized: true
  };

  // Preload all images immediately for smooth transitions
  slides.forEach((slide, index) => {
    const img = slide.querySelector('img[data-src]');
    if (img) {
      loadCarouselImage(img);
    }
  });

  // Setup event listeners
  setupCarouselEvents(carouselId);
  
  // Initialize first slide (currentSlide starts at 0, so this will run)
  goToSlide(carouselId, 1, false);
  
  // Ensure progress bars are initialized after DOM is ready
  // Use requestAnimationFrame to ensure DOM updates are complete
  requestAnimationFrame(() => {
    setTimeout(() => {
      if (typeof updateProgressBars === 'function' && typeof initProgressBarClickHandlers === 'function') {
        const state = carouselState[carouselId];
        if (state) {
          // Double-check progress bars are initialized
          const firstBar = document.querySelector('#progress-1');
          if (firstBar) {
            // Check if animation is running or if width is still 0% (not started)
            const hasAnimation = firstBar.style.animation && 
                                firstBar.style.animation !== 'none' &&
                                firstBar.style.animation.includes('fillProgress');
            const widthIsZero = firstBar.style.width === '0%' || !firstBar.style.width;
            
            // If no animation and width is still 0%, reinitialize
            if (!hasAnimation && widthIsZero) {
              updateProgressBars(state.currentSlide, state.totalSlides, state.interval);
            }
          }
          initProgressBarClickHandlers();
        }
      }
    }, 100);
  });
  
  // Start autoplay if enabled
  if (autoplay) {
    startAutoplay(carouselId);
  }
}

function setupCarouselEvents(carouselId) {
  const carousel = document.getElementById(carouselId);
  if (!carousel) return;
  
  const state = carouselState[carouselId];
  
  // Keyboard navigation (only add once)
  if (!state.keyboardListener) {
    const keyboardHandler = (e) => {
      if (state.isTransitioning) return;
      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        carouselPrev(carouselId);
      }
      if (e.key === 'ArrowRight') {
        e.preventDefault();
        carouselNext(carouselId);
      }
    };
    document.addEventListener('keydown', keyboardHandler);
    state.keyboardListener = keyboardHandler;
  }

  // Only pause on hover over interactive elements (buttons, progress bars)
  // Not on the entire carousel to allow progress bar to continue when hovering over images
  const interactiveElements = carousel.querySelectorAll('.carousel-actions, .carousel-progress-container');
  const buttons = carousel.querySelectorAll('.carousel-actions .md-button');
  
  // Add listeners to containers
  interactiveElements.forEach(element => {
    element.addEventListener('mouseenter', () => {
      pauseAutoplay(carouselId);
    });
    
    element.addEventListener('mouseleave', () => {
      if (state.autoplay) {
        resumeAutoplay(carouselId);
      }
    });
  });
  
  // Also add listeners directly to buttons for more reliable detection
  buttons.forEach(button => {
    button.addEventListener('mouseenter', () => {
      pauseAutoplay(carouselId);
    });
    
    button.addEventListener('mouseleave', () => {
      if (state.autoplay) {
        resumeAutoplay(carouselId);
      }
    });
  });
}

function goToSlide(carouselId, slideIndex, animate = true) {
  const carousel = document.getElementById(carouselId);
  if (!carousel) return;
  
  const state = carouselState[carouselId];
  if (!state) return;
  
  // Prevent rapid successive calls
  if (state.isTransitioning) return;
  if (state.currentSlide === slideIndex) return;
  
  // Validate slide index
  if (slideIndex < 1 || slideIndex > state.totalSlides) return;
  
  state.isTransitioning = true;
  const previousSlide = state.currentSlide;
  state.currentSlide = slideIndex;
  
  const slides = carousel.querySelectorAll('.carousel-slide');
  const currentSlideEl = carousel.querySelector(`.carousel-slide[data-slide-index="${slideIndex}"]`);
  const previousSlideEl = carousel.querySelector(`.carousel-slide[data-slide-index="${previousSlide}"]`);
  
  if (!currentSlideEl) {
    state.isTransitioning = false;
    return;
  }
  
  // Ensure image is loaded before transition
  const img = currentSlideEl.querySelector('img');
  if (img && img.dataset.src) {
    loadCarouselImage(img);
  }
  
  // Use requestAnimationFrame for smooth transition
  requestAnimationFrame(() => {
    // Remove active class from all slides
    slides.forEach(slide => {
      slide.classList.remove('carousel-slide--active');
    });
    
    // Add active class to current slide
    currentSlideEl.classList.add('carousel-slide--active');
    
    // Preload next slide for smooth transition
    const nextSlideIndex = slideIndex % state.totalSlides + 1;
    preloadSlideImages(carouselId, nextSlideIndex);
    
    // Update progress bars
    if (typeof updateProgressBars === 'function') {
      updateProgressBars(slideIndex, state.totalSlides, state.interval);
    }
    
    // Mark transition as complete after animation duration
    setTimeout(() => {
      state.isTransitioning = false;
    }, animate ? 600 : 0); // Match CSS transition duration
  });
}

function carouselNext(carouselId) {
  const state = carouselState[carouselId];
  if (!state || state.isTransitioning) return;
  
  const nextSlide = state.currentSlide >= state.totalSlides ? 1 : state.currentSlide + 1;
  goToSlide(carouselId, nextSlide);
}

function carouselPrev(carouselId) {
  const state = carouselState[carouselId];
  if (!state || state.isTransitioning) return;
  
  const prevSlide = state.currentSlide <= 1 ? state.totalSlides : state.currentSlide - 1;
  goToSlide(carouselId, prevSlide);
}

// ============================================================================
// Autoplay Management
// ============================================================================

function startAutoplay(carouselId) {
  const state = carouselState[carouselId];
  if (!state || !state.autoplay) return;
  
  // Clear any existing interval
  if (state.autoplayInterval) {
    clearInterval(state.autoplayInterval);
  }
  
  state.autoplayInterval = setInterval(() => {
    if (!state.isTransitioning) {
      carouselNext(carouselId);
    }
  }, state.interval);
}

function pauseAutoplay(carouselId) {
  const state = carouselState[carouselId];
  if (!state) return;
  
  if (state.autoplayInterval) {
    clearInterval(state.autoplayInterval);
    state.autoplayInterval = null;
  }
  
  // Pause progress bar animations
  document.querySelectorAll('.progress-bar--active').forEach(bar => {
    if (bar.style.animation && bar.style.animation !== 'none') {
      bar.style.animationPlayState = 'paused';
    }
  });
}

function resumeAutoplay(carouselId) {
  const state = carouselState[carouselId];
  if (!state || !state.autoplay) return;
  
  // Resume progress bar animations
  document.querySelectorAll('.progress-bar--active').forEach(bar => {
    if (bar.style.animationPlayState === 'paused') {
      bar.style.animationPlayState = 'running';
    }
  });
  
  startAutoplay(carouselId);
}

// ============================================================================
// Progress Bars System
// ============================================================================

let isUpdatingProgressBars = false;

function updateProgressBars(currentSlide, totalSlides, duration) {
  if (isUpdatingProgressBars) return;
  isUpdatingProgressBars = true;
  
  const progressBars = document.querySelectorAll('.progress-bar');
  
  requestAnimationFrame(() => {
    progressBars.forEach((bar, index) => {
      const slideNum = index + 1;
      
      // Reset animation state
      bar.classList.remove('progress-bar--active');
      bar.style.animation = 'none';
      bar.style.transition = 'none';
      
      // Force reflow
      void bar.offsetWidth;
      
      if (slideNum < currentSlide) {
        // Past slides - fully filled
        bar.style.width = '100%';
        bar.style.background = '#9a9a9a';
      } else if (slideNum === currentSlide) {
        // Current slide - animate from empty to full
        bar.style.width = '0%';
        bar.style.background = 'linear-gradient(90deg, #ff6b35, #ff8c42, #ffa657)';
        bar.classList.add('progress-bar--active');
        
        // Force reflow before starting animation
        void bar.offsetWidth;
        
        // Use double requestAnimationFrame to ensure animation starts
        requestAnimationFrame(() => {
          requestAnimationFrame(() => {
            bar.style.animation = `fillProgress ${duration}ms linear forwards`;
          });
        });
      } else {
        // Future slides - empty
        bar.style.width = '0%';
        bar.style.background = '#9a9a9a';
      }
    });
    
    setTimeout(() => {
      isUpdatingProgressBars = false;
    }, 50);
  });
}

function initProgressBarClickHandlers() {
  const progressItems = document.querySelectorAll('.progress-item');
  
  progressItems.forEach((item) => {
    // Remove existing listeners by cloning
    const newItem = item.cloneNode(true);
    item.parentNode.replaceChild(newItem, item);
    
    newItem.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      
      const carouselId = 'mdx-carousel';
      const slideIndex = parseInt(newItem.getAttribute('data-slide'));
      const state = carouselState[carouselId];
      
      if (state && slideIndex >= 1 && slideIndex <= state.totalSlides && !state.isTransitioning) {
        pauseAutoplay(carouselId);
        goToSlide(carouselId, slideIndex);
        
        if (state.autoplay) {
          setTimeout(() => {
            resumeAutoplay(carouselId);
          }, 700); // Wait for transition + buffer
        }
      }
    });
  });
}

// ============================================================================
// Initialization
// ============================================================================

function lazyInitCarousel() {
  const carouselContainer = document.querySelector('.mdx-carousel-container');
  if (!carouselContainer) return;
  
  // Check if already initialized
  if (carouselState['mdx-carousel'] && carouselState['mdx-carousel'].initialized) {
    return;
  }
  
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          initCarousel('mdx-carousel');
          observer.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: '100px'
    });
    
    observer.observe(carouselContainer);
  } else {
    // Fallback: initialize immediately
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => {
        initCarousel('mdx-carousel');
      });
    } else {
      initCarousel('mdx-carousel');
    }
  }
}

function initializeProgressBars() {
  const carousel = document.getElementById('mdx-carousel');
  if (!carousel) return false;
  
  const state = carouselState['mdx-carousel'];
  if (!state) return false;
  
  const firstBar = document.querySelector('#progress-1');
  if (!firstBar) return false;
  
  // Check if already initialized
  const hasAnimation = firstBar.style.animation && 
                      firstBar.style.animation !== 'none' &&
                      firstBar.style.animation.includes('fillProgress');
  
  if (!hasAnimation) {
    updateProgressBars(state.currentSlide || 1, state.totalSlides, state.interval);
    initProgressBarClickHandlers();
    return true;
  }
  return false;
}

// ============================================================================
// Countdown Timer
// ============================================================================

function initCountdown() {
  const countdownElement = document.getElementById('kvm-go-countdown');
  if (!countdownElement) return;
  
  const targetDate = new Date('2025-12-30T23:59:59').getTime();
  
  function updateCountdown() {
    const now = new Date().getTime();
    const distance = targetDate - now;
    
    if (distance < 0) {
      countdownElement.style.display = 'none';
      return;
    }
    
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    
    if (days > 0) {
      countdownElement.style.display = '';
      countdownElement.textContent = `${days} day${days !== 1 ? 's' : ''} left until Dec 30, 2025`;
    } else {
      // Hide countdown when days reach 0
      countdownElement.style.display = 'none';
    }
  }
  
  // Update immediately
  updateCountdown();
  
  // Update every minute
  setInterval(updateCountdown, 60000);
}

// ============================================================================
// DOM Ready Initialization
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {
  // Initialize carousel
  lazyInitCarousel();
  
  // Initialize slideshow carousels if available
  if (typeof initSlideshow === 'function') {
    initSlideshow();
  }
  
  // Initialize countdown
  initCountdown();
  
  // Initialize progress bars with retry logic
  let attempts = 0;
  const maxAttempts = 5;
  
  const tryInitProgressBars = () => {
    if (attempts >= maxAttempts) return;
    
    if (typeof updateProgressBars === 'function' && typeof initProgressBarClickHandlers === 'function') {
      const initialized = initializeProgressBars();
      if (!initialized && attempts < 3) {
        attempts++;
        setTimeout(tryInitProgressBars, 300);
      }
    } else {
      attempts++;
      setTimeout(tryInitProgressBars, 100);
    }
  };
  
  setTimeout(tryInitProgressBars, 200);
});

// ============================================================================
// Fallback Functions for Compatibility
// ============================================================================

if (typeof changeSlide === 'undefined') {
  window.changeSlide = function(carouselId, n) {
    const state = carouselState[carouselId];
    if (state) {
      const newSlide = state.currentSlide + n;
      goToSlide(carouselId, newSlide);
    }
  };
}

if (typeof currentSlide === 'undefined') {
  window.currentSlide = function(carouselId, n) {
    goToSlide(carouselId, n);
  };
}

// Export for potential external use
window.carouselGoto = goToSlide;
window.carouselNext = carouselNext;
window.carouselPrev = carouselPrev;
