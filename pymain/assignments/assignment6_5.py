
"""
5.Design python application which contains two threads named as thread1 and thread2. 
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on 
screen. After execution of thread1 gets completed then schedule thread2.
"""
import threading

def Display1(No):
     
     for i in range(1,No+1):
         print(i)
        
    
       
       
            
            
def Display2(No):
        
        for i in range(No,0,-1):
            print(i)
            
    
       

    
    
def main():
    No = (int(input("Enter the Number")))
    
    t1 = threading.Thread(target = Display1,args =(No,))
    t2 = threading.Thread(target = Display2,args =(No,))
    
    t1.start()
    t1.join()
    t2.start()
    
    
    t2.join()
    
    
        
        
if __name__ == "__main__":
    main()