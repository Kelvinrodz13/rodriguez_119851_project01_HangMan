from graphics import *
import random

def Search(word='',selected_Word='',i=0):
    if word[0] == selectedWord[i]:
        return True
    else:
        return False

def FindWord(letter,word):
    for i in word:
        if letter[0] == word[i]:
            return True
        else:
            return False

words = ['nun','sky','dog','cat','fox','gum','die','gun','fun','car','ray']
dash = list('___')

win = GraphWin('HangMan',600,600)
win.setCoords(0,0,600,600)

randomNum = random.randint(0,10)

selectedWord = words[randomNum]

title_str = "GUESS THE WORD OR YOUR FRIEND DIES!\nYOU HAVE 5 FAIL ATTEMPTS\n\n"

attempts = 0

Title = Text(Point(300,500),title_str)
Title.draw(win)
####################################################Building Post
hangPost_Base = Line(Point(250,200), Point(350,200))
hangPost_Base.draw(win)
postCoords = hangPost_Base.getCenter()
postCoords.move(0,200)

hangPost_Col = Line(hangPost_Base.getCenter(),postCoords)
hangPost_Col.draw(win)

ledge_x = postCoords

hangPost_ledge = Line(ledge_x,Point(360,400))
hangPost_ledge.draw(win)
########################################################

centerCol = hangPost_Col.getCenter()
centerCol.move(-100,0)

guessWord = Text(centerCol, 'test')
guessWord.draw(win)

wordCount = len(selectedWord)

finalCompare = "lorem"

while attempts < 5 and selectedWord != finalCompare:

    textEntry = Entry(Point(300,50),1)
    textEntry.setFill(color_rgb(167, 197, 253))
    textEntry.draw(win)

    clickWord = Text(Point(300,25), 'Click anywhere to enter guess!')
    clickWord.draw(win)
    
    win.getMouse() #click function as enter
    clickWord.undraw()

    user_Guess = textEntry.getText()

    found = str.find(selectedWord,user_Guess)

    if found < 0:
        found = False
    else:
        found = True

    if found == True:

        for i in range(wordCount):
            if Search(user_Guess,selectedWord,i) == True:  
                    dash[i] = user_Guess
    else:
        attempts += 1
    
    guessWord.undraw()

    guessWord = Text(centerCol, dash)
    guessWord.draw(win)

    finalCompare= "".join(dash)


    userBox = Text(Point(300,150), dash)
    userBox.draw(win)


            

win.getMouse()
win.close()

