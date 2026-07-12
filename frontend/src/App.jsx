import "./App.css";
import { useState } from "react";

import UploadCard from "./components/UploadCard";
import AnalysisCard from "./components/AnalysisCard";

function App() {

  const [analysisResult, setAnalysisResult] = useState(null);

  return (
    <div className="app">

      <header className="navbar">

        <div className="logo">
          🎙️ PronounceAI
        </div>

        <a href="#" className="docs-link">
          Documentation
        </a>

      </header>

      <main className="hero">

        <section className="hero-left">

          <h1>
            AI Pronunciation Checker for
            <br />
            English Speakers
          </h1>

          <p>
            Upload a 30–45 second English audio recording and receive
            AI-powered transcription, pronunciation scoring and
            detailed pronunciation feedback.
          </p>

          <div className="features">

            <div>✓ AI Transcription</div>
            <div>✓ Pronunciation Score</div>
            <div>✓ Word Suggestions</div>

          </div>

        </section>

        <section className="hero-right">

          <UploadCard
            setAnalysisResult={setAnalysisResult}
          />

        </section>

      </main>

      <AnalysisCard
        analysisResult={analysisResult}
      />

      <footer className="footer">

        <h3>PronounceAI</h3>

        <p>
          AI-powered English Pronunciation Assessment
        </p>

        <div className="footer-tech">

          <span>React</span>

          <span>FastAPI</span>

          <span>OpenAI Whisper</span>

        </div>

        <p className="copyright">
          © 2026 PronounceAI. Built for the Livo AI Software Engineer Assessment.
        </p>

      </footer>

    </div>
  );
}

export default App;