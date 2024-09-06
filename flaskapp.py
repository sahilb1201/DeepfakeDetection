from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'avi', 'mov'}

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def preprocess_frame(frame, img_size=(224, 224)):
    resized_frame = cv2.resize(frame, img_size)
    normalized_frame = resized_frame / 255.0
    return np.expand_dims(normalized_frame, axis=0)

def predict_video(video_path, model_path, threshold=0.5, img_size=(224, 224)):
    model = load_model(model_path)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return {"error": "Could not open video file."}

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
        "total_frames": frame_count,
        "fake_frames": fake_frames,
        "fake_percentage": fake_percentage,
        "prediction": "FAKE" if fake_percentage > 50 else "REAL"
    }
    return result

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Define the path to your model
        model_path = "C:\\Users\\SAHIL\\Desktop\\SIH\\deepfake_detector_model.h5"
        
        result = predict_video(file_path, model_path)
        return jsonify(result)
    
    return jsonify({"error": "Invalid file type"}), 400

if __name__ == '__main__':
    app.run(debug=True)
