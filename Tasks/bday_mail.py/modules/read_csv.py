import csv
from datetime import datetime
from modules.sendMail_Module import MailSender
from modules.create_log import logg

def dob(csv_file):
    log_entries = []

    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    email = row['email']
                    birthdate = datetime.strptime(row['birthdate'], '%d-%m-%Y')

                    today = datetime.today()
                    if birthdate.month == today.month and birthdate.day == today.day:
                        subject = "Happy Birthday!"
                        body = f"Dear,\n\nWishing you a very Happy Birthday!\n\nBest regards,\nNavnath Jadhav"

                        MailSender(email, subject, body)

                        log_entries.append(f"Sent birthday email to {email} on {today.strftime('%Y-%m-%d')}")
                except KeyError as ke:
                    error_message = f"KeyError in dob function: Missing column in CSV file - {ke}"
                    print(error_message)
                    logg(error_message)
                except Exception as e:
                    error_message = f"Error in dob function: Exception occurred while processing row - {e}"
                    print(error_message)
                    logg(error_message)
    except Exception as e:
        error_message = f"Error in dob function: Exception occurred while reading CSV file - {e}"
        print(error_message)
        logg(error_message)

    logg(log_entries)
