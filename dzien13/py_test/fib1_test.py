9# W tej wersji funkcja, którą chcemy przetestować, oraz jej testy umieszczamy w jednym pliku.
# 0 1 1 2 3 5 8 13 21 34 55

import pytest

def fib(n):
   if n < 0:
       raise ValueError('Ujemny argument fib')
   if n <= 1:
       return n
   return fib(n-1) + fib(n-2)


def test_fib_0():
   assert fib(0) == 0

def test_fib_1():
   assert fib(1) == 1

def test_fib_5():
   assert fib(8) == 21



def test_fib_ujemna():
   # ma dojść do takiego wyjątku
   with pytest.raises(ValueError):
       fib(-1)


a = 1234
for i in range(2, 23):
    pass