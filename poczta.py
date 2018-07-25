# TESTOWY PLIK

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

fromaddr = "Kajetan.Dreliszak@engave.pl"
toaddr = "Kajetan.Dreliszak@engave.pl"
msg = MIMEMultipart()
msg['From'] = fromaddr
#msg['To'] = email
msg['To'] = toaddr
msg['Subject'] = 'subject'

msg.attach(MIMEText('body', 'plain'))

server = smtplib.SMTP('smtp.engave.pl', 587)
server.starttls()
server.login(fromaddr, "haslo")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

print("Email send")