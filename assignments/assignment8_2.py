
"""

2. Write a program which contains one class named as BankAccount. 
BankAccount class contains two instance variables as Name & Amount. 
That class contains one class variable as ROI which is initialise to 10.5. 
Inside init method initialise all name and amount variables by accepting the values from user. 
There are Four instance methods inside class as Display(), Deposit(), Withdraw(), 
CalculateIntrest().
Deposit() method will accept the amount from user and add that value in class instance variable 
Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount 
from class instance variable Amount.
CalculateIntrest() method calculate the interest based on Amount by considering rate of interest 
which is Class variable as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects.

"""

class BankAccount:
    
    ROI = 10.5
    
    def __init__(self):
        self.Name = 0
        self.Amount = 0
       
    def Accept(self):
        self.Name = input("Enter YOur Name : ")
        self.Amount = int(input("Enter Amount : "))
    
    def Deposit(self):
        amt = int(input("Enter Amount to Deposit : "))
        self.Amount = amt + self.Amount
        
    def Withdraw(self):
        amt = int(input("Enter Amount for Withdraw : "))
        self.Amount =  self.Amount - amt
        
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest calculated: {interest}")
     
    def Display(self):
        print(f"Name: {self.Name}, Amount: {self.Amount}")
        
         
        
        
        
def main():
    
    Obj1 = BankAccount()
    Obj2 = BankAccount()


    
    Obj1.Accept()
    Obj1.Display()
    Obj1.Deposit()
    Obj1.Withdraw()
    Obj1.CalculateInterest()
    Obj1.Display()

    
    Obj2.Accept()
    Obj1.Display()
    Obj2.Deposit()
    Obj2.Withdraw()
    Obj2.CalculateInterest()
    Obj1.Display()


if __name__ == "__main__":
    main()