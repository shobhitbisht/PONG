from turtle import Turtle

RIGHT = 280
LEFT = -280

class Paddle(Turtle):
  
  def __init__(self,pos):
    
    super().__init__()
    self.color("white")
    self.shape("square")
    self.shapesize(5,1)
    self.penup()
    self.goto(pos,0)
    
   

  def up(self):
    if self.ycor() < 240:
      new_y = self.ycor() + 20
      self.goto(self.xcor(),new_y)


  def down(self):
    if self.ycor() > -240:
      new_y = self.ycor() - 20
      self.goto(self.xcor(),new_y)
    

    
    
  