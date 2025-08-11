from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from design import Design
import time

ALIGN="center"
FONT=("OCR A Extended",25,"normal")

screen=Screen()
screen.bgcolor("black")
screen.title("Pong Mania")
screen.setup(width=800,height=600)

game_over=Turtle()
game_over.hideturtle()
game_over.color("red")
screen.tracer(0)
design=Design()
ball=Ball()
scoreboard=Scoreboard()

rpaddle=Paddle((350,0),"pink")
lpaddle=Paddle((-350,0),"sky blue")
user_choice = int(screen.textinput("🏆 First to...",
                                   "How many points should it take to win?"))
screen.listen()
screen.onkeypress(fun=rpaddle.up,key="Up")
screen.onkeypress(fun=rpaddle.down,key="Down")
screen.onkeypress(fun=lpaddle.up,key="w")
screen.onkeypress(fun=lpaddle.down,key="s")

game_on=True

while game_on:
    time.sleep(ball.speeding_ball)
    screen.update()
    ball.move()
    # corner detection
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.switch_y()

    elif (ball.distance(rpaddle)<50 or ball.distance(lpaddle)<50) and (ball.xcor()>260 or ball.xcor()<-260):
        ball.switch_x()
    # for right
    elif ball.xcor()>400 :
        ball.reset_position()
        ball.switch_x()
        scoreboard.increase_p1()

    # for left
    elif ball.xcor()<-400:
        ball.reset_position()
        ball.switch_x()
        scoreboard.increase_p2()

    if scoreboard.score1>=user_choice or scoreboard.score2>=user_choice:
        if scoreboard.score1==scoreboard.score2:
            result=" 🤝🤝DRAW🤝🤝"
        elif scoreboard.score1>scoreboard.score2:
            result="🏆PLAYER-1 WON!!!🏆"
        else:
            result="🏆PLAYER-2 WON!!!🏆"
        game_over.write(arg=f"""{result}\n☠GAME OVER☠""",align=ALIGN,font=FONT)
        game_on=False

screen.exitonclick()