# Getting data from REGON api and then printing then, finally tehy will be sent to front-end

from litex.regon import REGONAPI

# getting data from REGON and putting them into class
class Regon:

    def __init__(self, nip):

        # data to testing environment
        api = REGONAPI('https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc')
        api.login('abcde12345abcde12345')

        entities = api.search(nip=nip)

        self.regon = entities[0].Regon
        self.nazwa = entities[0].Nazwa
        self.wojewodztwo = entities[0].Wojewodztwo
        self.powiat = entities[0].Powiat
        self.gmina = entities[0].Gmina
        self.miejscowosc = entities[0].Miejscowosc
        self.kod_pocztow = entities[0].KodPocztowy
        self.ulica = entities[0].Ulica

        api.logout()

    def send(self):
        print(self.regon)
        print(self.nazwa)
        print(self.wojewodztwo)
        print(self.powiat)
        print(self.gmina)
        print(self.miejscowosc)
        print(self.ulica)
        print(self.kod_pocztow)
