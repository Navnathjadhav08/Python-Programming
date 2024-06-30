
"""
1.Write a program which contains one class named as Demo. 
Demo class contains two instance variables as no1 ,no2. 
That class contains one class variable as Value. 
There are two instance methods of class as Fun and Gun which displays values of instance 
variables. 
Initialise instance variable in init method by accepting the values from user.
 
After creating the class create the two objects of Demo class as
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)
Now call the instance methods as
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()

"""

class Demo:
    value = 10
    
    def __init__(self,n1,n2):
        self.no1 = n1
        self.no2 = n2
        
    def Fun(self):
        print("Inside Fun method ")
        print("value of no1 is",self.no1)        
        print("value of no2 is",self.no2)        
        
    def Gun(self):
        print("Inside Gun method ")
        print("value of no1 is",self.no1)        
        print("value of no2 is",self.no2)        
        
def main():
    # print("Enter two Numbers : ")
    # i1 = int(input())
    # i2 = int(input())
    
    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)
    
    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()


if __name__ == "__main__":
    main()