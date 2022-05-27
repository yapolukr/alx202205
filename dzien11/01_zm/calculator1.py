dzalania ={
	'+':lambda x,y: x+y,
	'-':lambda x,y: x-y,
	'*':lambda x,y: x*y,
	'/':lambda x,y: x/y
}

x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))
op = input('Podaj rodzaj operacji: ')

funk = dzalania[op]
wynik = funk(x, y)
print('Wynik:', wynik)
