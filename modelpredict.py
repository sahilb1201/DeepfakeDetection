import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model

def preprocess_frame(frame, img_size=(224, 224)):

    # Resize the frame
    resized_frame = cv2.resize(frame, img_size)
    # Normalize the image
    normalized_frame = resized_frame / 255.0
    # Expand dimensions to match model input
    return np.expand_dims(normalized_frame, axis=0)

def predict_video(video_path, model_path, threshold=0.5, img_size=(224, 224)):
   
    # Load the trained model
    model = load_model(model_path)
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    frame_count = 0
    fake_frames = 0
    
    # Process the video frame by frame
    while True:
        ret, frame = cap.read()
        if not ret:  
            break
        
        frame_count += 1
        
        # Preprocess the frame
        preprocessed_frame = preprocess_frame(frame, img_size)
        
        # Make prediction
        prediction = model.predict(preprocessed_frame)
        
        # Check if the frame is predicted as fake
        if prediction[0][0] > threshold:
            fake_frames += 1

    cap.release()

    # Determine overall result based on majority vote
    fake_percentage = (fake_frames / frame_count) * 100
    print(f"Total Frames: {frame_count}")
    print(f"Fake Frames: {fake_frames} ({fake_percentage:.2f}%)")
    
    if fake_percentage > 50:
        print("The video is predicted to be FAKE.")
    else:
        print("The video is predicted to be REAL.")

# Get user input for the video file and model path
video_path = input("Enter the path to the video file: ").strip().strip('"')
model_path = input("Enter the path to the trained model: ").strip().strip('"')

# Predict if the video is real or fake
predict_video(video_path, model_path)
