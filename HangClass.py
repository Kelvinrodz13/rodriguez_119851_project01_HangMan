
class Hman:
    def __init__(self, aWord, userAtt=6):
        self.word = aWord
        self.userAtt = userAtt

    def setWord(self, Aword):
        self.word = Aword

    def getWord(self):
        return self.word

    def getUserAtt(self):
        return self.userAtt

    def setUserAtt(self, aTT):
        if (aTT > 0):
	    self.userAtt = aTT
	else:
		self.userAtt = 8

    def Search(self, word='', selected_Word='', i=0):
        if word[0] == selected_Word[i]:
            return True
        else:
            return False

    def decreaseAtt(self):
        self.userAtt -= 1

    # function to create the hanged man
    def drawHang(self, att=0, ledge=Point(0, 0), win=GraphWin):
        import graphics
        ledge.move(0, -10)
        head = graphics.Circle(ledge, 10)

        torso_p1 = head.getCenter()
        torso_p1.move(0, -10)

        torso_p2 = graphics.Point(torso_p1.getX(), 300)
        #torso_p2.move()

        torso = graphics.Line(torso_p1, torso_p2)

        left_p1 = torso.getCenter()
        left_p1.move(0, 20)
        left_p2 = left_p1.clone()
        left_p2.move(-30, -30)
        left_arm = graphics.Line(left_p1, left_p2)

        right_p1 = left_arm.getP1()
        right_p2 = left_arm.getP2()

        right_p2.move(60, 0)

        right_arm = graphics.Line(right_p1, right_p2)

        centerLeg = torso.getP2()
        left_leg = torso.getP2()

        left_leg.move(-30, -30)
        right_leg = left_leg.clone()
        right_leg.move(60, 0)

        LegLineL = graphics.Line(centerLeg, left_leg)
        LegLineR = graphics.Line(centerLeg, right_leg)

        if att == 6:
            head.setFill('black')
            head.draw(win)
        elif att == 5:
            torso.draw(win)
        elif att == 4:
            left_arm.draw(win)
        elif att == 3:
            right_arm.draw(win)
        elif att == 2:
            LegLineL.draw(win)
        elif att == 1:
            LegLineR.draw(win)
