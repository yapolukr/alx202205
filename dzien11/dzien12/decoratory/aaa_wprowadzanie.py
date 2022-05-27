
def poczatek_i_koniec(f):
   def zmieniona_funkcja():
       print('POCZATEK')
       f()
       print('KONIEC')

   return zmieniona_funkcja


def powitaj():
   print('Witamy serdecznie')

print('Normalne powitaj:')
powitaj()
print()

zmienione_powitaj = poczatek_i_koniec(powitaj)
print('Zmienione powitaj:')
zmienione_powitaj()
print()





