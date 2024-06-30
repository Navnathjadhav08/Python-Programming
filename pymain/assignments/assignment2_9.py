"""9. Write a program which accept number from user and return number of digits in that number. 
Input : 5187934 Output : 7 
  
 """
    
def CountDigi(No):
     Cnt = 0
     while(No>0):
        No=No//10
        Cnt = Cnt + 1
     return Cnt
        
    
def main():
    No = (int(input("Enter the Number")))
    print("Number of Digits Are :> ",CountDigi(No)) 
        
        
if __name__ == "__main__":
    main()