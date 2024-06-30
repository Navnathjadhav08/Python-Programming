
"""
1.Design python application which creates two thread named as even and odd. Even 
thread will display first 10 even numbers and odd thread will display first 10 odd 
numbers.

"""
import threading

def CheckEven(No):
     start = 0
     for i in range(No):
        print(i,":",start)
        start = start +2
    
       
       
            
            
def CheckOdd(No):
        start = 1
        for i in range(No):
            print(i,":",start)
            start = start +2
    
       

    
    
def main():
    No = (int(input("Enter the Number")))
    
    t1 = threading.Thread(target = CheckEven,args =(No,))
    t2 = threading.Thread(target = CheckOdd,args =(No,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    
        
        
if __name__ == "__main__":
    main()