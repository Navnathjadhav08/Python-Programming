"""4.Write a program which accept one number form user and return addition of its factors. 
Input : 12 Output : 16 '(1+2+3+4+6)'
 """
    
   
def Addfact(No):
    ans = 0
    for i in range(1,No):
        if(No%i == 0):
            ans = ans+i
    
    return ans
    
def main():
    No = (int(input("Enter the Number :> ")))
    print("Addition of factor of \
number ",No," is ",Addfact(No)) 
   # \ in string use in multiline string but in program it treated  as a single line also use """    
        
if __name__ == "__main__":
    main()