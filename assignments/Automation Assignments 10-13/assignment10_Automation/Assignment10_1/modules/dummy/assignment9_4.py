#Run Using Command Prompt

"""
4.Write a program which accept two file names from user and compare contents of both the 
files. If both the files contains same contents then display success otherwise display failure. 
Accept names of both the files from command line. 
Input : Demo.txt Hello.txt 
Compare contents of Demo.txt and Hello.txt 

"""

import os

def Compare(file1,file2):
    fobj1 = open(file1,"r")
    fobj2 = open(file2,"r")
        
    print(f"file is open in Read mode Successfully {file1} & {file2}")
    
        
    data1 = fobj1.read()
    data2 = fobj2.read()
        
    if(data1 == data2):
        print( "Success")
    else:
        print("Failure")
        
    fobj1.close()
    fobj2.close()
    
    


def display(fname):
    
    if os.path.exists(fname):
        
        
        fobj = open(fname,"r")
        
        print("file is open in Read mode Successfully ")
        print(f"data from {fname}")
        
        data = fobj.read()
        
        print(data)
        
        fobj.close()
        
    else:
        print("Enable to open the File and read the file !!!")
        
        
 
    


def main():
    fname = input("Enter the file name first: ")
    
    
    
    fname1 = input("enter the name for file Second :  ")
    Compare(fname,fname1)
    
    
    
if __name__ == "__main__":
    main()