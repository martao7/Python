# program Kreator postaci do gry z podzialem na role
# gracz otrzymuje pule 30 pkt
# ktore moze spozytkowac na 4 atrybuty:
# sila, zdrowie, madrosc i zrecznosc
# gracz moze przeznaczac pkt z puli na dowolny atrybut
# moze tez odbierac pkt przypisane do atrybutu
# i przekazywac je z powrotem do puli

ATTRIBUTES = (['power'],
              ['healthy'],
              ['wisdom'],
              ['agility'])

power = ATTRIBUTES [0]
healthy = ATTRIBUTES [1]
wisdom = ATTRIBUTES [2]
agility = ATTRIBUTES [3]


print (
        '''      program -Kreator postaci-
''')

total = 30    
print ('Masz pule dostepnych ', total, 'pkt.')

print ('Do wyboru masz nastepujace atrybuty:')
for item in attributs:
    print (item)

    choice = input ('Wybierasz atrybut: ')
    print ()
    
  elif.choice == 'power':
      print('Otrzymujesz punkty sily.', power)
      points = int (input('\nIle punktow atrybutu chcesz dodac?'))
      power.append (int(points)
      total -= points
      print (power, 'pozostalo ci jeszcze ', total, 'pkt')
                  
elif choice == healthy:
    print('Otrzymujesz punkty zdrowia.', healthy)
    points = int (input('\nIle punktow atrybutu chcesz dodac?'))
    healthy.append (int(points)
    total -= points
    print (healthy, 'pozostalo ci jeszcze ', total, 'pkt')
   
elif choice == wisdom:
    print('Otrzymujesz punkty madrosci.', wisdom)
    points = int (input('\nIle punktow atrybutu chcesz dodac?'))
    wisdom.append (int(points)
    total -= points
    print (wisdom, 'pozostalo ci jeszcze ', total, 'pkt')

elif choice == agility:
    print('Otrzymujesz punkty zrecznosci.', agility)
    points = int (input('\nIle punktow atrybutu chcesz dodac?'))
    agility.append (int(points)
    total -= points
    print (agility, 'pozostalo ci jeszcze ', total, 'pkt')   


