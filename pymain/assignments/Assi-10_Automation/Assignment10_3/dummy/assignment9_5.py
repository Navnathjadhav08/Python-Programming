#Run Using Command Prompt

"""
5. Accept file name and one string from user and return the frequency of that string from file. 
Input : Demo.txt Marvellous 
Search “Marvellous” in Demo.txt 

"""

import os

def frequency(file1,str):
    fobj1 = open(file1,"r")
   
        
    print(f"file is open in Read mode Successfully {file1} ")
    
        
    data1 = fobj1.read()
    
    cnt = data1.count(str) 
   
    fobj1.close()
   
    return cnt
    


    


def main():
    fname = input("Enter the file name first: ")
    
    
    
    str1 = input("enter the string for count frequency :  ")
    print("frequency is ",frequency(fname,str1))
    
    
    
if __name__ == "__main__":
    main()