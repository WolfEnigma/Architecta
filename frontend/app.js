const form = document.getElementById('generateForm');
const resultDiv = document.getElementById('result');

const languageSelect = document.getElementById("language");
const frameworkSelect = document.getElementById("framework");

// Available languages and frameworks
const LANGUAGES = {
  python: ["flask", "fastapi", "cli"],
  javascript: ["nodejs", "express"],
  bash: ["automation"]
};

// Populate languages
for (let lang in LANGUAGES) {
  let option = document.createElement("option");
  option.value = lang;
  option.textContent = lang.charAt(0).toUpperCase() + lang.slice(1);
  languageSelect.appendChild(option);
}

// Populate frameworks based on selected language
function populateFrameworks(selectedLang) {
  frameworkSelect.innerHTML = "";
  LANGUAGES[selectedLang].forEach((fw) => {
    let option = document.createElement("option");
    option.value = fw;
    option.textContent = fw.charAt(0).toUpperCase() + fw.slice(1);
    frameworkSelect.appendChild(option);
  });
}

populateFrameworks(languageSelect.value);

languageSelect.addEventListener("change", () => {
  populateFrameworks(languageSelect.value);
});

// Form submission
form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const project_name = document.getElementById('project_name').value;
  const language = languageSelect.value;
  const framework = frameworkSelect.value;
  const base_path = document.getElementById('base_path').value;

  try {
    const response = await fetch('http://127.0.0.1:8000/generate', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
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
