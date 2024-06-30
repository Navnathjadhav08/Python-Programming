#Run Using Command Prompt

"""
3.Write a program which accept file name from user and create new file named as Demo.txt and 
copy all contents from existing file into new file. Accept file name through command line 
arguments. 
Input : ABC.txt 
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt

"""

import os

def creatFile(fname):
    if os.path.exists(fname):
        print("File is Exist")
    else:
        open(fname,"x")
        print("file is Created !!!")
        
        

def Write(fname):
    if os.path.exists(fname):
        fobj = open(fname,"w")
        
        print("write in the file : ")
        data = input()
        
        fobj.write(data)
        
        fobj.close()
        
    else : 
        fobj1 = open(fname,"x")
       
        print("write in the file : ")
        data = input()
        
        fobj1.write(data)
        
        fobj1.close()
        
        display(fname)
        
        
       
def copy(fname1,fname2):
    fobj1 = open(fname1,"r")
    fobj2 = open(fname2,"w")
    
    data = fobj1.read()
    print(f"readingfrom {fname1} is Successfull" )
    
    fobj2.write(data)
    print(f"Write into {fname2} is Successfull" )
    
    print(f"Data of copy file {fname2} is")
    display(fname2)
    
     
        
        

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
    
    print("Write data into first file ")
    Write(fname)
    
    fname1 = input("enter the name for file Second :  ")
    creatFile(fname1)
    copy(fname,fname1)
        
    
    
    
if __name__ == "__main__":
    main()