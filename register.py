import sqlite3
from itsdangerous import TimedSerializer, BadSignature
import time #only for sleep method not needed in final code
from nipy import Regon
from user_class import User
import mail
import auth
from datetime import datetime

# Amount of time when the token is valid in [s]
expiration = 1

# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('database.db')

cursor = db.cursor()


# Insert user to table
def insert_user_into_table():
    cursor.execute('''INSERT INTO users(name, surname, email, password, nip) VALUES(?,?,?,?,?)''', 
                  (user.name.lower(), user.surname.lower(), user.email.lower(), user.password, user.nip))
    db.commit()

    print('User inserted into table')

# Answer questions about user data only for testing purposes
def manual_register():
    user.name = input("Eneter your name: ")
    user.surname = input("Enter your surname: ")
    user.email = input("Enter your email: ")
    user.nip = input("Enter your nip: ")
    user.password = input("Enter your password: ")

    register_user()

# Register user
def register_user():
    insert_user_into_table()
    
    token = auth.generate_token(user.password, user.email)

    # Send mail with veryficaton token (link from front-end)
    link = '\nhttps://pythonhosted.org/itsdangerous/#itsdangerous.TimestampSigner'
    body, subject = mail.template_veryfication(token, link)
    mail.send_email(user.email, body, subject)

    cursor.execute('''UPDATE users SET confirmation_sent = ? where email = ?''', (datetime.now(), user.email))
    db.commit()

    # Artificial waiting for confirmation-------
    time.sleep(2)
    #-------------------------------

    (confirmed, token_email) = auth.confirm_token(token, expiration, user.password)
    if confirmed:
        user_confirmed(token_email)
        print("User registered")
        get_data_from_REGON(user.nip)
    else:
        print('User not registered')

# Setting user value CONFIRM to True
def user_confirmed(email):
    cursor.execute('''UPDATE users SET confirmed = 1 where email = ?''', (email,))
    cursor.execute('''UPDATE users SET confirmed_on = ? where email = ?''', (datetime.now(), email))
    db.commit()

# Get data about the Company from REGON
def get_data_from_REGON(nip):
    Regon(nip).send()


#manual_register()
user = User("A", "H", "mail3", '8671154898', "haslo2")
register_user()

#get_data_from_REGON('8671154898')

#token = 'hejka'
#mail.send_verify_email(token)

db.close()

