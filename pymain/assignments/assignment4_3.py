
"""
3.Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all such numbers which greater than or equal to 70 and less than or equal to 
90. Map function will increase each number by 10. Reduce will return product of all that 
numbers.  
"""
from functools import reduce

Check = lambda x: (x>=70 and x<=90)
increase = lambda y: y+10
Mult = lambda u,v : u*v

def main():
    print("Enter Size")
    n = int(input())
    
    Data = [] 
    print("Enter numbers")
    for i in range(n):
        no = int(input("Enter {} Number".format(i)))
        Data.append(no)
        
    print("Data from List",Data)
    
    fData = list(filter(Check,Data))
    print("Data after filter Activity : ",fData)
    
    mData = list(map(increase,fData))
    print("Data after map activity : ",mData)
    
    rData = reduce(Mult, mData)
    print("Data after reduce activity : ",rData)
   
        
if __name__ == '__main__':
    main()
    