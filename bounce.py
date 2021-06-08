import turtle

wn=turtle.Screen()
wn.bgcolor("Blue")
wn.title("Bouncing ball")

ball=turtle.Turtle()
ball.shape("circle")
ball.color("Orange")
ball.penup()
ball.speed(0)
ball.goto(0,200)

gravity= 0.1
ball.dy = -2
while True:
    ball.dy -=gravity
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() < -300:
        ball.dy *= -1
