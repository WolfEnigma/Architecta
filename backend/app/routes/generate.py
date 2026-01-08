from fastapi import APIRouter, HTTPException
from backend.app.schemas.project import ProjectGenerateRequest
from backend.app.services.template_loader import load_template
from backend.app.services.generator import generate_project, ProjectGenerationError

router = APIRouter()

@router.post("/generate")
def generate_project_api(request: ProjectGenerateRequest):
    try:
        template = load_template(request.language, request.framework)
        generate_project(
            template=template,
            project_name=request.project_name,
            base_path=request.base_path
        )
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ProjectGenerationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal generation error")

    return {
        "message": "Project generated successfully",
        "path": f"{request.base_path}/{request.project_name}"
    }
