
"""
1.Write a program which accept N numbers from user and store it into List. Return addition of all 
elements from that List. 
Input : Number of elements : 6 
Input Elements : 13 5 45 7 4 56 
Output : 130 
"""

def addition(numbers):
    ans = 0
    for i in range(len(numbers)):
        ans = ans + numbers[i]
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
        
    ret = addition(listX)
        
    print("Addition of Number is",ret)
    
if __name__ == '__main__':
    main()
    