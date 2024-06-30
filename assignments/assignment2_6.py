"""6. Write a program which accept one number and display below pattern. 
Input : 5 
Output :
 * * * * * 
 * * * * 
 * * * 
 * * 
 *  
 """
    
def display(No):
    Cnt = No
    for i in range(No):
        for i in range(Cnt,0,-1):
            print("*",end=" ")
        print()
        Cnt= Cnt-1
    
def main():
    No = (int(input("Enter the Number")))
    display(No) 
        
        
if __name__ == "__main__":
    main()