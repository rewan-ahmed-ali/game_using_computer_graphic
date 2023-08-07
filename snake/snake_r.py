from turtle import *
import time
import random

delay = 0.09

#درجات
score = 0
high_score = 0

# screen
tu=Turtle()
    # screensize(600,600)
tu.screen.bgcolor("#e3f2fd")
tu.speed("fastest")
    # pensize(20)
tu.hideturtle()
setup(width=600, height=600)


#snake بداية 
head = Turtle()
head.speed(0)
head.shape("circle")
head.color("#23C6AE")
head.penup()
head.goto(0,0)
head.direct = "stop"
# head.hideturtle()

#snake food
food= Turtle()
food.speed(0)
food.shape("circle")
food.color("#6C7675")
food.penup()
food.goto(0,100)
# food.hideturtle()
segments = []

#scoreboards
sc = Turtle()
sc.speed(0)
sc.shape("circle")
sc.color("#016665")
sc.penup()
sc.hideturtle()
sc.goto(0,265)
sc.write("Score: 0  High score: 0", align = "center", font=("Courier", 18))

#Functions
def keyboardbindings():
    listen()
    onkeypress(go_up, "Up")
    onkeypress(go_down, "Down")
    onkeypress(go_left, "Left")
    onkeypress(go_right, "Right")

    listen()
    onkeypress(go_up, "w")
    onkeypress(go_down, "s")
    onkeypress(go_left, "a")
    onkeypress(go_right, "d")

def go_up():
    if head.direct != "down":
        head.direct = "up"
def go_down():
    if head.direct != "up":
        head.direct = "down"
def go_left():
    if head.direct != "right":
        head.direct = "left"
def go_right():
    if head.direct != "left":
        head.direct = "right"
def move():
    if head.direct == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direct == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direct == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direct == "right":
        x = head.xcor()
        head.setx(x+20)

keyboardbindings()

while True:
    update()
    #check 
    if head.xcor()>270 or head.xcor()<-270 or head.ycor()>250 or head.ycor()<-270:
        time.sleep(1)
        head.goto(0,0)
        head.direct = "stop"

        for segment in segments:
            segment.goto(700,700) #خارج range
    
        segments.clear()

        score = 0

        delay = 0.09

        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center", font=("Courier", 18))

    if head.distance(food) <20:
        #الاكل يتحرك في منطقه محدده دي 
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        food.goto(x,y)

        # زود ع دايره دائره
        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("#23C6AE")
        # new_segment.hideturtle()
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        #increase the score
        score += 5

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("Courier", 18)) 

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            # head.hideturtle()
            head.goto(0,0)
            head.direct = "stop"

            #hide segments
            for segment in segments:
                segment.goto(700,700)
            segments.clear()
            score = 0
            delay = 0.1

            #update the score     
            sc.clear()
            sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("Courier", 18))
    time.sleep(delay)
    
done()   