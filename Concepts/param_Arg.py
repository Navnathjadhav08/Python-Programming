"""Parameters are specified within the pair of parentheses in the function definition,
separated by commas. When we call the function, we supply the values in the same
way. Note the terminology used - the names given in the function definition are called
parameters whereas the values you supply in the function call are called arguments"""

def Add(No1,No2):    #No1&No2 are parameters
    return No1+No2
    ''' This is Docstring for function Add.

 First line start with capital letter and end with. '''
            
               # and sencod line must be in 3rd line and followed by blnkspace .'''

    
def main():
    No1 = (int(input("Enter the first Number ")))
    No2 = (int(input("Enter the Second Number ")))
    ans = Add(No1,No2) #No1&No2 are Arguments
    
    print("Addition is ",ans)   
    print(Add.__doc__) 
        
        
if __name__ == "__main__":
    main()
    
