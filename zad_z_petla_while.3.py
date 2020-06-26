'''
Zadanie 3
Rozszerz grę z punktu powyżej.
Gracz powinen otrzymać informację
czy jego liczba jest za duża czy za mała.

'''

import random

number = random.randrange (1, 30)

guess = int(input('Jaka to liczba (1 - 30)? '))
while guess != number:
    if guess > number:
        print('za duza!')
    if guess < number:
        print('za mala!')
    guess = int(input('Podaj liczbe: '))

print('Zgadles! Ta liczba to ', number)
