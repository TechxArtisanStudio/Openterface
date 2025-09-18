// Reusable Slideshow JavaScript
class Slideshow {
  constructor(containerId, options = {}) {
    this.container = document.getElementById(containerId);
    if (!this.container) {
      console.error('Slideshow container not found:', containerId);
      return;
    }
    this.slideIndex = 1;
    this.slides = this.container.getElementsByClassName("slide");
    this.dots = this.container.getElementsByClassName("dot");
    this.currentSlideElement = null;
    
    // Auto-sliding configuration
    this.autoSlide = options.autoSlide || false;
    this.autoSlideInterval = options.autoSlideInterval || 3000; // Default 3 seconds
    this.autoSlideTimer = null;
    this.isPaused = false;
    
    // Lazy loading configuration
    this.loadedImages = new Set();
    this.loadingImages = new Set();
    this.preloadNext = true;
    this.waitForImageLoad = true;
    
    console.log('Slideshow initialized with', this.slides.length, 'slides and', this.dots.length, 'dots');
    console.log('Auto-slide:', this.autoSlide, 'Interval:', this.autoSlideInterval + 'ms');
    console.log('Preload next:', this.preloadNext, 'Wait for load:', this.waitForImageLoad);
    this.init();
  }

  init() {
    // Initialize the first slide as active
    if (this.slides.length > 0) {
      this.currentSlideElement = this.slides[0];
      this.currentSlideElement.classList.add("active");
    }
    this.addTouchSupport();
    this.addHoverSupport();
    this.addMobileOptimizations();
    this.initializeImageLoading();
    if (this.autoSlide) {
      this.startAutoSlide();
    }
  }

  showSlides(n) {
    if (n > this.slides.length) { this.slideIndex = 1; }
    if (n < 1) { this.slideIndex = this.slides.length; }
    
    // If we're already showing the same slide, don't do anything
    if (this.currentSlideElement === this.slides[this.slideIndex - 1]) {
      return;
    }
    
    // Remove active class from all dots
    for (let i = 0; i < this.dots.length; i++) {
      this.dots[i].classList.remove("active");
    }
    
    // Activate corresponding dot immediately
    this.dots[this.slideIndex - 1].classList.add("active");
    
    // Handle fade transition
    this.fadeToSlide(this.slideIndex - 1);
    
    // Preload next image if enabled
    if (this.preloadNext) {
      this.preloadNextImage();
    }
  }

  fadeToSlide(targetIndex) {
    const targetSlide = this.slides[targetIndex];
    const currentSlide = this.currentSlideElement;
    
    // If no current slide (initial load), just show the target
    if (!currentSlide) {
      this.currentSlideElement = targetSlide;
      targetSlide.classList.add("active");
      return;
    }
    
    // If same slide, do nothing
    if (currentSlide === targetSlide) {
      return;
    }
    
    // Start fade out of current slide
    currentSlide.classList.remove("active");
    
    // Wait for fade out to complete, then show new slide
    setTimeout(() => {
      this.currentSlideElement = targetSlide;
      targetSlide.classList.add("active");
    }, 300); // Match the CSS transition duration
  }

  initializeImageLoading() {
    // Load the first image immediately
    this.loadImage(0);
    
    // Preload the second image
    if (this.slides.length > 1) {
      this.preloadImage(1);
    }
  }

  loadImage(slideIndex) {
    if (slideIndex < 0 || slideIndex >= this.slides.length) return;
    
    const slide = this.slides[slideIndex];
    const img = slide.querySelector('img');
    if (!img) return;
    
    const imageSrc = img.src || img.dataset.src;
    if (!imageSrc) return;
    
    // If already loaded, mark as loaded
    if (img.complete && img.naturalHeight !== 0) {
      this.loadedImages.add(slideIndex);
      return;
    }
    
    // If already loading, don't start again
    if (this.loadingImages.has(slideIndex)) return;
    
    this.loadingImages.add(slideIndex);
    
    // Create a new image to preload
    const preloadImg = new Image();
    preloadImg.onload = () => {
      this.loadedImages.add(slideIndex);
      this.loadingImages.delete(slideIndex);
      console.log(`Image ${slideIndex + 1} loaded successfully`);
    };
    preloadImg.onerror = () => {
      this.loadingImages.delete(slideIndex);
      console.warn(`Failed to load image ${slideIndex + 1}`);
    };
    preloadImg.src = imageSrc;
  }

  preloadImage(slideIndex) {
    if (slideIndex < 0 || slideIndex >= this.slides.length) return;
    if (this.loadedImages.has(slideIndex) || this.loadingImages.has(slideIndex)) return;
    
    this.loadImage(slideIndex);
  }

  preloadNextImage() {
    const nextIndex = this.slideIndex < this.slides.length ? this.slideIndex : 0;
    this.preloadImage(nextIndex);
  }

  isImageLoaded(slideIndex) {
    return this.loadedImages.has(slideIndex);
  }

  isImageLoading(slideIndex) {
    return this.loadingImages.has(slideIndex);
  }

  changeSlide(n) {
    this.showSlides(this.slideIndex += n);
    this.resetAutoSlide();
  }

  currentSlide(n) {
    this.showSlides(this.slideIndex = n);
    this.resetAutoSlide();
  }

  startAutoSlide() {
    if (this.autoSlide && !this.isPaused) {
      this.autoSlideTimer = setInterval(() => {
        this.autoSlideToNext();
      }, this.autoSlideInterval);
    }
  }

  autoSlideToNext() {
    const nextIndex = this.slideIndex < this.slides.length ? this.slideIndex : 0;
    
    // If we should wait for image load and next image is not loaded yet
    if (this.waitForImageLoad && !this.isImageLoaded(nextIndex)) {
      console.log(`Waiting for image ${nextIndex + 1} to load before auto-sliding`);
      
      // If image is loading, wait for it
      if (this.isImageLoading(nextIndex)) {
        return; // Skip this cycle, will try again next interval
      }
      
      // If image failed to load or not started, start loading it
      this.preloadImage(nextIndex);
      return; // Skip this cycle, will try again next interval
    }
    
    // Image is loaded or we don't wait for loading, proceed with slide
    this.changeSlide(1);
  }

  stopAutoSlide() {
    if (this.autoSlideTimer) {
      clearInterval(this.autoSlideTimer);
      this.autoSlideTimer = null;
    }
  }

  resetAutoSlide() {
    this.stopAutoSlide();
    if (this.autoSlide && !this.isPaused) {
      this.startAutoSlide();
    }
  }

  pauseAutoSlide() {
    this.isPaused = true;
    this.stopAutoSlide();
  }

  resumeAutoSlide() {
    this.isPaused = false;
    if (this.autoSlide) {
      this.startAutoSlide();
    }
  }

  toggleAutoSlide() {
    if (this.isPaused) {
      this.resumeAutoSlide();
    } else {
      this.pauseAutoSlide();
    }
  }

  addTouchSupport() {
    let startX = 0;
    let endX = 0;

    this.container.addEventListener('touchstart', (e) => {
      startX = e.touches[0].clientX;
    });

    this.container.addEventListener('touchend', (e) => {
      endX = e.changedTouches[0].clientX;
      this.handleSwipe(startX, endX);
    });
  }

  addHoverSupport() {
    if (this.autoSlide) {
      this.container.addEventListener('mouseenter', () => {
        this.pauseAutoSlide();
      });

      this.container.addEventListener('mouseleave', () => {
        this.resumeAutoSlide();
      });
    }
  }

  addMobileOptimizations() {
    // Detect mobile device
    const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) || 
                     window.innerWidth <= 768;
    
    if (isMobile) {
      // On mobile, be more aggressive with preloading
      this.preloadNext = true;
      
      // Preload more images on mobile for better experience
      this.preloadMultipleImages();
      
      // Add touch event optimizations
      this.optimizeTouchEvents();
    }
  }

  preloadMultipleImages() {
    // Preload current + next 2 images on mobile
    const currentIndex = this.slideIndex - 1;
    const totalSlides = this.slides.length;
    
    for (let i = 0; i < 3; i++) {
      const index = (currentIndex + i) % totalSlides;
      this.preloadImage(index);
    }
  }

  optimizeTouchEvents() {
    // Prevent default touch behaviors that might interfere
    this.container.addEventListener('touchstart', (e) => {
      e.preventDefault();
    }, { passive: false });
    
    // Add momentum scrolling prevention
    this.container.style.touchAction = 'pan-x';
  }

  handleSwipe(startX, endX) {
    const threshold = 50; // Minimum distance for a swipe
    const diff = startX - endX;
    
    if (Math.abs(diff) > threshold) {
      if (diff > 0) {
        // Swipe left - next slide
        this.changeSlide(1);
      } else {
        // Swipe right - previous slide
        this.changeSlide(-1);
      }
    }
  }
}

// Global functions for HTML onclick handlers
function changeSlide(slideshowId, n) {
  const slideshow = window.slideshows[slideshowId];
  if (slideshow) {
    slideshow.changeSlide(n);
  }
}

function currentSlide(slideshowId, n) {
  const slideshow = window.slideshows[slideshowId];
  if (slideshow) {
    slideshow.currentSlide(n);
  }
}

// Initialize all slideshows on page load
document.addEventListener('DOMContentLoaded', function() {
  console.log('Slideshow script loaded');
  window.slideshows = {};
  const slideshowContainers = document.querySelectorAll('.slideshow-container');
  console.log('Found slideshow containers:', slideshowContainers.length);
  
  slideshowContainers.forEach((container, index) => {
    const slideshowId = container.id || `slideshow-${index}`;
    container.id = slideshowId;
    
    // Check for data attributes to configure auto-sliding
    const autoSlide = container.dataset.autoSlide === 'true';
    const autoSlideInterval = parseInt(container.dataset.autoSlideInterval) || 3000;
    
    const options = {
      autoSlide: autoSlide,
      autoSlideInterval: autoSlideInterval
    };
    
    console.log('Initializing slideshow:', slideshowId, 'with options:', options);
    window.slideshows[slideshowId] = new Slideshow(slideshowId, options);
  });
});
