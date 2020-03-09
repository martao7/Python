# kolko i krzyzyk
# komputer gra w kolko i krzyzyk przeciw czlowiekowi

# stale globalne
X = 'x'
O = 'o'
EMPTY = ''
TIE = 'TIE'
NUM_SQUARES = 9

def display_instruct():
    '''Wyswietl instrukcje gry.'''
    print( '''
    - Gra kolko i krzyzyk - 
    0 1 2
    3 4 5
    6 7 8
    ''')
def ask_yes_no(question):
    '''pytanie: odp tak lub nie'''
    response = None
    while response not in ('t', 'n'):
        response = input(question).lower()
    return response
def ask_number(question, low, high):
    '''Popros o podanie liczby z odpowiedniego zakresu.'''
    response = None
    while response not in range (low, high):
        response = int(input(question))
        return response
def pieces():
    '''Ustal czy pierwszy ruch nalezy do gracza czy do kompa.'''
    go_first = ask_yes_no('Czy chcesz wykonac pierwszy ruch? (t/n):')
    if go_first == 't':
        print ('pierwszy ruch nalezy do ciebie.')
        human = X
        komp = O
    else:
        print ('komp wykonuje pierwszy ruch.')
        komp = X
        human = O
    return komp, human
def new_board():
    '''Utworz nowa plansze gry.'''
    board = []
    for square in range (NUM_SQUARES):
        board.append(EMPTY)
    return board
def display_board(board):
    '''Wyswietl plansze gry na ekranie.'''
    print ('\n\t', board[0], ' I ', board [1], ' I ', board[2])
    print ('\t', '-----------')
    print ('\t', board[3], ' I ', board[4], ' I ', board[5])
    print ('\t', '-----------')
    print ('\t', board[6], ' I ', board[7], ' I ', board[8], '\n')
def legal_moves(board):
    '''Utworz liste prawidlowych ruchow.'''
    moves = []
    for square in range (NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
def winner(board):
    '''Ustal zwyciezce gry.'''
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None
def human_move(board, human):
    '''Odczytaj ruch czlowieka'''
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('Jaki bedzie twoj ruch(0 - 8):', 0, NUM_SQUARES)
        if move not in legal:
            print ('\nTo pole jest juz zajete. wybierz inne')
    print ('Super.')
    return move
def komp_move(board, komp, human):
    '''Spowoduj wykonanie ruchu przez komp.'''
    # utworz kopie robocza poniewaz funkcja bedzie zmienia liste
    board = board[:]
# najlepsze pozycje do zajecia wg kolejnosci
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print ('Wybieram pole numer', end='')
    #jesli komp moze wygrac wykonaj ten ruch
    for move in legal_moves(board):
        board[move] = komp
        if winner(board) == komp:
            print (move)
            return move
        # ten ruch zostal sprawdzony, wycofaj go
        board[move] = EMPTY
    # jesli czlowiek moze wygrac, zablokuj ten ruch
    for move in legal_moves(board):
        board[move] = human
        if winner (board) == human:
            print(move)
            return move
        # ten ruch zostal sprawdzony, wycofaj go
        board[move] = EMPTY
    # jesli nikt nie moze wygrac w nastepnym ruchu, wybierz najlepsze wolne pole
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print (move)
            return move
def next_turn(turn):
    '''Zmien wykonawce ruchu'''
    if turn == X:
        return O
    else:
        return X
def congrat_winner(the_winner, komp, human):
    '''Pogratuluj zwyciezcy'''
    if the_winner != TIE:
        print ('Congratulations!', the_winner, 'jest zwyciezca')
    else:
        print ('Remis')

def main():
    display_instruct()
    komp, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner (board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = komp_move(board, komp, human)
            board[move] = komp
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, komp, human)
# rozpocznij program
main()
input ('/nAby zakonczyc wcisnij Enter.')


