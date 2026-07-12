import whisper


class SpeechService:

    def __init__(self):
        print("Loading Whisper model...")
        self.model = whisper.load_model("tiny")
        print("Whisper model loaded successfully.")

    def transcribe_audio(self, audio_path):
        try:
            print("Starting transcription...")

            result = self.model.transcribe(
                audio_path,
                language="en"
            )

            print("Transcription completed.")

            return result["text"]

        except Exception as e:
            print(f"Transcription failed: {e}")
            raise