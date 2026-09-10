from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
from app.config import settings
from app.database import get_db

from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt

from app.model import User


SECRET_KEY = settings.SECRET_KEY
ACCESS_EXPIRE_TOKEN_TIME = settings.ACCESS_EXPIRE_TOKEN_TIME
ALGORITHM = settings.ALGORITHM


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


auth_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_EXPIRE_TOKEN_TIME
    )

    to_encode.update({
        "exp": expire
    })

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def get_username(
    token: str = Depends(auth_scheme)
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("username")

        if not username:
            raise HTTPException(
                status_code=401,
                detail="Username was not found"
            )

        return username

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


def get_current(
    username: str = Depends(get_username),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.username == username
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user