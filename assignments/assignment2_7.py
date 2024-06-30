"""7. Write a program which accept one number and display below pattern. 
Input : 5 
Output :
 1 2 3 4 5 
 1 2 3 4 5
 1 2 3 4 5
 1 2 3 4 5 
 1 2 3 4 5  
  
 """
    
def display(No):
   
    for i in range(1,No+1):
        for i in range(1,No+1):
            print(i,end=" ")
        print()
        
    
def main():
    No = (int(input("Enter the Number")))
    display(No) 
        
        
if __name__ == "__main__":
    main()