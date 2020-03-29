# Utworz w programie Opiekun zwierzaka mechanizm 'tylnych drzwi'
# ktory pokazuje dokladne wartosci atrybutow obiektu.
# Zrealizuj to poprzez wyswietlenie obiektu po wprowadzeniu przez uzytkownika
# ukrytej wartosci, ktora nie zostala uwzgledniona w menu.
# (wskazowka: dodaj specjalna metode __str__() do klasy Critter).

class Critter(object):
    '''Wirtualny pupil'''
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'szczesliwy'
        elif 5 <= unhappiness <= 10:
            m = 'zadowolony'
        elif 11 <= unhappiness <= 15:
            m = 'podenerwowany'
        else:
            m = 'wsciekly'
        return m

    def __str__(self):
        rep = 'Obiekt klasy Critter\n'
        rep += 'name:' + self.name + '\n'
        return rep

    def talk(self):
        print ('Nazywam sie', self.name, 'i jestem', self.mood, 'teraz.\n')
        self.__pass_time()
    def eat(self, food = 4):
        print('Mniam, mniam. Dziekuje.')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self, fun = 4):
        print('Hurra!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
def main():
    crit_name = input ('Jak nazwiesz swojego zwierzaka?')
    crit = Critter(crit_name)

    choice = None
    while choice != '0':
        print ('''\nOpiekun zwierzaka
        0 - zakoncz
        1 - sluchaj swojego zwierzaka
        2 - nakarm swojego zwierzaka
        3 - pobaw sie ze swoim zwierzakiem
        ''')
        choice = input('Wybierasz:')
        print()

        # wyjdz z petli
        if choice == '0':
            print ('Do widzenia.')
        # sluchaj zwierzaka
        elif choice == '1':
            crit.talk()

            print ('Wyswietlenie obiektu crit:')
            print(crit)
            
            print('Bezposrednie wyswietlenie wartosci atrybutu crit.name:')
            print(crit.name)

        # nakarm zwierzaka
        elif choice == '2':
            crit.eat()
        # pobaw sie z nim
        elif choice == '3':
            crit.play()
        # nieznany wybor
        else:
            print ('\nNie wiem co masz na mysli.')

main ()

input ('\nAby zakonczyc gre, wcisnij Enter.')
