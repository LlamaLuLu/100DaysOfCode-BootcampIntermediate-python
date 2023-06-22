# 21/6/2022

import turtle as t
import pandas
from state_name import State
import time

# idea: add timer/ stopwatch
# idea: make African countries ver.
# idea: make plants/animals quiz ver.

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"  # file directory
screen.addshape(image)
t.shape(image)
screen.setup(width=725, height=491)  # change screensize to only fit image
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

answer_state = screen.textinput(title="Guess the State", prompt="What's a state's name? ")
correct = []

game_on = True
while game_on:  # use loop to allow user keep guessing
    # check if answer exists
    if len(correct) == 50:  # when all states full -> WIN
        game_on = False
        win = t.Turtle()
        win.hideturtle()
        win.write("WELL DONE! You knew all the states!")
        screen.update()
    elif answer_state.title() == "Exit":
        game_on = False
        # shows states to learn
        for state in correct:
            all_states.remove(state)
        data = pandas.DataFrame(all_states)
        data.to_csv("states_to_learn.csv")
    else:
        if answer_state.title() in all_states:
            if answer_state.title() in correct:  # duplicate answer
                answer_state = screen.textinput(title=f"{len(correct)}/50 States Correct",
                                                prompt="You've already guessed that.\nWhat's another state's name? ")
                continue
            correct.append(answer_state.title())  # record correct guesses in list
            state_name = State(correct[-1])  # show state name when answer == state name

            screen.update()
            time.sleep(1)  # move text box out of the way
            # keep track of no. of states correct (score) / 50 (in title)
            answer_state = screen.textinput(title=f"{len(correct)}/50 States Correct",
                                            prompt="That's correct!\nWhat's another state's name? ")
        else:
            answer_state = screen.textinput(title=f"{len(correct)}/50 States Correct",
                                            prompt="That's incorrect...\nWhat's another state's name? ")
