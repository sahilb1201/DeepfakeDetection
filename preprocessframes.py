import cv2
import os

def preprocess_frames(input_folder, output_folder, img_size=(224, 224)):
    # Ensure output folder path is correctly formatted and does not contain any invalid characters
    output_folder = output_folder.strip().strip('"')

    # Check if the output folder exists; create it if it doesn't
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        if img is not None:
            # Resize the image
            resized_img = cv2.resize(img, img_size)
            # Normalize the image (scaling to [0, 1] range)
            normalized_img = resized_img / 255.0
            # Save the preprocessed image back to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, normalized_img * 255)  # Convert back to 0-255 for saving
        else:
            print(f"Could not read image: {img_path}")

# Get user inputs for multiple input and output folders
input_folders = input("Enter the paths to the input folders with frames, separated by commas: ").split(',')
output_folders = input("Enter the corresponding paths to the output folders, separated by commas: ").split(',')

# Process each pair of input and output folders
for input_folder, output_folder in zip(input_folders, output_folders):
    input_folder = input_folder.strip().strip('"')
    output_folder = output_folder.strip().strip('"')
    print(f"Processing frames from {input_folder} to {output_folder}")
    preprocess_frames(input_folder, output_folder)


