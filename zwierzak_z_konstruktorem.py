# Zwierzak z konstruktorem
# demonstruje konstruktory

class Critter(object):
    '''Wirtualny pupil'''
    def _init_(self):
        print('Urodzil sie nowy zwierzak!')

    def talk(self):
        print('Czesc! Jestem egzepmplarzem klasy Critter.')

#czesc glowna
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

input('\nAby zakonczyc wcisnij Enter.')
