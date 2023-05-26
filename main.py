from turtle import Screen
from wall import Wall
from padel import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

wall = Wall()
rpaddle = Paddle(370)
lpaddle = Paddle(-370)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(rpaddle.up, "Up")
screen.onkey(rpaddle.down, "Down")
screen.onkey(lpaddle.up, "w")
screen.onkey(lpaddle.down, "s")

game_is_on = True

while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  #Detech the collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  #Detech the collison with paddel
  if ball.distance(rpaddle) < 50 and ball.xcor() > 340 or ball.distance(lpaddle) < 50 and ball.xcor() < -350:
    
    
    ball.bounce_x()
   
    

  #Detech if the rpaddel miss the ball
  if ball.xcor() > 380:
    scoreboard.l_point()
    ball.reset_pos()
    ball.bounce_x()
    
    
    
  #Detech if the rpaddel miss the ball 
  elif ball.xcor() < -380:
    scoreboard.r_point()
    ball.reset_pos()
    ball.bounce_x()
  


  if scoreboard.lscore == 5:
    scoreboard.game_over("Left")
    game_is_on = False

  elif scoreboard.rscore == 5:
    scoreboard.game_over("Right")
    game_is_on = False
   
    