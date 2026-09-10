import os

from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.services.resume_parser import extract_resume_text
from app.services.mistral import analyze_resume

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


    extracted_text = extract_resume_text(file_path)

    analysis = analyze_resume(extracted_text)


    new_resume = Resume(
        user_id=current_user.id,
        filename=filename,
        file_path=file_path,
        extracted_text=extracted_text,
        analysis=analysis
    )


    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)


    return {
        "message": "Resume analyzed successfully",
        "filename": filename
    }


@resume_router.get("/analysis/data")
def get_analysis_data(
    db: Session = Depends(get_db),
    current_user = Depends(get_current)
):

    resume = db.query(Resume).filter(
        Resume.user_id == current_user.id
    ).first()


    if not resume:
        return {
            "message": "No resume found"
        }


    return {
        "filename": resume.filename,
        "analysis": resume.analysis
    }

    