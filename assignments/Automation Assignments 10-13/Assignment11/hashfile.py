import hashlib
from LoggingFileModules import logging

def hashfile(path, blocksize=1024):
    try:
        fd = open(path, 'rb')
    except FileNotFoundError:
        logging(f"Error: File '{path}' not found.")
        return None
    except Exception as e:
        logging(f"Error opening file: {e}")
        return None
    
    hasher = hashlib.md5()
    buf = fd.read(blocksize)
    
    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)
        
    fd.close()
    
    return hasher.hexdigest()
