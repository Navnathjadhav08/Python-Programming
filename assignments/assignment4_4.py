
"""
4.Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all such numbers which are even. Map function will calculate its square. 
Reduce will return addition of all that numbers. 
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
List after filter = [2, 4, 4, 2, 8, 10] 
List after map = [4, 16, 16, 4, 64, 100] 
Output of reduce = 204 
"""
from functools import reduce

CheckEven = lambda x: (x%2 == 0)
Squre = lambda y: y*y
Add = lambda u,v : u+v

def main():
    print("Enter Size")
    n = int(input())
    
    Data = [] 
    print("Enter numbers")
    for i in range(n):
        no = int(input("Enter {} Number".format(i)))
        Data.append(no)
        
    print("Data from List",Data)
    
    fData = list(filter(CheckEven,Data))
    print("Data after filter Activity : ",fData)
    
    mData = list(map(Squre,fData))
    print("Data after map activity : ",mData)
    
    rData = reduce(Add, mData)
    print("Data after reduce activity : ",rData)
   
        
if __name__ == '__main__':
    main()
    