# Vaishnavi_111
# Ping Pong Ball Game in Python
# The game is endless, ends only when the paticipant gives up

import turtle
import winsound # Sound functionality will work only on windows


# Creating the game window
window = turtle.Screen()
window.title("Ping Pong Ball")
window.bgcolor("#a0ecd1")
window.setup(width=800, height=800)
window.tracer(0)


# Creating borders for the main game window
border = turtle.Turtle()
border.penup()
border.goto(-400,300)
border.pendown()
border.goto(+400,300)
border.goto(+400,-300)
border.goto(-400,-300)
border.goto(-400,300)
border.hideturtle()


# Creating the Scoreboard
score_one=0
score_two=0


# Paddle A
paddle_one = turtle.Turtle()
paddle_one.speed(0)    #setting up the animation speed to max
paddle_one.shape("square")    #creates 20*20 pixel square
paddle_one.color("black")
paddle_one.shapesize(stretch_wid=6, stretch_len=2)
paddle_one.penup()  #makes sure that the moving object does not draw anything on the window
paddle_one.goto(-380,0)  #start off at (left, mid)


# Paddle B
paddle_two = turtle.Turtle()
paddle_two.speed(0)    #setting up the animation speed to max
paddle_two.shape("square")    #creates 20*20 pixel square
paddle_two.color("black")
paddle_two.shapesize(stretch_wid=6, stretch_len=2)
paddle_two.penup()  #makes sure that the moving object does not draw anything on the window
paddle_two.goto(+380,0)  #start off at (left, mid)


# Ball
ball = turtle.Turtle()
ball.speed(0)    
ball.shape("circle")    
ball.color("red")
ball.penup()  
ball.goto(0,0)
ball.dx = -0.35
ball.dy = 0.35


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Player One: 0 \t \t \t Player Two: 0", align="center", font=("Arial", 24, "bold"))


# Functions to move the paddles
def paddle_one_up():
     y = paddle_one.ycor()         
     y += 20
     if y <= 240:
          paddle_one.sety(y)

def paddle_one_down():
     y = paddle_one.ycor()         
     y -= 20
     if y >= -240:
          paddle_one.sety(y)

def paddle_two_up():
     y = paddle_two.ycor()         
     y += 20
     if y <= 240:
          paddle_two.sety(y)

def paddle_two_down():
     y = paddle_two.ycor()         
     y -= 20
     if y >= -240:
          paddle_two.sety(y)



# Getting instructions using keyboard 
window.listen()

window.onkeypress(paddle_one_up, "Up")
window.onkeypress(paddle_one_down, "Down")


# Main Game Loop
while True:
     window.update()

     # Moving the Ball
     ball.setx(ball.xcor() + ball.dx)
     ball.sety(ball.ycor() + ball.dy)

     # Checking for Edges
     if ball.ycor() > 290:
          ball.sety(290)
          ball.dy *= -1
          winsound.PlaySound("edge.wav", winsound.SND_ASYNC)

     if ball.ycor() < -290:
          ball.sety(-290)
          ball.dy *= -1
          winsound.PlaySound("edge.wav", winsound.SND_ASYNC)

     if ball.xcor() > 390:
          ball.setx(390)
          ball.dx *= -1
          winsound.PlaySound("score.wav", winsound.SND_ASYNC)
          score_one += 1
          pen.clear()
          pen.write("Player One: {} \t \t \t Player Two: {}".format(score_one, score_two), align="center", font=("Arial", 24, "bold"))

     if ball.xcor() < -390:
          ball.setx(-390)
          ball.dx *= -1
          winsound.PlaySound("score.wav", winsound.SND_ASYNC)
          score_two += 1
          pen.clear()
          pen.write("Player One: {} \t \t \t Player Two: {}".format(score_one, score_two), align="center", font=("Arial", 24, "bold"))


     # Paddle and Ball Collision
     if ball.xcor() > 350 and ball.xcor() < 360 and (ball.ycor() < paddle_two.ycor() + 60) and (ball.ycor() > paddle_two.ycor() - 60):
          ball.setx(350)
          ball.dx *= -1
          winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)
     if ball.xcor() < -350 and ball.xcor() > -360 and (ball.ycor() < paddle_one.ycor() + 60) and (ball.ycor() > paddle_one.ycor() - 60):
          ball.setx(-350)
          ball.dx *= -1
          winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

     # AI Player
     if paddle_two.ycor() < ball.ycor() and abs(paddle_two.ycor() - ball.ycor()) > 20:
          paddle_two_up()

     elif paddle_two.ycor() > ball.ycor() and abs(paddle_two.ycor() - ball.ycor()) > 20:
          paddle_two_down()