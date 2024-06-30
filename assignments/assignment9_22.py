
"""
2. Write a program which accept file name from user and open that file and display the contents 
of that file on screen. 
Input : Demo.txt 
Display contents of Demo.txt on console. 
"""

import os

def display(fname):
    
    if os.path.exists(fname):
        
        fobj=open(fname,"r")
        
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