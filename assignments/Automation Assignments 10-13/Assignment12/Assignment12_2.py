"""Please follow below rules while designing automation script as 

    • Accept input through command line or through file. 
    • Display any message in log file instead of console. 
    • For separate task define separate function. 
    • For robustness handle every expected exception. 
    • Perform validations before taking any action. 
    • Create user defined modules to store the functionality. 
    
2.Design automation script which accept process name and display information of that process if 
  it is running. 

  Usage : ProcInfo.py Notepad

"""


from sys import *
from LoggingModule import logg
from DisplayProcessesModule import DisplayProc
from CheckProcRunModule import Check


def main():
    print("====================================================================================")
    print("----------------------Automation Application by Navnath Jadhav----------------------")
    print("====================================================================================")

    
    print("Apllication  Name is : "+argv[0])
    
    if(len(argv) != 2):
        print("Error : Invalid Numbers of Arguments" )
        logg("Error : Invalid Numbers of Arguments")
        exit()
        
    if(argv[1] == "-h" )or( argv[1] == "-H"):
    
        print("HELP : automation script which accept process name and display information of that process if \
  it is running")
        logg("HELP : automation script which accept process name and display information of that process if \
  it is running")
        exit()
    
    
    if argv[1] in ("-u", "-U"):
        print("Usage: Application_name.py proccesname")
        logg("Usage: Application_name.py proccesname")
        exit()
        
    try:
       
        procinfo = Check(argv[1])
        
        if procinfo:
            print(f"Process {argv[1]} is running ....")
            logg(f"Process {argv[1]} is running ....")
            print("Info is : \n")
            logg("Info is : \n")
            for info in procinfo:
                print(info)
                logg(str(info))
            
        else:
            print(f"No running process found with the name: {argv[1]}")
            logg(f"No running process found with the name: {argv[1]}")

        
        
    except ValueError as v:
        print("Error: Value Error "+v)
        logg(v)
    
    except Exception as e:
        logg(f"Error: Exception occurred ({e})")
        print(f"Error: {e}")
        
          
if __name__ == "__main__":
    main()
    

