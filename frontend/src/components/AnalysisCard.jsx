import { FiFileText } from "react-icons/fi";
import { FiTarget } from "react-icons/fi";
import { FiMessageSquare } from "react-icons/fi";
import { FiAward } from "react-icons/fi";

import { useEffect, useRef } from "react";
import "./AnalysisCard.css";

function AnalysisCard({ analysisResult }) {
  const analysisRef = useRef(null);

  useEffect(() => {
    if (analysisResult && analysisRef.current) {
      analysisRef.current.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  }, [analysisResult]);

  if (!analysisResult) return null;

  return (
    <div ref={analysisRef} className="analysis-card">

      <h2>Pronunciation Analysis</h2>

      {/* Transcript */}

      <div className="result-section">
        <h3><FiFileText /> Transcript</h3>
        <p>{analysisResult.transcript}</p>
      </div>

      {/* Score */}

      <div className="score-card">
        <div className="score-number">
          {analysisResult.score}
        </div>

        <div className="score-title">
          <FiAward />
          Pronunciation Score
        </div>
      </div>

      {/* Feedback */}

      <div className="result-section">
        <h3><FiMessageSquare /> AI Feedback</h3>
        <p>{analysisResult.feedback}</p>
      </div>

      {/* Mistakes */}

      <div className="result-section">
        <h3><FiTarget /> Words to Improve</h3>

        {analysisResult.mistakes &&
        analysisResult.mistakes.length > 0 ? (
          <div className="mistakes">
            {analysisResult.mistakes.map((mistake, index) => (
              <span
                key={index}
                className="mistake-chip"
              >
                {mistake.word}
              </span>
            ))}
          </div>
        ) : (
          <p>No pronunciation issues detected.</p>
        )}
      </div>

    </div>
  );
}

export default AnalysisCard;