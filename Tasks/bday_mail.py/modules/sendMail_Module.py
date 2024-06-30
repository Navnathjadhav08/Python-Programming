import urllib.request
import smtplib
import time
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib.request.urlopen('https://www.wikipedia.org/', timeout=1)
        return True
    except Exception as err:
        return False

def MailSender(to_email, subject, body, log_file_path=None, toaddr=""):
    try:
        starttime = time.time()
        fromaddr = "navnathjadhav0789@gmail.com"
        password = "wkqe htem jllg carl"
        
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        if log_file_path:
            with open(log_file_path, "rb") as attachment:
                p = MIMEBase('application', 'octet-stream')
                p.set_payload(attachment.read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', f"attachment; filename= {log_file_path}")
                msg.attach(p)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, to_email, text)
        server.quit()
        
        endtime = time.time()
        print(f"Log file successfully sent through Mail. Time taken to send mail is {endtime - starttime} seconds")

    except Exception as e:
        error_message = f"Error in MailSender: Unable to send mail ({e})"
        print(error_message)
        logg(error_message)
