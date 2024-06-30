"""4. Design automation script which accept two directory names and one file extension. Copy all 
files with the specified extension from first directory into second directory. Second directory 
should be created at run time. 
 Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe” 
Demo is name of directory which is existing and contains files in it. We have to create new 
Directory as Temp and copy all files with extension .exe from Demo to Temp."""

import sys
import os
import logging
from DireactoryCopyExt_module import copy_files_with_extension, validate_directories

def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    log_file = 'directory_copy_ext.log'
    setup_logging(log_file)

    if len(sys.argv) != 4:
        logging.error("Usage: DirectoryCopyExt.py <SourceDirectory> <DestinationDirectory> <FileExtension>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    file_extension = sys.argv[3]

    try:
        validate_directories(source_directory, destination_directory)
        copy_files_with_extension(source_directory, destination_directory, file_extension)
    except Exception as e:
        logging.error(f"Error during copying process: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
