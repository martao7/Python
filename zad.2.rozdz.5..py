# program Kreator postaci do gry z podzialem na role
# gracz otrzymuje pule 30 pkt
# ktore moze spozytkowac na 4 atrybuty:
# sila, zdrowie, madrosc i zrecznosc
# gracz moze przeznaczac pkt z puli na dowolny atrybut
# moze tez odbierac pkt przypisane do atrybutu
# i przekazywac je z powrotem do puli

ATTR       = (['power'],
              ['healthy'],
              ['wisdom'],
              [ 'agility'])

power = ATTR[0]
healthy = ATTR[1]
wisdom = ATTR[2]
agility = ATTR[3]

inventory = []
total = int(30)
choice = None

while choice != '0':
    print('''  -Kreator postaci-

    0 - zakoncz program
    1 - pokaz liste atrybutow
    2 - dodaj atrybut
    3 - usun atrybut
    4 - pokaz atrybuty postaci

''')

    choice = input('\nWybierasz: ')
    print()

    # zakoncz program
    if choice == '0':
        print('\nGame over.')
    # wypisz liste atrybutow do wyboru
    elif choice == '1':
        attribut = ['power','healthy','wisdom','agility']
        print('Atrybuty:')
        for item in attribut:
            print(item)
    # dodaj atrybut
    elif choice == '2' and total != 0:
        print(ATTR)
        odp = int(input('Jaki atrybut chcesz dodac? (wpisz od 0 do 3'))
        print ('Wybierasz atrybut: ', ATTR[odp])
        points = int(input('Ile pkt atrybutu chcesz dodac?'))

        if odp == 0:
            power.append(int(points))
            total -= int(points)
            print(power, 'masz jeszcze: ', total, 'pkt')
            input ('Aby kontynuowac wcisnij Enter.')
        elif odp == 1:
            healthy.append(int(points))
            total -= int(points)
            print(healthy, 'masz jeszcze: ', total, 'pkt')
            input('Aby kontynuowac wcisnij Enter.')
        elif odp == 2:
            wisdom.append(int(points))
            total -= int(points)
            print(wisdom, 'masz jeszcze: ', total, 'pkt')
            input('Aby kontynuowac wcisnij Enter.')
        elif odp == 3:
            agility.append(int(points))
            total -= int(points)
            print(agility, 'masz jeszcze: ', total, 'pkt')
            input('Aby kontynuowac wcisnij Enter.')
        else:
            print ('Nie ma takiego atrybutu.')

        print ('\nTwoj aktualny inwentarz to: ', inventory)


    # usun atrybut
    elif choice == '3':
        print (ATTR)
        odp = int(input('Jaki atrybut chcesz usunac? (wpisz od 0 do 3'))
        print('Wybierasz atrybut: ', ATTR[odp])
        points = int(input('Ile pkt atrybutu chcesz odjac?'))
        if odp == 0 and points in power:
           power.remove(points)
           total += points
           print('Masz jeszcze do dyspozycji ', total, 'pkt.')
           input ('Aby kontynuowac wcisnij Enter.')
        elif odp == 1 and points in healthy:
           healthy.remove(points)
           total += points
           print('Masz jeszcze do dyspozycji ', total, 'pkt.')
           input ('Aby kontynuowac wcisnij Enter.')
        elif odp == 2 and points in wisdom:
           wisdom.remove(points)
           total += points
           print('Masz jeszcze do dyspozycji ', total, 'pkt.')
           input ('Aby kontynuowac wcisnij Enter.')
        elif odp == 3 and points in agility:
           agility.remove(points)
           total += points
           print('Masz jeszcze do dyspozycji ', total, 'pkt.')
           input ('Aby kontynuowac wcisnij Enter.')
        else:
           print('Nie ma takiego atrybutu na Twojej liscie.')

    # posortuj posiadane atrybuty postaci
    elif choice == '4':
        inventory.sort(reverse=True)

    # nieznana opcja
    else:
        print('\nNiestety', choice, 'nie ma takiej opcji.')

    input('\nAby kontynuowac wcisnij Enter.')







