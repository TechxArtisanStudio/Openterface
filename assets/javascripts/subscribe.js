document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('subscribe-form');
    const message = document.getElementById('form-message');
  
    form.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission
  
      // Collect form data
      const formData = new FormData(form);
      const data = {};
      formData.forEach((value, key) => { data[key] = value; });
  
      // Send AJAX request
      fetch('https://script.google.com/macros/s/AKfycbwBqXSVZWT5GBsq5bPyz6xqF_RR7JZhK9PyszpvcztgZf3HbXhB4bUFALgkNq-DBpp2/exec', {
        method: 'POST',
        mode: 'no-cors', // Required for Google Apps Script
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams(data).toString(),
      })
      .then(response => {
        // Since 'no-cors' mode doesn't return response body, assume success
        message.style.display = 'block';
        message.style.color = '#df4d3f';
        message.textContent = 'Thank you for subscribing!';
        form.reset(); // Clear the form
        setTimeout(() => { message.style.display = 'none'; }, 5000); // Hide message after 5 seconds
      })
      .catch(error => {
        message.style.display = 'block';
        message.style.color = 'red';
        message.textContent = 'Error subscribing. Please try again.';
        console.error('Error:', error);
      });
    });
  });