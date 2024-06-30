import psutil
from LoggingModule import logg


def DisplayProc():
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            print(pinfo)
            logg(str(pinfo))
            
        except (psutil.NoSuchprocess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    
    
def DisplayProc1():
    listprocess = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
           # print(pinfo)
            listprocess.append(pinfo)
            
        except (psutil.NoSuchprocess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    
    return listprocess