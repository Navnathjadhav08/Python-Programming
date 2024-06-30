"""9. Write a program which display first 10 even numbers on screen. 
Output : 2 4 6 8 10 12 14 16 18 20 """
    
   
def display(No):
    s = 0
    cnt = 0
    while(cnt <= No):
        print(s,end=" ")
        s = s+2
        cnt = cnt+1
    
def main():
    No = (int(input("Enter the Number")))
    display(No) 
        
        
if __name__ == "__main__":
    main()
    
        