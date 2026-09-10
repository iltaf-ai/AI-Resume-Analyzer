from pydantic import BaseModel

class UserCreate(BaseModel):
    email = str
    password : str
    username : str


class UserLogin(BaseModel):
    email : str
    password : str


class ResumeCreate(BaseModel):
    filename : str
    file_path : str
    extracted_text : str