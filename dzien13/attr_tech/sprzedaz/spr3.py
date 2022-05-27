from spredaz2_class import wczytaj_plik

lista = wczytaj_plik('spzedaz.csv')
print(len(lista))

suma = 0
for i in lista:
    if i.miasto == "Katowice":
        suma += i.cena * i.sztuk

print(suma)