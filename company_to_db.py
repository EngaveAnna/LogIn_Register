# Putting comapany data from forms into data base
import sqlite3
import config_data


db = config_data.db
cursor = db.cursor()

def insert_user_into_table(table_name, nip, regon, name, woj, powiat, gmina, miejscowosc, kod_pocztowy, ulica):
    cursor.execute('''INSERT INTO {}(nip, regon, name, wojewodztwo, powiat, gmina, miejscowosc, kod_pocztowy, ulica) VALUES(?,?,?,?,?,?,?,?,?)'''
                .format(table_name), (nip, regon,name, woj, powiat, gmina, miejscowosc, kod_pocztowy, ulica))
    db.commit()

    print('Inserted into table')

try:
    insert_user_into_table('firma_platnik','8671154898','830405467','Monika XXXXXXXX - P.P.H.U " Litex "','PODKARPACKIE','tarnobrzeski','Baranów Sandomierski','Suchorzów', '39-450','ul. Test-Wilcza')
except sqlite3.IntegrityError as e:
    print(e)
