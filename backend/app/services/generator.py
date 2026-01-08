from pathlib import Path

class ProjectGenerationError(Exception):
    pass

def generate_project(template: dict, project_name: str, base_path: str) -> None:
    root_path = Path(base_path).resolve() / project_name

    if root_path.exists():
        raise ProjectGenerationError(f"Target directory already exists: {root_path}")

    structure = template.get("structure", {})
    folders = structure.get("folders", [])
    files = structure.get("files", {})

    root_path.mkdir(parents=True, exist_ok=False)

    for folder in folders:
        (root_path / folder).mkdir(parents=True, exist_ok=True)

    for relative_path, content in files.items():
        file_path = root_path / relative_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
