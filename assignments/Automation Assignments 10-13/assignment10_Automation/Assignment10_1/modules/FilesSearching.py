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

from Search_Files import search
from Logf import Log
import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: FilesSearching.py <directory_name> <file_extension>")
        sys.exit(1)
    
    directory = sys.argv[1]
    extension = sys.argv[2]
    
    search(directory,extension)

main()