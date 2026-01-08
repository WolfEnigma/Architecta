from pydantic import BaseModel

class ProjectGenerateRequest(BaseModel):
    project_name: str
    language: str
    framework: str
    base_path: str
