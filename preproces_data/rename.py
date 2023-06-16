import os

folder_path = r'E:\Nanda\Pekerjaan Rumah\Kuliah D3 TE Poltek\Bangkit_Academy\Capstone\esp32 Devkit V1-20230524T091437Z-001\esp32 Devkit V1'
  # Specify the folder path here
 # Specify the folder path here
counter = 1  # Initial counter value

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):  # Make sure it's a file and not a subdirectory
        file_name, file_extension = os.path.splitext(filename)
        new_filename = f"esp32__{counter}{file_extension}"
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(file_path, new_file_path)
        print(f"Renamed '{filename}' to '{new_filename}'")
        counter += 1

