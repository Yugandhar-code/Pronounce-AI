import whisper


class SpeechService:

    def __init__(self):
        # Load the model once when the backend starts
        self.model = whisper.load_model("tiny")

    def transcribe_audio(self, audio_path):
        result = self.model.transcribe(audio_path)

        return result["text"]