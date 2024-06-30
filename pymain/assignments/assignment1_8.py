"""8. Write a program which accept number from user and print that number of “*” on screen. 
Input : 5 Output : * * * * *  """
    
   
def display(No):
    for i in range(No):
        print("*",end=" ")
    
def main():
    No = (int(input("Enter the Number")))
    display(No) 
        
        
if __name__ == "__main__":
    main()
    
        