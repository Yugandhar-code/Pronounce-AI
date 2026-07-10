from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "AI Pronunciation Analyzer Backend is running!"
    }


@app.post("/upload")
async def upload_audio(audio: UploadFile = File(...)):
    return {
        "filename": audio.filename,
        "content_type": audio.content_type,
        "message": "File received successfully!"
    }