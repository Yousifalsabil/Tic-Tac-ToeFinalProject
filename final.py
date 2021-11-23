from turtle import Turtle, Screen 
from random import choice

BoxSize = 280
FONT_SIZE = 80
FONT = ('Arial', FONT_SIZE, 'bold')
LineThickness = 23
GameSize = 3
FunNumbers=Turtle()
class TicTacToe1:
    number = 1
    for x in range(3):
              for y in range(3):
                  FunNumbers.penup()
                  FunNumbers.goto(-250 + y  * 250, 300 - x  * 300) 
                  FunNumbers.pendown()

                  FunNumbers.write(number, font = ( "Arial", 20))
                  number+=1



    wins = [
        [True, True, True, False, False, False, False, False, False],
        [False, False, False, True, True, True, False, False, False],
        [False, False, False, False, False, False, True, True, True],
        [True, False, False, True, False, False, True, False, False],
        [False, True, False, False, True, False, False, True, False],
        [False, False, True, False, False, True, False, False, True],
        [True, False, False, False, True, False, False, False, True],
        [False, False, True, False, True, False, True, False, False]
    ]

    def __init__(self):
        self.board = [Turtle('square', visible=False) for _ in range(GameSize * GameSize)]
        self.background = Turtle('square', visible=False)

    def drawBoard(self):
        screen.tracer(False)

        self.background.shapesize(BoxSize * GameSize / LineThickness)
        self.background.color('blue')
        self.background.stamp()

        for j in range(GameSize):
            for i in range(GameSize):
                square = self.board[i + j * GameSize]
                square.shapesize(BoxSize / LineThickness)
                square.color('white')
                square.penup()
                square.goto((i - 1) * (BoxSize + 2), (j - 1) * (BoxSize + 2))
                square.state = None
                square.onclick(lambda x, y, s=square: self.mouse(s))
                square.showturtle()
                square.stamp()  # blank out background behind turtle (for later)
        screen.tracer(True)

    def select(self, square, turn):
        square.onclick(None)  # disable further moves to this square
        square.state = turn
        # replace square/turtle with (written) X or O
        square.hideturtle()
        square.color('red')
        square.sety(square.ycor() - FONT_SIZE / 2)
        square.write(turn, align='center', font=FONT)

        return self.is_winner(turn)

    def is_winner(self, turn):
        for win in self.wins:
            for index, flag in enumerate(win):
                if flag and self.board[index].state != turn:
                    break

            else:  # no break
                self.deactivate()
                a=screen.textinput("This Game Is Over", turn + " Wins. write Q if you want to Quit")
                if a == 'Q':
                    quit()


                return True
        return False

    def deactivate(self):
        for square in self.board:
            if square.state is None:
                square.onclick(None)

    def mouse(self, square):

        if self.select(square, 'X'):
            return

        choices = [square for square in self.board if square.state is None]

        if not choices:
            self.deactivate()
            return

        if self.select(choice(choices), 'O'):
            return

screen = Screen()

game = TicTacToe1()
game.drawBoard()
screen.mainloop()
