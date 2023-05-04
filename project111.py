import os
import shutil

from_dir = "C:/Users/hi/Downloads"
to_dir = "C:/Users/hi/Document_files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    