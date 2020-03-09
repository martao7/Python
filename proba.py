import random

print("\tWitaj w grze 'Jaka to liczba'!")
print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n")

the_number = random.randint(1, 100)

# definicja zmiennej
def ask_the_number(guess):
    tries = 1
    while guess != the_number:
        if guess > the_number:
            print("Za duża...")
        else:
            print("Za mała...")
        tries += 1
        guess = int(input("Wprowadź liczbę: "))
    return tries

# kod główny
tries = ask_the_number(int(input("Wprowadź liczbę: ")))

print("Odgadłeś! Ta liczba to", the_number)
print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!\n")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")