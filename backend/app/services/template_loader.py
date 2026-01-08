import json
from pathlib import Path

TEMPLATES_DIR = Path("templates")

def load_template(language: str, framework: str) -> dict:
    template_path = TEMPLATES_DIR / language / framework / "template.json"
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found for {language}/{framework}")
    with open(template_path, "r", encoding="utf-8") as f:
        return json.load(f)
