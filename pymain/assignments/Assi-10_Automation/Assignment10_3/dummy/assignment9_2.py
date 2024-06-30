#Run Using Command Prompt

"""
2. Write a program which accept file name from user and open that file and display the contents 
of that file on screen. 
Input : Demo.txt 
Display contents of Demo.txt on console. 
"""

import os

def display(fname):
    
    absolute_path = os.path.abspath(fname)
    
    print(f"Debug: Checking file at {absolute_path}")
    
    if os.path.exists(absolute_path):
        
        fobj = open(absolute_path,"r")
        
        print("file is open in Read mode Successfully ")
        
        data = fobj.read()
        
        print(data)
        
        fobj.close()
        
    else:
        print("Enable to open the File and read the file !!!")
        
        
    
    


def main():
    fname = input("Enter the file name: ")
    display(fname)
        
    
    
    
if __name__ == "__main__":
    main()