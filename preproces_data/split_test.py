import os
import random
import shutil

# Set the source folder paths
BASE_DIR = r'E:\Nanda\Pekerjaan Rumah\Kuliah D3 TE Poltek\Bangkit_Academy\preproces_big'
# print(BASE_DIR + r"\resistor")
source_folders = {
    "ic" : BASE_DIR + r'\ic',
    "resistor" : BASE_DIR + r'\resistor',
    "transistor" :BASE_DIR + r'\transistor',
    "capacitor": BASE_DIR + r'\capacitor',
    "arduino_uno": BASE_DIR + r'\arduino_uno',
    "diode": BASE_DIR + r'\diode',
    "inductor": BASE_DIR + r'\inductor',
    "transformator": BASE_DIR + r'\transformator',
    "esp32" : BASE_DIR + r'\esp32'

}

# Set the destination folder paths
destination_folders = {
    'train': r'E:\Nanda\Pekerjaan Rumah\Kuliah D3 TE Poltek\Bangkit_Academy\Capstone\data_4cls\train',
    'validation': r'E:\Nanda\Pekerjaan Rumah\Kuliah D3 TE Poltek\Bangkit_Academy\Capstone\data_4cls\validation'
}

# Set the train-validation ratio
train_ratio = 0.8

# Create the destination folders
for folder in destination_folders.values():
    os.makedirs(folder, exist_ok=True)
    print("Make Folder")

# Iterate through each source folder
for category, source_folder in source_folders.items():
    # Get the list of image files in the source folder
    image_files = os.listdir(source_folder)
    random.shuffle(image_files)  # Shuffle the list randomly
    
    # Split the image files into train and validation sets
    train_count = int(train_ratio * len(image_files))
    train_files = image_files[:train_count]
    validation_files = image_files[train_count:]
    
    # Move the train files to the train folder
    train_folder = os.path.join(destination_folders['train'], category)
    os.makedirs(train_folder, exist_ok=True)
    for file in train_files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(train_folder, file)
        shutil.copyfile(source_path, destination_path)
        print("Train Succes")

    # Move the validation files to the validation folder
    validation_folder = os.path.join(destination_folders['validation'], category)
    os.makedirs(validation_folder, exist_ok=True)
    for file in validation_files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(validation_folder, file)
        shutil.copyfile(source_path, destination_path)
        print("Validation Succes")