class Klasa:
   # W Pythonie, podobnie jak w C++ czy Javie, można deklarować atrybuty w ciele klasy (a nie w init).
   # Jednak w Pythonie działa to w sposób specyficzny, nieoczywisty.
   # Te zmienne są przechowywane w klasie, a nie w obiekcie, a obiekty mają do nich dostęp.
   # Jednak zapisanie atrybutu o tej samej nazwie w obiekcie (poprzez self) przesłania definicję z poziomu klasy.

   x = 100
   s = 'Ala ma kota'
   lista = []

   def __init__(self, y):
       self.y = y

   def __str__(self):
       return f'x = {self.x} , y = {self.y}, s = {self.s}, lista: {self.lista}'

   def dodajZwierze(self, zwierze):
       self.s += f' oraz {zwierze}'


a = Klasa(1)
print('a:', a)

b = Klasa(2)
print('b:', b)
print()

print("x z różnych perspektyw:")
print(a.x)
print(b.x)
print(Klasa.x)
print()

# Tutaj operacja jest wykonywana na zmiennej klasy

