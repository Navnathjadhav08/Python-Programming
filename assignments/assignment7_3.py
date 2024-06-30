
"""
3. Write a program which contains one class named as Arithmetic. 
Arithmetic class contains three instance variables as Value1 ,Value2. 
Inside init method initialise all instance variables to 0. 
There are three instance methods inside class as Accept(), Addition(), Subtraction(), 
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects

"""

class Arithmetic:
    
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
        
    def Accept(self):
        print("Enter Two Numbers : ")
        self.Value1 = int(input())
        self.Value2 = int(input())
        
        
        
    def Addition(self):
        Result =  self.Value1 + self.Value2
        return Result
        
    def Subtraction(self):
        Result =  self.Value1 - self.Value2
        return Result
        
    def Multiplication(self):
        Result =  self.Value1 * self.Value2
        return Result
        
    def Division(self):
        Result =  self.Value1 / self.Value2
        return Result
         
        
        
        
def main():
    
    Obj1 = Arithmetic()
    Obj2 = Arithmetic()
    
    Obj1.Accept()
    print("addition is " ,Obj1.Addition())
    print("substraction is " ,Obj1.Subtraction())
    print("multification is " ,Obj1.Multiplication())
    print("division  is " ,Obj1.Division())
   
    
    Obj2.Accept()
    print("addition is " ,Obj2.Addition())
    print("substraction is " ,Obj2.Subtraction())
    print("multification is " ,Obj2.Multiplication())
    print("division  is " ,Obj2.Division())
    
   
    
    


if __name__ == "__main__":
    main()