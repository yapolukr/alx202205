# Gdy w funkcji zamiast return użyjemy operacji yield, to
#  - w wyniku powstaje "generator", który obrazowo działa tak, że
#  po zwróceniu wyniku, funkcja działa dalej i może zwrócić kolejne wyniki za pomocą kolejnych yield
def abc():
   yield 'Ala'
   yield 'Basia'
   yield 'Celina'


generator = abc()
print(generator)
# Generator jest iterowalny i najczęściej korzysta z niego porzez pętlę for
for x in generator:
   print(x)
print()


def cba():
   print('> 0')
   yield 'Celina'
   print('> 1')
   yield 'Basia'
   print('> 2')
   yield 'Ala'
   print('> 3')

print('Starujemy')
for x in cba():
   print(x)
   print('*')
print('Koniec\n')

# wszystkie wyniki na raz: rzutowanie na listę:
imiona = list(abc())
print(imiona)
print()
