import os
from PIL import Image


class PreprocessingImage:
    def __init__(self, root_directory, target_directory, target_size):
        self.root_directory = root_directory
        self.target_directory = target_directory
        self.target_size = target_size

    def preproces_image(self):
        # Iterate through each subdirectory in the root directory
        for subdirectory in os.listdir(self.root_directory):
            subdirectory_path = os.path.join(self.root_directory, subdirectory)

            # Check if the item is a directory if None Create Dir
            if os.path.isdir(subdirectory_path):
                # Create the corresponding subdirectory in the target directory
                target_subdirectory = os.path.join(self.target_directory, subdirectory)
                os.makedirs(target_subdirectory, exist_ok=True)

                # Iterate through each image file in the subdirectory and its subdirectories
                for dirpath, dirnames, filenames in os.walk(subdirectory_path):
                    for filename in filenames:
                        file_path = os.path.join(dirpath, filename)

                        # Check if the file is an image
                        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                            try:
                                # Open the image
                                image = Image.open(file_path)

                                # Convert image to RGB
                                if image.mode != 'RGB':
                                    image = image.convert('RGB')

                                # Resize the image
                                resized_image = image.resize(self.target_size)

                                # Set the output file path with the new format in the target directory
                                output_file_path = os.path.join(target_subdirectory, os.path.splitext(filename)[0] + '.jpg')

                                # Save the resized image
                                resized_image.save(output_file_path, 'JPEG')

                                # Optionally, you can also delete the original file if needed
                                # os.remove(file_path)

                                # Print success message
                                print(f"Resized and converted '{filename}' to {self.target_size} and saved in the target directory.")
                            except UnidentifiedImageError:
                                print(f"Failed to resize and convert '{filename}'. Invalid or unsupported image file.")

if __name__ == '__main__':
    root_directory = r'C:\data'
    target_directory = r'E:\preproces_data'
    target_size = (224, 224)
    preprocess = PreprocessingImage(root_directory, target_directory, target_size)
    preprocess.preproces_image()
