from random import randint
class matlibs():
    def __init__(self):
        self.user_num = 0
        self.system_num = 0
        self.user_score = 0
        self.system_score = 0
        self.playagain = 0
        self.setNumber()
    def setNumber(self):
        self.user_num = (int(input('enter any number between 1 and 99999'))
        self.system_num = randint(1,99999)
        self.compareNumber()
    def compareNumber(self):
        if self.user_num == self.system_num:
            self.score = 5
            print('you won')
            self.playagain()
        elif self.user_num < self.system_num:
            self.score = -5
            print('sorry you predicted less you missed by',self.system_num - self.user_num)
        elif
    def playagain(self):
        self.playagain = int(input('wanna play again'))
        if self.playagain == 1:
            self.setNumber()
        else:
            print('your score is: ',self.score)
