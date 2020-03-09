
print ('''      program -Kreator postaci-
''')


points = [('power', 5), ('healthy', 4), ('wisdom', 10), ('agility', 6)]
print (points[0])
print (points[1])
print (points[2])
print (points[3])


total = 30
choice = None

STATS = (["siła"],
         ["zdrowie"],
         ["mądrość"], 
         ["zręczność"])

a_score = STATS[0]
b_score = STATS[1]
c_score = STATS[2]
d_score = STATS[3]

while choice != "0":
    print(
    """
   KREATOR POSTACI

   0 - zakończ
   1 - wyświetl obecny stan punktów do rozlokowania
   2 - dodaj punkty do wybranego atrybutu
   3 - usuń punkty z danego atrybutu i dodaj do puli dostępnych punktów
   4 - posortuj statystyki
   """
    )

    choice = input("Wybierasz: ")
    print()

    # zakończ program
    if choice == "0":
        print("Do widzenia.")

    elif choice == "1":
        print("Twoja ilość dostępnych punktów to:", total)

    # dodaj punkty do wybranego atrybutu
    elif choice == "2" and total != 0:
         print(STATS)
         wybór = int(input("Wprowadź indeks atrybutu (od 0 do 3): "))
         print("Wybrałeś:", STATS[wybór])
         liczba = int(input("Ile punktów chcesz dodać do tego atrybutu: "))
         
         if wybór == 0:
             a_score.append(int(liczba))
             total -= int(liczba)
             print(a_score, "pozostało ci:", total, "do rozdania")
             input("\nAby powrócić do menu, naciśnij klawisz Enter")
         elif wybór == 1:
             b_score.append(int(liczba))
             total -= int(liczba)
             print(b_score, "pozostało ci:", total, "do rozdania")
             input("\nAby powrócić do menu, naciśnij klawisz Enter")
         elif wybór == 2:
             c_score.append(int(liczba))
             input("\nAby powrócić do menu, naciśnij klawisz Enter")
             total -= int(liczba)
             print(c_score, "pozostało ci:", total, "do rozdania")
             input("\nAby powrócić do menu, naciśnij klawisz Enter")
         elif wybór == 3:
             d_score.append(int(liczba))
             total -= int(liczba)
             print(d_score, "pozostało ci:", total, "do rozdania")
             input("\nAby powrócić do menu, naciśnij klawisz Enter")
        
    
             
    # przekazywanie punktów z powrotem do puli
    elif choice == "3":
        print(STATS)
        wybór = int(input("Wprowadź indeks atrybutu, od którego chcesz odjąć punkty (od 0 do 3): "))
        print("Wybrałeś:", STATS[wybór])
        liczba = (input("Ile punktów chcesz odjąć od tego atrybutu: "))
        if wybór == 0 and liczba in a_score:
             a_score[1].remove(liczba)
             total += liczba
             print(a_score, "pozostało ci:", total, "do rozdania")
             input("\nAby powrócić do menu, nacisnij klawisz Enter")
        elif wybór == 1:
             b_score.remove(int(liczba))
             total += liczba
             print(b_score, "pozostało ci:", total, "do rozdania")
             input("\nAby powrócić do menu, nacisnij klawisz Enter")
        elif wybór == 2:
             c_score.remove(int(liczba))
             input("\nAby powrócić do menu, nacisnij klawisz Enter")
             total += liczba
             print(c_score, "pozostało ci:", total, "do rozdania")
             input("\nAby powrócić do menu, nacisnij klawisz Enter")
        elif wybór == 3:
             d_score.remove(int(liczba))
             total += liczba
             print(d_score, "pozostało ci:", total, "do rozdania")
             input("\nAby powrócić do menu, nacisnij klawisz Enter")

    elif choice == "5":
        print(STATS)
 
