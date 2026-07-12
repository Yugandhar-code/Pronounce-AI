from faster_whisper import WhisperModel


class SpeechService:

    def __init__(self):
        print("Loading Whisper model...")

        self.model = WhisperModel(
            "tiny",
            device="cpu",
            compute_type="int8",
            cpu_threads=8,
            num_workers=4
        )

        print("Whisper model loaded successfully.")

    def transcribe_audio(self, audio_path):
        try:
            print("Starting transcription...")

            segments, info = self.model.transcribe(
                audio_path,
                language="en",
                beam_size=1,
                vad_filter=True
            )

            transcript = ""

            for segment in segments:
                transcript += segment.text + " "

            print("Transcription completed.")

            return transcript.strip()

        except Exception as e:
            print(f"Transcription failed: {e}")
            raise