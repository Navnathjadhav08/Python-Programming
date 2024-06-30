# file_utils.py

import os
import hashlib

def calculate_file_hash(file_path, block_size=65536):
    """Calculate MD5 hash of the file for comparison."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(block_size), b""):
            hash_md5.update(block)
    return hash_md5.hexdigest()

def find_duplicates(directory):
    """Find and return duplicate files in the given directory."""
    file_hashes = {}
    duplicates = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)
            if file_hash in file_hashes:
                duplicates.append(file_path)
            else:
                file_hashes[file_hash] = file_path

    return duplicates

def delete_files(files):
    """Delete the given list of files."""
    for file in files:
        try:
            os.remove(file)
        except Exception as e:
            raise Exception(f"Error deleting file {file}: {e}")
