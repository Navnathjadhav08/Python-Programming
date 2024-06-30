"""10. Write a program which accept number from user and return addition of digits in that number. 
Input : 5187934 Output : 37 
  
 """
    
def SumDigi(No):
     Cnt = 0
     Sum = 0
     i = 0
     while(No>0):
        i = No%10
        No=No//10
        Cnt = Cnt + 1
        Sum = Sum+i
     return Sum
        
    
def main():
    No = (int(input("Enter the Number")))
    print("Summation of Digits Are :> {0}".format(SumDigi(No))) 
        
        
if __name__ == "__main__":
    main()