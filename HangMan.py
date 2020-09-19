from graphics import *
import random

def Search(word='',selected_Word='',i=0):
    if word[0] == selectedWord[i]:
        return True
    else:
        return False


def drawHang(att=0,ledge=Point(0,0),win=GraphWin): # function to create the hanged man

    ledge.move(0,-10)
    head = Circle(ledge,10)

    torso_p1 = head.getCenter()
    torso_p1.move(0,-10)

    torso_p2 = Point(torso_p1.getX(),300)
    #torso_p2.move()

    torso = Line(torso_p1,torso_p2)

    left_p1 = torso.getCenter()
    left_p1.move(0,20)
    left_p2 = left_p1.clone()
    left_p2.move(-30,-30)
    left_arm = Line(left_p1,left_p2)

    right_p1 = left_arm.getP1()
    right_p2 = left_arm.getP2()

    right_p2.move(60,0)

    right_arm = Line(right_p1,right_p2)

    centerLeg = torso.getP2()
    left_leg = torso.getP2()

    left_leg.move(-30,-30)
    right_leg = left_leg.clone()
    right_leg.move(60,0)

    LegLineL = Line(centerLeg,left_leg)
    LegLineR = Line(centerLeg,right_leg)



    if att == 1:
        head.setFill('black')
        head.draw(win)
    elif att ==2:
        torso.draw(win)
    elif att == 3:
        left_arm.draw(win)
    elif att == 4:
        right_arm.draw(win)
    elif att == 5:
         LegLineL.draw(win)
    elif att == 6:
        LegLineR.draw(win)




words = ['nun','sky','dog','cat','fox','gum','die','gun','fun','car','ray']
dash = list('___')

win = GraphWin('HangMan',600,600)
win.setCoords(0,0,600,600)

randomNum = random.randint(0,10)

selectedWord = words[randomNum]

title_str = "GUESS THE WORD OR YOUR FRIEND DIES!\nYOU HAVE 6 FAIL ATTEMPTS\nCLICK ANYWHERE TO START\n"

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

finalCompare = "lorem"



win.getMouse()

while attempts < 6 and selectedWord != finalCompare:

    attempt_str = "You have {} attempts left".format(abs(attempts-6))

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
            if Search(user_Guess,selectedWord,i) == True:  
                    dash[i] = user_Guess
    else:
        attempts += 1
        drawHang(attempts,hangPost_ledge.getP2(),win)
    
    #guessWord.undraw()

   #guessWord = Text(centerCol, dash)
    #guessWord.setText(dash)
    #guessWord.draw(win)

    finalCompare= "".join(dash)


    userBox = Text(Point(300,150), dash)
    userBox.draw(win)


attempt_str = "You have {} attempts left".format(abs(attempts-6))

Title.setText(attempt_str)
textEntry.undraw()

gameOver_str = 'You lost the game!, your word was: {}'.format(selectedWord)

clickWord.setText(gameOver_str)
clickWord.draw(win)
win.getMouse()
win.close()

