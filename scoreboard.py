from turtle import Turtle


class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.color("Pink")
    self.hideturtle()
    self.penup()
    self.color("white")
    self.rscore = 0
    self.lscore = 0
    self.update_score()
  
  def update_score(self):
    self.clear()
    self.goto(-100, 200)
    self.write(f"{self.lscore}",
               align="center",
               font=('Arial', 60, 'normal'))
    self.goto(100, 200)
    self.write(f"{self.rscore}",
               align="center",
               font=('Arial', 60, 'normal'))
    

  
  def l_point(self):
    self.lscore += 1
    self.update_score()
  def r_point(self):
    self.rscore += 1
    self.update_score()

  def game_over(self,winner):
    
    self.goto(0, 0)
    self.write(f"Game Over",
               align="center",
               font=('Arial', 40, 'normal'))
    self.goto(0, -60)
    self.write(f"{winner} Player Wins!!",
               align="center",
               font=('Arial', 40, 'normal'))