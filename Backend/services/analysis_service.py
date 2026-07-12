import re


class AnalysisService:

    def analyze(self, transcript: str):

        # --------------------------
        # Empty / invalid transcript
        # --------------------------
        if not transcript or transcript.strip() == "":
            return {
                "score": 0,
                "feedback": "No speech detected. Please upload a clear English recording.",
                "mistakes": [],
                "transcript": ""
            }

        words = re.findall(r"\b[\w']+\b", transcript)
        word_count = len(words)

        # Whisper sometimes returns only a few random words
        if word_count < 5:
            return {
                "score": 20,
                "feedback": "Very little speech was detected. Please speak clearly for 30–45 seconds.",
                "mistakes": [],
                "transcript": transcript
            }

        # --------------------------
        # Initial score
        # --------------------------
        score = 95

        # Penalize short transcript
        if word_count < 60:
            score -= 15
        elif word_count < 80:
            score -= 8

        # Penalize repeated consecutive words
        repeated = 0

        for i in range(1, len(words)):
            if words[i].lower() == words[i - 1].lower():
                repeated += 1

        score -= repeated * 3

        # Penalize hesitation words
        hesitation_words = [
            "um",
            "uh",
            "erm",
            "hmm",
            "ah"
        ]

        hesitations = sum(
            1
            for word in words
            if word.lower() in hesitation_words
        )

        score -= hesitations * 2

        # Clamp score
        score = max(0, min(score, 98))

        # --------------------------
        # Feedback
        # --------------------------
        if score >= 90:
            feedback = "Excellent pronunciation with clear and fluent speech."

        elif score >= 80:
            feedback = "Good pronunciation. A little more clarity would improve fluency."

        elif score >= 70:
            feedback = "Fair pronunciation. Focus on speaking more clearly and confidently."

        else:
            feedback = "Pronunciation needs improvement. Slow down and articulate words more clearly."

        # --------------------------
        # Difficult words
        # --------------------------
        difficult_words = []

        for word in words:
            if len(word) > 8 and word not in difficult_words:
                difficult_words.append(word)

        difficult_words = difficult_words[:5]

        mistakes = [
            {
                "word": word,
                "reason": "Practice pronouncing this longer word more clearly."
            }
            for word in difficult_words
        ]

        return {
            "score": score,
            "feedback": feedback,
            "mistakes": mistakes,
            "transcript": transcript
        }