import hashlib
from .logging_module import logging

def hashfile(path, blocksize=1024):
    try:
        with open(path, 'rb') as fd:
            hasher = hashlib.md5()
            buf = fd.read(blocksize)
            while len(buf) > 0:
                hasher.update(buf)
                buf = fd.read(blocksize)
        return hasher.hexdigest()
    except FileNotFoundError:
        logging(f"Error: File '{path}' not found.")
        return None
    except Exception as e:
        logging(f"Error opening file: {e}")
        return None
