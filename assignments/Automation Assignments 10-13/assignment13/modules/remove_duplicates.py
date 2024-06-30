import os
from .logging_module import logging

def remove_duplicates(duplicates):
    logging("File deleting process started")
    deleted_count = 0
    for checksum, paths in duplicates.items():
        for path in paths[1:]:  # Keep the first file, delete the rest
            try:
                os.remove(path)
                logging(f"{path} is removed")
                deleted_count += 1
            except OSError as e:
                logging(f"Error deleting {path}: {e}")
    logging(f"{deleted_count} files are removed")
