import schedule
import time

def schedulefun(log_fun, dob_func, mail_func, csv_file, interval='daily', at_time='10:00', mail=""):
    def job_func():
        try:
            t = time.ctime()
            log_file_path = 'email_log.txt'
            body = f"""
            Hello {mail},

            Welcome To Softnath Pvt Limited,
            please find attached the document which contains the log of the running process.

            Log file is created at: {t}

            ---------------This is an auto-generated mail-------------------------

            Thanks & Regards,
            Navnath Jadhav
            Softnath Pvt Limited
            """
            dob_func(csv_file)
            mail_func(mail, f"Sent email Log Generated at: {t}", body, log_file_path)
        except Exception as e:
            error_message = f"Error in schedulefun job_func: Exception occurred ({e})"
            print(error_message)
            log_fun(error_message)

    try:
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
            error_message = f"Error in schedulefun: Unknown interval type {interval}"
            print(error_message)
            log_fun(error_message)

        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        error_message = f"Error in schedulefun: Exception occurred ({e})"
        print(error_message)
        log_fun(error_message)
