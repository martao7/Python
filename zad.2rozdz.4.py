# program ktory wczytuje komunikat uzytkownika
# a nastepnie wypisuje go w odwrotnej kolejnosci


message = input ('\nWprowadz komunikat: ')
wspak = len (message)
for i in range(wspak, 0, -1):
    print (message[i - 1])

input ('\nAby zakonczyc wcisnij Enter.')
   


