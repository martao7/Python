# Opiekun zwierzaka
# ulepsz program, pozwalajac uzytkownikowi na okreslenie
# ilosci pozywienia podawanego zwierzakowi
# i czasu poswieconego na zabawe z nim.
# Wartosci te powinny wplywac na
# szybkosc spadku poziomu glodu
# i nudy u zwierzaka.

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

    def talk(self):
        print ('Nazywam sie', self.name, 'i jestem', self.mood, 'teraz.\n')
        self.__pass_time()

    def eat(self):
        food = int(input('Ile porcji jedzenia chcesz podac?'))
        if food < 0:
            print('Jestem glodny!')
        elif food > 10:
            print('Max.porcja jedzenia to 10.')
        elif food >= 0 or food <= 10:
            print(self.name, 'mowi: Teraz jestem najedzony!')
            self.hunger -= food
        self.__pass_time()

    def play(self):
        fun = int(input('Ile godzin chcesz poswiecic na zabawe?'))
        if fun < 0:
            print ('Nudzi mi sie!')
        elif fun > 10:
            print('Mozesz poswiecic 10 godzin na zabawe.')
        elif fun >= 0 or fun <= 10:
            print(self.name, 'mowi: Hurra, ale fun!')
            self.boredom -= fun
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
