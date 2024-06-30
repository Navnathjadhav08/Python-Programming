"""Please follow below rules while designing automation script as 

    • Accept input through command line or through file. 
    • Display any message in log file instead of console. 
    • For separate task define separate function. 
    • For robustness handle every expected exception. 
    • Perform validations before taking any action. 
    • Create user defined modules to store the functionality. 
    
1.Design automation script which display information of running processes as its name, PID, 
  Username.
   
   Usage : ProcInfo.py

"""

from sys import *
from LoggingModule import logg
from DisplayProcessesModule import DisplayProc


def main():
    print("====================================================================================")
    print("----------------------Automation Application by Navnath Jadhav----------------------")
    print("====================================================================================")

    
    print("Apllication  Name is : "+argv[0])
    
    # if(len(argv) != 2):
    #     print("Error : Invalid Numbers of Arguments" )
    #     logg("Error : Invalid Numbers of Arguments")
    #     exit()
        
    if(argv[1] == "-h" )or( argv[1] == "-H"):
    
        print("HELP : This automation script which display information of running processes as its name, PID, \
Username")
        logg("HELP : This automation script which display information of running processes as its name, PID, \
Username")
        exit()
    
    
    if argv[1] in ("-u", "-U"):
        print("Usage: Application_name.py")
        logg("Usage: Application_name.py")
        exit()
        
    try:
        proc = DisplayProc()
        
        
    except ValueError as v:
        print("Error: Value Error "+v)
        logg(v)
    
    except Exception as e:
        logg(f"Error: Exception occurred ({e})")
        print(f"Error: {e}")
        
          
if __name__ == "__main__":
    main()
    

