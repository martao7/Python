# inwentarz bohatera
# demonstruje listy

# utworz liste zawierajaca pewne elementy i wyswietl jej zawartosc
# za pomoca petli for

inventory = ['miecz', 'zbroja', 'tarcza', 'napoj uzdrawiajacy']
print ('elementy twojego inwentarza:')
for item in inventory:
    print (item)

# wyswietl dlugosc listy
print ('Twoj dobytek zawiera', len (inventory), 'elementow.')

input ('\nAby kontynuowac wcisnij Enter.')

# sprawdz czy element nalezy do listy, za pomoca operatora in
if 'napoj uzdrawiajacy' in inventory:
    print ('Dozyjesz dnia, w ktorym stoczysz walke.')

    # wyswietl jeden element wskazany pzez indeks
    index = int (input('\nWprowadz indeks elemntu inwentarza: '))
    print ('pod indeksem ', index, 'znajduje sie', inventory[index])

# wyswietl wycinek
start = int (input('\nWprowadz indeks wyznaczajacy poczatek wycinka: '))
finish = int (input('\nWprowdz indeks wyznaczajacy koniec wycinka: '))
print ('inventory[', start, ':', finish, '] to', end= '')
print (inventory[start:finish])

input('\nAby kontynuowac wcisnij Enter.')

# dokonaj konkatenacji dwoch list
chest = ['zloto', 'klejnoty']
print ('Znjadujesz skrzynie, ktora zawiera:')
print (chest)
print ('Dodajesz zawrtosc skrzyni do swojego inwentarza.')
inventory + chest
print ('Twoj aktualny inwentarz to: ', inventory)


input ('\nAby kontynuowac wcisnij Enter.')

# przypisz poprzez indeks
print ('Wymieniasz swoj miecz na kusze.')
inventory[0] = 'kusza'
print ('Twoj aktualny inwentarz to: ', inventory)


input ('\nAby kontynuowac wcisnij Enter.')

# przypisz poprzez wycinek
print ('zuzywasz swoje zloto i klejnoty na zakup kuli do wrozenia.')
inventory[4:6] = ['kula do wrozenia']
print ('Twoj aktualny inwentarz to: ', inventory)


input ('\nAby kontynuowac wcisnij Enter.')

# usun element
print ('W wielkiej bitwie twoja tarcza zostaje zniszczona.')
del inventory[2]
print ('Twoj aktualny inwentarz to: ', inventory)


input ('\nAby kontynuowac wcisnij Enter.')

# usun wycinek
print ('Twoja kusza i zbroja zostaly skradzione przez zlodziei.')
del inventory[:2]
print ('Twoj aktualny inwentarz to: ', inventory)

input ('\nAby zakonczyc wcisnij Enter.')






    
