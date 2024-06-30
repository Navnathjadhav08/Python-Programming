

import os
from Logf import Log

def validations(extension1,extension2,Directory):
    if not os.path.isdir(Directory):
        raise NotADirectoryError(f"unable to Find the Directory {Directory}")

    if not extension1.startswith('.'):
        raise ValueError(f"The provided extension '{extension1}' is not valid. It should start with a '.'.")

    if not extension2.startswith('.'):
        raise ValueError(f"The provided extension '{extension2}' is not valid. It should start with a '.'.")


def Replacer(DirName,fext1,fext2):
    try:
         validations(fext1,fext2,DirName)
         exist = os.path.isdir(DirName)
         matchfilenamelist = []
    
         if(exist == True):
            Log("Searching for the files .....")
            for foldername, subfoldername, filename in os.walk(DirName):
 
                for name in filename:
                    if name.endswith(fext1):
                          Log("Renaming.....")
                          old_file = os.path.join(foldername, name)
                          new_file = os.path.join(foldername, name.replace(fext1, fext2))
                          os.rename(old_file, new_file)
                          Log(f"Renamed: {old_file} to {new_file}")
                          
            
                
                
            else:
                Log(f"No files with extension '{fext1}' found in directory '{DirName}'.")
            
    except Exception as e:
        Log(f"Error occurred: {e}")
        raise
    
 
            
            

