// Carousel state management
const carouselState = {};

// Lazy load carousel images
function loadCarouselImage(img) {
  if (img.dataset.src && !img.src) {
    img.src = img.dataset.src;
    img.classList.remove('carousel-lazy-image');
    img.removeAttribute('data-src');
  }
}

// Preload next slide image
function preloadNextSlide(carouselId, currentSlideIndex) {
  const carousel = document.getElementById(carouselId);
  if (!carousel) return;
  
  const slides = carousel.querySelectorAll('.carousel-slide');
  const nextIndex = (currentSlideIndex % slides.length);
  const nextSlide = slides[nextIndex];
  
  if (nextSlide) {
    const nextImg = nextSlide.querySelector('img[data-src]');
    if (nextImg) {
      loadCarouselImage(nextImg);
    }
  }
}

function initCarousel(carouselId) {
  const carousel = document.getElementById(carouselId);
  if (!carousel) return;

  const autoplay = carousel.getAttribute('data-autoplay') === 'true';
  const interval = parseInt(carousel.getAttribute('data-interval')) || 5000;
  
  carouselState[carouselId] = {
    currentSlide: 1,
    totalSlides: carousel.querySelectorAll('.carousel-slide').length,
    autoplayInterval: null,
    autoplay: autoplay,
    interval: interval
  };

  // Load first slide image immediately (already loaded with eager)
  // Preload second slide image
  preloadNextSlide(carouselId, 1);

  // Initialize progress bars for first slide - ensure function is available
  // Don't initialize here - let it be handled by the main initialization
  // This prevents multiple calls

  if (autoplay) {
    startAutoplay(carouselId);
  }

  // Add keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') carouselPrev(carouselId);
    if (e.key === 'ArrowRight') carouselNext(carouselId);
  });

  // Pause autoplay on hover
  carousel.addEventListener('mouseenter', () => {
    const state = carouselState[carouselId];
    if (state.autoplayInterval) {
      clearInterval(state.autoplayInterval);
      state.autoplayInterval = null;
      // Pause progress bar animations
      document.querySelectorAll('.progress-bar--active').forEach(bar => {
        const animation = bar.style.animation;
        if (animation && animation !== 'none') {
          bar.style.animationPlayState = 'paused';
        }
      });
    }
  });

  carousel.addEventListener('mouseleave', () => {
    const state = carouselState[carouselId];
    if (state.autoplay) {
      // Resume progress bar animations
      document.querySelectorAll('.progress-bar--active').forEach(bar => {
        if (bar.style.animationPlayState === 'paused') {
          bar.style.animationPlayState = 'running';
        }
      });
      startAutoplay(carouselId);
    }
  });
}

function carouselNext(carouselId) {
  const state = carouselState[carouselId];
  let nextSlide = state.currentSlide + 1;
  if (nextSlide > state.totalSlides) {
    nextSlide = 1;
  }
  carouselGoto(carouselId, nextSlide);
}

function carouselPrev(carouselId) {
  const state = carouselState[carouselId];
  let prevSlide = state.currentSlide - 1;
  if (prevSlide < 1) {
    prevSlide = state.totalSlides;
  }
  carouselGoto(carouselId, prevSlide);
}

function carouselGoto(carouselId, slideIndex) {
  const carousel = document.getElementById(carouselId);
  if (!carousel) return;

  const state = carouselState[carouselId];
  state.currentSlide = slideIndex;

  // Update slides visibility
  const slides = carousel.querySelectorAll('.carousel-slide');
  slides.forEach((slide, index) => {
    if (index + 1 === slideIndex) {
      slide.classList.add('carousel-slide--active');
      // Load image for active slide if not already loaded
      const img = slide.querySelector('img[data-src]');
      if (img) {
        loadCarouselImage(img);
      }
    } else {
      slide.classList.remove('carousel-slide--active');
    }
  });

  // Preload next slide image for smooth transition
  preloadNextSlide(carouselId, slideIndex);

  // Update progress bars if updateProgressBars function exists
  if (typeof updateProgressBars === 'function') {
    updateProgressBars(slideIndex, state.totalSlides, state.interval);
  }

  // Update dots
  const dots = carousel.querySelectorAll('.carousel-dot');
  dots.forEach((dot, index) => {
    if (index + 1 === slideIndex) {
      dot.classList.add('carousel-dot--active');
    } else {
      dot.classList.remove('carousel-dot--active');
    }
  });

  // Restart autoplay timer - clear existing first
  if (state.autoplayInterval) {
    clearInterval(state.autoplayInterval);
    state.autoplayInterval = null;
  }
  if (state.autoplay) {
    // Start autoplay after progress bar animation has started
    setTimeout(() => {
      startAutoplay(carouselId);
    }, 100);
  }
}

function startAutoplay(carouselId) {
  const state = carouselState[carouselId];
  state.autoplayInterval = setInterval(() => {
    carouselNext(carouselId);
  }, state.interval);
}

// Lazy initialize carousel when it enters viewport
function lazyInitCarousel() {
  const carouselContainer = document.querySelector('.mdx-carousel-container');
  if (!carouselContainer) return;

  // Check if Intersection Observer is supported
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Initialize carousel when it enters viewport
          initCarousel('mdx-carousel');
          observer.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: '50px' // Start loading 50px before entering viewport
    });

    observer.observe(carouselContainer);
  } else {
    // Fallback for browsers without Intersection Observer
    document.addEventListener('DOMContentLoaded', () => {
      initCarousel('mdx-carousel');
    });
  }
}

// Enhanced Carousel with Progress Bars
// Make updateProgressBars globally available
let isUpdatingProgressBars = false;

function updateProgressBars(currentSlide, totalSlides, duration) {
  // Prevent multiple simultaneous updates
  if (isUpdatingProgressBars) return;
  isUpdatingProgressBars = true;
  
  const progressBars = document.querySelectorAll('.progress-bar');
  
  progressBars.forEach((bar, index) => {
    const slideNum = index + 1;
    
    // Stop any running animations first
    if (bar.style.animation && bar.style.animation !== 'none') {
      bar.style.animation = 'none';
    }
    
    // Completely reset bar state - clear all animations and transitions
    bar.classList.remove('progress-bar--active');
    bar.style.animation = 'none';
    bar.style.animationName = '';
    bar.style.animationDuration = '';
    bar.style.animationTimingFunction = '';
    bar.style.animationFillMode = '';
    bar.style.transition = 'none';
    
    // Force reflow to ensure all styles are cleared
    void bar.offsetWidth;

    if (slideNum < currentSlide) {
      // Past slides - fully filled grey (no animation, no transition)
      bar.style.width = '100%';
      bar.style.background = '#9a9a9a';
      bar.style.animation = 'none';
    } else if (slideNum === currentSlide) {
      // Current slide - start empty then animate to full
      bar.style.width = '0%';
      bar.style.background = 'linear-gradient(90deg, #ff6b35, #ff8c42, #ffa657)';
      bar.classList.add('progress-bar--active');
      
      // Force reflow to ensure width reset is applied
      void bar.offsetWidth;
      
      // Start animation after a brief delay to ensure reset is complete
      setTimeout(() => {
        bar.style.animation = `fillProgress ${duration}ms linear forwards`;
      }, 10);
    } else {
      // Future slides - empty (no animation, no transition)
      bar.style.width = '0%';
      bar.style.background = '#9a9a9a';
      bar.style.animation = 'none';
    }
  });
  
  // Reset flag after a short delay
  setTimeout(() => {
    isUpdatingProgressBars = false;
  }, 50);
}

// Add click handlers to progress items
function initProgressBarClickHandlers() {
  const progressItems = document.querySelectorAll('.progress-item');
  progressItems.forEach((item) => {
    // Remove any existing click listeners by cloning
    const newItem = item.cloneNode(true);
    item.parentNode.replaceChild(newItem, item);
    
    // Add click handler to the new item
    newItem.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      
      const carouselId = 'mdx-carousel';
      const slideIndex = parseInt(newItem.getAttribute('data-slide'));
      const state = carouselState[carouselId];
      
      if (state && slideIndex >= 1 && slideIndex <= state.totalSlides) {
        // Stop current autoplay
        if (state.autoplayInterval) {
          clearInterval(state.autoplayInterval);
          state.autoplayInterval = null;
        }
        
        // Go to the selected slide
        carouselGoto(carouselId, slideIndex);
        
        // Restart autoplay after a brief delay
        if (state.autoplay) {
          setTimeout(() => {
            startAutoplay(carouselId);
          }, 100);
        }
      }
    });
  });
}

// Ensure progress bars are initialized after DOM and scripts are ready
// This ensures the first slide's progress bar starts animating
function ensureProgressBarsInitialized() {
  const carousel = document.getElementById('mdx-carousel');
  if (!carousel) return false;
  
  const state = carouselState['mdx-carousel'];
  if (!state) return false;
  
  const firstBar = document.querySelector('#progress-1');
  if (!firstBar) return false;
  
  // Check if progress bar is already animating
  const hasAnimation = firstBar.style.animation && 
                      firstBar.style.animation !== 'none' &&
                      firstBar.style.animation.includes('fillProgress');
  
  if (!hasAnimation) {
    // Initialize progress bars
    updateProgressBars(state.currentSlide || 1, state.totalSlides, state.interval);
    // Initialize click handlers only once
    if (typeof initProgressBarClickHandlers === 'function') {
      initProgressBarClickHandlers();
    }
    return true;
  }
  return false;
}

// Try to initialize progress bars when DOM is ready
// Use multiple attempts to ensure initialization
function tryInitializeProgressBars(attempts = 0) {
  if (attempts > 5) return; // Max 5 attempts
  
  if (typeof updateProgressBars === 'function' && typeof initProgressBarClickHandlers === 'function') {
    const initialized = ensureProgressBarsInitialized();
    if (!initialized && attempts < 3) {
      setTimeout(() => tryInitializeProgressBars(attempts + 1), 300);
    }
  } else {
    setTimeout(() => tryInitializeProgressBars(attempts + 1), 100);
  }
}

// Initialize all carousels on page load
document.addEventListener('DOMContentLoaded', () => {
  // Lazy initialize primary carousel
  lazyInitCarousel();

  // Initialize existing slideshow carousels
  if (typeof initSlideshow === 'function') {
    initSlideshow();
  }
  
  // Try to initialize progress bars
  setTimeout(() => tryInitializeProgressBars(), 200);
});

// Fallback for old slideshow code
if (typeof changeSlide === 'undefined') {
  window.changeSlide = function(carouselId, n) {
    carouselGoto(carouselId, carouselState[carouselId].currentSlide + n);
  };
}

if (typeof currentSlide === 'undefined') {
  window.currentSlide = function(carouselId, n) {
    carouselGoto(carouselId, n);
  };
}
