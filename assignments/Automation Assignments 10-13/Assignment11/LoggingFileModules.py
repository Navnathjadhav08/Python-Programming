import time
import os

def logging(msg):
    separator = "-" * 80
    log_filename = "DirectoryFileChecksum_%s.log" % time.strftime("%Y%m%d-%H%M%S")
    log_path = os.path.join(log_filename)

    try:
        with open(log_path, "a") as fobj:  # Change "w" to "a" for append mode
            fobj.write(separator + "\n")
            fobj.write("DirectoryFile Checksum Logger: " + time.ctime() + "\n")
            fobj.write(separator + "\n")
            fobj.write(msg + " : " + time.ctime() + "\n")
    except IOError as e:
        print(f"Error: Unable to write to log file. {e}")
