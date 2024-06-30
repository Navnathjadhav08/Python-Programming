import psutil

def Check(Process_name):
    
    process_list = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        try:
            if proc.info['name'] == Process_name:
                process_list.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_list