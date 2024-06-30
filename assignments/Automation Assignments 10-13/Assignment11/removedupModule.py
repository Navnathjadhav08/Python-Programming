import os
from LoggingFileModules import logging
def removedup(dups):
    logging("File deleting process Started")
    deleted_count = 0
    for checksum, paths in dups.items():
        for path in paths:
            try:
                os.remove(path)
                logging(f"{path} is removed or deleted")
                deleted_count += 1
            except OSError as e:
                logging(f"Error deleting {path}: {e}")
    logging(f"{deleted_count} files are removed")