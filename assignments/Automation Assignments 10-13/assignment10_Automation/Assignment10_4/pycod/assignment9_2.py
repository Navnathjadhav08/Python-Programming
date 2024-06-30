import hashlib

def hashfile(path, blocksize=1024):
    try:
        # Attempt to open the file
        fd = open(path, 'rb')
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except Exception as e:
        print(f"Error opening file: {e}")
        return None

    # Create the hash object
    hasher = hashlib.md5()
    
    # Read the first block
    buf = fd.read(blocksize)
    print(f"Initial buffer read (up to {blocksize} bytes): {buf}")

    while len(buf) > 0:
        hasher.update(buf)
        print(f"Updated hash with buffer: {buf}")
        buf = fd.read(blocksize)
        print(f"Next buffer read (up to {blocksize} bytes): {buf}")
    
    # Close the file
    fd.close()
    print("File closed.")

    # Return the hex digest of the hash
    hex_digest = hasher.hexdigest()
    print(f"Final hash (hex digest): {hex_digest}")
    return hex_digest
