from pathlib import Path


class ProjectGenerationError(Exception):
    pass


def generate_project(template: dict, project_name: str, base_path: str) -> None:
    """
    Generate a project structure based on a template definition.
    """

    root_path = Path(base_path).resolve() / project_name

    # Safety check: do not overwrite existing projects
    if root_path.exists():
        raise ProjectGenerationError(
            f"Target directory already exists: {root_path}"
        )

    structure = template.get("structure", {})
    folders = structure.get("folders", [])
    files = structure.get("files", {})

    # Create root project directory
    root_path.mkdir(parents=True, exist_ok=False)

    # Create folders
    for folder in folders:
        folder_path = root_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)

    # Create files
    for relative_path, content in files.items():
        file_path = root_path / relative_path
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
