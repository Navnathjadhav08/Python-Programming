"""2. Write a program which accept one number and display below pattern. 
Input : 5 
Output : 
 * * * * * 
 * * * * *
 * * * * * 
 * * * * * 
 * * * * *
 """
    
   
def display(No):
    for i in range(No):
        for i in range(No):
            print("*",end=" ")
        print()
    
def main():
    No = (int(input("Enter the Number")))
    display(No) 
        
        
if __name__ == "__main__":
    main()