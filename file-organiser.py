#Import OS for operating system interaction.
import os
#Import Shell Utilities for high level file operations.
import shutil

def organize_files(directory):
    #Assigned folders for different file categories.
    folders = {
        "Excel Spreadsheets": [".xls", ".xlsx", ".csv"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Text Files": [".txt"],
        "Word Documents": [".doc", ".docx"]
        #To add more: "Folder Name": [".extension"]. Remember to add/remove the ',' as required.
    }

    #Go through every file in the specifed directory.
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            #Get the file extension
            extension = os.path.splitext(filename)[1]

            #Check the extension against each category above and move the file.
            for folder, extensions in folders.items():
                if extension.lower() in extensions:
                    target_folder = os.path.join(directory, folder)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    shutil.move(os.path.join(directory, filename), os.path.join(target_folder, filename))

#Provide the directory path where the files are located.
directory_path = "C:/file-organiser-script/test-data"

#Call the function to organize the files.
organize_files(directory_path)

#A nice little confirmation message for when it's completed.
print("File organization complete.")