import time
import os

def logging(message, dir_path="logs"):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    log_filename = f"DuplicateFileRemoveLog_{time.strftime('%Y%m%d-%H%M%S')}.log"
    log_path = os.path.join(dir_path, log_filename)

    try:
        with open(log_path, "a") as fobj:
            fobj.write("-" * 80 + "\n")
            #fobj.write(f"Logger: {time.ctime()}\n")
            fobj.write("-" * 80 + "\n")
            fobj.write(f"{message} : {time.ctime()}\n")
        return log_path
    except IOError as e:
        print(f"Error: Unable to write to log file. {e}")
        return None
