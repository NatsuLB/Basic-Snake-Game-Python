from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
       
        with open("Score.txt") as data:
            self.high_score = int(data.read())
        
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.update_board()
       
    
    def update_board(self):
        self.clear()
        self.write(f"Score : {self.count} High Score : {self.high_score}",False,align="center", font=('Arial', 24, 'normal'))
    
    def reset(self):
        if self.count > self.high_score:
            self.high_score = self.count
            with open("/Score.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.count = 0
        self.update_board()

    
    def increase_score(self):
        self.count = self.count + 1
        self.update_board()
        