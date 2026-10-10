import os
import shutil

# Folder containing this Python file
source_folder = os.path.dirname(os.path.abspath(__file__))

# Destination folder
destination_folder = os.path.join(source_folder, "JPG_Files")

# Create destination folder
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move JPG images
for file in os.listdir(source_folder):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(file, "moved successfully!")

print("All JPG files have been moved!")