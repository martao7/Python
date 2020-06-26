'''Zadanie 2

Zapoznaj się z modułem random.
 import random

Stwórz prostą grę zgadywankę.
Komputer losuje wartość z przedziału od 1-30.
Poproś użytkownika o zgadnięcie liczby.
Program pyta użytkownika o podanie liczby tak długo, dopóki gracz nie zgadnie.
'''

import random

number = random.randrange (1, 30)

guess = int(input('Jaka to liczba (1 - 30)? '))
while guess != number:
    print('to nie jest ta liczba!')
    guess = int(input('Podaj liczbe: '))

print('Zgadles! Ta liczba to ', number)