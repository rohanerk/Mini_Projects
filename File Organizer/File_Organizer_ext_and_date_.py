#python3

# File organizer tool by extension

import os
import shutil

def organize_by_extension(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            # Get the file extension
            ext = filename.split(".")[-1].lower()
            # Create folder for this extension
            ext_folder = os.path.join(folder_path, ext.upper())
            os.makedirs(ext_folder, exist_ok = True)

            shutil.move(file_path, os.path.join(ext_folder,filename))

    print("Files sorted")



# File organizer tool by date

import os
import shutil
import datetime

def organize_by_date(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            # Get last modified time
            timestamp = os.path.getmtime(file_path)
            date = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

            # Create a folder
            date_folder = os.path.join(folder_path, date)
            os.makedirs(date_folder, exist_ok = True)

            # Move file to that folder
            shutil.move(file_path, os.path.join(date_folder,filename))

    print("Files sorted")
