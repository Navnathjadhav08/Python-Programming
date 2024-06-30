from .logging_module import logging

def find_duplicates(checksums):
    inverted_dict = {}
    for filepath, checksum in checksums.items():
        if checksum in inverted_dict:
            inverted_dict[checksum].append(filepath)
        else:
            inverted_dict[checksum] = [filepath]

    duplicates = {checksum: paths for checksum, paths in inverted_dict.items() if len(paths) > 1}
    return duplicates

def log_duplicates(duplicates):
    for checksum, paths in duplicates.items():
        logging(f"Duplicate files: {paths}")
