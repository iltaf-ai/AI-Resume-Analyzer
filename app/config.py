from dotenv import load_dotenv
import os
load_dotenv()

class settings():
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    SECRET_KEY  = os.getenv("SECRET_KEY")
    ACCESS_EXPIRE_TOKEN_TIME = int(os.getenv("ACCESS_EXPIRE_TOKEN_TIME", "30"))
    DATABASE_URL = os.getenv("DATABASE_URL")
    ALGORITHM = os.getenv("ALGORITHM")

settings = settings()