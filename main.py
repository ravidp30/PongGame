import time
from turtle import *
from tkinter import *

#setup
window=Screen()
window.title('Pong Game')
window.setup(width=800,height=600)
window.bgcolor('green')
window.addshape("ball.gif")
window.addshape("goal.gif")
window.addshape("football.gif")
window.tracer(0)
cnt=1#speed change
p1_keeper=10 #keeper player 1 change width
p2_keeper=10 #keeper player 2 change width


#BackGround
football=Turtle()
football.shape('football.gif')

#pause
Opt=Turtle()
Opt.hideturtle()
Opt.penup()
Opt.goto(-340,270)
Opt.color('Black')
Opt.write("'p' to pause the game", font=('Ariel', 15, 'bold'))

#Score
Score_p1=0
Score_p2=0
Score=Turtle()
Score.penup()
Score.hideturtle()
Score.goto(0,255)
Score.color('White')
Score.write("Score: 0 - 0" ,font=('Ariel',25,'bold'),align='center')

#Goooooooal
Goal=Turtle()
Goal.hideturtle()
Goal.shape('goal.gif')

#GameOver
gameover=Turtle()
gameover.hideturtle()
gameover.goto(0,0)
gameover.color('Black')

#Ball
ball= Turtle()
ball.shape('ball.gif')
ball.penup()
ball.goto(0,0)
x_ball=cnt# choose speed
y_ball=cnt # choose speed

#Pause
pause= Turtle()
pause.hideturtle()
pause.goto(0,0)
pause.color('Black')


#Player 1
player1=Turtle()
player1.penup()
player1.shape('square')
player1.color('black')
player1.goto(350,0)
player1.shapesize(stretch_wid=p1_keeper,stretch_len=1)

#Player 2
player2=Turtle()
player2.penup()
player2.shape('square')
player2.color('black')
player2.goto(-350,0)
player2.shapesize(stretch_wid=p2_keeper,stretch_len=1)



#Player1 movement
def P1_go_up():
    y=player1.ycor()
    y+=50
    player1.sety(y)

def P1_go_down():
    y = player1.ycor()
    y -= 50
    player1.sety(y)

#Player2 movement
def P2_go_up():
    y = player2.ycor()
    y += 50
    player2.sety(y)
def P2_go_down():
    y = player2.ycor()
    y -= 50
    player2.sety(y)

def pause():
      time.sleep(3)




window.listen() # get arrows from keyboard
window.onkeypress(P1_go_up,'Up')
window.onkeypress(P1_go_down,'Down')
window.onkeypress(P2_go_up,'w')
window.onkeypress(P2_go_down,'s')
window.onkeypress(pause,'p')



while True:
    window.update()

    #Game Over
    if Score_p1 ==3 or Score_p2 ==3:
        gameover.write("game over"  ,font=('Ariel', 50, 'bold'), align='center')
        time.sleep(2)
        quit()

    #ball momvement
    ball.setx(ball.xcor()+x_ball)
    ball.sety(ball.ycor()+y_ball)

    #ball borders
    if ball.ycor()>240:
        ball.sety(240)
        y_ball*=-1
    elif ball.ycor() < -240:
        ball.sety(-240)
        y_ball *= -1
    if ball.xcor() < -340:
        ball.setx(-340)
        x_ball *= -1
    elif ball.xcor() > 340:
        ball.setx(340)
        x_ball *= -1

    #Attacks :

    #Player1 attack
    if ball.xcor() < -339:    #The ball in left side (danger zone)
         if  (player2.ycor() -(p2_keeper*10)) < ball.ycor() < (player2.ycor() + (p2_keeper*10)):
               x_ball *= -1
         else :  #Gooooooalllll
               p1_keeper -= 1   #make the keeper smaller
               player1.shapesize(stretch_wid=p1_keeper, stretch_len=1)
               ball.goto(0,0)
               Score_p1+=1
               Score.clear()
               Score.write(f'Score:{Score_p2} - {Score_p1}', font=('Ariel', 25, 'bold'), align='center')
               time.sleep(3)

    #Player2 Attack
    if ball.xcor()> 339 : #The ball in right side (danger zone)
        if (player1.ycor() - (p1_keeper*10) < ball.ycor() < (player1.ycor() + (p1_keeper*10))):
            x_ball *= -1
        else:  # Gooooooalll
            p2_keeper -= 1 # make the keeper smaller
            player2.shapesize(stretch_wid=p2_keeper, stretch_len=1)
            ball.goto(0, 0)
            Score_p2 += 1
            Score.clear()
            Score.write(f'Score:{Score_p2} - {Score_p1}', font=('Ariel', 25, 'bold'), align='center')
            time.sleep(3)



    #players borders (dynamic changing while score go up)
    if player1.ycor()>150 + (Score_p1*10):
        player1.sety(150 + (Score_p1*10))
    elif player1.ycor() < -150 - (Score_p1*10):
        player1.sety(-150 - (Score_p1*10))
    if player2.ycor()>150 + (Score_p2*10):
        player2.sety(150+ (Score_p2*10))
    elif player2.ycor() < -150 - (Score_p2*10):
        player2.sety(-150 - (Score_p2*10))

