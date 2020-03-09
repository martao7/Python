# zmodyfikuj nowa wersje gry Jaka to liczba?,
# ktora utworzyles w ramach poprzedniego zadania,
# tak aby kod programu znalazl sie w funkcji o nazwie main().
# nie zapomnij o wywolaniu funkcji main() w celu uruchomienia gry

def game_instruct():
     print("\tWitaj w grze 'Jaka to liczba'!")
     print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
     print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n")

import random
the_number = random.randint(1, 100)


def ask_number (guess):
    tries = 1
    while guess != the_number:
         if guess > the_number:
            print("Za duża...")
         else:
            print("Za mała...")
         guess = int(input('Ta liczba to (1 - 100): '))
         tries += 1
    return tries

tries = ask_number (int(input('Ta liczba to (1 - 100): ')))

def when_winner():
    print("Odgadłeś! Ta liczba to", the_number)
    print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!\n")

def main():
    game_instruct()
    import random
    the_number = random.randint
    ask_number(guess)
    return tries
    when_winner

# kod glowny
main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")