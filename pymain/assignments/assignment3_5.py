
"""
5.Write a program which accept N numbers from user and store it into List. Return addition of all 
prime numbers from that List. Main python file accepts N numbers from user and pass each 
number to ChkPrime() function which is part of our user defined module named as 
MyNum. Name of the function from main python file should be ListPrime(). 
Input : Number of elements : 11 
Input Elements : 13 5 45 7 4 56 10 34 2 5 8 
Output : 54 (13 + 5 + 7 +2 + 5) 
"""

import sys
sys.path.append(R'\Users\NAVNATH\OneDrive\Desktop\Py\assignments\modules')

import MyNum as num

def ListPrime(numbers):
    prime_list = []
    prime_list = num.CheckPrime(numbers)
    
    
    
    addition = 0
    for i in prime_list:
        addition += i
        
    return addition
    

def main():
    print("Enter size")
    size = int(input())
    #size = int(input())
    
    listX = [ ]
    
    
    
    print("Enter the {} Number".format(size))
    
    for i in range(size):
        no = int(input())
        listX.append(no)
        
        
    ret = ListPrime(listX)
        
    print("Addition  of prime Number is",ret)
    
if __name__ == '__main__':
    main()
    