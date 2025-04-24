from fastapi import APIRouter
from fastapi.responses import FileResponse
from utils.email_generator import gen_emails

router = APIRouter()

@router.get("/generate-emails")
def generate_emails(count: int = 10):
    file_path = gen_emails(count)
    return FileResponse(file_path, media_type="text/plain", filename="emails.txt")
