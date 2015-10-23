""" Primary email alert system for nol  """
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
from datetime import datetime

def send_email(msg):
    now = datetime.now()
    msg = MIMEText(msg)
    msg["From"] = "deathnotices@michigan.com"
    # msg["To"] = ', '.join([])
    msg["Subject"] = "Death Notice Feed for {}-{}-{}".format(now.year, now.month, now.day)
    try:
        p = Popen(["/usr/sbin/sendmail", 'neurosnap@gmail.com', 'mvarano@michigan.com', 'rwilliams@michigan.com'], stdin=PIPE)
        p.communicate(bytes(msg.as_string(), 'utf-8'))
        print("Successfully sent the mail\n ")
    except Exception as e:
        print("Error sending email...")
        print(e)
        print(msg.as_string())

