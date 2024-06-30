
"""
1. Write a recursive program which display below pattern. 
Input : 5 
Output : * * * * *
"""

cnt = 0
def display(No):
    global cnt
    if(cnt < No):
        print("*",end=" ")
        cnt +=1
        display(No)
    
def main():
    No = (int(input("Enter the Number")))
    display(No) 
        
        
if __name__ == "__main__":
    main()