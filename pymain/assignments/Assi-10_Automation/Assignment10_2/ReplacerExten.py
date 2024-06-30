"""
2. Design automation script which accept directory name and two file extensions from user. 
    Rename all files with first file extension with the second file extenntion. 
    Usage : DirectoryRename.py “Demo” “.txt” “.doc” 
    Demo is name of directory and .txt is the extension that we want to search and rename 
    with .doc. 
        After execution this script each .txt file gets renamed as .doc
"""


from ReplacerFun import Replacer
from Logf import Log
import os
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: FilesSearching.py <directory_name> <file_extension> <file_extension>")
        sys.exit(1)
    
    directory = sys.argv[1]
    extension1 = sys.argv[2]
    extension2 = sys.argv[3]
    
    
    Replacer(directory,extension1,extension2)

main()