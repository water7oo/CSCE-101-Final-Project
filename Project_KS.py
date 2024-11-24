# Kody Scott
# Section-004
# 11/1/2024
# kodys@email.sc.edu
# FINAL PROJECT: AIM LABS

#Pseudo Code

# Aim training game, click the turtle with your mouse,
# turtle moves to a random spot within the screens range, track the time
# it takes the person to click each turtle
# A game timer will tick down (30 secs? 60 secs?)
# Final score will be calculated (Average time per click, total turtles killed)

# Average time per click: timer will run, when player clicks turtle, timer will reset to 0 (log and append all times in a list, then find average time taken)
# Each turtle is 100 points, (maybe inforporate a golden turtle??? = 300 points?)
# Could have a situation where more than 1 turtle spawns????

## Tasks ##

# Make turtle spawn in random spot
# Allow player to click turtle, then turtle goes to a random spot on the screen
# Have timer go up from 0 (time.delta time???, Time resets when turtle is clicked, have boolean triggers when turtle is clicked)
# compile the last time documented before reset happens, then throw it into a list (append it)
# Have score counter
# When game is finished tally points and give a final score
# give the player the option to play again, this resets the game timer to 60 or 30 and runs the while loop again


import turtle
import random

score = 0
screen = turtle.Screen()
screen.title("Aim Labs")
screen.bgcolor()

isTargetHit = False

target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.speed(0)
msTime = 250
target.shapesize(3)

timerDisplay = turtle.Turtle()
timerDisplay.hideturtle()
timerDisplay.penup()
timerDisplay.goto(0,200)
timerDisplay.write("Time: 0", align="center", font=("Arial", 24, "normal"))

hitTimer = 0
timeElapsed = 0

print(isTargetHit)
def targetHit(x,y):
    global score
    score += 1
    print(score)
    isTargetHit = True
    print(f"Turtle clicked at {x},{y}, {isTargetHit}")
    screen.ontimer(target.color("gray"),msTime)
    target.goto(random.randint(-200,200),random.randint(-200,200))
    
    isTargetHit = False
    print(isTargetHit)
    target.color("red")


def updateHitTimer():
    global timeElapsed, isTargetHit

    if isTargetHit:
        timeElapsed = 0
        isTargetHit = False  
    else:
        timeElapsed += 0.1


 
    timerDisplay.clear()
    timerDisplay.write(f"Time: {round(timeElapsed, 1)}", align="center", font=("Arial", 24, "normal"))

    screen.ontimer(updateHitTimer, 10)

  
    
    
updateHitTimer()
target.onclick(targetHit)


