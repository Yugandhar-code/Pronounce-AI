import { useState } from "react";

function UploadCard() {
  const [selectedFile, setSelectedFile] = useState(null);

  // Handles file selection
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  // Handles removing the selected file
  const handleRemoveFile = () => {
    setSelectedFile(null);
  };

  const handleAnalyze = async () => {
  if (!selectedFile) {
    alert("Please select an audio file first.");
    return;
  }

  const formData = new FormData();
  formData.append("audio", selectedFile);

  try {
    const response = await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    console.log("Backend Response:", data);
  } catch (error) {
    console.error("Upload failed:", error);
  }
};

  return (
    <div className="upload-card">
      <h2>Upload Your Recording</h2>

      <p>
        Please upload an English audio recording between 30 and 45 seconds.
      </p>

      <input
        type="file"
        accept="audio/*"
        onChange={handleFileChange}
      />

      <p>
        {selectedFile
          ? `Selected File: ${selectedFile.name}`
          : "No file selected"}
      </p>

      {selectedFile && (
        <button onClick={handleRemoveFile}>
          Remove File
        </button>
      )}

      <br />
      <br />

      <button
        onClick={handleAnalyze}
        disabled={!selectedFile}
      >
        Analyze
      </button>
    </div>
  );
}

export default UploadCard;