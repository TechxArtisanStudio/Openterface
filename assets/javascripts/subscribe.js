// Function to initialize the form
function initializeForm() {
  const form = document.getElementById('subscribe-form');
  if (!form) return; // Return if form doesn't exist

  const submitButton = document.getElementById('form-submit');
  const originalButtonText = submitButton.value;

  // Enable the form and remove loading class
  form.classList.remove('js-loading');
  submitButton.disabled = false;

  // Remove existing event listener if any
  form.removeEventListener('submit', handleSubmit);

  // Add new event listener
  form.addEventListener('submit', handleSubmit);
}

// Function to initialize product-specific signup forms
function initializeProductSignupForm() {
  const form = document.getElementById('product-signup-form');
  if (!form) return; // Return if form doesn't exist

  const submitButton = document.getElementById('product-form-submit');
  const originalButtonText = submitButton.value;

  // Enable the form and remove loading class
  form.classList.remove('js-loading');
  submitButton.disabled = false;

  // Remove existing event listener if any
  form.removeEventListener('submit', handleProductSubmit);

  // Add new event listener
  form.addEventListener('submit', handleProductSubmit);
}

function handleSubmit(event) {
  event.preventDefault();

  const form = document.getElementById('subscribe-form');
  const submitButton = document.getElementById('form-submit');
  const originalButtonText = submitButton.value;

  // Get form data
  const formData = new FormData(form);
  const data = {
    email: formData.get('email'),
    name: formData.get('name') || ''
  };

  // Get translated feedback messages
  const t = {
    processing: window.OpenterfaceI18n?.getTranslation('forms', 'subscribe_processing', 'Processing... ⏳'),
    success: window.OpenterfaceI18n?.getTranslation('forms', 'subscribe_success', '✓ Successfully subscribed! 🎉'),
    failed: window.OpenterfaceI18n?.getTranslation('forms', 'subscribe_failed', '✗ Subscription failed. Try again.'),
    error: window.OpenterfaceI18n?.getTranslation('forms', 'subscribe_error', '✗ An error occurred. Try again.')
  };

  // Disable button and show loading state
  submitButton.disabled = true;
  submitButton.value = t.processing;
  submitButton.style.backgroundColor = '#FAA22B';
  submitButton.classList.add('submitting');

  // Send AJAX request
  fetch('https://subscribe.openterface.com/api/subscribe/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(result => {
    if (result.success) {
      // Success state
      submitButton.value = t.success;
      submitButton.style.backgroundColor = '#2e4e1f';
      submitButton.classList.remove('submitting');
      submitButton.classList.add('success');
      form.reset();
      
      // Re-enable after 3 seconds
      setTimeout(() => {
        submitButton.value = originalButtonText;
        submitButton.style.backgroundColor = '';
        submitButton.disabled = false;
        submitButton.classList.remove('success');
      }, 3000);
    } else {
      // Error state
      submitButton.value = t.failed;
      submitButton.style.backgroundColor = '#d32f2f';
      submitButton.classList.remove('submitting');
      submitButton.classList.add('error');
      submitButton.disabled = false;
      
      setTimeout(() => {
        submitButton.value = originalButtonText;
        submitButton.style.backgroundColor = '';
        submitButton.classList.remove('error');
      }, 3000);
    }
  })
  .catch(error => {
    console.error('Error:', error);
    // Error state
    submitButton.value = t.error;
    submitButton.style.backgroundColor = '#d32f2f';
    submitButton.classList.remove('submitting');
    submitButton.classList.add('error');
    submitButton.disabled = false;
    
    setTimeout(() => {
      submitButton.value = originalButtonText;
      submitButton.style.backgroundColor = '';
      submitButton.classList.remove('error');
    }, 3000);
  });
}

function handleProductSubmit(event) {
  event.preventDefault();

  const form = document.getElementById('product-signup-form');
  const submitButton = document.getElementById('product-form-submit');
  const originalButtonText = submitButton.value;

  // Get form data
  const formData = new FormData(form);
  const data = {
    email: formData.get('email'),
    name: formData.get('name') || ''
  };

  // Get translated feedback messages
  const t = {
    processing: window.OpenterfaceI18n?.getTranslation('forms', 'subscribe_processing', 'Processing... ⏳'),
    success: window.OpenterfaceI18n?.getTranslation('forms', 'subscribe_success', '✓ Successfully subscribed! 🎉'),
    failed: window.OpenterfaceI18n?.getTranslation('forms', 'subscribe_failed', '✗ Subscription failed. Try again.'),
    error: window.OpenterfaceI18n?.getTranslation('forms', 'subscribe_error', '✗ An error occurred. Try again.')
  };

  // Disable button and show loading state
  submitButton.disabled = true;
  submitButton.value = t.processing;
  submitButton.style.backgroundColor = '#FAA22B';
  submitButton.classList.add('submitting');

  // Send AJAX request
  fetch('https://subscribe.openterface.com/api/subscribe/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(result => {
    if (result.success) {
      // Success state
      submitButton.value = t.success;
      submitButton.style.backgroundColor = '#2e4e1f';
      submitButton.classList.remove('submitting');
      submitButton.classList.add('success');
      form.reset();
      
      // Re-enable after 3 seconds
      setTimeout(() => {
        submitButton.value = originalButtonText;
        submitButton.style.backgroundColor = '';
        submitButton.disabled = false;
        submitButton.classList.remove('success');
      }, 3000);
    } else {
      // Error state
      submitButton.value = t.failed;
      submitButton.style.backgroundColor = '#d32f2f';
      submitButton.classList.remove('submitting');
      submitButton.classList.add('error');
      submitButton.disabled = false;
      
      setTimeout(() => {
        submitButton.value = originalButtonText;
        submitButton.style.backgroundColor = '';
        submitButton.classList.remove('error');
      }, 3000);
    }
  })
  .catch(error => {
    console.error('Error:', error);
    // Error state
    submitButton.value = t.error;
    submitButton.style.backgroundColor = '#d32f2f';
    submitButton.classList.remove('submitting');
    submitButton.classList.add('error');
    submitButton.disabled = false;
    
    setTimeout(() => {
      submitButton.value = originalButtonText;
      submitButton.style.backgroundColor = '';
      submitButton.classList.remove('error');
    }, 3000);
  });
}

// Initialize forms on DOMContentLoaded
document.addEventListener('DOMContentLoaded', function() {
  initializeForm();
  initializeProductSignupForm();
});

// Initialize forms on navigation
document.addEventListener('md-navigation', function() {
  initializeForm();
  initializeProductSignupForm();
});

// Initialize forms immediately if DOM is already loaded
if (document.readyState === 'complete' || document.readyState === 'interactive') {
  initializeForm();
  initializeProductSignupForm();
}

// Listen for MkDocs navigation events
document.addEventListener('md-navigation', function() {
  // Small delay to ensure the new content is loaded
  setTimeout(function() {
    initializeForm();
    initializeProductSignupForm();
  }, 100);
});