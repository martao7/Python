# program ktory liczy za uzytkownika
# umozliw uzytkownikowi wprowadzenie :liczby poczatkowej, koncowej i wielk odstepu

print ('Program ktory liczy za uzytkownika')

first_number = int (input ('\nWpisz liczbe poczatkowa: '))
end_number = int (input ('\nWpisz liczbe koncowa: '))
odstep = int (input ('\nJaki powinien byc odstep miedzy kolejnymi liczbami? '))
for i in range (first_number, end_number, odstep):
     print (i, end= ' ')

input ('\nAby zakonczyc wcisnij Enter.')
