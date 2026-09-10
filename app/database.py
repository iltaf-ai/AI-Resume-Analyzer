from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker , DeclarativeBase

from app.config import settings
DATABASE_URL = settings.DATABASE_URL

enigne = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
     connect_args={
        "ssl_verify_cert": True,
        "ssl_verify_identity": True,
        "ssl_ca": "ca.pem"
    }
)

SessionLocal = sessionmaker(
    bind=enigne,
    autoflush=False,
    atuo_commit = False
)

Base = DeclarativeBase()

def get_db():
    try: 
        db = SessionLocal()
        yield db
    finally :
        db.close()