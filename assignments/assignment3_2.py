
"""
2.Write a program which accept N numbers from user and store it into List. Return Maximum 
number from that List. 
Input : Number of elements : 7 
Input Elements : 13 5 45 7 4 56 34 
Output : 56 
"""

def Max(numbers):
    ans = 0
    for i in range(len(numbers)):
        if numbers[i]>ans:
            ans = numbers[i]
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
        
    ret = Max(listX)
        
    print("MAx of Number is",ret)
    
if __name__ == '__main__':
    main()
    