from dotenv import load_dotenv
import os
load_dotenv()

class settings():
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    SECRET_KEY  = os.getenv("SECRET_KEY")
    ACCESS_EXPIRE_TOEKN_TIME = os.getenv("ACCESS_EXPIRE_TOEKN_TIME")
    DATABASE_URL = os.getenv("DATABASE_URL")

settings = settings()