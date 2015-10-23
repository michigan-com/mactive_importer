""" Primary email alert system for nol  """
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
from datetime import datetime

def send_email(msg):
    now = datetime.now()
    msg = MIMEText(msg)
    msg["From"] = "deathnotices@michigan.com"
    msg["To"] = 'mvarano@michigan.com' #', '.join(['neurosnap@gmail.com', 'mvarano@michigan.com', 'rwilliams@michigan.com'])
    msg["Subject"] = "Death Notice Feed for {}-{}-{}".format(now.year, now.month, now.day)
    try:
        p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
        p.communicate(msg.as_string())
        print("Successfully sent the mail\n ")
    except:
        print("Error sending email\n ")
        print(msg.as_string())