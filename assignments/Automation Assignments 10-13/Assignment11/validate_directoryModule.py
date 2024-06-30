from LoggingFileModules import logging
import os

def validate_directory(Dir):
    if not os.path.isdir(Dir):
        logging("Error: Given Directory is not Present")
        return False
    return True
