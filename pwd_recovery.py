# Basic password recovery, sending enal wuth passsword on given email

import sqlite3
import mail


# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('database.db')

cursor = db.cursor()

def confirm_email(email):
    try:
        cursor.execute('''SELECT password, confirmed FROM users WHERE email = ?''', (email,))
        temp = cursor.fetchone()
        password = temp[0]
        confirmed = int(temp[1])
        if confirmed:
            send_password(email, password)
        else: raise Exception
    except:
        print('Wrong email')

def send_password(email, password):
    body, subject = mail.template_pwd_recovery(password)
    mail.send_email(email, body, subject)

# Written only for testing purposes
# Variable email wil be given by fron-end
confirm_email('mail2')