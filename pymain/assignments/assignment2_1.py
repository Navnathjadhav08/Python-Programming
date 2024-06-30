"""1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() 
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two 
parameters as number and perform the operation. Write on python program which call all the 
functions from Arithmetic module by accepting the parameters from user.  """
    
   
import sys
sys.path.append(R'\Users\NAVNATH\OneDrive\Desktop\Py\assignments\modules')

"""Raw String
If you need to specify some strings where no special processing such as escape
sequences are handled, then what you need is to specify a raw string by prefixing r or
R to the string"""

import Arithmatic as ar
def main():
    no1 = (int(input("Enter the first no ")))
    no2 = (int(input("Enter the second no ")))
    
    print("Addition is ",ar.Add(no1,no2))
    print("Substraction is ",ar.Sub(no1,no2))
    print("Multification is ",ar.Mult(no1,no2))
    print("Division is ",ar.Div(no1,no2))
    
    #print( '\n\nThe PYTHONPATH is', sys.path, '\n') show module directory path
   
        
        
if __name__ == "__main__":
    main()
    
        