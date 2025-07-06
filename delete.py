#!python3
# Deleting unwanted files from a folder3



import os

def deleteFiles(folder):
    folder = os.path.abspath(folder)

    for foldername,subfolders,filenames in os.walk(folder):
        for filename in filenames:
            filepath = os.path.join(foldername,filename)
            if os.path.getsize(filepath) > 2000000:
                print(f'Deleting {filepath}')
                os.unlink(filepath)



deleteFiles("C:\\Users\\rohan\\Desktop\\waste")
 
print('Task Completed')



# Find all the files greater than 5 MB in size and delete them
# Print those files with their absolute path to the screen
