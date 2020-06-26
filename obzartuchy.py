'''
GLUTTON - Obżartuchy
Co roku w Megabajtolandii odbywa się Zlot Obżartuchów.
Podczas każdego zlotu tradycją jest, że pierwszego dnia
wszyscy uczestnicy obżerają się ciastkami przez całą dobę non-stop,
nie mając ani ułamka sekundy przerwy. Jak tylko obżartuch skończy
jeść jedno ciastko to od razu musi zabrać się za następne
(nie dotyczy to sytuacji pod koniec doby, kiedy to uczestnikowi
nie wolno napocząć ciastka jeśli wie, że nie zdąży go zjeść przed końcem doby).
Kolejnym ważnym elementem tradycji jest to, że każdy obżartuch je
każde swoje ciastko w niezmiennym przez całą dobę, charakterystycznym dla siebie tempie.

Na najbliższy Zlot zostały zaproszone tylko te obżartuchy,
które już uczestniczyły w poprzednich Zlotach.
Dzięki temu wiadomo z góry w jakim tempie każdy z nich je ciastka
(obżartuchy nie lubią zmieniać swojego wyuczonego tempa).
Na podstawie tych danych, organizatorzy Zlotu chcą określić ile należy kupić ciastek.
Sytuację utrudnia fakt, że ciastka w sklepie sprzedawane są w pudełkach o stałej wielkości,
a nie na sztuki - przez to być może trzeba będzie kupić trochę więcej ciastek niż zostanie zjedzonych.

Zadanie
Mając daną liczbę obżartuchów zaproszonych na Zlot
oraz czas jedzenia pojedynczego ciastka (podany w sekundach)
przez każdego z nich Twój program powinien
policzyć ile należy kupić pudełek z ciastkami.


Specyfikacja wejścia
W pierwszej linii wejścia znajduje się
jedna dodatnia liczba całkowita, oznaczająca liczbę
zestawów testowych, które dalej pojawią się na wejściu.
Każdy zestaw ma następującą postać. W pierwszej linii
znajdują się dwie liczby całkowite N i M oddzielone pojedynczą spacją
(1 ≤ N ≤ 10.000, 1 ≤ M ≤ 1.000.000.000).
Oznaczają one odpowiednio liczbę zaproszonych obżartuchów na Zlot
oraz liczbę ciastek w jednym pudełku.
Kolejne N wierszy zestawu zawiera po jednej liczbie całkowitej
dodatniej niewiększej niż 100.000.
Są to czasy (w sekundach) jedzenia pojedynczego ciastka przez kolejnych obżartuchów.

Specyfikacja wyjścia
Dla każdego zestawu danych pojawiającego się na wejściu
należy wypisać dokładnie jedną liczbę całkowitą
(każdą w osobnej linii), oznaczającą liczbę pudełek z ciastkami,
jaką organizatorzy muszą kupić na Zlot.

Przykład
Wejście
2        ilosc testow
2 10     N -ilosc obzartuchow  M-liczba ciastek w jednym pudelku
3600     time -czas w sec jedzenia jednego ciastka
1800     time
3 356
123
32999
10101
Wyjście
8       pudelka z ciastkami
2
 Submit solution!
 '''

test_score = int (input('Ile testow? 2'))

persons = int (input('Ile osob zaproszonych? 2 '))

cookies_in_the_box = int(input('Ile jest ciastek w jednym pudelku? 10 '))


for n in range(persons):
    cookie_times = []
    cookie_time = int(input('Czas jedzenia jednego ciastka w sec? 3600 i 1800'))
    while cookie_time <= 0:
        print('czas nie moze byc rowny 0')
        cookie_time = int(input('Czas jedzenia jednego ciastka w sec? 1800'))
    cookie_times.append(cookie_time)

    print(cookie_times)

    cookie_times_total = 0
    for i in range (persons):
        cookie_times_total += int(cookie_times[i])
        print('laczny czas jedzenia ciastek przez obzartuchow: ', cookie_times_total )

time = 24 * 60 *60

cookies_per_one_day = time / cookie_times_total
print ('ilosc zjedzonych ciastek w ciagu doby to ', cookies_per_one_day)

cookies_box = cookies_per_one_day / cookies_in_the_box
print('ilosc opakowan ciastek do kupienia: ', cookies_box )






