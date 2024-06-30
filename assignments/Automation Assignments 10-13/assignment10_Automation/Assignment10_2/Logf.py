

import os

def Log(message):
    
    if os.path.exists("logFile"):
        lobj = open("lfile.log","a")
        lobj.write(message + "\n")
        
    else:
        lobj = open("lfile.log","a")
        lobj.write(message + "\n")
        
        
import os

# def Log(message):
#     # Ensure the log file is appended to, not overwritten each time
#     with open("logfile.log", "a") as lobj:
#         lobj.write(message + "\n")
