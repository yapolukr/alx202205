dzalania ={
	'+':lambda x,y: x+y,
	'-':lambda x,y: x-y,
	'*':lambda x,y: x*y,
	'/':lambda x,y: x/y
	'^':lambda x,y: x**y
}

x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))
op = input('Podaj rodzaj operacji: ')

if op not in dzalania:
	print("Nie znana operacja", op)
else:
	wynik = dzalania[op](x, y)
	print('Wynik:', wynik)
