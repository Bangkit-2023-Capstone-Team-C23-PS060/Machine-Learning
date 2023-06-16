import os
import shutil

class MergeDir:
    def __init__(self, train_dir, validation_dir, merged_dir):
        self.train_dir = train_dir 
        self.validation_dir = validation_dir 

        self.merged_dir = merged_dir 
    def create_dir(self):
        if not os.path.exists(self.merged_dir):
            os.makedirs(self.merged_dir)
    def merged(self):
        for component in os.listdir(self.train_dir):
            components_dir = os.path.join(self.train_dir, component)
            merged_components_dir = os.path.join(self.merged_dir,component)
            if not os.path.exists(merged_components_dir):
                shutil.copytree(components_dir, merged_components_dir)
                print("Train Merge Done")

    def merged_val(self):
        for components in os.listdir(self.validation_dir):
            component_dir = os.path.join(self.validation_dir, components)
            merged_component_dir = os.path.join(self.merged_dir, components)
            # #trying to overwrite file but, it doesn't work
            
            # Copy the files from the validation directory to the merged directory
            if not os.path.exists(merged_component_dir):
                shutil.copytree(component_dir, merged_component_dir)
                print("Validation Merge Done")
            # else:
            #     shutil.rmtree(merged_component_dir)
            #     shutil.copytree(component_dir, merged_component_dir, dirs_exist_ok=True)
            #     print("Validation Merge Done (Overwritten)")


if __name__ == '__main__':
    train_dir = r'E:\data\train'
    validation_dir = r'E:\data\validation'
    merged_dir = r'E:\merged_data'
    merger = MergeDir(train_dir, validation_dir, merged_dir)
    merger.create_dir()
    merger.merged()
    merger.merged_val()