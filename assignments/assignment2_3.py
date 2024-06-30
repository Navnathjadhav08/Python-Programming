"""3. Write a program which accept one number from user and return its factorial. 
Input : 5 Output : 120
 
 """
    
   
def factorial(No):
    ans = 1
    for i in range(1,No+1):
        ans = ans * i;
    return ans
    
def main():
    No = (int(input("Enter the Number :> ")))
    print("factorial of number ",No," is ",factorial(No)) 
        
        
if __name__ == "__main__":
    main()