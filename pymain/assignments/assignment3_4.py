
"""
4.Write a program which accept N numbers from user and store it into List. Accept one another 
number from user and return frequency of that number from List. 
Input : Number of elements : 11 
Input Elements : 13 5 45 7 4 56 5 34 2 5 65 
Element to search : 5 
Output : 3
"""

def SearchX(numbers,n):
    ans = 0
    for i in range(len(numbers)):
        if numbers[i] == n:
            ans = ans + 1 
    return ans

def main():
    print("Enter size")
    size = int(input())
    #size = int(input())
    
    listX = [ ]
    
    
    
    print("Enter the {} Number".format(size))
    
    for i in range(size):
        no = int(input())
        listX.append(no)
        
    fn = int(input("Enter Number to Serach : "))
        
    ret = SearchX(listX,fn)
        
    print("Frequency of Number is",ret)
    
if __name__ == '__main__':
    main()
    