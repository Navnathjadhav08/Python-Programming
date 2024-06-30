import os
from DisplayProcessesModule import DisplayProc1
import time

def logg(msg,log_Dir = "softnath"):
    
    if not os.path.exists(log_Dir):
        try:
            os.mkdir(log_Dir)
        except:
            pass
        
    separator = "-" * 80
    log_filename = "RunningProcessinfo%s.log" % time.strftime("%Y%m%d-%H%M%S")
    log_path = os.path.join(log_Dir,log_filename)

    try:
        with open(log_path, "a") as fobj:  # Change "w" to "a" for append mode
            fobj.write(separator + "\n")
            fobj.write("Process info Logger: " + time.ctime() + "\n")
            fobj.write(separator + "\n")
            fobj.write(msg)
            procs = DisplayProc1()
            
            for p in procs:
                
                fobj.write("%s\n"%p)
            
    
          
    except IOError as e:
        print(f"Error: Unable to write to log file. {e}")
        
    return log_path
