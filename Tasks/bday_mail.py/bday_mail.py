"""
   This automation script which accept CSV file which contains email ids and users birth date and  send the mail to the user which contains
   Greeting 
     After creating log file send that log file to the specified mail. 
    
 Usage : bday_mail.py dob.csv xyz@gmail.com 
 
dob.csv is name of Directory/file. 

xyz@gmail.com is the mail id.

"""

import sys
import time
from modules.create_log import logg
from modules.sendMail_Module import is_connected, MailSender
from modules.scheduleModule import schedulefun
from modules.read_csv import dob

def main():
    print("====================================================================================")
    print("----------------------Automation Application by Navnath Jadhav----------------------")
    print("====================================================================================")

    print("Application Name is : " + sys.argv[0])

    if len(sys.argv) != 3:
        error_message = "Error: Invalid Number of Arguments"
        print(error_message)
        logg(error_message)
        sys.exit()

    if sys.argv[1] in ("-h", "-H"):
        help_message = """This automation script accepts a CSV file containing email IDs and users' birth dates and sends a greeting email to the user on their birthday.
After creating the log file, send that log file to the specified email."""
        print(help_message)
        logg(help_message)
        sys.exit()

    if sys.argv[1] in ("-u", "-U"):
        usage_message = """Usage: bday_mail.py dob.csv xyz@gmail.com

dob.csv is the name of the directory/file.
xyz@gmail.com is the email ID."""
        print(usage_message)
        logg(usage_message)
        sys.exit()

    try:
        print("....Checking Connection......")
        if is_connected():
            print("Connected..........")
            print("Sending Mail......")

            interval_type = "daily"
            at_time = "13:48:55"

            schedulefun(logg, dob, MailSender, sys.argv[1], interval_type, at_time, sys.argv[2])
        else:
            error_message = "Unable to Connect"
            print(error_message)
            logg(error_message)
    except ValueError as v:
        error_message = f"Error: Value Error {v}"
        print(error_message)
        logg(error_message)
    except Exception as e:
        error_message = f"Error: Exception occurred in main: {e}"
        print(error_message)
        logg(error_message)

if __name__ == "__main__":
    main()
