"""
Please follow below rules while designing automation script as 

    • Accept input through command line or through file. 
    • Display any message in log file instead of console. 
    • For separate task define separate function. 
    • For robustness handle every expected exception. 
    • Perform validations before taking any action. 
    • Create user defined modules to store the functionality. 
    

4. Design automation script which accept directory name and mail id from user and create log 
    file in that directory which contains information of running processes as its name, PID, 
    Username. After creating log file send that log file to the specified mail. 
    
 Usage : ProcInfoLog.py Demo xyz@gmail.com 
 
Demo is name of Directory. 

xyz@gmail.com is the mail id.

"""


from sys import *
import time
from CreateLog import logg
from DisplayProcessesModule import DisplayProc
from sendMail_Module import is_connected,MailSender
from scheduleModule import schedulefun

def main():
    print("====================================================================================")
    print("----------------------Automation Application by Navnath Jadhav----------------------")
    print("====================================================================================")

    
    print("Apllication  Name is : "+argv[0])
    
    if(len(argv) != 3):
        print("Error : Invalid Numbers of Arguments" )
        logg("Error : Invalid Numbers of Arguments")
        exit()
        
    if(argv[1] == "-h" )or( argv[1] == "-H"):
    
        print("HELP : automation script which accept directory name and mail id from user and create log \
file in that directory which contains information of running processes as its name, PID, \
Username. After creating log file send that log file to the specified mail.")
        logg("automation script which accept directory name and mail id from user and create log \
    file in that directory which contains information of running processes as its name, PID, \
    Username. After creating log file send that log file to the specified mail.")
        exit()
    
    
    if argv[1] in ("-u", "-U"):
        print("Usage : ProcInfoLog.py Demo xyz@gmail.com \
 \
Demo is name of Directory. \
\
xyz@gmail.com is the mail id.")
        logg("Usage : ProcInfoLog.py Demo xyz@gmail.com \
 \
Demo is name of Directory. \
\
xyz@gmail.com is the mail id.")
        
        exit()
        
    try:
       
        t= time.ctime()
        fname = logg(f"log created at {argv[1]}",argv[1])
        MailSender(fname,str(t),argv[2])
        print("....Checking Connection......")
        if is_connected:
            print("Connected..........")
            print("Sending Mail......")
            
            interval_type = "seconds"
            at_time = "20"
            
            schedulefun(logg, MailSender, interval_type, at_time, argv[1], argv[2])
            
        else:
            print("Unable to Connect !!!")
            
        
            
        
    except ValueError as v:
        print("Error: Value Error "+v)
        logg(v)
    
    except Exception as e:
        logg(f"Error: Exception occurred ({e})")
        print(f"Error: {e}")
        
          
if __name__ == "__main__":
    main()
    


