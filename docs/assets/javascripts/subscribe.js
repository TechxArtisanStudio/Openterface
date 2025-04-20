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

  function handleSubmit(event) {
    event.preventDefault();

    // Show loading message on button
    submitButton.value = 'Processing... ⏳';
    submitButton.style.backgroundColor = '#FAA22B';

    // Create a hidden input for source if it doesn't exist
    let sourceInput = form.querySelector('input[name="source"]');
    if (!sourceInput) {
      sourceInput = document.createElement('input');
      sourceInput.type = 'hidden';
      sourceInput.name = 'source';
      form.appendChild(sourceInput);
    }

    // Set the source input to the clean URL (protocol + domain + path, without query parameters or hash)
    const url = new URL(window.location.href);
    sourceInput.value = url.origin + url.pathname;

    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => { data[key] = value; });

    fetch('https://script.google.com/macros/s/AKfycbwBqXSVZWT5GBsq5bPyz6xqF_RR7JZhK9PyszpvcztgZf3HbXhB4bUFALgkNq-DBpp2/exec', {
      method: 'POST',
      mode: 'no-cors',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams(data).toString(),
    })
    .then(response => {
      submitButton.value = 'Thank you for subscribing! 🎉';
      submitButton.style.backgroundColor = '#2e4e1f';
      form.reset();
      setTimeout(() => {
        submitButton.value = originalButtonText;
        submitButton.style.backgroundColor = '';
      }, 5000);
    })
    .catch(error => {
      submitButton.value = 'Error subscribing. Please try again.';
      submitButton.style.backgroundColor = 'red';
      console.error('Error:', error);
      setTimeout(() => {
        submitButton.value = originalButtonText;
        submitButton.style.backgroundColor = '';
      }, 5000);
    });
  }
}

// Initialize form on DOMContentLoaded
document.addEventListener('DOMContentLoaded', initializeForm);

// Initialize form on navigation
document.addEventListener('md-navigation', initializeForm);

// Initialize form immediately if DOM is already loaded
if (document.readyState === 'complete' || document.readyState === 'interactive') {
  initializeForm();
}

// Listen for MkDocs navigation events
document.addEventListener('md-navigation', function() {
  // Small delay to ensure the new content is loaded
  setTimeout(initializeForm, 100);
});