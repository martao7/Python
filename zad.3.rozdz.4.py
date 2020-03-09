# popraw program wymieszane litery
# kazdemu slowu ma towarzyszyc podpowiedz, jesli gracz utknie w martwym punkcie
# dodaj system punktacji nagradzajacy,jesli odp bez podpowiedzi

import random

WORDS = ('rezept', 'schinken', 'butter', 'plätzchen', 'pommes')

word = random.choice (WORDS)

correct = word

jumble = ''

while word:
    
   position = random.randrange(len(word))

   jumble += word[position]

   word = word[:position] + word[(position + 1):]

print('''

         das Spiel -Gemischte Buchstaben-  Viel Spaß!
     '''  )

print ('\nRate, was für Wort das ist: ', jumble)
odp = input ('\nDeine Antwort: ')

point_counter = 0
podp_counter = 0

    
while odp != correct and odp != '':
    print ('Leider nicht.')
    podp = input ('Brauchst du Hilfe? yes/no: ')
    if podp == 'yes'and WORDS == [0]:
          print ('nach ... backt man ein Kuchen')
    elif podp == 'yes' and WORDS == [1]:
          print ('toast mit ... und käse')
    elif podp == 'yes' and WORDS == [2]:
          print ('man schmiert damit Brot')
    elif podp == 'yes' and WORDS == [3]:
          print ('weihnachtsgebäck')
    elif podp == 'yes' and WORDS == [4]:
          print ('man isst die mit ketchup')
    
    podp_counter += 1
    odp = input('Deine Antwort: ')

    if odp == correct:
        print ('\nRichtige Antwort! Congratulations!')
        break

    elif podp == correct and podp == 0:
        point_counter += 1
        print ('\nRichtige Antwort! Du bekommst 1 Punkt.')
        break
      
input ('\nUm es zu beenden drücke mal den Enter.')
