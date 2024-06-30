
"""
5. Write a recursive program which accept number from user and return its 
factorial. 
Input : 5 
 
Output : 120
"""

factX = 1
#cnt = 5
def Fact(No):
    # global cnt
    global factX
    if(No > 0):
        factX *= No
        Fact(No-1)
        

    return factX

def FactXX(No):
    
    if(No == 0):
        return 1
    else:
        return No * FactXX(No-1)

    
    
def main():
    No = (int(input("Enter the Number")))
    ret = FactXX(No)
    print(" Fact is ",ret) 
    
        
        
if __name__ == "__main__":
    main()