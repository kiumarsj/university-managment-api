const form = document.getElementById('login-form');

form.addEventListener('submit', async (event) => {
  event.preventDefault(); // prevent the form from submitting normally

  const formData = new FormData(form);

  const data = JSON.stringify(Object.fromEntries(formData));
  console.log(formData);

  const response = await fetch('http://localhost:5000/login', {
    method: "POST",
    body: JSON.stringify(formData),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  
  });

  if (response.ok) {
    const data = await response.json();
    console.log(data); // do something with the response data
  } else {
    console.error('Error:', response.statusText);
  }
});
