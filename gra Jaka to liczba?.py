#gra 'jaka to liczba?'
#prezentuje zycie algorytmow do napisania programu

print ('\nWitaj w grze ``Jaka to liczba?``.')
print ('\nGra polega na zgadnieciu losowo wybranej liczby od 1 do 100.')
print ('Sprobuj ja odgadnac w jak najmniejszej liczbie prob.')

import random

#ustaw wartosci poczatkowe
number = random.randint (1, 100)
odp = int (input('Ta liczba to: '))
tries = 1

#petla zgadywania
while odp != number:
            if odp > number :
                print ('Za duza liczba.')
            else:
                print ('Za mala liczba.')
                
            odp = int (input ('Ta liczba to: '))
            tries += 1

print ('Zgadles! Gratulacje! Ta liczba to ', number)
print ('Do odgadniecia liczby potrzebowales tylko ', tries, 'prob!\n')

input ('\nAby zakonczyc wcisnij Enter.')
