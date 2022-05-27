class Konto:
    def __init__(self, numer, wlasciciel, saldo=0):
        self.numer = numer
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def wplata(self, wplata):
        if wplata <= 0:
            raise ValueError('Uemna kwota')
        else:
            self.saldo = self.saldo + wplata


    def wyplata(self, wyplata):

        if wyplata
        if wyplata > self.saldo:
            print("Nie ")
        else:
            self.saldo = self.saldo - wyplata
    

gdfgdfgfdggh


