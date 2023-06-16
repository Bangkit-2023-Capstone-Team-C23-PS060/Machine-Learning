import os
import random

base_directory = r"E:\path\data"  # Specify the base directory path
classes = ["ic",
               "resistor",
               "transistor",
               "capacitor"]
                #  "arduino_uno",
                #  "diode",
                #  "inductor",
                #  "transformator",
                #  "esp32"]  # Specify the directories
def deleted_desired_count():
    desired_file_count = 500  # Number of files to keep
    for directory in classes:
        # Get the full directory path
        full_directory_path = os.path.join(base_directory, directory)
        # Get a list of all files in the directory
        files = os.listdir(full_directory_path)
        # Shuffle the files randomly
        random.shuffle(files)
        # Determine the number of files to delete
        files_to_delete = len(files) - desired_file_count
        # Delete the extra files
        for i in range(files_to_delete):
            file_path = os.path.join(full_directory_path, files[i])
            os.remove(file_path)
            print(f"Deleted: {file_path}")

def delete_duplicate():
    directory = r'E:\path\data\class'  # Specify the directory path
    file_names = os.listdir(directory)  # Get a list of all files in the directory
    unique_names = set()  # Set to store unique file names
    for file_name in file_names:
        if file_name in unique_names:
            file_path = os.path.join(directory, file_name)  # Complete file path
            os.remove(file_path)  # Delete the duplicate file
        else:
            unique_names.add(file_name)  # Add the file name to the set
    print("Duplicate files removed successfully.")

if __name__ == '__main__':
    deleted_desired_count()
    # delete_duplicate()
