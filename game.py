from __future__ import division
from graphics import *
import random
import math
import string
import time

class Words():
    """Class handle all things related to checking the validity of a word"""
    def __init__(self, letters):
        self.letters = letters

    def dictionaryList(self):
        """Imports a dictionary, and then turns that dictionary into a list of string values."""
        text = open("dictionary.txt", 'r')
        dictionary = text.read()
        dictlist = dictionary.split()
        return dictlist

    def wordSelections(self,dictlist, selections=[]):
        """ Generates a list of possible words and returns that list"""
        for e in range(len(self.letters)):
            for word in dictlist:
                if word[0] == self.letters[e]:
                    selections += word,
        return selections

    def wordVal(self,userword):
        """evaluates if the word inputed(userword) is a possible to formulate that word from a list of letters(letters).
        If it is not possible the function returns False. If possible it returns True."""
        for i in range(len(userword)):
            if userword[i] in self.letters:
                return True
            else:
                return False

def compilescore(alist):
    """Compiles a score from the given words in a list and returns the score"""
    score = 0
    for word in alist:
        score += len(word)

    return score

def lettersRandom(chrcount):
    """Generates a list of 6 "randomly" selected letters and returns that list"""
    xtravowel = "aeiou"
    alpha = "abcdefghjklmnpqrstvwxzy"
    randomnum = random.randrange(0,5)
    letters = xtravowel[randomnum]
    for i in range(10):
        randomnum2 = random.randrange(0,20)
        if alpha[randomnum2] not in letters:
            letters += alpha[randomnum2]
        if len(letters) == 6:
            break
    return letters

def displayletters(alist, win):
    """Displays a list of letters on screen"""
    j = .45
    i = 0
    for i in range(6):
        displayletter = Text(Point(j, 2.7),alist[i])
        displayletter.setSize(36)
        displayletter.draw(win)
        j += .43

def main():
    """ A variation of the game WordTwist. To begin playing click the textfield provided.
    Rules are simple, create as many words as you can with the given words on the screen and you are allowed to use a word more than once.
    The score of the game is compiled by the length of the word you spell, the longer the word the more point you get!
    N.B. The dictionary used is not a standard dictionary so some words that make sense to you will not be granted points.
    To exit - press the exit button. To restart the game and see your final score - press restart. To submit your word - click the cubmit button"""
    win=GraphWin("Word Jumble",700,500)
    image = Image(Point(350,250), 'background.gif')
    image.draw(win)

    win.setCoords(0.0, 0.0, 3.0, 4.0)
    ainput = Entry(Point(1.5,1.5), 25)
    ainput.setText("")
    ainput.draw(win)

    letters = lettersRandom(6)
    displayletters(letters, win)

    w = Words(letters)
    dictionary = w.dictionaryList()
    selections = w.wordSelections(dictionary)
    scorewordslist = []

    t1 = time.time()
    m = win.getMouse()
    mx = m.getX()
    my = m.getY()
    while True:
        #the exit button
        if mx>= 0.0429184549356 and mx <= 0.403433476395 and my >= 0.176352705411 and my <= 0.801603206413:
                win.close()
                break

        #submit button
        elif mx >= 2.29184549356 and mx <= 2.64806866953 and my >= 1.30661322645 and my <= 1.93186372745:
               userword = ainput.getText().lower()
               val1 = w.wordVal(userword)
               val2 = userword in selections
               val3 = userword in scorewordslist
               if val1 == True and val2 == True and val3 == False:
                   response = Text(Point(2.45,.63),"Correct")
                   response.setSize(30)
                   response.draw(win)
                   scorewordslist.append(userword)
                   time.sleep(1)
                   response.undraw()
                   scoring = compilescore(scorewordslist)
                   box = Rectangle(Point(2.25, .45), Point(2.63, .20))
                   box.setFill('white')
                   box.draw(win)
                   score = Text(Point(2.45,.32), scoring)
                   score.setSize(20)
                   score.draw(win)
                   ainput.setText("")

               else:
                   response2 = Text(Point(2.45,.63),"Try Again")
                   response2.setSize(25)
                   response2.draw(win)
                   time.sleep(1)
                   response2.undraw()
                   ainput.setText("")

        #restart button
        elif mx >= 0.523605150215 and mx <= 0.87982832618 and my >= 0.176352705411 and my <= 0.809619238477:
            box = Rectangle(Point(2.25, .45), Point(2.63, .20))
            box.setFill('white')
            box.draw(win)
            thescore = compilescore(scorewordslist)
            finalscore = Text(Point(2.45,.32), "Final Score: %d "%(thescore) )
            finalscore.setSize(10)
            finalscore.draw(win)

            i = 5
            while i != 0:
                time.sleep(.5)
                countdown = Text(Point(1.5,2),i)
                countdown.setSize(36)
                countdown.draw(win)
                countdown.undraw()
                i -= 1

            win.close()
            main()
            break

        m = win.getMouse()
        mx = m.getX()
        my = m.getY()

main()
