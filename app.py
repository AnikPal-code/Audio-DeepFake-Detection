from flask import Flask, request, jsonify, render_template
import os
import librosa
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
MODEL_PATH = "my_model.h5"
model = load_model(MODEL_PATH)

# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Allowed file types
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'ogg', 'flac', 'm4a'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"result": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"result": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"result": "Invalid audio file format"}), 400

    # Save the uploaded file
    filepath = os.path.join("temp", file.filename)
    os.makedirs("temp", exist_ok=True)
    file.save(filepath)

    try:
        # Load and preprocess the audio
        audio, sr = librosa.load(filepath, sr=16000)  # Resample to 16kHz
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=20)  # Extract MFCC features
        mfccs = np.mean(mfccs.T, axis=0)  # Average over time axis
        input_data = np.expand_dims(mfccs, axis=0)  # Reshape for model
        input_data = np.expand_dims(input_data, axis=-1)  # Ensure input shape matches model expectation

        # Get prediction from model
        prediction = model.predict(input_data)[0][0]  # Assuming binary classification

        # Interpret result
        result_text = "Fake" if prediction > 0.5 else "Real"

        os.remove(filepath)  # Clean up the file

        return jsonify({"result": f"The audio is {result_text}."})
    
    except Exception as e:
        print("Error processing file:", str(e))  # Debugging
        os.remove(filepath)
        return jsonify({"result": f"Error processing the file: {str(e)}"}), 400

@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/api/process', methods=['POST'])
def process_input():
    data = request.json
    user_text = data.get("text", "")
    response_message = f"You sent: {user_text}"
    return jsonify({"response": response_message})

def classify_audio(file_path):
    return "Real Audio" if "real" in file_path else "Fake Audio"

@app.route('/upload', methods=["POST"])  # ✅ Fixed the typo
def upload_file():
    if "file" not in request.files:
        return jsonify({"result": "No file uploaded"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"result": "No file selected"}), 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)
    
    result = classify_audio(file_path)
    
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
