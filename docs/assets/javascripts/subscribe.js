document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('subscribe-form');
  const submitButton = document.getElementById('form-submit');
  const originalButtonText = submitButton.value;

  form.addEventListener('submit', function(event) {
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
          submitButton.style.backgroundColor = '#df4d3f';
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
  });
});