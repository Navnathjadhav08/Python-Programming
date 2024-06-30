import urllib.request
import smtplib

import time

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib.request.urlopen('https://www.wikipedia.org/',timeout=1) 
        return True
    except urllib2.URLError as err:
        return False
    
    
def MailSender(filename,timme,toaddr = ""):
    try:
        starttime = time.time()
        fromaddr = "navnathjadhav0789@gmail.com"
        if toaddr == "":
            toaddr = "nj618021@gmail.com"
            
        
        
        msg = MIMEMultipart()
        
        msg['From'] = fromaddr
        msg['To'] = toaddr
        
        body = """
        Hello %s,
        
        Welcome To Softnath Pvt Limited,
        please Find attached Document Which contains Log of Running process.
        
        
        Log file is created at : %s
        
        
        ---------------This is auto gennerated mail------------------------->
        
        Thanks & Regards,
        Navnath Jadhav
        Softnath Pvt Limited
        """%(toaddr,timme)
        
        Subject = """
        System Process Log Generated at : %s
        """%(timme)
        
        msg['Subject'] = Subject
        
        msg.attach(MIMEText(body,'plain'))
        
        attachment = open(filename,"rb")
        
        p = MIMEBase('application','octet-stream')
        
        p.set_payload((attachment).read())
        
        encoders.encode_base64(p)
        
        p.add_header('Content-Disposition',"attachment;filename=%s"%filename)
        
        msg.attach(p)
        
        s = smtplib.SMTP('smtp.gmail.com',587)
        
        s.starttls()
        
        s.login(fromaddr,"wkqe htem jllg carl")
        
        text = msg.as_string()
        
        s.sendmail(fromaddr,toaddr,text)
        
        s.quit()
        
        endtime = time.time()
       
        
        print("Log file successfully sent through Mail \n Time taken to send mail is %s"%(endtime - starttime))
        
        
    except Exception as E:
        
        print("Unable to send mail.",E)
                
        