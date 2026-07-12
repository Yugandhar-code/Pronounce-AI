import re


class AnalysisService:

    HESITATION_WORDS = {"um", "uh", "erm", "hmm", "ah"}

    def analyze(self, transcript: str):

        print("Starting transcript analysis...")

        if not transcript or transcript.strip() == "":
            return {
                "score": 0,
                "feedback": "No speech detected. Please upload a clear English recording.",
                "mistakes": [],
                "transcript": ""
            }

        words = re.findall(r"\b[\w']+\b", transcript)
        word_count = len(words)

        if word_count < 5:
            return {
                "score": 20,
                "feedback": "Very little speech was detected. Please speak clearly for 30–45 seconds.",
                "mistakes": [],
                "transcript": transcript
            }

        score = 95

        if word_count < 60:
            score -= 15
        elif word_count < 80:
            score -= 8

        repeated = 0

        for i in range(1, len(words)):
            if words[i].lower() == words[i - 1].lower():
                repeated += 1

        score -= repeated * 3

        hesitations = sum(
            1
            for word in words
            if word.lower() in self.HESITATION_WORDS
        )

        score -= hesitations * 2

        score = max(0, min(score, 98))

        if score >= 90:
            feedback = "Excellent pronunciation with clear and fluent speech."
        elif score >= 80:
            feedback = "Good pronunciation. A little more clarity would improve fluency."
        elif score >= 70:
            feedback = "Fair pronunciation. Focus on speaking more clearly and confidently."
        else:
            feedback = "Pronunciation needs improvement. Slow down and articulate words more clearly."

        difficult_words = []

        for word in words:
            if len(word) > 8 and word not in difficult_words:
                difficult_words.append(word)

        mistakes = [
            {
                "word": word,
                "reason": "Practice pronouncing this longer word more clearly."
            }
            for word in difficult_words[:5]
        ]

        print("Transcript analysis completed.")

        return {
            "score": score,
            "feedback": feedback,
            "mistakes": mistakes,
            "transcript": transcript
        }