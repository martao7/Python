# gra w ktorej komp wybiera losowo slowo
# gracz musi je odgadnac
# komp informuje gracza ile liter znajduje sie w wybranym slowie
# gracz dostaje 5 szans na zadanie pytania czy jakas litera jest zawarta w slowie
# komp odp tylko tak lub nie
# potem gracz musi odgadnac slowo

import random

WORDS = ('butter', 'schinken', 'brot')

word = random.choice (WORDS)

correct = word


print ('''                         das Wortspiel

          - rate, was für Wort habe ich versteckt -
       ''')
print ('\nDu hast die Möglichkeit zu fragen, ')
print ('welche Buchstaben befinden sich in diesem Wort')
print (' - ein tip: es geht immer ums essen :D ')

tries = 0

print ('\nDas Wort hat ' , len (word), 'Buchstaben.')

for litera in range (10):
      litera = input('Welcher Buchstabe möchtest du prüfen?')
      if litera in word:
       print ('yes')
      else:
       print ('no')
   

print ('Was meinst du, was für Wort ist das?')

odp = input ('\nDeine Antwort: ')

while odp !=correct and odp != '':
    print ('\nLeider nicht.')
    odp = input ('Deine Antwort: ')

if odp == correct:
    print ('\nDas ist das Wort! Congratultions!')



input ('\nUm es zu beenden, drucke Enter.')
