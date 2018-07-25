# Getting data from REGON api and then printing then, finally tehy will be sent to front-end
import config_data

# getting data from REGON and putting them into class
class Regon:

    def __init__(self, nip):

        # data to testing environment
        api = config_data.regon_api_url
        api.login(config_data.regon_api_login)

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
