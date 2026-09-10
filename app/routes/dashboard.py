from fastapi.requests import Request  
from fastapi.responses import Response , HTMLResponse
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="app/templates")


dashboard_router = APIRouter()
@dashboard_router.get("/dashboard")
def dashboard(request = Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard_page"
    )


@dashboard_router("/resume_page")
def resume(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="resume.html"
    )
