#Import OS for operating system interaction
import os
#Import Shell Utilities for high level file operations
import shutil

def organize_files(directory):
    #Assigned folders for different file categories
    folders = {
        "Excel Spreadsheets": [".xls", ".xlsx", ".csv"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Text Files": [".txt"],
        "Word Documents": [".doc", ".docx"]
        #Structure: "Folder Name": [".fileextension"]. Remember to add/remove the ',' as required.
    }
