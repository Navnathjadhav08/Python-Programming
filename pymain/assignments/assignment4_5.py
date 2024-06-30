
"""
5.Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will 
return Maximum number from that numbers. (You can also use normal functions instead of 
lambda functions). 
Input List = [2, 70 , 11, 10, 17, 23, 31, 77] 
List after filter = [2, 11, 17, 23, 31] 
List after map = [4, 22, 34, 46, 62] 
Output of reduce = 62
"""
from functools import reduce

CheckPrime = lambda x: all(x%i!=0 for i in range (2,int(x**0.5)+1)) and x>1
MultByTwo = lambda y: y*2
FindMax = lambda u,v : max(u,v)

def main():
    print("Enter Size")
    n = int(input())
    
    Data = [] 
    print("Enter numbers")
    for i in range(n):
        no = int(input("Enter {} Number".format(i)))
        Data.append(no)
        
    print("Data from List",Data)
    
    fData = list(filter(CheckPrime,Data))
    print("Data after filter Activity : ",fData)
    
    mData = list(map(MultByTwo,fData))
    print("Data after map activity : ",mData)
    
    rData = reduce(FindMax, mData)
    print("Data after reduce activity : ",rData)
   
        
if __name__ == '__main__':
    main()
    