"""Write a program which contains one functionnamed as Add() which accept two parameter
    as Number . & return addition of that two numbers"""
    
def Add(No1,No2):
    return No1+No2
    
def main():
    No1 = (int(input("Enter the first Number ")))
    No2 = (int(input("Enter the Second Number ")))
    ans = Add(No1,No2)
    
    print("Addition is ",ans)    
        
        
if __name__ == "__main__":
    main()
    
        