// Download Version and Format Selector
document.addEventListener('DOMContentLoaded', function() {
  initializeDownloadSelectors();
});

function initializeDownloadSelectors() {
  // Get all version selectors
  const versionSelectors = document.querySelectorAll('.version-selector');
  
  versionSelectors.forEach(selector => {
    const versionOptions = selector.querySelectorAll('.version-option');
    const platformDownload = selector.closest('.platform-download');
    
    if (!platformDownload) return;
    
    versionOptions.forEach(option => {
      option.addEventListener('click', function(e) {
        e.preventDefault();
        
        const selectedVersion = this.dataset.version;
        
        // Update version selector UI
        versionOptions.forEach(opt => opt.classList.remove('selected'));
        this.classList.add('selected');
        
        // Update format selector links based on selected version
        updateFormatSelectorLinks(platformDownload, selectedVersion);
        
        // Update main download button
        updateMainDownloadButton(platformDownload, selectedVersion);
      });
    });
  });
}

function updateFormatSelectorLinks(platformDownload, version) {
  const formatOptions = platformDownload.querySelectorAll('.format-option');
  
  formatOptions.forEach(option => {
    const hrefKey = `data-href-${version}`;
    const href = option.getAttribute(hrefKey);
    
    if (href) {
      option.dataset.href = href;
      
      // Update onclick if exists
      option.onclick = function() {
        window.location.href = this.dataset.href;
      };
    }
  });
  
  // Make sure first format option is selected
  if (formatOptions.length > 0) {
    formatOptions.forEach(opt => opt.classList.remove('selected'));
    formatOptions[0].classList.add('selected');
  }
}

function updateMainDownloadButton(platformDownload, version) {
  const mainButton = platformDownload.querySelector('.big-download-btn');
  const selectedFormat = platformDownload.querySelector('.format-option.selected');
  
  if (mainButton && selectedFormat) {
    const href = selectedFormat.getAttribute(`data-href-${version}`);
    if (href) {
      mainButton.href = href;
      mainButton.onclick = function(e) {
        e.preventDefault();
        window.location.href = href;
      };
    }
  }
}
