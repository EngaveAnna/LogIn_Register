# Managing Data Base
# Creating and Deleting Tables

import sqlite3

# Create a database in RAM
db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('database.db')

cursor = db.cursor()


# Delete table
def drop_table():
    cursor.execute('''DROP TABLE users''')

    print('Table deleted')
    db.commit()

# Create table
def create_table():
    cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                    surname TEXT, email TEXT UNIQUE, nip NUMBERS(10), password TEXT, 
                    confirmed BOOLEAN DEFAULT(0), confirmation_sent DATETIME, confirmed_on DATETIME)''')

    print('Table created')
    db.commit()

# Delete user from table
def delete_user_from_table(id):
    cursor.execute('''DELETE FROM users WHERE id = ? ''', (id,))
    db.commit()

    print("user deleted")


#delete_user_from_table('8')

#drop_table()
#create_table()

db.close()