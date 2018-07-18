# Sending mail and mail body templates
# Testing mails are send from my private gmail account
# Trzeba podac dane do logowania zeby kod dzialal

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Send mail with veryficaton token
def send_email(email, body, subject):    
    fromaddr = "mail@gmail.com"
    toaddr = "mail@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    #msg['To'] = email
    msg['To'] = toaddr
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "password_to_gmail_account")
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