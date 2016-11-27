import os
import shutil

def filepaths(directory):
    for root, directories, files in os.walk(directory):
        for filename in directories:
            filepath = os.path.join(root, filename)
            if ',' in filename:
                print(filepath)
                shutil.rmtree(filepath)
            else:
                filepaths(filepath)


filepaths(".")
