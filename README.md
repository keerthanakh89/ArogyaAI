# ArogyaAI
# 🩺 ArogyaAI — Intelligent Rural Health Support System

> **Team Sensors** | WitchHunt Hackathon 2026 | Theme: Health Wellbeing  
> AI-Powered Telemedicine for Rural India

---

## 👥 Team Members

| Name | Role |
|------|------|
| Keerthana K H | Android Developer & ML Lead |
| Bhavani G K | AI & Backend Engineer |
| Likitha | UI/UX & Frontend Design |
| Bhoomika | Research & Data Analysis |

---

## 🧠 Problem Statement

70% of India's population lives in rural areas, yet only 30% of doctors serve them. Rural patients face:
- Doctor-to-patient ratio of **1:10,000**
- **5+ hours** average travel to the nearest specialist
- **40%** of diagnoses delayed by 48+ hours
- No affordable digital health solution

---

## 💡 Our Solution

**ArogyaAI** is an AI-powered telemedicine Android application that:
- 🔍 Triages symptoms using on-device NLP & ML
- 🩺 Connects patients with doctors via video call
- ☁️ Maintains encrypted cloud-based health records
- 🌐 Works in low-bandwidth environments with offline support
- 🗣️ Supports Kannada, Hindi, Tamil, Telugu via voice UI

---

## 🏗️ System Architecture

```
Patient App (Kotlin)
        ↓
AI Triage Engine (TensorFlow Lite + FastAPI)
        ↓
Cloud Health Records (Firebase / AWS S3)
        ↓
Doctor Dashboard (Web Portal)
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|------------|
| Mobile | Kotlin, Jetpack Compose, MVVM |
| AI/ML | Python, TensorFlow Lite, Hugging Face NLP |
| Backend | FastAPI, scikit-learn |
| Cloud | Firebase Firestore, Firebase Auth, AWS S3 |
| DevOps | GitHub Actions, Docker |

---

## 🚀 How to Run Locally

### Prerequisites
- Android Studio Hedgehog or newer
- Python 3.10+
- Node.js 18+
- Git

### Step 1 — Clone the Repository
```bash
git clone https://github.com/keerthanakh89/ArogyaAI.git
cd ArogyaAI
```

### Step 2 — Run the Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
Backend runs at: `http://localhost:8000`

### Step 3 — Run the Android App
```bash
# Open the /app folder in Android Studio
# Connect an emulator or physical device
# Click ▶ Run
```

### Step 4 — Run the UI Prototype (React)
```bash
cd prototype
npm install
npm start
```
Opens at: `http://localhost:3000`

---

## 📁 Project Structure

```
ArogyaAI/
├── app/                    # Android Kotlin app
│   ├── src/main/java/
│   │   └── com/sensors/arogyaai/
│   │       ├── MainActivity.kt
│   │       ├── ui/
│   │       └── viewmodel/
│   └── build.gradle
├── backend/                # Python FastAPI + AI models
│   ├── main.py
│   ├── models/
│   ├── routes/
│   └── requirements.txt
├── prototype/              # Interactive React UI prototype
│   └── ArogyaAI_Prototype.jsx
├── presentation/           # WitchHunt submission deck
│   └── ArogyaAI_Sensors_WitchHunt.pptx
└── README.md
```

---

## 📊 Expected Impact

| Metric | Target |
|--------|--------|
| Faster diagnosis | 3x improvement |
| Travel reduction | 60% less |
| Potential users | 500M+ rural Indians |
| Availability | 24/7 |

---

## 🔒 Security & Compliance

- End-to-end encrypted patient data (AES-256)
- DPDPA (India Data Protection) compliant
- No PII stored locally on device
- Firebase Auth with OTP for patient identity

---

## 📄 License

MIT License — see [LICENSE](LICENSE)

---

*Built with ❤️ by Team Sensors for WitchHunt 2026*
