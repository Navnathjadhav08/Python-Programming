
"""
2. Write a recursive program which display below pattern. 
Input : 5 
Output : 1 2 3 4 5
"""

cnt = 1
def display(No):
    global cnt
    if(cnt < No+1):
        print(cnt,end=" ")
        cnt +=1
        display(No)
        
    
def main():
    No = (int(input("Enter the Number")))
    display(No) 
        
        
if __name__ == "__main__":
    main()