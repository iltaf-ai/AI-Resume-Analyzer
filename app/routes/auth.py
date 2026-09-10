from fastapi import HTTPException , Depends , APIRouter
from app.dependencies import get_current , hash_password , verify_password , create_token
from app.database import get_db
from app.model import User
from app.schema import UserCreate , UserLogin
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates 
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse 

templates =  Jinja2Templates(directory="app/templates")

auth_router = APIRouter()

@auth_router.post("/register")
def register(user: UserCreate , db:Session = Depends(get_db)):
    user_existing = db.query(User).filter(User.email == user.email).first()
    if user_existing:
        return {
            "message" :"User Already Exits"
        }

    new_user = User(
        email = user.email,
        password = hash_password(user.password),
        username = user.username
    )

    db.add(new_user)
    db.commit()

@auth_router.post("/login")
def login(user:UserLogin , db:Session = Depends(get_db)):

    user_exiting = db.query(User).filter(User.email == user.email).first()
    if not user_exiting:
        return {
            "message" : "User Not found"
        }
    password_verify = verify_password(
        user.password,
        user_exiting.password
    )

    if not password_verify:
        return{
            "message" : "Password Worng"
        }

    token = create_token({
        "password" : user.username
    })

    return {
    "message": "Login successful",
    "token": token
        }



@auth_router.get("/register", response_class=HTMLResponse)
def register_page(request : Request):
    return templates.TemplateResponse(
        request=register,
        name= "register.html"
    )

@auth_router.post("/login" , response_class=HTMLResponse)
def login_page(request : Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )