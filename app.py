from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Define the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load your trained model
MODEL_PATH = "C:\\Users\\SAHIL\\Desktop\\SIH\\deepfake_model.h5"
model = load_model(MODEL_PATH)

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """
    Check if the file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_frame(frame, img_size=(224, 224)):
    """
    Preprocess a single frame for prediction.
    """
    resized_frame = cv2.resize(frame, img_size)
    normalized_frame = resized_frame / 255.0
    return np.expand_dims(normalized_frame, axis=0)

def predict_video(video_path, threshold=0.5, img_size=(224, 224)):
    """
    Predict if a video is real or fake based on the trained model.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return "Error: Could not open video file."

    frame_count = 0
    fake_frames = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        preprocessed_frame = preprocess_frame(frame, img_size)
        prediction = model.predict(preprocessed_frame)

        if prediction[0][0] > threshold:
            fake_frames += 1

    cap.release()

    fake_percentage = (fake_frames / frame_count) * 100
    result = {
        'total_frames': frame_count,
        'fake_frames': fake_frames,
        'fake_percentage': fake_percentage,
        'video_status': 'FAKE' if fake_percentage > 50 else 'REAL'
    }
    return result

@app.route('/upload', methods=['POST'])
def upload_video():
    """
    Handle video upload and prediction.
    """
    if 'video' not in request.files:
        return jsonify({'error': 'No video part'}), 400

    file = request.files['video']

    if file.filename == '':
        return jsonify({'error': 'No selected video'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Predict if the video is real or fake
        prediction_result = predict_video(file_path)
        return jsonify(prediction_result)
    else:
        return jsonify({'error': 'Invalid file type. Allowed types are mp4, avi, mov'}), 400

if __name__ == '__main__':
    app.run(debug=True)
