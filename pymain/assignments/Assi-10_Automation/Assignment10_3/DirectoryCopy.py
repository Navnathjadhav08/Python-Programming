"""
3. Design automation script which accept two directory names. Copy all files from first directory 
        into second directory. Second directory should be created at run time.
         
     Usage : DirectoryCopy.py “Demo” “Temp”
  
    Demo is name of directory which is existing and contains files in it. We have to create new 
    Directory as Temp and copy all files from Demo to Temp.
    
"""


import sys
import os
import logging
import configparser
from directory_copy_module import copy_files, validate_directories

def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    log_file = 'directory_copy.log'
    setup_logging(log_file)

    if len(sys.argv) == 3:
        
        
        src_dir = sys.argv[1]
        
        dst_dir = sys.argv[2]
        
    else:
        
        logging.error("Usage: DirectoryCopy.py <SourceDirectory> <DestinationDirectory> or DirectoryCopy.py <ConfigFile>")
        sys.exit(1)

    try:
        validate_directories(src_dir, dst_dir)
        copy_files(src_dir, dst_dir)
        
    except Exception as e:
        logging.error(f"Error during copying process: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
