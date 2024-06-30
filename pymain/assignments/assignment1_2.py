"""Write a program which contains one functionnamed as ChkNum() which accept one parameter
    as Number . If Number is even then it should display "Even Number" Otherwise display "Odd number" on console"""
    
def ChkNum(No1):
    if((No1%2 )== 0):
        return 1;
    else:
        return 0;
    
def main():
    No = (int(input("Enter the Number")))
    ans = ChkNum(No)
    
    if(ans == 1):
        print("Number is even")
    else:
        print("Number is Odd")    
        
        
if __name__ == "__main__":
    main()
    
        