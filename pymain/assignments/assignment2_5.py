"""5.Write a program which accept one number for user and check whether number is prime or not. 
Input : 5 Output : It is Prime Number 
 """
    
   
def CheckPrime(No):
    ans = 0
    for i in range(2,No):
        if(No%i == 0):
            print(No,"is not prime")
            return
        else:
            print(No,"is a prime ")
            return
            
    
   
    
def main():
    No = (int(input("Enter the Number :> ")))
    CheckPrime(No)
        
        
if __name__ == "__main__":
    main()