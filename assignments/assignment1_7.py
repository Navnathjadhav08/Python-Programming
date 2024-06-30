"""7. Write a program which contains one function that accept one number from user and returns 
true if number is divisible by 5 otherwise return false. 
Input : 8 Output : False 
Input : 25 Output : True """
    
def ChkNum(No1):
    if((No1%5 )== 0):
        return 1;
    else:
        return 0;
    
def main():
    No = (int(input("Enter the Number")))
    ans = ChkNum(No)
    
    if(ans == 1):
        print("Number Divisible by 5 ")
    else:
        print("Number is Not divisible by 5")    
        
        
if __name__ == "__main__":
    main()
    
        