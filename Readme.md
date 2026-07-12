# 🎙️ PronounceAI

An AI-powered English Pronunciation Analyzer built using **React**, **FastAPI**, and **OpenAI Whisper**.

Upload a 30–45 second English audio recording and receive:
- Automatic speech transcription
- Pronunciation score
- AI-generated pronunciation feedback
- Suggested words to improve

---

## 📸 Screenshots

### Landing Page

![Landing Page](screenshots/landing-page.png)

---

### Upload Audio

![Upload Audio](screenshots/upload-page.png)

---

### Pronunciation Analysis

![Analysis Result](screenshots/analysis-page.png)

---

## ✨ Features

- 🎤 Upload English audio recordings (30–45 seconds)
- 📝 AI-powered speech transcription using Whisper
- 📊 Pronunciation scoring
- 💬 Personalized pronunciation feedback
- 🎯 Suggested words for improvement
- 🚫 Silent audio detection
- 📱 Clean and responsive user interface

---

## 🛠 Tech Stack

### Frontend

- React
- Vite
- CSS3

### Backend

- FastAPI
- Python
- OpenAI Whisper
- FFmpeg

---

## 📂 Project Structure

```
Pronounce-AI
│
├── Backend
│   ├── services
│   │   ├── analysis_service.py
│   │   └── speech_service.py
│   │
│   ├── main.py
│   ├── requirements.txt
│   └── .gitignore
│
├── frontend
│   ├── src
│   │   ├── components
│   │   │   ├── UploadCard.jsx
│   │   │   ├── AnalysisCard.jsx
│   │   │   └── AnalysisCard.css
│   │   │
│   │   ├── App.jsx
│   │   └── App.css
│   │
│   ├── package.json
│   └── ...
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Yugandhar-code/Pronounce-AI.git
```

```
cd Pronounce-AI
```

---

## Backend Setup

```
cd Backend
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the FastAPI server

```bash
uvicorn main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

---

## Frontend Setup

```
cd frontend
```

Install packages

```bash
npm install
```

Run the development server

```bash
npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

## How It Works

1. User uploads an English audio recording.
2. Backend receives the audio.
3. Whisper transcribes the speech.
4. Transcript is analyzed.
5. Pronunciation score and feedback are generated.
6. Results are displayed in the React frontend.

---

## Current Limitations

- Pronunciation score is generated using a heuristic analysis based on transcript characteristics.
- Supports English audio only.
- Requires a local Whisper model and FFmpeg installation.

---

## Future Improvements

- Real phoneme-level pronunciation assessment
- Audio waveform visualization
- Audio playback
- Speech confidence visualization
- User authentication
- History of previous analyses
- Cloud deployment

---

## Author

**Yugandhar**

GitHub:
https://github.com/Yugandhar-code