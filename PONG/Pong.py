import turtle

wn = turtle.Screen()
wn.title("PONG!!!")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
# PADDLE
paddle_1 = turtle.Turtle()
paddle_1.speed(11)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.penup()
paddle_1.goto(-350, 0)
paddle_1.shapesize(stretch_wid=5, stretch_len=1)

paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.penup()
paddle_2.goto(350, 0)
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.dx = 0.40
ball.dy = 0.40
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0 Player B : 0", align="center", font=("Courier", 24, "normal"))
#scre
scorea = 0
scoreb = 0
# function
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)
    print("Moving up")


def paddle_1_dw():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)
    print("Moving down1")


def paddle_2_up():
    y = paddle_2.ycor()
    y = y + 20
    paddle_2.sety(y)
    print("Moving up2")


def paddle_2_dw():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)
    print("Moving down2")


# keyboardbinding
wn.listen()
wn.onkey(paddle_1_up, "Up")
wn.onkey(paddle_1_dw, "Down")
wn.onkey(paddle_2_up, "w")
wn.onkey(paddle_2_dw, "s")

# MAIN
while True:
    wn.update()
    #BALL MOVEMENT
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #BORDER
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx*=-1
        pen.clear()
        scorea+=1
        pen.write("Player A : {} Player B : {}".format (scorea, scoreb), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        scoreb+=1
        pen.write("Player A : {} Player B : {}".format (scorea, scoreb), align="center", font=("Courier", 24, "normal"))

    #paddle and ball ccoll
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
        print("collide2")
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
        print("Collide1")
        ball.setx(-340)
        ball.dx *= -1