# config file with all sensitive data
from litex.regon import REGONAPI
import sqlite3

# data to connnect and login to regon api
regon_api_url = REGONAPI('https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc')
regon_api_login = 'abcde12345abcde12345'

# names of table in data base
table_names = ['users', 'firma_platnik', 'firma_zamawiajaca', 'firma_realizujaca']

# expiration time of the auth token in sec
expiration = 10

# data base connection
db = sqlite3.connect('database.db')

# email sever, login and password
server = 'smtp.gmail.com'
fromaddr = "mail@gmail.com"
password = "haslo"