class Critter(object):
    """Pupilek"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        rep = "Obiekt klasy Critter\n"
        rep += "Imię zwierzaka: " + str(self.name) + "\n"
        rep += "Głod:" + str(self.hunger) + "\n"
        rep += "Nuda:" + str(self.boredom) + "\n"
        return rep

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    
    
 
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczęśliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 11 <= unhappiness <= 15:
            m = "podenerwowany"
        else:
            m = "wściekły"
        return m
 
    def talk(self):
        print("Nazywam się", self.name, "i jestem", self.mood, "teraz.\n")
        self.__pass_time()
 
    def eat(self):
        food = int(input("Ile jedzenia chcesz podać?"))
        if food < 0:
          print("Podaj jedzenie.")
        elif food > 15:
          print("Podaj zwierzakowi do 15 dawek jedzenia.")
        elif food >= 0 or food <= 15:
          self.hunger = self.hunger - food
        self.__pass_time()
 
    def play(self, fun = 4):
        print("Hura!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

 
def main():
    crit_name = input("Jak chcesz nazwać swojego zwierzaka?: ")
    crit = Critter(crit_name)
 
    choice = None  
    while choice != "0":
        print \
        ("""
        Opiekun zwierzaka
 
        0 - zakończ
        1 - słuchaj swojego zwierzaka
        2 - nakarm swojego zwierzaka
        3 - pobaw się ze swoim zwierzakiem
        """)
 
        choice = input("Wybierasz: ")
        print()
 
        # wyjdź z pętli 
        if choice == "0":
            print("Do widzenia, wpadnij jeszcze.")
 
        # słuchaj swojego zwierzaka
        elif choice == "1":
            crit.talk()
 
        # nakarm swojego zwierzaka
        elif choice == "2":
            crit.eat()
 
        # pobaw się ze swoim zwierzakiem
        elif choice == "3":
            crit.play()

        #Zadanie domowe
        elif choice == "4":
            crit.__str__()
            print(crit)
 
        # nieznany wybór 
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")


main()

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
