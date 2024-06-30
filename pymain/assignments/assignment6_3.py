
"""
3.Design python application which creates two threads as evenlist and oddlist. Both the 
threads accept list of integers as parameter. Evenlist thread add all even elements 
from input list and display the addition. Oddlist thread add all odd elements from input 
list and display the addition.

"""
import threading

def Evenlist(Numbers):
    sum = 0
    for i in Numbers:
        if (i%2 == 0):
            sum = sum + i
    print("Sum of even list:",sum)
       
            
            
def Oddlist(No):
    sum = 0
    for i in No:
        if  (i%2 != 0):
            sum = sum + i
    print("Sum of odd list:",sum)
    
    
def main():
    print("Enter size")
    size = int(input())
    #size = int(input())
    
    listX = [ ]
    
    
    
    print("Enter the {} Numbers".format(size))
    
    for i in range(size):
        no = int(input())
        listX.append(no)
    
    t1 = threading.Thread(target=Evenlist ,args=(listX,))
    t2 = threading.Thread(target=Oddlist,args=(listX,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    
        
        
if __name__ == "__main__":
    main()