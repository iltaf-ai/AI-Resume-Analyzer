import os
from app.services.resume_parser import extract_resume_text
from app.services.mistral import analyze_resume
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.model import Resume
from app.database import get_db
from app.dependencies import get_current

resume_router = APIRouter()

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


@resume_router.post("/upload")
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current)
):

    filename = file.filename

    existing_resume = db.query(Resume).filter(
        Resume.user_id == current_user.id
    ).first()

    if existing_resume:
        return {
            "message": "Resume already exists"
        }

    file_path = os.path.join(
        UPLOAD_DIR,
        filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    new_resume = Resume(
        user_id=current_user.id,
        filename=filename,
        file_path=file_path
    )
    
    db.add(new_resume)
    db.commit()

    extracted_text = extract_resume_text(file_path)

    analysis = analyze_resume(extracted_text)

    return {
        "message": "Resume analyzed successfully",
        "filename": filename,
        "user": current_user.username,
        "analysis": analysis
    }