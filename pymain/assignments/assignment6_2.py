
"""
2.Design python application which creates two threads as evenfactor and oddfactor. 
Both the thread accept one parameter as integer. Evenfactor thread will display 
addition of even factors of given number and oddfactor will display addition of odd 
factors of given number. After execution of both the thread gets completed main 
thread should display message as “exit from main”.

"""
import threading

def EvenFactAdd(No):
    sum = 0
    for i in range(1,No+1):
        if (No%i == 0) and (i%2 == 0):
            sum = sum + i
    print("Sum of even factors:",sum)
       
            
            
def OddFactAdd(No):
    sum = 0
    for i in range(1,No+1):
        if (No%i == 0) and (i%2 != 0):
            sum = sum + i
    print("Sum of odd factors:",sum)
    
    
def main():
    No = (int(input("Enter the Number")))
    
    t1 = threading.Thread(target=EvenFactAdd ,args=(No,))
    t2 = threading.Thread(target=OddFactAdd,args=(No,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    
        
        
if __name__ == "__main__":
    main()