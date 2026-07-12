import { useState, useRef } from "react";

function UploadCard({ setAnalysisResult }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [duration, setDuration] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const fileInputRef = useRef(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (!file) return;

    setError("");
    setDuration(null);
    setAnalysisResult(null);

    const audio = new Audio();
    const objectURL = URL.createObjectURL(file);

    audio.src = objectURL;

    audio.onloadedmetadata = () => {
      const audioDuration = audio.duration;

      setDuration(audioDuration);
      setSelectedFile(file);

      if (audioDuration < 30 || audioDuration > 45) {
        setError("Audio must be between 30 and 45 seconds.");
      } else {
        setError("");
      }

      URL.revokeObjectURL(objectURL);
    };
  };

  const handleRemoveFile = () => {
    setSelectedFile(null);
    setAnalysisResult(null);
    setDuration(null);
    setError("");

    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  const handleAnalyze = async () => {
    if (!selectedFile) {
      alert("Please select an audio file first.");
      return;
    }

    setLoading(true);
    setAnalysisResult(null);

    const formData = new FormData();
    formData.append("audio", selectedFile);

    try {
      const response = await fetch(
        "https://pronounce-ai-jh40.onrender.com",
        {
          method: "POST",
          body: formData,
        }
      );

      if (!response.ok) {
        throw new Error("Server returned an error.");
      }

      const data = await response.json();
      setAnalysisResult(data);
    } catch (error) {
      console.error(error);
      alert(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-card">
      <h2>Upload Your Recording</h2>

      <p>
        Please upload an English audio recording between 30 and 45 seconds.
      </p>

      <input
        ref={fileInputRef}
        id="audio-upload"
        type="file"
        accept="audio/*"
        onChange={handleFileChange}
        hidden
      />

      <label htmlFor="audio-upload" className="upload-btn">
        📁 Choose Audio File
      </label>

      {selectedFile && (
        <div className="file-info">
          <div className="file-name">📄 {selectedFile.name}</div>

          {duration && (
            <div className="file-duration">
              {duration.toFixed(1)} seconds
            </div>
          )}
        </div>
      )}

      {error && <p style={{ color: "red" }}>{error}</p>}

      <div className="button-group">
        {selectedFile && (
          <button className="remove-btn" onClick={handleRemoveFile}>
            Remove
          </button>
        )}

        <button
          className="analyze-btn"
          onClick={handleAnalyze}
          disabled={!selectedFile || !!error || loading}
        >
          {loading ? (
            <>
              <span className="loader"></span>
              <span>Analyzing...</span>
            </>
          ) : (
            "Analyze"
          )}
        </button>
      </div>
    </div>
  );
}

export default UploadCard;