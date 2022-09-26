import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
#convert to list with all states
all_states = data.state.to_list()
guessed_states = []

#uses guessed_states to track guesses. Only continue until guessed_states len is < 50
while len(guessed_states) < 50:
    #.title() is used to capitalize first letter of the answer
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    print(answer_state)

    #Break statement. Returns states missing from your guesses
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    #if answer_state is 1 of the states in all of the 50_states.csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        #used to get x,y coor for current state (answer_state)
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        #if correct:
            #Create turtle to write the name of the state at the state's x,y coordinates

