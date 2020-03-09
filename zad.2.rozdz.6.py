# zmodyfikuj projekt Jaka to liczba? z rozdz.3
# przez uzycie w nim funkcji ask_number()

# Jaka to liczba?
#
# Komputer wybiera losowo liczbę z zakresu od 1 do 100.
# Gracz próbuje ją odgadnąć, a komputer go informuje,
# czy podana przez niego liczba jest: za duża, za mała,
# prawidłowa.

import random

print("\tWitaj w grze 'Jaka to liczba'!")
print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n")

the_number = random.randint(1, 100)


def ask_number (guess):
    tries = 1
    while guess != the_number:
         if guess > the_number:
            print("Za duża...")
         else:
            print("Za mała...")
         guess = int(input("Ta liczba to: (1 - 100"))
         tries += 1
    return tries

# kod glowny
tries = ask_number (int(input("Ta liczba to: (1 - 100")))

print("Odgadłeś! Ta liczba to", the_number)
print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!\n")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")