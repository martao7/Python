# program Kto jest moim tata?
# ktory umozliwia uzytkownikowi wprowadzenie
# imienia i nazwiska osoby plci meskiej
# i przedstawia imie i nazwisko jej ojca
# umozliw uzytkownikowi
# dodawanie, wymiane i usuwanie par syn-ojciec


MEN = {'Adam Kiszka': 'Jerzy Kiszka',
        'Julian Zak': 'Cezary Zak',
        'Boleslaw Chrobry': 'Mieszko I',
        'Otto II': 'Otto I'}

choice = None
while choice != '0':
    print(''' 
     -Kto jest moim tata?-
    
     0 - zakoncz program
     1 - znajdz ojca
     2 - wymien ojca
     3 - dodaj nowa pare syn-ojciec
     4 - usun pare syn-ojciec
''')
    choice = input ('Wybierasz: ')
    print ()

    # wyjdz
    if choice == '0':
       print('Game over.')

    # znajdz ojca
    elif choice == '1':
       print('\nAdam Kiszka, Julian Zak, Boleslaw Chrobry, Otto II')
       son = (input('\nWprowadz imie i nazwisko osoby plci meskiej:'))
       if son in MEN:
           father = MEN[son]
           print ('\nOjcem ', son, 'jest', father )
       else:
           print ('\nNiestety nie ma podanego ojca')

    # wymien ojca
    elif choice == '2':
       print('\nAdam Kiszka, Julian Zak, Boleslaw Chrobry, Otto II')
       son = input ('Czyjego ojca chcesz wymienic?')
       if son in MEN:
           father = input ('Jak powinien nazywac sie ojciec?')
           MEN[son] = father
           print ('\n', son, 'zmienil teraz ojca na', father)
       else:
           print ('\nTaka osoba nie istnieje, sprobuj ja dodac do listy.')

    # dodaj nowa pare ojciec-syn
    elif choice == '3':
       son = input ('Podaj nowe imie i nazwisko syna:')
       if son not in MEN:
           father = input ('\nPodaj nowe imie i nazwisko ojca: ')
           MEN[son] = father
           print ('\n', son, 'i jego ojciec zostali dodani do listy.')
       else:
           print ('\nTakie nazwisko juz jest na liscie!')

    # usun pare syn-ojciec
    elif choice == '4':
       print('\nAdam Kiszka, Julian Zak, Boleslaw Chrobry, Otto II')
       son = input('Ktore nazwisko syna chcesz usunac?')
       if son in MEN:
           del MEN[son]
           print ('\nok,', son, 'i jego ojciec zostali usunieci z listy')
       else:
           ('\nNie ma takiego nazwiska na liscie!')

input ('\nAby kontynuowac wcisnij Enter.')






