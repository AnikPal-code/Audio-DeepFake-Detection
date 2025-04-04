# Documentation

[🔗 Download the User Guide (PDF)]([Momenta - Audio Deepfake Detection.pdf](https://github.com/AnikPal-code/Audio-DeepFake-Detection/blob/main/Momenta%20-%20Audio%20Deepfake%20Detection.pdf))

# Audio DeepFake Detection

This project is an **Audio DeepFake Detection** system built using **React (Frontend)** and **Flask (Backend)** with a deep learning model to classify audio files as real or fake.

## Features
- Supports **MP3, WAV, and MP4 audio files**.
- Uses a **pretrained deep learning model** to analyze audio.
- Deployable via **Netlify (Frontend)** and **Flask API (Backend)**.
- Provides real-time classification results.

## Demo: Click or copy paste this link below:
https://anikpal-audio-deepfake-detection.netlify.app/

---
## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AnikPal-code/Audio-DeepFake-Detection.git
cd Audio-DeepFake-Detection
```

### 2️⃣ Backend (Flask API) Setup

#### Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

#### Run Flask Server
```bash
python app.py
```
> The Flask server will start at `http://127.0.0.1:5000/`

### 3️⃣ Frontend (React) Setup

#### Install Dependencies
```bash
cd frontend
npm install
```

#### Start Development Server
```bash
npm start
```
> The React frontend will be available at `http://localhost:3000/`

---
## Deployment

### 🔥 Deploy Flask Backend (Python)
1. Use **Render** or **Heroku** to host the Flask API.
2. Update `frontend/src/config.js` with the hosted backend URL.

### 🚀 Deploy React Frontend (Netlify)
1. Build the project:
   ```bash
   npm run build
   ```
2. Deploy the `build/` folder to **Netlify** or **Vercel**.

---
## API Endpoints

### 🔹 Upload & Predict Audio
**Endpoint:** `/predict`  
**Method:** `POST`
```json
{
  "file": "audio.mp3"
}
```
**Response:**
```json
{
  "result": "The audio is Fake."
}
```

---
## Troubleshooting

### 🛠 CORS Issues on Netlify Deployment
- Ensure backend has `CORS(app)` enabled.
- Use the correct **backend URL** in frontend requests.

### 🔥 Upload Button Not Working on Netlify
- Check browser console for errors.
- Make sure **backend API URL is correctly set** in frontend.

---
## Contributing
Feel free to submit issues or pull requests for improvements! 🎯

## License
This project is **MIT Licensed**.

