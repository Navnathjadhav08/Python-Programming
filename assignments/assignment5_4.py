
"""
4.Write a recursive program which accept number from user and return 
summation of its digits. 
Input : 879 
Output : 24
"""

sum = 0
#cnt = 5
def sumDigi(No):
    # global cnt
    global sum
    if(No > 0):
        sum += No%10
        sumDigi(No//10)
        #return n % 10 + sum_of_digits(n // 10)

    return sum
    
def main():
    No = (int(input("Enter the Number")))
    ret = sumDigi(No)
    print("Sum of digit is ",ret) 
    
        
        
if __name__ == "__main__":
    main()