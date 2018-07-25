# Logging in and attemts to log in

import sqlite3
from user_class import User
import config_data

# Creates or opens a file called mydb with a SQLite3 DB
db = config_data.db
cursor = db.cursor()

# Give data to log in maually for testing purposes
def manual_log_in():
    email = input("Enter your email: ")
    given_pwd = input("Enter your password: ")
    logging_data(email, given_pwd)

# Logging in process
def logging_data(email, given_pwd, attempts=2):

    for a in range(attempts, -1, -1):
        cursor.execute('''SELECT password, confirmed FROM users WHERE email = ?''', (email,))
        temp = cursor.fetchone()

        if temp:
            User.email = email
            User.password = temp[0]
            confirmed = int(temp[1])
            # Checking if the password is correct and the user is confirmed
            if confirmed and given_pwd == User.password: 
                print("Correct password")
                break
            elif a>0:
                email, given_pwd = wrong_data(a)
            
        elif a>0:
            email, given_pwd = wrong_data(a)

    else: print("Account blocked")

# Informations about wrong data and getting new one
def wrong_data(attempts):
    print("--------------------------")
    print("Incorrect email or password")
    print('%d attempts left' % (attempts))
    email = input("Enter your email: ")
    given_pwd = input("Enter your password: ")

    return email, given_pwd


manual_log_in()
#logging_data("mai3@mail.com", "haslo")

db.close()