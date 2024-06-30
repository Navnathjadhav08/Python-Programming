import time

def logg(log_entries):
    fname = 'email_log.txt'

    with open(fname, 'w') as log_file:
        log_file.write("-" * 80 + "\n")
        log_file.write(f"Logger: {time.ctime()}\n")
        log_file.write("-" * 80 + "\n")
        if isinstance(log_entries, list):
            for entry in log_entries:
                log_file.write(entry + '\n')
        else:
            log_file.write(log_entries + '\n')
