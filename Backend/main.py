import os
import tempfile
import time

from services.speech_service import SpeechService
from services.analysis_service import AnalysisService

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

speech_service = SpeechService()
analysis_service = AnalysisService()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://pronounce-ai-nine.vercel.app"],
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

    total_start = time.time()

    print("=" * 60)
    print("New upload received")
    print(f"Filename: {audio.filename}")

    suffix = os.path.splitext(audio.filename)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        temp_file.write(await audio.read())
        temp_path = temp_file.name

    try:

        print("Starting Whisper transcription...")
        transcription_start = time.time()

        transcript = speech_service.transcribe_audio(temp_path)

        transcription_end = time.time()

        print(
            f"Whisper completed in "
            f"{transcription_end - transcription_start:.2f} seconds"
        )

        print("Starting analysis...")
        analysis_start = time.time()

        analysis = analysis_service.analyze(transcript)

        analysis_end = time.time()

        print(
            f"Analysis completed in "
            f"{analysis_end - analysis_start:.2f} seconds"
        )

        total_end = time.time()

        print(
            f"TOTAL REQUEST TIME: "
            f"{total_end - total_start:.2f} seconds"
        )

        print("=" * 60)

        return {
            "transcript": transcript,
            "score": analysis["score"],
            "feedback": analysis["feedback"],
            "mistakes": analysis["mistakes"]
        }

    finally:
        os.remove(temp_path)