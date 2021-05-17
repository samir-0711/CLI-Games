import random
from random_words import RandomWords

class Game:
    def __init__(self):
        # self.words=["devsnest","sanjay","samir","nishant"]
        rw = RandomWords()
        self.word = rw.random_word() #self.words[random.randint(0,len(self.words))]
        self.gameBoard = ["_"]*len(self.word)
        length=len(set(list(self.word)))
        if length<4:
            self.move = length
        else:
            self.move = length-2

    def convertToString(self):
        print(" ".join(self.gameBoard))
    
    def validateCharacter(self, character):
        return character in self.word

    def markPosition(self, character):
        for pos,char in enumerate(self.word):
            if char==character:
                self.gameBoard[pos]=char

    def isMoveRemaining(self):
        return self.move>0

    def getMove(self):
        return self.move

    def isWinner(self):
        return "_" not in self.gameBoard

    def decrementMmove(self):
        self.move-=1

    def showAnswer(self):
        print(f"\nCorrect Word was {self.word}")

        