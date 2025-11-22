// Download Version and Format Selector
document.addEventListener('DOMContentLoaded', function() {
  initializeDownloadSelectors();
});

function initializeDownloadSelectors() {
  // Get all version dropdowns
  const versionDropdowns = document.querySelectorAll('.version-dropdown');
  
  versionDropdowns.forEach(dropdown => {
    const platformDownload = dropdown.closest('.platform-download');
    
    if (!platformDownload) return;
    
    // Initialize with stable version selected
    dropdown.value = 'stable';
    updateFormatSelectorLinks(platformDownload, 'stable');
    updateMainDownloadButton(platformDownload, 'stable');
    
    // Handle dropdown change
    dropdown.addEventListener('change', function(e) {
      const selectedVersion = this.value;
      updateFormatSelectorLinks(platformDownload, selectedVersion);
      updateMainDownloadButton(platformDownload, selectedVersion);
    });
  });
  
  // Add click handlers to format options
  const formatOptions = document.querySelectorAll('.format-option');
  formatOptions.forEach(option => {
    option.addEventListener('click', function(e) {
      e.preventDefault();
      
      const platformDownload = this.closest('.platform-download');
      const dropdown = platformDownload.querySelector('.version-dropdown');
      const selectedVersion = dropdown ? dropdown.value : 'stable';
      
      const href = this.getAttribute(`data-href-${selectedVersion}`);
      if (href) {
        window.location.href = href;
      }
    });
  });
}

function updateFormatSelectorLinks(platformDownload, version) {
  const formatOptions = platformDownload.querySelectorAll('.format-option');
  
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

