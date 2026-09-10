from sqlalchemy import ForeignKey, String, Integer, Column, Text
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    username = Column(String(40), nullable=False)


from sqlalchemy import Column, Integer, String, Text, ForeignKey

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    filename = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    extracted_text = Column(Text, nullable=True)
    analysis = Column(Text, nullable=True)