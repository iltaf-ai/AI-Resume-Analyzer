from pypdf import PdfReader


def extract_resume_text(file_path: str):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text