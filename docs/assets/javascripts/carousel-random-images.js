// Random image selection for carousel slides
(function() {
  function selectRandomImage() {
    const randomImageElements = document.querySelectorAll('.carousel-random-image');
    
    randomImageElements.forEach(function(img) {
      const imageOptions = JSON.parse(img.getAttribute('data-slide-images') || '[]');
      
      if (imageOptions.length > 0) {
        // Randomly select one image from the options
        const randomIndex = Math.floor(Math.random() * imageOptions.length);
        const selectedImage = imageOptions[randomIndex];
        
        // Update the image source
        if (img.hasAttribute('data-src')) {
          // For lazy-loaded images
          img.setAttribute('data-src', selectedImage);
        } else {
          // For eager-loaded images
          img.src = selectedImage;
        }
      }
    });
  }
  
  // Run immediately if DOM is ready, otherwise wait for DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', selectRandomImage);
  } else {
    selectRandomImage();
  }
})();

