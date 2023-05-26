from turtle import Turtle

class Wall(Turtle):
  def __init__(self):
    super().__init__()
    self.color("purple")
    self.hideturtle()
    self.penup()
    self.goto(400,-300)
    self.hideturtle()
    self.pendown()
    self.pensize(5)
    self.setheading(90)
    self.forward(600)
    self.setheading(180)
    self.forward(800)
    self.setheading(270)
    self.forward(600)
    self.setheading(0)
    
    self.forward(800)
    jim = Turtle()
    jim.pensize(5)
    jim.hideturtle()
    jim.color("white")
    jim.penup()
    jim.goto(0,-300)
    
    for i in range(15):
      jim.setheading(90)
      jim.pendown()
      jim.forward(20)
      jim.penup()
      jim.forward(20)