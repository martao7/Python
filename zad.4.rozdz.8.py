# Utworz program Farma zwierzakow,
# konkretyzujac kilka obiektow klasy Critter
# i sledzac ich stan poprzez liste.
# Nasladuj program Opiekun zwierzaka, lecz zamiast wymagac od uzytkownika
# zajmowania sie pojedynczym zwierzakiem,
# zazadaj od niego opieki nad cala farma.
# Kazda pozycja menu powinna umozliwic uzytkownikowi
# wykonanie pewnej czynnosci obejmujacej wszystkie zwierzaki
# ('nakarm wszystkie zwierzaki',
# 'pobaw sie ze wszystkimi zwierzakami',
# czy 'sluchaj wszystkich zwierzakow').
# Aby program byl ciekawszy, nadaj kazdemu zwierzakowi wybrany losowo
# poczatkowy poziom glodu i nudy.


class Critter(object):
    '''-Farma zwierzakow-'''
    def __init__(self, name, hunger= 0, boredom = 0):
        print('Hurra, urodzil ci sie zwierzak!')
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

    def talk(self):
        print ('Nazywam sie', self.name, 'i jestem', self.mood, 'teraz.\n')
        self.__pass_time()

    def eat(self, food = 4):
        print(self.name, 'mowi: Mniam, mniam. Thanks.')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print(self.name, 'mowi: Wow, ale fun!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
def main():
    crit1_name = input ('Jak nazwiesz pierwszego zwierzaka?')
    crit1 = Critter(crit1_name)

    crit2_name = input('Jak nazwiesz drugiego zwierzaka?')
    crit2 = Critter(crit2_name)

    crit3_name = input ('Jak nazwiesz trzeciego zwierzaka?')
    crit3 = Critter(crit3_name)

    choice = None
    while choice != '0':
        print ('''\n-Farma zwierzakow-
        0 - zakoncz
        1 - sluchaj wszystkich zwierzakow
        2 - nakarm wszystkie zwierzaki
        3 - pobaw sie ze wszystkimi zwierzakami
        ''')
        choice = input('Wybierasz:')
        print()

        # wyjdz z petli
        if choice == '0':
            print ('Do widzenia.')
        # sluchaj zwierzaka
        elif choice == '1':
            crit1.talk()
            crit2.talk()
            crit3.talk()

        # nakarm zwierzaka
        elif choice == '2':
            crit1.eat()
            crit2.eat()
            crit3.eat()

        # pobaw sie z nim
        elif choice == '3':
            crit1.play()
            crit2.play()
            crit3.play()

        # nieznany wybor
        else:
            print ('\nZwierzaki pasa sie na lace.')

main ()

input ('\nAby zakonczyc gre, wcisnij Enter.')
