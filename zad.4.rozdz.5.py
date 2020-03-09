# udoskonal program Kto jest moim tata?
# poprzez dodanie opcji
# ktora umozliwi uzytownikowi wprowadzenie imienia i (lub) nazwiska
# jakieis osoby i uzyskanie odpowiedzi, kto jest jej dziadkiem.
# Twoj program powinien nadal wykorzystywac tylko jeden slownik par syn-ojciec.
# pamietaj o wlaczeniu do slownika kilku pokolen, tak
# aby mozliwe bylo tego rodzaju dopasowanie.

MEN = {'Adam Kiszka': 'Jerzy Kiszka',
        'Julian Zak': 'Cezary Zak',
        'Boleslaw Chrobry': 'Mieszko I',
        'Otto II': 'Otto I'}

choice = None
while choice != '0':
    print (''' -Kto jest moim tata i dziadkiem?-
    0 - zakoncz program
    1 - znajdz powiazanie syn-ojciec
    2 - dodaj nowe nazwisko
    3 - zmien nazwisko
    4 - zobacz kto jest dziadkiem
    ''')
    choice = input ('Wybierasz:')
    print ()

# zakoncz program
    if choice == '0':
        print ('goodbye')
# znajdz pow syn-ojciec
    elif choice == '1':
        print ('Adam Kiszka, Julian Zak, Boleslaw Chrobry, Otto II')
        son = input('Podaj imie i nazwisko syna:')
        if son in MEN:
            father = MEN[son]
            print ('\n', father, 'jest ojcem', son)
        else: print ('\nNie ma takiej opcji')
# dodaj nowe nazwisko
    elif choice == '2':
        son = input ('Jakie imie i nazwisko chcesz dodac?')
        if son not in MEN:
            father = input ('\nI kto jest ojcem tej osoby? ')
            MEN[son] = father
            print ('\n Ojciec', father, 'i syn', son, 'zostali dodani.')
        else: print ('\nNie ma takiej opcji.')
# zmien nazwisko
    elif choice == '3':
        print('Adam Kiszka, Julian Zak, Boleslaw Chrobry, Otto II')
        son = input ('Czyjego ojca chcesz usunac?')
        if son in MEN:
            father = input ('Podaj nowe imie i nazwisko ojca:')
            MEN[son] = father
            print ('Ojcem syna', son, 'jest teraz', father )
        else: print ('\nNie ma takiej opcji.')
# kto jest dziadkiem
    elif choice == '4':
        print('Adam Kiszka, Julian Zak, Boleslaw Chrobry, Otto II')
        grandfather = input ('Czyjego dziadka chcesz znalezc?')
        if grandfather in MEN:
            son = MEN[grandfather]
            father = MEN[son]
            print ('\nDziadkiem jest', grandfather)
        else: print ('\nNie ma takiej opcji.')

    input('Aby kontynuowac, wcisnij Enter.')


