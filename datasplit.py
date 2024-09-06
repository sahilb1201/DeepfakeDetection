import os
import shutil
import random

def create_directory_structure(base_dir):
    """Create directories for train, val, and test sets."""
    for category in ['train', 'val', 'test']:
        for label in ['real', 'fake']:
            os.makedirs(os.path.join(base_dir, category, label), exist_ok=True)

def split_data(input_folder, output_folder, split_ratios=(0.7, 0.15, 0.15)):
    """Split data into train, val, and test sets."""
    
    # Convert to absolute paths
    input_folder = os.path.abspath(input_folder)
    output_folder = os.path.abspath(output_folder)

    # Debug print to verify paths
    print(f"Input Folder: {input_folder}")
    print(f"Output Folder: {output_folder}")
    
    # Create directory structure
    create_directory_structure(output_folder)
    
    for label in ['real', 'fake']:
        # Construct the full path for preprocessed frames
        label_path = os.path.join(input_folder, f'preprocessed_frames_{label}')
        
        # Check if the directory exists
        if not os.path.exists(label_path):
            print(f"Error: The folder {label_path} does not exist.")
            return
        
        # Get all file names from the preprocessed folders
        file_names = os.listdir(label_path)
        
        # Shuffle file names to ensure randomness
        random.shuffle(file_names)
        
        # Compute split indices
        train_split = int(split_ratios[0] * len(file_names))
        val_split = int((split_ratios[0] + split_ratios[1]) * len(file_names))
        
        # Assign files to train, val, and test sets
        train_files = file_names[:train_split]
        val_files = file_names[train_split:val_split]
        test_files = file_names[val_split:]
        
        # Move files to their respective directories
        for file_name in train_files:
            shutil.copy(
                os.path.join(label_path, file_name),
                os.path.join(output_folder, 'train', label, file_name)
            )
        
        for file_name in val_files:
            shutil.copy(
                os.path.join(label_path, file_name),
                os.path.join(output_folder, 'val', label, file_name)
            )
        
        for file_name in test_files:
            shutil.copy(
                os.path.join(label_path, file_name),
                os.path.join(output_folder, 'test', label, file_name)
            )
            
    print("Data splitting complete!")

# Input folder containing preprocessed frames
input_folder = "C:\\Users\\SAHIL\\Desktop\\SIH\\preprocessed"  # Use your actual path

# Output folder where split datasets will be stored
output_folder = "C:\\Users\\SAHIL\\Desktop\\SIH\\splitting_data"  # Use your actual path

# Call the function to split data
split_data(input_folder, output_folder)
