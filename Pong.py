import turtle
import os
from time import sleep
import sys
import datetime

Easy_Mediom_Hard = input("Easy Medium or hard: ")

# Game Window #
wn = turtle.Screen()
wn.title("Pong by @mickyslats")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()

# Socre
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


ball = turtle.Turtle()
ball.speed()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 8
ball.dy = -8


# Score Boared & How TO Play#
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("For Player A it's W to move up and S to move down", align="center", font=("Courier", 16, "normal"))
sleep(5)
pen.clear()
pen.write("For Player B it's Up Key to move Up and Down key to move down", align="center", font=("Courier", 16, "normal"))
sleep(5)
pen.clear()
pen.write("Game Starts in 5 Seconds")
pen.clear()
pen.write("5",align="center", font=("Courier", 25, "normal"))
sleep(1)
pen.clear()
pen.write("4",align="center", font=("Courier", 25, "normal"))
sleep(1)
pen.clear()
pen.write("3",align="center", font=("Courier", 25, "normal"))
sleep(1)
pen.clear()
pen.write("2",align="center", font=("Courier", 25, "normal"))
sleep(1)
pen.clear()
pen.write("1",align="center", font=("Courier", 25, "normal"))
sleep(1)
pen.clear()
pen.write("Go !",align="center", font=("Courier", 25, "normal"))
sleep(1)
pen.clear()
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 20, "normal"))



# Functions and Logic #
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboared Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game loop
time = datetime.datetime.now()
time_played = time.strftime("%c")
last_playee_book = open('History_Played.txt', "w")
last_playee_book.write(f'It Was last played {time_played}')
last_playee_book.close()

while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("aplay bounce.wav")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("aplay bounce.wav")

    if score_a == 5:
        pen.clear()
        pen.write("Player A Well Done You Win", align="center", font=("Courier", 24, "normal"))
        sleep(5)
        pen.clear()
        pen.write("Hope You Enjoyed The Game",  align="center", font=("Courier", 24, "normal"))
        sleep(5)
        pen.clear()
        pen.write("mickyslats", align="center", font=("Courier", 24, "normal"))
        sleep(5)
        sys.exit()

    if score_b == 5:
        pen.clear()
        pen.write("Player B Well Done You Win", align="center", font=("Courier", 24, "normal"))
        sleep(5)
        pen.clear()
        pen.write("Hope You Enjoyed The Game",  align="center", font=("Courier", 24, "normal"))
        sleep(5)
        pen.clear()
        pen.write("mickyslats", align="center", font=("Courier", 24, "normal"))
        sleep(5)
        sys.exit()

    # Paddle and ball Collissions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        os.system("aplay bounce.wav")

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("aplay bounce.wav")
