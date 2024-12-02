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



# .clear() method is used to clear the written information on screen, which causing the blinking


#Importing packages
import turtle
import random


#declaring screen and colors
screen = turtle.Screen()
screen.title("Aim Labs")
screen.bgcolor("white")

#score variables
score = 0
gameTime = 30

#boolean to determine if target is hit
isTargetHit = False

#determine how much time has elapsed
timeElapsed = 0
#stores that elapsed time in a list
storedTime = []

#turtle variables
target = turtle.Turtle()
target.shape("turtle")
target.color("red")
target.penup()
target.speed(0)
target.shapesize(3)

#displays an invisible timer that tracks time taken between clicks
timerDisplay = turtle.Turtle()
timerDisplay.hideturtle()
timerDisplay.penup()
timerDisplay.goto(0, 200)

#basically the games timer
countdownDisplay = turtle.Turtle()
countdownDisplay.hideturtle()
countdownDisplay.penup()
countdownDisplay.goto(-200, 200)

#writes the countdown on screen using the following parameters
countdownDisplay.write("Time Left: 30", align="left", font=("Arial", 24, "normal"))

#displays the actually score on screen
scoreDisplay = turtle.Turtle()
scoreDisplay.hideturtle()
scoreDisplay.penup()
scoreDisplay.goto(100, 200)
scoreDisplay.write("Score: 0", align="left", font=("Arial", 24, "normal"))


#main target function that fires when target is clicked
def targetHit(x, y):
    global score, isTargetHit

    #increments 100 points every click
    score += 100
    isTargetHit = True
    scoreDisplay.
    scoreDisplay.write(f"Score: {score}", align="left", font=("Arial", 24, "normal"))
    target.color("gray")

    #using the lambda function it can take in more than 1 arguement (target.color(),timer alotted) and 
    screen.ontimer(lambda: target.color("red"), 250)

    #makes target go to random spot on the screen
    target.goto(random.randint(-200, 200), random.randint(-200, 200))


#Main target function that fires when target is missed
def targetMiss(x, y):
    global score
    score -= 10
    score = max(score, 0)
    scoreDisplay.clear()
    scoreDisplay.write(f"Score: {score}", align="left", font=("Arial", 24, "normal"))


#updates the hit timer, every time the player clicks the target, the current
# time is appended to a list called storedTime, taking the sum to calculate the average
def updateHitTimer():
    global timeElapsed, isTargetHit
    if isTargetHit:
        storedTime.append(timeElapsed)
        timeElapsed = 0
        isTargetHit = False
    else:
        timeElapsed += 0.1
   
    screen.ontimer(updateHitTimer, 100)


#updates the game countdown
def updateCountdown():
    global gameTime
    if gameTime > 0:
        gameTime -= 1
        countdownDisplay.clear()
        countdownDisplay.write(f"Time: {gameTime}", align="left", font=("Arial", 24, "normal"))
        screen.ontimer(updateCountdown, 1000)
    else:
        target.hideturtle()
        countdownDisplay.clear()
        countdownDisplay.write("Time Left: 0", align="left", font=("Arial", 24, "normal"))
        print(f"Final Score: {score}")

        #the if statement within the f-string is using a
        #form of ternary operator/conditional to check if stored time isn't empty
        #if not empty calculate average reaction time
        print(f"Average Reaction Time: {sum(storedTime) / len(storedTime) if storedTime else 0:.2f}")


#methods below to fire when clicks occur, timer methods are also below
target.onclick(targetHit)
screen.onclick(targetMiss)
updateHitTimer()
updateCountdown()
screen.mainloop()






