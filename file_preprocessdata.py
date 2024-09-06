import cv2
import os

def sanitize_path(path):
    # Remove leading and trailing quotes and whitespace
    return path.strip().strip('"').strip("'")

def extract_frames(video_path, output_folder, frame_rate=1):
    # Sanitize paths
    video_path = sanitize_path(video_path)
    output_folder = sanitize_path(output_folder)

    # Debug print statements
    print(f"Processing Video: {video_path}")
    print(f"Saving Frames to: {output_folder}")

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  

    cap = cv2.VideoCapture(video_path)  
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}.")
        return

    frame_id = 0

    while True:
        ret, frame = cap.read()
        if not ret: 
            break

        if frame_id % frame_rate == 0:  
            filename = os.path.join(output_folder, f'frame_{frame_id}.jpg')  
            cv2.imwrite(filename, frame)  

        frame_id += 1

    cap.release()  
    print(f"Finished processing {video_path}.\n")

# Get user inputs
video_paths = input("Enter the paths to the video files, separated by commas: ").split(',')
output_folders = input("Enter the corresponding output folder paths, separated by commas: ").split(',')
frame_rate = int(input("Enter the frame rate (frames per second to extract): "))

# Process each video and corresponding output folder
for video_path, output_folder in zip(video_paths, output_folders):
    extract_frames(video_path.strip(), output_folder.strip(), frame_rate)


