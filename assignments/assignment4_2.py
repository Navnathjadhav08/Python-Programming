
"""
2.Write a program which contains one lambda function which accepts two parameters and return 
its multiplication. 
Input : 4 3 Output : 12 
Input : 6 3 Output : 18  
"""




def main():
    print("Enter 2 Number")
    n1 = int(input())
    n2 = int(input())
    
    mult = lambda n1,n2 : n1*n2
    
    print("Power off 2 of number is ",mult(n1,n2))
        
if __name__ == '__main__':
    main()
    