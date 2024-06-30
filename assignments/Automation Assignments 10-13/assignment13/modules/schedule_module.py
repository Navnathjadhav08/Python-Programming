import schedule
import time
from threading import Thread
from .display_checksum import calculate_checksums
from .check_duplicates import find_duplicates, log_duplicates
from .remove_duplicates import remove_duplicates
from .logging_module import logging
from .send_mail import send_log_via_mail

def perform_removal_task(directory, email):
    
    start_time = time.ctime()
    
    checksums = calculate_checksums(directory)
    
    total_scan = len(checksums)
    
    duplicates = find_duplicates(checksums)
    
    no_ofDup = len(duplicates)
    
    log_duplicates(duplicates)
    
    log_file = logging(f"Duplicate files: {duplicates}")
    
 
    remove_duplicates(duplicates)
    
    end_time = time.ctime()
    logging(f"start time : {start_time} \nNumber of files scan : {total_scan}\n Number of Duplicate Found : {no_ofDup}\n End time : {end_time} \n \
      Thank You for Using Our Script\n\
        Regards,\n\
        Navnath Jadhav\n\
        Softnath Pvt Limited\n")
    
    send_log_via_mail(log_file, start_time,total_scan,no_ofDup, email)

def schedule_removal(directory, interval, email):
   
    schedule.every(interval).minutes.do(perform_removal_task, directory=directory, email=email)
    
    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    scheduler_thread = Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()
    
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")
