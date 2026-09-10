from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

home_router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@home_router.get("/")
def home_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html"
    )