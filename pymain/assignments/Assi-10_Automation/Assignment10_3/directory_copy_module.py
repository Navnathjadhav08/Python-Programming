
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

def copy_files(src_dir, dst_dir):
    
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        
        logging.info(f"Destination directory '{dst_dir}' created.")

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dst_dir, item)
        
        if os.path.isfile(src_path):
            shutil.copy2(src_path, dst_path)
            logging.info(f"Copied: {src_path} to {dst_path}")
            
        elif os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path)
            logging.info(f"Copied directory: {src_path} to {dst_path}")

