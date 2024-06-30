"""6.Write a program which accept number from user and check whether that number is positive or 
negative or zero. 
Input : 11 Output : Positive Number 
Input : -8 Output : Negative Number 
Input : 0 Output : Zero """
    
def ChkNum(No1):
    if((No1 < 0 )):
        print("Negative Number")
    elif(No1>0):
        print("positive Number")
    else:
        print("zero")
    
def main():
    No = (int(input("Enter the Number")))
    ans = ChkNum(No)
    
       
        
        
if __name__ == "__main__":
    main()
    
        