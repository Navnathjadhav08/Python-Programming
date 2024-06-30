"""8. Write a program which accept one number and display below pattern. 
Input : 5 
 
Output : 
 1 
 1 2 
 1 2 3 
 1 2 3 4 
 1 2 3 4 5 
  
 """
    
def display(No):
    Cnt = 1
    for i in range(No):
        for i in range(1,Cnt+1):
            print(i,end=" ")
        print()
        Cnt= Cnt+1
        
    
def main():
    No = (int(input("Enter the Number")))
    display(No) 
        
        
if __name__ == "__main__":
    main()