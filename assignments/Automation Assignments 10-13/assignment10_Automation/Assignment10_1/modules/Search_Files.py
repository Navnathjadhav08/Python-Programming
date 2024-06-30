"""
Please follow below rules while designing automation script as 
• Accept input through command line or through file. 
• Display any message in log file instead of console. 
• For separate task define separate function. 
• For robustness handle every expected exception. 
• Perform validations before taking any action. 
• Create user defined modules to store the functionality. 
1.Design automation script which accept directory name and file extension from user. Display all 
files with that extension. 
 Usage : DirectoryFileSearch.py “Demo” “.txt” 
Demo is name of directory and .txt is the extension that we want to search.

"""

import os
from Logf import Log

def validations(extension,Directory):
    if not os.path.isdir(Directory):
        raise NotADirectoryError(f"unable to Find the Directory {DirName}")

    if not extension.startswith('.'):
        raise ValueError(f"The provided extension '{extension}' is not valid. It should start with a '.'.")


def search(DirName,fext):
    try:
         validations(fext,DirName)
         exist = os.path.isdir(DirName)
         matchfilenamelist = []
    
         if(exist == True):
            Log("Searching for the files .....")
            for foldername, subfoldername, filename in os.walk(DirName):
            # print(foldername)
            # print(subfoldername)
            # print(filename)
                for name in filename:
                    if name.endswith(fext):
                          matchfilenamelist.append(name)
            
            if matchfilenamelist:
                for file in matchfilenamelist:
                    Log(file)     
                
            else:
                Log(f"No files with extension '{fext}' found in directory '{DirName}'.")
            
    except Exception as e:
        Log(f"Error occurred: {e}")
        raise
    
 
            
            

