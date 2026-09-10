from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import Base, engine

from app.routes.auth import auth_router
from app.routes.dashboard import dashboard_router
from app.routes.home import home_router
from app.routes.resume import resume_router


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)


app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(home_router)
app.include_router(resume_router)