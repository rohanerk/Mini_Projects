#! Walk through the directory and search for files ending with .pdf and .jpg
# and copy these files into a new folder

import shutil,os

def selectivecopy(source_folder, dest_folder, extension):
    source_folder = os.path.abspath(source_folder)
    dest_folder = os.path.abspath(dest_folder)

    # Create destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)             # Creating a new folder

    # Walk through the folder

    for folders, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.lower().endswith(extension.lower()):
                sourceFile = os.path.join(folders,filename)
                destFile = os.path.join(dest_folder,filename)

                print(f'Copying {sourceFile} to {destFile}')
                shutil.copy2(sourceFile, destFile)
    print('Done Copying')

selectivecopy("C:\\Users\\rohan\\Desktop\\personal\\data engineering","C:\\Users\\rohan\\Desktop\\data science",".pdf")
