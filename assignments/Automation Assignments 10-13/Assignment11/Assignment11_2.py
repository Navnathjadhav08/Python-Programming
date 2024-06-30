"""Please follow below rules while designing automation script as 

    • Accept input through command line or through file. 
    • Display any message in log file instead of console. 
    • For separate task define separate function. 
    • For robustness handle every expected exception. 
    • Perform validations before taking any action. 
    • Create user defined modules to store the functionality. 
    
2. Design automation script which accept directory name and write names of duplicate files from 
    that directory into log file named as Log.txt. Log.txt file should be created into current 
    directory. 
    
    Usage : DirectoryDusplicate.py “Demo” 
    
    Demo is name of directory.

"""

from sys import argv
import os
from DisplayChecksumModule import Checksums
from LoggingFileModules import logging
from checkDuplicatesModule import checkDup,printDuplicate

def main():
    print("====================================================================================")
    print("----------------------Automation Application by Navnath Jadhav----------------------")
    print("====================================================================================")

    print("Application Name is : " + argv[0])

    if len(argv) != 2:
        print("Error: Invalid number of arguments!")
        exit()

    if argv[1] in ("-h", "-H"):
        print("This script is used to accept a directory name and display checksum of all files in log files.")
        exit()

    if argv[1] in ("-u", "-U"):
        print("Usage: Application_name.py DirectoryName")
        exit()

    try:
        msg = "Logging activity started..."
        logging(msg)
        
        # Use a dictionary to store the checksums
        sums = {}
        dup = {}
        
        # Calculate checksums
        sums = Checksums(argv[1])
        
        # Convert the sums dictionary to a string for logging
        sums_str = "\n".join(f"{k}: {v}" for k, v in sums.items())
        
        # Log the checksums
        logging("CheckSums of Files Are Following:\n" + sums_str)
        #print(sums_str)
        
        dup = checkDup(sums)
        printDuplicate(dup)
        
       
            
        
        
        
    except ValueError as e:
        logging(f"Error: Value Error ({e})")
        print(f"Error: {e}")
        
    except Exception as e:
        logging(f"Error: Exception occurred ({e})")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
