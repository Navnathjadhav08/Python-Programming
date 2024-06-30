"""
Please follow below rules while designing automation script as 

        • Accept input through command line or through file. 
        • Display any message in log file instead of console. 
        • For separate task define separate function. 
        • For robustness handle every expected exception. 
        • Perform validations before taking any action. 
        • Create user defined modules to store the functionality. 
        
Design automation script which performs following task. 

    Accept Directory name from user and delete all duplicate files from the specified directory by 
    considering the checksum of files. 
    Create one Directory named as logs and inside that directory create log file which 
    maintains all names of duplicate files which are deleted. 
    Name of that log file should contains the date and time at which that file gets created. 
    Accept duration in minutes from user and perform task of duplicate file removal after the specific 
    time interval. 
    
Accept Mail id from user and send the attachment of the log file. 

Mail body should contains statistics about the operation of duplicate file removal. 
Mail body should contains below things : 

    Starting time of scanning 
    Total number of files scanned 
    Total number of duplicate files found 
    
Consider below command line options for the gives script 

DuplicateFileRemoval.py E:/Data/Demo 50 xyz@gmail.com 
    - DuplicateFileRemoval.py 
 Name of python automation script 
    - E:/Data/Demo 
 Absolute path of directory which may contains duplicate files 
    - 50 
 Time interval of script in minutes 
    - xyz@gmail.com 
 Mail ID of the receiver 
 
Note : 

    For every separate task write separate function. 
    Write all user defined functions in one user defined module. 
    Use proper validation techniques. 
    Provide Help and usage option for script. 
    Create one Readme file which contains description of our script, details of command line options.
    
"""


from sys import argv
import sys
import time
import os
from modules.display_checksum import calculate_checksums
from modules.logging_module import logging
from modules.check_duplicates import find_duplicates, log_duplicates
from modules.remove_duplicates import remove_duplicates
from modules.validate_directory import validate_directory
from modules.schedule_module import schedule_removal
from modules.send_mail import send_log_via_mail

def main():
    print("====================================================================================")
    print("----------------------Automation Application by Navnath Jadhav----------------------")
    print("====================================================================================")

    print("Application Name is : " + argv[0])

    if len(argv) != 4:
        print("Error: Invalid number of arguments!")
        print("Usage: DuplicateFileRemoval.py <directory> <interval> <email>")
        exit()

    if argv[1] in ("-h", "-H"):
        print("""THis Application - Accept Directory name from user and delete all duplicate files from the specified directory by 
    considering the checksum of files. 
    Create one Directory named as logs and inside that directory create log file which 
    maintains all names of duplicate files which are deleted. 
    Name of that log file should contains the date and time at which that file gets created. 
    Accept duration in minutes from user and perform task of duplicate file removal after the specific 
    time interval. 
    
Accept Mail id from user and send the attachment of the log file.""")
        exit()

    if argv[1] in ("-u", "-U"):
        print("""DuplicateFileRemoval.py E:/Data/Demo 50 xyz@gmail.com 
    - DuplicateFileRemoval.py 
 Name of python automation script 
    - E:/Data/Demo 
 Absolute path of directory which may contains duplicate files 
    - 50 
 Time interval of script in minutes 
    - xyz@gmail.com 
 Mail ID of the receiver """)
        exit()
        
    directory = argv[1]
    interval = argv[2]
    email = argv[3]

    if not validate_directory(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    if not interval.isdigit():
        print(f"Error: {interval} is not a valid time interval.")
        sys.exit(1)
        
    interval = int(interval)
        
    try:
        schedule_removal(directory, interval, email)
                   
        
        
    except ValueError as e:
        logging(f"Error: Value Error ({e})")
        print(f"Error: {e}")
        
    except Exception as e:
        logging(f"Error: Exception occurred ({e})")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

