'''Zadanie 4
Napisz skrypt obliczający wartość silnii.
Rozwiąż zadanie za pomocą pętli for oraz pętli while.
Wejście: „Podaj dowolną liczbę całkowitą do 15:” 4
Wyjście: 4! = 24
'''


n = int (input('Podaj dowolna liczbe calkowita do 15:'))

i = 1
silnia = 1
while i != n:
    i = i + 1
    silnia = silnia * i

print (str(n)+'! = ' + str(silnia))

