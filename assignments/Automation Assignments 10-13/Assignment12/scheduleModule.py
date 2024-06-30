import schedule
import time
import threading
from datetime import datetime, timedelta

def schedulefun(log_fun,mail_func,interval='daily', at_time='10:00',log_Dir = "demo", mail="nj618021@gmail.com"):
    
    """
    Schedule a job function to run at specified intervals.
    
    Parameters:
    job_func (function): The function to be scheduled.
    interval (str): Interval type (e.g., 'seconds', 'minutes', 'hours', 'days', 'daily', 'weekly').
    at_time (str): Specific time for 'daily' and 'weekly' intervals (e.g., '10:00', 'Monday 10:00').
    *args: Arguments to be passed to the job function.
    """
    
    def job_func():
        try:
            t = time.ctime()
            fname = log_fun((f"log created at {t}"),log_Dir)
            mail_func(fname,str(t),mail)
            
        except Exception as e:
            print(f"Error: Exception occurred ({e})")
            log_fun(f"Error: Exception occurred ({e})")
    
    if interval == 'seconds':
        schedule.every(int(at_time)).seconds.do(job_func)
    elif interval == 'minutes':
        schedule.every(int(at_time)).minutes.do(job_func)
    elif interval == 'hours':
        schedule.every(int(at_time)).hours.do(job_func)
    elif interval == 'days':
        schedule.every(int(at_time)).days.do(job_func)
    elif interval == 'daily':
        schedule.every().day.at(at_time).do(job_func)
    elif interval == 'weekly':
        schedule.every().week.at(at_time).do(job_func)
    else:
        print(f"Error: Unknown interval type {interval}")
    

    def calculate_next_run_time():
        next_run = schedule.next_run()
        now = datetime.now()
        remaining_time = next_run - now
        return remaining_time

    def countdown_timer():
        while True:
            remaining_time = calculate_next_run_time()
            if remaining_time.total_seconds() > 0:
                print(f"Next mail will be sent in: {remaining_time}")
            else:
                print("Mail is being sent...")
            time.sleep(1)

    # Start the countdown timer in a separate thread
    timer_thread = threading.Thread(target=countdown_timer)
    timer_thread.daemon = True
    timer_thread.start()
    
    while True:
        schedule.run_pending()
        time.sleep(1)
