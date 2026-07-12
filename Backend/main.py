import os
import tempfile

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from services.speech_service import SpeechService
from services.analysis_service import AnalysisService

app = FastAPI()

speech_service = SpeechService()
analysis_service = AnalysisService()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://pronounce-ai-nine.vercel.app"
    ],
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
        print(f"Received file: {audio.filename}")

        transcript = speech_service.transcribe_audio(temp_path)

        analysis = analysis_service.analyze(transcript)

        print("Analysis completed successfully.")

        return {
            "transcript": transcript,
            "score": analysis["score"],
            "feedback": analysis["feedback"],
            "mistakes": analysis["mistakes"]
        }

    except Exception as e:
        print(f"Backend Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)