
"""
2. Write a program which contains one class named as Circle. 
Circle class contains three instance variables as Radius ,Area, Circumference. 
That class contains one class variable as PI which is initialise to 3.14. 
Inside init method initialise all instance variables to 0.0. 
TThere are three instance methods inside class as Accept() , CalculateArea() , 
CalculateCircumference(), Display().
Accept method will accept value of Radius from user.
CalculateArea() method will calculate area of circle and store it into instance variable Area.
CalculateCircumference() method will calculate circumference of circle and store it into instance 
variable Circumference.
And Display() method will display value of all the instance variables as Radius , Area, 
Circumference.
After designing the above class call all instance methods by creating multiple objects.

"""

class Circle:
    Pi = 3.14
    
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
        
    def Accept(self):
        print("Enter the Radius of Circle : ")
        self.Radius = float(input())
        
        
    def CalculateArea(self):
        self.Area = Circle.Pi*(self.Radius**2)
        #return self.area 
        
         
    def CalculateCircumference(self):
        self.Circumference = 2*(Circle.Pi*self.Radius)
       # return self.Circumference
        
        
    def Display(self):
        print("Area of circle is ",self.Area)
        print("circumference of circle is : ",self.Circumference)
        
        
         
        
        
        
def main():
    # print("Enter two Numbers : ")
    # i1 = int(input())
    # i2 = int(input())
    
    Obj1 = Circle()
    Obj2 = Circle()
    
    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()
    
    Obj2.Accept()
    Obj2.CalculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()
    
    


if __name__ == "__main__":
    main()