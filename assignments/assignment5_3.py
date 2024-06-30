
"""
3.Write a recursive program which display below pattern. 
Input : 5 
Output : 5 4 3 2 1
"""

#cnt = 5
def display(No):
    # global cnt
    if(No > 0):
        print(No,end=" ")
        display(No-1)
    
def main():
    No = (int(input("Enter the Number")))
    display(No) 
        
        
if __name__ == "__main__":
    main()