# szubienica
# komp losow wybiera slowo,
# a gracz probuje je odgadnac

# import modulow
import random

#stale
HANGMAN = (
    '''
   ------
   l    l
   l    
   l
   l
   l
   l
   l
  --------------
  ''',
'''
   ------
   l    l
   l    O
   l
   l
   l
   l
   l
  --------------
  ''',

'''
   ------
   l    l
   l    O
   l   -+-
   l
   l
   l
   l
  --------------
''',

'''
   ------
   l    l
   l    O
   l  /-+-
   l
   l
   l
   l
  --------------
  ''',
'''
 ------
   l    l
   l    O
   l  /-+-/
   l
   l
   l
   l
  --------------
  ''',
'''
 ------
   l    l
   l    O
   l  /-+-/
   l    l
   l
   l
   l
  --------------
  ''',
'''
 ------
   l    l
   l    O
   l  /-+-/
   l    l
   l   l  
   l   l
   l
  --------------
  ''',
'''
 ------
   l    l
   l    O
   l  /-+-/
   l    l
   l   l l
   l   l l
   l
  --------------
  ''')

MAX_WRONG = len(HANGMAN) - 1

WORDS = ('HASE', 'REISEPASS', 'KUHLSCHRANK', 'ANGEBOT', 'PULLOVER')

# inicjalizacja zmiennych
word = random.choice(WORDS)    # slowo do odgadniecia

so_far = '-' * len (word)      # kreska zastepuje nieoodgadnieta litere
wrong = 0                      # liczba nietrafionych liter
used = []                      # litery juz uzyte w zgadywaniu

print (''' _Wortspiel-  ''')

while wrong < MAX_WRONG and so_far != word:
    print (HANGMAN[wrong])
    print ('\nDu hast schon die Buchstaben ausprobiert: ', used)
    print ('\nJetzt sieht das Wort so aus: ', so_far)
    
    guess = input ('\nDie Buchstabe: ')
    guess = guess.upper ()

    while guess in used:
       print ('Du hast schon die Buchstabe ', guess, 'ausprobiert.')
       guess = input ('Die Buchstabe: ')
       guess = guess.upper ()
    
    used.append (guess)

    if guess in word:
     print ('\nJa!', guess, 'befindet sich in diesem Wort!')

    # utworz nowa wersje zmiennej so_far, aby zawierala odgadnieta litere
     new = ''
     for i in range (len(word)):
        if guess == word[i]:
           new += guess
        else:
           new += so_far[i]
     so_far = new

    else:
       print ('\nLeider,', guess, 'befindet sich nicht in diesem Wort.')
       wrong += 1

if wrong == MAX_WRONG:
    print (HANGMAN[wrong])
    print ('\nDu bist aufgehängt!')
else:
    print ('\Congratulations!')
print ('\nDas Wort ist: ', word)

input ('\nUm es zu beenden druck Enter.')



  
