document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('subscribe-form');
  const message = document.getElementById('form-message');

  form.addEventListener('submit', function(event) {
      event.preventDefault();

      // Set the source input to the current page's domain (protocol + domain + port)
      const sourceInput = form.querySelector('input[name="source"]');
      sourceInput.value = window.location.origin;

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
          message.style.display = 'block';
        message.style.color = '#df4d3f';
          message.textContent = 'Thank you for subscribing!';
          form.reset();
          setTimeout(() => { message.style.display = 'none'; }, 5000);
      })
      .catch(error => {
          message.style.display = 'block';
          message.style.color = 'red';
          message.textContent = 'Error subscribing. Please try again.';
          console.error('Error:', error);
      });
  });
});