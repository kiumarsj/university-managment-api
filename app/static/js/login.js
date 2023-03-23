const form = document.getElementById('login-form');

form.addEventListener('submit', async (event) => {
  event.preventDefault(); // prevent the form from submitting normally

  // const formData = new FormData(form);

  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  const data = JSON.stringify({"email": email, "password": password});

  const response = await fetch('http://localhost:5000/login', {
    method: "POST",
    body: data,
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  
  });

  if (response.ok) {
    const data = await response.json();
    document.cookie = "token=" + data['token'] + "; path=/";
  } else {
    console.error('Error:', response.statusText);
  }
});
