def parzyste(l):
    liczba = 0
    while True:

        yield liczba
        liczba +=2
        if liczba > l:
            break



for x in parzyste(1000):
    print(x)




