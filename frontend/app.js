const form = document.getElementById('generateForm');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const project_name = document.getElementById('project_name').value;
  const language = document.getElementById('language').value;
  const framework = document.getElementById('framework').value;
  const base_path = document.getElementById('base_path').value;

  try {
    const response = await fetch('http://127.0.0.1:8000/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ project_name, language, framework, base_path })
    });

    const data = await response.json();

    if (response.ok) {
      resultDiv.textContent = `✅ Success! Project created at ${data.path}`;
      resultDiv.style.color = 'green';
    } else {
      resultDiv.textContent = `❌ Error: ${data.detail}`;
      resultDiv.style.color = 'red';
    }
  } catch (err) {
    resultDiv.textContent = `❌ Network error: ${err.message}`;
    resultDiv.style.color = 'red';
  }
});
