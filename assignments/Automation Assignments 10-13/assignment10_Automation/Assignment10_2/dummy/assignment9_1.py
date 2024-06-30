#Run Using Command Prompt

"""
1.Write a program which accepts file name from user and check whether that file exists in 
current directory or not. 
Input : Demo.txt 
Check whether Demo.txt exists or not. 
"""

import os

def check_exists(fname):
    if os.path.exists(fname):
        print(f" file '{fname}' exists ")
    else:
        print(f" file '{fname}'  not exist ")


def main():
    fname = input("Enter the file name: ")
    check_exists(fname)
        
    
    
    
if __name__ == "__main__":
    main()