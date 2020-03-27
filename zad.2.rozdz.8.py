# Napisz program, ktory symuluje telewizor,
# tworzac go jako obiekt.
# Uzytkownik powinien miec mozliwosc wprowadzenia
# numeru kanalu
# oraz zwiekszenia lub zmniejszenia glosnosci.
# Zastosuj mechanizm zapewniajacy utrzymywanie numeru kanalu
# i poziomu glosnosci we wlasciwych zakresach.


class Critter(object):
    '''Twoj telewizor'''
    def __init__(self, name, sound = 0, sound_down = 0):
        self.name = name
        self.sound = sound
        self.sound_down = sound_down

    def __pass_time(self):
        self.sound += 1
        self.sound_down += 1

    def canal(self):
        print('Wybrales program numer', self.name, 'i teraz mozesz go ogladac.\n')
        self.__pass_time()

    def podglasnianie(self):
        sound = int(input('o ile chcesz zwiekszyc glosnosc?'))
        if sound < 0:
            print('sound = 0')
        elif sound > 10:
            print('Max.sound to 10.')
        elif sound >= 0 or sound <= 10:
            self.podglasnianie -= sound
            self.__pass_time()

    def sciszanie(self):
        sound_down = int(input('o ile chcesz sciszyc?'))
        if sound_down < 0:
            print('sound = 0')
        elif sound_down > 10:
            print('min.sound to 0.')
        elif sound_down >= 0 or sound_down <= 10:
            self.sciszanie -= sound_down
            self.__pass_time()

def main():
    crit_name = input('Ktory program wybierasz? 1-8')
    crit = Critter(crit_name)

    choice = None
    while choice != '0':
            print('''\n-Twoj telewizor-
                0 - zakoncz program
                1 - wprowadz kanal programu
                2 - zwieksz glosnosc
                3 - zmniejsz glosnosc
                ''')
            choice = input('Wybierasz:')
            print()

            # wyjdz z petli
            if choice == '0':
                print('wylaczyles telewizor.')
            # wprowadz kanal programu
            elif choice == '1':
                crit.canal()
            # zwieksz glosnosc
            elif choice == '2':
                crit.podglasnianie()
            # zmniejsz glosnosc
            elif choice == '3':
                crit.sciszanie()
            # nieznany wybor
            else:
                print('\nglosnosc bez zmian.')

main()

input('\nAby zakonczyc gre, wcisnij Enter.')
