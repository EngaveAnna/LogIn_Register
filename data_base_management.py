# Managing Data Base
# Creating and Deleting Tables
import config_data
import sqlite3

# Create a database in RAM
db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
db = config_data.db

cursor = db.cursor()


# Delete table
def drop_table(table_name):
    if not isinstance(table_name, str):
        for name in table_name:
            cursor.execute('''DROP TABLE {}'''.format(name))
    else:
        cursor.execute('''DROP TABLE {}'''.format(table_name))
    
    print('Table deleted')
    db.commit()


# Create table
def create_table(table_name):
    if not isinstance(table_name, str):
        for name in table_name:
            if 'users' == name:
                cursor.execute('''CREATE TABLE {}(id INTEGER PRIMARY KEY, name TEXT, surname TEXT, email TEXT UNIQUE, nip NUMBERS CHECK(length(nip)=10), 
                                password TEXT, confirmed BOOLEAN DEFAULT(0), confirmation_sent DATETIME, confirmed_on DATETIME)'''.format(name))
            else:
                cursor.execute('''CREATE TABLE {}(id INTEGER PRIMARY KEY, nip NUMBERS CHECK(length(nip)=10), regon INTEGER, name TEXT, wojewodztwo TEXT, 
                                powiat TEXT, gmina TEXT, miejscowosc TEXT, kod_pocztowy NUMBERS CHECK(length(kod_pocztowy)=6), ulica TEXT)'''.format(name))
    else:
        if 'users' == table_name:
            cursor.execute('''CREATE TABLE {}(id INTEGER PRIMARY KEY, name TEXT, surname TEXT, email TEXT UNIQUE, nip NUMBERS CHECK(length(nip)=10), 
                            password TEXT, confirmed BOOLEAN DEFAULT(0), confirmation_sent DATETIME, confirmed_on DATETIME)'''.format(table_name))
        else:
            cursor.execute('''CREATE TABLE {}(id INTEGER PRIMARY KEY, nip NUMBERS CHECK(length(nip)=10), regon INTEGER, name TEXT, wojewodztwo TEXT, 
                            powiat TEXT, gmina TEXT, miejscowosc TEXT, kod_pocztowy NUMBERS CHECK(length(kod_pocztowy)=6), ulica TEXT)'''.format(table_name))

    print('Table created')
    db.commit()


# Delete user from table
def delete_user_from_table(id):
    cursor.execute('''DELETE FROM users WHERE id = ? ''', (id,))
    db.commit()

    print("user deleted")


#delete_user_from_table('8')

try:
    drop_table(config_data.table_names[0:4])
except:
    create_table(config_data.table_names[0:4])

db.close()