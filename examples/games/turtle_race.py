from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
#set screen size using keyword arguments
screen.setup(width=500, height=400)
#open a screen for user to select winner
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
#create empty all_turtles list to be appended to later on
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    #setup turtle on left side of screen
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    #append new turtle to all_turtles list
    all_turtles.append(new_turtle)

#Once initial bet is placed, change is_race_on to True
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        #if turtles x coordinate is > 230, it has finished the race
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()


