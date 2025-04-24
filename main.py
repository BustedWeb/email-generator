from fastapi import FastAPI
from routes import test, email

app = FastAPI()

app.include_router(test.router, prefix="/api")
app.include_router(email.router, prefix="/api")