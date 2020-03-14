# Turniej wiedzy
# gra sprawdzajaca wiedze ogolna, odczytujaca dane ze zwyklego pliku tekstowego

import sys

def open_file(file_name, mode):
    '''Otworz plik.'''
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print('Nie mozna otworzyc pliku', file_name, 'Program zostanie zakonczony.', e)
        input('\nAby zakonczyc wcisnij Enter.')
        sys.exit()
    else:
        return the_file
    
def next_line(the_file):
    '''Zwroc kolejny wiersz pliku kwiz po sformatowaniu go.'''
    line = the_file.readline()
    line = line.replace('/', '\n')
    return line

def next_block(the_file):
    '''Zwroc kolejny blok danych z pliku kwiz.'''
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    return category, question, answers, correct, explanation

def welcome(title):
    '''Przywitaj gracza i pobierz jego nazwe.'''
    print('\t\t Witaj w turnieju wiedzy!')
    print('\t\t', title, '\n')
    
def main():
    trivia_file = open_file('kwiz.txt', 'r')
    title = next_line(trivia_file)
    welcome(title)
    score = 0

# pobierz pierwszy blok
category, question, answers, correct, explanation = next_block(trivia_file)
while category:
    # zadaj pytanie
    print (category)
    print (question)
    for i in range(4):
        print ('\t', i + 1, '-', answers[i])
    # uzyskaj odpowiedz
    answer = input('Twoja odpowiedz:')
    # sprawdz odpowiedz
    if answer == correct:
        print ('\nOdpowiedz prawidlowa!', end='')
        score += 1
    else:
        print ('\nOdpowiedz niepoprawna.', end= '')
        print(explanation)
        print('Wynik:', score, '\n\n')
    # pobierz kolejny blok
    category, question, answer, correct, explanation = next_block(trivia_file)

    trivia_file.close()

print('To bylo ostatnie pytanie!')
print('Twoj koncowy wynik wynosi:', score)

main()
input('Aby zakonczyc wcisnij Enter.')
