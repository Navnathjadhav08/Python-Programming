import os
from .validate_directory import validate_directory
from .logging_module import logging
from .hashfile import hashfile

def calculate_checksums(directory):
    checksums = {}
    
    if not validate_directory(directory):
        raise ValueError("Invalid directory")
    
    if not os.path.isabs(directory):
        directory = os.path.abspath(directory)
        
    if os.path.isdir(directory):
        for dirname, subdir, filelist in os.walk(directory):
            for file in filelist:
                filepath = os.path.join(dirname, file)
                hash_code = hashfile(filepath)
                checksums[filepath] = hash_code
    else:
        raise ValueError("Directory does not exist")
                
    return checksums
