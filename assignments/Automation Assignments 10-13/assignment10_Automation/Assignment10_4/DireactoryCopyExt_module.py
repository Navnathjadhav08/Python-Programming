import os
import shutil
import logging

def validate_directories(src_dir, dst_dir):
    if not os.path.exists(src_dir):
        raise ValueError(f"Source directory '{src_dir}' does not exist.")
    
    if not os.path.isdir(src_dir):
        raise ValueError(f"Source directory '{src_dir}' is not a directory.")
    
    if os.path.exists(dst_dir) and not os.path.isdir(dst_dir):
        raise ValueError(f"Destination path '{dst_dir}' exists and is not a directory.")

def copy_files_with_extension(src_dir, dst_dir, file_extension):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        logging.info(f"Destination directory '{dst_dir}' created.")
    
    # Ensure the file extension starts with a dot
    if not file_extension.startswith('.'):
        file_extension = '.' + file_extension

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dst_dir, item)
        
        if os.path.isfile(src_path) and src_path.endswith(file_extension):
            shutil.copy2(src_path, dst_path)
            logging.info(f"Copied: {src_path} to {dst_path}")

