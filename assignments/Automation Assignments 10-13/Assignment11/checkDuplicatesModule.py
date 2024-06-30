from hashfile import hashfile
from LoggingFileModules import logging

import os

def  checkDup(sums):
    # Step 1: Invert the dictionary
    inverted_dict = {}
    for filepath, checksum in sums.items():
        if checksum in inverted_dict:
            inverted_dict[checksum].append(filepath)
        else:
            inverted_dict[checksum] = [filepath]

    # Initialize an empty dictionary to store duplicates
    duplicates = {}

    # Iterate through the inverted dictionary
    for checksum, paths in inverted_dict.items():
        # Check if there are multiple file paths for the same checksum
        if len(paths) > 1:
            # If there are, add this checksum and its associated paths to the duplicates dictionary
            duplicates[checksum] = paths
    # Output the duplicates
    for checksum, paths in duplicates.items():
        logging(f"Checksum: {checksum} has the following duplicate files: {paths}")
       
       
    return duplicates


def printDuplicate(dict1):
    results = list(filter(lambda x:len(x)>1,dict1.values()))
    
    if len(results)> 0:
        logging("Diplicate Found:")
        
        logging("The Following files are identical.")
        
        inct = 0;
        for result in results:
            for subresult in result:
                icnt +=1
                if icnt >= 2:
                    logging('\t\t%s'%subresult)
                else:
                    logging("No duplicate files found")