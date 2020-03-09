# zad.3, rozdz-4
# rozwiazanie sciagniete z neta


import random 

SLOWA = ("affe",
         "pferd",
         "katze")

zagadka = random.choice(SLOWA)

poprawne = zagadka

pomieszane = ""

while zagadka:
    pozycja = random.randrange(len(zagadka))
    pomieszane += zagadka[pozycja]
    zagadka = zagadka[:pozycja] + zagadka[(pozycja + 1):]

print("Zaczynamy gre")
print("Zgadnij co to za zwrot: ",pomieszane)

gosc = input ("zgaduj: ")
x=0
z=0
p = ""
while gosc != poprawne and gosc != "":
    print("to nie to")
    x+=1
    if x>=3:
        print("Nie udało Ci się zgadnąć w 3 ruchach")
        p = str(input("Potrzebujesz pomocy? Jeśli tak napisz 'yes', jeśli wolisz zgadywać bez podpowiedzi naciśnij 'no': "))
        if p == "yes":
            print("pierwsze dwie litery to: ",poprawne[:2])
            z+=1
        elif p == "no":
            print("ok zgaduj dalej")
    gosc = input("spróbuj jeszcze raz: \n")

if gosc == poprawne and z==0:
    print ("brawo Ty, zgadłeś sam i otrzymujesz 3ptk")
elif gosc == poprawne and z==1:
    print ("brawo udało Ci się ale z podpowiedzią... Otrzymujesz tylko 2ptk")
elif gosc == poprawne and z>=2:
    print ("no cóż nie poszło Ci najlepiej i mimo podpowiedzi nie zgadłeś odrazu, otrzymujesz 1ptk")

print("Dziękuję za udział w grze.")
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
