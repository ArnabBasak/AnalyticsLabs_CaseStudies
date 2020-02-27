#this is python program for dice game
from random import randint
def gamePlay():
    num = int(input('enter any number between 1 and 6'))
    dice = randint(1,6)
    if num == dice:
        print('congrats you won.. You perdicted:',num,'dice number was',dice)
        choice = int(input('enter 1 to play again'))
        if choice == 1:
            gamePlay()
        else:
            print('Thanks your score')
    else:
        print('sorry you lost..You predicted:',num,'dice number was',dice)
        choice = int(input('enter 1 to play again'))
        if choice == 1:
            gamePlay()
        else:
            print('Thanks your score')
gamePlay()
