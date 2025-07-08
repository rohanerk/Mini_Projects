#! python3
# backupToZip.py - Copies an entire folder and its contents into a ZIP file
# whose filename increments

import zipfile,os

def backupToZip(folder):
    # Backup the entire contents of a folder into a ZIP file

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName): # If the file exists, it will increment by 1 , 
            break                           # if it doesn't exist, the loop will break and the zip file will be created
        number = number + 1

    # TODO : Create the ZIP File

    print('Creating %s...'% (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName,'w')   # ZIp file is created

    # TODO : Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file
        backupZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('zip'):
                cotinue
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('Done')

backupToZip('C:\\delicious1')
