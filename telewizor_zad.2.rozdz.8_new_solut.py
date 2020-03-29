# Napisz program, ktory symuluje telewizor,
# tworzac go jako obiekt.
# Uzytkownik powinien miec mozliwosc wprowadzenia
# numeru kanalu
# oraz zwiekszenia lub zmniejszenia glosnosci.
# Zastosuj mechanizm zapewniajacy utrzymywanie numeru kanalu
# i poziomu glosnosci we wlasciwych zakresach.

class Telewizor(object):
    '''Twoj telewizor'''
    def __init__(self, canal = 1,  sound = 15):
        self.canal = canal
        self.__sound = sound

    def canal(self, zmiana):
        self.new_canal = zmiana
        if self.new_canal > 25:
            self.new_canal = 25
        elif self.new_canal < 1:
            self.new_canal = 1
        print('Przelaczono na program: ', self.new_canal, '\n.')

    def podglasnianie(self):
        self.__sound += 1
        if self.__sound > 10:
            self.__sound = 10
        print('sound = ', self.__sound)

    def sciszanie(self):
        self.__sound -= 1
        if self.__sound < 0:
            self.__sound = 0
        print('sound = ', self.__sound)

def main():
    crit = Telewizor()

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
                try:
                    zmiana = int(input('Wprowadz numer kanalu: 1-25'))
                    crit.canal(zmiana)
                except:
                    print ('niepoprawny numer kanalu.')
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
