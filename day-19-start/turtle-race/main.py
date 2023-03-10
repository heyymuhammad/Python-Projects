from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet.", prompt="Which turtle will win the race? Choose a color.")
colors = ["red", "purple", "orange", "green", "yellow", "blue"]
y_positions = [-100, -70, -40, -10, 20, 50]
is_race_on = False
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on =True    


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winning color.")
                screen.textinput(title="Exit", prompt=f"You've won! The {winning_color} turtle is the winning color.\nPress any key to exit.")
                turtle.bye()
            else:
                print(f"You've lost! The {winning_color} turtle is the winning color.")
                screen.textinput(title="Exit", prompt=f"You've lost! The {winning_color} turtle is the winning color.\nPress any key to exit.")
                turtle.bye()
        spaces = random.randint(1,10)
        turtle.forward(spaces)

screen.exitonclick()