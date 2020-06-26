''''Wejście
Pierwsza linia wejścia zawiera liczbę t (t <= 80),
określającą ile liczb znajduje się na kartce Piotrusia.
Każda z następnych t linii zawiera dokładnie jedną
liczbę naturalną n (1 <= n <= 80),
dla której Piotruś musi wykonać obliczenia.

Wyjście
Dla kolejnych liczb podanych na kartce wypisz
po jednej linijce zawierającej dwie liczby całkowite
oddzielone spacją. Pierwsza oznacza palindrom
otrzymany przez Piotrusia, druga -- liczbę dodawań wykonanych,
by go otrzymać.

Przykład
Wejście:
3
28
68
5

Wyjście:
121 2
1111 3
5 0
'''

def szukaj_palindromu(numbers):
    sum = 0
    sum += int(numbers)

ile_liczb = int(input('ile liczb ma sie pojawic na kartce?'))

for n in range (ile_liczb):
    numbers = []
    numbers = int(input('Jaka liczbe wypisujesz?'))
    print (numbers)

for i in range(numbers):
    # program wpadnie w nieskończoną pętlę przy 200 i 196. Dla tych liczb nie można osiągnąć palindromu
    if(i != 196 and i != 200):
        print('Palindrom dla {}:'.format(i), szukaj_palindromu(i))
    else:
        print('Nie istnieje palindrom dla {}'.format(i))





