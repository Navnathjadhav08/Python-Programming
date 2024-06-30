
"""
4.Design python application which creates three threads as small, capital, digits. All the 
threads accepts string as parameter. Small thread display number of small characters, 
capital thread display number of capital characters and digits thread display number of 
digits. Display id and name of each thread.
"""
import threading



def small_letters(string):
    thread_id = threading.get_ident()
    thread_name = threading.current_thread().name
    count = 0
    
    for char in string:
        if char.islower():
            count += 1
    print(f"Thread ID: {thread_id}, Name: {thread_name} - Number of small letters: {count}")

def capital_letters(string):
    thread_id = threading.get_ident()
    thread_name = threading.current_thread().name
    count = 0
    
    for char in string:
        if char.isupper():
            count += 1    
            
    print(f"Thread ID: {thread_id}, Name: {thread_name} - Number of capital letters: {count}")

def digits(string):
    thread_id = threading.get_ident()
    thread_name = threading.current_thread().name
    count = 0
    
    for char in string:
        if char.isdigit():
            count += 1    
    
    print(f"Thread ID: {thread_id}, Name: {thread_name} - Number of digits: {count}")

def main():
    input_string = input("Enter a string: ")

    t1 = threading.Thread(target=small_letters, args=(input_string,))
    t2 = threading.Thread(target=capital_letters, args=(input_string,))
    t3 = threading.Thread(target=digits, args=(input_string,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Main thread exiting")

    
    
        
        
if __name__ == "__main__":
    main()