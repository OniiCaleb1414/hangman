# Hangman
import math, os, csv, random
def hangman(word):
    wrong = 0
    stages = ['___________',
              '|          |',
              '|          0',
              '|        / | \'',
              '|         /  \'',
              '|']
    rLetters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Welcome to Hangman!')
    while wrong < len(stages)- 1:
        print('\n')
        msg = 'Guess a letter'
        char = input(msg)
        if char in rLetters:
            cind = rLetters.index(char) 
            board[cind] = char
            rLetters[cind] = '$'
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong +1 
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('You Win!')
            print('It was {}'.format(word))
            win = True
            break      
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You lose! It was {}'.format(word))
              
words = ['book', 'dog', 'chair', 'cat', 'laptop']
num = random.randint(0,len(words)-1)
hangman(words[num]) 