import os
import tempfile
from services.speech_service import SpeechService
from services.analysis_service import AnalysisService

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



speech_service = SpeechService()
analysis_service = AnalysisService()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://pronounce-ai-nine.vercel.app/"],
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

    suffix = os.path.splitext(audio.filename)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        temp_file.write(await audio.read())
        temp_path = temp_file.name

    try:
        transcript = speech_service.transcribe_audio(temp_path)
        analysis = analysis_service.analyze(transcript)

        return {
            "transcript": transcript,
            "score": analysis["score"],
            "feedback": analysis["feedback"],
            "mistakes": analysis["mistakes"]
        }

    finally:
        os.remove(temp_path)