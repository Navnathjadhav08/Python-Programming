
"""

3. Write a program which contains one class named as Numbers. 
Arithmetic class contains one instance variables as Value. 
Inside init method initialise that instance variables to the value which is accepted from user. 
There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), 
Factors().
ChkPrime() method will returns true if number is prime otherwise return false.
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method 
as a helper method if required.
After designing the above class call all instance methods by creating multiple objects

"""
class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        return self.SumFactors() == self.Value * 2

    def Factors(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        print("Factors of", self.Value, ":", factors)

    def SumFactors(self):
        factors_sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors_sum += i
        return factors_sum

         
        
        
        
def main():
    
    o1 = Numbers(int(input("Enter a number: ")))
    o2 = Numbers(int(input("Enter number: ")))

    
    print("is prime", o1.ChkPrime())
    print("is perfect?", o1.ChkPerfect())
    o1.Factors()
    print("Sum of factors of :", o1.SumFactors())



    print("is  prime", o2.ChkPrime())
    print("iss  perfect", o2.ChkPerfect())
    o2.Factors()
    print("Sum of factors of num2:", o2.SumFactors())


if __name__ == "__main__":
    main()