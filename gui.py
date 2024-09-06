import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import numpy as np
from tensorflow.keras.models import load_model

def preprocess_frame(frame, img_size=(224, 224)):
    resized_frame = cv2.resize(frame, img_size)
    normalized_frame = resized_frame / 255.0
    return np.expand_dims(normalized_frame, axis=0)

def predict_video(video_path, model_path, threshold=0.5, img_size=(224, 224)):
    model = load_model(model_path)
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not open video file.")
        return

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
    
    result = f"Total Frames: {frame_count}\nFake Frames: {fake_frames} ({fake_percentage:.2f}%)"
    if fake_percentage > 50:
        result += "\nThe video is predicted to be FAKE."
    else:
        result += "\nThe video is predicted to be REAL."
    
    messagebox.showinfo("Prediction Result", result)

def select_video_file():
    video_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")]
    )
    video_entry.delete(0, tk.END)
    video_entry.insert(0, video_path)

def select_model_file():
    model_path = filedialog.askopenfilename(
        title="Select Trained Model File",
        filetypes=[("H5 Model Files", "*.h5")]
    )
    model_entry.delete(0, tk.END)
    model_entry.insert(0, model_path)

def start_detection():
    video_path = video_entry.get()
    model_path = model_entry.get()
    
    if not video_path or not model_path:
        messagebox.showwarning("Warning", "Please select both video and model files.")
        return
    
    predict_video(video_path, model_path)

# Create the main window
root = tk.Tk()
root.title("Deepfake Detection Tool")

# Create the widgets
video_label = tk.Label(root, text="Video File:")
video_label.grid(row=0, column=0, padx=5, pady=5)

video_entry = tk.Entry(root, width=50)
video_entry.grid(row=0, column=1, padx=5, pady=5)

video_button = tk.Button(root, text="Browse", command=select_video_file)
video_button.grid(row=0, column=2, padx=5, pady=5)

model_label = tk.Label(root, text="Model File:")
model_label.grid(row=1, column=0, padx=5, pady=5)

model_entry = tk.Entry(root, width=50)
model_entry.grid(row=1, column=1, padx=5, pady=5)

model_button = tk.Button(root, text="Browse", command=select_model_file)
model_button.grid(row=1, column=2, padx=5, pady=5)

detect_button = tk.Button(root, text="Start Detection", command=start_detection)
detect_button.grid(row=2, column=1, pady=20)

# Run the main loop
root.mainloop()
