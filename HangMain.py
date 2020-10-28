from HangClass import*
from graphics import *
import random

def CreateWordFile(fileName):
    data = open(fileName,)
    wordCount = int(input("How many word do you wish to add?: "))
    wordList = list()

    for i in range(wordCount):
        wordList.append(input("Enter word: ") + '\n')
    
    data.writelines(wordList)

    data.close()

def ReadWordFile(fileName):
    data = open(fileName)
    wordList = list()

    for lines in data.readlines():
        for words in lines.split():
            wordList.append(words)
    
    return wordList


def main():

    #words = ['nun','sky','dog','cat','fox','gum','die','gun','fun','car','ray']

    fileName = "WordFile.txt"

    #CreateWordFile(fileName)

    words = ReadWordFile(fileName) 

    

    win = GraphWin('HangMan',600,600)
    win.setCoords(0,0,600,600)

    randomNum = random.randint(1,len(words))

    selectedWord = words[randomNum]

    dash = list('_' * len(selectedWord))

    title_str = "GUESS THE WORD OR YOUR FRIEND DIES!\nYOU HAVE {} FAIL ATTEMPTS\nCLICK ANYWHERE TO START\n".format(7)

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

    #guessWord = Text(centerCol,'none')
    #guessWord.draw(win)
    #Text()

    wordCount = len(selectedWord)

    finalCompare = ""

    win.getMouse()

    game = Hman(selectedWord)
    #game.setWord(selectedWord)

    while game.getUserAtt() > 0 and selectedWord != finalCompare:

        attempt_str = "You have {} attempts left".format(abs(game.getUserAtt()))

        Title.setText(attempt_str)

        textEntry = Entry(Point(300,50),1)
        textEntry.setFill(color_rgb(167, 197, 253))
        if attempts < 7:

            textEntry.draw(win)
        else:
            textEntry.undraw()

        clickWord = Text(Point(300,25), 'Click anywhere to enter guess!')
        clickWord.draw(win)
        
        win.getMouse() #click function as enter
        clickWord.undraw()

        user_Guess = textEntry.getText()

        while user_Guess == '':
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
                if game.Search(user_Guess,selectedWord,i) == True:  
                        dash[i] = user_Guess
        else:
            game.decreaseAtt()
            game.drawHang(game.getUserAtt(),hangPost_ledge.getP2(),win)

        finalCompare= "".join(dash)


        userBox = Text(Point(300,150), dash)
        userBox.draw(win)


    attempt_str = "You have {} attempts left".format(abs(game.getUserAtt()))

    Title.setText(attempt_str)
    textEntry.undraw()

    gameOver_str = 'You lost the game!, your word was: {}'.format(selectedWord)

    clickWord.setText(gameOver_str)
    clickWord.draw(win)
    win.getMouse()
    win.close()


main()