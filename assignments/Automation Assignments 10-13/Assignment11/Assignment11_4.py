"""
Please follow below rules while designing automation script as 

    • Accept input through command line or through file. 
    • Display any message in log file instead of console. 
    • For separate task define separate function. 
    • For robustness handle every expected exception. 
    • Perform validations before taking any action. 
    • Create user defined modules to store the functionality. 
    

4. Design automation script which accept directory name and delete all duplicate files from that 
    directory. Write names of duplicate files from that directory into log file named as Log.txt. 
    Log.txt file should be created into current directory. Display execution time required for the 
    script. 
    
    Usage : DirectoryDusplicateRemoval.py “Demo” 
    Demo is name of directory.

"""

# DirectoryDuplicateRemoval.py

import os
import sys
import time
import logging
from file_utils import find_duplicates, delete_files

def setup_logging():
    """Setup logging configuration."""
    logging.basicConfig(filename='Log.txt', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def validate_directory(directory):
    """Validate if the given directory exists."""
    if not os.path.isdir(directory):
        raise ValueError(f"The directory {directory} does not exist.")

def main(directory):
    """Main function to remove duplicate files from the directory."""
    start_time = time.time()
    setup_logging()

    try:
        validate_directory(directory)
        logging.info(f"Processing directory: {directory}")
        
        duplicates = find_duplicates(directory)
        
        if duplicates:
            logging.info(f"Duplicate files found: {duplicates}")
            delete_files(duplicates)
            logging.info(f"Duplicate files deleted successfully.")
        else:
            logging.info("No duplicate files found.")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(f"Execution time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: DirectoryDuplicateRemoval.py <DirectoryPath>")
        sys.exit(1)
    
    directory = sys.argv[1]
    main(directory)
