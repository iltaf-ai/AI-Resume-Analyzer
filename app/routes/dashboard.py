from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

dashboard_router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@dashboard_router.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )


@dashboard_router.get("/resume_page")
def resume_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="upload.html"
    )


@dashboard_router.get("/analysis")
def analysis_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="result.html"
    )