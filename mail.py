# Sending mail and mail body templates
# Testing mails are send from my private gmail account
# Trzeba podac dane do logowania zeby kod dzialal

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config_data

# Send mail with veryficaton token
def send_email(email, body, subject):    
    fromaddr = config_data.fromaddr
    toaddr = email
    #toaddr = "kajetan.dre@gmail.com"
    
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP(config_data.server, 587)
    server.starttls()
    server.login(fromaddr, config_data.password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    print('Email send')

def template_veryfication(token, link):
    body = 'Witaj,\noto Twoj token:\n' + token + '\nKliknij poniżej aby przejsc dalej:' + link
    subject = 'Veryfication mail'

    return (body, subject)

def template_pwd_recovery(password):
    body = 'Witaj,\nOto Twoje haslo: ' + password
    subject = 'Password recovery'

    return (body, subject)