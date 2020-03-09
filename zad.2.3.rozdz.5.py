# program Kreator postaci do gry z podzialem na role
# gracz otrzymuje pule 30 pkt
# ktore moze spozytkowac na 4 atrybuty:
# sila, zdrowie, madrosc i zrecznosc
# gracz moze przeznaczac pkt z puli na dowolny atrybut
# moze tez odbierac pkt przypisane do atrybutu
# i przekazywac je z powrotem do puli

attribut = ['power','healthy','wisdom','agility']
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
    elif choice == '2':
        print('power = 0, healthy = 1, wisdom = 2 , agility = 3')
        odp = int(input('Jaki atrybut chcesz dodac?'))
        if odp == 0:
            print (attribut[0])
            inventory += attribut[0]
        elif odp == 1:
            print (attribut[1])
            inventory += attribut[1]
        elif odp == 2:
            print (attribut[2])
            inventory += attribut[2]
        elif odp == 3:
            print (attribut[3])
            inventory += attribut[3]
        else:
            print ('Nie ma takiego atrybutu.')

        points = int(input('Ile pkt atrybutu chcesz dodac?'))
        print ('\nTwoj aktualny inwentarz to: ', inventory)
        total -= points
        print('Masz jeszcze do dyspozycji ', total, 'pkt.')

    # usun atrybut
    elif choice == '3':
        print ('power, healthy, wisdom, agility')
        inventory = print(input('Ktory atrybut chcesz usunac?'))
        if attribut in inventory:
           inventory.remove(attribut)
           points = int(input('Ile pkt atrybutu chcesz usunac?'))
           total += points
           print('Masz jeszcze do dyspozycji ', total, 'pkt.')
        else:
           print(attribut, 'nie ma takiego atrybutu na Twojej liscie.')

    # posortuj posiadane atrybuty postaci
    elif choice == '4':
        inventory.sort(reverse=True)

    # nieznana opcja
    else:
        print('\nNiestety', choice, 'nie ma takiej opcji.')

    input('\nAby kontynuowac wcisnij Enter.')







