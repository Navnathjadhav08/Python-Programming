#in this program we study concept of modules using importing sys module and comand line argv

import sys

print("THis is demonstration of comand line arguments")

for i in sys.argv:
    print(i)
    
print( '\n\nThe PYTHONPATH is', sys.path, '\n')
    
#while running program use command " python module_using_sys.py this is Arguments "