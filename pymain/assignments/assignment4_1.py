
"""
1.Write a program which contains one lambda function which accepts one parameter and return 
power of two. 
Input : 4 Output : 16 
Input : 6 Output : 64  
"""




def main():
    print("Enter Number")
    n = int(input())
    
    pow = lambda n : n**2
    
    print("Power off 2 of number is ",pow(n))
        
if __name__ == '__main__':
    main()
    