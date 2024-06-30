import os
from validate_directoryModule import validate_directory
from LoggingFileModules import logging
from hashfile import hashfile

def Checksums(DirPath):
    Checksums = {}
    
    # Validate the directory
    if not validate_directory(DirPath):
        raise ValueError("Invalid directory")
    
    # Convert to absolute path if necessary
    if not os.path.isabs(DirPath):
        DirPath = os.path.abspath(DirPath)
        
    # Check if the directory exists
    if os.path.isdir(DirPath):
        for Dirname, subdir, filelist in os.walk(DirPath):
            for file in filelist:
                filepath = os.path.join(Dirname, file)
                hashc = hashfile(filepath)
                Checksums[filepath] = hashc
    else:
        raise ValueError("Directory does not exist")
                
    return Checksums
